# Feature Specification: Physical Runtime Restructure

**Feature Branch**: `014-physical-runtime-restructure`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Delete the root README.md first so the project is not anchored to the old architecture, consult an expert, then plan and fix the structural mistake."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Make Runtime Ownership Legible (Priority: P1)

As the project owner, I need the physical folder structure to show which part owns runtime memory, RAG, context building, access adapters, and file-first workspace artifacts so future agents do not follow stale README-era assumptions.

**Why this priority**: The current structure works functionally, but it does not clearly express the architecture agreed during consolidation. Without this, future work will keep reintroducing duplicated retrieval and unclear ownership.

**Independent Test**: A maintainer can inspect the feature artifacts and current import surface and identify the intended runtime owner, file workspace owner, adapters, compatibility shims, and stop rules without relying on the deleted root README.

**Acceptance Scenarios**:

1. **Given** the root README has been removed, **When** a maintainer reads this feature's plan and migration map, **Then** they can identify the target package layout and the order of safe migration steps.
2. **Given** feature 013 already unified context contracts, **When** feature 014 is reviewed, **Then** it is scoped to physical structure and compatibility only, not new retrieval behavior.

---

### User Story 2 - Preserve Agent Access While Moving Modules (Priority: P2)

As a Codex/MCP consumer of this project, I need existing imports, API routes, MCP tool names, and file paths to continue working while internals move into clearer packages.

**Why this priority**: The project is already usable through scripts, API, and MCP. A folder cleanup that breaks agent access would be worse than the existing messy structure.

**Independent Test**: Compatibility checks prove that public imports such as `from agent_core import MemoryManager, KnowledgeBase, ContextBuilder`, existing API imports, and MCP import smoke still pass after each migration step.

**Acceptance Scenarios**:

1. **Given** a module has moved to a new package, **When** old public import paths are used, **Then** they still resolve through documented compatibility shims.
2. **Given** MCP is configured for Codex, **When** the MCP server imports its tool definitions, **Then** existing tool names and argument contracts remain unchanged.

---

### User Story 3 - Retire Stale Structure Safely (Priority: P3)

As a maintainer, I need deprecated legacy module paths to be documented and kept only as shims until a later feature proves no external caller still depends on them.

**Why this priority**: The goal is a cleaner structure, not an uncontrolled delete. Safe retirement requires evidence and a future deprecation window.

**Independent Test**: Deprecated paths are listed with replacements, tests cover public compatibility, and no shim is removed in this feature.

**Acceptance Scenarios**:

1. **Given** a deprecated import path is still present, **When** tests run, **Then** it verifies the path maps to the new implementation.
2. **Given** a future cleanup feature wants to delete shims, **When** it reviews feature 014 artifacts, **Then** it can see which evidence must exist before deletion.

### Edge Cases

- `agent_core/memory.py` cannot coexist with an `agent_core/memory/` package; this migration must happen after compatibility tests exist and must preserve `agent_core.memory` as a public import path.
- Restructuring must not move `second-brain/` to a new storage path because it is already the file-first bounded workspace used by scripts, specs, and generated artifacts.
- Restructuring must not rename REST routes or MCP tools because external agent configuration can depend on those names.
- Tests must use small representative fixtures and import smoke checks, not full official documentation corpora.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST define a target physical structure that separates runtime packages, adapter entrypoints, deterministic scripts, and file-first workspace artifacts.
- **FR-002**: The migration plan MUST preserve current public imports for `MemoryManager`, `KnowledgeBase`, and `ContextBuilder`.
- **FR-003**: The migration plan MUST preserve existing REST route names, MCP tool names, and `second-brain/` workspace paths.
- **FR-004**: The migration plan MUST identify compatibility shims for old module paths before implementation moves code.
- **FR-005**: The migration plan MUST treat `agent_core.memory` as the highest-risk migration because the current file-to-package conversion is name-conflicting.
- **FR-006**: Durable planning artifacts MUST include provenance, status, confidence, scope, and version metadata when they define long-term architecture decisions.
- **FR-007**: Restructuring validation MUST use focused import, API, MCP, context-pack, memory, and knowledge tests before any full-suite validation.
- **FR-008**: The feature MUST document stop rules that prevent scope creep into new retrieval behavior, storage relocation, route renaming, or shim deletion.
- **FR-009**: Root README removal MUST be recorded as intentional removal of stale architecture guidance, not accidental documentation loss.

### Key Entities

- **Runtime Package**: A package under `agent_core/` that owns runtime behavior such as RAG, memory, context, access, or MCP helper logic.
- **Compatibility Shim**: A legacy import path that forwards to a new implementation path while callers migrate.
- **Adapter Entrypoint**: A script, REST server, or MCP server file that exposes runtime behavior without owning core logic.
- **File-First Workspace**: The governed `second-brain/` folder holding reviewable data, audit, registry, and generated artifacts.
- **Migration Step**: A bounded move with tests, public import preservation, and an explicit stop rule.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of identified public import paths remain usable after each completed migration step.
- **SC-002**: API and MCP import smoke checks pass without route or tool renames.
- **SC-003**: Focused tests for memory, knowledge, context-pack, API, and MCP pass before any full-suite run.
- **SC-004**: No full-corpus documentation scan is required to validate this restructure.
- **SC-005**: At least one migration map documents every deprecated path, replacement path, owner, risk level, and validation command.
- **SC-006**: No compatibility shim is removed during feature 014.

## Assumptions

- Feature 013 remains complete and is not reopened for physical folder restructure.
- The root README was deleted because it encoded stale architecture direction; a new README or ADR may be created after feature 014 has implemented the new structure.
- `second-brain/` remains the file-first workspace instead of being moved under `data/`.
- `api/api_server.py`, `second_brain_mcp.py`, and `scripts/` remain adapter or wrapper locations during this feature.
- The project continues using the current Python runtime, pytest validation style, LlamaIndex/Qdrant/Mem0 runtime concepts, and file-first governance model.
