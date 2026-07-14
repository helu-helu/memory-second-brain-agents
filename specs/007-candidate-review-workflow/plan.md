# Implementation Plan: Candidate Review Workflow

**Branch**: `007-candidate-review-workflow` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/007-candidate-review-workflow/spec.md`

## Summary

Add a deterministic file-first review workflow that lists candidate lessons and skills, validates lifecycle transitions, records review decisions, and activates only approved artifacts. The first slice is a local script so Codex can operate it directly before API/MCP wrappers are added.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: PyYAML, pytest. No new dependencies.

**Storage**: Markdown/YAML frontmatter artifacts under `second-brain/memory/`, `second-brain/skills/`, and `second-brain/reviews/`.

**Testing**: pytest.

**Target Platform**: Local Windows development environment.

**Project Type**: Local scripts + file-first artifacts.

**Performance Goals**: Review listing handles at least 100 local artifacts in under 10 seconds.

**Constraints**: No activation without approval; invalid transitions must not modify artifacts; preserve candidate provenance.

**Scale/Scope**: Personal local review workflow for generated candidates.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Review decisions protect the user's personal memory from unapproved extraction output.
- **Provenance and governance**: PASS. Lifecycle transitions and decision records are the core feature.
- **File-first compatibility**: PASS. Artifacts remain Markdown/YAML files.
- **Retrieval quality**: PASS. Retrieval is not in scope; reviewed lessons/skills may later improve retrieval usage.
- **Versioned corpus routing**: PASS. Corpus routing is not changed.
- **Script determinism**: PASS. Repeatable lifecycle changes are handled by a deterministic script.

## Project Structure

### Documentation (this feature)

```text
specs/007-candidate-review-workflow/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── review-command.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
└── review_candidate.py

second-brain/
├── reviews/
│   └── decisions/
├── memory/
│   └── lessons/
└── skills/
    ├── candidates/
    └── active/

tests/
└── test_candidate_review.py
```

**Structure Decision**: Add one deterministic lifecycle script first. Keep API/MCP wrappers out of the MVP until the file-first contract is proven.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
