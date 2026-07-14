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
- `record_agent_handoff`

## Notes

- The MCP bridge auto-starts the REST API on `127.0.0.1:8001` if it is not
  already running.
- `SECOND_BRAIN_PRELOAD_KB=0` keeps startup fast for file-first tools. RAG search
  can still load the knowledge base on demand.
- Full Qdrant/RAG readiness is separate from file-first second-brain readiness.
