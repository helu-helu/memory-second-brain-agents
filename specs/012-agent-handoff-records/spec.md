# Feature Specification: Agent Handoff Records

**Feature Branch**: `012-agent-handoff-records`

**Created**: 2026-07-14

**Status**: Draft

**Input**: Continue by adding file-first handoff records so agents can leave task outcomes as evidence for future extraction and review.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Record Task Handoff (Priority: P1)

As an agent finishing meaningful work, I want to record a concise handoff with summary, files, decisions, and follow-ups so future agents can learn from the completed task.

**Why this priority**: Experience extraction works better when completed work leaves structured evidence.

**Independent Test**: Calling the script, access helper, or API writes a Markdown handoff with YAML frontmatter.

**Acceptance Scenarios**:

1. **Given** a title and summary, **When** a handoff is recorded, **Then** a file is created under `second-brain/memory/handoffs/`.
2. **Given** missing title or summary, **When** a handoff is requested, **Then** it is rejected.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST record handoffs as Markdown files with YAML frontmatter.
- **FR-002**: Handoff records MUST include id, title, status, agent, created_at, files, decisions, and followups.
- **FR-003**: System MUST expose handoff recording through script, access helper, REST API, and MCP.
- **FR-004**: System MUST reject empty title or summary.
- **FR-005**: Handoff tests MUST use small fixtures and avoid corpus scans.

### Key Entities *(include if feature involves data)*

- **AgentHandoff**: End-of-task evidence record for future extraction.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Script, access helper, and API tests pass.
- **SC-002**: Full test suite remains warning-free.
- **SC-003**: Generated handoff files are readable standalone Markdown.

## Assumptions

- Handoffs are evidence, not active memory.
- Extraction/review will decide later whether a handoff becomes a lesson or skill candidate.
