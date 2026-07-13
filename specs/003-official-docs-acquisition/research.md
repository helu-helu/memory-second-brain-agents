# Research: Official Docs Acquisition

## Decision: Manual import first

**Rationale**: The current workflow is manual conversion/import. Supporting it
well gives immediate value without introducing crawler risk.

**Alternatives considered**:

- Build crawler first: rejected because source policies, domains, limits, and
  snapshot semantics are not stable yet.

## Decision: Acquisition manifests are separate from corpus registry records

**Rationale**: A corpus registry says what a corpus is and whether it is
available. An acquisition manifest says how that corpus was obtained, validated,
or planned.

**Alternatives considered**:

- Put all acquisition metadata into registry: rejected because run history and
  warnings would bloat routing records.

## Decision: No live scraping during retrieval

**Rationale**: Retrieval must be reproducible and version-aware. Live scraping
would make context packs non-deterministic and harder to cite.

**Alternatives considered**:

- Fetch missing docs on demand: rejected because it bypasses snapshot/version
  policy and can break during agent tasks.

## Decision: Crawl plans require allowed domains and manual approval

**Rationale**: Official docs sources vary in access patterns. A crawler should
only run from explicit approved plans.

**Alternatives considered**:

- Free-form URL crawler: rejected because it is too easy to crawl the wrong
  source or mix unofficial content.
