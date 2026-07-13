# Tasks: Official Docs Crawler

**Input**: Design documents from `/specs/004-official-docs-crawler/`

**Prerequisites**: spec.md, plan.md, research.md, data-model.md, contracts/

**Tests**: Required. No test may use live internet.

## Phase 1: Setup

- [ ] T001 Add crawl fixture site in `tests/fixtures/crawl-site/`
- [ ] T002 Add crawl run contract test in `tests/test_crawler.py`
- [ ] T003 Add crawler quickstart docs in `second-brain/docs/crawler-workflow.md`

---

## Phase 2: User Story 1 - Crawl from an Approved Plan (Priority: P1) MVP

**Goal**: Crawler reads approved plans and refuses draft plans by default.

- [ ] T004 Implement `scripts/crawl_official_docs.py`
- [ ] T005 [P] [US1] Add tests for refusing draft plans in `tests/test_crawler.py`
- [ ] T006 [P] [US1] Add tests for allowed-domain enforcement in `tests/test_crawler.py`

---

## Phase 3: User Story 2 - Create a Local Snapshot (Priority: P2)

**Goal**: Crawler saves fetched HTML pages under the output path.

- [ ] T007 [US2] Add local HTTP server test fixture in `tests/test_crawler.py`
- [ ] T008 [US2] Save fetched pages to stable local paths in `scripts/crawl_official_docs.py`
- [ ] T009 [US2] Write crawl run manifest under `second-brain/corpora/acquisitions/`
- [ ] T010 [US2] Enforce `max_pages` and record limit warnings

---

## Phase 4: User Story 3 - Prepare Markdown Conversion (Priority: P3)

**Goal**: Snapshot output is conversion-ready but conversion is not required.

- [ ] T011 [US3] Include intended Markdown output path in crawl run manifest
- [ ] T012 [US3] Document conversion handoff in `second-brain/docs/crawler-workflow.md`
- [ ] T013 [US3] Ensure crawler does not update corpus status to indexed

---

## Phase 5: Polish

- [ ] T014 Run quickstart scenarios from `specs/004-official-docs-crawler/quickstart.md`
- [ ] T015 Run full test suite and record warnings
- [ ] T016 Review crawler artifacts for no-live-retrieval and approved-domain policy

## Dependencies & Execution Order

- Phase 1 before implementation.
- US1 is MVP.
- US2 depends on US1.
- US3 depends on snapshot output.

## Implementation Strategy

1. Implement approved-plan gating first.
2. Add local fixture crawling.
3. Write run manifests.
4. Keep conversion and registry promotion separate.
