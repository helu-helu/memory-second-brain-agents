# Feature Specification: Agent Access Tools

**Feature Branch**: `005-agent-access-tools`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Continue after the crawler by exposing the file-first second-brain capabilities to agents through API/MCP tools. Agents should be able to list corpora, route queries, build context packs, validate acquisition/crawl plans, and inspect generated artifacts without bypassing the file-first source of truth."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Agent Lists and Routes Corpora (Priority: P1)

As an agent connected through the existing API/MCP bridge, I want to list
registered corpora and route a query before retrieval so I can select the right
official docs source and version.

**Why this priority**: Routing and registry access are the minimum useful bridge
from file-first governance to agent runtime behavior.

**Independent Test**: Call the local function/API/MCP wrapper for list corpora
and route query, then verify the response matches the registry and query router.

**Acceptance Scenarios**:

1. **Given** the corpus registry exists, **When** an agent lists corpora, **Then**
   it receives corpus id, product, version, status, and authority metadata.
2. **Given** a Unity query, **When** an agent routes it, **Then** it selects the
   project-bound Unity corpus and excludes newer Unity corpora.

---

### User Story 2 - Agent Builds Context Packs (Priority: P2)

As an agent, I want to request a bounded context pack through an access tool so I
can use official docs without reading source folders directly.

**Why this priority**: Context packs are the main agent-facing retrieval
artifact.

**Independent Test**: Invoke the access tool for a Unity query and verify that a
context pack path, applied source count, corpus id, and warnings are returned.

**Acceptance Scenarios**:

1. **Given** a local Unity corpus is available, **When** an agent builds a context
   pack, **Then** the output file is written under `second-brain/demo/runs/` or a
   configured output path.
2. **Given** a planned corpus has no local root path, **When** an agent builds a
   pack, **Then** the response reports a warning and does not fetch live web
   content.

---

### User Story 3 - Agent Inspects Acquisition and Crawl Status (Priority: P3)

As an agent, I want to inspect acquisition manifests and crawl plans so I can
know whether a corpus is ready for retrieval, planned, or missing local content.

**Why this priority**: Agents need status awareness before deciding whether to
answer, ask for clarification, or request an acquisition step.

**Independent Test**: Invoke status tools for Unity and Codex docs and verify
that Unity reports available acquisition metadata while Codex reports planned or
dry-run crawl state.

**Acceptance Scenarios**:

1. **Given** `unity-6.3` has an acquisition manifest, **When** the agent inspects
   it, **Then** the response includes source, version, authority, and readiness.
2. **Given** `codex-docs` has a crawl plan but no local snapshot, **When** the
   agent inspects it, **Then** it reports planned/draft status instead of
   pretending local docs are available.

### Edge Cases

- API server is not running but file-first scripts work.
- MCP bridge is called with missing or invalid query.
- Context pack output path already exists.
- Corpus registry is malformed.
- A tool tries to mutate active memory without review.
- A crawler plan is draft and an agent requests execution.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Agent access tools MUST reuse file-first scripts/contracts instead
  of duplicating registry, routing, context-pack, acquisition, or crawler logic.
- **FR-002**: System MUST expose list-corpora and route-query behavior through a
  callable Python/API layer suitable for MCP wrapping.
- **FR-003**: System MUST expose build-context-pack behavior and return path,
  source count, selected corpora, and warnings.
- **FR-004**: System MUST expose acquisition/crawl status inspection without
  running crawls by default.
- **FR-005**: Tools MUST NOT live-scrape during retrieval.
- **FR-006**: Tools MUST NOT auto-promote lessons, skills, or memory artifacts.
- **FR-007**: Tool responses MUST be structured and testable.
- **FR-008**: Existing MCP memory/RAG tools MUST remain backward compatible.
- **FR-009**: Errors MUST be user-readable and not hide registry or path
  validation failures.

### Key Entities

- **AgentToolResponse**: Structured response returned to API/MCP callers.
- **CorpusStatus**: Combined registry, acquisition, and crawl-plan status.
- **ContextPackRequest**: Query, limit, mode, client, and output path.
- **ContextPackResult**: Path, selected corpora, applied sources, warnings, and
  retrieval mode.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Agent access tests cover list corpora, route query, build context
  pack, and inspect corpus status.
- **SC-002**: Building a Unity context pack through the access layer returns a
  valid output path and no more than the requested source limit.
- **SC-003**: Inspecting `codex-docs` reports planned/missing local snapshot
  state without network access.
- **SC-004**: Existing tests for API, MCP-adjacent scripts, and retrieval still
  pass.

## Assumptions

- File-first registry, context-pack builder, acquisition, and crawler features
  already exist.
- The first implementation can be a local Python service/helper layer before
  adding new FastAPI endpoints or MCP tool decorators.
- MCP/API exposure should be narrow and backward compatible.
