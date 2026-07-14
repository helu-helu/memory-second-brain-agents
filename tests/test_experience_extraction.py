from pathlib import Path

import yaml

from scripts.extract_experience import main


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}


def write_context_pack(path: Path) -> None:
    path.write_text(
        """---
id: context-pack-test
query: How do I use the Unity Input System?
created_at: '2026-07-14T00:00:00+00:00'
client: codex
corpus:
  selected:
  - unity-6.3
  excluded:
  - unity-6.5
status: generated
---

# Context Pack

## Ranked Sources

### 1. docs/massive/Unity_6_3_Markdown/en/Manual/Input.md

- Corpus: unity-6.3
- Relevance: high
- Why selected: Matched path, symbol.
- Snippet: Unity supports input from many types of devices.
""",
        encoding="utf-8",
    )


def test_context_pack_creates_candidate_lesson_and_run(tmp_path):
    evidence = tmp_path / "context-pack.md"
    out_root = tmp_path / "second-brain"
    write_context_pack(evidence)

    assert main([str(evidence), "--out-root", str(out_root)]) == 0

    lesson = next((out_root / "memory" / "lessons").glob("*.md"))
    lesson_data = frontmatter(lesson)
    assert lesson_data["status"] == "candidate"
    assert lesson_data["confidence"] == "medium"
    assert lesson_data["trigger"]
    assert lesson_data["evidence"][0]["path"] == str(evidence)
    assert "docs/massive/Unity_6_3_Markdown/en/Manual/Input.md" in lesson.read_text(encoding="utf-8")
    assert "status: active" not in lesson.read_text(encoding="utf-8")

    run = next((out_root / "memory" / "extraction-runs").glob("*.md"))
    run_data = frontmatter(run)
    assert run_data["review_status"] == "pending"
    assert str(evidence) in run_data["inputs"]
    assert str(lesson) in run_data["outputs"]


def test_workflow_note_creates_skill_candidate(tmp_path):
    evidence = tmp_path / "workflow.md"
    out_root = tmp_path / "second-brain"
    evidence.write_text(
        """---
id: workflow-note
title: Repeatable context pack workflow
---

# Repeatable workflow

Workflow: route the user query, build a bounded context pack, review warnings.
Steps:
1. Route the query to the right corpus.
2. Build the context pack.
3. Inspect warnings before answering.
""",
        encoding="utf-8",
    )

    assert main([str(evidence), "--out-root", str(out_root)]) == 0

    skill = next((out_root / "skills" / "candidates").glob("*/SKILL.md"))
    skill_data = frontmatter(skill)
    assert skill_data["status"] == "candidate"
    assert skill_data["confidence"] == "medium"
    assert skill_data["workflow"]
    assert skill_data["evidence"][0]["path"] == str(evidence)
    assert "status: active" not in skill.read_text(encoding="utf-8")


def test_factual_note_does_not_create_skill_candidate(tmp_path):
    evidence = tmp_path / "fact.md"
    out_root = tmp_path / "second-brain"
    evidence.write_text(
        """---
id: factual-note
title: Unity fact
---

# Unity fact

Unity supports input from many types of devices.
""",
        encoding="utf-8",
    )

    assert main([str(evidence), "--out-root", str(out_root)]) == 0

    assert not (out_root / "skills" / "candidates").exists()
    run = next((out_root / "memory" / "extraction-runs").glob("*.md"))
    run_data = frontmatter(run)
    assert any("No workflow-like evidence found" in item for item in run_data["decisions"])
