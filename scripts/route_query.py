"""Route a user query to the smallest relevant docs corpus set."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "second-brain" / "corpora" / "registry.yaml"
BINDINGS = ROOT / "second-brain" / "corpora" / "project-bindings.yaml"


PRODUCT_RULES = [
    ("Unity", "engines", ["unity", "gameobject", "monobehaviour", "input system", "urp", "hdrp"]),
    ("Codex", "agent_platforms", ["codex", "agents.md", "skill", "plugin", "mcp", "sandbox", "approval"]),
    ("Python", "languages", ["python", "asyncio", "pytest", "pip", "venv", "taskgroup"]),
    ("TypeScript", "languages", ["typescript", "tsconfig", "tsx", "typecheck", "npm", "node"]),
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def detect_product(query: str) -> tuple[str, str, str]:
    q = query.lower()
    matches = []
    for product, category, needles in PRODUCT_RULES:
        score = sum(1 for needle in needles if needle in q)
        if score:
            matches.append((score, product, category))
    if not matches:
        return "unknown", "unknown", "low"
    matches.sort(reverse=True)
    top = matches[0]
    if len(matches) > 1 and matches[1][0] == top[0]:
        return top[1], top[2], "low"
    return top[1], top[2], "high" if top[0] > 1 else "medium"


def selected_corpus(product: str, registry: dict, bindings: dict) -> tuple[list[str], list[str], str | None]:
    corpora = registry.get("corpora", [])
    candidates = [c for c in corpora if c.get("product") == product]
    if not candidates:
        return [], [], "No matching corpus is registered."

    for binding in bindings.get("bindings", []):
        if binding.get("product") == product:
            preferred = binding["preferred_corpus_id"]
            excluded = [c["corpus_id"] for c in candidates if c["corpus_id"] != preferred]
            return [preferred], excluded, None

    available = [c for c in candidates if c.get("status") in {"available", "indexed"}]
    selected = available[:1] or candidates[:1]
    excluded = [c["corpus_id"] for c in candidates if c not in selected]
    return [selected[0]["corpus_id"]], excluded, None


def route(query: str) -> dict:
    registry = load_yaml(REGISTRY)
    bindings = load_yaml(BINDINGS)
    product, category, confidence = detect_product(query)
    selected, excluded, issue = selected_corpus(product, registry, bindings)
    clarification = None
    if issue:
        clarification = issue
    elif confidence == "low":
        clarification = "The query may match multiple or unknown documentation domains."

    return {
        "query": query,
        "detected_category": category,
        "detected_product": product,
        "selected_corpora": selected,
        "excluded_corpora": excluded,
        "route_confidence": confidence if selected else "low",
        "clarification_needed": clarification,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    args = parser.parse_args()
    print(yaml.safe_dump(route(args.query), sort_keys=False).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
