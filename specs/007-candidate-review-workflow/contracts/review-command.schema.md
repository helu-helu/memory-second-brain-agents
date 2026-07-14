# Contract: Candidate Review Command

The review workflow exposes a deterministic command interface.

## Commands

```text
python scripts/review_candidate.py list --root second-brain [--status candidate]
python scripts/review_candidate.py approve <artifact_id> --reviewer codex --reason "..."
python scripts/review_candidate.py reject <artifact_id> --reviewer codex --reason "..."
python scripts/review_candidate.py activate <artifact_id> --reviewer codex --reason "..."
```

## List Output

List output is YAML with:

- `artifacts`
  - `id`
  - `artifact_type`
  - `path`
  - `status`
  - `confidence`
  - `title_or_name`
  - `evidence_count`
  - `last_modified`

## Transition Output

Transition output is YAML with:

- `ok`
- `artifact_id`
- `artifact_type`
- `previous_status`
- `new_status`
- `artifact_path`
- `decision_path`
- `warnings`

## Rules

- Invalid transitions MUST return `ok: false`.
- Invalid transitions MUST NOT modify the artifact.
- Successful transitions MUST write one decision record under `second-brain/reviews/decisions/`.
- Activation of skill candidates MUST copy into `second-brain/skills/active/{skill_id}/SKILL.md`.
