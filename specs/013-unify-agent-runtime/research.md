# Research: Unify Agent Runtime

## Decision: Merge the projects into one unified runtime

**Rationale**: Expert review and local code inspection agree that separating the new second-brain layer from the original project would create two sources of truth. The original project already owns model-backed retrieval and personal memory through `agent_core`, API, and MCP. The new layer should supply file-first governance, audit, corpus lifecycle, and context-pack snapshots.

**Alternatives considered**:

- Fully separate project: rejected because agents would still need to choose between RAG-backed tools and file-first tools.
- Keep both systems parallel: rejected because duplicated retrieval already produced a quality mismatch during MCP testing.
- Rewrite everything under the new second-brain structure: rejected because it discards working LlamaIndex, Qdrant, Mem0, model registry, API, and MCP investments.

## Decision: `agent_core` is the runtime source of truth

**Rationale**: `agent_core/knowledge.py` already wraps LlamaIndex, Qdrant, embeddings, HyDE, corpus metadata, and capability filters. `agent_core/memory.py` owns Mem0 memory. `agent_core/context_builder.py` combines memory and knowledge for agent prompts. This is the natural runtime spine.

**Alternatives considered**:

- Make `scripts/build_context_pack.py` the retrieval engine: rejected because it is deterministic lexical/file scanning and cannot replace vector/model retrieval.
- Move runtime into `second-brain/`: rejected for now because it would be a broad structural rewrite.

## Decision: `second-brain/` is a file-first workspace

**Rationale**: The constitution requires file-first artifacts, provenance, lifecycle states, and auditability. Those goals fit `second-brain/` as a data/review/spec workspace, not as a competing runtime.

**Alternatives considered**:

- Delete `second-brain/`: rejected because it contains the new governance model, reviews, memory packs, corpus registry, and spec-kit-aligned lifecycle.
- Treat `second-brain/` as an app package: rejected because runtime ownership already exists in `agent_core`.

## Decision: Context packs become audit/export snapshots

**Rationale**: Agents need bounded context packs, but source selection should come from unified runtime retrieval. Context-pack generation should consume or call runtime results, then write a Markdown/YAML snapshot for inspection and reuse.

**Alternatives considered**:

- Continue lexical context-pack ranking as primary retrieval: rejected because it bypasses Qdrant/model-backed retrieval and fails non-English/user-intent queries.
- Remove context packs: rejected because they are the agent-facing contract and audit trail.

## Decision: Feature 013 is contract-first, then thin cutover

**Rationale**: The safest start is to map specs 001-012 and current runtime capabilities before moving code. The completion phase should prove one end-to-end flow through API/MCP and runtime, not solve every future concern.

**Alternatives considered**:

- Start deleting folders immediately: rejected because some files are still source of truth or evidence.
- Combine migration, auth, observability, provider changes, and RAG tuning into this phase: rejected as scope creep.

## Expert Consultation Summary

- Multi-agent architecture review recommended one runtime path: query -> MCP/API -> ContextBuilder -> KnowledgeBase/Mem0.
- Project management review recommended `013-unify-agent-core-second-brain` as a contract-first consolidation phase with a stop rule before code integration.
- Both expert perspectives warned against keeping lexical/manual search as a parallel production engine.
