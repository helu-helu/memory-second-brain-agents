# Research: Versioned Official Docs Agent Experience Layer

## Decision: Build a versioned corpus registry before expanding ingestion

**Rationale**: The project will ingest official docs from Unity, Python,
TypeScript, Codex/OpenAI, and future sources. A registry is the control plane for
authority, version, mutability, update policy, root paths, and project defaults.

**Alternatives considered**:

- Add each docs folder ad hoc: rejected because query routing would become
  brittle and version mistakes would be likely.
- Build crawler/download automation first: rejected because manual ingestion is
  the current workflow and schema clarity matters more than automation.

## Decision: Treat Unity 6.3 as an immutable source corpus

**Rationale**: The corpus is official Unity 6.3 documentation already converted
to Markdown and contains 39,056 files. It should be indexed and cited, not edited
or mixed directly into personal memory.

**Alternatives considered**:

- Put Unity docs into memory records: rejected because source docs are not
  learned personal behavior.
- Summarize the whole corpus up front: rejected because it risks losing API and
  version details before actual task intent is known.

## Decision: Treat Codex/OpenAI docs as refreshable snapshots

**Rationale**: Codex and OpenAI product documentation changes more often than a
fixed engine release. The local corpus should record snapshot date and manual
refresh policy instead of pretending to be permanently immutable.

**Alternatives considered**:

- Rolling latest only: rejected because agent answers need reproducible source
  context.
- Immutable forever: rejected because Codex/OpenAI behavior and docs can change.

## Decision: Classify Codex as an agent platform corpus

**Rationale**: Codex is not just a programming language or API reference. Its
documentation spans surfaces, customization, skills, plugins, MCP, permissions,
workflows, and troubleshooting. It belongs under `agent_platforms/openai_codex`,
not under `languages`.

**Alternatives considered**:

- Put Codex under code docs: rejected because it hides governance, tooling, and
  agent-operating-environment topics.
- Put Codex under OpenAI API only: rejected because Codex product behavior and
  customization are separate from generic API usage.

## Decision: Use hybrid retrieval, but validate lexical and metadata signals

**Rationale**: Vector search helps with vague questions and intent matching.
Unity technical work also depends on exact API names, headings, package names,
and version filters. The retrieval plan should combine vector search with exact
terms, metadata, path taxonomy, and source deduplication.

**Alternatives considered**:

- Vector-only: rejected because semantic matches can be plausible but wrong for
  API/version-specific questions.
- ripgrep/BM25-only: rejected because the user wants ambiguity handling and
  better question recognition where embeddings can help.

## Decision: Context-pack source limit starts adaptive, not fixed

**Rationale**: Different tasks need different context volume. Default pack limits
should protect agent context while allowing deeper searches when the query is
large.

**Recommended limits**:

- Tiny/direct lookup: 3 to 5 primary sources.
- Normal implementation question: 8 to 12 primary sources.
- Broad design or troubleshooting question: 12 to 20 primary sources.
- Above 20 sources requires an explicit deep-research mode or generated summary.

**Alternatives considered**:

- Always return 5: too little for multi-domain Unity tasks.
- Always return 20: too noisy and costly for simple API questions.

## Decision: Use YAML frontmatter plus Markdown body for human-facing artifacts

**Rationale**: The user wants English artifacts that agents can query well.
Markdown remains readable, while YAML frontmatter carries status, provenance,
confidence, and lifecycle data.

**Alternatives considered**:

- JSON-only: easier to validate but harder to review as knowledge.
- Database-only: premature for schema evolution and harder to repair manually.

## Decision: Codex-compatible skills through an adapter, not lock-in

**Rationale**: Codex is the first client, but the project goal is cross-agent
reuse. Active skills should use a portable folder contract that can be exported
to Codex skill format when needed.

**Alternatives considered**:

- Native Codex-only skill layout: useful now but constrains future agents.
- Abstract skill registry only: too vague for immediate Codex use.
