import os
import sys
from qdrant_client import QdrantClient

# Thêm root_dir vào sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.config import config, COLLECTION_NAME, MEM0_CONFIG

def main():
    print("=" * 55)
    print("  QDRANT REBUILD SCRIPT (PHASE 2)")
    print("=" * 55)
    
    qdrant_host = config["memory"]["qdrant"]["host"]
    qdrant_port = config["memory"]["qdrant"]["port"]
    
    try:
        client = QdrantClient(host=qdrant_host, port=qdrant_port)
    except Exception as e:
        print(f"[Error] Could not connect to Qdrant at {qdrant_host}:{qdrant_port} - {e}")
        return

    # Drop RAG Collection
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        print(f"[SUCCESS] Deleted RAG collection: {COLLECTION_NAME}")
    else:
        print(f"[INFO] RAG collection {COLLECTION_NAME} does not exist.")
        
    # Drop Mem0 Collection
    mem0_collection = MEM0_CONFIG["vector_store"]["config"]["collection_name"]
    if client.collection_exists(mem0_collection):
        client.delete_collection(mem0_collection)
        print(f"[SUCCESS] Deleted Mem0 collection: {mem0_collection}")
    else:
        print(f"[INFO] Mem0 collection {mem0_collection} does not exist.")

    print("\n[INFO] Re-indexing RAG with Semantic Chunking (MarkdownNodeParser)...")
    from agent_core.knowledge import KnowledgeBase
    kb = KnowledgeBase()
    # force_rebuild = True to ensure it creates the collection again
    success = kb.load(force_rebuild=True)
    
    if success:
        print("\n[SUCCESS] Rebuild complete! Vectors have been updated.")
    else:
        print("\n[FAILED] Rebuild encountered an error.")

if __name__ == '__main__':
    main()
