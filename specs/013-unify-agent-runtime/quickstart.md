# Quickstart: Unify Agent Runtime Validation

## Prerequisites

- Project virtualenv is available.
- Local API config is present.
- Qdrant/Mem0/model provider availability may vary; degraded behavior is acceptable only when explicit warnings are returned.

## Validation Scenario 1: Capability Map Exists

Expected outcome:

- Specs 001-012 are classified as reuse, extend, replace, or drop.
- No duplicate capability lacks an owner.

## Validation Scenario 2: API Uses Runtime Path

Run representative API checks for:

- knowledge search
- memory search
- context build
- second-brain context-pack export

Expected outcome:

- Knowledge and memory behavior route through the unified runtime.
- Context-pack export is an audit snapshot, not an independent retrieval engine.

## Validation Scenario 3: MCP Uses Same Runtime Behavior

Run MCP smoke checks for:

- `search_knowledge`
- `search_memory`
- `route_docs_query`
- unified context/context-pack behavior after adapter work

Expected outcome:

- MCP and API return equivalent selected sources for the same routed query.
- MCP startup does not corrupt stdio with API logs.

## Validation Scenario 4: Degraded Behavior

Simulate or mock:

- missing Qdrant collection
- unavailable memory store
- ambiguous corpus route
- no matching docs

Expected outcome:

- Each case returns explicit warnings and bounded output.
- No path silently falls back to unrelated lexical matches.

## Validation Scenario 5: Representative Retrieval Matrix

Use at least 20 small representative queries across:

- Unity version-bound docs
- personal memory
- active skills/workflows
- ambiguous corpora
- no-result cases

Expected outcome:

- Routes are correct or request clarification.
- Context output stays within configured limits.
- Sources are inspectable.
