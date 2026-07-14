# Tasks: Candidate Review Workflow

**Input**: Design documents from `/specs/007-candidate-review-workflow/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Required because lifecycle transitions can alter durable memory artifacts.

## Phase 1: Setup

- [X] T001 Create `second-brain/reviews/decisions/`
- [X] T002 Create `second-brain/skills/active/`
- [X] T003 Add candidate review tests in `tests/test_candidate_review.py`

---

## Phase 2: User Story 1 - Review Candidate State (Priority: P1) MVP

- [X] T004 Implement `scripts/review_candidate.py`
- [X] T005 [US1] Parse lesson candidates from `second-brain/memory/lessons/*.md`
- [X] T006 [US1] Parse skill candidates from `second-brain/skills/candidates/*/SKILL.md`
- [X] T007 [US1] Implement list output with status filtering
- [X] T008 [P] [US1] Test list includes candidate metadata
- [X] T009 [P] [US1] Test list excludes non-matching statuses

---

## Phase 3: User Story 2 - Approve or Reject Candidates (Priority: P2)

- [X] T010 [US2] Implement allowed transition validation
- [X] T011 [US2] Implement approve transition with reviewer and reason
- [X] T012 [US2] Implement reject transition with reviewer and reason
- [X] T013 [US2] Write review decision records under `second-brain/reviews/decisions/`
- [X] T014 [P] [US2] Test approve updates status and writes decision
- [X] T015 [P] [US2] Test reject updates status and writes decision
- [X] T016 [US2] Test invalid transition leaves artifact unchanged

---

## Phase 4: User Story 3 - Activate Approved Artifacts (Priority: P3)

- [X] T017 [US3] Implement lesson activation from approved to active
- [X] T018 [US3] Implement skill candidate activation copy to `second-brain/skills/active/`
- [X] T019 [US3] Preserve source candidate provenance during activation
- [X] T020 [P] [US3] Test unapproved artifact cannot activate
- [X] T021 [P] [US3] Test approved skill candidate creates active skill copy

---

## Phase 5: Polish

- [X] T022 Run quickstart scenarios from `specs/007-candidate-review-workflow/quickstart.md`
- [X] T023 Run full test suite and record warnings
- [X] T024 Review generated decision records for append-only audit readability

## Dependencies & Execution Order

- Phase 1 before all stories.
- US1 is MVP and must complete before transition commands.
- US2 depends on artifact lookup from US1.
- US3 depends on transition validation from US2.

## Implementation Strategy

1. Ship candidate listing first.
2. Add approve/reject with decision records.
3. Add activation last because it exposes artifacts to agents.
4. Refuse unsafe transitions rather than guessing user intent.
