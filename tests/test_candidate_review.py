from pathlib import Path

import yaml

from scripts.review_candidate import activate, approve, list_artifacts, reject


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}


def write_lesson(root: Path, status: str = "candidate") -> Path:
    path = root / "memory" / "lessons" / "lesson-test.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: lesson-test
title: Test Lesson
status: {status}
confidence: medium
trigger: test
scope: test
guidance: Use evidence.
evidence:
  - path: source.md
    type: source
---

# Test Lesson
""",
        encoding="utf-8",
    )
    return path


def write_skill(root: Path, status: str = "candidate") -> Path:
    path = root / "skills" / "candidates" / "skill-test" / "SKILL.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: skill-test
name: skill-test
status: {status}
confidence: medium
trigger: test
inputs:
  - input
workflow:
  - step
outputs:
  - output
scripts: []
eval: Run once.
failure_modes:
  - failure
evidence:
  - path: source.md
    type: source
---

# Skill Test
""",
        encoding="utf-8",
    )
    return path


def test_list_candidates_includes_metadata_and_filters_status(tmp_path):
    root = tmp_path / "second-brain"
    write_lesson(root, "candidate")
    write_skill(root, "active")

    artifacts = list_artifacts(root, status="candidate")

    assert len(artifacts) == 1
    assert artifacts[0]["id"] == "lesson-test"
    assert artifacts[0]["artifact_type"] == "lesson"
    assert artifacts[0]["evidence_count"] == 1


def test_approve_updates_status_and_writes_decision(tmp_path):
    root = tmp_path / "second-brain"
    lesson = write_lesson(root, "candidate")

    result = approve(root, "lesson-test", reviewer="codex", reason="Good scoped evidence.")

    assert result["ok"] is True
    assert result["previous_status"] == "candidate"
    assert result["new_status"] == "approved"
    assert frontmatter(lesson)["status"] == "approved"
    decision = Path(result["decision_path"])
    decision_data = frontmatter(decision)
    assert decision_data["artifact_id"] == "lesson-test"
    assert decision_data["reviewer"] == "codex"


def test_reject_updates_status_and_writes_decision(tmp_path):
    root = tmp_path / "second-brain"
    skill = write_skill(root, "approved")

    result = reject(root, "skill-test", reviewer="codex", reason="Too broad.")

    assert result["ok"] is True
    assert result["new_status"] == "rejected"
    assert frontmatter(skill)["status"] == "rejected"
    assert Path(result["decision_path"]).exists()


def test_invalid_transition_leaves_artifact_unchanged(tmp_path):
    root = tmp_path / "second-brain"
    lesson = write_lesson(root, "active")

    result = approve(root, "lesson-test", reviewer="codex", reason="Again.")

    assert result["ok"] is False
    assert frontmatter(lesson)["status"] == "active"
    assert not (root / "reviews" / "decisions").exists()


def test_unapproved_artifact_cannot_activate(tmp_path):
    root = tmp_path / "second-brain"
    lesson = write_lesson(root, "candidate")

    result = activate(root, "lesson-test", reviewer="codex", reason="Use it.")

    assert result["ok"] is False
    assert frontmatter(lesson)["status"] == "candidate"


def test_approved_skill_candidate_creates_active_skill_copy(tmp_path):
    root = tmp_path / "second-brain"
    skill = write_skill(root, "approved")

    result = activate(root, "skill-test", reviewer="codex", reason="Ready.")

    assert result["ok"] is True
    assert frontmatter(skill)["status"] == "active"
    active = root / "skills" / "active" / "skill-test" / "SKILL.md"
    assert active.exists()
    active_data = frontmatter(active)
    assert active_data["status"] == "active"
    assert active_data["source_candidate"].endswith("skills/candidates/skill-test/SKILL.md")
