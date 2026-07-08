"""
api_server.py
FastAPI Centralized Bridge for Memory (Mem0) and Knowledge (LlamaIndex RAG).
Acts as a unified backend for lightweight Agents (like Hermes) to avoid heavy local dependencies.

Run: uvicorn api_server:app --host 127.0.0.1 --port 8000
"""

import os
import sys
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# Add project root to sys.path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.memory import MemoryManager
from agent_core.knowledge import KnowledgeBase

app = FastAPI(
    title="Memory and Second Brain API",
    description="Centralized Bridge for Multi-Agent Orchestration",
    version="1.0.0"
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

class MemoryAddRequest(BaseModel):
    text: str

@app.get("/rag/search")
async def rag_search(q: str):
    """Search static RAG documents."""
    try:
        kb = get_knowledge()
        result = kb.search(q, top_k=3)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/memory/search")
async def memory_search(q: str):
    """Search dynamic long-term memories."""
    try:
        mem = get_memory()
        memories = mem.search(q, limit=5)
        formatted = mem.format_for_prompt(memories)
        return {"result": formatted}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/memory/add")
async def memory_add(req: MemoryAddRequest):
    """Add a new dynamic memory."""
    try:
        mem = get_memory()
        success = mem.add(req.text)
        return {"success": success}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="127.0.0.1", port=8000, reload=True)
