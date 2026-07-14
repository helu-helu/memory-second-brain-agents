# Feature Specification: MCP Post-Restructure Validation

**Feature Branch**: `015-mcp-post-restructure-validation`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User approved the next step after feature 014: validate Codex/MCP access after the physical runtime restructure.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Verify Codex Can Still Use The MCP Server (Priority: P1)

As the project owner, I need confidence that Codex can still connect to the Second Brain MCP server after runtime modules moved into packages.

**Why this priority**: Feature 014 changed physical module locations. The most important risk is that agent access still works through the same MCP entrypoint and tool names.

**Independent Test**: Start or import the MCP entrypoint and confirm the known tool surface remains available without changing the Codex MCP command.

**Acceptance Scenarios**:

1. **Given** feature 014 has moved runtime modules, **When** the MCP entrypoint imports, **Then** it does not fail on legacy module paths.
2. **Given** Codex uses the existing MCP command, **When** tools are inspected, **Then** existing tool names are still present.

---

### User Story 2 - Validate One Representative Runtime Query (Priority: P2)

As an agent user, I need one small representative query to prove docs routing, runtime context, and context-pack output still work after restructure.

**Why this priority**: Passing imports is not enough. The project needs evidence that the path from agent question to usable context still works.

**Independent Test**: Use a Unity 6.3 multiplayer camera query and confirm route/context/context-pack behavior returns bounded, cited, runtime-backed output or a clear degraded warning.

**Acceptance Scenarios**:

1. **Given** the query asks about creating a camera per user in Unity 6.3 multiplayer, **When** the MCP/API path is exercised, **Then** Unity 6.3 routing is selected or a clarification/degraded warning is reported.
2. **Given** runtime context is available, **When** a context pack is built, **Then** it uses runtime-backed mode and remains bounded.

---

### User Story 3 - Record Validation Evidence (Priority: P3)

As a maintainer, I need the validation result recorded so future agents know whether MCP is ready or what remains blocked.

**Why this priority**: Without a short handoff/status record, future work repeats the same smoke tests and uncertainty.

**Independent Test**: Project status or a feature validation note records the exact checks, dates, outcomes, and any blocked real-runtime checks.

**Acceptance Scenarios**:

1. **Given** validation completes, **When** a future agent reads feature 015 artifacts, **Then** it can see which MCP checks passed and which were mocked or runtime-heavy.
2. **Given** a real-runtime check cannot run, **When** status is recorded, **Then** the blocker and safe small-data retry path are documented.

### Edge Cases

- Real runtime MCP validation may load Qdrant, embeddings, Mem0, or model providers and can timeout; use small representative checks first.
- MCP stdio must not be polluted by API server logs.
- Codex MCP configuration must not change unless the existing command is broken.
- Validation must not scan the full Unity docs corpus.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The feature MUST validate that `second_brain_mcp.py` remains the stable MCP entrypoint.
- **FR-002**: The feature MUST verify existing MCP tool names are still available.
- **FR-003**: The feature MUST validate a small representative Unity 6.3 query through route/context/context-pack behavior.
- **FR-004**: The feature MUST distinguish mocked smoke checks from real-runtime checks.
- **FR-005**: The feature MUST record status and blockers in project documentation.
- **FR-006**: The feature MUST NOT rename MCP tools, REST routes, `second-brain/`, or `db/`.
- **FR-007**: The feature MUST NOT require a full official-docs corpus scan.

### Key Entities

- **MCP Entrypoint**: The stable script Codex uses to expose Second Brain tools.
- **Tool Surface**: The list of MCP tool names that agents can call.
- **Representative Query**: A small Unity 6.3 task query used for validation.
- **Validation Evidence**: A documented record of checks, outcomes, warnings, and blockers.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: MCP import/tool-surface smoke passes with the existing entrypoint.
- **SC-002**: At least one Unity 6.3 representative query is validated through the smallest safe route/context/context-pack path.
- **SC-003**: Validation completes without scanning the full Unity corpus.
- **SC-004**: Project status clearly reports whether MCP is ready, degraded, or blocked.
- **SC-005**: No MCP tool names, REST routes, or storage paths are renamed.

## Assumptions

- Feature 014 restructure is complete and tests pass.
- Existing Codex MCP setup remains the intended primary access path.
- If real-runtime validation is too expensive or times out, a mocked runtime smoke plus documented blocker is acceptable until the user opts into heavier validation.
