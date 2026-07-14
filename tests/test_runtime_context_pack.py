from pathlib import Path

from scripts.build_context_pack import build_pack_from_context_result, render_markdown


def test_runtime_context_pack_uses_unified_context_sources():
    context = {
        "trace_id": "ctx-test",
        "query": "Unity Input System",
        "route": {"selected_corpora": ["unity-6.3"], "excluded_corpora": ["unity-6.5"]},
        "selected_corpora": ["unity-6.3"],
        "excluded_corpora": ["unity-6.5"],
        "memory_hits": [{"id": "m1", "source": "mem0", "confidence": "medium", "text": "Use Unity 6.3."}],
        "knowledge_hits": [
            {"source": "docs/unity/Input.md", "corpus_id": "unity-6.3", "score": 0.9, "snippet": "Input docs"}
        ],
        "quality": {"confidence": "high", "coverage": "partial", "retrieval_mode": "vector"},
        "warnings": [],
    }
    frontmatter, body = build_pack_from_context_result(context, limit=3)
    rendered = render_markdown(frontmatter, body)
    assert frontmatter["retrieval"]["mode"] == "runtime"
    assert body[0]["sources"][0]["path"] == "docs/unity/Input.md"
    assert "## Memory Hits" in rendered


def test_runtime_context_pack_reports_empty_runtime_sources():
    frontmatter, body = build_pack_from_context_result(
        {
            "trace_id": "ctx-empty",
            "query": "missing",
            "route": {},
            "quality": {"confidence": "low", "coverage": "none", "retrieval_mode": "runtime"},
            "knowledge_hits": [],
            "warnings": ["Qdrant unavailable"],
        },
        limit=3,
    )
    assert frontmatter["limits"]["applied_sources"] == 0
    assert "Qdrant unavailable" in body[0]["warnings"]
    assert "Runtime context returned no knowledge sources." in body[0]["warnings"]
