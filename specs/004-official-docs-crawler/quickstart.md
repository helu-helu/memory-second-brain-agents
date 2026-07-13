# Quickstart: Validate Official Docs Crawler

## Scenario 1: Refuse Draft Plan

```bash
python scripts/crawl_official_docs.py second-brain/corpora/crawl-plans/codex-docs.yaml --dry-run
```

Expected result:

- Dry run reports what would be crawled.
- No network fetch is required.

## Scenario 2: Run Local Test Crawl

```bash
.venv\Scripts\python.exe -m pytest tests/test_crawler.py -q
```

Expected result:

- Local fixture site is crawled.
- Off-domain links are skipped.
- Run manifest is written.

## Scenario 3: Run Full Tests

```bash
.venv\Scripts\python.exe -m pytest -q
```

Expected result:

- Full test suite passes.
