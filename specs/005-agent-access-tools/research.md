# Research: Agent Access Tools

## Decision: Add a helper layer before MCP/API wrappers

**Rationale**: A helper module can be tested directly and reused by both FastAPI
and MCP without copying logic.

**Alternatives considered**:

- Add only MCP tools: rejected because API clients would duplicate behavior.
- Add only FastAPI endpoints: rejected because MCP would still need wrappers.

## Decision: Tools inspect status, not mutate reviewed memory

**Rationale**: Corpus/context access is safe. Memory/skill promotion requires
review and should not be hidden behind simple agent tools.

**Alternatives considered**:

- Let agents promote artifacts directly: rejected because it violates
  governance.

## Decision: Preserve existing MCP tools

**Rationale**: Existing `second_brain_mcp.py` exposes memory/RAG/admin workflows.
New tools should be additive.

**Alternatives considered**:

- Rewrite MCP bridge: rejected because the runtime plane is already working.
