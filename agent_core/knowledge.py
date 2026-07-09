"""
agent_core/knowledge.py
Wrapper for LlamaIndex RAG using google-genai integration.
Indexes documents from ./docs.
Supports: .md, .html, .json, .txt
Stores vector database locally in ./db/qdrant_rag, loads existing index if available.
"""

import os
from dotenv import load_dotenv

load_dotenv()

DOCS_DIR = "./docs"
QDRANT_PATH = "./db/qdrant_rag"
COLLECTION_NAME = "personal_knowledge_base"


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
        from llama_index.llms.google_genai import GoogleGenAI
        api_key = os.getenv("GEMINI_API_KEY")
        
        # 1. Use HuggingFace for offline, unlimited local embeddings (CPU optimized for Ryzen 7)
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
        
        # 2. Use Gemini for LLM synthesis (if needed)
        Settings.llm = GoogleGenAI(
            model="gemini-2.5-flash", api_key=api_key
        )

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

            client = QdrantClient(host="localhost", port=6333)
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
                reader = SimpleDirectoryReader(input_files=input_files)
            else:
                # Count valid document files
                valid_exts = {".md", ".html", ".json", ".txt"}
                doc_files = []
                for root, _, files in os.walk(DOCS_DIR):
                    for f in files:
                        if os.path.splitext(f)[1].lower() in valid_exts:
                            doc_files.append(os.path.join(root, f))
                if not doc_files:
                    print(f"[KnowledgeBase] [WARN] Directory {DOCS_DIR} has no valid files.")
                    self._ready = False
                    return False

                # Apply limit if specified
                if limit:
                    print(f"[KnowledgeBase] Indexing limited to first {limit} files (total files: {len(doc_files)})...")
                else:
                    print(f"[KnowledgeBase] Indexing all {len(doc_files)} files...")

                reader = SimpleDirectoryReader(
                    input_dir=DOCS_DIR, recursive=True,
                    required_exts=list(valid_exts),
                    num_files_limit=limit
                )

            storage_context = StorageContext.from_defaults(vector_store=vector_store)
            documents = reader.load_data()
            self._index = VectorStoreIndex.from_documents(
                documents, storage_context=storage_context, show_progress=True
            )
            self._ready = True
            print(f"[KnowledgeBase] [SUCCESS] Indexed {len(documents)} document chunks.")
            return True
        except Exception as e:
            print(f"[KnowledgeBase.load] Error: {e}")
            return False

    def reload(self, limit: int = None, input_files: list[str] = None) -> bool:
        """Reload index when docs are updated."""
        self._index = None
        self._ready = False
        return self.load(limit=limit, input_files=input_files, force_rebuild=True)

    def search(self, query: str, top_k: int = 3) -> str:
        """
        Search and retrieve raw text snippets.
        No LLM synthesis is done here to save context tokens.
        """
        if not self._ready or self._index is None:
            return "(KnowledgeBase not loaded. Please call kb.load() first)"
        try:
            retriever = self._index.as_retriever(similarity_top_k=top_k)
            nodes = retriever.retrieve(query)
            if not nodes:
                return "(No matching documentation found)"
            parts = []
            for node in nodes:
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
