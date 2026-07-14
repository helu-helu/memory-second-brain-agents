# Codex MCP Setup

## Status

The project MCP bridge is runtime-ready for Phase 1 after installing the `mcp`
Python package.

Validated locally:

```text
import second_brain_mcp -> ok
API_BASE -> http://127.0.0.1:8001
targeted access/API tests -> pass
full test suite -> pass
MCP stdio initialize/list_tools/call_tool -> pass
MCP thin smoke after feature 013 -> pass
Mocked runtime MCP smoke -> pass
```

## Server Command

Use the project virtualenv Python and run the MCP bridge from the project root:

```text
D:\Workspace\Another\Agent\Memory\Memory and Second Brain for Agents\.venv\Scripts\python.exe
```

Arguments:

```text
second_brain_mcp.py
```

Working directory:

```text
D:\Workspace\Another\Agent\Memory\Memory and Second Brain for Agents
```

Environment:

```text
APP_API_KEY=my-super-secret-key-123
SECOND_BRAIN_PRELOAD_KB=0
```

Use your real `APP_API_KEY` value if it differs from local default.

## Phase 1 Tools To Smoke Test

- `inspect_second_brain_status`
- `build_agent_bootstrap`
- `build_active_memory_pack`
- `list_corpora`
- `route_docs_query`
- `build_docs_context_pack`
- `build_unified_context`
- `record_agent_handoff`

Validated MCP tool list includes:

- `search_knowledge`
- `search_memory`
- `add_memory`
- `save_verified_workflow`
- `deprecate_workflow`
- `search_workflows`
- `convert_docs_to_md`
- `build_massive_index`
- `open_dashboard`
- `list_corpora`
- `route_docs_query`
- `build_docs_context_pack`
- `build_unified_context`
- `inspect_corpus_status`
- `build_active_memory_pack`
- `inspect_second_brain_status`
- `build_agent_bootstrap`
- `record_agent_handoff`

## Notes

- The MCP bridge auto-starts the REST API on `127.0.0.1:8001` if it is not
  already running.
- `SECOND_BRAIN_PRELOAD_KB=0` keeps startup fast for file-first tools. RAG search
  can still load the knowledge base on demand.
- Full Qdrant/RAG readiness is separate from file-first second-brain readiness.
- Feature 013 adds `build_unified_context` as the MCP/API-facing runtime context
  contract path. `build_docs_context_pack` defaults to runtime mode for MCP, but
  `mode="lexical"` remains available as an explicit fallback/audit smoke path.
- Runtime-heavy MCP smoke can load Qdrant, embeddings, Mem0, and model providers;
  use small representative tests or mocks before full local runtime validation.
- `tests/test_mcp_runtime_smoke.py` is the small mocked runtime smoke for route,
  knowledge search, memory search, unified context, and context-pack export.
