"""
setup_phase1.py
Script to check and verify the Phase 1 setup.
Run: python setup_phase1.py
"""

import os
import sys

def step(n, total, label):
    print(f"\n[{n}/{total}] {label}...")

def check_env():
    step(1, 5, "Checking GEMINI_API_KEY")
    from dotenv import load_dotenv
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY", "")
    if not key or "your_gemini" in key:
        print("  [ERROR] GEMINI_API_KEY not configured in .env")
        print("  -> Copy .env.example to .env and fill in your API key")
        print("  -> Get free key: https://aistudio.google.com/app/apikey")
        return False
    print(f"  [SUCCESS] Key configured successfully ({key[:8]}...)")
    return True

def check_libs():
    step(2, 5, "Checking Python libraries")
    libs = {
        "mem0ai": "mem0",
        "llama_index": "llama_index.core",
        "qdrant_client": "qdrant_client",
        "dotenv": "dotenv",
    }
    import importlib
    missing = [pkg for pkg, mod in libs.items() if importlib.util.find_spec(mod) is None]
    if missing:
        print(f"  [ERROR] Missing packages: {', '.join(missing)}")
        print("  -> Run: pip install -r requirements.txt")
        return False
    print("  [SUCCESS] All libraries are installed.")
    return True

def check_dirs():
    step(3, 5, "Checking directory structure")
    for d in ["./docs", "./db", "./scratch", "./agent_core"]:
        os.makedirs(d, exist_ok=True)
    print("  [SUCCESS] Folders ready: docs/, db/, scratch/, agent_core/")

    # Check doc files
    docs = []
    valid_exts = {".md", ".html", ".json", ".txt"}
    for root, _, files in os.walk("./docs"):
        for f in files:
            if os.path.splitext(f)[1].lower() in valid_exts:
                docs.append(f)
    if not docs:
        sample = "./docs/00_coding_preferences.md"
        with open(sample, "w", encoding="utf-8") as f:
            f.write("""# Coding Preferences

## Language & Style
- Main language: Python 3.11+
- Always write async/await for I/O tasks
- Handle exceptions using try/except

## Database & Config
- Vector DB: Qdrant (local path ./db/qdrant_mem0)
- History DB: SQLite (./db/mem0_history.db)
- Default local port: 8000
""")
        print(f"  [FILE] Created sample doc: {sample}")
    else:
        print(f"  [FILE] docs/ has {len(docs)} files. Example: {docs[:3]}")
    return True

def check_memory():
    step(4, 5, "Checking Mem0 (write + search)")
    try:
        from agent_core.memory import MemoryManager
        mem = MemoryManager(user_id="setup_test")
        test = "User prefers Python async coding and runs DB on port 8000"
        ok = mem.add(test)
        if not ok:
            print("  [ERROR] Failed to write to Mem0")
            return False
        results = mem.search("coding style database port", limit=3)
        if results:
            print(f"  [SUCCESS] Mem0 OK - Found {len(results)} memories:")
            for r in results[:2]:
                fact = r.get("memory") or r.get("fact") or str(r)
                print(f"     . {fact[:80]}")
        else:
            print("  [WARN] Mem0 wrote successfully but search returned no results yet.")
        return True
    except Exception as e:
        print(f"  [ERROR] Mem0 Error: {e}")
        return False

def check_knowledge():
    step(5, 5, "Checking RAG LlamaIndex (indexing + search)")
    try:
        from agent_core.knowledge import KnowledgeBase
        kb = KnowledgeBase()
        ok = kb.load()
        if not ok:
            print("  [ERROR] Failed to index documents (docs/ empty or error)")
            return False
        result = kb.search("database port config", top_k=1)
        if "(Không tìm" in result or "(Lỗi" in result or "(chưa được" in result or "(No document" in result:
            print(f"  [WARN] RAG: {result[:100]}")
        else:
            print("  [SUCCESS] RAG OK - Example search result:")
            print(f"     {result[:150]}...")
        return True
    except Exception as e:
        print(f"  [ERROR] RAG Error: {e}")
        return False

def report(results: dict):
    print("\n" + "=" * 55)
    print("  PHASE 1 SYSTEM VERIFICATION REPORT")
    print("=" * 55)
    for name, passed in results.items():
        status = "[OK]" if passed else "[FAIL]"
        print(f"  {status} {name}")
    print("=" * 55)
    if all(results.values()):
        print("  🎉 System is ready!\n")
        print("  Next steps:")
        print("  1. Add your documentation files to ./docs/")
        print("  2. Import agent_core in your scripts:")
        print("     from agent_core import MemoryManager, KnowledgeBase, ContextBuilder")
        print("  3. Run session_reset.py to checkpoint and save tokens")
    else:
        print("  [WARN] Please check the errors above to fix setup issues.")
    print("=" * 55)

if __name__ == "__main__":
    print("=" * 55)
    print("  SETUP PHASE 1: Mem0 + LlamaIndex RAG + Gemini Flash")
    print("=" * 55)

    results = {}
    if not check_env():
        results["Env config (.env)"] = False
        report(results)
        sys.exit(1)
    results["Env config (.env)"] = True

    if not check_libs():
        results["Python Libraries (requirements.txt)"] = False
        report(results)
        sys.exit(1)
    results["Python Libraries (requirements.txt)"] = True

    results["Directory structure & sample docs"] = check_dirs()
    results["Mem0 (Dynamic Memory)"] = check_memory()
    results["RAG LlamaIndex (Static Knowledge)"] = check_knowledge()

    report(results)
