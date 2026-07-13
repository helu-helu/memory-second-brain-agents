# Feature Specification: Official Docs Crawler

**Feature Branch**: `004-official-docs-crawler`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Continue after official docs acquisition by adding a controlled crawler/downloader that reads approved crawl plans, fetches only allowed official domains, snapshots pages locally, converts or prepares content for Markdown, and updates acquisition run records without ever live-scraping during retrieval."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Crawl from an Approved Plan (Priority: P1)

As the user, I want the system to crawl official documentation only from an
approved crawl plan so docs snapshots are controlled, reproducible, and safe.

**Why this priority**: Crawl automation is useful only if it respects the
governance created in the acquisition feature.

**Independent Test**: Run the crawler against a local test website using an
approved crawl plan and verify that only allowed pages are saved.

**Acceptance Scenarios**:

1. **Given** a crawl plan has `approval_status: approved`, **When** the crawler
   runs, **Then** it fetches only URLs under `allowed_domains`.
2. **Given** a crawl plan is `draft`, **When** the crawler runs, **Then** it
   refuses to crawl unless explicitly run in dry-run mode.
3. **Given** a linked page points outside allowed domains, **When** the crawler
   sees it, **Then** it skips that URL and records a warning.

---

### User Story 2 - Create a Local Snapshot (Priority: P2)

As the user, I want crawled docs saved as a local snapshot with stable paths so
future retrieval and conversion use reproducible files rather than live web
content.

**Why this priority**: Retrieval must never depend on live web state.

**Independent Test**: Crawl a local test site and verify HTML files and a run
manifest are written under the configured output path.

**Acceptance Scenarios**:

1. **Given** pages are fetched successfully, **When** the crawl completes, **Then**
   each page is saved under the snapshot output path.
2. **Given** duplicate or fragment-only URLs appear, **When** the crawler runs,
   **Then** it deduplicates them before fetching.
3. **Given** the crawl reaches `max_pages`, **When** more links remain, **Then**
   it stops and records a limit warning.

---

### User Story 3 - Prepare Markdown Conversion (Priority: P3)

As the maintainer, I want the crawler output to be compatible with the existing
HTML-to-Markdown/MarkItDown flow so snapshots can become searchable corpora.

**Why this priority**: Crawling is only useful if the result can enter the
existing acquisition and retrieval pipeline.

**Independent Test**: After crawling, verify that snapshot metadata points to
HTML files and a conversion-ready output directory.

**Acceptance Scenarios**:

1. **Given** crawled HTML exists, **When** the run manifest is inspected, **Then**
   it lists saved HTML files and the intended Markdown output directory.
2. **Given** conversion is not run, **When** the crawl finishes, **Then** the
   corpus registry remains planned or snapshot-only rather than indexed.

### Edge Cases

- A page returns a non-200 response.
- A page has links with fragments, query strings, or relative paths.
- Multiple links point to the same normalized URL.
- Crawl plan output path already exists.
- Crawl plan has `approval_status: draft`.
- Allowed domain includes subpaths but page links escape the intended section.
- Network is unavailable.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Crawler MUST read crawl plans created by the acquisition feature.
- **FR-002**: Crawler MUST refuse non-approved plans unless running dry-run mode.
- **FR-003**: Crawler MUST fetch only URLs whose host is in `allowed_domains`.
- **FR-004**: Crawler MUST respect `max_pages`.
- **FR-005**: Crawler MUST deduplicate normalized URLs before fetching.
- **FR-006**: Crawler MUST save fetched pages to the plan output path.
- **FR-007**: Crawler MUST write an acquisition/crawl run manifest with fetched
  count, skipped URLs, warnings, and output paths.
- **FR-008**: Crawler MUST NOT be called from retrieval or context-pack generation.
- **FR-009**: Tests MUST use a local/mock HTTP server or fixture files, not live
  internet.
- **FR-010**: Crawler output MUST be compatible with later HTML-to-Markdown or
  MarkItDown conversion.

### Key Entities

- **CrawlPlan**: Approved policy file from `second-brain/corpora/crawl-plans/`.
- **CrawlRun**: One crawler execution result.
- **FetchedPage**: Saved HTML file with source URL and status.
- **SkippedUrl**: URL skipped due to domain, duplicate, non-HTML, or limit.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Crawler refuses draft plans by default.
- **SC-002**: Local test crawl saves expected pages and skips off-domain links.
- **SC-003**: Crawl run manifest includes fetched count, skipped count, warnings,
  and output path.
- **SC-004**: No test requires live internet.
- **SC-005**: Full test suite passes after crawler implementation.

## Assumptions

- The acquisition feature has already created crawl plan contracts.
- Initial crawler may save HTML snapshots only; Markdown conversion can remain a
  follow-up step or call existing conversion scripts later.
- Crawl politeness is enforced by simple request/page limits in the MVP.
- Live retrieval still uses local snapshots only.
