"""Build a small Markdown context pack for an agent query."""

from __future__ import annotations

import argparse
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml

try:
    from scripts.route_query import REGISTRY, ROOT, load_yaml, route
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import REGISTRY, ROOT, load_yaml, route


STOPWORDS = {
    "a",
    "an",
    "and",
    "do",
    "for",
    "it",
    "how",
    "i",
    "in",
    "is",
    "me",
    "of",
    "should",
    "the",
    "this",
    "to",
    "unity",
    "use",
    "work",
}


@dataclass
class RetrievalCandidate:
    path: Path
    corpus_id: str
    scores: dict[str, int]

    @property
    def total_score(self) -> int:
        return sum(self.scores.values())

    def reason(self) -> str:
        active = [name for name, score in self.scores.items() if score]
        return "Matched " + ", ".join(active) + "."


def query_terms(query: str) -> list[str]:
    words = re.findall(r"[a-zA-Z][a-zA-Z0-9_.-]+", query.lower())
    return [word for word in words if word not in STOPWORDS]


def query_phrases(query: str) -> list[str]:
    q = query.lower()
    phrases = []
    for phrase in ["input system", "build pipeline"]:
        if phrase in q:
            phrases.append(phrase)
    return phrases


def scoring_terms(query: str) -> list[str]:
    terms = query_terms(query)
    if "input" in terms:
        terms = [term for term in terms if term != "system"]
    return terms


def symbol_terms(query: str) -> list[str]:
    symbols = [symbol for symbol in re.findall(r"\b[A-Z][A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)?\b", query) if symbol.lower() not in STOPWORDS]
    if any(symbol.lower() == "input" for symbol in symbols):
        symbols = [symbol for symbol in symbols if symbol.lower() != "system"]
    return symbols


def corpus_by_id() -> dict[str, dict]:
    return {item["corpus_id"]: item for item in load_yaml(REGISTRY).get("corpora", [])}


def snippet(path: Path, terms: list[str], max_chars: int = 360) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lower = text.lower()
    positions = [lower.find(term) for term in terms if term in lower]
    start = max(min(positions), 0) if positions else 0
    return " ".join(text[start : start + max_chars].split())


def score_path(root: Path, path: Path, query: str) -> dict[str, int]:
    terms = scoring_terms(query)
    phrases = query_phrases(query)
    symbols = symbol_terms(query)
    path_text = str(path.relative_to(root)).lower()
    return {
        "path": sum(4 for term in terms if term in path_text),
        "phrase": sum(20 for phrase in phrases if phrase in path_text),
        "symbol": sum(12 for symbol in symbols if symbol.lower() in path_text),
        "vector": 0,
    }


def search_markdown(root: Path, query: str, limit: int, corpus_id: str) -> list[dict]:
    terms = scoring_terms(query)
    scored: list[RetrievalCandidate] = []
    for path in root.rglob("*.md"):
        candidate = RetrievalCandidate(path=path, corpus_id=corpus_id, scores=score_path(root, path, query))
        if candidate.total_score:
            scored.append(candidate)
        if len(scored) >= limit * 20:
            break
    scored.sort(key=lambda item: (-item.total_score, str(item.path)))

    results = []
    seen = set()
    for candidate in scored:
        rel_path = str(candidate.path.relative_to(ROOT)).replace("\\", "/")
        if rel_path.lower() in seen:
            continue
        seen.add(rel_path.lower())
        results.append(
            {
                "path": rel_path,
                "corpus_id": candidate.corpus_id,
                "relevance": "medium" if candidate.total_score < 12 else "high",
                "why": candidate.reason(),
                "scores": asdict(candidate)["scores"],
                "snippet": snippet(candidate.path, terms),
            }
        )
        if len(results) >= limit:
            break
    return results


def vector_warning(mode: str) -> str | None:
    if mode == "lexical":
        return None
    return "Vector retrieval requested but unavailable; degraded to lexical retrieval."


def build_pack(query: str, limit: int, mode: str = "lexical") -> tuple[dict, list[dict]]:
    query_route = route(query)
    corpora = corpus_by_id()
    sources: list[dict] = []
    warnings: list[str] = []
    warning = vector_warning(mode)
    if warning:
        warnings.append(warning)

    for corpus_id in query_route["selected_corpora"]:
        corpus = corpora.get(corpus_id, {})
        root_path = corpus.get("root_path")
        if not root_path:
            warnings.append(f"{corpus_id} has no local root_path yet.")
            continue
        root = ROOT / root_path
        if not root.exists():
            warnings.append(f"{corpus_id} root_path does not exist: {root_path}")
            continue
        for source in search_markdown(root, query, limit - len(sources), corpus_id):
            sources.append(source)
            if len(sources) >= limit:
                break

    quality = {
        "confidence": "medium" if sources else "low",
        "ambiguity": "low" if not query_route.get("clarification_needed") else "high",
        "coverage": "partial" if sources else "none",
    }
    frontmatter = {
        "id": "context-pack-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
        "query": query,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "client": "codex",
        "corpus": {
            "selected": query_route["selected_corpora"],
            "excluded": query_route["excluded_corpora"],
            "route_reason": query_route.get("clarification_needed") or "Route selected by query router.",
        },
        "limits": {"requested_sources": limit, "applied_sources": len(sources)},
        "retrieval": {
            "mode": "lexical" if not warning else "degraded",
            "requested_mode": mode,
            "lexical_enabled": True,
            "vector_enabled": False,
        },
        "quality": quality,
        "status": "generated",
    }
    body = {
        "route": query_route,
        "sources": sources,
        "warnings": warnings,
    }
    return frontmatter, [body]


def build_pack_from_context_result(context: dict, limit: int = 12) -> tuple[dict, list[dict]]:
    """Build an audit context pack from a unified runtime context result."""
    applied_limit = max(1, min(int(limit), 20))
    route_data = context.get("route") or {}
    knowledge = context.get("knowledge_hits") or []
    sources = []
    for hit in knowledge[:applied_limit]:
        score = hit.get("score")
        vector_score = int(score * 100) if isinstance(score, (int, float)) else 0
        sources.append(
            {
                "path": hit.get("source", "runtime"),
                "corpus_id": hit.get("corpus_id", "unknown"),
                "relevance": "high" if vector_score >= 80 else "medium",
                "why": "Runtime-backed knowledge hit.",
                "scores": {"path": 0, "phrase": 0, "symbol": 0, "vector": vector_score},
                "snippet": hit.get("snippet", ""),
            }
        )

    warnings = list(context.get("warnings") or [])
    if not sources:
        warnings.append("Runtime context returned no knowledge sources.")

    frontmatter = {
        "id": "context-pack-" + datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S"),
        "trace_id": context.get("trace_id"),
        "query": context.get("query", ""),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "client": "codex",
        "corpus": {
            "selected": context.get("selected_corpora", []),
            "excluded": context.get("excluded_corpora", []),
            "route_reason": route_data.get("clarification_needed") or "Route selected by unified runtime.",
        },
        "limits": {"requested_sources": limit, "applied_sources": len(sources)},
        "retrieval": {
            "mode": "runtime",
            "requested_mode": "runtime",
            "lexical_enabled": True,
            "vector_enabled": context.get("quality", {}).get("retrieval_mode") != "lexical",
        },
        "quality": context.get("quality", {"confidence": "low", "coverage": "none"}),
        "status": "generated",
    }
    body = {
        "route": route_data,
        "sources": sources,
        "memory_hits": context.get("memory_hits", []),
        "warnings": warnings,
    }
    return frontmatter, [body]


def render_markdown(frontmatter: dict, body: list[dict]) -> str:
    data = body[0]
    lines = [
        "---",
        yaml.safe_dump(frontmatter, sort_keys=False).strip(),
        "---",
        "",
        "# Context Pack",
        "",
        "## Query Route",
        "",
        "```yaml",
        yaml.safe_dump(data["route"], sort_keys=False).strip(),
        "```",
        "",
        "## Ranked Sources",
        "",
    ]
    if not data["sources"]:
        lines.append("No local sources found for the selected corpus.")
    for idx, source in enumerate(data["sources"], 1):
        lines.extend(
            [
                f"### {idx}. {source['path']}",
                "",
                f"- Corpus: {source['corpus_id']}",
                f"- Relevance: {source['relevance']}",
                f"- Why selected: {source['why']}",
                f"- Scores: {yaml.safe_dump(source['scores'], sort_keys=False).strip()}",
                f"- Snippet: {source['snippet']}",
                "",
            ]
        )
    if data.get("memory_hits"):
        lines.extend(["## Memory Hits", ""])
        for idx, hit in enumerate(data["memory_hits"], 1):
            lines.extend(
                [
                    f"### {idx}. {hit.get('id', 'memory')}",
                    "",
                    f"- Source: {hit.get('source', 'unknown')}",
                    f"- Confidence: {hit.get('confidence', 'unknown')}",
                    f"- Text: {hit.get('text', '')}",
                    "",
                ]
            )
    lines.extend(["## Retrieval Warnings", ""])
    lines.extend(f"- {warning}" for warning in data["warnings"]) if data["warnings"] else lines.append("None.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=12)
    parser.add_argument("--mode", choices=["lexical", "hybrid", "vector"], default="lexical")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    limit = max(1, min(args.limit, 20))
    frontmatter, body = build_pack(args.query, limit, mode=args.mode)
    rendered = render_markdown(frontmatter, body)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
