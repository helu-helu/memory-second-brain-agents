# Research: Hybrid Retrieval Context Packs

## Decision: Keep query routing before retrieval

**Rationale**: Version mistakes are more damaging than weak ranking. The system
must choose the correct corpus/version before running lexical or vector search.

**Alternatives considered**:

- Search all corpora then filter: rejected because vector search may surface
  plausible but wrong-version results.

## Decision: Improve deterministic lexical ranking before vector integration

**Rationale**: Exact path, heading, symbol, and metadata signals are cheap,
testable, and essential for technical docs. Vector search should augment these
signals, not replace them.

**Alternatives considered**:

- Vector-first ranking: rejected because technical API queries often require
  exact terms and version filters.
- Keep lexical path-only ranking: rejected because it produced noisy results for
  terms such as "system".

## Decision: Treat vector search as optional until index readiness is detectable

**Rationale**: Local Qdrant may not be running and some corpora are planned but
not locally available. Context-pack generation should still work and report
honest retrieval mode.

**Alternatives considered**:

- Fail when vector search is unavailable: rejected because Codex still needs a
  usable degraded context pack.

## Decision: Add retrieval eval fixtures before tuning ranking

**Rationale**: Ranking tweaks are easy to overfit. A small fixture set gives the
project a repeatable quality floor.

**Alternatives considered**:

- Rely on full test suite only: rejected because unit tests can pass while
  retrieval quality gets worse.
