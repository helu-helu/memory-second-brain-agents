# Implementation Plan: Hybrid Retrieval Context Packs

**Branch**: `002-hybrid-retrieval-context-packs` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/002-hybrid-retrieval-context-packs/spec.md`

## Summary

Improve the current context-pack builder from a lexical demo into a hybrid,
version-aware retrieval layer. Keep query routing and corpus registry as the
front door, preserve the context-pack contract, and add eval fixtures so
retrieval quality can be measured before future vector or ranking changes are
accepted.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: Existing FastAPI/LlamaIndex/Qdrant stack, PyYAML,
pytest. No new dependency is required for the MVP.

**Storage**: File-first fixtures and context packs; existing Qdrant index when
vector retrieval is available.

**Testing**: pytest plus a lightweight retrieval eval script.

**Target Platform**: Local Windows development environment with optional Qdrant.

**Project Type**: Local retrieval scripts + existing runtime service.

**Performance Goals**: Default context packs return no more than 12 sources and
complete fast enough for interactive Codex use on representative queries.

**Constraints**: Query routing must happen before retrieval; Unity version
binding must be honored; vector retrieval must degrade gracefully when absent.

**Scale/Scope**: Unity 6.3 is the primary large-corpus target. Codex and missing
corpus cases are included to verify routing and graceful degradation.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Better context packs improve the user's Codex
  workflow first.
- **Provenance and governance**: PASS. Sources retain corpus id, citation path,
  ranking reasons, and quality signals.
- **File-first compatibility**: PASS. Eval fixtures, generated packs, and
  contracts remain file-first.
- **Retrieval quality**: PASS. This feature is explicitly about bounded, ranked,
  measured retrieval.
- **Versioned corpus routing**: PASS. Search only happens after route selection.
- **Script determinism**: PASS. Ranking and eval are deterministic scripts where
  possible.

## Project Structure

### Documentation (this feature)

```text
specs/002-hybrid-retrieval-context-packs/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── retrieval-eval.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
├── build_context_pack.py
├── route_query.py
└── evaluate_retrieval.py

tests/
├── fixtures/
│   └── retrieval_eval.yaml
├── test_build_context_pack.py
└── test_retrieval_eval.py

agent_core/
└── knowledge.py
```

**Structure Decision**: Improve the existing scripts before adding new API/MCP
surface. Keep vector integration behind the same context-pack output.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Optional vector scoring | Existing project already uses Qdrant and user requested vector search | Lexical-only is insufficient for vague or semantic questions |
| Retrieval eval fixtures | Retrieval quality can regress silently | Manual inspection alone is not repeatable |
