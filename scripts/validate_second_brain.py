"""Validate the lightweight second-brain file contracts."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    return yaml.safe_load(text[4:end]) or {}


def check_required(name: str, data: dict, required: list[str]) -> list[str]:
    return [f"{name}: missing {field}" for field in required if field not in data]


def validate_registry(path: Path) -> list[str]:
    schema = load_yaml(ROOT / "schemas" / "corpus.schema.yaml")
    registry = load_yaml(path)
    errors: list[str] = []
    for item in registry.get("corpora", []):
        label = item.get("corpus_id", "<missing corpus_id>")
        errors.extend(check_required(label, item, schema["required"]))
        if (
            item.get("status") in {"available", "indexed"}
            and item.get("update_policy") == "refreshable_snapshot"
            and not item.get("snapshot_date")
        ):
            errors.append(f"{label}: refreshable_snapshot requires snapshot_date")
    if not registry.get("corpora"):
        errors.append(f"{path}: no corpora found")
    return errors


def validate_context_pack(path: Path) -> list[str]:
    schema = load_yaml(ROOT / "schemas" / "context-pack.schema.yaml")
    data = frontmatter(path)
    errors = check_required(str(path), data, schema["required"])
    selected = ((data.get("corpus") or {}).get("selected") or [])
    if not selected:
        errors.append(f"{path}: corpus.selected must include at least one corpus")
    applied = (data.get("limits") or {}).get("applied_sources")
    if applied is not None and applied > 20:
        errors.append(f"{path}: applied_sources should stay <= 20 outside deep-research mode")
    return errors


def validate_all() -> list[str]:
    errors = []
    errors.extend(validate_registry(ROOT / "second-brain" / "corpora" / "registry.yaml"))
    errors.extend(validate_context_pack(ROOT / "second-brain" / "demo" / "context-pack.example.md"))
    return errors


def main() -> int:
    errors = validate_all()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("second-brain contracts ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
