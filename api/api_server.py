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
from contextlib import asynccontextmanager
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
from agent_core.config import config, DOCS_DIR, SKILLS_DIR, MODEL_REGISTRY
from agent_core.access_tools import build_active_memory_pack, build_agent_bootstrap, build_docs_context_pack, inspect_corpus_status, inspect_second_brain_status, list_corpora, record_agent_handoff, route_docs_query

API_KEY = os.environ.get("APP_API_KEY", "my-super-secret-key-123")
API_KEY_NAME = config["app"]["api_key_name"]
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header and secrets.compare_digest(api_key_header, API_KEY):
        return api_key_header
    raise HTTPException(status_code=403, detail="Could not validate API Key")

# Lazy initialization
_memory_managers = {}
_knowledge_base = None

def get_memory(user_id: str = None):
    target_user = user_id or os.getenv("MEM0_USER_ID", "personal_user")
    if target_user not in _memory_managers:
        _memory_managers[target_user] = MemoryManager(user_id=target_user)
    return _memory_managers[target_user]

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
    def __init__(self):
        super().__init__()
        self._debounce_timers = {}
        
    def _do_insert(self, path):
        try:
            kb = get_knowledge()
            if hasattr(kb, "insert_file"):
                kb.insert_file(path)
            else:
                # Fallback if insert_file is not available
                global _reload_timer
                if _reload_timer is not None:
                    _reload_timer.cancel()
                _reload_timer = threading.Timer(5.0, _trigger_reload)
                _reload_timer.start()
        except Exception as e:
            print(f"[Watchdog] Error inserting {path}: {e}")

    def on_any_event(self, event):
        # Ignore hidden files or directories
        if event.is_directory or os.path.basename(event.src_path).startswith('.'):
            return
            
        # Ignore non-text files
        if not event.src_path.lower().endswith(('.md', '.html', '.txt', '.json', '.pdf')):
            return
        
        # Apply Phase 2: Incremental RAG Sync with Debounce
        path = event.src_path
        if path in self._debounce_timers:
            self._debounce_timers[path].cancel()
            
        timer = threading.Timer(2.0, self._do_insert, args=[path])
        self._debounce_timers[path] = timer
        timer.start()

def start_watchdog():
    """Starts the directory observer in a background thread"""
    observer = Observer()
    handler = DocsChangeHandler()
    
    for watch_dir in [DOCS_DIR, SKILLS_DIR]:
        os.makedirs(watch_dir, exist_ok=True)
        observer.schedule(handler, watch_dir, recursive=True)
        print(f"[Watchdog] Started monitoring {watch_dir} for Auto-Sync.")
        
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Pre-load knowledge base unless a thin MCP client wants fast file-first startup.
    if os.getenv("SECOND_BRAIN_PRELOAD_KB", "1") != "0":
        get_knowledge()
    watchdog_thread = threading.Thread(target=start_watchdog, daemon=True)
    watchdog_thread.start()
    yield


app = FastAPI(
    title="Memory and Second Brain API",
    description="Centralized Bridge for Multi-Agent Orchestration with Security & Auto-Sync",
    version="2.0.0",
    lifespan=lifespan,
)

@app.get("/ping")
async def ping():
    return {"status": "ok"}

class MemoryAddRequest(BaseModel):
    text: str
    user_id: Optional[str] = None

class ContextPackRequest(BaseModel):
    query: str
    limit: int = 12
    mode: str = "lexical"
    out: Optional[str] = None

class MemoryPackRequest(BaseModel):
    query: str
    limit: int = 5
    out: Optional[str] = None

class BootstrapRequest(BaseModel):
    query: str
    memory_limit: int = 5
    out: Optional[str] = None

class HandoffRequest(BaseModel):
    title: str
    summary: str
    status: str = "completed"
    agent: str = "codex"
    files: List[str] = []
    decisions: List[str] = []
    followups: List[str] = []

@app.get("/rag/search")
def rag_search(q: str, tags: list[str] = Query(None), requires_tier: str = None, requires_features: list[str] = Query(None), api_key: str = Depends(get_api_key)):
    """Search static RAG documents."""
    try:
        kb = get_knowledge()
        requires = {}
        if requires_tier:
            requires["tier"] = requires_tier
        if requires_features:
            requires["features"] = requires_features
            
        result = kb.search(q, top_k=3, tags=tags, requires=requires if requires else None)
        return {"result": result}
    except Exception as e:
        print(f"[Error] /rag/search: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/search")
def memory_search(q: str, user_id: Optional[str] = None, api_key: str = Depends(get_api_key)):
    """Search dynamic long-term memories."""
    try:
        mem = get_memory(user_id)
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
        mem = get_memory(req.user_id)
        success = mem.add(req.text)
        return {"success": success}
    except Exception as e:
        print(f"[Error] /memory/add: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/all")
def memory_all(user_id: Optional[str] = None, api_key: str = Depends(get_api_key)):
    """Get all dynamic memories for a user."""
    try:
        mem = get_memory(user_id)
        memories = mem.get_all()
        return {"memories": memories}
    except Exception as e:
        print(f"[Error] /memory/all: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/context/build")
async def context_build(q: str, user_id: Optional[str] = None, model_id: str = None, api_key: str = Depends(get_api_key)):
    """Build system prompt in parallel using Asyncio."""
    try:
        from agent_core.context_builder import ContextBuilder
        mem = get_memory(user_id)
        kb = get_knowledge()
        ctx_builder = ContextBuilder(memory=mem, knowledge=kb)
        
        # Capability-Based Routing mapping
        requires = None
        if model_id and "available_models" in MODEL_REGISTRY:
            for model_info in MODEL_REGISTRY["available_models"]:
                if model_info.get("id") == model_id:
                    requires = {
                        "tier": model_info.get("tier"),
                        "features": model_info.get("features", [])
                    }
                    print(f"[Router] Mapped model {model_id} to capabilities: {requires}")
                    break
        
        # Gọi song song để giảm nửa thời gian chờ
        prompt = await ctx_builder.build_async(q, requires=requires)
        return {"prompt": prompt}
    except Exception as e:
        print(f"[Error] /context/build: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/second-brain/corpora")
def second_brain_list_corpora(status: Optional[str] = None, product: Optional[str] = None, api_key: str = Depends(get_api_key)):
    result = list_corpora(status=status, product=product)
    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.get("/second-brain/route")
def second_brain_route_query(q: str, api_key: str = Depends(get_api_key)):
    result = route_docs_query(q)
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/second-brain/context-pack")
def second_brain_context_pack(req: ContextPackRequest, api_key: str = Depends(get_api_key)):
    result = build_docs_context_pack(req.query, limit=req.limit, mode=req.mode, out=req.out)
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.get("/second-brain/corpora/{corpus_id}/status")
def second_brain_corpus_status(corpus_id: str, api_key: str = Depends(get_api_key)):
    result = inspect_corpus_status(corpus_id)
    if not result["ok"]:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@app.post("/second-brain/memory-pack")
def second_brain_memory_pack(req: MemoryPackRequest, api_key: str = Depends(get_api_key)):
    result = build_active_memory_pack(req.query, limit=req.limit, out=req.out)
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.get("/second-brain/status")
def second_brain_status(api_key: str = Depends(get_api_key)):
    result = inspect_second_brain_status()
    if not result["ok"]:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@app.post("/second-brain/bootstrap")
def second_brain_bootstrap(req: BootstrapRequest, api_key: str = Depends(get_api_key)):
    result = build_agent_bootstrap(req.query, memory_limit=req.memory_limit, out=req.out)
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

@app.post("/second-brain/handoff")
def second_brain_handoff(req: HandoffRequest, api_key: str = Depends(get_api_key)):
    result = record_agent_handoff(
        req.title,
        req.summary,
        status=req.status,
        agent=req.agent,
        files=req.files,
        decisions=req.decisions,
        followups=req.followups,
    )
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["error"])
    return result

# --- Admin & MCP Tools Endpoints ---
import subprocess
import re
from datetime import datetime

class WorkflowRequest(BaseModel):
    title: str
    content: str
    requires_tier: str = "standard"
    requires_features: str = "tool_calling"
    success_rate: str = "100%"
    task_id: str = "N/A"

@app.post("/admin/save_workflow")
def admin_save_workflow(req: WorkflowRequest, api_key: str = Depends(get_api_key)):
    try:
        workflows_dir = os.path.join(project_root, "docs", "Workflows")
        os.makedirs(workflows_dir, exist_ok=True)
        filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', req.title).lower() + ".md"
        filepath = os.path.join(workflows_dir, filename)
        features_list = [f.strip() for f in req.requires_features.split(",")]
        features_yaml = "\n  - ".join(features_list)
        if features_yaml:
            features_yaml = f"\n  - {features_yaml}"
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        markdown_content = f"""---
title: "{req.title}"
status: "Verified"
date: "{date_str}"
success_rate: "{req.success_rate}"
task_id: "{req.task_id}"
tags: ["Workflows"]
requires:
  tier: "{req.requires_tier}"
  features:{features_yaml}
---

# {req.title}

{req.content}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        return {"success": True, "message": f"Saved to {filepath}"}
    except Exception as e:
        print(f"[Error] /admin/save_workflow: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class DeprecateRequest(BaseModel):
    filename: str
    reason: str

@app.post("/admin/deprecate_workflow")
def admin_deprecate_workflow(req: DeprecateRequest, api_key: str = Depends(get_api_key)):
    try:
        workflows_dir = os.path.join(project_root, "docs", "Workflows")
        filepath = os.path.join(workflows_dir, req.filename)
        if not os.path.exists(filepath):
            raise HTTPException(status_code=404, detail="File not found")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        if 'status: "Verified"' in content:
            content = content.replace('status: "Verified"', f'status: "Deprecated"\ndeprecation_reason: "{req.reason}"')
        else:
            raise HTTPException(status_code=400, detail="Not a verified workflow")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return {"success": True, "message": f"Deprecated {req.filename}"}
    except Exception as e:
        print(f"[Error] /admin/deprecate_workflow: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class ConvertDocsRequest(BaseModel):
    source_dir: str

@app.post("/admin/convert_docs")
def admin_convert_docs(req: ConvertDocsRequest, api_key: str = Depends(get_api_key)):
    try:
        script_path = os.path.join(project_root, "scripts", "convert_html_to_md.py")
        target_dir = os.path.join(project_root, "docs", "daily")
        result = subprocess.run([sys.executable, script_path, req.source_dir, target_dir], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return {"success": True, "output": result.stdout}
    except Exception as e:
        print(f"[Error] /admin/convert_docs: {e}")
        raise HTTPException(status_code=500, detail=str(e))

class BuildIndexRequest(BaseModel):
    target_dir: str

@app.post("/admin/build_index")
def admin_build_index(req: BuildIndexRequest, api_key: str = Depends(get_api_key)):
    try:
        script_path = os.path.join(project_root, "scripts", "build_massive_index.py")
        result = subprocess.run([sys.executable, script_path, req.target_dir], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)
        return {"success": True, "output": result.stdout}
    except Exception as e:
        print(f"[Error] /admin/build_index: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/admin/open_dashboard")
def admin_open_dashboard(api_key: str = Depends(get_api_key)):
    try:
        dash_path = os.path.join(project_root, "dashboard.py")
        subprocess.Popen(["streamlit", "run", dash_path], cwd=project_root)
        return {"success": True, "message": "Dashboard opened"}
    except Exception as e:
        print(f"[Error] /admin/open_dashboard: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host=config["app"]["api_server"]["host"], port=config["app"]["api_server"]["port"], reload=False)
