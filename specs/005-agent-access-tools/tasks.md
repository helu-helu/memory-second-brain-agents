# Tasks: Agent Access Tools

**Input**: Design documents from `/specs/005-agent-access-tools/`

**Prerequisites**: spec.md, plan.md, research.md, data-model.md, contracts/

**Tests**: Required.

## Phase 1: Setup

- [x] T001 Create `agent_core/access_tools.py`
- [x] T002 Add response contract helpers in `agent_core/access_tools.py`
- [x] T003 Add access tool tests in `tests/test_access_tools.py`

---

## Phase 2: User Story 1 - Agent Lists and Routes Corpora (Priority: P1) MVP

- [x] T004 [US1] Implement `list_corpora()` in `agent_core/access_tools.py`
- [x] T005 [US1] Implement `route_docs_query()` in `agent_core/access_tools.py`
- [x] T006 [P] [US1] Test list and route responses in `tests/test_access_tools.py`

---

## Phase 3: User Story 2 - Agent Builds Context Packs (Priority: P2)

- [x] T007 [US2] Implement `build_docs_context_pack()` in `agent_core/access_tools.py`
- [x] T008 [P] [US2] Test context-pack output path/source limit in `tests/test_access_tools.py`
- [x] T009 [US2] Ensure missing local corpus warnings are returned for planned corpora

---

## Phase 4: User Story 3 - Agent Inspects Acquisition and Crawl Status (Priority: P3)

- [x] T010 [US3] Implement `inspect_corpus_status()` in `agent_core/access_tools.py`
- [x] T011 [P] [US3] Test Unity acquisition status in `tests/test_access_tools.py`
- [x] T012 [P] [US3] Test Codex crawl-plan/planned status in `tests/test_access_tools.py`

---

## Phase 5: Optional API/MCP Wrappers

- [x] T013 Add thin FastAPI endpoints for list/route/context/status if low-risk
- [x] T014 Add thin MCP tools in `second_brain_mcp.py` if low-risk
- [x] T015 Preserve existing MCP tool behavior

---

## Phase 6: Polish

- [x] T016 Run quickstart scenarios from `specs/005-agent-access-tools/quickstart.md`
- [x] T017 Run full test suite and record warnings
- [x] T018 Review tools for no live scraping and no auto-promotion behavior

## Dependencies & Execution Order

- Phase 1 before all stories.
- US1 is MVP.
- US2 depends on US1 routing.
- US3 can run after Phase 1.
- API/MCP wrappers are optional after helper tests pass.

## Implementation Strategy

1. Build tested helper layer.
2. Add wrappers only if thin and safe.
3. Keep file-first scripts/contracts as source of truth.
