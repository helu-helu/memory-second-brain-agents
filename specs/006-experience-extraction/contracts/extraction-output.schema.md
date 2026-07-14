# Contract: Extraction Output

Extraction writes candidate artifacts and a run record.

## Output Layout

```text
second-brain/memory/lessons/{lesson_id}.md
second-brain/memory/extraction-runs/{run_id}.md
second-brain/skills/candidates/{skill_id}/SKILL.md
```

## Rules

- Generated lessons MUST use `status: candidate`.
- Generated skills MUST use `status: candidate`.
- Extraction runs MUST use `review_status: pending` unless no artifacts were
  created, in which case they may use `partial`.
- Every output MUST include evidence pointing back to input files.
- No generated artifact may use `status: active`.
