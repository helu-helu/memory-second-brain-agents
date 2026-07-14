# Contract: MCP Post-Restructure Validation

## Stable Entrypoint

The MCP server entrypoint remains:

```text
second_brain_mcp.py
```

## Required Tool Surface

The validation must confirm these tool functions are importable:

- `search_knowledge`
- `search_memory`
- `add_memory`
- `search_workflows`
- `convert_docs_to_md`
- `build_massive_index`
- `list_corpora`
- `route_docs_query`
- `build_docs_context_pack`
- `build_unified_context`
- `inspect_corpus_status`
- `build_active_memory_pack`
- `inspect_second_brain_status`
- `build_agent_bootstrap`
- `record_agent_handoff`

## Representative Query

Use this query for the small validation path:

```text
I want to create a separate camera for each user in a Unity 6.3 multiplayer game.
```

## Expected Evidence

Validation must record:

- Check name
- Command or path exercised
- Result
- Whether runtime was mocked or real
- Warnings/blockers
- Follow-up if real-runtime validation is deferred
