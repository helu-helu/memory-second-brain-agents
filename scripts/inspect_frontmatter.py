"""Inspect YAML frontmatter in Markdown files."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    return yaml.safe_load(text[4:end]) or {}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: python scripts/inspect_frontmatter.py <markdown-file>", file=sys.stderr)
        return 2
    data = read_frontmatter(Path(argv[1]))
    print(yaml.safe_dump(data, sort_keys=False).strip())
    return 0 if data else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
