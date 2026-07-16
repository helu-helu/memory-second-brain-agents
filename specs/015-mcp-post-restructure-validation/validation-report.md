# Validation Report: MCP Post-Restructure Validation

**Status**: Mocked MCP ready; real-runtime smoke degraded with bounded timeout

## Checks

| Check | Mode | Result | Notes |
|-------|------|--------|-------|
| MCP import/tool surface | Mocked/import | Passed | `pytest tests/test_import_compatibility.py tests/test_mcp_runtime_smoke.py -q` -> 5 passed |
| Mocked runtime MCP smoke | Mocked API session | Passed | Representative Unity 6.3 multiplayer camera query routes to Unity 6.3 and returns runtime context/context-pack contract |
| Representative Unity 6.3 query | Real local runtime | Degraded, bounded | Initial direct MCP function smoke timed out after ~90 seconds; API now returns `504 Runtime context build timed out` after 20 seconds while keeping lightweight routes responsive |
| Full pytest gate | Local tests | Passed | `pytest -q` -> 101 passed |

## Blockers

- Real-runtime `/context/build` depends on loading/searching the RAG runtime and may exceed the bounded 20 second smoke window.
- Treat full runtime validation as an operational check. Retry with explicit user approval for a longer runtime-heavy run that may load Qdrant, embeddings, Mem0, and model providers.
- Lightweight route and lexical context-pack paths remain responsive when runtime context times out.

## Representative Query

```text
I want to create a separate camera for each user in a Unity 6.3 multiplayer game.
```

## Stop-Rule Confirmation

- MCP tool names were not renamed.
- REST routes were not renamed.
- `second-brain/` and `db/` were not moved.
- No full official-docs corpus scan was used.
- Runtime context timeout is bounded by `SECOND_BRAIN_RUNTIME_CONTEXT_TIMEOUT` and defaults to 20 seconds.
