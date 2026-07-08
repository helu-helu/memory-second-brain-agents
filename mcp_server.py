"""
mcp_server.py
Model Context Protocol (MCP) Server stdio bridge.
Exposes Memory (Mem0) and Knowledge (LlamaIndex RAG) as tools for AI Agents.

Run: python mcp_server.py
"""

import os
import sys
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Add project root to sys.path to ensure agent_core is importable
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

# Lazy import core managers to speed up startup
from agent_core.memory import MemoryManager
from agent_core.knowledge import KnowledgeBase

# Initialize FastMCP server
mcp = FastMCP("Memory-Second-Brain-Bridge")

# Lazy initialized managers
_memory_manager = None
_knowledge_base = None


def get_memory_manager():
    global _memory_manager
    if _memory_manager is None:
        _memory_manager = MemoryManager()
    return _memory_manager


def get_knowledge_base():
    global _knowledge_base
    if _knowledge_base is None:
        _knowledge_base = KnowledgeBase()
        _knowledge_base.load()  # Index/Load documents on startup
    return _knowledge_base


@mcp.tool()
def search_knowledge(query: str) -> str:
    """
    Search static technical documentation (like Unity 6.3 reference or project manuals) inside the RAG database.
    Use this tool when the user asks questions about Unity 6.3 APIs, physics, features, or project guidelines.
    """
    try:
        kb = get_knowledge_base()
        return kb.search(query, top_k=3)
    except Exception as e:
        return f"Error searching RAG knowledge: {e}"


@mcp.tool()
def search_memory(query: str) -> str:
    """
    Search long-term dynamic memories and user preferences from Mem0.
    Use this tool to find user's coding styles, preferred tools, database ports, or past project decisions.
    """
    try:
        mem = get_memory_manager()
        memories = mem.search(query, limit=5)
        return mem.format_for_prompt(memories)
    except Exception as e:
        return f"Error searching Mem0 memory: {e}"


@mcp.tool()
def add_memory(text: str) -> str:
    """
    Add a new fact, project configuration, or developer preference into the Mem0 long-term memory.
    Use this tool when the user shares a personal style, choice, port, or coding rule.
    """
    try:
        mem = get_memory_manager()
        success = mem.add(text)
        if success:
            return f"Successfully recorded memory: '{text}'"
        else:
            return "Failed to save memory."
    except Exception as e:
        return f"Error adding memory: {e}"


if __name__ == "__main__":
    # Start stdio server
    mcp.run()
