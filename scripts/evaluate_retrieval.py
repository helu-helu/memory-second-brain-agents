"""Run lightweight retrieval eval cases against context-pack generation."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

try:
    from scripts.build_context_pack import build_pack
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from build_context_pack import build_pack


def load_cases(path: Path) -> list[dict]:
    return (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("cases", [])


def evaluate_case(case: dict) -> list[str]:
    frontmatter, body = build_pack(case["query"], case["max_sources"])
    route = body[0]["route"]
    sources = body[0]["sources"]
    warnings = body[0]["warnings"]
    failures = []

    if route["detected_product"] != case["expected_product"]:
        failures.append(f"product {route['detected_product']!r} != {case['expected_product']!r}")
    expected_corpus = case.get("expected_corpus")
    if expected_corpus and expected_corpus not in frontmatter["corpus"]["selected"]:
        failures.append(f"missing expected corpus {expected_corpus}")
    if frontmatter["limits"]["applied_sources"] > case["max_sources"]:
        failures.append("source limit exceeded")
    if case.get("expect_clarification") and not route.get("clarification_needed"):
        failures.append("expected clarification")
    if case.get("expect_warning") and not warnings:
        failures.append("expected warning")

    patterns = case.get("expected_path_patterns") or []
    if patterns and not any(any(pattern.lower() in source["path"].lower() for pattern in patterns) for source in sources[:3]):
        failures.append(f"top sources did not match patterns {patterns}")
    return failures


def run(path: Path) -> tuple[int, list[str]]:
    failures = []
    cases = load_cases(path)
    for case in cases:
        case_failures = evaluate_case(case)
        if case_failures:
            failures.append(f"{case['id']}: " + "; ".join(case_failures))
    return len(cases) - len(failures), failures


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path)
    args = parser.parse_args(argv)
    passed, failures = run(args.fixture)
    for failure in failures:
        print(f"FAIL {failure}", file=sys.stderr)
    print(f"retrieval eval: {passed} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
