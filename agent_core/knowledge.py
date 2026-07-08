"""
agent_core/knowledge.py
Wrapper cho LlamaIndex RAG — lập chỉ mục tài liệu từ ./docs.
Hỗ trợ: .md, .html, .json, .txt
Lưu trữ vector cục bộ trong ./db/qdrant_rag
"""

import os
from dotenv import load_dotenv

load_dotenv()

DOCS_DIR = "./docs"
QDRANT_PATH = "./db/qdrant_rag"
COLLECTION_NAME = "personal_knowledge_base"


class KnowledgeBase:
    """
    Quản lý tri thức tĩnh từ các file tài liệu trong ./docs.
    
    Cách dùng:
        kb = KnowledgeBase()
        kb.load()
        result = kb.search("cấu hình database")
    """

    def __init__(self):
        self._index = None
        self._ready = False

    def _setup_settings(self):
        """Cấu hình Gemini làm LLM + Embedder cho LlamaIndex."""
        from llama_index.core import Settings
        from llama_index.embeddings.gemini import GeminiEmbedding
        from llama_index.llms.gemini import Gemini
        api_key = os.getenv("GEMINI_API_KEY")
        Settings.embed_model = GeminiEmbedding(
            model_name="models/text-embedding-004", api_key=api_key
        )
        Settings.llm = Gemini(
            model="models/gemini-1.5-flash", api_key=api_key
        )

    def load(self) -> bool:
        """
        Lập chỉ mục toàn bộ file trong ./docs và nạp vào bộ nhớ.
        Gọi hàm này 1 lần khi khởi động, hoặc sau khi thêm file mới.
        """
        try:
            from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
            from llama_index.vector_stores.qdrant import QdrantVectorStore
            from qdrant_client import QdrantClient

            self._setup_settings()
            os.makedirs(QDRANT_PATH, exist_ok=True)
            os.makedirs(DOCS_DIR, exist_ok=True)

            # Đếm file hợp lệ
            valid_exts = {".md", ".html", ".json", ".txt"}
            doc_files = [
                f for root, _, files in os.walk(DOCS_DIR)
                for f in files if os.path.splitext(f)[1].lower() in valid_exts
            ]
            if not doc_files:
                print(f"[KnowledgeBase] ⚠️  Thư mục {DOCS_DIR} trống. "
                      "Hãy thêm file .md/.html/.json/.txt vào đó.")
                self._ready = False
                return False

            print(f"[KnowledgeBase] Đang lập chỉ mục {len(doc_files)} file...")
            client = QdrantClient(path=QDRANT_PATH)
            vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
            storage_context = StorageContext.from_defaults(vector_store=vector_store)

            reader = SimpleDirectoryReader(
                input_dir=DOCS_DIR, recursive=True,
                required_exts=list(valid_exts)
            )
            documents = reader.load_data()
            self._index = VectorStoreIndex.from_documents(
                documents, storage_context=storage_context, show_progress=True
            )
            self._ready = True
            print(f"[KnowledgeBase] ✅ Đã lập chỉ mục {len(documents)} đoạn văn bản.")
            return True
        except Exception as e:
            print(f"[KnowledgeBase.load] Lỗi: {e}")
            return False

    def reload(self) -> bool:
        """Nạp lại chỉ mục sau khi thêm file mới vào ./docs."""
        self._index = None
        self._ready = False
        return self.load()

    def search(self, query: str, top_k: int = 3) -> str:
        """
        Tìm kiếm và trả về các đoạn tài liệu gốc liên quan nhất.
        Không tóm tắt qua LLM — trả về nội dung nguyên bản để tiết kiệm token.
        """
        if not self._ready or self._index is None:
            return "(KnowledgeBase chưa được load. Hãy gọi kb.load() trước)"
        try:
            retriever = self._index.as_retriever(similarity_top_k=top_k)
            nodes = retriever.retrieve(query)
            if not nodes:
                return "(Không tìm thấy thông tin liên quan trong tài liệu)"
            parts = []
            for node in nodes:
                source = node.metadata.get("file_name", "unknown")
                content = node.get_content()[:1000]  # Giới hạn 1000 ký tự/đoạn
                parts.append(f"[Nguồn: {source}]\n{content}")
            return "\n\n---\n\n".join(parts)
        except Exception as e:
            return f"(Lỗi khi tìm kiếm RAG: {e})"

    def list_docs(self) -> list[str]:
        """Liệt kê các file tài liệu đang được theo dõi trong ./docs."""
        valid_exts = {".md", ".html", ".json", ".txt"}
        files = []
        if os.path.exists(DOCS_DIR):
            for root, _, filenames in os.walk(DOCS_DIR):
                for f in filenames:
                    if os.path.splitext(f)[1].lower() in valid_exts:
                        files.append(os.path.relpath(os.path.join(root, f), DOCS_DIR))
        return files
