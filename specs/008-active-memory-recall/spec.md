# Feature Specification: Active Memory Recall

**Feature Branch**: `008-active-memory-recall`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Continue the second-brain plan by letting agents retrieve a bounded pack of active personal lessons and skills for the current task after candidates have been reviewed and activated."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Build Active Memory Pack (Priority: P1)

As an agent working for the user, I want a small active memory pack for the current task so I can apply approved lessons and skills without scanning every memory file.

**Why this priority**: The project becomes useful only when approved memory is available to agents as bounded context.

**Independent Test**: Given active lessons and skills, a task query returns a Markdown memory pack with ranked relevant items and source paths.

**Acceptance Scenarios**:

1. **Given** one active lesson matching the task query, **When** a memory pack is built, **Then** the pack includes that lesson with status, confidence, path, and guidance.
2. **Given** no active artifact matches the task query, **When** a memory pack is built, **Then** the pack reports no matches without falling back to inactive candidates.

---

### User Story 2 - Keep Recall Bounded and Governed (Priority: P2)

As the user, I want memory recall to include only active artifacts and respect a source limit so agent prompts remain focused and safe.

**Why this priority**: Personal memory can degrade agent output if stale or unreviewed artifacts leak into context.

**Independent Test**: A query with many active matches returns no more than the configured limit and excludes candidate, approved, rejected, and deprecated items.

**Acceptance Scenarios**:

1. **Given** active and non-active artifacts, **When** recall runs, **Then** only active artifacts appear.
2. **Given** more matching active artifacts than the limit, **When** recall runs, **Then** only the highest-ranked items appear.

---

### User Story 3 - Record Recall Quality Signals (Priority: P3)

As the user, I want memory packs to show confidence, match reasons, and warnings so I can judge whether an agent used memory appropriately.

**Why this priority**: A memory pack is a contract with the agent, not a hidden internal lookup.

**Independent Test**: Every generated pack includes query metadata, match count, warnings, and selected memory item reasons.

**Acceptance Scenarios**:

1. **Given** a successful recall, **When** the pack is inspected, **Then** it includes query, created_at, limit, selected count, and quality metadata.
2. **Given** no active matches, **When** the pack is inspected, **Then** it includes a warning that no active memory matched.

### Edge Cases

- Active artifact has missing or malformed frontmatter.
- Active skill copy is missing `source_candidate`.
- Query is empty.
- Limit is zero or too high.
- A large memory directory exists; recall should stay bounded and deterministic.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST build a task-specific memory pack from active lessons and active skills.
- **FR-002**: System MUST exclude candidate, draft, approved, rejected, deprecated, and superseded artifacts from recall.
- **FR-003**: System MUST cap recalled items to a configurable limit with a safe default.
- **FR-004**: System MUST include artifact id, type, path, status, confidence, title or name, trigger, guidance or workflow summary, and match reason for each selected item.
- **FR-005**: System MUST include query, created_at, limit, selected count, and warnings in memory pack metadata.
- **FR-006**: System MUST report no active matches without treating non-active artifacts as fallback memory.
- **FR-007**: System MUST use small representative fixtures for tests and avoid scanning full official docs corpora.
- **FR-008**: Durable memory or skill artifacts MUST include provenance, status, confidence, scope, and version metadata when the feature creates or changes long-term artifacts.

### Key Entities *(include if feature involves data)*

- **ActiveMemoryItem**: A lesson or active skill eligible for recall.
- **MemoryPack**: A bounded Markdown context artifact for one task query.
- **RecallQuality**: Confidence, selected count, warnings, and match reasons.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A memory pack for 100 active artifacts is generated in under 10 seconds using a narrow test fixture.
- **SC-002**: 100% of recalled items have `status: active`.
- **SC-003**: Generated packs never exceed the requested item limit.
- **SC-004**: No-match queries return an explicit warning instead of empty silent output.

## Assumptions

- Personal memory recall is separate from official documentation retrieval.
- The initial interface is a deterministic local script that can later be wrapped by API/MCP.
- Only active lessons and active skills are eligible for agent-facing recall.
