# Research: Physical Runtime Restructure

## Decision: Create feature 014 instead of expanding feature 013

**Rationale**: Feature 013 completed contract-first consolidation and runtime-backed context-pack behavior. Physical package movement is a different risk profile and should have its own stop rules, migration map, and compatibility checks.

**Alternatives considered**:

- Reopen feature 013: rejected because it would mix completed behavior changes with structural movement.
- Move code immediately after deleting README: rejected because the current import surface includes a high-risk `agent_core.memory` file-to-package conversion.

## Decision: Keep `second-brain/` as the file-first workspace

**Rationale**: The folder already acts as the governed workspace for registry, review, generated artifacts, audit, and file-first second brain state. Moving it to `data/second-brain` would create churn without improving agent-facing behavior.

**Alternatives considered**:

- Move to `data/second-brain`: rejected because it would break existing scripts/spec paths and add low-value migration work.
- Split generated files into multiple top-level folders now: rejected because this feature is about runtime package clarity, not storage redesign.

## Decision: Move runtime code into packages with compatibility shims

**Rationale**: The target runtime layout should make ownership legible: `agent_core/rag`, `agent_core/context`, `agent_core/access`, and later `agent_core/memory`. Existing public imports must continue to work through shims.

**Alternatives considered**:

- Rename modules without shims: rejected because Codex/MCP/API scripts and tests already use current public paths.
- Leave all modules flat: rejected because it preserves the ambiguity that caused this correction.

## Decision: Migrate `agent_core.memory` last

**Rationale**: Python cannot keep both `agent_core/memory.py` and `agent_core/memory/` as equivalent import targets. This move should happen after lower-risk module shims are established and import compatibility tests exist.

**Alternatives considered**:

- Move memory first: rejected because it carries the highest import breakage risk.
- Avoid moving memory forever: rejected as a final target, but acceptable to defer until shims and tests are ready.

## Decision: Preserve adapter entrypoints

**Rationale**: `api/api_server.py`, `second_brain_mcp.py`, and `scripts/` are already part of the user and agent access surface. They can import clearer runtime packages without becoming runtime owners.

**Alternatives considered**:

- Move MCP entrypoint under `agent_core/mcp` immediately: rejected because MCP process configuration often expects a top-level script.
- Move scripts into runtime packages: rejected because deterministic scripts are wrappers/exporters, not owners of core memory/RAG behavior.

## Expert Recommendation Summary

A software architecture review recommended this target:

```text
agent_core/
  rag/knowledge.py
  memory/manager.py
  context/builder.py
  access/second_brain.py
  mcp/tools.py
api/api_server.py
scripts/
second_brain_mcp.py
second-brain/
db/
```

The review explicitly advised keeping `second-brain/`, preserving top-level MCP entrypoint behavior, and treating old `agent_core.knowledge`, `agent_core.context_builder`, and `agent_core.access_tools` as shims for at least one feature cycle.
