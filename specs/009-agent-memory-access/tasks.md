# Tasks: Agent Memory Access

**Input**: Design documents from `/specs/009-agent-memory-access/`

**Prerequisites**: spec.md

**Tests**: Required because this changes agent-facing access paths.

## Phase 1: Implementation

- [X] T001 Add `build_active_memory_pack` helper in `agent_core/access_tools.py`
- [X] T002 Add `/second-brain/memory-pack` endpoint in `api/api_server.py`
- [X] T003 Add `build_active_memory_pack` MCP tool in `second_brain_mcp.py`
- [X] T004 Add access-tool test in `tests/test_access_tools.py`
- [X] T005 Add API endpoint test in `tests/test_api_server.py`
- [X] T006 Replace deprecated FastAPI startup event with lifespan in `api/api_server.py`
- [X] T007 Replace FastAPI TestClient usage with httpx ASGI transport in `tests/test_api_server.py`

## Phase 2: Validation

- [X] T008 Run targeted access/API tests
- [X] T009 Run full test suite and confirm warning status
