# Implementation Plan: Versioned Official Docs Agent Experience Layer

**Branch**: `001-agent-experience-layer` | **Date**: 2026-07-13 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/001-agent-experience-layer/spec.md`

## Summary

Build the spec-kit-governed path for a file-first personal agent experience
layer backed by a versioned official documentation registry. The MVP uses Unity
6.3 as the first immutable corpus, adds placeholders for Unity 6.5, Python,
TypeScript, and Codex/OpenAI docs, routes queries to the right corpus/version,
and exposes bounded context packs for Codex before adding broader API/MCP
wrappers.

## Technical Context

**Language/Version**: Python 3.10+ project

**Primary Dependencies**: FastAPI, LlamaIndex, Qdrant, Mem0, existing MCP bridge,
MarkItDown as upstream conversion tool

**Storage**: File-first artifacts for corpus registry, schemas, memory, and
skills; SQLite manifest for ingestion checkpoints; Qdrant for vector retrieval

**Testing**: pytest plus script-level validation commands and representative
retrieval queries

**Target Platform**: Local-first Windows development environment with self-hosted
services

**Project Type**: Local service + scripts + MCP bridge

**Performance Goals**: Representative Unity queries return bounded context packs
quickly enough for interactive agent work; large corpus indexing is resumable

**Constraints**: Unity corpus contains 39,056 Markdown files; source docs are
immutable for Unity 6.3; artifacts must remain human-readable and git-reviewable

**Scale/Scope**: Personal-first memory, multiple official docs corpora, Codex as
the first agent client and corpus, future API/MCP access using the same contracts

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. The MVP optimizes for the user's own Codex
  workflow and project-bound doc versions before team/public sharing.
- **Provenance and governance**: PASS. Source documents, lessons, and skills all
  require status, confidence, source, and scope fields.
- **File-first compatibility**: PASS. Durable artifacts are Markdown/YAML files
  with schemas and can be wrapped later.
- **Retrieval quality**: PASS. The core demo is version-aware routing plus a
  bounded context pack with ranked sources and quality signals.
- **Script determinism**: PASS. Conversion validation, schema checks, indexing,
  and context-pack assembly are assigned to scripts.

## Project Structure

### Documentation (this feature)

```text
specs/001-agent-experience-layer/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── context-pack.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
schemas/                    # File-first YAML schemas for durable artifacts
second-brain/               # Future governed file-first memory workspace
  corpora/
  inbox/
  sources/
  memory/
  skills/
  indexes/
  demo/
scripts/                    # Deterministic helpers for validation/index/context packs
docs/massive/Unity_6_3_Markdown/
                            # Immutable Unity 6.3 Markdown demo corpus
agent_core/                 # Existing memory/retrieval services
api/                        # Existing FastAPI service
second_brain_mcp.py         # Existing MCP bridge for Codex/agent clients
tests/                      # Validation and retrieval quality tests
```

**Structure Decision**: Add a file-first corpus registry, schemas, and artifact
directories beside the existing service implementation. Do not move the Unity
corpus or rewrite the current API/MCP bridge during the setup phase.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Vector search in MVP planning | User asked to include vector search if reasonable, and the repo already uses Qdrant | Lexical-only retrieval is simpler but weaker for vague user questions and intent recognition |
| API/MCP future contract in file-first MVP | Prevents schema redesign when other agents connect later | Pure local files alone would not prove agent-access readiness |
| Multi-corpus registry before all ingestion scripts exist | Needed to avoid baking Unity-only assumptions into the project | A Unity-only MVP would be faster but would need redesign for Python, TypeScript, and Codex docs |
