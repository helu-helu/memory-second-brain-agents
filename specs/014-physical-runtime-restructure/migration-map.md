# Migration Map: Physical Runtime Restructure

## Current Import Surface

Observed public/internal import families:

- `agent_core.memory`
- `agent_core.knowledge`
- `agent_core.context_builder`
- `agent_core.access_tools`
- `agent_core.context_contract`
- `agent_core.config`
- `agent_core` package exports

## Target Paths

| Current path | Target path | Risk | Feature 014 action | Validation |
|--------------|-------------|------|--------------------|------------|
| `agent_core.knowledge` | `agent_core.rag.knowledge` | Medium | Implemented: moved implementation, kept alias shim | `tests/test_knowledge.py`, import smoke |
| `agent_core.context_builder` | `agent_core.context.builder` | Medium | Implemented: moved implementation, kept alias shim | `tests/test_context_contract.py`, `tests/test_runtime_context_pack.py` |
| `agent_core.access_tools` | `agent_core.access.second_brain` | Medium | Implemented: moved implementation, kept alias shim | `tests/test_access_tools.py`, API/MCP smoke |
| `agent_core.memory` | `agent_core.memory.manager` via package | High | Implemented last: package exports `MemoryManager` at `agent_core.memory` | `tests/test_memory.py`, package import smoke |
| `second_brain_mcp.py` | optional helper import from `agent_core.mcp.tools` | Low | Kept top-level entrypoint stable; helper extraction deferred | MCP import smoke |
| `second-brain/` | unchanged | High if moved | Do not move | Path existence and script tests |
| `db/` | unchanged | Medium if moved | Do not move | Existing tests only |

## Package Skeleton Status

- `agent_core/rag/`: active package; owns `KnowledgeBase` implementation.
- `agent_core/context/`: active package; owns `ContextBuilder` implementation.
- `agent_core/access/`: active package; owns second-brain access helper implementation.
- `agent_core/memory/`: active package; owns `MemoryManager` implementation.
- `agent_core/mcp/`: reserved helper package; no tool extraction performed in this feature.

## Deprecated Paths For One Feature Cycle

These paths may become shims, but must not be deleted in feature 014:

- `agent_core/knowledge.py`
- `agent_core/context_builder.py`
- `agent_core/access_tools.py`

The `agent_core.memory` import path is not deprecated because it is public. Its implementation file was replaced by a package with equivalent exports.

The shim files use module aliasing instead of star re-exports so existing monkeypatch and runtime callers touching legacy module globals still affect the new implementation module.

## Root README Status

The root `README.md` was removed intentionally before this feature so stale architecture notes no longer anchor future agents. A new README or ADR should be written only after the physical structure is implemented and validated.
