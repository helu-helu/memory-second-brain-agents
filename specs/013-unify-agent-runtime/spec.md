# Feature Specification: Unify Agent Runtime

**Feature Branch**: `013-unify-agent-runtime`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Choose whether to separate the new second-brain work from the original project or merge both into one, then update spec-kit with a clear starting phase and completion phase before implementation."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Establish One Source Of Truth (Priority: P1)

As the user, I want the existing agent memory/RAG runtime and the new file-first second-brain layer unified into one project direction so agents do not choose between competing retrieval paths.

**Why this priority**: This removes the core ambiguity discovered during MCP testing: file-first context packs were using lexical/manual retrieval while the original project already had model-backed RAG and memory.

**Independent Test**: Can be tested by producing a complete capability map that classifies every existing spec and runtime capability as reuse, extend, replace, or drop.

**Acceptance Scenarios**:

1. **Given** specs 001-012 and the original runtime modules, **When** the capability map is reviewed, **Then** every capability has one owner and one disposition.
2. **Given** a retrieval capability appears in both file-first scripts and `agent_core`, **When** the decision is recorded, **Then** the runtime source of truth is `agent_core` and the file-first path is audit/export/fallback only.

---

### User Story 2 - Define Unified Agent Contracts (Priority: P2)

As an agent or tool client, I want a stable contract for memory search, knowledge search, context building, context-pack export, and handoff recording so API and MCP behavior stay aligned.

**Why this priority**: A single project still fails if REST, MCP, scripts, and context builders expose slightly different semantics.

**Independent Test**: Can be tested by validating that each operation has required inputs, outputs, error states, provenance fields, and quality signals.

**Acceptance Scenarios**:

1. **Given** a user query, **When** the context contract is applied, **Then** the result includes memory hits, knowledge hits, selected corpora, source metadata, confidence, warnings, and a trace id.
2. **Given** Qdrant, Mem0, or a model provider is unavailable, **When** a contract operation runs, **Then** it returns a bounded degraded result with explicit warnings instead of silently using an unrelated retrieval path.

---

### User Story 3 - Cut Over Without Rewrite (Priority: P3)

As a maintainer, I want the file-first workflows to call the existing runtime through thin adapters so the project becomes simpler without a deep rewrite.

**Why this priority**: The goal is consolidation, not redesigning all memory, RAG, model routing, API, and MCP behavior at once.

**Independent Test**: Can be tested by one end-to-end query path: file/source registration -> indexing or retrieval -> context build -> API/MCP response -> context-pack audit snapshot.

**Acceptance Scenarios**:

1. **Given** a Unity 6.3 query through MCP and API, **When** the unified path runs, **Then** both interfaces use the same runtime behavior and return equivalent selected sources.
2. **Given** a duplicate lexical/manual retrieval path remains, **When** production access is inspected, **Then** it is marked deprecated, unreachable from the normal agent path, or replaced by a runtime-backed adapter.

---

### Edge Cases

- Qdrant is not running or has no relevant collection.
- Mem0 memory search is unavailable or returns no results.
- The corpus registry routes to a version that has not been indexed.
- A query is ambiguous across Unity versions or across product families.
- Existing specs assume file-first retrieval as the engine rather than as an audit/export layer.
- Context-pack output is requested before runtime retrieval is available.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST treat the original `agent_core` runtime as the source of truth for knowledge retrieval, personal memory, context building, and model capability routing.
- **FR-002**: System MUST treat `second-brain/` as a file-first data, audit, review, and spec workspace rather than as a second independent retrieval runtime.
- **FR-003**: System MUST classify each spec from 001 through 012 as reuse, extend, replace, or drop against the unified runtime direction.
- **FR-004**: System MUST define a unified agent context contract covering query, route, selected/excluded corpora, knowledge hits, memory hits, source metadata, confidence, warnings, trace id, and generated context-pack path when exported.
- **FR-005**: System MUST align REST API, MCP tools, scripts, and context builder behavior to the same operation semantics.
- **FR-006**: System MUST keep lexical/file-first retrieval only as fallback, audit, or deterministic export unless explicitly promoted by a future spec.
- **FR-007**: System MUST provide degraded behavior for unavailable vector DB, memory store, model provider, missing corpus index, and ambiguous routing.
- **FR-008**: System MUST preserve current user-facing MCP/API capabilities during consolidation unless a capability is explicitly deprecated with a replacement.
- **FR-009**: System MUST include validation scenarios that use small representative data rather than scanning the full official docs corpus in routine tests.
- **FR-010**: Durable memory or skill artifacts MUST include provenance, status, confidence, scope, and version metadata when the feature creates or changes long-term artifacts.
- **FR-011**: Retrieval-facing features MUST produce bounded context packs with ranked sources rather than unbounded raw search output.
- **FR-012**: Official documentation features MUST register corpora with vendor, product, version, authority, mutability, update policy, and status before retrieval.

### Key Entities *(include if feature involves data)*

- **RuntimeCapability**: A memory, retrieval, context, ingestion, API, MCP, or script capability that needs one owner and one disposition.
- **CapabilityDisposition**: The consolidation decision for a capability: reuse, extend, replace, drop, deprecate, or fallback-only.
- **UnifiedContextResult**: Agent-facing result containing routed query data, memory hits, knowledge hits, quality signals, warnings, and trace metadata.
- **ContextPackSnapshot**: File-first Markdown/YAML artifact exported from a runtime result for audit, review, and reuse.
- **IntegrationGap**: A missing or conflicting behavior that blocks cutover until resolved.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of specs 001-012 are mapped to a reuse, extend, replace, or drop decision before integration begins.
- **SC-002**: 0 production retrieval capabilities have more than one active source of truth after completion.
- **SC-003**: At least 20 representative retrieval/context cases validate route, source selection, degraded behavior, and context-pack boundaries before completion.
- **SC-004**: A single end-to-end validation demonstrates API and MCP calls using the same runtime behavior for one documentation query and one memory-aware context query.
- **SC-005**: Routine validation completes on small representative fixtures without scanning the full Unity documentation corpus.
- **SC-006**: For retrieval features, representative queries return a usable context pack with cited sources and no more than the configured source limit.
- **SC-007**: For multi-corpus documentation features, representative queries route to the intended corpus/version or report a clarification need.

## Assumptions

- The project will merge the two layers into one repository/runtime direction rather than splitting them into separate projects.
- `agent_core` remains the runtime home for memory, knowledge, context, and model routing.
- `second-brain/` remains valuable as file-first workspace for corpora registry, review lifecycle, active skills, handoffs, and audit snapshots.
- This feature is limited to consolidation contracts and thin integration; deep RAG tuning, provider replacement, production auth, and full migration of large corpora are future work.
- Existing tests may be updated when they encode the old duplicated behavior, but changes must be explained by the capability map.
