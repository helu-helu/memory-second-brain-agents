# Implementation Plan: Official Docs Crawler

**Branch**: `004-official-docs-crawler` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/004-official-docs-crawler/spec.md`

## Summary

Implement a controlled crawler that reads approved crawl plans, fetches only
allowed official domains, saves HTML snapshots locally, and writes crawl run
manifests. The crawler will be tested against local fixtures or a local HTTP
server and will not be part of retrieval.

## Technical Context

**Language/Version**: Python 3.10+

**Primary Dependencies**: Standard library `urllib`, `html.parser`, `http.server`
for tests, PyYAML, pytest. Avoid new dependencies in MVP.

**Storage**: HTML snapshots under crawl plan output path; run manifests under
`second-brain/corpora/acquisitions/`.

**Testing**: pytest with local HTTP server fixtures.

**Target Platform**: Local Windows development environment.

**Project Type**: Local CLI script + file contracts.

**Performance Goals**: Respect `max_pages`; default crawler stays bounded and
does not run unbounded recursive crawls.

**Constraints**: No live internet in tests; no live scraping during retrieval;
only approved crawl plans execute.

**Scale/Scope**: MVP crawler fetches HTML snapshots. Markdown conversion and
registry status promotion can be separate follow-ups.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **Personal-first memory**: PASS. Crawler serves the user's personal docs base.
- **Provenance and governance**: PASS. Crawl plans and run manifests preserve
  source, status, warnings, and output paths.
- **File-first compatibility**: PASS. Plans and run manifests are YAML files.
- **Retrieval quality**: PASS. Crawler improves local sources while retrieval
  remains snapshot-based.
- **Versioned corpus routing**: PASS. Crawler operates on registered corpus ids.
- **Script determinism**: PASS. Crawling is bounded by plan fields and tests.

## Project Structure

### Documentation (this feature)

```text
specs/004-official-docs-crawler/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── crawl-run.schema.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
└── crawl_official_docs.py

tests/
├── fixtures/crawl-site/
└── test_crawler.py

second-brain/corpora/acquisitions/
```

**Structure Decision**: Add one crawler script and local tests. Reuse crawl plan
files from `003`.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Local HTTP server tests | Need realistic link handling without live internet | Pure unit tests would miss URL normalization and fetch behavior |
