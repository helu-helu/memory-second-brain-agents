# Tasks: Agent Bootstrap Context

**Input**: Design documents from `/specs/011-agent-bootstrap-context/`

**Prerequisites**: spec.md

**Tests**: Required because this adds an agent-facing orchestration path.

## Phase 1: Implementation

- [X] T001 Add `build_agent_bootstrap` helper in `agent_core/access_tools.py`
- [X] T002 Add `/second-brain/bootstrap` endpoint in `api/api_server.py`
- [X] T003 Add `build_agent_bootstrap` MCP tool in `second_brain_mcp.py`
- [X] T004 Add access-tool bootstrap test in `tests/test_access_tools.py`
- [X] T005 Add API bootstrap test in `tests/test_api_server.py`

## Phase 2: Validation

- [X] T006 Run targeted access/API tests
- [X] T007 Run full test suite and confirm warning-free status
