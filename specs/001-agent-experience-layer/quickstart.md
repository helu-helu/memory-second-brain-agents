# Quickstart: Validate the Versioned Official Docs Agent Experience Layer

## Prerequisites

- Unity 6.3 Markdown corpus exists at
  `docs/massive/Unity_6_3_Markdown`.
- Qdrant is available if vector retrieval is being exercised.
- The project environment can run existing Python scripts.

## Scenario 1: Confirm Corpus Scale

Run or verify a file count for the corpus.

Expected result:

- The corpus contains about 39,056 Markdown files.
- The corpus is treated as immutable Unity 6.3 source material.

## Scenario 2: Register Official Corpora

Create or inspect corpus records for Unity 6.3, Unity 6.5 placeholder, Python,
TypeScript, and Codex/OpenAI docs.

Expected result:

- Unity 6.3 is available and immutable.
- Unity 6.5 is planned unless its docs have been imported.
- Codex/OpenAI docs are refreshable snapshots with a snapshot date.
- Python and TypeScript records include version or clarification policy.

## Scenario 3: Route Queries Before Retrieval

Use representative queries:

```text
How do I use the Unity Input System in this project?
How do Codex skills differ from plugins?
How does Python TaskGroup cancellation work?
How should I configure tsconfig paths?
```

Expected result:

- Unity routes to the project-bound Unity version.
- Codex routes to agent platform docs.
- Python routes to language docs.
- TypeScript routes to language/toolchain docs.
- Ambiguous versions trigger clarification or documented assumptions.

## Scenario 4: Register a Converted Document

Add a small demo Markdown document to the future demo input folder and register
metadata for it.

Expected result:

- A SourceDocument record exists.
- Required fields include source path, checksum, status, taxonomy, visibility,
  sensitivity, and conversion information.

## Scenario 5: Produce a Codex Context Pack

Use a representative Unity query:

```text
How should an agent find the correct Unity 6.3 documentation for input handling?
```

Expected result:

- A context pack is generated for Codex.
- It includes no more than 12 primary sources by default.
- Each source has a citation path and selection reason.
- Quality signals identify confidence and ambiguity.

## Scenario 6: Distill Candidate Experience

Use a source document or context pack to propose lessons and one skill candidate.

Expected result:

- Proposed lessons remain in candidate status.
- The skill candidate includes trigger, workflow, deterministic scripts, eval
  notes, and failure modes.
- Nothing becomes active without review.

## Scenario 7: Check Future API/MCP Readiness

Compare the generated context pack against
`contracts/context-pack.schema.md`.

Expected result:

- The context pack can be represented as Markdown/YAML files.
- The same fields can be exposed later through MCP/API without changing their
  meaning.
