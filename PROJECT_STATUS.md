# Project Status

## Phase 1 Status

Phase 1 is complete as an end-to-end MVP for a personal, file-first second brain
for agents.

Implemented flow:

1. Register official documentation corpora.
2. Route documentation queries to the intended corpus/version.
3. Build bounded documentation context packs.
4. Extract candidate lessons and skill candidates from evidence.
5. Review, approve, reject, and activate candidates with audit records.
6. Build bounded active personal memory packs.
7. Expose docs, memory, status, bootstrap, and handoff actions through script/API/MCP paths.
8. Record agent handoffs as future extraction evidence.

Current spec-kit coverage:

- `001-agent-experience-layer`
- `002-hybrid-retrieval-context-packs`
- `003-official-docs-acquisition`
- `004-official-docs-crawler`
- `005-agent-access-tools`
- `006-experience-extraction`
- `007-candidate-review-workflow`
- `008-active-memory-recall`
- `009-agent-memory-access`
- `010-second-brain-status`
- `011-agent-bootstrap-context`
- `012-agent-handoff-records`
- `013-unify-agent-runtime`

Specs 001-012 are complete. Spec 013 is active and in progress.

## Active Next Phase

Feature `013-unify-agent-runtime` is the active Phase 2 preparation track.

Decision:

- Merge the original runtime and the file-first second-brain layer into one project.
- Treat `agent_core` as the runtime source of truth for memory, knowledge retrieval, context building, and model routing.
- Treat `second-brain/` as the file-first data, audit, review, corpus, skills, and spec workspace.
- Do not continue building an independent lexical/manual retrieval runtime in parallel with LlamaIndex/Qdrant/Mem0.

Start rule:

- Begin with the contract-first consolidation tasks in `specs/013-unify-agent-runtime/tasks.md`.
- Do not delete duplicate paths until a replacement runtime-backed path is documented and tested.

## Validation

Latest validation:

```text
97 passed
MCP stdio smoke test passed
tests/test_unified_context_contract.py -> 4 passed
Focused 013 tests -> 40 passed
Focused memory/knowledge/API/context-pack tests -> 51 passed
MCP thin smoke -> 18 tools, route OK, lexical context-pack export OK
Mocked runtime MCP smoke -> pass
```

The test suite is warning-free.

Testing policy:

- Use small representative fixtures by default.
- Do not scan full official docs corpora in unit tests.
- Treat full-corpus validation as an explicit operational check.
- Treat runtime-heavy MCP validation as an explicit operational check because it
  may load Qdrant, embeddings, Mem0, and model providers.

## Stop Rule

Do not automatically add new product features after Phase 1. The selected Phase
2 work is consolidation only: unify runtime ownership, contracts, API/MCP
behavior, and context-pack export paths.

See `MVP_BOUNDARY_AND_ROADMAP.md` for Phase 2 options.
