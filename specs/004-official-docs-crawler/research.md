# Research: Official Docs Crawler

## Decision: Standard-library crawler first

**Rationale**: The MVP needs bounded, testable crawl behavior. Python standard
library is enough for fetching HTML, parsing links, and saving snapshots.

**Alternatives considered**:

- Add Scrapy/Playwright: rejected for MVP because it adds weight before crawl
  policy and snapshot output are proven.

## Decision: Tests use local HTTP server

**Rationale**: Crawler behavior must be repeatable and not depend on internet
availability or external site changes.

**Alternatives considered**:

- Test against official sites directly: rejected because tests would be flaky and
  may violate the no-live-network principle.

## Decision: Save HTML snapshots first

**Rationale**: HTML snapshots preserve source material and can be converted later
with existing conversion scripts or MarkItDown.

**Alternatives considered**:

- Convert to Markdown during crawl: rejected for MVP because crawling and
  conversion are separate failure modes.

## Decision: Refuse draft plans by default

**Rationale**: Crawl plans are governance gates. Draft plans should not fetch
content unless dry-run is explicit.

**Alternatives considered**:

- Allow all plans: rejected because accidental crawler runs are too easy.
