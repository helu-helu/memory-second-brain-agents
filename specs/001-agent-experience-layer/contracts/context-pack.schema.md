# Contract: Retrieval Context Pack

This contract defines the file-first payload that Codex uses now and future
MCP/API wrappers can expose later.

## ContextPack Markdown Shape

```markdown
---
id: context-pack-20260713-001
query: "How should I implement input handling in Unity 6.3?"
created_at: "2026-07-13T00:00:00+07:00"
client: codex
corpus:
  selected:
    - unity-6.3
  excluded:
    - unity-6.5
  route_reason: "Project binding requires Unity 6.3."
limits:
  requested_sources: 12
  applied_sources: 10
retrieval:
  mode: hybrid
  lexical_enabled: true
  vector_enabled: true
quality:
  confidence: medium
  ambiguity: low
  coverage: partial
status: generated
---

# Context Pack

## Detected Intent

how_to

## Clarification Needed

None.

## Ranked Sources

### 1. Input System overview

- Path: docs/massive/Unity_6_3_Markdown/...
- Source type: official_docs
- Relevance: high
- Why selected: Matches query intent and Unity 6.3 scope.
- Snippet: ...

## Relevant Memory

- lesson-id: ...

## Retrieval Warnings

- ...
```

## Required Fields

- `id`
- `query`
- `created_at`
- `client`
- `corpus.product`
- `corpus.selected`
- `limits.requested_sources`
- `limits.applied_sources`
- `retrieval.mode`
- `quality.confidence`
- `quality.ambiguity`
- `status`
- at least one ranked source or one clarification-needed entry

## Quality Rules

- Default context packs SHOULD include 8 to 12 primary sources for normal
  implementation questions.
- Packs MUST deduplicate near-identical sources before reaching the source limit.
- Packs MUST flag ambiguity when top results span unrelated domains.
- Packs MUST cite Unity 6.3 source paths for Unity answers.
- Packs MUST show which corpora were selected and excluded.
- Packs MUST honor strict project bindings for engine docs such as Unity.
- Packs MUST distinguish source documents from approved memory and skills.
