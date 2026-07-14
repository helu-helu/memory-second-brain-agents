# Tasks: Second Brain Status

**Input**: Design documents from `/specs/010-second-brain-status/`

**Prerequisites**: spec.md

**Tests**: Required because this adds agent-facing status access.

## Phase 1: Implementation

- [X] T001 Add status summary helper in `agent_core/access_tools.py`
- [X] T002 Add `/second-brain/status` endpoint in `api/api_server.py`
- [X] T003 Add `inspect_second_brain_status` MCP tool in `second_brain_mcp.py`
- [X] T004 Add access-tool status test in `tests/test_access_tools.py`
- [X] T005 Add API status test in `tests/test_api_server.py`

## Phase 2: Validation

- [X] T006 Run targeted access/API tests
- [X] T007 Run full test suite and confirm warning-free status
