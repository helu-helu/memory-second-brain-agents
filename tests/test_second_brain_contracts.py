from pathlib import Path

from scripts.validate_second_brain import validate_all, validate_context_pack, validate_registry


ROOT = Path(__file__).resolve().parents[1]


def test_demo_second_brain_contracts_are_valid():
    assert validate_all() == []


def test_registry_contains_initial_corpus_families():
    registry = ROOT / "second-brain" / "corpora" / "registry.yaml"
    assert validate_registry(registry) == []
    text = registry.read_text(encoding="utf-8")
    for corpus_id in ["unity-6.3", "unity-6.5", "python-docs", "typescript-docs", "codex-docs"]:
        assert corpus_id in text


def test_context_pack_keeps_sources_bounded():
    context_pack = ROOT / "second-brain" / "demo" / "context-pack.example.md"
    assert validate_context_pack(context_pack) == []
