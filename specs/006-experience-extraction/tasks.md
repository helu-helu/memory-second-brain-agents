# Tasks: Experience Extraction

**Input**: Design documents from `/specs/006-experience-extraction/`

**Prerequisites**: spec.md, plan.md, research.md, data-model.md, contracts/

**Tests**: Required.

## Phase 1: Setup

- [X] T001 Create `second-brain/memory/lessons/`
- [X] T002 Create `second-brain/memory/extraction-runs/`
- [X] T003 Create `second-brain/skills/candidates/`
- [X] T004 Add extraction tests in `tests/test_experience_extraction.py`

---

## Phase 2: User Story 1 - Propose Lessons from Evidence (Priority: P1) MVP

- [X] T005 Implement `scripts/extract_experience.py`
- [X] T006 [US1] Parse context-pack frontmatter and ranked sources
- [X] T007 [US1] Generate candidate lesson with evidence and candidate status
- [X] T008 [P] [US1] Test candidate lesson schema fields
- [X] T009 [US1] Test no active status is generated

---

## Phase 3: User Story 2 - Propose Skill Candidates (Priority: P2)

- [X] T010 [US2] Add workflow-like evidence detection
- [X] T011 [US2] Generate skill candidate folder with `SKILL.md`
- [X] T012 [P] [US2] Test skill candidate schema fields
- [X] T013 [US2] Test factual notes do not generate skills

---

## Phase 4: User Story 3 - Record Extraction Runs (Priority: P3)

- [X] T014 [US3] Write extraction-run record for every run
- [X] T015 [US3] Record no-output decisions and warnings
- [X] T016 [P] [US3] Test extraction-run links inputs and outputs

---

## Phase 5: Polish

- [X] T017 Run quickstart scenarios from `specs/006-experience-extraction/quickstart.md`
- [X] T018 Run full test suite and record warnings
- [X] T019 Review generated artifacts for candidate-only status and English-first content

## Dependencies & Execution Order

- Phase 1 before all stories.
- US1 is MVP.
- US2 can follow after extraction script exists.
- US3 runs alongside US1/US2 because every extraction needs a run record.

## Implementation Strategy

1. Create candidate lesson extraction first.
2. Add skill candidate extraction only for workflow-like evidence.
3. Always write run records.
4. Never activate artifacts.
