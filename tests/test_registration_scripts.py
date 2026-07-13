from pathlib import Path

import yaml

from scripts.register_source_document import main as register_source_main


ROOT = Path(__file__).resolve().parents[1]


def test_register_source_document_creates_frontmatter(tmp_path, monkeypatch):
    source = tmp_path / "source.md"
    source.write_text("# Demo\n", encoding="utf-8")
    out = tmp_path / "registered.md"
    monkeypatch.setattr(
        "sys.argv",
        [
            "register_source_document.py",
            str(source),
            "--id",
            "doc-test",
            "--title",
            "Doc Test",
            "--out",
            str(out),
        ],
    )
    assert register_source_main() == 0
    text = out.read_text(encoding="utf-8")
    data = yaml.safe_load(text.split("---\n", 2)[1])
    assert data["id"] == "doc-test"
    assert data["checksum"]
