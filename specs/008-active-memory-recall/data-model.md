# Data Model: Active Memory Recall

## ActiveMemoryItem

Represents a personal memory artifact eligible for recall.

**Fields**:

- `id`
- `item_type`: lesson, skill
- `path`
- `status`
- `confidence`
- `title_or_name`
- `trigger`
- `summary`
- `score`
- `reason`

**Validation rules**:

- Only `status: active` artifacts are eligible.
- Lessons are read from `second-brain/memory/lessons/*.md`.
- Skills are read from `second-brain/skills/active/*/SKILL.md`.

## MemoryPack

Bounded context artifact for one task query.

**Fields**:

- `id`
- `query`
- `created_at`
- `client`
- `limits`
- `quality`
- `status`
- `selected_memory`
- `warnings`

## RecallQuality

Signals the agent can inspect before relying on the memory pack.

**Fields**:

- `confidence`
- `coverage`
- `selected_count`
- `warnings`
