from scripts.build_context_pack import build_pack, render_markdown


def test_context_pack_uses_router_fields():
    frontmatter, body = build_pack("How should Codex skills use MCP?", 5)
    assert frontmatter["corpus"]["selected"] == ["codex-docs"]
    assert frontmatter["limits"]["applied_sources"] == 0
    assert "codex-docs has no local root_path yet" in body[0]["warnings"][0]


def test_context_pack_render_is_markdown_with_frontmatter():
    frontmatter, body = build_pack("How should I configure this thing?", 5)
    rendered = render_markdown(frontmatter, body)
    assert rendered.startswith("---\n")
    assert "# Context Pack" in rendered
    assert "## Query Route" in rendered


def test_context_pack_sources_include_score_signals():
    frontmatter, body = build_pack("How do I use the Unity Input System?", 5)
    assert frontmatter["limits"]["applied_sources"] <= 5
    source = body[0]["sources"][0]
    assert source["corpus_id"] == "unity-6.3"
    assert source["scores"]
    assert {"path", "phrase", "symbol", "vector"} <= set(source["scores"])
    rendered = render_markdown(frontmatter, body)
    assert "- Scores:" in rendered


def test_context_pack_degrades_when_vector_requested():
    frontmatter, body = build_pack("How do I use the Unity Input System?", 5, mode="hybrid")
    assert frontmatter["retrieval"]["mode"] == "degraded"
    assert frontmatter["retrieval"]["requested_mode"] == "hybrid"
    assert frontmatter["retrieval"]["vector_enabled"] is False
    assert "Vector retrieval requested but unavailable" in body[0]["warnings"][0]
