# Second Brain Workspace

This directory is the file-first workspace for personal agent memory.

Artifacts are English-first and reviewable in Git. Source corpora are not active
memory by themselves; they become useful through query routing, context packs,
and reviewed lessons or skills.

## Layout

```text
corpora/      Versioned official-docs registry and project bindings
inbox/        Raw or converted items waiting for review
sources/      Registered source document metadata
memory/       Lessons, preferences, principles, decisions
skills/       Skill candidates and active portable skills
indexes/      Generated indexes and lookup files
demo/         Fixtures and example artifacts
```

## Lifecycle

Use explicit statuses: `draft`, `candidate`, `approved`, `active`,
`deprecated`, `superseded`, and `rejected`.

Unreviewed generated artifacts stay `candidate` until the user approves them.
