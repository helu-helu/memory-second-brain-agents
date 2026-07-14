# Feature Specification: Agent Memory Access

**Feature Branch**: `009-agent-memory-access`

**Created**: 2026-07-14

**Status**: Draft

**Input**: Continue after active memory recall by exposing active memory packs through API/MCP and remove reasonable warning noise.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Agent Builds Active Memory Pack (Priority: P1)

As Codex or another agent, I want to request a bounded active memory pack through the same access layer used for official docs context packs.

**Why this priority**: The active recall script is useful only after agents can call it without shell access.

**Independent Test**: API and access-tool calls create a memory pack and return path, applied item count, quality, and warnings.

**Acceptance Scenarios**:

1. **Given** active personal memory exists, **When** an agent requests a memory pack, **Then** the response includes pack metadata and a file path.
2. **Given** an empty query, **When** an agent requests a memory pack, **Then** the request is rejected.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST expose active memory pack creation through agent access tools.
- **FR-002**: System MUST expose active memory pack creation through REST API.
- **FR-003**: System MUST expose active memory pack creation through MCP.
- **FR-004**: System MUST keep item limits bounded to 20 or fewer.
- **FR-005**: System SHOULD remove deprecation warnings caused by project-owned API/test code when a small safe fix exists.

### Key Entities *(include if feature involves data)*

- **MemoryPackAccessResult**: Agent-facing result containing path, applied item count, quality, warnings, and error state.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Access tool and API tests pass for active memory pack creation.
- **SC-002**: Full test suite passes without project-owned FastAPI deprecation warnings.
- **SC-003**: Existing docs context pack endpoints continue to pass.

## Assumptions

- The underlying active memory recall script remains the source of truth.
- Full MCP runtime smoke testing is deferred; MCP wrapper is kept thin and uses the API endpoint.
