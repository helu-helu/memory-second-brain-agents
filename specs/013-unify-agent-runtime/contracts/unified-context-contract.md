# Contract: Unified Agent Context

## Purpose

Define the shared behavior that REST, MCP, scripts, and context-pack export must align to after consolidation.

## Operation: route_query

Input:

- `query`: required user query.
- `project_context`: optional project/version hints.

Output:

- `selected_corpora`
- `excluded_corpora`
- `route_confidence`
- `clarification_needed`
- `warnings`

Failure behavior:

- Empty query returns validation error.
- Ambiguous query returns clarification requirement rather than silently choosing unrelated corpora.

## Operation: search_knowledge

Input:

- `query`: required user query.
- `corpus_ids`: optional routed corpus ids.
- `limit`: bounded source count.
- `requires`: optional model capability constraints.

Output:

- `knowledge_hits`: source-ranked snippets with metadata.
- `quality`: confidence and coverage.
- `warnings`: degraded modes or filter effects.

Failure behavior:

- Missing vector index returns a degraded warning.
- No matches returns an explicit empty result, not unrelated lexical results.

## Operation: search_memory

Input:

- `query`: required user query.
- `user_id`: optional user scope.
- `limit`: bounded memory count.

Output:

- `memory_hits`
- `quality`
- `warnings`

Failure behavior:

- Missing memory store returns a degraded warning and an empty memory section.

## Operation: build_context

Input:

- `query`
- `user_id`
- `model_id`
- `corpus_ids`
- `limits`

Output:

- `trace_id`
- `route`
- `memory_hits`
- `knowledge_hits`
- `selected_corpora`
- `excluded_corpora`
- `quality`
- `warnings`
- `prompt_context` or bounded context text

Failure behavior:

- Partial subsystem failure returns a degraded result if at least one subsystem can answer.
- Total failure returns a structured error with no generated context.

## Operation: export_context_pack

Input:

- `UnifiedContextResult`
- `out`: optional output path.

Output:

- `context_pack_path`
- `status`
- `warnings`

Failure behavior:

- Export failure does not change runtime retrieval state.
- Snapshot must label fallback mode clearly.
