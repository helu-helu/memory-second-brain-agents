"""Review and promote second-brain lesson and skill candidates."""

from __future__ import annotations

import argparse
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


ALLOWED = {
    "approve": {"draft": "approved", "candidate": "approved"},
    "reject": {"draft": "rejected", "candidate": "rejected", "approved": "rejected"},
    "activate": {"approved": "active"},
}


@dataclass
class Artifact:
    path: Path
    artifact_type: str
    frontmatter: dict
    body: str


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def load_artifact(path: Path, artifact_type: str) -> Artifact:
    frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return Artifact(path=path, artifact_type=artifact_type, frontmatter=frontmatter, body=body)


def render(frontmatter: dict, body: str) -> str:
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False).strip() + "\n---\n" + body


def iter_artifacts(root: Path) -> list[Artifact]:
    artifacts = []
    for path in (root / "memory" / "lessons").glob("*.md"):
        artifacts.append(load_artifact(path, "lesson"))
    for path in (root / "skills" / "candidates").glob("*/SKILL.md"):
        artifacts.append(load_artifact(path, "skill_candidate"))
    return artifacts


def artifact_row(root: Path, artifact: Artifact) -> dict:
    data = artifact.frontmatter
    return {
        "id": data.get("id"),
        "artifact_type": artifact.artifact_type,
        "path": str(artifact.path.relative_to(root)).replace("\\", "/"),
        "status": data.get("status"),
        "confidence": data.get("confidence"),
        "title_or_name": data.get("title") or data.get("name"),
        "evidence_count": len(data.get("evidence") or []),
        "last_modified": datetime.fromtimestamp(artifact.path.stat().st_mtime, tz=timezone.utc).isoformat(),
    }


def list_artifacts(root: Path, status: str | None = "candidate") -> list[dict]:
    rows = [artifact_row(root, artifact) for artifact in iter_artifacts(root)]
    if status:
        rows = [row for row in rows if row["status"] == status]
    return sorted(rows, key=lambda row: (row["artifact_type"], row["id"] or ""))


def find_artifact(root: Path, artifact_id: str) -> Artifact:
    matches = [artifact for artifact in iter_artifacts(root) if artifact.frontmatter.get("id") == artifact_id]
    if not matches:
        raise ValueError(f"Artifact not found: {artifact_id}")
    if len(matches) > 1:
        raise ValueError(f"Duplicate artifact id: {artifact_id}")
    return matches[0]


def decision_path(root: Path, artifact_id: str, action: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return root / "reviews" / "decisions" / f"review-{artifact_id}-{action}-{stamp}.md"


def write_decision(root: Path, artifact: Artifact, previous: str, new: str, reviewer: str, reason: str) -> Path:
    out = decision_path(root, artifact.frontmatter["id"], new)
    out.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "id": out.stem,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "artifact_id": artifact.frontmatter["id"],
        "artifact_type": artifact.artifact_type,
        "artifact_path": str(artifact.path),
        "previous_status": previous,
        "new_status": new,
        "reviewer": reviewer,
        "reason": reason,
        "evidence": artifact.frontmatter.get("evidence") or [],
    }
    out.write_text(render(data, "\n# Review Decision\n"), encoding="utf-8")
    return out


def require_review(reviewer: str, reason: str) -> None:
    if not reviewer.strip() or not reason.strip():
        raise ValueError("reviewer and reason are required")


def promote_skill(root: Path, artifact: Artifact, decision: Path) -> None:
    active = root / "skills" / "active" / artifact.frontmatter["id"] / "SKILL.md"
    if active.exists():
        raise ValueError(f"Active skill already exists: {active}")
    active.parent.mkdir(parents=True, exist_ok=True)
    data = dict(artifact.frontmatter)
    data["status"] = "active"
    data["source_candidate"] = str(artifact.path).replace("\\", "/")
    data["activated_at"] = datetime.now(timezone.utc).isoformat()
    data["review_decision"] = str(decision).replace("\\", "/")
    active.write_text(render(data, artifact.body), encoding="utf-8")


def transition(root: Path, artifact_id: str, action: str, reviewer: str, reason: str) -> dict:
    require_review(reviewer, reason)
    artifact = find_artifact(root, artifact_id)
    previous = artifact.frontmatter.get("status")
    new = ALLOWED[action].get(previous)
    if not new:
        return {
            "ok": False,
            "artifact_id": artifact_id,
            "artifact_type": artifact.artifact_type,
            "previous_status": previous,
            "new_status": None,
            "artifact_path": str(artifact.path),
            "decision_path": None,
            "warnings": [f"Invalid transition: {previous} -> {action}"],
        }

    updated = dict(artifact.frontmatter)
    updated["status"] = new
    if new == "active":
        updated["activated_at"] = datetime.now(timezone.utc).isoformat()
    artifact.path.write_text(render(updated, artifact.body), encoding="utf-8")
    artifact.frontmatter = updated
    decision = write_decision(root, artifact, previous, new, reviewer, reason)
    if action == "activate" and artifact.artifact_type == "skill_candidate":
        promote_skill(root, artifact, decision)
    return {
        "ok": True,
        "artifact_id": artifact_id,
        "artifact_type": artifact.artifact_type,
        "previous_status": previous,
        "new_status": new,
        "artifact_path": str(artifact.path),
        "decision_path": str(decision),
        "warnings": [],
    }


def approve(root: Path, artifact_id: str, reviewer: str, reason: str) -> dict:
    return transition(root, artifact_id, "approve", reviewer, reason)


def reject(root: Path, artifact_id: str, reviewer: str, reason: str) -> dict:
    return transition(root, artifact_id, "reject", reviewer, reason)


def activate(root: Path, artifact_id: str, reviewer: str, reason: str) -> dict:
    return transition(root, artifact_id, "activate", reviewer, reason)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    list_parser = sub.add_parser("list")
    list_parser.add_argument("--root", type=Path, default=Path("second-brain"))
    list_parser.add_argument("--status", default="candidate")
    for command in ("approve", "reject", "activate"):
        action = sub.add_parser(command)
        action.add_argument("artifact_id")
        action.add_argument("--root", type=Path, default=Path("second-brain"))
        action.add_argument("--reviewer", required=True)
        action.add_argument("--reason", required=True)

    args = parser.parse_args(argv)
    try:
        if args.command == "list":
            print(yaml.safe_dump({"artifacts": list_artifacts(args.root, args.status)}, sort_keys=False), end="")
            return 0
        result = transition(args.root, args.artifact_id, args.command, args.reviewer, args.reason)
        print(yaml.safe_dump(result, sort_keys=False), end="")
        return 0 if result["ok"] else 1
    except ValueError as exc:
        print(yaml.safe_dump({"ok": False, "error": str(exc)}, sort_keys=False), end="")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
