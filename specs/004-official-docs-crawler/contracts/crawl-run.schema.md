# Contract: Crawl Run Manifest

Crawl run manifests are YAML files written under:

```text
second-brain/corpora/acquisitions/
```

## Example

```yaml
run_id: crawl-codex-docs-20260714
plan_id: crawl-codex-docs
corpus_id: codex-docs
started_at: "2026-07-14T00:00:00+07:00"
status: completed
output_path: docs/external/codex/snapshot-2026-07-14
fetched:
  - url: https://developers.openai.com/codex/
    status_code: 200
    path: docs/external/codex/snapshot-2026-07-14/index.html
    content_type: text/html
skipped:
  - url: https://example.com/
    reason: off_domain
warnings: []
```

## Required Fields

- `run_id`
- `plan_id`
- `corpus_id`
- `started_at`
- `status`
- `output_path`
- `fetched`
- `skipped`
- `warnings`
