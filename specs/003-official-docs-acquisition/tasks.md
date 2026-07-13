# Tasks: Official Docs Acquisition

**Input**: Design documents from `/specs/003-official-docs-acquisition/`

**Prerequisites**: spec.md, plan.md, research.md, data-model.md, contracts/

**Tests**: Required for acquisition validation and crawl plan contracts.

## Phase 1: Setup

- [x] T001 Create `second-brain/corpora/acquisitions/` and `second-brain/corpora/crawl-plans/`
- [x] T002 Add `schemas/acquisition-manifest.schema.yaml`
- [x] T003 Add `schemas/crawl-plan.schema.yaml`
- [x] T004 [P] Add acquisition fixture files in `tests/fixtures/`

---

## Phase 2: User Story 1 - Register a Manual Docs Import (Priority: P1) MVP

**Goal**: Manual local docs imports can be validated and represented with an
acquisition manifest.

**Independent Test**: A local docs folder dry-run produces counts, warnings, and
readiness status.

- [x] T005 [US1] Implement `scripts/validate_acquisition.py`
- [x] T006 [P] [US1] Add tests for local dry-run validation in `tests/test_acquisition.py`
- [x] T007 [US1] Add Unity 6.3 acquisition manifest example in `second-brain/corpora/acquisitions/unity-6.3.yaml`
- [x] T008 [US1] Validate planned vs available corpus path rules against `second-brain/corpora/registry.yaml`

---

## Phase 3: User Story 2 - Track Acquisition Runs (Priority: P2)

**Goal**: Dry-runs and future imports have inspectable run records.

**Independent Test**: A dry-run writes or prints a run report with stable fields.

- [x] T009 [US2] Add `--out` support to `scripts/validate_acquisition.py`
- [x] T010 [P] [US2] Add acquisition run report tests in `tests/test_acquisition.py`
- [x] T011 [US2] Document acquisition run lifecycle in `second-brain/docs/acquisition-workflow.md`

---

## Phase 4: User Story 3 - Prepare for Official Website Crawling (Priority: P3)

**Goal**: Crawl/download behavior is governed by plan files before any crawler
automation exists.

**Independent Test**: A Codex docs crawl plan validates allowed domains, output
path, and approval status.

- [x] T012 [US3] Implement `scripts/create_crawl_plan.py`
- [x] T013 [P] [US3] Add crawl plan validation tests in `tests/test_acquisition.py`
- [x] T014 [US3] Add Codex crawl plan example in `second-brain/corpora/crawl-plans/codex-docs.yaml`
- [x] T015 [US3] Document no-live-scraping policy in `second-brain/docs/acquisition-workflow.md`

---

## Phase 5: Polish

- [x] T016 Run quickstart scenarios from `specs/003-official-docs-acquisition/quickstart.md`
- [x] T017 Run full test suite and record warnings
- [x] T018 Review acquisition artifacts for source/version/snapshot/authority metadata

## Dependencies & Execution Order

- Phase 1 before all stories.
- US1 is MVP.
- US2 depends on US1 validation output.
- US3 can run after Phase 1, but should not implement crawling yet.

## Implementation Strategy

1. Validate local manual imports first.
2. Record run manifests.
3. Add crawl plan contracts without crawler execution.
4. Keep retrieval free of live scraping.
