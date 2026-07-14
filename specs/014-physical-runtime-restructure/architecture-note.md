# Architecture Note: Runtime Package Ownership

Feature 014 makes the physical package layout match the consolidated runtime direction from feature 013.

## Current Source Of Truth

- `agent_core/rag/` owns RAG and `KnowledgeBase`.
- `agent_core/context/` owns context building and `ContextBuilder`.
- `agent_core/access/` owns second-brain access helper functions.
- `agent_core/memory/` owns Mem0-backed `MemoryManager`.
- `agent_core/mcp/` is reserved for future helper extraction only.
- `api/api_server.py` remains the REST adapter.
- `second_brain_mcp.py` remains the MCP process entrypoint.
- `scripts/` remains deterministic wrappers and operational helpers.
- `second-brain/` remains the file-first workspace.
- `db/` remains generated/local persistence.

## Compatibility Policy

These legacy module paths are compatibility shims and must not be deleted in feature 014:

- `agent_core.knowledge`
- `agent_core.context_builder`
- `agent_core.access_tools`

The public `agent_core.memory` import path is preserved by the new package itself.

## What Did Not Change

- REST route names did not change.
- MCP tool names did not change.
- `second-brain/` and `db/` did not move.
- Retrieval behavior did not change.
- Full official-docs corpus scans are not part of restructure validation.
