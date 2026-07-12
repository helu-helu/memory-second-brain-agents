"""Incrementally embed a large document tree and bulk-upload it to Qdrant."""

import argparse
import hashlib
import json
import os
import sqlite3
import sys
import time
import uuid
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from agent_core.config import COLLECTION_NAME, ROOT_DIR, config

VALID_EXTS = {".md", ".txt", ".json"}
BATCH_SIZE = 128


def get_all_valid_files(target_dir):
    root = Path(target_dir)
    if not root.exists():
        print(f"Directory not found: {root}")
        return []
    return sorted(str(path) for path in root.rglob("*") if path.suffix.lower() in VALID_EXTS)


def file_digest(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


class Manifest:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute(
            """CREATE TABLE IF NOT EXISTS indexed_files (
                collection TEXT NOT NULL,
                path TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                point_ids TEXT NOT NULL,
                indexed_at REAL NOT NULL,
                PRIMARY KEY (collection, path)
            )"""
        )

    def get(self, collection, path):
        row = self.db.execute(
            "SELECT content_hash, point_ids FROM indexed_files WHERE collection=? AND path=?",
            (collection, path),
        ).fetchone()
        return (row[0], json.loads(row[1])) if row else None

    def put(self, collection, path, content_hash, point_ids):
        self.db.execute(
            """INSERT INTO indexed_files VALUES (?, ?, ?, ?, ?)
               ON CONFLICT(collection, path) DO UPDATE SET
               content_hash=excluded.content_hash,
               point_ids=excluded.point_ids,
               indexed_at=excluded.indexed_at""",
            (collection, path, content_hash, json.dumps(point_ids), time.time()),
        )
        self.db.commit()

    def entries(self, collection):
        rows = self.db.execute(
            "SELECT path, point_ids FROM indexed_files WHERE collection=?", (collection,)
        ).fetchall()
        return [(path, json.loads(point_ids)) for path, point_ids in rows]

    def remove(self, collection, path):
        self.db.execute(
            "DELETE FROM indexed_files WHERE collection=? AND path=?", (collection, path)
        )
        self.db.commit()

    def close(self):
        self.db.close()


def make_client():
    from qdrant_client import QdrantClient

    qdrant = config["rag"]
    mode = qdrant.get("mode", "local")
    if mode == "server":
        return QdrantClient(
            host=qdrant.get("host", "127.0.0.1"),
            port=qdrant.get("port", 6333),
            prefer_grpc=qdrant.get("prefer_grpc", True),
        )
    if mode == "local":
        return QdrantClient(path=os.path.join(ROOT_DIR, qdrant["db_path"].replace("./", "")))
    raise ValueError(f"Unsupported Qdrant mode: {mode}")


def ensure_collection(client, collection, vector_size, recreate=False):
    from qdrant_client.models import Distance, VectorParams

    if recreate and client.collection_exists(collection):
        client.delete_collection(collection)
    if not client.collection_exists(collection):
        client.create_collection(
            collection_name=collection,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE),
        )


def chunk_file(path, splitter, root, content_hash):
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    relative = Path(path).resolve().relative_to(root).as_posix()
    tags = list(Path(relative).parts[:-1])
    records = []
    for index, chunk in enumerate(splitter.split_text(text)):
        if not chunk.strip():
            continue
        point_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"{relative}:{content_hash}:{index}"))
        records.append(
            {
                "id": point_id,
                "text": chunk,
                "payload": {
                    "file_path": relative,
                    "file_name": Path(path).name,
                    "tags": tags,
                    "content_hash": content_hash,
                    "chunk_index": index,
                },
            }
        )
    return relative, records


def process_batch(files, root, collection, manifest, model, splitter, client, args):
    from qdrant_client.models import PointIdsList, PointStruct

    changed = []
    skipped = 0
    for path in files:
        digest = file_digest(path)
        relative = Path(path).resolve().relative_to(root).as_posix()
        previous = manifest.get(collection, relative)
        if previous and previous[0] == digest:
            skipped += 1
            continue
        relative, records = chunk_file(path, splitter, root, digest)
        changed.append((relative, digest, previous[1] if previous else [], records))

    if not changed:
        return 0, skipped, 0

    records = [record for _, _, _, file_records in changed for record in file_records]
    if records:
        vectors = model.encode(
            [record["text"] for record in records],
            batch_size=args.embedding_batch,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        points = [
            PointStruct(id=record["id"], vector=vector.tolist(), payload={**record["payload"], "text": record["text"]})
            for record, vector in zip(records, vectors)
        ]
        client.upload_points(
            collection_name=collection,
            points=points,
            batch_size=args.upload_batch,
            parallel=args.parallel,
            max_retries=3,
            wait=True,
        )

    for relative, digest, old_ids, file_records in changed:
        new_ids = [record["id"] for record in file_records]
        stale_ids = list(set(old_ids) - set(new_ids))
        if stale_ids:
            client.delete(
                collection_name=collection,
                points_selector=PointIdsList(points=stale_ids),
                wait=True,
            )
        manifest.put(collection, relative, digest, new_ids)
    return len(changed), skipped, len(records)


def prune_deleted(manifest, client, collection, current_paths):
    from qdrant_client.models import PointIdsList

    removed = 0
    for path, point_ids in manifest.entries(collection):
        if path in current_paths:
            continue
        if point_ids:
            client.delete(
                collection_name=collection,
                points_selector=PointIdsList(points=point_ids),
                wait=True,
            )
        manifest.remove(collection, path)
        removed += 1
    return removed


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target_dir")
    parser.add_argument("--collection", default=COLLECTION_NAME)
    parser.add_argument("--manifest", default=str(project_root / "db" / "ingestion_manifest.sqlite"))
    parser.add_argument("--file-batch", type=int, default=BATCH_SIZE)
    parser.add_argument("--embedding-batch", type=int, default=64)
    parser.add_argument("--upload-batch", type=int, default=128)
    parser.add_argument("--parallel", type=int, default=1)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--recreate", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    if os.name == "nt" and args.parallel > 1:
        print("Windows: forcing --parallel 1 to avoid orphaned multiprocessing workers.", flush=True)
        args.parallel = 1
    root = Path(args.target_dir).resolve()
    files = get_all_valid_files(root)
    if args.limit:
        files = files[: args.limit]
    if not files:
        print("No valid documents found.")
        return
    print(f"Corpus: {len(files):,} files in {root}", flush=True)
    if args.dry_run:
        print("Dry run complete; Qdrant and embedding model were not touched.", flush=True)
        return

    from llama_index.core.node_parser import SentenceSplitter
    from sentence_transformers import SentenceTransformer

    device = "cuda" if __import__("torch").cuda.is_available() else "cpu"
    model_name = config["rag"]["embedding_model"]
    print(f"Embedding: {model_name} on {device}", flush=True)
    model = SentenceTransformer(model_name, device=device)
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=64)
    client = make_client()
    ensure_collection(client, args.collection, model.get_embedding_dimension(), args.recreate)
    manifest = Manifest(args.manifest)

    started = time.time()
    indexed = skipped = chunks = 0
    try:
        for offset in range(0, len(files), args.file_batch):
            batch = files[offset : offset + args.file_batch]
            done, unchanged, batch_chunks = process_batch(
                batch, root, args.collection, manifest, model, splitter, client, args
            )
            indexed += done
            skipped += unchanged
            chunks += batch_chunks
            print(
                f"Files {min(offset + len(batch), len(files)):,}/{len(files):,} | "
                f"indexed={indexed:,} skipped={skipped:,} chunks={chunks:,}",
                flush=True,
            )
        if not args.limit:
            current_paths = {
                Path(path).resolve().relative_to(root).as_posix() for path in files
            }
            removed = prune_deleted(manifest, client, args.collection, current_paths)
            if removed:
                print(f"Removed {removed:,} deleted files from Qdrant.", flush=True)
    finally:
        manifest.close()
        client.close()
    print(f"Complete in {time.time() - started:.1f}s", flush=True)


if __name__ == "__main__":
    main()
