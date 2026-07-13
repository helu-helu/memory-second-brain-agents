# Tasks: Versioned Official Docs Agent Experience Layer

**Input**: Design documents from `/specs/001-agent-experience-layer/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/context-pack.schema.md, quickstart.md

**Tests**: Include validation tasks because retrieval quality and schema safety
are core requirements.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish file-first directories and schemas without changing the
existing runtime behavior.

- [x] T001 Create `schemas/` with YAML schemas for Corpus, ProjectBinding, QueryRoute, SourceDocument, ContextPack, Lesson, Preference, SkillCandidate, and ExtractionRun
- [x] T002 Create `second-brain/corpora/`, `second-brain/inbox/`, `second-brain/sources/`, `second-brain/memory/`, `second-brain/skills/`, `second-brain/indexes/`, and `second-brain/demo/`
- [x] T003 [P] Add `second-brain/README.md` describing artifact classes, lifecycle states, and English-first artifact policy
- [x] T004 [P] Add `.gitkeep` placeholders where needed in empty `second-brain/` directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core validation and demo contracts that all user stories depend on.

**CRITICAL**: No user story work should begin until this phase is complete.

- [x] T005 Implement schema validation helper in `scripts/validate_second_brain.py`
- [x] T006 [P] Implement Markdown frontmatter inspection helper in `scripts/inspect_frontmatter.py`
- [x] T007 [P] Create representative Unity retrieval query set in `tests/fixtures/unity_queries.yaml`
- [x] T008 Create demo corpus registry fixture in `second-brain/demo/corpus-registry.example.yaml`
- [x] T009 Create demo context-pack fixture in `second-brain/demo/context-pack.example.md`
- [x] T010 Add lifecycle/status examples for source documents, lessons, and skill candidates in `second-brain/demo/`

**Checkpoint**: File-first artifacts can be validated before indexing or retrieval.

---

## Phase 3: User Story 1 - Route Questions to the Right Official Corpus (Priority: P1) MVP

**Goal**: Codex can request task context, route to the right official
corpus/version, and receive a bounded context pack with cited sources.

**Independent Test**: Representative Unity, Codex, Python, and TypeScript queries
produce expected corpus routes or clarification needs.

### Tests for User Story 1

- [x] T011 [P] [US1] Add corpus registry contract validation in `tests/test_second_brain_contracts.py`
- [x] T012 [P] [US1] Add context-pack contract validation in `tests/test_second_brain_contracts.py`
- [x] T013 [P] [US1] Add routing quality fixture checks in `tests/test_route_query.py`

### Implementation for User Story 1

- [x] T014 [US1] Add corpus registry loader script in `scripts/load_corpus_registry.py`
- [x] T015 [US1] Add query routing script in `scripts/route_query.py`
- [x] T016 [US1] Add context-pack assembly script in `scripts/build_context_pack.py`
- [x] T017 [US1] Add Unity corpus metadata filters and source-limit handling in `agent_core/`
- [x] T018 [US1] Add Codex-facing context-pack output path under `second-brain/demo/runs/`
- [x] T019 [US1] Document Codex retrieval workflow in `second-brain/docs/codex-context-pack-workflow.md`

**Checkpoint**: User Story 1 is demoable without implementing lesson extraction.

---

## Phase 4: User Story 2 - Govern Versioned Official Corpora (Priority: P2)

**Goal**: Imported MarkItDown Markdown corpora and documents have explicit
authority, version, update policy, metadata, and lifecycle states.

**Independent Test**: A demo Markdown file registers as a SourceDocument with
required metadata and validates successfully.

### Tests for User Story 2

- [x] T020 [P] [US2] Add Corpus schema validation tests in `tests/test_second_brain_contracts.py`
- [x] T021 [P] [US2] Add SourceDocument schema validation tests in `tests/test_registration_scripts.py`

### Implementation for User Story 2

- [x] T022 [US2] Add corpus registration script in `scripts/register_corpus.py`
- [x] T023 [US2] Add document registration script in `scripts/register_source_document.py`
- [x] T024 [US2] Add demo source document metadata in `second-brain/demo/source-document.example.md`
- [x] T025 [US2] Add taxonomy guidance for engines, languages, frameworks, tools, and agent platforms in `second-brain/docs/document-taxonomy.md`

**Checkpoint**: Imported docs can be tracked without being confused with approved memory.

---

## Phase 5: User Story 3 - Distill Lessons and Skill Candidates (Priority: P3)

**Goal**: Documents or task records can produce candidate lessons and skill
candidates with review status.

**Independent Test**: A demo extraction run produces candidate artifacts and does
not activate them automatically.

### Tests for User Story 3

- [x] T026 [P] [US3] Add Lesson and SkillCandidate schema tests in `tests/test_experience_artifacts.py`

### Implementation for User Story 3

- [x] T027 [US3] Add extraction-run template in `second-brain/demo/extraction-run.example.md`
- [x] T028 [US3] Add lesson candidate example in `second-brain/demo/lesson.example.md`
- [x] T029 [US3] Add skill candidate example with script hooks in `second-brain/demo/skill-candidate/SKILL.md`
- [x] T030 [US3] Add review/promote lifecycle documentation in `second-brain/docs/experience-distillation-workflow.md`

**Checkpoint**: Experience distillation is visible and governed, even before automation.

---

## Phase 6: User Story 4 - Prepare for API/MCP Access (Priority: P4)

**Goal**: The file-first contracts can be exposed later through MCP/API without
schema redesign.

**Independent Test**: The context-pack schema maps cleanly to a future MCP tool
response and Codex skill export notes.

### Implementation for User Story 4

- [x] T031 [US4] Add future MCP tool contract notes in `specs/001-agent-experience-layer/contracts/mcp-tools.md`
- [x] T032 [US4] Add Codex skill export guidance in `second-brain/docs/codex-skill-export.md`
- [x] T033 [US4] Add adapter boundary notes in `second-brain/docs/mcp-adapter-boundary.md`

**Checkpoint**: Future API/MCP work has a stable contract target.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Validate the spec-kit setup and keep the MVP small.

- [x] T034 [P] Add project ownership map in `second-brain/docs/project-ownership-map.md`
- [x] T035 Run quickstart validation from `specs/001-agent-experience-layer/quickstart.md`
- [x] T036 Run existing test suite and record any unrelated failures
- [x] T037 Review all new artifacts for English-first language and no active unreviewed memories

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion and blocks all user stories.
- **US1 (Phase 3)**: Depends on Foundational and is the MVP.
- **US2 (Phase 4)**: Depends on Foundational; can run after or alongside US1.
- **US3 (Phase 5)**: Depends on Foundational and benefits from US2 examples.
- **US4 (Phase 6)**: Depends on the context-pack contract from US1.
- **Polish (Phase 7)**: Depends on desired user stories.

### Parallel Opportunities

- T003 and T004 can run in parallel.
- T006 and T007 can run in parallel.
- T010 and T011 can run in parallel.
- T016 and T020 can run in parallel once schemas exist.

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 only.
3. Validate that Codex can consume a bounded Unity context pack.
4. Stop and review retrieval quality before adding extraction automation.

### Incremental Delivery

1. File-first schemas and demo folders.
2. Codex context-pack retrieval.
3. Imported document governance.
4. Lesson and skill candidate distillation.
5. API/MCP adapter contracts.
