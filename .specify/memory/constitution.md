<!--
Sync Impact Report
Version change: template -> 1.0.0
Modified principles:
- Template principle 1 -> I. Personal-First Agent Memory
- Template principle 2 -> II. Provenance and Governance Before Recall
- Template principle 3 -> III. File-First, API/MCP-Ready Design
- Template principle 4 -> IV. Retrieval Quality Is a Product Requirement
- Template principle 5 -> V. Script Determinism Over Repeated Agent Reasoning
Added sections:
- Corpus and Memory Boundaries
- Versioned Official Docs Registry
- Development Workflow and Quality Gates
Removed sections:
- Placeholder template sections
Templates requiring updates:
- updated: .specify/templates/plan-template.md
- updated: .specify/templates/spec-template.md
- updated: .specify/templates/tasks-template.md
Follow-up TODOs:
- None
-->
# Memory and Second Brain for Agents Constitution

## Core Principles

### I. Personal-First Agent Memory
The project MUST optimize first for a single user's persistent agent experience:
preferences, working style, lessons, reusable skills, and approved operational
knowledge. Shared-team or public memory MUST remain secondary until the personal
memory loop is useful, inspectable, and trusted.

Rationale: a second brain becomes valuable when agents stop behaving like new
assistants on every task and start acting like collaborators that understand the
user's standards.

### II. Provenance and Governance Before Recall
Every durable memory, lesson, skill candidate, and indexed corpus item MUST keep
source, version, status, confidence, and scope metadata. The system MUST support
clear lifecycle states such as draft, candidate, approved, active, deprecated,
superseded, and rejected. Unreviewed extraction output MUST NOT be treated as
active personal memory.

Rationale: remembering the wrong thing is worse than forgetting. Trust requires
knowing where knowledge came from, when it applies, and who approved it.

### III. File-First, API/MCP-Ready Design
New memory and skill artifacts MUST be readable and editable as files first,
preferably Markdown with YAML frontmatter or adjacent YAML metadata. The file
layout MUST remain stable enough to wrap later with CLI commands, REST APIs, or
MCP tools without changing the conceptual data model.

Rationale: file-first artifacts are easy to inspect, version, review, and repair
while the schema is still evolving.

### IV. Retrieval Quality Is a Product Requirement
Retrieval MUST be designed as an agent-facing contract, not a raw search result.
For large corpora such as Unity, Python, TypeScript, and Codex/OpenAI
documentation, the system MUST route to the correct corpus and version before
searching. It MUST return bounded context packs with ranked sources, snippets,
metadata, selected/excluded corpora, and quality signals. Retrieval changes MUST
be validated with representative queries before being treated as improvements.

Rationale: the core user value is not storing 39,000 files; it is giving an agent
the right small set of trustworthy context for the user's current task.

### V. Script Determinism Over Repeated Agent Reasoning
Repeatable transformations and validations MUST be implemented as scripts when
they are deterministic: conversion checks, schema validation, index generation,
frontmatter extraction, status transitions, and context-pack assembly. Agents
SHOULD orchestrate, review, and handle ambiguity rather than re-solving fixed
procedures on every run.

Rationale: scripts reduce cost, variance, and latency while preserving agent
attention for judgment-heavy work.

## Corpus and Memory Boundaries

Official documentation corpora MUST be treated separately from distilled
personal memory. Source documents may be normalized, indexed, and retrieved, but
they are not themselves approved lessons or skills.

The Unity 6.3 Markdown corpus under `docs/massive/Unity_6_3_Markdown` is the
first immutable demo corpus, not a special-case architecture. Unity 6.5, Python,
TypeScript, Codex/OpenAI docs, and future sources MUST be represented through the
same registry model.

The project distinguishes these artifact classes:

- Source corpus: official or imported documents with version and checksum.
- Corpus registry: source-of-truth for vendor, product, version, authority,
  update policy, project binding, and status.
- Document index: generated metadata, headings, symbols, and retrieval records.
- Task memory: factual record of a completed task or demo run.
- Lesson: a scoped behavioral rule learned from sources or work.
- Preference: a user-specific working-style or quality preference.
- Skill candidate: a repeatable workflow proposed for future reuse.
- Active skill: reviewed workflow with triggers, procedure, scripts, examples,
  and failure modes.

## Versioned Official Docs Registry

Every official documentation source MUST have a corpus registry record before it
is treated as searchable agent context. Registry records MUST distinguish
immutable versioned docs from refreshable snapshots and rolling latest sources.

Unity and similar engine docs MUST prefer the version bound to the current
project. The system MUST NOT silently substitute a newer engine version when the
project is bound to an older version.

Codex/OpenAI docs MUST be treated as refreshable official snapshots unless a
specific immutable export is provided. They SHOULD be categorized as an agent
platform corpus, not as a programming language corpus.

## Development Workflow and Quality Gates

Every substantial feature MUST pass through spec-kit artifacts before
implementation: specification, plan, research decisions, data model or contracts
when relevant, quickstart validation, and tasks.

Plans MUST explicitly address:

- file-first artifact layout and schema compatibility;
- provenance, status, confidence, and version metadata;
- retrieval contract and context-pack limits;
- corpus registry, query routing, version/project binding, and refresh policy;
- Codex-first access path and future MCP/API compatibility;
- deterministic scripts for repeated operations;
- validation using a small representative query set.

Generated tasks MUST be independently executable, path-specific, and grouped by
user story. The MVP slice MUST demonstrate agent-visible value, not just internal
storage.

## Governance

This constitution supersedes ad hoc project preferences when they conflict with
memory safety, provenance, or retrieval quality. Amendments require updating this
file, documenting the version bump, and checking dependent spec-kit templates.

Versioning follows semantic versioning:

- MAJOR for principle removals or incompatible governance changes.
- MINOR for new principles or materially expanded required gates.
- PATCH for clarifications that do not change project obligations.

All feature plans and implementation reviews MUST check compliance with the core
principles. Any violation MUST be documented in the feature plan with the simpler
alternative that was considered and rejected.

**Version**: 1.0.0 | **Ratified**: 2026-07-13 | **Last Amended**: 2026-07-13
