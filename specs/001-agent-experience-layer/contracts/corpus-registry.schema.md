# Contract: Corpus Registry

The corpus registry is the file-first source of truth for official documentation
collections that agents may retrieve from.

## Registry Location

```text
second-brain/corpora/registry.yaml
```

## Example

```yaml
corpora:
  - corpus_id: unity-6.3
    category: engines
    vendor: Unity
    product: Unity
    version: "6.3"
    authority_level: official
    mutability: immutable
    update_policy: fixed_snapshot
    snapshot_date: null
    refresh_cadence: none
    root_path: docs/massive/Unity_6_3_Markdown
    acquisition: manual
    status: available
    default_for:
      - unity-projects-using-6.3

  - corpus_id: unity-6.5
    category: engines
    vendor: Unity
    product: Unity
    version: "6.5"
    authority_level: official
    mutability: immutable
    update_policy: fixed_snapshot
    snapshot_date: null
    refresh_cadence: none
    root_path: null
    acquisition: manual
    status: planned

  - corpus_id: codex-docs-2026-07-13
    category: agent_platforms
    vendor: OpenAI
    product: Codex
    version: snapshot-2026-07-13
    authority_level: official
    mutability: refreshable
    update_policy: refreshable_snapshot
    snapshot_date: "2026-07-13"
    refresh_cadence: manual
    root_path: null
    acquisition: crawl
    status: planned
```

## Required Fields

- `corpus_id`
- `category`
- `vendor`
- `product`
- `version`
- `authority_level`
- `mutability`
- `update_policy`
- `refresh_cadence`
- `acquisition`
- `status`

## Routing Rules

- Unity queries MUST prefer the project-bound Unity version.
- Unity queries MUST NOT silently substitute Unity 6.5 docs for Unity 6.3
  projects.
- Refreshable snapshots MUST include `snapshot_date`.
- Queries about Codex customization, skills, plugins, MCP, permissions, or
  Codex surfaces route to `agent_platforms/openai_codex`.
- Language questions route to language corpora unless the query explicitly asks
  about an agent workflow or project tool.
