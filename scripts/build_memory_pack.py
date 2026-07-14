"""Build a bounded active personal memory pack for an agent task."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


STOPWORDS = {"a", "an", "and", "for", "how", "i", "in", "is", "of", "the", "to", "use"}


@dataclass
class MemoryItem:
    path: Path
    item_type: str
    frontmatter: dict
    body: str
    score: int


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def terms(query: str) -> list[str]:
    return [word for word in re.findall(r"[a-zA-Z][a-zA-Z0-9_.-]+", query.lower()) if word not in STOPWORDS]


def score_text(data: dict, body: str, query_terms: list[str]) -> int:
    haystack = " ".join(
        str(value)
        for value in [
            data.get("id"),
            data.get("title"),
            data.get("name"),
            data.get("trigger"),
            data.get("guidance"),
            data.get("workflow"),
            body[:500],
        ]
    ).lower()
    return sum(1 for term in query_terms if term in haystack)


def load_item(path: Path, item_type: str, query_terms: list[str]) -> MemoryItem | None:
    data, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if data.get("status") != "active":
        return None
    score = score_text(data, body, query_terms)
    if score <= 0:
        return None
    return MemoryItem(path=path, item_type=item_type, frontmatter=data, body=body, score=score)


def active_items(root: Path, query: str) -> list[MemoryItem]:
    query_terms = terms(query)
    items = []
    for path in (root / "memory" / "lessons").glob("*.md"):
        item = load_item(path, "lesson", query_terms)
        if item:
            items.append(item)
    for path in (root / "skills" / "active").glob("*/SKILL.md"):
        item = load_item(path, "skill", query_terms)
        if item:
            items.append(item)
    return sorted(items, key=lambda item: (-item.score, item.item_type, item.frontmatter.get("id", "")))


def summary(item: MemoryItem) -> str:
    data = item.frontmatter
    if data.get("guidance"):
        return str(data["guidance"])
    if data.get("workflow"):
        return "; ".join(str(step) for step in data["workflow"][:3])
    return " ".join(item.body.split())[:240]


def item_row(root: Path, item: MemoryItem) -> dict:
    data = item.frontmatter
    return {
        "id": data.get("id"),
        "item_type": item.item_type,
        "path": str(item.path.relative_to(root)).replace("\\", "/"),
        "status": data.get("status"),
        "confidence": data.get("confidence"),
        "title_or_name": data.get("title") or data.get("name"),
        "trigger": data.get("trigger"),
        "reason": f"Matched {item.score} query term(s).",
        "summary": summary(item),
    }


def build_pack(query: str, root: Path = Path("second-brain"), limit: int = 5) -> tuple[dict, dict]:
    applied_limit = max(1, min(limit, 20))
    selected = [item_row(root, item) for item in active_items(root, query)[:applied_limit]]
    warnings = [] if selected else ["No active memory matched the query."]
    frontmatter = {
        "id": "memory-pack-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
        "query": query,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "client": "codex",
        "limits": {"requested_items": limit, "applied_items": len(selected)},
        "quality": {
            "confidence": "medium" if selected else "low",
            "coverage": "partial" if selected else "none",
            "selected_count": len(selected),
        },
        "status": "generated",
    }
    return frontmatter, {"items": selected, "warnings": warnings}


def render_markdown(frontmatter: dict, body: dict) -> str:
    lines = [
        "---",
        yaml.safe_dump(frontmatter, sort_keys=False).strip(),
        "---",
        "",
        "# Active Memory Pack",
        "",
        "## Selected Memory",
        "",
    ]
    if not body["items"]:
        lines.append("No active memory matched the query.")
    for idx, item in enumerate(body["items"], 1):
        lines.extend(
            [
                f"### {idx}. {item['title_or_name'] or item['id']}",
                "",
                f"- ID: {item['id']}",
                f"- Type: {item['item_type']}",
                f"- Path: {item['path']}",
                f"- status: {item['status']}",
                f"- Confidence: {item['confidence']}",
                f"- Trigger: {item['trigger']}",
                f"- Reason: {item['reason']}",
                f"- Summary: {item['summary']}",
                "",
            ]
        )
    lines.extend(["## Recall Warnings", ""])
    lines.extend(f"- {warning}" for warning in body["warnings"]) if body["warnings"] else lines.append("None.")
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--root", type=Path, default=Path("second-brain"))
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)
    frontmatter, body = build_pack(args.query, root=args.root, limit=args.limit)
    rendered = render_markdown(frontmatter, body)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
