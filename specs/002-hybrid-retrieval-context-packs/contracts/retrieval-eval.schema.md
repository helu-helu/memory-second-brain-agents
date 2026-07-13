# Contract: Retrieval Eval Fixture

Retrieval eval fixtures are YAML files under `tests/fixtures/`.

## Example

```yaml
cases:
  - id: unity-input-system
    query: "How do I use the Unity Input System?"
    expected_product: Unity
    expected_corpus: unity-6.3
    expected_path_patterns:
      - Input
    max_sources: 12
    expect_clarification: false
```

## Required Fields

- `id`
- `query`
- `expected_product`
- `expected_corpus`
- `expected_path_patterns`
- `max_sources`
- `expect_clarification`

## Pass Rules

- Query route selects `expected_corpus`.
- Generated context pack uses no more than `max_sources`.
- If `expect_clarification` is true, route or context-pack quality must report
  ambiguity.
- If `expected_path_patterns` is not empty, at least one top source path matches
  one pattern.
