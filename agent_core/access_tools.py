"""Agent-facing helpers over the file-first second-brain layer."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from scripts.build_context_pack import build_pack, render_markdown
from scripts.build_memory_pack import build_pack as build_memory_pack
from scripts.build_memory_pack import render_markdown as render_memory_pack
from scripts.route_query import REGISTRY, ROOT, load_yaml, route


def response(data: Any = None, warnings: list[str] | None = None, error: str | None = None) -> dict:
    return {"ok": error is None, "data": data if error is None else None, "warnings": warnings or [], "error": error}


def _read_yaml_files(folder: Path) -> list[dict]:
    if not folder.exists():
        return []
    records = []
    for path in sorted(folder.glob("*.yaml")):
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            data["_path"] = str(path.relative_to(ROOT)).replace("\\", "/")
            records.append(data)
        except Exception as exc:
            records.append({"_path": str(path), "_error": str(exc)})
    return records


def list_corpora(status: str | None = None, product: str | None = None) -> dict:
    try:
        corpora = load_yaml(REGISTRY).get("corpora", [])
        if status:
            corpora = [item for item in corpora if item.get("status") == status]
        if product:
            corpora = [item for item in corpora if item.get("product") == product]
        return response(corpora)
    except Exception as exc:
        return response(error=str(exc))


def route_docs_query(query: str) -> dict:
    if not query.strip():
        return response(error="query is required")
    try:
        return response(route(query))
    except Exception as exc:
        return response(error=str(exc))


def build_docs_context_pack(query: str, limit: int = 12, mode: str = "lexical", out: str | None = None) -> dict:
    if not query.strip():
        return response(error="query is required")
    try:
        limit = max(1, min(int(limit), 20))
        out_path = Path(out) if out else ROOT / "second-brain" / "demo" / "runs" / "agent-context-pack.md"
        if not out_path.is_absolute():
            out_path = ROOT / out_path
        frontmatter, body = build_pack(query, limit, mode=mode)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render_markdown(frontmatter, body), encoding="utf-8")
        data = {
            "path": str(out_path.relative_to(ROOT)).replace("\\", "/"),
            "selected_corpora": frontmatter["corpus"]["selected"],
            "applied_sources": frontmatter["limits"]["applied_sources"],
            "retrieval_mode": frontmatter["retrieval"]["mode"],
        }
        return response(data, warnings=body[0]["warnings"])
    except Exception as exc:
        return response(error=str(exc))


def inspect_corpus_status(corpus_id: str) -> dict:
    try:
        registry = load_yaml(REGISTRY).get("corpora", [])
        corpus = next((item for item in registry if item.get("corpus_id") == corpus_id), None)
        if not corpus:
            return response(error=f"{corpus_id}: corpus not registered")

        acquisitions = [item for item in _read_yaml_files(ROOT / "second-brain" / "corpora" / "acquisitions") if item.get("corpus_id") == corpus_id]
        crawl_plans = [item for item in _read_yaml_files(ROOT / "second-brain" / "corpora" / "crawl-plans") if item.get("corpus_id") == corpus_id]
        warnings = []
        root_path = corpus.get("root_path")
        if not root_path:
            warnings.append(f"{corpus_id} has no local root_path")
        elif not (ROOT / root_path).exists():
            warnings.append(f"{corpus_id} root_path does not exist: {root_path}")
        for plan in crawl_plans:
            if plan.get("approval_status") != "approved":
                warnings.append(f"{plan.get('plan_id', 'crawl plan')} is not approved")

        ready = bool(root_path and (ROOT / root_path).exists() and corpus.get("status") in {"available", "indexed"})
        return response(
            {
                "corpus_id": corpus_id,
                "registry": corpus,
                "acquisitions": acquisitions,
                "crawl_plans": crawl_plans,
                "ready_for_retrieval": ready,
            },
            warnings=warnings,
        )
    except Exception as exc:
        return response(error=str(exc))


def build_active_memory_pack(query: str, limit: int = 5, out: str | None = None) -> dict:
    if not query.strip():
        return response(error="query is required")
    try:
        limit = max(1, min(int(limit), 20))
        out_path = Path(out) if out else ROOT / "second-brain" / "memory" / "packs" / "agent-memory-pack.md"
        if not out_path.is_absolute():
            out_path = ROOT / out_path
        frontmatter, body = build_memory_pack(query, root=ROOT / "second-brain", limit=limit)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render_memory_pack(frontmatter, body), encoding="utf-8")
        data = {
            "path": str(out_path.relative_to(ROOT)).replace("\\", "/"),
            "applied_items": frontmatter["limits"]["applied_items"],
            "quality": frontmatter["quality"],
        }
        return response(data, warnings=body["warnings"])
    except Exception as exc:
        return response(error=str(exc))
