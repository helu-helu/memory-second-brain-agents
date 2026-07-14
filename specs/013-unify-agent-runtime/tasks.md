# Tasks: Unify Agent Runtime

**Input**: Design documents from `/specs/013-unify-agent-runtime/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Include focused representative tests; avoid full official-docs corpus scans.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare consolidation artifacts and protect current work.

- [x] T001 Create a capability inventory document in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T002 [P] Record current API/MCP/runtime entrypoints in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T003 [P] Record current file-first scripts and generated artifact paths in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T004 [P] Add representative retrieval cases for unified runtime validation in `tests/fixtures/unified_runtime_queries.yaml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Decide owners and contracts before any runtime cutover.

**CRITICAL**: No user story implementation should begin until this phase is complete.

- [x] T005 Map specs 001-012 to reuse/extend/replace/drop decisions in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T006 Mark `agent_core` as runtime owner for memory, knowledge, context, and model routing in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T007 Mark `second-brain/` as data/audit/spec workspace in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T008 Identify open integration gaps and stop/go status in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T009 [P] Add contract fixtures for `UnifiedContextResult` in `tests/fixtures/unified_context_result.yaml`
- [x] T010 [P] Add contract validation tests for unified context shape in `tests/test_unified_context_contract.py`

**Checkpoint**: Foundation ready only when no more than three high/blocking gaps remain undecided.

---

## Phase 3: User Story 1 - Establish One Source Of Truth (Priority: P1) MVP

**Goal**: Remove architectural ambiguity without changing runtime behavior yet.

**Independent Test**: Review `capability-map.md` and run contract validation tests.

### Implementation for User Story 1

- [x] T011 [US1] Update `PROJECT_STATUS.md` to state that feature 013 is the active consolidation phase
- [x] T012 [US1] Update `MVP_BOUNDARY_AND_ROADMAP.md` to identify duplicated retrieval as a Phase 2 consolidation target
- [x] T013 [US1] Update `README.md` architecture notes to distinguish runtime source of truth from file-first workspace
- [x] T014 [US1] Document deprecated/fallback-only lexical retrieval paths in `specs/013-unify-agent-runtime/capability-map.md`
- [x] T015 [US1] Run `tests/test_unified_context_contract.py` and existing focused route/context tests

**Checkpoint**: User Story 1 is complete when a maintainer can tell which module owns every memory/retrieval/context capability.

---

## Phase 4: User Story 2 - Define Unified Agent Contracts (Priority: P2)

**Goal**: Align API, MCP, scripts, and context builder around the unified context contract.

**Independent Test**: Contract tests pass for mock runtime results and degraded cases.

### Implementation for User Story 2

- [x] T016 [P] [US2] Add a unified context result helper in `agent_core/context_contract.py`
- [x] T017 [P] [US2] Add tests for successful unified context results in `tests/test_context_contract.py`
- [x] T018 [P] [US2] Add tests for degraded warnings in `tests/test_context_contract.py`
- [x] T019 [US2] Adapt `agent_core/context_builder.py` to emit or support the unified context result shape
- [x] T020 [US2] Align `api/api_server.py` context endpoints with the unified context contract
- [x] T021 [US2] Align `second_brain_mcp.py` context-facing tools with the unified context contract

**Checkpoint**: User Story 2 is complete when REST and MCP can expose equivalent context semantics from the same runtime shape.

---

## Phase 5: User Story 3 - Cut Over Without Rewrite (Priority: P3)

**Goal**: Make file-first context-pack output consume runtime results instead of acting as a competing retrieval engine.

**Independent Test**: One representative API/MCP query can produce a context-pack snapshot from runtime-backed results.

### Implementation for User Story 3

- [x] T022 [P] [US3] Add runtime-backed context-pack tests in `tests/test_runtime_context_pack.py`
- [x] T023 [US3] Refactor `scripts/build_context_pack.py` into an export/audit wrapper over unified runtime results
- [x] T024 [US3] Preserve lexical behavior only as explicit fallback mode in `scripts/build_context_pack.py`
- [x] T025 [US3] Update `agent_core/access_tools.py` to call runtime-backed context-pack behavior
- [x] T026 [US3] Update API `/second-brain/context-pack` behavior in `api/api_server.py`
- [x] T027 [US3] Run MCP smoke test for route, knowledge search, memory search, and context-pack export

**Checkpoint**: User Story 3 is complete when the file-first context pack no longer silently bypasses RAG/memory runtime.

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, cleanup, and regression safety.

- [x] T028 [P] Update `CODEX_MCP_SETUP.md` with unified runtime test instructions
- [x] T029 [P] Update `PROJECT_STATUS.md` with feature 013 progress and stop rule
- [x] T030 [P] Add at least 20 representative query cases to `tests/fixtures/unified_runtime_queries.yaml`
- [x] T031 Run focused tests for memory, knowledge, API, MCP, and context-pack behavior
- [x] T032 Run full test suite when focused tests pass
- [x] T033 Mark replaced duplicate paths as deprecated in docs before deleting any code

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on setup and blocks all user stories.
- **US1 (P1)**: Starts after foundational; delivers architecture clarity.
- **US2 (P2)**: Starts after foundational; may proceed after US1 docs are stable.
- **US3 (P3)**: Starts after US2 contract shape is available.
- **Polish**: Depends on selected user stories.

## Parallel Opportunities

- T002, T003, and T004 can run in parallel.
- T009 and T010 can run in parallel.
- T016, T017, and T018 can run in parallel.
- T028, T029, and T030 can run in parallel after implementation stabilizes.

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete US1 only.
3. Stop and validate that the project has one documented runtime direction.

### Incremental Delivery

1. US1: source-of-truth map.
2. US2: contract alignment.
3. US3: runtime-backed context-pack cutover.
4. Polish: docs, query matrix, focused/full tests.

### Stop Rule

Do not delete code until a replacement path has a passing representative test and is documented in `capability-map.md`.
