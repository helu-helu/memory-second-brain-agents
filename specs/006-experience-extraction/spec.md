# Feature Specification: Experience Extraction

**Feature Branch**: `006-experience-extraction`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Continue after agent access tools by adding a governed experience extraction workflow. The system should turn source documents, context packs, and task records into candidate lessons, preferences, and skill candidates for review, without automatically activating memory or skills."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Propose Lessons from Evidence (Priority: P1)

As the user, I want the system to extract candidate lessons from source evidence
so useful experience can be reviewed and reused by future agents.

**Why this priority**: The project's core value is turning documents and work
experience into future agent behavior, not just storing docs.

**Independent Test**: Run extraction on a context pack or source document and
verify candidate lesson files are created with evidence, trigger, scope,
confidence, and `candidate` status.

**Acceptance Scenarios**:

1. **Given** a context pack contains Unity source citations, **When** extraction
   runs, **Then** it creates candidate lessons referencing the context pack and
   source paths.
2. **Given** the extracted guidance has no clear future behavior change, **When**
   extraction runs, **Then** it records no lesson rather than producing a summary
   disguised as memory.
3. **Given** extraction creates a lesson, **When** the file is inspected, **Then**
   its status is `candidate`, not `active`.

---

### User Story 2 - Propose Skill Candidates (Priority: P2)

As the user, I want repeated workflows to become skill candidates with scripts,
inputs, outputs, eval notes, and failure modes so they can later be reviewed as
portable skills.

**Why this priority**: Skills are the bridge from learned experience to reusable
agent behavior.

**Independent Test**: Run extraction on a workflow-like source and verify a
skill candidate folder is created with `SKILL.md` and metadata-compatible
frontmatter.

**Acceptance Scenarios**:

1. **Given** evidence describes a repeatable workflow, **When** extraction runs,
   **Then** it creates a skill candidate with trigger, workflow, inputs, outputs,
   scripts, eval, and failure modes.
2. **Given** evidence is only a factual note, **When** extraction runs, **Then**
   it does not create a skill candidate.

---

### User Story 3 - Record Extraction Runs (Priority: P3)

As the maintainer, I want every extraction attempt to create a run record so I
can audit what evidence produced which candidate artifacts.

**Why this priority**: Extraction without provenance becomes memory pollution.

**Independent Test**: Run extraction and verify an extraction-run artifact links
inputs, method, outputs, review status, and warnings.

**Acceptance Scenarios**:

1. **Given** extraction produces candidates, **When** the run completes, **Then**
   the extraction run lists every created artifact.
2. **Given** extraction produces nothing, **When** the run completes, **Then** the
   run record explains why no artifacts were created.

### Edge Cases

- Evidence file has no YAML frontmatter.
- Context pack has no sources.
- Candidate artifact already exists.
- Evidence contains conflicting advice.
- Generated lesson would duplicate an existing candidate.
- User asks for activation without review.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Extraction MUST create only candidate artifacts by default.
- **FR-002**: Extraction MUST write an extraction-run record for every run.
- **FR-003**: Candidate lessons MUST include id, title, status, confidence,
  trigger, scope, guidance, and evidence.
- **FR-004**: Candidate skills MUST include id, name, status, confidence,
  trigger, inputs, workflow, outputs, scripts, eval, and failure modes.
- **FR-005**: Extraction MUST not activate, approve, or promote artifacts.
- **FR-006**: Extraction MUST preserve evidence links to input files and source
  paths when available.
- **FR-007**: Extraction MUST prefer no output over low-value summaries.
- **FR-008**: Extraction output MUST be written in English.
- **FR-009**: Extraction MUST be scriptable and deterministic for the MVP.

### Key Entities

- **ExtractionInput**: Context pack, source document, task record, or manual note.
- **CandidateLesson**: Reviewable lesson artifact.
- **CandidateSkill**: Reviewable skill candidate folder.
- **ExtractionRun**: Audit record for one extraction attempt.
- **ExtractionDecision**: Reason why a candidate was or was not created.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Running extraction on a valid context pack creates an extraction-run
  record and at least one candidate lesson.
- **SC-002**: Candidate artifacts validate against existing schemas.
- **SC-003**: No generated artifact has `status: active`.
- **SC-004**: Extraction tests cover lesson creation, skill candidate creation,
  no-output cases, and duplicate-safe behavior.
- **SC-005**: Full test suite passes after extraction workflow changes.

## Assumptions

- MVP extraction is deterministic and template-based, not LLM-generated.
- LLM-assisted extraction can be a future feature once review and provenance are
  stable.
- Existing `second-brain/demo/` artifacts remain examples; real candidate output
  belongs under `second-brain/memory/` and `second-brain/skills/`.
