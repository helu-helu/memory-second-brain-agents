"""Record an agent task handoff as a file-first memory artifact."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:64] or "handoff"


def split_values(values: list[str] | None) -> list[str]:
    return [value.strip() for value in values or [] if value.strip()]


def render(frontmatter: dict, summary: str) -> str:
    return "\n".join(
        [
            "---",
            yaml.safe_dump(frontmatter, sort_keys=False).strip(),
            "---",
            "",
            f"# {frontmatter['title']}",
            "",
            "## Summary",
            "",
            summary.strip(),
            "",
        ]
    )


def record_handoff(
    title: str,
    summary: str,
    out_root: Path = Path("second-brain"),
    status: str = "completed",
    agent: str = "codex",
    files: list[str] | None = None,
    decisions: list[str] | None = None,
    followups: list[str] | None = None,
) -> Path:
    if not title.strip() or not summary.strip():
        raise ValueError("title and summary are required")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    handoff_id = f"handoff-{slugify(title)}-{stamp}"
    out = out_root / "memory" / "handoffs" / f"{handoff_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = {
        "id": handoff_id,
        "title": title,
        "status": status,
        "agent": agent,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "files": split_values(files),
        "decisions": split_values(decisions),
        "followups": split_values(followups),
    }
    out.write_text(render(frontmatter, summary), encoding="utf-8")
    return out


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--out-root", type=Path, default=Path("second-brain"))
    parser.add_argument("--status", default="completed")
    parser.add_argument("--agent", default="codex")
    parser.add_argument("--file", action="append", dest="files")
    parser.add_argument("--decision", action="append", dest="decisions")
    parser.add_argument("--followup", action="append", dest="followups")
    args = parser.parse_args(argv)
    out = record_handoff(
        args.title,
        args.summary,
        out_root=args.out_root,
        status=args.status,
        agent=args.agent,
        files=args.files,
        decisions=args.decisions,
        followups=args.followups,
    )
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
