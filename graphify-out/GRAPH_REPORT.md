# Graph Report - .  (2026-07-12)

## Corpus Check
- Corpus is ~9,596 words - fits in a single context window. You may not need a graph.

## Summary
- 205 nodes · 316 edges · 14 communities (12 shown, 2 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 26 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9
- Community 10
- Community 11
- Community 13

## God Nodes (most connected - your core abstractions)
1. `MemoryManager` - 31 edges
2. `KnowledgeBase` - 28 edges
3. `ContextBuilder` - 16 edges
4. `DocsChangeHandler` - 10 edges
5. `Manifest` - 10 edges
6. `main()` - 9 edges
7. `get_memory()` - 8 edges
8. `get_knowledge()` - 8 edges
9. `MemoryAddRequest` - 6 edges
10. `WorkflowRequest` - 6 edges

## Surprising Connections (you probably didn't know these)
- `BuildIndexRequest` --uses--> `KnowledgeBase`  [INFERRED]
  api/api_server.py → agent_core/knowledge.py
- `ConvertDocsRequest` --uses--> `KnowledgeBase`  [INFERRED]
  api/api_server.py → agent_core/knowledge.py
- `DeprecateRequest` --uses--> `KnowledgeBase`  [INFERRED]
  api/api_server.py → agent_core/knowledge.py
- `DocsChangeHandler` --uses--> `KnowledgeBase`  [INFERRED]
  api/api_server.py → agent_core/knowledge.py
- `MemoryAddRequest` --uses--> `KnowledgeBase`  [INFERRED]
  api/api_server.py → agent_core/knowledge.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Centralized Second Brain Architecture** — readme_central_api_server, readme_mem0_memory, readme_llamaindex_rag, readme_mcp_bridge [EXTRACTED 1.00]
- **Qdrant-Backed Memory and Knowledge Stores** — compose_qdrant_service, config_rag_server, config_memory_configuration [EXTRACTED 1.00]

## Communities (14 total, 2 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.08
Nodes (29): ContextBuilder, Kết hợp Mem0 + RAG để tạo System Prompt hoàn chỉnh trước mỗi lần gọi LLM., Tạo System Prompt hoàn chỉnh bằng cách chạy Song Song (Parallel)         tìm kiế, Lưu cuộc tương tác vào Mem0 để Agent học từ phản hồi.         CHỈ gọi khi phát h, admin_build_index(), admin_convert_docs(), admin_deprecate_workflow(), admin_save_workflow() (+21 more)

### Community 1 - "Community 1"
Cohesion: 0.08
Nodes (25): extract_metadata_from_path(), KnowledgeBase, Loads the index from Qdrant local storage, or builds it from ./docs if not found, Extract folder names as tags, and parse YAML frontmatter for 'requires' capabili, Reload index when docs are updated., Incremental RAG Sync: Update a single file without rebuilding everything., Search and retrieve raw text snippets.         Uses HyDE Query Transform for ac, List files currently in the docs/ directory. (+17 more)

### Community 2 - "Community 2"
Cohesion: 0.10
Nodes (18): MemoryManager, Format list of memories into a bulleted string for the System Prompt., Manages long-term personal agent memory.          Usage:         mem = MemoryMan, Record new facts/dialogue history. Mem0 automatically extracts facts., Search related memories using semantic retrieval with Mem0 v2.0+ filters., Retrieve all facts across the user., Clear all stored memories for the user., Record the execution result of a specific skill for capability tracking. (+10 more)

### Community 3 - "Community 3"
Cohesion: 0.20
Nodes (13): chunk_file(), ensure_collection(), file_digest(), get_all_valid_files(), main(), make_client(), Manifest, parse_args() (+5 more)

### Community 4 - "Community 4"
Cohesion: 0.10
Nodes (19): add_memory(), build_massive_index(), convert_docs_to_md(), deprecate_workflow(), open_dashboard(), second_brain_mcp.py Model Context Protocol (MCP) Server stdio bridge (Thin-Clien, Đánh dấu một Workflow là lỗi thời (Deprecated) nếu nó không còn hoạt động tốt ho, Tìm kiếm các Workflow và Kinh nghiệm đã được xác minh (Verified) trong Second Br (+11 more)

### Community 5 - "Community 5"
Cohesion: 0.13
Nodes (18): Qdrant 1.18.2 Service, Qdrant Persistent Named Volume, BAAI bge-small-en-v1.5 Embedding Model, Mem0 v1.1 Memory Configuration, Server-Mode RAG Configuration, API-First Architecture, Central API Server, LlamaIndex Static Knowledge RAG (+10 more)

### Community 6 - "Community 6"
Cohesion: 0.20
Nodes (6): get_memory(), memory_all(), memory_search(), Search dynamic long-term memories., Get all dynamic memories for a user., test_memory_managers_are_isolated_by_user()

### Community 7 - "Community 7"
Cohesion: 0.31
Nodes (4): agent_core/context_builder.py Tự động xây dựng System Prompt bằng cách kết hợp:, agent_core/__init__.py Module trung tâm — cung cấp interface thống nhất cho Mem0, agent_core/knowledge.py Wrapper for LlamaIndex RAG using google-genai integrati, agent_core/memory.py Wrapper for Mem0 using Gemini Flash as the LLM extractor. S

### Community 8 - "Community 8"
Cohesion: 0.29
Nodes (6): mock_llama_settings(), mock_mem0(), mock_qdrant(), Mocks the mem0.Memory class to avoid real API/DB calls., Mocks QdrantClient used in KnowledgeBase., Mocks LlamaIndex Settings to avoid loading heavy models.

### Community 9 - "Community 9"
Cohesion: 0.47
Nodes (5): get_git_branch(), get_git_changes(), main(), session_reset.py Công cụ chốt phiên chat để tiết kiệm token. Hỗ trợ quản lý nhiề, Lấy tên branch hiện tại để tự động đặt tên session.

### Community 10 - "Community 10"
Cohesion: 0.67
Nodes (3): main(), process_html_file(), tools/convert_html_to_md.py Parses Unity documentation HTML files, extracts the

## Knowledge Gaps
- **5 isolated node(s):** `Memory and Second Brain for Agents`, `Watchdog Auto-Sync`, `Second Brain MCP Bridge`, `Qdrant Persistent Named Volume`, `Tiered Model Registry`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `MemoryManager` connect `Community 2` to `Community 0`, `Community 1`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.204) - this node is a cross-community bridge._
- **Why does `KnowledgeBase` connect `Community 1` to `Community 0`, `Community 7`?**
  _High betweenness centrality (0.182) - this node is a cross-community bridge._
- **Why does `ContextBuilder` connect `Community 0` to `Community 1`, `Community 2`, `Community 7`?**
  _High betweenness centrality (0.047) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `MemoryManager` (e.g. with `ContextBuilder` and `BuildIndexRequest`) actually correct?**
  _`MemoryManager` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `KnowledgeBase` (e.g. with `ContextBuilder` and `BuildIndexRequest`) actually correct?**
  _`KnowledgeBase` has 7 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `ContextBuilder` (e.g. with `KnowledgeBase` and `MemoryManager`) actually correct?**
  _`ContextBuilder` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `DocsChangeHandler` (e.g. with `ContextBuilder` and `KnowledgeBase`) actually correct?**
  _`DocsChangeHandler` has 3 INFERRED edges - model-reasoned connections that need verification._