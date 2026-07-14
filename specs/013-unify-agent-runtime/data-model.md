# Data Model: Unify Agent Runtime

## RuntimeCapability

Represents an existing or planned capability in the project.

Fields:

- `id`: stable capability identifier.
- `name`: human-readable capability name.
- `current_paths`: files or endpoints currently implementing it.
- `category`: memory, knowledge, context, corpus, API, MCP, script, dashboard, test.
- `owner`: selected source of truth after consolidation.
- `disposition`: reuse, extend, replace, drop, deprecate, fallback-only.
- `notes`: rationale and migration notes.

Validation:

- Each capability MUST have exactly one owner.
- Each capability MUST have one disposition.
- Capabilities with duplicate implementations MUST identify the retained runtime path.

## UnifiedContextResult

Represents the agent-facing result for a query.

Fields:

- `trace_id`
- `query`
- `route`
- `selected_corpora`
- `excluded_corpora`
- `memory_hits`
- `knowledge_hits`
- `quality`
- `warnings`
- `context_pack_path`
- `created_at`

Validation:

- Results MUST be bounded by configured source limits.
- Warnings MUST be explicit when any subsystem degrades.
- Source hits MUST include provenance enough for an agent/user to inspect the source.

## ContextPackSnapshot

Represents a Markdown/YAML file exported from a runtime result.

Fields:

- frontmatter: trace id, query, route, corpora, quality, limits, status, created time.
- body: ranked sources, memory summary when available, warnings, validation notes.

Validation:

- Snapshot MUST NOT silently invent sources.
- Snapshot MUST identify whether results came from vector/model retrieval or lexical fallback.

## IntegrationGap

Represents a blocking mismatch discovered during consolidation.

Fields:

- `id`
- `description`
- `affected_capability`
- `severity`: blocking, high, medium, low.
- `decision_required`
- `resolution`
- `status`: open, decided, implemented, deferred.

Validation:

- Code integration MUST NOT begin while more than three blocking/high gaps are undecided.

## SpecMapping

Represents how specs 001-012 map into the unified architecture.

Fields:

- `spec_id`
- `feature_name`
- `mapped_capabilities`
- `disposition`
- `owner`
- `gap`
- `decision`

Validation:

- Every existing spec MUST have one mapping row before cutover tasks begin.
