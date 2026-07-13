# Tasks: Hybrid Retrieval Context Packs

**Input**: Design documents from `/specs/002-hybrid-retrieval-context-packs/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Required. Retrieval quality must be repeatable.

**Organization**: Tasks are grouped by user story.

## Phase 1: Setup

**Purpose**: Add eval fixtures and contracts without changing runtime behavior.

- [x] T001 Create retrieval eval fixture in `tests/fixtures/retrieval_eval.yaml`
- [x] T002 [P] Add retrieval eval contract test in `tests/test_retrieval_eval.py`
- [x] T003 [P] Add score/signal expectations to context-pack tests in `tests/test_build_context_pack.py`

---

## Phase 2: Foundational

**Purpose**: Refactor context-pack building enough to support scored candidates.

- [x] T004 Add `RetrievalCandidate` helpers in `scripts/build_context_pack.py`
- [x] T005 Add score breakdown fields to ranked source output in `scripts/build_context_pack.py`
- [x] T006 Add source deduplication by path/section in `scripts/build_context_pack.py`
- [x] T007 Ensure context-pack output preserves the existing frontmatter contract

---

## Phase 3: User Story 1 - Retrieve Relevant Unity Sources (Priority: P1) MVP

**Goal**: Unity context packs rank task-relevant docs above generic pages.

**Independent Test**: Unity eval cases pass and Input-related docs appear in top results.

- [x] T008 [P] [US1] Add Unity retrieval eval cases for Input, GameObject/MonoBehaviour, URP, and build pipeline in `tests/fixtures/retrieval_eval.yaml`
- [x] T009 [US1] Improve lexical/path/phrase ranking in `scripts/build_context_pack.py`
- [x] T010 [US1] Add exact symbol scoring for API-like tokens in `scripts/build_context_pack.py`
- [x] T011 [US1] Validate source limit behavior for Unity packs in `tests/test_build_context_pack.py`

---

## Phase 4: User Story 2 - Explain Retrieval Quality (Priority: P2)

**Goal**: Context packs explain why each source was selected.

**Independent Test**: Every ranked source includes score signals and selection reason.

- [x] T012 [P] [US2] Add source score signal assertions in `tests/test_build_context_pack.py`
- [x] T013 [US2] Render score breakdown and reason in context-pack Markdown
- [x] T014 [US2] Add low-confidence warning behavior for no-source and ambiguous routes

---

## Phase 5: User Story 3 - Evaluate Retrieval Changes (Priority: P3)

**Goal**: Retrieval quality can be checked repeatedly.

**Independent Test**: Eval script exits non-zero on failing required cases.

- [x] T015 [US3] Implement `scripts/evaluate_retrieval.py`
- [x] T016 [P] [US3] Add eval pass/fail tests in `tests/test_retrieval_eval.py`
- [x] T017 [US3] Add quickstart eval output examples in `second-brain/docs/retrieval-eval.md`

---

## Phase 6: Optional Vector Integration

**Purpose**: Add vector scoring only after deterministic retrieval and eval pass.

- [x] T018 Add vector availability detection without requiring Qdrant for lexical mode
- [x] T019 Add optional vector request mode behind the existing context-pack contract
- [x] T020 Add degraded-mode warning when vector retrieval is requested but unavailable

---

## Phase 7: Polish

- [x] T021 Run quickstart scenarios from `specs/002-hybrid-retrieval-context-packs/quickstart.md`
- [x] T022 Run full test suite and record warnings
- [x] T023 Review generated context packs for bounded sources, corpus id, citation path, reason, and snippets

## Dependencies & Execution Order

- Phase 1 before all implementation.
- Phase 2 before user stories.
- US1 is MVP.
- US2 depends on score fields from Phase 2.
- US3 depends on fixture cases and context-pack generation.
- Vector integration is optional and only starts after eval passes.

## Implementation Strategy

1. Build eval fixtures and scored lexical ranking first.
2. Keep context-pack contract stable.
3. Add vector scoring only behind the same output shape.
4. Stop if eval quality regresses.
