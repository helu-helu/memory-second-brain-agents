# Implementation Plan: MCP Post-Restructure Validation

**Branch**: `015-mcp-post-restructure-validation` | **Date**: 2026-07-14 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `/specs/015-mcp-post-restructure-validation/spec.md`

## Summary

Validate that Codex can still use the Second Brain MCP server after feature 014's package restructure. Keep the scope to import/tool-surface checks, one small representative Unity 6.3 query path, and clear status documentation.

## Technical Context

**Language/Version**: Python project using the currently configured local runtime

**Primary Dependencies**: Existing MCP server script, API adapter, pytest, current runtime modules

**Storage**: Existing `second-brain/` and `db/` paths unchanged

**Testing**: pytest import/mocked MCP smoke first; optional real-runtime smoke only if safe

**Target Platform**: Local Codex MCP integration

**Project Type**: Python runtime with MCP adapter

**Performance Goals**: Validation should complete using small representative checks without full-corpus scans

**Constraints**: Do not rename MCP tools, REST routes, or storage paths

**Scale/Scope**: One representative Unity 6.3 query plus MCP smoke checks

## Constitution Check

- **Personal-first memory**: Pass. Codex MCP access is the primary personal agent access path.
- **Provenance and governance**: Pass. Validation evidence and blockers are recorded.
- **File-first compatibility**: Pass. No file workspace paths move.
- **Retrieval quality**: Pass. Representative query validates bounded context behavior.
- **Versioned corpus routing**: Pass. Unity 6.3 routing is part of validation.
- **Script determinism**: Pass. Repeated checks use tests/scripts instead of ad hoc reasoning.

## Project Structure

### Documentation (this feature)

```text
specs/015-mcp-post-restructure-validation/
├── spec.md
├── plan.md
├── research.md
├── quickstart.md
├── validation-report.md
├── contracts/
│   └── mcp-validation-contract.md
├── checklists/
│   └── requirements.md
└── tasks.md
```

### Source Code

```text
second_brain_mcp.py          # stable MCP entrypoint
tests/test_mcp_runtime_smoke.py
tests/test_import_compatibility.py
PROJECT_STATUS.md
```

**Structure Decision**: Prefer validating existing tests and entrypoints before adding any new code. Add code only if a gap is found.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None | N/A | N/A |
