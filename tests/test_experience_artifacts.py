from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n")
    return yaml.safe_load(text.split("---\n", 2)[1])


def schema_required(name: str) -> set[str]:
    return set(yaml.safe_load((ROOT / "schemas" / name).read_text(encoding="utf-8"))["required"])


def test_lesson_example_matches_schema():
    data = frontmatter(ROOT / "second-brain" / "demo" / "lesson.example.md")
    assert schema_required("lesson.schema.yaml") <= set(data)
    assert data["status"] == "candidate"


def test_skill_candidate_example_matches_schema():
    data = frontmatter(ROOT / "second-brain" / "demo" / "skill-candidate" / "SKILL.md")
    assert schema_required("skill-candidate.schema.yaml") <= set(data)
    assert data["status"] == "candidate"


def test_extraction_run_example_matches_schema():
    data = frontmatter(ROOT / "second-brain" / "demo" / "extraction-run.example.md")
    assert schema_required("extraction-run.schema.yaml") <= set(data)
    assert data["review_status"] == "pending"
