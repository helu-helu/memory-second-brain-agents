from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_FIXTURE = ROOT / "tests" / "fixtures" / "unified_context_result.yaml"
QUERY_FIXTURE = ROOT / "tests" / "fixtures" / "unified_runtime_queries.yaml"


def test_unified_context_result_fixture_shape():
    data = yaml.safe_load(CONTRACT_FIXTURE.read_text(encoding="utf-8"))
    required = {
        "trace_id",
        "query",
        "route",
        "selected_corpora",
        "excluded_corpora",
        "memory_hits",
        "knowledge_hits",
        "quality",
        "warnings",
        "context_pack_path",
        "created_at",
    }
    assert required <= set(data)
    assert {"confidence", "coverage", "retrieval_mode"} <= set(data["quality"])
    assert data["route"]["selected_corpora"] == data["selected_corpora"]


def test_unified_context_hits_are_inspectable():
    data = yaml.safe_load(CONTRACT_FIXTURE.read_text(encoding="utf-8"))
    for hit in data["memory_hits"] + data["knowledge_hits"]:
        assert hit["id"]
        assert hit["source"]
    for hit in data["knowledge_hits"]:
        assert "corpus_id" in hit
        assert "snippet" in hit


def test_unified_runtime_query_fixture_has_representative_matrix():
    data = yaml.safe_load(QUERY_FIXTURE.read_text(encoding="utf-8"))
    cases = data["cases"]
    assert len(cases) >= 20
    required = {"id", "query", "expected_route", "expects_memory", "expects_knowledge", "expected_behavior"}
    for case in cases:
        assert required <= set(case)
        assert case["id"]
        assert "expected_behavior" in case


def test_unified_runtime_query_fixture_covers_degraded_paths():
    cases = yaml.safe_load(QUERY_FIXTURE.read_text(encoding="utf-8"))["cases"]
    ids = {case["id"] for case in cases}
    assert {"missing-qdrant", "missing-memory", "empty-query", "no-results"} <= ids
