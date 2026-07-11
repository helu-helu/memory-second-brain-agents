"""
agent_core/knowledge.py
Wrapper for LlamaIndex RAG using google-genai integration.
Indexes documents from ./docs.
Supports: .md, .html, .json, .txt
Stores vector database locally in ./db/qdrant_rag, loads existing index if available.
"""

import os
import yaml
from dotenv import load_dotenv

from agent_core.config import config, DOCS_DIR, SKILLS_DIR, QDRANT_PATH, COLLECTION_NAME, ROOT_DIR

load_dotenv()


def extract_metadata_from_path(file_path: str) -> dict:
    """Extract folder names as tags, and parse YAML frontmatter for 'requires' capability."""
    metadata = {}
    
    # 1. Tags from folder path
    file_path_norm = os.path.normcase(os.path.abspath(file_path))
    docs_dir_norm = os.path.normcase(os.path.abspath(DOCS_DIR))
    skills_dir_norm = os.path.normcase(os.path.abspath(SKILLS_DIR))
    
    if file_path_norm.startswith(docs_dir_norm):
        rel_path = os.path.relpath(file_path, docs_dir_norm)
    elif file_path_norm.startswith(skills_dir_norm):
        rel_path = os.path.relpath(file_path, skills_dir_norm)
    else:
        rel_path = os.path.basename(file_path)
        
    parts = os.path.normpath(rel_path).split(os.sep)[:-1]
    tags = [p for p in parts if p != "." and p != ".."]
    metadata["tags"] = tags
    
    # 2. Parse YAML Frontmatter for Capability routing
    if file_path.endswith('.md'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content.startswith('---'):
                    end_idx = content.find('---', 3)
                    if end_idx != -1:
                        frontmatter = content[3:end_idx]
                        data = yaml.safe_load(frontmatter)
                        if data and "requires" in data:
                            reqs = data["requires"]
                            if isinstance(reqs, dict):
                                if "tier" in reqs:
                                    metadata["requires_tier"] = reqs["tier"]
                                if "features" in reqs and isinstance(reqs["features"], list):
                                    metadata["requires_features"] = reqs["features"]
        except Exception:
            pass
            
    return metadata


class KnowledgeBase:
    """
    Manages static knowledge retrieval from ./docs.
    
    Usage:
        kb = KnowledgeBase()
        kb.load()
        result = kb.search("database setup")
    """

    def __init__(self):
        self._index = None
        self._ready = False

    def _setup_settings(self):
        """Configure LLM and Embedding models."""
        from llama_index.core import Settings
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding
        
        # 1. Use HuggingFace for offline, unlimited local embeddings (CPU optimized for Ryzen 7)
        Settings.embed_model = HuggingFaceEmbedding(model_name=config["rag"]["embedding_model"])
        
        # 2. Use LLM dynamically based on model_registry
        llm_model = config.get("model_registry", {}).get("llm_model", "gemini-2.5-flash")
        llm_model_lower = llm_model.lower()
        
        if "gemini" in llm_model_lower:
            from llama_index.llms.google_genai import GoogleGenAI
            Settings.llm = GoogleGenAI(model=llm_model, api_key=os.getenv("GEMINI_API_KEY"))
        elif "gpt" in llm_model_lower:
            from llama_index.llms.openai import OpenAI
            Settings.llm = OpenAI(model=llm_model, api_key=os.getenv("OPENAI_API_KEY"))
        elif "claude" in llm_model_lower:
            from llama_index.llms.anthropic import Anthropic
            Settings.llm = Anthropic(model=llm_model, api_key=os.getenv("ANTHROPIC_API_KEY"))
        else:
            print(f"[KnowledgeBase] Warning: Unknown LLM {llm_model}. Falling back to Gemini.")
            from llama_index.llms.google_genai import GoogleGenAI
            Settings.llm = GoogleGenAI(model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

    def load(self, limit: int = None, input_files: list[str] = None, force_rebuild: bool = False) -> bool:
        """
        Loads the index from Qdrant local storage, or builds it from ./docs if not found.
        """
        try:
            from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
            from llama_index.vector_stores.qdrant import QdrantVectorStore
            from qdrant_client import QdrantClient

            self._setup_settings()
            os.makedirs(QDRANT_PATH, exist_ok=True)
            os.makedirs(DOCS_DIR, exist_ok=True)

            client = QdrantClient(path=os.path.join(ROOT_DIR, config["rag"]["db_path"].replace("./", "")))
            vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)

            # Check if index already exists in Qdrant to avoid rebuilding (saves tokens and time)
            try:
                if not force_rebuild and client.collection_exists(COLLECTION_NAME):
                    collection_info = client.get_collection(COLLECTION_NAME)
                    if collection_info.points_count > 0 and not input_files:
                        print(f"[KnowledgeBase] Found existing index with {collection_info.points_count} vectors. Loading...")
                        self._index = VectorStoreIndex.from_vector_store(
                            vector_store=vector_store
                        )
                        self._ready = True
                        return True
            except Exception as e:
                print(f"[KnowledgeBase] Info checking collection: {e}")

            # Rebuild index from files
            if input_files:
                print(f"[KnowledgeBase] Indexing specific files: {input_files}")
                reader = SimpleDirectoryReader(
                    input_files=input_files,
                    file_metadata=extract_metadata_from_path
                )
            else:
                # Count valid document files
                valid_exts = {".md", ".html", ".json", ".txt"}
                doc_files = []
                for search_dir in [DOCS_DIR, SKILLS_DIR]:
                    if os.path.exists(search_dir):
                        for root, _, files in os.walk(search_dir):
                            for f in files:
                                if os.path.splitext(f)[1].lower() in valid_exts:
                                    doc_files.append(os.path.join(root, f))
                if not doc_files:
                    print(f"[KnowledgeBase] [WARN] No valid files found in {DOCS_DIR} or {SKILLS_DIR}.")
                    self._ready = False
                    return False

                # Apply limit if specified
                if limit:
                    print(f"[KnowledgeBase] Indexing limited to first {limit} files (total files: {len(doc_files)})...")
                    doc_files = doc_files[:limit]
                else:
                    print(f"[KnowledgeBase] Indexing all {len(doc_files)} files...")

                reader = SimpleDirectoryReader(
                    input_files=doc_files,
                    file_metadata=extract_metadata_from_path
                )

            from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter
            
            # Apply Phase 2: Advanced Semantic Chunking
            md_parser = MarkdownNodeParser()
            text_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=100)
            
            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            documents = reader.load_data()
            
            # Set deterministic doc_id based on file path for easy updates
            for doc in documents:
                doc.doc_id = doc.metadata.get("file_path", doc.doc_id)
                
            self._index = VectorStoreIndex.from_documents(
                documents, 
                storage_context=storage_context, 
                transformations=[md_parser, text_parser],
                show_progress=True
            )
            self._ready = True
            print(f"[KnowledgeBase] [SUCCESS] Indexed {len(documents)} documents using Semantic Chunking.")
            return True
        except Exception as e:
            print(f"[KnowledgeBase.load] Error: {e}")
            return False

    def reload(self, limit: int = None, input_files: list[str] = None) -> bool:
        """Reload index when docs are updated."""
        self._index = None
        self._ready = False
        return self.load(limit=limit, input_files=input_files, force_rebuild=True)

    def insert_file(self, file_path: str) -> bool:
        """Incremental RAG Sync: Update a single file without rebuilding everything."""
        if not self._ready or self._index is None:
            return self.load()
        try:
            from llama_index.core import SimpleDirectoryReader
            reader = SimpleDirectoryReader(
                input_files=[file_path], 
                file_metadata=extract_metadata_from_path
            )
            documents = reader.load_data()
            
            # Use file_path as doc_id to overwrite existing embeddings
            for doc in documents:
                doc.doc_id = doc.metadata.get("file_path", file_path)
                
            for doc in documents:
                self._index.insert(doc)
            print(f"[KnowledgeBase] [Incremental Sync] Successfully updated: {file_path}")
            return True
        except Exception as e:
            print(f"[KnowledgeBase] [Incremental Sync] Failed for {file_path}: {e}")
            return False

    def search(self, query: str, top_k: int = None, tags: list[str] = None, requires: dict = None) -> str:
        """
        Search and retrieve raw text snippets.
        Uses HyDE Query Transform for accuracy and supports metadata tag & capability filtering.
        """
        try:
            from llama_index.core.indices.query.query_transform import HyDEQueryTransform
            from llama_index.core.vector_stores import MetadataFilters, ExactMatchFilter

            if not self._ready:
                return "(Knowledge Base is not loaded)"

            top_k = top_k or config.get("rag", {}).get("top_k", 3)
            
            # Setup Metadata Filters (Tags only)
            filters = None
            if tags:
                filter_list = [ExactMatchFilter(key="tags", value=tag) for tag in tags]
                filters = MetadataFilters(filters=filter_list)
                
            # Increase initial retrieval if we are applying capability filters later
            retriever_k = top_k * 3 if requires else top_k
            retriever = self._index.as_retriever(similarity_top_k=retriever_k, filters=filters)
            
            # Setup HyDE Query Rewriting
            print(f"[KnowledgeBase] Running HyDE Query Transform for: '{query}'")
            hyde = HyDEQueryTransform(include_original=True)
            query_bundle = hyde(query)
            print(f"[KnowledgeBase] HyDE generated fake answer length: {len(query_bundle.custom_embedding_strs[0]) if query_bundle.custom_embedding_strs else 0}")
            
            nodes = retriever.retrieve(query_bundle)
            if not nodes:
                return "(No matching documentation found)"
                
            # Post-retrieval Capability Filtering
            valid_nodes = []
            tier_rank = {"nano": 1, "standard": 2, "reasoning": 3, "frontier": 4}
            
            for node in nodes:
                req_tier = node.metadata.get("requires_tier")
                req_features = node.metadata.get("requires_features", [])
                
                # General document without requirements
                if not req_tier and not req_features:
                    valid_nodes.append(node)
                    continue
                    
                # Capability check
                if requires:
                    model_tier = requires.get("tier", "nano")
                    model_features = set(requires.get("features", []))
                    
                    if req_tier and tier_rank.get(model_tier, 0) < tier_rank.get(req_tier, 1):
                        continue # Model tier is too low
                        
                    if req_features:
                        if isinstance(req_features, str):
                            req_features = [req_features]
                        missing_features = set(req_features) - model_features
                        if missing_features:
                            continue # Missing features
                            
                    valid_nodes.append(node)
                    
            valid_nodes = valid_nodes[:top_k]
            if not valid_nodes:
                return "(Matching documentation found but filtered out due to model capability constraints)"
                
            parts = []
            for node in valid_nodes:
                source = node.metadata.get("file_name", "unknown")
                content = node.get_content()[:1000]
                parts.append(f"[Source: {source}]\n{content}")
            return "\n\n---\n\n".join(parts)
        except Exception as e:
            return f"(RAG Search Error: {e})"

    def list_docs(self) -> list[str]:
        """List files currently in the docs/ directory."""
        valid_exts = {".md", ".html", ".json", ".txt"}
        files = []
        if os.path.exists(DOCS_DIR):
            for root, _, filenames in os.walk(DOCS_DIR):
                for f in filenames:
                    if os.path.splitext(f)[1].lower() in valid_exts:
                        files.append(os.path.relpath(os.path.join(root, f), DOCS_DIR))
        return files
