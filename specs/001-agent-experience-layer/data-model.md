# Data Model: Versioned Official Docs Agent Experience Layer

## Corpus

Represents one official or trusted documentation collection.

**Fields**:

- `corpus_id`: stable identifier such as `unity-6.3` or `codex-docs-2026-07-13`.
- `category`: engines, languages, frameworks, agent_platforms, tools, libraries.
- `vendor`: source owner.
- `product`: product or platform name.
- `version`: product version or snapshot label.
- `authority_level`: official, vendor, community, internal, unknown.
- `mutability`: immutable, refreshable, rolling.
- `update_policy`: fixed_snapshot, refreshable_snapshot, rolling_latest.
- `snapshot_date`: required for refreshable snapshots.
- `refresh_cadence`: manual, scheduled, none.
- `root_path`: project-relative corpus path when locally available.
- `acquisition`: manual, download, crawl, generated.
- `status`: planned, available, indexed, deprecated, rejected.
- `default_for`: optional project or domain binding.

## ProjectBinding

Represents which corpus/version a project should use by default.

**Fields**:

- `binding_id`: stable identifier.
- `project_path`: project root or project identifier.
- `product`: Unity, Python, TypeScript, Codex, etc.
- `preferred_corpus_id`: corpus to use when user does not specify a version.
- `strict_version`: whether fallback to other versions is allowed.
- `notes`: reason for the binding.

## QueryRoute

Represents the routing decision before retrieval.

**Fields**:

- `query`: original query.
- `detected_category`: engines, languages, frameworks, agent_platforms, tools.
- `detected_product`: Unity, Python, TypeScript, Codex, etc.
- `detected_version`: explicit version if present.
- `selected_corpora`: corpus ids to search.
- `excluded_corpora`: corpus ids intentionally skipped.
- `route_confidence`: high, medium, low.
- `clarification_needed`: optional question when routing is unsafe.

## SourceDocument

Represents one imported or converted document.

**Fields**:

- `id`: stable document identifier.
- `title`: human-readable title.
- `source_path`: project-relative path.
- `source_type`: official_docs, third_party_guidance, project_doc, user_note.
- `vendor`: source owner when applicable.
- `product`: product or domain when applicable.
- `version`: source version, such as Unity 6.3.
- `mutability`: immutable or mutable.
- `checksum`: content hash.
- `conversion`: converter name, version if known, converted_at.
- `taxonomy`: doc_class, domain, intent, artifact_type.
- `visibility`: private, project, team, public.
- `sensitivity`: low, medium, high.
- `status`: raw, converted, normalized, indexed, deprecated, rejected.

## DocumentChunk

Represents a retrievable portion of a source document.

**Fields**:

- `id`: stable chunk identifier.
- `document_id`: parent SourceDocument.
- `heading_path`: ordered headings.
- `text`: chunk text or pointer to text.
- `source_span`: line range or section marker when available.
- `symbols`: detected API/class/member/package terms.
- `embedding_ref`: optional vector record reference.
- `rank_features`: lexical score, vector score, recency/version match,
  taxonomy match, dedup group.

## ContextPack

Agent-facing retrieval output.

**Fields**:

- `query`: original user or agent query.
- `query_route`: selected corpora, excluded corpora, and routing confidence.
- `detected_intent`: how_to, api_reference, troubleshoot, explain, configure,
  migrate, optimize, compare.
- `scope`: product/version/domain constraints.
- `limits`: requested and applied source/snippet limits.
- `quality`: confidence, ambiguity, coverage, warnings.
- `sources`: ranked source snippets with citations and reasons.
- `memory`: relevant approved lessons, preferences, or skills.
- `clarification_needed`: optional question when retrieval is unsafe.

## Lesson

Scoped behavioral knowledge distilled from work or documents.

**Fields**:

- `id`, `title`, `status`, `confidence`.
- `trigger`: when agents should consider the lesson.
- `scope`: where the lesson applies.
- `guidance`: behavior-changing instruction.
- `evidence`: source documents, tasks, or context packs.
- `failure_modes`: when not to apply it.
- `supersedes`: optional previous lesson ids.

## Preference

User-specific collaboration or quality preference.

**Fields**:

- `id`, `title`, `status`, `confidence`.
- `applies_when`: task/context conditions.
- `preference`: user-specific behavior.
- `exceptions`: known exceptions.
- `evidence`: conversations, approvals, or rejections.

## SkillCandidate

Proposed repeatable agent workflow.

**Fields**:

- `id`, `name`, `status`, `confidence`.
- `trigger`: when to use the skill.
- `inputs`: required user/context inputs.
- `workflow`: ordered steps.
- `outputs`: expected artifacts.
- `scripts`: deterministic helpers used by the skill.
- `examples`: sample invocations or results.
- `eval`: checks that prove correct use.
- `failure_modes`: when to avoid or ask for clarification.
- `export_targets`: Codex, MCP, generic.

## ExtractionRun

Record of a distillation attempt.

**Fields**:

- `id`, `created_at`, `operator`.
- `inputs`: source documents, task transcript, diff, logs, or context pack.
- `method`: script, agent, model, or hybrid.
- `outputs`: proposed lessons, preferences, skill candidates.
- `review_status`: pending, approved, rejected, partial.
- `notes`: reviewer or agent notes.

## State Transitions

Source documents:

```text
raw -> converted -> normalized -> indexed -> deprecated
                              \-> rejected
```

Lessons, preferences, and skills:

```text
draft -> candidate -> approved -> active -> deprecated
                              \-> rejected
active -> superseded
```
