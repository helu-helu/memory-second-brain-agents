"""Validate a local official-docs acquisition source."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import yaml

try:
    from scripts.route_query import REGISTRY, ROOT, load_yaml
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import REGISTRY, ROOT, load_yaml


SUPPORTED_EXTS = {".md", ".txt", ".json", ".html"}


def corpus_record(corpus_id: str) -> dict:
    for corpus in load_yaml(REGISTRY).get("corpora", []):
        if corpus.get("corpus_id") == corpus_id:
            return corpus
    return {}


def registry_path_errors() -> list[str]:
    errors = []
    for corpus in load_yaml(REGISTRY).get("corpora", []):
        status = corpus.get("status")
        root_path = corpus.get("root_path")
        corpus_id = corpus.get("corpus_id")
        if status in {"available", "indexed"}:
            if not root_path:
                errors.append(f"{corpus_id}: available/indexed corpus requires root_path")
            elif not (ROOT / root_path).exists():
                errors.append(f"{corpus_id}: root_path does not exist: {root_path}")
        if status in {"available", "indexed"} and corpus.get("update_policy") == "refreshable_snapshot" and not corpus.get("snapshot_date"):
            errors.append(f"{corpus_id}: refreshable available/indexed corpus requires snapshot_date")
    return errors


def count_files(path: Path, limit: int | None = None) -> dict:
    total = supported = unsupported = 0
    for item in path.rglob("*"):
        if not item.is_file():
            continue
        total += 1
        if item.suffix.lower() in SUPPORTED_EXTS:
            supported += 1
        else:
            unsupported += 1
        if limit and total >= limit:
            break
    return {"total": total, "supported": supported, "unsupported": unsupported}


def build_manifest(corpus_id: str, source_path: Path, limit: int | None = None) -> dict:
    corpus = corpus_record(corpus_id)
    warnings = []
    if not corpus:
        warnings.append(f"{corpus_id}: corpus is not registered")
    if not source_path.exists():
        counts = {"total": 0, "supported": 0, "unsupported": 0}
        warnings.append(f"source path does not exist: {source_path}")
    elif not source_path.is_dir():
        counts = {"total": 1, "supported": int(source_path.suffix.lower() in SUPPORTED_EXTS), "unsupported": int(source_path.suffix.lower() not in SUPPORTED_EXTS)}
    else:
        counts = count_files(source_path, limit=limit)
    if counts["supported"] == 0:
        warnings.append("no supported documentation files found")

    return {
        "manifest_id": f"acquisition-{corpus_id}",
        "corpus_id": corpus_id,
        "method": "manual_import",
        "authority_level": corpus.get("authority_level", "unknown"),
        "source": str(source_path.relative_to(ROOT)).replace("\\", "/") if source_path.is_absolute() and source_path.is_relative_to(ROOT) else str(source_path).replace("\\", "/"),
        "product": corpus.get("product", "unknown"),
        "version": corpus.get("version", "unknown"),
        "snapshot_date": corpus.get("snapshot_date"),
        "status": "dry_run",
        "file_counts": counts,
        "warnings": warnings,
        "ready_for_indexing": bool(corpus and counts["supported"] > 0 and not warnings),
        "created_at": datetime.now(timezone.utc).isoformat(),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-id", required=True)
    parser.add_argument("--path", required=True)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    source_path = Path(args.path)
    if not source_path.is_absolute():
        source_path = ROOT / source_path
    manifest = build_manifest(args.corpus_id, source_path, limit=args.limit)
    output = yaml.safe_dump(manifest, sort_keys=False)
    if args.out:
        out = args.out if args.out.is_absolute() else ROOT / args.out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(output, encoding="utf-8")
    else:
        print(output.strip())
    return 0 if manifest["ready_for_indexing"] or manifest["status"] == "dry_run" else 1


if __name__ == "__main__":
    raise SystemExit(main())
