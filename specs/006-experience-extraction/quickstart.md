# Quickstart: Validate Experience Extraction

## Scenario 1: Extract from a Context Pack

```bash
python scripts/extract_experience.py second-brain/demo/runs/hybrid-unity-input.md --out-root second-brain
```

Expected result:

- A candidate lesson is created.
- An extraction-run record is created.
- No artifact is active.

## Scenario 2: Run Tests

```bash
.venv\Scripts\python.exe -m pytest tests/test_experience_extraction.py -q
```

Expected result:

- Extraction tests pass.

## Scenario 3: Full Suite

```bash
.venv\Scripts\python.exe -m pytest -q
```

Expected result:

- Full suite passes.
