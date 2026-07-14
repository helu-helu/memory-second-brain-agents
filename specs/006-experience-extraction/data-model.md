# Data Model: Experience Extraction

## ExtractionInput

Represents one evidence file.

**Fields**:

- `path`: input file path.
- `type`: context_pack, source_document, task_record, note.
- `frontmatter`: parsed YAML frontmatter when present.
- `body`: Markdown body.

## CandidateLesson

Reviewable lesson artifact.

**Fields**:

- `id`
- `title`
- `status`
- `confidence`
- `trigger`
- `scope`
- `guidance`
- `evidence`
- `failure_modes`

## CandidateSkill

Reviewable skill candidate folder.

**Fields**:

- `id`
- `name`
- `status`
- `confidence`
- `trigger`
- `inputs`
- `workflow`
- `outputs`
- `scripts`
- `eval`
- `failure_modes`

## ExtractionRun

Audit record for extraction.

**Fields**:

- `id`
- `created_at`
- `operator`
- `inputs`
- `method`
- `outputs`
- `review_status`
- `warnings`
- `decisions`
