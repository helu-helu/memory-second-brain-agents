# Feature Specification: Versioned Official Docs Agent Experience Layer

**Feature Branch**: `001-agent-experience-layer`

**Created**: 2026-07-13

**Status**: Draft

**Input**: User description: "Create a file-first personal second brain for agents that ingests manually supplied official documentation, supports multiple versioned corpora such as Unity 6.3, Unity 6.5, Python, TypeScript, Codex/OpenAI docs, and other future sources, routes user questions to the right corpus/version, distills lessons and skill candidates, connects to Codex first, and later wraps the same model with API/MCP."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Route Questions to the Right Official Corpus (Priority: P1)

As the user working with Codex, I want an agent to classify my task, choose the
right official documentation corpus and version, and receive a small cited
context pack so it can answer or work without searching every document blindly.

**Why this priority**: The long-term value is version-aware knowledge routing,
not one-off search over Unity files. Unity 6.3 is the first proof corpus.

**Independent Test**: Ask a Unity, Python, TypeScript, or Codex-style question
and verify that the system chooses the expected corpus family/version or asks for
clarification when version/project context is missing.

**Acceptance Scenarios**:

1. **Given** a Unity project is bound to Unity 6.3, **When** Codex asks a Unity
   question without naming a version, **Then** the system searches Unity 6.3
   instead of silently using a newer Unity version.
2. **Given** a query is about Codex customization, **When** retrieval runs,
   **Then** the system routes to the Codex/OpenAI docs corpus instead of language
   or engine docs.
3. **Given** a query could belong to multiple products or versions, **When**
   confidence is low, **Then** the context pack asks for clarification instead of
   pretending the answer is certain.

---

### User Story 2 - Govern Versioned Official Corpora (Priority: P2)

As the user importing official or third-party guidance, I want every corpus and
document to have authority, version, lifecycle status, source provenance, and
update policy so I can trust what agents retrieve later.

**Why this priority**: The project will ingest external guidance manually before
full agent-log ingestion exists. That content must not pollute memory without
traceability.

**Independent Test**: Register Unity 6.3, Unity 6.5 placeholder, Python,
TypeScript, and Codex/OpenAI corpus records and verify that each has authority,
version, update policy, root path or acquisition notes, and status metadata.

**Acceptance Scenarios**:

1. **Given** a MarkItDown-converted Markdown corpus, **When** it is registered,
   **Then** the system records corpus id, vendor, product, version, authority,
   update policy, taxonomy, root path, and status metadata.
2. **Given** docs are refreshable such as Codex/OpenAI docs, **When** they are
   registered, **Then** the system records snapshot date and manual refresh
   policy instead of treating them as immutable.

---

### User Story 3 - Distill Lessons and Skill Candidates (Priority: P3)

As the user, I want the system to propose lessons and skill candidates from
documents or completed work so future agents can reuse experience instead of
starting from scratch.

**Why this priority**: The strategic value is not storing documents; it is turning
documents and work experience into future behavior.

**Independent Test**: Run a demo extraction from a sample guidance document and
verify that proposed lessons and skill candidates are stored as candidate
artifacts with review status and clear triggers.

**Acceptance Scenarios**:

1. **Given** a source document with repeatable guidance, **When** extraction runs,
   **Then** it creates candidate lessons with trigger, scope, confidence, and
   source evidence.
2. **Given** a repeated workflow is detected, **When** a skill candidate is
   proposed, **Then** it includes trigger, workflow, inputs, outputs, scripts,
   examples, eval notes, and failure modes.

---

### User Story 4 - Prepare for API/MCP Access (Priority: P4)

As the user, I want the file-first model to expose clear contracts so Codex can
use it now and MCP/API wrappers can use the same artifacts later.

**Why this priority**: The long-term goal is cross-agent reuse, but the MVP must
avoid premature service complexity.

**Independent Test**: Validate that the context-pack and artifact schemas can be
read from files and mapped to a future MCP/API contract without changing their
meaning.

**Acceptance Scenarios**:

1. **Given** a context pack exists as a file, **When** a future API/MCP wrapper
   reads it, **Then** it can expose the same fields without schema redesign.
2. **Given** a skill candidate is approved, **When** it is exported for Codex,
   **Then** the export keeps metadata and script references intact.

### Edge Cases

- The query mentions a feature name that exists across multiple products or
  versions.
- The best matching documents are API reference pages with little explanatory
  text.
- A source document is converted but missing expected headings or metadata.
- A lesson conflicts with an existing active lesson or preference.
- Retrieval returns many near-duplicates from the same section of the corpus.
- Vector search returns semantically plausible but version-wrong context.
- Codex/OpenAI docs have changed since the last local snapshot.
- A project uses Unity 6.3 while newer Unity 6.5 docs are also available.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a corpus registry for multiple official docs
  sources, including Unity, Python, TypeScript, Codex/OpenAI, and future corpora.
- **FR-002**: System MUST treat `docs/massive/Unity_6_3_Markdown` as an immutable
  Unity 6.3 source corpus and first demo corpus.
- **FR-003**: System MUST support MarkItDown-converted Markdown as the primary
  document input format for the MVP.
- **FR-004**: System MUST maintain corpus metadata including vendor, product,
  version, authority level, update policy, project binding policy, root path or
  acquisition notes, status, and snapshot date when applicable.
- **FR-005**: System MUST maintain source document metadata including source,
  version, checksum, status, taxonomy, visibility, and conversion information.
- **FR-006**: System MUST distinguish source corpus records from distilled
  memory, lessons, preferences, skill candidates, and active skills.
- **FR-007**: System MUST support explicit lifecycle states for durable artifacts:
  draft, candidate, approved, active, deprecated, superseded, and rejected.
- **FR-008**: System MUST provide a Codex-first retrieval path that returns a
  bounded context pack instead of unbounded raw documents.
- **FR-009**: Context packs MUST include query, detected intent, routed corpora,
  excluded corpora, source citations, ranked snippets, quality signals, limits
  used, and clarification needs when applicable.
- **FR-010**: Retrieval MUST support hybrid search planning: exact/BM25-style
  lexical matching plus vector search when available and useful.
- **FR-011**: Unity retrieval MUST prefer the version bound to the current Unity
  project and MUST NOT silently substitute another Unity version.
- **FR-012**: Refreshable docs such as Codex/OpenAI docs MUST record
  `snapshot_date`, `update_policy`, and manual refresh status.
- **FR-013**: The system MUST avoid promoting extracted lessons or skills to
  active status without review.
- **FR-014**: Skill candidates MUST include triggers, workflow, inputs, outputs,
  deterministic script hooks, examples, eval notes, and failure modes.
- **FR-015**: Deterministic repeated operations MUST be scriptable, including
  schema validation, index generation, frontmatter extraction, and context-pack
  assembly.
- **FR-016**: All primary memory and skill artifacts MUST be written in English.

### Key Entities *(include if feature involves data)*

- **Corpus**: A registered official documentation source with vendor, product,
  version, authority, update policy, and status.
- **ProjectBinding**: A project-specific preference that chooses the default
  corpus/version for a product such as Unity.
- **QueryRoute**: The selected corpus/corpora, version assumptions, exclusions,
  and clarification state for a user or agent query.
- **SourceDocument**: A converted or imported document with provenance,
  taxonomy, checksum, lifecycle status, and corpus membership.
- **DocumentChunk**: A retrievable portion of a source document with heading,
  path, rank signals, and optional embedding metadata.
- **ContextPack**: A bounded agent-facing retrieval result containing query
  interpretation, ranked sources, snippets, quality signals, and warnings.
- **Lesson**: A scoped behavioral rule with trigger, source evidence, confidence,
  status, and failure modes.
- **Preference**: A user-specific working preference with scope, confidence, and
  status.
- **SkillCandidate**: A repeatable workflow proposed for reuse, including
  procedure, scripts, examples, eval notes, and review state.
- **ExtractionRun**: A record of a document/task distillation attempt, inputs,
  outputs, model/script used, and review result.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A representative Unity query routes to the project-bound Unity
  version and returns a context pack with no more than 12 primary sources and
  clear source citations.
- **SC-002**: Representative Codex, Python, and TypeScript queries route to the
  expected corpus family or ask for clarification when version context is absent.
- **SC-003**: At least 95% of registered source documents include required
  provenance, status, checksum, and taxonomy fields.
- **SC-004**: A demo imported document can move from converted source to candidate
  lesson and skill candidate without manual file reshaping.
- **SC-005**: A reviewer can tell whether each retrieved item is source context,
  candidate memory, or active memory in under 30 seconds.
- **SC-006**: Future API/MCP wrappers can expose the context-pack fields without
  changing the file-first artifact schema.

## Assumptions

- Unity 6.3 documentation is fixed for this project version and will not be
  edited by Unity after import. Unity 6.5 and later versions are separate corpora.
- The existing project remains Python-based with FastAPI, MCP bridge, Qdrant, and
  script-driven ingestion.
- MarkItDown conversion happens before this MVP receives documents; conversion
  validation and normalization are in scope, but building MarkItDown itself is
  not.
- Codex is the first agent client and the first non-engine documentation corpus.
  Other agents should use the same contracts
  later through MCP/API.
- Vector search is desirable when it improves retrieval quality, but exact terms,
  headings, API symbols, and metadata filters remain required quality controls.
