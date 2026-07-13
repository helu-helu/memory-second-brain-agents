from scripts.route_query import route


def test_unity_uses_project_bound_version():
    result = route("How do I use the Unity Input System?")
    assert result["detected_product"] == "Unity"
    assert result["selected_corpora"] == ["unity-6.3"]
    assert "unity-6.5" in result["excluded_corpora"]


def test_codex_routes_to_agent_platform_docs():
    result = route("How should Codex skills and plugins use MCP?")
    assert result["detected_product"] == "Codex"
    assert result["detected_category"] == "agent_platforms"
    assert result["selected_corpora"] == ["codex-docs"]


def test_unknown_query_asks_for_clarification():
    result = route("How should I configure this thing?")
    assert result["selected_corpora"] == []
    assert result["route_confidence"] == "low"
    assert result["clarification_needed"]
