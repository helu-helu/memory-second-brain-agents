from agent_core.context_contract import build_unified_context_result, knowledge_hits, memory_hits


def test_memory_hits_normalize_mem0_results():
    hits = memory_hits([{"memory": "User prefers concise code.", "id": "m1"}])
    assert hits == [
        {
            "id": "m1",
            "source": "mem0",
            "confidence": "unknown",
            "text": "User prefers concise code.",
        }
    ]


def test_knowledge_hits_parse_source_blocks():
    hits, warnings = knowledge_hits("[Source: unity.md]\nCamera docs\n\n---\n\n[Source: input.md]\nInput docs")
    assert warnings == []
    assert [hit["source"] for hit in hits] == ["unity.md", "input.md"]
    assert hits[0]["snippet"] == "Camera docs"


def test_knowledge_hits_degraded_warning():
    hits, warnings = knowledge_hits("(Knowledge Base is not loaded)")
    assert hits == []
    assert warnings == ["(Knowledge Base is not loaded)"]


def test_build_unified_context_result_shape():
    result = build_unified_context_result(
        query="Unity Input System",
        route={"selected_corpora": ["unity-6.3"], "excluded_corpora": ["unity-6.5"]},
        memories=[{"memory": "Use project-bound Unity docs."}],
        knowledge_text="[Source: Input.md]\nInput docs",
        prompt_context="prompt",
    )
    assert result["selected_corpora"] == ["unity-6.3"]
    assert result["excluded_corpora"] == ["unity-6.5"]
    assert result["memory_hits"]
    assert result["knowledge_hits"]
    assert result["quality"]["confidence"] == "high"
    assert result["prompt_context"] == "prompt"
