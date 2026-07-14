# Implementation Plan: Experience Extraction

**Branch**: `006-experience-extraction` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/006-experience-extraction/spec.md`

## Summary

Add a deterministic extraction workflow that reads evidence files such as context
packs or source documents and creates candidate lessons, skill candidates, and
extraction-run records. The MVP is intentionally conservative: it creates
reviewable candidates only and never activates memory or skills.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: PyYAML, pytest. No new dependencies.

**Storage**: Candidate lessons under `second-brain/memory/lessons/`, skill
candidates under `second-brain/skills/candidates/`, run records under
`second-brain/memory/extraction-runs/`.

**Testing**: pytest.

**Target Platform**: Local Windows development environment.

**Project Type**: Local scripts + file-first artifacts.

**Performance Goals**: Extraction runs quickly on one evidence file and avoids
large corpus scans.

**Constraints**: Candidate-only, no activation, no LLM dependency in MVP.

**Scale/Scope**: One evidence file per run in MVP.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Extraction creates personal reusable
  experience candidates.
- **Provenance and governance**: PASS. Every extraction has evidence and run
  records.
- **File-first compatibility**: PASS. Outputs are Markdown/YAML files.
- **Retrieval quality**: PASS. Context packs can become evidence, not hidden
  memory.
- **Versioned corpus routing**: PASS. Evidence can retain corpus/source paths.
- **Script determinism**: PASS. MVP uses deterministic scripts.

## Project Structure

### Documentation (this feature)

```text
specs/006-experience-extraction/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── extraction-output.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
└── extract_experience.py

second-brain/
├── memory/
│   ├── lessons/
│   └── extraction-runs/
└── skills/
    └── candidates/

tests/
└── test_experience_extraction.py
```

**Structure Decision**: Add one deterministic extraction script first. Keep LLM
extraction out of scope.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Deterministic heuristic extraction | Needed to prove artifact workflow without LLM cost/risk | Manual-only examples do not validate pipeline behavior |
