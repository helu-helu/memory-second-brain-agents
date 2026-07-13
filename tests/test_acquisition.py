from pathlib import Path

import pytest
import yaml

from scripts.create_crawl_plan import main as create_crawl_plan_main
from scripts.validate_acquisition import build_manifest, main as validate_acquisition_main, registry_path_errors


ROOT = Path(__file__).resolve().parents[1]


def test_validate_acquisition_counts_supported_files():
    manifest = build_manifest("unity-6.3", ROOT / "tests" / "fixtures" / "acquisition-sample")
    assert manifest["file_counts"] == {"total": 3, "supported": 2, "unsupported": 1}
    assert manifest["ready_for_indexing"] is True


def test_validate_acquisition_warns_on_missing_path(tmp_path):
    manifest = build_manifest("unity-6.3", tmp_path / "missing")
    assert manifest["ready_for_indexing"] is False
    assert manifest["warnings"]


def test_registry_path_rules_pass_current_registry():
    assert registry_path_errors() == []


def test_validate_acquisition_writes_report(tmp_path, monkeypatch):
    out = tmp_path / "run.yaml"
    monkeypatch.setattr(
        "sys.argv",
        [
            "validate_acquisition.py",
            "--corpus-id",
            "unity-6.3",
            "--path",
            "tests/fixtures/acquisition-sample",
            "--out",
            str(out),
        ],
    )
    assert validate_acquisition_main() == 0
    data = yaml.safe_load(out.read_text(encoding="utf-8"))
    assert data["corpus_id"] == "unity-6.3"
    assert data["file_counts"]["supported"] == 2


def test_create_crawl_plan_writes_policy_file(tmp_path, monkeypatch):
    out = tmp_path / "codex.yaml"
    monkeypatch.setattr(
        "sys.argv",
        [
            "create_crawl_plan.py",
            "--plan-id",
            "crawl-codex-docs",
            "--corpus-id",
            "codex-docs",
            "--url",
            "https://developers.openai.com/codex/",
            "--domain",
            "developers.openai.com",
            "--output",
            "docs/external/codex/snapshot-2026-07-14",
            "--out",
            str(out),
        ],
    )
    assert create_crawl_plan_main() == 0
    data = yaml.safe_load(out.read_text(encoding="utf-8"))
    assert data["approval_status"] == "draft"
    assert data["allowed_domains"] == ["developers.openai.com"]


def test_create_crawl_plan_rejects_unapproved_domain(tmp_path, monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "create_crawl_plan.py",
            "--plan-id",
            "bad",
            "--corpus-id",
            "bad",
            "--url",
            "https://example.com/docs/",
            "--domain",
            "developers.openai.com",
            "--output",
            "docs/external/bad",
            "--out",
            str(tmp_path / "bad.yaml"),
        ],
    )
    with pytest.raises(ValueError):
        create_crawl_plan_main()
