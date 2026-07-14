# Quickstart: Validate Candidate Review Workflow

## Scenario 1: List Pending Candidates

```bash
python scripts/review_candidate.py list --root second-brain --status candidate
```

Expected result:

- Candidate lessons and skill candidates are listed.
- Active and rejected artifacts are excluded.

## Scenario 2: Approve a Candidate Lesson

```bash
python scripts/review_candidate.py approve lesson-how-do-i-use-the-unity-input-system-20260714040956 --root second-brain --reviewer codex --reason "Useful Unity input guidance with evidence."
```

Expected result:

- The lesson status becomes `approved`.
- A review decision file is created.
- The lesson does not become `active`.

## Scenario 3: Reject a Candidate

```bash
python scripts/review_candidate.py reject <artifact_id> --root second-brain --reviewer codex --reason "Too broad for active memory."
```

Expected result:

- The artifact status becomes `rejected`.
- A review decision file is created.

## Scenario 4: Run Tests

```bash
.venv\Scripts\python.exe -m pytest tests/test_candidate_review.py -q
```

Expected result:

- Candidate review tests pass.
