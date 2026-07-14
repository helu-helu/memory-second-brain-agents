# Contract: Active Memory Pack

## Command

```text
python scripts/build_memory_pack.py "task query" --limit 5 --out second-brain/memory/packs/example.md
```

## Frontmatter

Generated memory packs include:

- `id`
- `query`
- `created_at`
- `client`
- `limits.requested_items`
- `limits.applied_items`
- `quality.confidence`
- `quality.coverage`
- `status`

## Body

The body includes:

- `## Selected Memory`
- one section per selected active memory item
- `## Recall Warnings`

Each selected item includes:

- type
- path
- status
- confidence
- trigger
- reason
- summary

## Rules

- Only `status: active` artifacts may be selected.
- Output item count must not exceed the requested limit.
- No active matches must produce a warning.
