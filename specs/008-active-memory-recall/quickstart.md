# Quickstart: Validate Active Memory Recall

## Scenario 1: Activate an Approved Lesson

```bash
python scripts/review_candidate.py activate lesson-how-do-i-use-the-unity-input-system-20260714040956 --root second-brain --reviewer codex --reason "Ready for active personal memory recall."
```

Expected result:

- The lesson status becomes `active`.
- A review decision file is created.

## Scenario 2: Build Memory Pack

```bash
python scripts/build_memory_pack.py "How should I answer Unity Input System questions?" --limit 5 --out second-brain/memory/packs/unity-input-memory.md
```

Expected result:

- The pack includes active Unity input guidance.
- The pack does not include candidate or rejected artifacts.

## Scenario 3: Run Tests

```bash
.venv\Scripts\python.exe -m pytest tests/test_memory_pack.py -q
```

Expected result:

- Active memory recall tests pass.
