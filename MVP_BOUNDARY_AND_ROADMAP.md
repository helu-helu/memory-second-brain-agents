# MVP Boundary and Roadmap

## Current Stop Point

The MVP stops at the end-to-end personal second-brain loop:

1. Register official documentation corpora.
2. Route documentation questions to the right corpus/version.
3. Build bounded documentation context packs.
4. Extract candidate lessons and skill candidates from evidence.
5. Review, approve, reject, and activate candidates with audit records.
6. Build bounded active memory packs.
7. Expose docs, memory, status, bootstrap, and handoff actions through script/API/MCP access paths.
8. Record agent handoffs as future extraction evidence.

Further work should not be implemented automatically just because another
"continue" request is given. Treat it as a new phase decision.

## Phase 1 Done Criteria

- All existing `specs/*/tasks.md` checkboxes are complete.
- Full test suite passes without warnings.
- Tests use small representative fixtures and avoid full-corpus scans.
- Demo artifacts are intentional and not produced by normal test runs.

## Phase 2 Backlog

- Production crawler hardening: resumable crawl state, robots/rate policy,
  retries, canonical URL handling, and checksum refresh.
- Vector search: embedding provider selection, index storage, rebuild strategy,
  eval set, and fallback behavior.
- UI/dashboard: inspect corpora, candidates, active memory, packs, handoffs, and
  review decisions.
- Memory lifecycle operations: deprecate, supersede, restore, and bulk review.
- Multi-agent packaging: installer docs, MCP server smoke tests, and client setup.
- Security and permissions: per-agent access labels, write approvals, and secret
  handling review.
- Release hygiene: changelog, architecture overview, and commit/PR slicing.

## Default Next Action

If the user says "continue" after Phase 1, default to hardening, cleanup,
documentation, tests, or release preparation. Do not create a new feature unless
the user explicitly chooses a Phase 2 backlog item.
