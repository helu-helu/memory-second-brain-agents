# Research: MCP Post-Restructure Validation

## Decision: Validate MCP access before adding new product features

**Rationale**: Feature 014 moved runtime modules. MCP is the user-selected primary agent access path, so its stability is the next highest-value check.

**Alternatives considered**:

- Start retrieval-quality improvements immediately: rejected because access stability should be proven first.
- Reconfigure Codex MCP first: rejected unless validation proves the existing command is broken.

## Decision: Use small representative validation

**Rationale**: Previous real runtime checks can time out when loading Qdrant, embeddings, Mem0, or model providers. A small query should validate routing and context behavior without scanning full corpora.

**Alternatives considered**:

- Full Unity corpus validation: rejected for normal development checks.
- Only import smoke: rejected because it does not prove agent-visible behavior.

## Decision: Keep mocked smoke separate from real-runtime smoke

**Rationale**: Mocked tests are fast and reliable for contract regression. Real-runtime checks are operational and may be blocked by local model/vector state.

**Alternatives considered**:

- Treat mocked smoke as full readiness: rejected because it hides runtime dependency risk.
- Require real runtime for every unit test: rejected because it is slow and flaky.
