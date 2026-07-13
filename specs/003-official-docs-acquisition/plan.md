# Implementation Plan: Official Docs Acquisition

**Branch**: `003-official-docs-acquisition` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/003-official-docs-acquisition/spec.md`

## Summary

Add file-first acquisition governance for official documentation corpora. The MVP
supports manual local imports and dry-run validation, records acquisition
manifests, and defines crawl/download plan contracts without performing live
scraping during retrieval.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: PyYAML, pytest, existing corpus registry scripts. No
new dependencies for MVP.

**Storage**: File-first acquisition manifests and run records under
`second-brain/corpora/`.

**Testing**: pytest plus deterministic script validation.

**Target Platform**: Local Windows development environment.

**Project Type**: Local scripts + file contracts.

**Performance Goals**: Dry-run validation should handle representative folder
samples quickly and avoid reading full massive corpora when a limit is provided.

**Constraints**: No live scraping during retrieval; crawl plans require explicit
approved domains and manual approval status.

**Scale/Scope**: Manual imports now, planned crawl/download contracts next,
automation later.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Better acquisition improves the user's own
  agent documentation base first.
- **Provenance and governance**: PASS. Acquisition manifests preserve source,
  authority, version, status, snapshot, and warnings.
- **File-first compatibility**: PASS. Manifests and reports are YAML/Markdown.
- **Retrieval quality**: PASS. Acquisition feeds trusted corpora into retrieval
  without live scraping.
- **Versioned corpus routing**: PASS. Acquisition writes registry-compatible
  corpus records.
- **Script determinism**: PASS. Validation and manifest generation are scripts.

## Project Structure

### Documentation (this feature)

```text
specs/003-official-docs-acquisition/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── acquisition-manifest.schema.md
│   └── crawl-plan.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
schemas/
├── acquisition-manifest.schema.yaml
└── crawl-plan.schema.yaml

second-brain/corpora/
├── acquisitions/
└── crawl-plans/

scripts/
├── register_corpus.py
├── validate_acquisition.py
└── create_crawl_plan.py

tests/
├── fixtures/
└── test_acquisition.py
```

**Structure Decision**: Keep acquisition artifacts under `second-brain/corpora/`
because they govern corpus availability, not personal memory.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Crawl plan contract before crawler exists | Prevents unsafe ad hoc scraping later | Waiting until crawler implementation risks designing policy after behavior |
