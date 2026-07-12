import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from scripts.build_massive_index import get_all_valid_files, BATCH_SIZE
from agent_core.knowledge import KnowledgeBase, extract_metadata_from_path
from agent_core.config import config, QDRANT_PATH, COLLECTION_NAME, ROOT_DIR
import time
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from llama_index.core.node_parser import MarkdownNodeParser, SentenceSplitter

def main():
    target_dir = os.path.abspath("docs")
    print(f"Scanning for valid documents in: {target_dir}")
    files = get_all_valid_files(target_dir)
    total_files = len(files)
    if total_files == 0:
        print("No valid text/markdown files found.")
        return
        
    kb = KnowledgeBase()
    print("Initializing Local Embedding Model...")
    kb._setup_settings()
    
    os.makedirs(QDRANT_PATH, exist_ok=True)
    host = config["rag"].get("host")
    if host:
        port = config["rag"].get("port", 6333)
        client = QdrantClient(url=f"http://{host}:{port}")
    else:
        db_path_absolute = os.path.join(ROOT_DIR, config["rag"]["db_path"].replace("./", ""))
        client = QdrantClient(path=db_path_absolute)
        
    vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION_NAME)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # Force rebuild: delete collection if exists
    if client.collection_exists(COLLECTION_NAME):
        client.delete_collection(COLLECTION_NAME)
        
    md_parser = MarkdownNodeParser()
    text_parser = SentenceSplitter(chunk_size=1024, chunk_overlap=100)
    
    # We create an empty index first
    index = VectorStoreIndex.from_documents(
        [], 
        storage_context=storage_context,
        transformations=[md_parser, text_parser]
    )
    
    start_time = time.time()
    for i in range(0, total_files, BATCH_SIZE):
        batch = files[i:i + BATCH_SIZE]
        print(f"\n--- Processing Batch {i//BATCH_SIZE + 1} ({i}/{total_files}) ---")
        try:
            reader = SimpleDirectoryReader(input_files=batch, file_metadata=extract_metadata_from_path)
            documents = reader.load_data()
            for doc in documents:
                doc.doc_id = doc.metadata.get("file_path", doc.doc_id)
                index.insert(doc)
            print(f"Batch {i//BATCH_SIZE + 1} Success!")
        except Exception as e:
            print(f"Failed to process batch {i//BATCH_SIZE + 1}: {e}")
            
    end_time = time.time()
    print(f"\nIndexing complete! Time taken: {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
