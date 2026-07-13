# Quickstart: Validate Official Docs Acquisition

## Scenario 1: Dry-Run a Local Corpus

```bash
python scripts/validate_acquisition.py --corpus-id unity-6.3 --path docs/massive/Unity_6_3_Markdown --limit 100
```

Expected result:

- A dry-run report is printed.
- Supported Markdown files are counted.
- No registry mutation is required.

## Scenario 2: Create a Planned Crawl Plan

```bash
python scripts/create_crawl_plan.py --plan-id crawl-codex-docs --corpus-id codex-docs --url https://developers.openai.com/codex/ --domain developers.openai.com --output docs/external/codex/snapshot-2026-07-14
```

Expected result:

- A crawl plan file is written under `second-brain/corpora/crawl-plans/`.
- The plan remains `draft` until manually approved.

## Scenario 3: Run Tests

```bash
.venv\Scripts\python.exe -m pytest -q
```

Expected result:

- Full test suite passes.
