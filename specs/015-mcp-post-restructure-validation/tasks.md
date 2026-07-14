# Tasks: MCP Post-Restructure Validation

**Input**: Design documents from `/specs/015-mcp-post-restructure-validation/`

**Prerequisites**: plan.md, spec.md, research.md, contracts/

**Tests**: Use small representative MCP checks; avoid full official-docs corpus scans.

## Phase 1: Setup

**Purpose**: Prepare validation evidence without changing MCP behavior.

- [x] T001 Confirm feature 014 is complete in `PROJECT_STATUS.md`
- [x] T002 [P] Confirm `.specify/feature.json` points to `specs/015-mcp-post-restructure-validation`
- [x] T003 [P] Confirm MCP command path remains `second_brain_mcp.py` in `CODEX_MCP_SETUP.md`

---

## Phase 2: Foundational

**Purpose**: Prove MCP import and tool surface before runtime checks.

- [x] T004 Add or update MCP tool-surface assertions in `tests/test_import_compatibility.py`
- [x] T005 Run `pytest tests/test_import_compatibility.py tests/test_mcp_runtime_smoke.py -q`
- [x] T006 Record fast-check results in `specs/015-mcp-post-restructure-validation/validation-report.md`

---

## Phase 3: User Story 1 - Verify Codex Can Still Use The MCP Server (Priority: P1)

**Goal**: Confirm the stable MCP entrypoint and tool names remain usable.

**Independent Test**: MCP import/tool-surface smoke passes.

- [x] T007 [US1] Verify `second_brain_mcp.py` imports without legacy module errors
- [x] T008 [US1] Verify required MCP tool functions exist in `second_brain_mcp.py`
- [x] T009 [US1] Record MCP readiness in `specs/015-mcp-post-restructure-validation/validation-report.md`

---

## Phase 4: User Story 2 - Validate One Representative Runtime Query (Priority: P2)

**Goal**: Validate one small Unity 6.3 query path after restructure.

**Independent Test**: Representative query route/context/context-pack path returns bounded output or a documented degraded warning.

- [x] T010 [US2] Run mocked runtime smoke for the Unity query path in `tests/test_mcp_runtime_smoke.py`
- [x] T011 [US2] Attempt the smallest safe real-runtime route/context/context-pack validation if local runtime is available
- [x] T012 [US2] Record mocked vs real-runtime results in `specs/015-mcp-post-restructure-validation/validation-report.md`

---

## Phase 5: User Story 3 - Record Validation Evidence (Priority: P3)

**Goal**: Leave future agents a clear MCP readiness record.

**Independent Test**: Project status and validation report show ready/degraded/blocked state.

- [x] T013 [US3] Update `PROJECT_STATUS.md` with feature 015 validation status
- [x] T014 [US3] Update `CODEX_MCP_SETUP.md` only if validation changes setup guidance
- [x] T015 [US3] Run full `pytest -q` after fast checks pass

---

## Final Phase: Polish

- [x] T016 Confirm no MCP tool names, REST routes, `second-brain/`, or `db/` paths changed
- [x] T017 Confirm no full official-docs corpus scan was used
- [x] T018 Mark feature 015 complete only after validation evidence is recorded

## Dependencies & Execution Order

- Setup precedes all checks.
- Foundational import/tool checks precede representative runtime validation.
- Real-runtime validation is optional and may be documented as blocked if it would load heavy local services.

## Stop Rule

Stop if validation requires renaming MCP tools, changing Codex MCP command path, moving storage paths, or scanning the full Unity corpus.
