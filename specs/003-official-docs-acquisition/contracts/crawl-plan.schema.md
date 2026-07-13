# Contract: Crawl Plan

Crawl plans are policy files, not crawler executions.

## Example

```yaml
plan_id: crawl-codex-docs
corpus_id: codex-docs
start_urls:
  - https://developers.openai.com/codex/
allowed_domains:
  - developers.openai.com
output_path: docs/external/codex/snapshot-2026-07-14
snapshot_policy: refreshable_snapshot
rate_limit:
  requests_per_minute: 30
max_pages: 500
approval_status: draft
notes: "Official OpenAI Codex docs only."
```

## Required Fields

- `plan_id`
- `corpus_id`
- `start_urls`
- `allowed_domains`
- `output_path`
- `snapshot_policy`
- `rate_limit`
- `max_pages`
- `approval_status`
