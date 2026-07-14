# Implementation Plan: Unify Agent Runtime

**Branch**: `013-unify-agent-runtime` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/013-unify-agent-runtime/spec.md`

## Summary

Unify the original `agent_core` runtime and the newer file-first `second-brain` layer into one project direction. The plan keeps `agent_core` as the runtime source of truth for memory, knowledge retrieval, context building, and model routing, while `second-brain/` remains the file-first workspace for corpus registry, review lifecycle, skills, memory artifacts, handoffs, and audit snapshots.

## Technical Context

**Language/Version**: Python project using the existing local virtualenv

**Primary Dependencies**: FastAPI, MCP Python SDK, LlamaIndex, Qdrant client, Mem0, HuggingFace embeddings, pytest

**Storage**: File-first Markdown/YAML artifacts, Qdrant collections, Mem0 backing store, local DB/config files

**Testing**: pytest with small representative fixtures and MCP/API smoke tests

**Target Platform**: Local Windows development environment with future API/MCP clients

**Project Type**: Agent memory/RAG service with CLI, REST API, and MCP access paths

**Performance Goals**: Routine validation must avoid full-corpus scans; runtime queries should return bounded context suitable for agent use

**Constraints**: No full Unity corpus processing in unit tests; no duplicate production retrieval engines; preserve current MCP/API usability during cutover

**Scale/Scope**: Existing project with 39,000+ Unity Markdown docs plus future Unity, Python, TypeScript, Codex/OpenAI, and other corpora

## Constitution Check

- **Personal-first memory**: PASS. The feature improves the user's agent experience by removing competing memory/retrieval paths.
- **Provenance and governance**: PASS. Context packs remain audit snapshots with trace, source, status, confidence, and scope metadata.
- **File-first compatibility**: PASS. `second-brain/` stays readable and editable as files while runtime calls move through `agent_core`.
- **Retrieval quality**: PASS. Runtime retrieval uses model/vector-backed paths first, with lexical only as fallback/audit.
- **Versioned corpus routing**: PASS. Corpus registry remains required before retrieval and selected/excluded corpora stay in the context contract.
- **Script determinism**: PASS. Deterministic scripts remain wrappers/exporters/validators rather than repeated agent reasoning.

## Project Structure

### Documentation (this feature)

```text
specs/013-unify-agent-runtime/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── unified-context-contract.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code (repository root)

```text
agent_core/                 # Runtime source of truth for memory, RAG, context, model routing
api/                        # FastAPI access layer wrapping agent_core behavior
second_brain_mcp.py         # MCP bridge wrapping API/runtime behavior
scripts/                    # Thin CLI wrappers, deterministic import/export/validation helpers
second-brain/               # File-first data, review, audit, corpus, memory, skills workspace
docs/                       # Official docs and workflow sources to index
db/                         # Local vector/memory persistence and generated DB state
tests/                      # Unit, API, MCP, and representative retrieval validation
specs/                      # Spec-kit history and implementation plans
```

**Structure Decision**: Do not split into a second project. Consolidate into one runtime with `agent_core` as execution owner and `second-brain/` as governed file workspace.

## Phase Khởi Đầu: Contract-First Consolidation

Goal: freeze architecture before code integration.

Exit criteria:

- Specs 001-012 are mapped to reuse, extend, replace, or drop.
- Every runtime capability has one owner.
- The unified context contract is accepted as the REST/MCP/script target.
- No implementation begins if more than three integration gaps lack a decision.

## Phase Hoàn Thành: Unified Runtime Cutover

Goal: prove the file-first layer uses the runtime instead of competing with it.

Exit criteria:

- A representative end-to-end path passes: source/corpus -> runtime retrieval -> memory/context -> API/MCP -> context-pack snapshot.
- API and MCP use the same core behavior for equivalent operations.
- Duplicate lexical/manual production paths are deprecated, unreachable, or rewritten as runtime-backed adapters.
- Regression tests for memory, knowledge, API, MCP smoke, and context packs pass on representative data.

## Complexity Tracking

No constitution violations are planned.
