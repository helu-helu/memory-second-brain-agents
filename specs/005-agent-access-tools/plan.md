# Implementation Plan: Agent Access Tools

**Branch**: `005-agent-access-tools` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/005-agent-access-tools/spec.md`

## Summary

Expose the file-first second-brain layer to agents through a small callable
access layer. The MVP should reuse existing scripts for listing corpora, routing
queries, building context packs, and inspecting acquisition/crawl status. API or
MCP wrappers can call this layer without moving ownership away from files.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: Existing project dependencies, PyYAML, pytest. No new
dependencies required.

**Storage**: Existing file-first artifacts under `second-brain/`.

**Testing**: pytest.

**Target Platform**: Local Windows development environment and existing MCP/API
bridge.

**Project Type**: Local helper module + optional API/MCP wrapper integration.

**Performance Goals**: Access calls return quickly for registry/routing and stay
bounded for context-pack generation.

**Constraints**: Preserve existing MCP tools, no live scraping during retrieval,
no auto-promotion of memory/skills.

**Scale/Scope**: MVP exposes helper functions and tests them. API/MCP endpoint
decorators may be added only if they are thin wrappers.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Agent access improves the user's own connected
  agents first.
- **Provenance and governance**: PASS. Tools surface status and provenance
  rather than bypassing them.
- **File-first compatibility**: PASS. Files remain source of truth.
- **Retrieval quality**: PASS. Context packs remain bounded and cited.
- **Versioned corpus routing**: PASS. Route-query remains the gateway.
- **Script determinism**: PASS. Access layer reuses deterministic scripts.

## Project Structure

### Documentation (this feature)

```text
specs/005-agent-access-tools/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── agent-tools.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
agent_core/
└── access_tools.py

api/
└── api_server.py

second_brain_mcp.py
tests/
└── test_access_tools.py
```

**Structure Decision**: Add `agent_core/access_tools.py` as the reusable boundary.
FastAPI and MCP wrappers should be thin if added.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Helper layer before direct MCP edits | Avoids duplicating logic in MCP and API wrappers | Direct wrapper-only implementation would be harder to test and reuse |
