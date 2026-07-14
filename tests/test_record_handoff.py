from pathlib import Path

import pytest
import yaml

from scripts.record_handoff import main, record_handoff


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return yaml.safe_load(text[4:end]) or {}


def test_record_handoff_writes_frontmatter_and_summary(tmp_path):
    out = record_handoff(
        "Finish feature",
        "Implemented and tested.",
        out_root=tmp_path / "second-brain",
        files=["scripts/x.py"],
        decisions=["Keep it small."],
        followups=["Wrap with MCP."],
    )

    data = frontmatter(out)
    assert data["status"] == "completed"
    assert data["agent"] == "codex"
    assert data["files"] == ["scripts/x.py"]
    assert data["decisions"] == ["Keep it small."]
    assert "Implemented and tested." in out.read_text(encoding="utf-8")


def test_record_handoff_requires_title_and_summary(tmp_path):
    with pytest.raises(ValueError):
        record_handoff("", "summary", out_root=tmp_path)


def test_record_handoff_cli(tmp_path):
    assert main(["--title", "CLI handoff", "--summary", "From CLI.", "--out-root", str(tmp_path / "second-brain")]) == 0
    assert list((tmp_path / "second-brain" / "memory" / "handoffs").glob("*.md"))
