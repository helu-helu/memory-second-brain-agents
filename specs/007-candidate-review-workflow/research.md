# Research: Candidate Review Workflow

## Decision: Separate approve and activate

**Rationale**: Approval means the user accepts the artifact as valid. Activation means agents may use it. Keeping these states separate prevents accidental agent-facing use and gives the user a staging point.

**Alternatives considered**:

- Approve immediately activates: rejected because it collapses review and deployment into one action.

## Decision: Deterministic lifecycle script first

**Rationale**: Status transitions, frontmatter updates, and audit records are repeatable operations and should not depend on repeated agent reasoning.

**Alternatives considered**:

- Agent-only review instructions: rejected because it would be harder to test and easier to apply inconsistently.

## Decision: Decision records are append-only files

**Rationale**: Audit records should remain readable, versionable, and independent from artifact edits.

**Alternatives considered**:

- Store decisions only inside artifact frontmatter: rejected because it makes review history harder to inspect and can grow noisy over time.

## Decision: Active skill promotion copies instead of moves

**Rationale**: The candidate remains the provenance record. The active skill is a reviewed derivative that can evolve later.

**Alternatives considered**:

- Move candidate folder into active skills: rejected because it erases the candidate review boundary.
