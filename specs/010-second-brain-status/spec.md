# Feature Specification: Second Brain Status

**Feature Branch**: `010-second-brain-status`

**Created**: 2026-07-14

**Status**: Draft

**Input**: Continue by adding a compact status summary so agents and the user can inspect current memory lifecycle state.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Inspect Lifecycle Status (Priority: P1)

As the user or an agent, I want one compact status response showing active memory, pending candidates, review decisions, generated memory packs, and registered corpora.

**Why this priority**: After adding extraction, review, activation, and recall, the system needs a quick health/status view.

**Independent Test**: Calling the status helper or API returns memory, reviews, and corpora summary sections.

**Acceptance Scenarios**:

1. **Given** existing second-brain artifacts, **When** status is requested, **Then** counts by lifecycle status and artifact type are returned.
2. **Given** memory packs or review decisions exist, **When** status is requested, **Then** latest artifact paths are included.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST summarize reviewable memory artifacts by status and type.
- **FR-002**: System MUST summarize active skills.
- **FR-003**: System MUST summarize review decision count and latest decision paths.
- **FR-004**: System MUST summarize memory pack paths.
- **FR-005**: System MUST summarize registered corpora by status and product.
- **FR-006**: System MUST expose status through access tools, REST API, and MCP.

### Key Entities *(include if feature involves data)*

- **SecondBrainStatus**: Compact summary of memory, reviews, and corpora.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Status access-tool and API tests pass.
- **SC-002**: Status response does not scan official docs corpus contents.
- **SC-003**: Full test suite remains warning-free.

## Assumptions

- Status is a summary, not a dashboard UI.
- Latest artifacts are represented by paths, not full file contents.
