# Contract: Agent Tool Responses

Agent access tools return structured payloads.

## Success Shape

```yaml
ok: true
data:
  selected_corpora:
    - unity-6.3
warnings: []
error: null
```

## Failure Shape

```yaml
ok: false
data: null
warnings: []
error: "corpus registry is missing"
```

## Required Fields

- `ok`
- `data`
- `warnings`
- `error`

## Tool Names

- `list_corpora`
- `route_query`
- `build_context_pack`
- `inspect_corpus_status`
- `validate_acquisition`
- `inspect_crawl_plan`
