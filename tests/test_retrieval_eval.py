from pathlib import Path

import yaml

from scripts.evaluate_retrieval import evaluate_case, load_cases, run


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "retrieval_eval.yaml"


def test_retrieval_eval_fixture_contract():
    cases = load_cases(FIXTURE)
    assert len(cases) >= 6
    required = {
        "id",
        "query",
        "expected_product",
        "expected_corpus",
        "expected_path_patterns",
        "max_sources",
        "expect_clarification",
    }
    for case in cases:
        assert required <= set(case)


def test_retrieval_eval_passes_current_fixture():
    passed, failures = run(FIXTURE)
    assert failures == []
    assert passed == len(load_cases(FIXTURE))


def test_retrieval_eval_reports_failure():
    case = {
        "id": "bad",
        "query": "How do I use the Unity Input System?",
        "expected_product": "Python",
        "expected_corpus": "python-docs",
        "expected_path_patterns": ["not-a-real-path"],
        "max_sources": 1,
        "expect_clarification": True,
    }
    assert evaluate_case(case)
