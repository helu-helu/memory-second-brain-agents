# Research: Active Memory Recall

## Decision: Recall active artifacts only

**Rationale**: Candidate and approved-but-not-active artifacts are review states, not agent-facing memory.

**Alternatives considered**:

- Include approved artifacts: rejected because approval and activation are intentionally separate lifecycle decisions.

## Decision: Lexical deterministic MVP

**Rationale**: The first recall loop should prove governance, bounded output, and context format without vector infrastructure.

**Alternatives considered**:

- Vector search immediately: deferred until active memory volume justifies embedding/index complexity.

## Decision: Separate personal memory packs from docs context packs

**Rationale**: Official docs answer "what does the source say?" Personal memory answers "how should this user's agents behave?" Mixing them would blur provenance.

**Alternatives considered**:

- Merge with docs context pack builder: rejected because the corpora and lifecycle rules are different.
