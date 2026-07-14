# Tasks: Physical Runtime Restructure

**Input**: Design documents from `/specs/014-physical-runtime-restructure/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Include focused representative tests and import smoke checks; avoid full official-docs corpus scans.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Protect the current working behavior before moving files.

- [x] T001 Record current import and adapter surface in `specs/014-physical-runtime-restructure/migration-map.md`
- [x] T002 [P] Add or update public import compatibility tests in `tests/test_import_compatibility.py`
- [x] T003 [P] Confirm root `README.md` deletion is intentional in `PROJECT_STATUS.md`
- [x] T004 [P] Run baseline focused tests from `specs/014-physical-runtime-restructure/quickstart.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create the target package skeleton and compatibility test gates.

**CRITICAL**: No implementation move should begin until import compatibility tests exist.

- [x] T005 Create target package directories and `__init__.py` files under `agent_core/rag/`, `agent_core/context/`, `agent_core/access/`, and optional `agent_core/mcp/`
- [x] T006 [P] Add tests proving `from agent_core import MemoryManager, KnowledgeBase, ContextBuilder` still works in `tests/test_import_compatibility.py`
- [x] T007 [P] Add tests proving legacy module imports still work in `tests/test_import_compatibility.py`
- [x] T008 [P] Add MCP import smoke coverage for stable tool entrypoint in `tests/test_import_compatibility.py`
- [x] T009 Update `specs/014-physical-runtime-restructure/migration-map.md` with actual package skeleton status

**Checkpoint**: Foundation is ready when compatibility tests fail before shims only where expected and pass after skeleton/shim setup.

---

## Phase 3: User Story 1 - Make Runtime Ownership Legible (Priority: P1) MVP

**Goal**: Move lower-risk runtime implementation into clearer package owners while preserving old paths as shims.

**Independent Test**: Focused tests for knowledge, context, and access tools pass through both new and legacy import paths.

### Implementation for User Story 1

- [x] T010 [P] [US1] Move knowledge implementation to `agent_core/rag/knowledge.py`
- [x] T011 [US1] Replace `agent_core/knowledge.py` with a compatibility shim to `agent_core.rag.knowledge`
- [x] T012 [US1] Update internal imports that own runtime behavior to use `agent_core.rag.knowledge`
- [x] T013 [P] [US1] Move context builder implementation to `agent_core/context/builder.py`
- [x] T014 [US1] Replace `agent_core/context_builder.py` with a compatibility shim to `agent_core.context.builder`
- [x] T015 [US1] Update internal imports that own runtime behavior to use `agent_core.context.builder`
- [x] T016 [P] [US1] Move access tools implementation to `agent_core/access/second_brain.py`
- [x] T017 [US1] Replace `agent_core/access_tools.py` with a compatibility shim to `agent_core.access.second_brain`
- [x] T018 [US1] Update internal imports that own runtime behavior to use `agent_core.access.second_brain`
- [x] T019 [US1] Run focused tests for knowledge, context, access tools, runtime context-pack, API, and MCP smoke

**Checkpoint**: User Story 1 is complete when old paths are shims, new package paths own implementation, and focused tests pass.

---

## Phase 4: User Story 2 - Preserve Agent Access While Moving Modules (Priority: P2)

**Goal**: Verify Codex/MCP/API access remains stable after package movement.

**Independent Test**: Existing MCP and API import smoke checks pass without route or tool renames.

### Implementation for User Story 2

- [x] T020 [P] [US2] Verify `api/api_server.py` imports only stable public or new runtime package paths
- [x] T021 [P] [US2] Verify `second_brain_mcp.py` remains a stable top-level entrypoint
- [x] T022 [US2] Defer optional MCP helper extraction; `second_brain_mcp.py` remains stable and no new helper code is needed
- [x] T023 [US2] Run API server import/start smoke from existing focused tests
- [x] T024 [US2] Run MCP import/runtime smoke from existing focused tests
- [x] T025 [US2] Keep `CODEX_MCP_SETUP.md` unchanged; MCP command path did not change

**Checkpoint**: User Story 2 is complete when Codex can still connect to the same MCP command and runtime-backed context tools still work.

---

## Phase 5: User Story 3 - Retire Stale Structure Safely (Priority: P3)

**Goal**: Move the high-risk memory implementation only after lower-risk moves and compatibility gates are stable.

**Independent Test**: `agent_core.memory` remains importable and memory tests pass after converting implementation to a package.

### Implementation for User Story 3

- [x] T026 [US3] Add explicit high-risk memory import assertions to `tests/test_import_compatibility.py`
- [x] T027 [US3] Move memory implementation from `agent_core/memory.py` to `agent_core/memory/manager.py`
- [x] T028 [US3] Create `agent_core/memory/__init__.py` exporting `MemoryManager`
- [x] T029 [US3] Update internal imports only if needed while preserving `agent_core.memory` as the public path
- [x] T030 [US3] Run memory, import compatibility, API, MCP, and context-pack focused tests

**Checkpoint**: User Story 3 is complete when the memory package replaces the file safely and all public imports still work.

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Documentation, validation, and no-surprise completion.

- [x] T031 [P] Update `PROJECT_STATUS.md` with feature 014 progress and stop rule
- [x] T032 [P] Update or add a new architecture note only after implementation validates the new structure
- [x] T033 [P] Update `specs/014-physical-runtime-restructure/migration-map.md` with final actual paths and shim status
- [x] T034 Run full `pytest` only after focused tests pass
- [x] T035 Confirm no compatibility shim was deleted during feature 014
- [x] T036 Confirm `second-brain/`, `db/`, REST routes, and MCP tool names were not renamed

---

## Dependencies & Execution Order

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on setup and blocks all code moves.
- **US1 (P1)**: Starts after foundational; moves low/medium-risk module families.
- **US2 (P2)**: Starts after US1 or in parallel only for read-only verification tasks.
- **US3 (P3)**: Starts only after US1 and compatibility tests are stable.
- **Polish**: Depends on selected user stories.

## Parallel Opportunities

- T002, T003, and T004 can run in parallel.
- T006, T007, and T008 can run in parallel.
- T010, T013, and T016 can be prepared in parallel only if each worker owns a distinct module family.
- T020 and T021 can run in parallel as verification tasks.
- T031, T032, and T033 can run in parallel after implementation stabilizes.

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete US1 only.
3. Stop and validate that package ownership is clear while legacy imports still work.

### Incremental Delivery

1. Create compatibility tests and package skeleton.
2. Move RAG, context, and access modules with shims.
3. Verify API/MCP access remains stable.
4. Move memory last.
5. Update status and architecture notes after validation.

### Stop Rule

Do not delete shims, move `second-brain/`, move `db/`, rename REST routes, rename MCP tools, or add new retrieval behavior during feature 014.
