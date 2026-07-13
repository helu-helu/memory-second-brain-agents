# Data Model: Hybrid Retrieval Context Packs

## RetrievalQuery

Represents a user or agent question after routing.

**Fields**:

- `query`: original query.
- `route`: selected corpora, excluded corpora, detected product, confidence.
- `limit`: requested source limit.
- `mode`: lexical, vector, hybrid, degraded.

## RetrievalCandidate

Represents a source before final ranking and deduplication.

**Fields**:

- `corpus_id`: registered corpus id.
- `path`: source path.
- `title`: heading or file-derived title.
- `snippet`: candidate snippet.
- `signals`: lexical score, phrase score, symbol score, metadata score, vector score.
- `reason`: human-readable selection reason.

## RankedSource

Represents a selected context-pack source.

**Fields**:

- `rank`: final rank.
- `corpus_id`: selected corpus.
- `path`: citation path.
- `relevance`: low, medium, high.
- `why`: source selection reason.
- `snippet`: bounded text excerpt.
- `scores`: score breakdown.

## RetrievalEvalCase

Represents one retrieval benchmark case.

**Fields**:

- `id`: stable case id.
- `query`: representative query.
- `expected_product`: expected routed product.
- `expected_corpus`: expected selected corpus.
- `expected_path_patterns`: path fragments that should appear in top results.
- `max_sources`: expected source limit.
- `expect_clarification`: whether clarification is expected.

## RetrievalEvalRun

Represents an eval execution.

**Fields**:

- `created_at`: run timestamp.
- `cases`: pass/fail case summaries.
- `passed`: total passing cases.
- `failed`: total failing cases.
- `warnings`: degraded mode or missing corpus notes.
