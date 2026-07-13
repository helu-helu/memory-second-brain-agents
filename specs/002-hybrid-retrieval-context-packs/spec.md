# Feature Specification: Hybrid Retrieval Context Packs

**Feature Branch**: `002-hybrid-retrieval-context-packs`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "After the multi-corpus MVP, implement the next spec-kit feature for hybrid retrieval behind context packs so agents get higher-quality, version-aware official documentation results from large corpora such as Unity, while preserving the file-first registry and Codex-facing context-pack contract."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Retrieve Relevant Unity Sources (Priority: P1)

As the user asking Codex a Unity task question, I want the system to retrieve
relevant Unity 6.3 documentation using hybrid ranking so the context pack
contains sources that match the actual task, not just generic path keywords.

**Why this priority**: The MVP context pack works, but lexical path matching is
too shallow for production use. The next value unlock is retrieval quality.

**Independent Test**: Ask representative Unity questions and verify that returned
sources are from the project-bound Unity corpus and match the task intent.

**Acceptance Scenarios**:

1. **Given** the project is bound to Unity 6.3, **When** the user asks about the
   Input System, **Then** the context pack ranks Input-related Unity 6.3 sources
   above generic Unity pages.
2. **Given** a Unity query contains exact API names, **When** retrieval runs,
   **Then** exact symbol/path matches contribute to ranking alongside vector
   similarity.
3. **Given** vector results include semantically plausible but version-wrong
   sources, **When** the context pack is built, **Then** those sources are
   excluded or clearly downgraded.

---

### User Story 2 - Explain Retrieval Quality (Priority: P2)

As the user reviewing a context pack, I want each source to include selection
reasons and quality signals so I can judge whether the agent is using good
evidence.

**Why this priority**: Trust depends on seeing why sources were selected,
especially when multiple corpora or versions exist.

**Independent Test**: Generate a context pack and verify every source includes
corpus id, rank, score signals, selected reason, and warnings when applicable.

**Acceptance Scenarios**:

1. **Given** a source is selected by exact path or symbol match, **When** the
   context pack is rendered, **Then** the reason names that signal.
2. **Given** a source is selected mainly by vector similarity, **When** the pack
   is rendered, **Then** the reason states that semantic similarity was the main
   signal.
3. **Given** retrieval confidence is low, **When** the pack is rendered, **Then**
   it includes a clarification or warning rather than pretending certainty.

---

### User Story 3 - Evaluate Retrieval Changes (Priority: P3)

As the maintainer, I want a small retrieval benchmark so future changes to
ranking, embeddings, or indexing do not silently make context packs worse.

**Why this priority**: Retrieval quality is a product requirement. Without an
eval set, vector search can feel better while becoming less reliable.

**Independent Test**: Run the retrieval evaluation script against fixture queries
and see pass/fail results for expected corpus, expected source patterns, source
limit, and warning behavior.

**Acceptance Scenarios**:

1. **Given** a fixture query has expected source path patterns, **When** eval
   runs, **Then** at least one top result matches the expected pattern.
2. **Given** a query is intentionally ambiguous, **When** eval runs, **Then** the
   context pack reports low confidence or clarification need.
3. **Given** source limit is configured, **When** eval runs, **Then** generated
   packs do not exceed that limit.

### Edge Cases

- The query contains common words such as "system" or "manager" that produce
  noisy lexical matches.
- The query uses an API symbol that appears in multiple Unity packages.
- A corpus is registered but not locally available.
- Vector store is unavailable or stale.
- Multiple near-duplicate documents rank highly.
- A query spans multiple products, such as Unity plus TypeScript tooling.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST keep query routing before retrieval and MUST only
  search selected corpora unless the context pack explicitly records expansion.
- **FR-002**: System MUST support hybrid retrieval signals: lexical/path,
  heading/title, exact symbol, metadata filter, and vector similarity when the
  vector index is available.
- **FR-003**: System MUST degrade gracefully to lexical retrieval when vector
  retrieval is unavailable.
- **FR-004**: System MUST preserve the existing context-pack file contract.
- **FR-005**: Context packs MUST include selected corpora, excluded corpora,
  source limit, applied source count, retrieval mode, and quality signals.
- **FR-006**: Each ranked source MUST include a citation path, corpus id,
  relevance level, selection reason, and snippet.
- **FR-007**: Retrieval MUST deduplicate near-identical or same-section sources
  before filling the source limit.
- **FR-008**: Retrieval MUST cap default context packs at 12 sources and MUST NOT
  exceed 20 sources outside an explicit deep-research mode.
- **FR-009**: Retrieval eval fixtures MUST cover Unity, Codex, unknown/ambiguous
  queries, and at least one missing-local-corpus case.
- **FR-010**: Retrieval changes MUST be validated by tests or eval scripts before
  being considered complete.

### Key Entities

- **RetrievalQuery**: Original query plus query route, selected corpora, and
  expected retrieval mode.
- **RetrievalCandidate**: A possible source with lexical, symbol, metadata, and
  vector scores.
- **RankedSource**: A deduplicated, selected source rendered into a context pack.
- **RetrievalEvalCase**: Fixture query with expected corpus, expected source
  patterns, confidence expectations, and source limit.
- **RetrievalEvalRun**: Result of running retrieval eval cases against current
  ranking behavior.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Representative Unity Input queries return at least one Input-related
  source in the top 3 results.
- **SC-002**: Context packs never exceed 12 sources by default or 20 sources with
  an explicit larger limit.
- **SC-003**: All ranked sources include corpus id, citation path, selection
  reason, relevance, and snippet.
- **SC-004**: Retrieval eval covers at least 8 representative queries across
  Unity, Codex, unknown, and missing-corpus scenarios.
- **SC-005**: Full test suite passes after hybrid retrieval changes.

## Assumptions

- The previous feature's corpus registry, query router, and context-pack contract
  are already present.
- Qdrant and the existing `agent_core/knowledge.py` remain the runtime retrieval
  plane.
- The first implementation may use lexical plus metadata ranking before enabling
  vector scoring, as long as the contract names the retrieval mode honestly.
- The Unity 6.3 corpus remains the primary large-corpus quality target.
