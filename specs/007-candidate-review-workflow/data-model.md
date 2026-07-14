# Data Model: Candidate Review Workflow

## ReviewableArtifact

Represents a lesson or skill candidate that can move through lifecycle states.

**Fields**:

- `id`
- `artifact_type`: lesson, skill_candidate
- `path`
- `status`
- `confidence`
- `title_or_name`
- `evidence`
- `last_modified`

**Validation rules**:

- `id`, `status`, and `path` are required.
- `status` must be one of draft, candidate, approved, active, deprecated, superseded, rejected.
- Skill candidates are read from `second-brain/skills/candidates/*/SKILL.md`.
- Lessons are read from `second-brain/memory/lessons/*.md`.

## ReviewDecision

Append-only record of a lifecycle decision.

**Fields**:

- `id`
- `created_at`
- `artifact_id`
- `artifact_type`
- `artifact_path`
- `previous_status`
- `new_status`
- `reviewer`
- `reason`
- `evidence`

**Validation rules**:

- `reviewer` and `reason` are required.
- The decision record is written only after a successful artifact transition.

## LifecycleTransition

Represents a requested lifecycle change.

**Fields**:

- `artifact_id`
- `action`: approve, reject, activate
- `from_status`
- `to_status`
- `allowed`
- `message`

**Allowed transitions**:

- draft -> approved
- candidate -> approved
- draft -> rejected
- candidate -> rejected
- approved -> rejected
- approved -> active

## ActiveSkill

Reviewed skill available for agent use.

**Fields**:

- `id`
- `name`
- `status`
- `source_candidate`
- `activated_at`
- `review_decision`

**Relationship**:

- Created from one approved `ReviewableArtifact` of type `skill_candidate`.
