# Contract: Future MCP Tools

These MCP tools are the future wrapper around the file-first contracts. They
must not change the meaning of the underlying files.

## `list_corpora`

Returns registered corpora from `second-brain/corpora/registry.yaml`.

**Input**

```yaml
status: planned | available | indexed | deprecated | rejected | null
product: string | null
```

**Output**

```yaml
corpora:
  - corpus_id: unity-6.3
    category: engines
    product: Unity
    version: "6.3"
    authority_level: official
    status: available
```

## `route_query`

Routes a user query to one or more corpora before retrieval.

**Input**

```yaml
query: "How should Codex skills use MCP?"
project_path: string | null
```

**Output**

```yaml
detected_product: Codex
selected_corpora:
  - codex-docs
route_confidence: high
clarification_needed: null
```

## `build_context_pack`

Builds a bounded context pack for an agent.

**Input**

```yaml
query: "How do I use the Unity Input System?"
limit: 12
client: codex
```

**Output**

```yaml
context_pack_path: second-brain/demo/runs/example.md
status: generated
applied_sources: 12
```

## `register_corpus`

Registers a manually imported or planned official docs corpus.

**Input**

```yaml
corpus_id: python-docs-3.13
category: languages
vendor: Python Software Foundation
product: Python
version: "3.13"
authority_level: official
update_policy: refreshable_snapshot
```

**Output**

```yaml
registered: true
corpus_id: python-docs-3.13
```

## `propose_experience`

Creates candidate lessons or skills from a source document, context pack, or
task record. It must never activate artifacts automatically.

**Input**

```yaml
input_paths:
  - second-brain/demo/context-pack.example.md
artifact_types:
  - lesson
  - skill_candidate
```

**Output**

```yaml
review_status: pending
created:
  - second-brain/memory/lessons/example.md
```
