from pathlib import Path

from agent_core.access_tools import build_active_memory_pack, build_docs_context_pack, inspect_corpus_status, inspect_second_brain_status, list_corpora, response, route_docs_query


ROOT = Path(__file__).resolve().parents[1]


def test_response_contract_success_and_failure():
    assert response({"x": 1}) == {"ok": True, "data": {"x": 1}, "warnings": [], "error": None}
    failed = response(error="bad")
    assert failed["ok"] is False
    assert failed["data"] is None
    assert failed["error"] == "bad"


def test_list_corpora_returns_registry_records():
    result = list_corpora()
    assert result["ok"]
    assert any(item["corpus_id"] == "unity-6.3" for item in result["data"])


def test_route_docs_query_uses_project_binding():
    result = route_docs_query("How do I use the Unity Input System?")
    assert result["ok"]
    assert result["data"]["selected_corpora"] == ["unity-6.3"]
    assert "unity-6.5" in result["data"]["excluded_corpora"]


def test_build_docs_context_pack_writes_bounded_pack():
    out = "second-brain/demo/runs/access-tool-unity.md"
    result = build_docs_context_pack("How do I use the Unity Input System?", limit=3, out=out)
    assert result["ok"]
    assert result["data"]["path"] == out
    assert result["data"]["selected_corpora"] == ["unity-6.3"]
    assert result["data"]["applied_sources"] <= 3
    assert (ROOT / out).exists()


def test_build_docs_context_pack_returns_missing_corpus_warning():
    result = build_docs_context_pack("How should Codex skills use MCP?", limit=5)
    assert result["ok"]
    assert result["data"]["selected_corpora"] == ["codex-docs"]
    assert result["warnings"]


def test_inspect_unity_corpus_status():
    result = inspect_corpus_status("unity-6.3")
    assert result["ok"]
    assert result["data"]["ready_for_retrieval"] is True
    assert result["data"]["acquisitions"]


def test_inspect_codex_corpus_status_reports_planned_state():
    result = inspect_corpus_status("codex-docs")
    assert result["ok"]
    assert result["data"]["ready_for_retrieval"] is False
    assert result["data"]["crawl_plans"]
    assert any("no local root_path" in warning for warning in result["warnings"])


def test_build_active_memory_pack_writes_pack():
    out = "second-brain/memory/packs/access-tool-memory.md"
    result = build_active_memory_pack("Unity Input System", limit=3, out=out)
    assert result["ok"]
    assert result["data"]["path"] == out
    assert result["data"]["applied_items"] <= 3
    assert (ROOT / out).exists()


def test_inspect_second_brain_status_returns_lifecycle_summary():
    result = inspect_second_brain_status()
    assert result["ok"]
    assert "memory" in result["data"]
    assert "reviews" in result["data"]
    assert "corpora" in result["data"]
    assert "by_status" in result["data"]["memory"]
