# Implementation Plan: Physical Runtime Restructure

**Branch**: `014-physical-runtime-restructure` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/014-physical-runtime-restructure/spec.md`

## Summary

Make the physical project layout match the consolidated architecture without changing behavior. Runtime ownership moves toward package-level boundaries under `agent_core/`, while scripts, API, MCP, and `second-brain/` remain stable access/workspace surfaces. Compatibility shims protect current public imports during migration.

## Technical Context

**Language/Version**: Python project using the currently configured local runtime

**Primary Dependencies**: Existing FastAPI/API layer, MCP bridge, LlamaIndex/Qdrant/Mem0 runtime concepts, pytest

**Storage**: Existing file-first `second-brain/` workspace and existing `db/` local state remain unchanged

**Testing**: pytest focused tests first; full suite after focused tests pass

**Target Platform**: Local Codex/agent development environment with future API/MCP access

**Project Type**: Python runtime plus scripts, API adapter, MCP adapter, and file-first workspace

**Performance Goals**: No new runtime performance target; restructure must not require full-corpus validation

**Constraints**: Preserve imports, REST routes, MCP tool names, `second-brain/`, `db/`, and context-pack behavior

**Scale/Scope**: Current project runtime and tests only; no official-docs crawling or new retrieval feature in this phase

## Constitution Check

- **Personal-first memory**: Pass. The restructure protects the Codex-first personal agent memory runtime before expanding scope.
- **Provenance and governance**: Pass. The feature records root README deletion, expert recommendation, migration decisions, status, and stop rules.
- **File-first compatibility**: Pass. `second-brain/` remains stable and readable as files.
- **Retrieval quality**: Pass. Retrieval behavior is preserved from feature 013; this feature validates bounded context-pack compatibility instead of adding raw search behavior.
- **Versioned corpus routing**: Pass. No corpus routing behavior changes are introduced.
- **Script determinism**: Pass. Scripts remain deterministic wrappers and validation helpers.

## Project Structure

### Documentation (this feature)

```text
specs/014-physical-runtime-restructure/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── migration-map.md
├── contracts/
│   └── import-compatibility.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
agent_core/
├── __init__.py
├── config.py
├── context_contract.py
├── knowledge.py              # future shim to agent_core.rag.knowledge
├── context_builder.py        # future shim to agent_core.context.builder
├── access_tools.py           # future shim to agent_core.access.second_brain
├── memory.py                 # high-risk future move to agent_core/memory/
├── rag/
│   ├── __init__.py
│   ├── knowledge.py
│   └── metadata.py
├── context/
│   ├── __init__.py
│   └── builder.py
├── access/
│   ├── __init__.py
│   └── second_brain.py
└── memory/
    ├── __init__.py
    └── manager.py

api/
└── api_server.py             # adapter entrypoint, stable path

scripts/                      # deterministic wrappers, stable paths

second_brain_mcp.py           # MCP process entrypoint, stable path

second-brain/                 # file-first workspace, stable path

db/                           # generated/local persistence, stable path
```

**Structure Decision**: Move runtime implementation inward under `agent_core/*` packages, but keep adapters and file workspace stable. Old module names become shims and are not deleted in this feature.

## Migration Order

1. Baseline current imports and focused tests.
2. Move RAG/knowledge implementation to `agent_core/rag/knowledge.py`; keep `agent_core/knowledge.py` as shim.
3. Move context builder implementation to `agent_core/context/builder.py`; keep `agent_core/context_builder.py` as shim.
4. Move access tools implementation to `agent_core/access/second_brain.py`; keep `agent_core/access_tools.py` as shim.
5. Optionally extract MCP helper logic to `agent_core/mcp/tools.py`, while keeping `second_brain_mcp.py` as the entrypoint.
6. Move memory last from `agent_core/memory.py` to `agent_core/memory/manager.py` and preserve `agent_core.memory` exports through package `__init__.py`.
7. Update docs/status after tests pass; do not recreate stale README content.

## Stop Rules

- Stop if a restructure requires renaming REST routes or MCP tools.
- Stop if a restructure requires moving `second-brain/` or `db/`.
- Stop if `agent_core.memory` import compatibility cannot be protected by tests.
- Stop if more than three import families outside `agent_core`, `api`, `scripts`, `tests`, and `second_brain_mcp.py` need manual changes.
- Stop before deleting any compatibility shim in feature 014.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
