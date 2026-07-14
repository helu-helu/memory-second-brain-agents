# Quickstart: Validate Agent Access Tools

## Scenario 1: List Corpora

```bash
.venv\Scripts\python.exe -m pytest tests/test_access_tools.py -q
```

Expected result:

- Access layer returns registered corpora.

## Scenario 2: Build Context Pack Through Access Layer

Expected result:

- Unity query returns `unity-6.3`.
- Context pack path exists.
- Applied sources do not exceed limit.

## Scenario 3: Inspect Codex Status

Expected result:

- `codex-docs` reports planned/no local root path and crawl plan draft status.

## Scenario 4: Full Tests

```bash
.venv\Scripts\python.exe -m pytest -q
```

Expected result:

- Full suite passes.
