"""
tools/build_massive_index.py
Offline batch indexing script for massive corpus (e.g. Unity Docs 40,000 files).
Uses local HuggingFace embeddings via CPU. Runs in batches to prevent OOM errors.
"""

import os
import sys
import time
import argparse

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.knowledge import KnowledgeBase

BATCH_SIZE = 100  # Safe batch size for Ryzen 7 5800H / 16GB RAM
VALID_EXTS = {".md", ".txt", ".json"}

def get_all_valid_files(target_dir):
    valid_files = []
    if not os.path.exists(target_dir):
        print(f"Directory not found: {target_dir}")
        return []
        
    for root, _, files in os.walk(target_dir):
        for f in files:
            if os.path.splitext(f)[1].lower() in VALID_EXTS:
                valid_files.append(os.path.join(root, f))
    return valid_files

def main():
    parser = argparse.ArgumentParser(description="Batch index documents for RAG")
    parser.add_argument("target_dir", help="Path to the directory containing Markdown/Text files to index")
    args = parser.parse_args()

    target_dir = os.path.abspath(args.target_dir)

    print(f"Scanning for valid documents in: {target_dir}")
    files = get_all_valid_files(target_dir)
    total_files = len(files)
    
    if total_files == 0:
        print("No valid text/markdown files found.")
        return
        
    print(f"Found {total_files} valid files. Starting batch indexing (Batch size: {BATCH_SIZE}).")
    kb = KnowledgeBase()
    
    # Pre-load settings (download HuggingFace model if first time)
    print("Initializing Local Embedding Model (HuggingFace BAAI/bge-small-en-v1.5)...")
    kb._setup_settings()
    
    start_time = time.time()
    for i in range(0, total_files, BATCH_SIZE):
        batch = files[i:i + BATCH_SIZE]
        print(f"\n--- Processing Batch {i//BATCH_SIZE + 1} ({i}/{total_files}) ---")
        
        success = kb.load(input_files=batch, force_rebuild=True)
        if not success:
            print(f"Failed to process batch {i//BATCH_SIZE + 1}. Continuing...")
            
    end_time = time.time()
    print(f"\nIndexing complete! Time taken: {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
