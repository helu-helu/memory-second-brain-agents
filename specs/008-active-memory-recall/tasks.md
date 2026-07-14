# Tasks: Active Memory Recall

**Input**: Design documents from `/specs/008-active-memory-recall/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Required because memory recall affects agent behavior.

## Phase 1: Setup

- [X] T001 Create `second-brain/memory/packs/`
- [X] T002 Add memory recall tests in `tests/test_memory_pack.py`

---

## Phase 2: User Story 1 - Build Active Memory Pack (Priority: P1) MVP

- [X] T003 Implement `scripts/build_memory_pack.py`
- [X] T004 [US1] Parse active lessons from `second-brain/memory/lessons/*.md`
- [X] T005 [US1] Parse active skills from `second-brain/skills/active/*/SKILL.md`
- [X] T006 [US1] Rank memory items using query terms and trigger/title/body text
- [X] T007 [P] [US1] Test matching active lesson appears in memory pack
- [X] T008 [P] [US1] Test no-match output reports no active matches

---

## Phase 3: User Story 2 - Keep Recall Bounded and Governed (Priority: P2)

- [X] T009 [US2] Enforce active-only eligibility
- [X] T010 [US2] Enforce configurable item limit
- [X] T011 [P] [US2] Test non-active artifacts are excluded
- [X] T012 [P] [US2] Test output does not exceed limit

---

## Phase 4: User Story 3 - Record Recall Quality Signals (Priority: P3)

- [X] T013 [US3] Add pack frontmatter quality metadata and warnings
- [X] T014 [US3] Add selected item match reasons to pack body
- [X] T015 [P] [US3] Test quality metadata and warnings

---

## Phase 5: Polish

- [X] T016 Run quickstart scenarios from `specs/008-active-memory-recall/quickstart.md`
- [X] T017 Run full test suite and record warnings
- [X] T018 Confirm tests use small representative fixtures only

## Dependencies & Execution Order

- Phase 1 before all stories.
- US1 is MVP.
- US2 depends on parsing/ranking from US1.
- US3 depends on pack rendering from US1.

## Implementation Strategy

1. Build active-only memory pack script first.
2. Add bounded recall checks.
3. Add quality signals and warnings.
4. Keep API/MCP wrapping for a later feature.
