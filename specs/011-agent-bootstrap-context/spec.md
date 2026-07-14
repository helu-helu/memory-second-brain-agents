# Feature Specification: Agent Bootstrap Context

**Feature Branch**: `011-agent-bootstrap-context`

**Created**: 2026-07-14

**Status**: Draft

**Input**: Continue by adding one compact bootstrap response for a new agent task.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Bootstrap a New Agent Task (Priority: P1)

As a newly connected agent, I want one compact startup response for the current task containing second-brain status, active memory pack metadata, and docs routing hint.

**Why this priority**: Agents should not need to discover and orchestrate multiple second-brain tools before doing useful work.

**Independent Test**: Calling the bootstrap helper or API with a Unity query returns memory pack metadata, status summary, and selected Unity corpus route.

**Acceptance Scenarios**:

1. **Given** a task query, **When** bootstrap is requested, **Then** a bounded active memory pack is generated and returned with status summary.
2. **Given** a documentation-like query, **When** bootstrap is requested, **Then** docs routing hint is included without building a full docs context pack.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST expose an access helper for agent bootstrap context.
- **FR-002**: System MUST expose bootstrap through REST API.
- **FR-003**: System MUST expose bootstrap through MCP.
- **FR-004**: Bootstrap MUST include active memory pack metadata.
- **FR-005**: Bootstrap MUST include second-brain status summary.
- **FR-006**: Bootstrap MUST include docs route hint when routing succeeds.
- **FR-007**: Bootstrap MUST remain bounded and must not scan full official docs corpora.

### Key Entities *(include if feature involves data)*

- **AgentBootstrapContext**: Compact startup response for one task query.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Bootstrap access-tool and API tests pass.
- **SC-002**: Full test suite remains warning-free.
- **SC-003**: Bootstrap creates at most one active memory pack and no full docs context pack.

## Assumptions

- Agents can call docs context-pack separately when route hints indicate official docs are needed.
