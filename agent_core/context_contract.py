"""Unified context result helpers for API, MCP, and context-pack exports."""

from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4


NO_KNOWLEDGE_MARKERS = (
    "(Knowledge Base is not loaded)",
    "(No matching documentation found)",
    "(Matching documentation found but filtered out",
    "(RAG Search Error:",
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _memory_hit(item: dict | str, index: int) -> dict:
    if isinstance(item, dict):
        text = item.get("memory") or item.get("text") or str(item)
        return {
            "id": str(item.get("id") or f"memory-{index}"),
            "source": str(item.get("source") or item.get("_path") or "mem0"),
            "confidence": item.get("confidence", "unknown"),
            "text": text,
        }
    return {"id": f"memory-{index}", "source": "mem0", "confidence": "unknown", "text": str(item)}


def memory_hits(items: list[dict] | None) -> list[dict]:
    return [_memory_hit(item, index) for index, item in enumerate(items or [], 1)]


def knowledge_hits(text: str | None) -> tuple[list[dict], list[str]]:
    if not text:
        return [], ["Knowledge retrieval returned no content."]
    for marker in NO_KNOWLEDGE_MARKERS:
        if text.startswith(marker):
            return [], [text]

    hits = []
    parts = text.split("\n\n---\n\n")
    for index, part in enumerate(parts, 1):
        source = "runtime"
        snippet = part.strip()
        if part.startswith("[Source: "):
            end = part.find("]")
            if end != -1:
                source = part[len("[Source: ") : end]
                snippet = part[end + 1 :].strip()
        hits.append(
            {
                "id": f"knowledge-{index}",
                "source": source,
                "corpus_id": "unknown",
                "score": None,
                "snippet": snippet[:1000],
            }
        )
    return hits, []


def build_unified_context_result(
    *,
    query: str,
    route: dict | None = None,
    memories: list[dict] | None = None,
    knowledge_text: str | None = None,
    prompt_context: str | None = None,
    warnings: list[str] | None = None,
    context_pack_path: str | None = None,
    retrieval_mode: str = "runtime",
) -> dict:
    route = route or {}
    memory = memory_hits(memories)
    knowledge, knowledge_warnings = knowledge_hits(knowledge_text)
    all_warnings = list(warnings or []) + knowledge_warnings
    confidence = "high" if knowledge else "medium" if memory else "low"
    coverage = "partial" if memory or knowledge else "none"

    return {
        "trace_id": f"ctx-{uuid4().hex[:12]}",
        "query": query,
        "route": route,
        "selected_corpora": route.get("selected_corpora", []),
        "excluded_corpora": route.get("excluded_corpora", []),
        "memory_hits": memory,
        "knowledge_hits": knowledge,
        "quality": {
            "confidence": confidence,
            "coverage": coverage,
            "retrieval_mode": retrieval_mode,
        },
        "warnings": all_warnings,
        "context_pack_path": context_pack_path,
        "prompt_context": prompt_context,
        "created_at": _now(),
    }
