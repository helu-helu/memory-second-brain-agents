from pathlib import Path

import yaml

from scripts.build_memory_pack import build_pack, main


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}


def write_lesson(root: Path, artifact_id: str, status: str, title: str) -> Path:
    path = root / "memory" / "lessons" / f"{artifact_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: {artifact_id}
title: {title}
status: {status}
confidence: medium
trigger: Unity Input System
scope: unity
guidance: Use active Unity input evidence before answering.
evidence:
  - path: source.md
    type: source
---

# {title}

Unity Input System guidance for agent answers.
""",
        encoding="utf-8",
    )
    return path


def write_skill(root: Path, artifact_id: str, status: str) -> Path:
    path = root / "skills" / "active" / artifact_id / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: {artifact_id}
name: {artifact_id}
status: {status}
confidence: high
trigger: context pack workflow
workflow:
  - Route query
  - Build pack
evidence:
  - path: source.md
    type: source
---

# Context Pack Workflow
""",
        encoding="utf-8",
    )
    return path


def test_matching_active_lesson_appears_in_pack(tmp_path):
    root = tmp_path / "second-brain"
    write_lesson(root, "lesson-input", "active", "Unity Input Memory")
    out = tmp_path / "pack.md"

    assert main(["Unity Input System", "--root", str(root), "--out", str(out)]) == 0

    data = frontmatter(out)
    text = out.read_text(encoding="utf-8")
    assert data["limits"]["applied_items"] == 1
    assert "lesson-input" in text
    assert "status: active" in text


def test_no_match_reports_warning(tmp_path):
    root = tmp_path / "second-brain"
    write_lesson(root, "lesson-input", "active", "Unity Input Memory")

    front, body = build_pack("Python packaging", root=root, limit=5)

    assert front["limits"]["applied_items"] == 0
    assert body["warnings"] == ["No active memory matched the query."]


def test_non_active_artifacts_are_excluded(tmp_path):
    root = tmp_path / "second-brain"
    write_lesson(root, "lesson-candidate", "candidate", "Unity Input Candidate")

    front, body = build_pack("Unity Input", root=root, limit=5)

    assert front["limits"]["applied_items"] == 0
    assert body["items"] == []


def test_output_does_not_exceed_limit(tmp_path):
    root = tmp_path / "second-brain"
    write_lesson(root, "lesson-one", "active", "Unity Input One")
    write_lesson(root, "lesson-two", "active", "Unity Input Two")
    write_skill(root, "skill-input", "active")

    front, body = build_pack("Unity Input", root=root, limit=2)

    assert front["limits"]["applied_items"] == 2
    assert len(body["items"]) == 2


def test_quality_metadata_and_reasons(tmp_path):
    root = tmp_path / "second-brain"
    write_skill(root, "skill-pack", "active")

    front, body = build_pack("context pack", root=root, limit=5)

    assert front["quality"]["confidence"] == "medium"
    assert front["quality"]["coverage"] == "partial"
    assert body["items"][0]["reason"]
