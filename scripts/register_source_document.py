"""Create a source-document metadata Markdown file."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_path")
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--source-type", default="official_docs")
    parser.add_argument("--vendor")
    parser.add_argument("--product")
    parser.add_argument("--version")
    parser.add_argument("--status", default="converted")
    parser.add_argument("--visibility", default="project")
    parser.add_argument("--sensitivity", default="low")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    source = Path(args.source_path)
    if not source.is_absolute():
        source = ROOT / source
    metadata = {
        "id": args.id,
        "title": args.title,
        "source_path": display_path(source),
        "source_type": args.source_type,
        "vendor": args.vendor,
        "product": args.product,
        "version": args.version,
        "checksum": sha256(source),
        "status": args.status,
        "visibility": args.visibility,
        "sensitivity": args.sensitivity,
    }
    out = Path(args.out)
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n", encoding="utf-8")
    print(display_path(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
