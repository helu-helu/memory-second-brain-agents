# Research: Experience Extraction

## Decision: Deterministic MVP extraction

**Rationale**: The first extractor should prove artifact creation, schema
validation, and review gating without introducing LLM variability.

**Alternatives considered**:

- LLM extraction immediately: rejected because memory pollution risk is high
  before review workflow is proven.

## Decision: Candidate-only outputs

**Rationale**: Unreviewed generated artifacts must not become active memory or
skills.

**Alternatives considered**:

- Auto-approve high-confidence candidates: rejected because confidence is not yet
  calibrated.

## Decision: Context packs are valid evidence

**Rationale**: Context packs already contain routed corpus, sources, snippets,
and quality signals. They are a good evidence unit for lessons.

**Alternatives considered**:

- Extract only from raw source docs: rejected because task-specific context packs
  better capture why sources mattered.
