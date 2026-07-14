# Capability Map: Unify Agent Runtime

**Status**: Phase 1/2 inventory and decision baseline.

## Consolidation Decision

The project will not split into a separate second-brain project. The selected
direction is one unified runtime:

- `agent_core/` owns runtime behavior.
- `api/` exposes runtime behavior over REST.
- `second_brain_mcp.py` exposes runtime behavior over MCP.
- `second-brain/` remains a file-first data, corpus, review, memory, skills,
  audit, and spec workspace.
- `scripts/` should become deterministic wrappers, exporters, importers, and
  validators around the runtime/workspace instead of competing runtime engines.

## Runtime Source Of Truth

| Capability | Current owner | Decision | Notes |
|---|---|---|---|
| Static knowledge retrieval | `agent_core/knowledge.py` | reuse/extend | LlamaIndex + Qdrant + embeddings + HyDE remain primary. |
| Personal memory | `agent_core/memory.py` | reuse/extend | Mem0-backed memory remains primary. |
| Combined context | `agent_core/context_builder.py` | extend | Should emit unified context result. |
| REST access | `api/api_server.py` | extend | Keep endpoints, align contracts. |
| MCP access | `second_brain_mcp.py` | extend | Keep tools, align behavior and stdio safety. |
| Corpus registry | `second-brain/corpora/registry.yaml` and scripts | extend | Registry remains file-first source for corpus metadata. |
| Context-pack export | `scripts/build_context_pack.py` | replace role | Should export runtime results; lexical only fallback/audit. |
| File-first memory packs | `scripts/build_memory_pack.py` | extend | Should remain audit/export over approved memory artifacts. |
| Official docs ingestion/indexing | `scripts/build_massive_index.py` and related scripts | extend | Should feed runtime index, not create competing retrieval. |

## Runtime Entry Points

| Layer | Entry point | Capability | Owner decision |
|---|---|---|---|
| Runtime | `agent_core.knowledge.KnowledgeBase.load()` | Load or build Qdrant/LlamaIndex index | runtime source of truth |
| Runtime | `agent_core.knowledge.KnowledgeBase.search()` | Vector/model-backed knowledge retrieval | runtime source of truth |
| Runtime | `agent_core.knowledge.KnowledgeBase.insert_file()` | Incremental index update | runtime source of truth |
| Runtime | `agent_core.memory.MemoryManager.add()` | Add personal memory | runtime source of truth |
| Runtime | `agent_core.memory.MemoryManager.search()` | Search personal memory | runtime source of truth |
| Runtime | `agent_core.memory.MemoryManager.format_for_prompt()` | Format memories for context | runtime source of truth |
| Runtime | `agent_core.context_builder.ContextBuilder.build_async()` | Combine memory and knowledge | extend to unified contract |
| Runtime | `agent_core.context_builder.ContextBuilder.save_interaction()` | Save learned interaction | runtime source of truth |
| Runtime/access | `agent_core.access_tools.*` | File-first second-brain helpers | adapter layer; align to runtime |

## REST API Entry Points

| Endpoint | Current behavior | Decision |
|---|---|---|
| `GET /ping` | Health check | reuse |
| `GET /rag/search` | Calls `KnowledgeBase.search()` | reuse as knowledge runtime endpoint |
| `GET /memory/search` | Calls `MemoryManager.search()` | reuse as memory runtime endpoint |
| `POST /memory/add` | Calls `MemoryManager.add()` | reuse |
| `GET /memory/all` | Lists user memories | reuse |
| `GET /context/build` | Calls `ContextBuilder.build_async()` | extend to unified contract |
| `GET /second-brain/corpora` | Lists file-first corpus registry | reuse as workspace/registry endpoint |
| `GET /second-brain/route` | Routes query to registry corpus/version | reuse as routing endpoint |
| `POST /second-brain/context-pack` | Builds lexical file-first context pack | replace role with runtime-backed export |
| `GET /second-brain/corpora/{corpus_id}/status` | Reports registry/acquisition status | reuse |
| `POST /second-brain/memory-pack` | Builds active file-first memory pack | extend as audit/export endpoint |
| `GET /second-brain/status` | Reports lifecycle status | extend with runtime/workspace split |
| `POST /second-brain/bootstrap` | Builds memory pack + route/status | extend to unified context/bootstrap |
| `POST /second-brain/handoff` | Records handoff evidence | reuse |
| `POST /admin/save_workflow` | Writes verified workflow file | reuse, but verify runtime indexing path |
| `POST /admin/deprecate_workflow` | Marks workflow deprecated | reuse |
| `POST /admin/convert_docs` | Converts docs to Markdown | reuse as ingestion helper |
| `POST /admin/build_index` | Runs massive Qdrant index builder | reuse as runtime indexing helper |
| `POST /admin/open_dashboard` | Starts dashboard | reuse |

## MCP Tool Entry Points

| Tool | Current target | Decision |
|---|---|---|
| `search_knowledge` | `/rag/search` | runtime-backed; keep |
| `search_memory` | `/memory/search` | runtime-backed; keep |
| `add_memory` | `/memory/add` | runtime-backed; keep |
| `save_verified_workflow` | `/admin/save_workflow` | workspace write + runtime indexing watch; keep |
| `deprecate_workflow` | `/admin/deprecate_workflow` | workspace lifecycle; keep |
| `search_workflows` | `/rag/search` with `Workflows` tag | runtime-backed; keep |
| `convert_docs_to_md` | `/admin/convert_docs` | deterministic ingestion helper; keep |
| `build_massive_index` | `/admin/build_index` | runtime indexing helper; keep |
| `open_dashboard` | `/admin/open_dashboard` | keep |
| `list_corpora` | `/second-brain/corpora` | workspace registry; keep |
| `route_docs_query` | `/second-brain/route` | workspace registry routing; keep |
| `build_docs_context_pack` | `/second-brain/context-pack` | replace role with runtime-backed context snapshot |
| `inspect_corpus_status` | `/second-brain/corpora/{corpus_id}/status` | keep |
| `build_active_memory_pack` | `/second-brain/memory-pack` | audit/export; keep |
| `inspect_second_brain_status` | `/second-brain/status` | extend |
| `build_agent_bootstrap` | `/second-brain/bootstrap` | extend to unified context/bootstrap |
| `record_agent_handoff` | `/second-brain/handoff` | keep |

## File-First Workspace Paths

| Path | Role | Decision |
|---|---|---|
| `second-brain/corpora/registry.yaml` | Corpus source of truth | keep |
| `second-brain/corpora/project-bindings.yaml` | Project/version binding | keep |
| `second-brain/corpora/acquisitions/` | Acquisition evidence | keep |
| `second-brain/corpora/crawl-plans/` | Crawl approvals/plans | keep |
| `second-brain/docs/` | Workspace operating docs | keep |
| `second-brain/demo/` | Examples and smoke artifacts | keep but avoid generated churn |
| `second-brain/memory/extraction-runs/` | Extraction evidence | keep |
| `second-brain/memory/lessons/` | Durable lessons | keep |
| `second-brain/memory/packs/` | Generated audit memory packs | keep as generated/export path |
| `second-brain/memory/handoffs/` | Agent handoff evidence | keep |
| `second-brain/reviews/decisions/` | Review audit trail | keep |
| `second-brain/skills/active/` | Reviewed active skills | keep |
| `second-brain/skills/candidates/` | Skill candidates | keep |
| `second-brain/sources/` | Registered source docs | keep |

## Script Entry Points

| Script | Current role | Decision |
|---|---|---|
| `scripts/build_context_pack.py` | Lexical routed context-pack builder | replace production role; runtime-backed export with explicit lexical fallback |
| `scripts/build_memory_pack.py` | File-first active memory pack builder | keep as audit/export over approved artifacts |
| `scripts/build_massive_index.py` | Incremental Qdrant indexing | keep as runtime indexing helper |
| `scripts/convert_html_to_md.py` | HTML to Markdown conversion | keep |
| `scripts/crawl_official_docs.py` | Approved docs crawler | keep |
| `scripts/create_crawl_plan.py` | Crawl plan generator | keep |
| `scripts/evaluate_retrieval.py` | Representative retrieval evaluation | extend for unified runtime cases |
| `scripts/extract_experience.py` | Candidate extraction from evidence | keep |
| `scripts/inspect_frontmatter.py` | Artifact inspection | keep |
| `scripts/load_corpus_registry.py` | Registry loader | keep |
| `scripts/rebuild_qdrant.py` | Qdrant rebuild helper | keep or fold into indexing helper later |
| `scripts/record_handoff.py` | Handoff writer | keep |
| `scripts/record_progress.py` | Legacy progress recording | review before reuse |
| `scripts/register_corpus.py` | Corpus registration | keep |
| `scripts/register_source_document.py` | Source registration | keep |
| `scripts/review_candidate.py` | Review lifecycle transitions | keep |
| `scripts/route_query.py` | Deterministic corpus route | keep for routing, not retrieval |
| `scripts/session_reset.py` | Local session helper | keep if still used |
| `scripts/setup_phase1.py` | Legacy setup helper | deprecate after setup docs replace it |
| `scripts/validate_acquisition.py` | Acquisition validation | keep |
| `scripts/validate_second_brain.py` | Workspace validation | keep/extend |

## Spec Mapping Seed

| Spec | Feature | Initial disposition | Owner direction |
|---|---|---|---|
| 001 | agent-experience-layer | extend | Map durable memory lifecycle into runtime-backed memory/context. |
| 002 | hybrid-retrieval-context-packs | replace role | Context packs become runtime-backed snapshots. |
| 003 | official-docs-acquisition | reuse | Keep corpus acquisition lifecycle. |
| 004 | official-docs-crawler | reuse | Keep deterministic acquisition, feed registry/index. |
| 005 | agent-access-tools | extend | Align access tools to unified runtime contract. |
| 006 | experience-extraction | reuse/extend | Keep extraction/review workflow, clarify runtime boundaries. |
| 007 | candidate-review-workflow | reuse | File-first governance remains valuable. |
| 008 | active-memory-recall | extend | Align with runtime memory/context. |
| 009 | agent-memory-access | extend | Use API/MCP contract consistently. |
| 010 | second-brain-status | reuse/extend | Status should report runtime and workspace health separately. |
| 011 | agent-bootstrap-context | extend | Bootstrap should call unified context path. |
| 012 | agent-handoff-records | reuse | Handoffs remain file-first evidence for future extraction. |

## Open Gaps

| Gap | Severity | Decision needed |
|---|---|---|
| Context-pack builder currently performs lexical corpus search directly | high | Replace production role with runtime-backed export. |
| API has both `/rag/search` and `/second-brain/context-pack` semantics | high | Align around unified context contract. |
| MCP exposes old RAG tools and new second-brain tools side by side | high | Keep tools but document which are runtime-backed and which are audit/export. |
| Qdrant/Mem0 availability differs by local setup | medium | Add degraded warnings and representative mocks. |
| Runtime-heavy MCP smoke can timeout while loading Qdrant/model providers | medium | Use thin MCP smoke for protocol checks and mocked/small runtime tests before full validation. |

## Stop/Go Status

Current status: **GO for US1 documentation and contract fixtures; HOLD on code
deletion and runtime cutover.**

Rationale:

- There are exactly three high-severity gaps and all have an initial decision.
- No blocking gap lacks an owner.
- Runtime cutover must wait for the unified context contract tests and a
  runtime-backed context-pack adapter.
- Full MCP runtime validation remains pending until Qdrant/model loading is
  tested with a small representative setup or mocks.

Do not delete or remove old lexical/manual paths until a replacement path has a
passing representative test and is documented here.
