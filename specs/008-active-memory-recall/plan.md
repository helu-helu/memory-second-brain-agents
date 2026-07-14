# Implementation Plan: Active Memory Recall

**Branch**: `008-active-memory-recall` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/008-active-memory-recall/spec.md`

## Summary

Add a deterministic script that builds a bounded Markdown memory pack from active personal lessons and active skills for one task query. The MVP keeps personal memory recall separate from official docs retrieval and uses lexical matching over approved active artifacts only.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: PyYAML, pytest. No new dependencies.

**Storage**: Active lessons under `second-brain/memory/lessons/`, active skills under `second-brain/skills/active/`, generated packs under `second-brain/memory/packs/`.

**Testing**: pytest.

**Target Platform**: Local Windows development environment.

**Project Type**: Local scripts + file-first artifacts.

**Performance Goals**: Generate a pack from 100 active artifacts in under 10 seconds.

**Constraints**: Active-only recall, bounded output, no full official docs scan, no LLM dependency in MVP.

**Scale/Scope**: Personal local active memory recall for agent context.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. This is the first direct agent-facing personal memory recall surface.
- **Provenance and governance**: PASS. Only active reviewed artifacts are recalled.
- **File-first compatibility**: PASS. Memory packs are Markdown/YAML files.
- **Retrieval quality**: PASS. Output is bounded with reasons and warnings.
- **Versioned corpus routing**: PASS. Official docs routing is not changed.
- **Script determinism**: PASS. Recall is deterministic lexical matching.

## Project Structure

### Documentation (this feature)

```text
specs/008-active-memory-recall/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── memory-pack.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
└── build_memory_pack.py

second-brain/
└── memory/
    └── packs/

tests/
└── test_memory_pack.py
```

**Structure Decision**: Add one script and one output directory. API/MCP wrappers can reuse this script after the contract stabilizes.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
