"""
record_progress.py
Script to test recording this session's work progress into Mem0.
Run: python record_progress.py
"""

import os
from dotenv import load_dotenv
from agent_core.memory import MemoryManager

# Load env variables
load_dotenv()

def test_record_progress():
    print("=== Testing Memory Registration ===")
    
    # 1. Initialize MemoryManager
    mem = MemoryManager(user_id="personal_user")
    
    # 2. Define the progress text to record
    progress_text = (
        "User successfully initialized the Git repository and completed the Phase 1 setup "
        "for the 'Memory and Second Brain for Agents' project. The local stack is fully functional, "
        "using Gemini 2.5 Flash for Mem0 fact extraction, Gemini Embedding 2 for vector indexing, "
        "and local Qdrant for storage. The static RAG is set up to read Unity 6.3 docs from ./docs."
    )
    
    print("\n[Step 1] Adding progress log to Mem0...")
    success = mem.add(progress_text)
    if success:
        print("  [SUCCESS] Progress logged successfully.")
    else:
        print("  [ERROR] Failed to log progress.")
        return

    # 3. Retrieve and verify the logged progress
    print("\n[Step 2] Querying Mem0 to verify the recorded progress...")
    query = "What is the status of Phase 1 setup and what models are used?"
    results = mem.search(query, limit=3)
    
    if results:
        print(f"  [SUCCESS] Found {len(results)} matching facts in Mem0:")
        for idx, r in enumerate(results):
            fact = r.get("memory") or r.get("fact") or str(r)
            print(f"     {idx+1}. {fact}")
    else:
        print("  [WARN] Search returned no results. Checking all stored memories...")
        all_m = mem.get_all()
        if all_m:
            print(f"  Currently stored memories ({len(all_m)}):")
            for idx, r in enumerate(all_m):
                fact = r.get("memory") or r.get("fact") or str(r)
                print(f"     - {fact}")
        else:
            print("  [ERROR] No memories found in Qdrant database.")

if __name__ == "__main__":
    test_record_progress()
