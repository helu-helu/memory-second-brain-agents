# Feature Specification: Official Docs Acquisition

**Feature Branch**: `003-official-docs-acquisition`

**Created**: 2026-07-14

**Status**: Draft

**Input**: User description: "Create the next spec-kit feature after hybrid retrieval: a controlled acquisition workflow for official documentation corpora. The system should support manual imports now and prepare for future crawl/download from official websites when docs are not available as downloadable archives."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Register a Manual Docs Import (Priority: P1)

As the user, I want to register an official docs corpus that I manually collected
or converted so agents can route to it with clear provenance and version policy.

**Why this priority**: Manual import is the current workflow and must be safe
before crawl/download automation exists.

**Independent Test**: Register a planned or local corpus and verify that the
registry, acquisition manifest, and validation report identify source, product,
version, authority, update policy, and local path state.

**Acceptance Scenarios**:

1. **Given** a local folder of converted Markdown docs, **When** the user
   registers it as a corpus, **Then** the corpus registry records root path,
   authority, version, acquisition method, and status.
2. **Given** a corpus is planned but not yet downloaded, **When** it is
   registered, **Then** retrieval can route to it but context packs report the
   missing local root path.
3. **Given** a corpus is refreshable, **When** it is registered, **Then** the
   record includes snapshot date or stays planned until a snapshot exists.

---

### User Story 2 - Track Acquisition Runs (Priority: P2)

As the user, I want every import/crawl/download attempt to produce an acquisition
run record so I can tell what was collected, from where, and whether it is ready
for indexing.

**Why this priority**: Large documentation sources need resumable, inspectable
provenance before they become searchable agent context.

**Independent Test**: Run a dry-run acquisition for a local folder and verify a
run record is written with counts, source paths, status, and warnings.

**Acceptance Scenarios**:

1. **Given** a local docs folder, **When** dry-run acquisition runs, **Then** the
   system reports file counts and supported extensions without copying files.
2. **Given** unsupported files exist, **When** acquisition is validated, **Then**
   the run record lists warnings instead of failing silently.
3. **Given** acquisition completes, **When** the run is inspected, **Then** it
   states whether the corpus is ready for indexing.

---

### User Story 3 - Prepare for Official Website Crawling (Priority: P3)

As the maintainer, I want a crawler/download contract that defines allowed
sources, crawl limits, robots/politeness notes, snapshot dates, and output layout
before any crawler is implemented.

**Why this priority**: Some official docs only exist on websites. Automation must
be designed before it is allowed to crawl.

**Independent Test**: Add a crawl plan for a refreshable official docs corpus and
verify that it includes source URL, allowed domains, snapshot date policy, output
folder, rate/pagination limits, and status.

**Acceptance Scenarios**:

1. **Given** Codex/OpenAI docs are planned, **When** a crawl plan is created,
   **Then** it records allowed official domains and refreshable snapshot policy.
2. **Given** a website source has no local snapshot, **When** retrieval routes to
   it, **Then** context packs report missing local corpus rather than scraping
   live content ad hoc.

### Edge Cases

- A corpus path exists but contains no Markdown files.
- A local import mixes multiple product versions in one folder.
- A refreshable corpus lacks a snapshot date.
- A crawler target is outside approved official domains.
- MarkItDown conversion produced malformed Markdown or missing headings.
- A large corpus import is interrupted midway.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support manual corpus registration before any crawler
  automation is required.
- **FR-002**: System MUST create an acquisition manifest for each import, dry-run,
  crawl plan, or download plan.
- **FR-003**: Acquisition manifests MUST include corpus id, source method, source
  path or URL, authority level, product, version, snapshot date when applicable,
  status, file counts, warnings, and readiness for indexing.
- **FR-004**: Planned corpora MAY omit local root path, but available/indexed
  corpora MUST have a valid local root path or a documented reason.
- **FR-005**: Refreshable official docs MUST use snapshot dates before becoming
  available for retrieval.
- **FR-006**: Crawler/download plans MUST define allowed domains, output layout,
  rate or page limits, and manual approval status.
- **FR-007**: The system MUST NOT live-scrape official docs during retrieval.
- **FR-008**: Acquisition validation MUST be scriptable and deterministic.
- **FR-009**: Acquisition output MUST stay compatible with the existing corpus
  registry and context-pack routing.

### Key Entities

- **AcquisitionManifest**: A file-first record describing how a corpus was or
  will be acquired.
- **AcquisitionRun**: One execution or dry-run of an acquisition plan.
- **CrawlPlan**: A planned website acquisition definition with domains, limits,
  output path, and approval status.
- **ImportValidationReport**: A deterministic report of local files, supported
  extensions, warnings, and readiness.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A local corpus dry run reports file counts and readiness in under
  60 seconds for a representative folder sample.
- **SC-002**: Registering a planned corpus produces a valid registry entry and
  acquisition manifest without requiring local docs.
- **SC-003**: Registering an available corpus with a missing path fails
  validation with a clear message.
- **SC-004**: Crawl plans for refreshable official docs include allowed domains,
  snapshot policy, output folder, and manual approval status.
- **SC-005**: Full test suite passes after acquisition workflow changes.

## Assumptions

- MarkItDown conversion remains an upstream or separate step; this feature
  validates converted Markdown but does not replace MarkItDown.
- Crawl/download automation is planned but not implemented in the MVP unless all
  file-first contracts are stable.
- Official OpenAI/Codex docs are refreshable snapshots; Unity versioned docs are
  fixed snapshots.
- Large binary/vector data remains outside Git.
