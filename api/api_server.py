"""
api_server.py
FastAPI Centralized Bridge for Memory (Mem0) and Knowledge (LlamaIndex RAG).
Acts as a unified backend for lightweight Agents (like Hermes) to avoid heavy local dependencies.

Run: uvicorn api_server:app --host 127.0.0.1 --port 8000
"""

import os
import sys
import threading
import time
import yaml
import secrets
from fastapi import FastAPI, HTTPException, Security, Depends, Query
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

load_dotenv()

# Add project root to sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.memory import MemoryManager
from agent_core.knowledge import KnowledgeBase
from agent_core.config import config, DOCS_DIR

API_KEY = os.environ["APP_API_KEY"]
API_KEY_NAME = config["app"]["api_key_name"]
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header and secrets.compare_digest(api_key_header, API_KEY):
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate API Key")

app = FastAPI(
    title="Memory and Second Brain API",
    description="Centralized Bridge for Multi-Agent Orchestration with Security & Auto-Sync",
    version="2.0.0"
)

# Lazy initialization
_memory_manager = None
_knowledge_base = None

def get_memory():
    global _memory_manager
    if _memory_manager is None:
        _memory_manager = MemoryManager()
    return _memory_manager

def get_knowledge():
    global _knowledge_base
    if _knowledge_base is None:
        _knowledge_base = KnowledgeBase()
        _knowledge_base.load()
    return _knowledge_base

_reload_timer = None

def _trigger_reload():
    print("[Watchdog] Debounce finished. Reloading RAG KnowledgeBase...")
    kb = get_knowledge()
    kb.reload()

class DocsChangeHandler(FileSystemEventHandler):
    """Watchdog event handler for docs/ directory"""
    def on_any_event(self, event):
        # Ignore hidden files or directories
        if event.is_directory or os.path.basename(event.src_path).startswith('.'):
            return
        
        # Debounce the rebuild
        global _reload_timer
        if _reload_timer is not None:
            _reload_timer.cancel()
        _reload_timer = threading.Timer(5.0, _trigger_reload)
        _reload_timer.start()

def start_watchdog():
    """Starts the directory observer in a background thread"""
    observer = Observer()
    docs_dir = DOCS_DIR
    os.makedirs(docs_dir, exist_ok=True)
    observer.schedule(DocsChangeHandler(), docs_dir, recursive=True)
    observer.start()
    print(f"[Watchdog] Started monitoring {docs_dir} for Auto-Sync.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

@app.on_event("startup")
async def startup_event():
    # Pre-load knowledge base and start auto-sync watchdog
    get_knowledge()
    watchdog_thread = threading.Thread(target=start_watchdog, daemon=True)
    watchdog_thread.start()

@app.get("/ping")
async def ping():
    return {"status": "ok"}

class MemoryAddRequest(BaseModel):
    text: str

@app.get("/rag/search")
def rag_search(q: str, tags: list[str] = Query(None), api_key: str = Depends(get_api_key)):
    """Search static RAG documents."""
    try:
        kb = get_knowledge()
        result = kb.search(q, top_k=3, tags=tags)
        return {"result": result}
    except Exception as e:
        print(f"[Error] /rag/search: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/search")
def memory_search(q: str, api_key: str = Depends(get_api_key)):
    """Search dynamic long-term memories."""
    try:
        mem = get_memory()
        memories = mem.search(q, limit=5)
        formatted = mem.format_for_prompt(memories)
        return {"result": formatted}
    except Exception as e:
        print(f"[Error] /memory/search: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/add")
def memory_add(req: MemoryAddRequest, api_key: str = Depends(get_api_key)):
    """Add a new dynamic memory."""
    try:
        mem = get_memory()
        success = mem.add(req.text)
        return {"success": success}
    except Exception as e:
        print(f"[Error] /memory/add: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/context/build")
async def context_build(q: str, api_key: str = Depends(get_api_key)):
    """Build system prompt in parallel using Asyncio."""
    try:
        from agent_core.context_builder import ContextBuilder
        mem = get_memory()
        kb = get_knowledge()
        ctx_builder = ContextBuilder(memory=mem, knowledge=kb)
        
        # Gọi song song để giảm nửa thời gian chờ
        prompt = await ctx_builder.build_async(q)
        return {"prompt": prompt}
    except Exception as e:
        print(f"[Error] /context/build: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host=config["app"]["api_server"]["host"], port=config["app"]["api_server"]["port"], reload=False)
