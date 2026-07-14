# Data Model: Agent Access Tools

## AgentToolResponse

Structured response for helper/API/MCP calls.

**Fields**:

- `ok`: boolean.
- `data`: response payload.
- `warnings`: non-fatal warnings.
- `error`: user-readable error when `ok` is false.

## CorpusStatus

Combined status for one corpus.

**Fields**:

- `corpus_id`: corpus registry id.
- `registry`: registry record.
- `acquisitions`: matching acquisition manifests.
- `crawl_plans`: matching crawl plans.
- `ready_for_retrieval`: boolean.
- `warnings`: missing local path, planned status, draft crawl plan, etc.

## ContextPackRequest

Input for building a context pack.

**Fields**:

- `query`: user or agent query.
- `limit`: source limit.
- `mode`: lexical, hybrid, vector.
- `out`: optional output path.
- `client`: codex or other agent client.

## ContextPackResult

Output from building a context pack.

**Fields**:

- `path`: generated context pack path when written.
- `selected_corpora`: selected corpus ids.
- `applied_sources`: number of sources.
- `retrieval_mode`: actual retrieval mode.
- `warnings`: warnings from generation.
