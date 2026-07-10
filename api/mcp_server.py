"""
mcp_server.py
Model Context Protocol (MCP) Server stdio bridge (Thin-Client).
Acts as a lightweight proxy, sending HTTP requests to api_server.py.
Requires zero heavy ML dependencies (no LlamaIndex, no Mem0, no QdrantClient).

Run: python mcp_server.py
"""

import os
import sys
import subprocess
import time
import requests
import requests
from mcp.server.fastmcp import FastMCP

# Add project root to sys.path to import agent_core
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.config import config

API_BASE = config["app"]["api_server"]["base_url"]
API_KEY = os.environ["APP_API_KEY"]
HEADERS = {config["app"]["api_key_name"]: API_KEY}

api_session = requests.Session()
api_session.headers.update(HEADERS)

# Initialize FastMCP server
mcp = FastMCP("Memory-Second-Brain-Bridge-Thin")

@mcp.tool()
def search_knowledge(query: str, tags: list[str] = None) -> str:
    """
    Search static technical documentation (like Unity 6.3 reference or project manuals) inside the RAG database.
    Use this tool when the user asks questions about Unity 6.3 APIs, physics, features, or project guidelines.
    Optionally pass 'tags' (e.g. ["Unity", "6.3"]) to filter metadata based on directory structure.
    """
    try:
        params = {"q": query}
        if tags:
            params["tags"] = tags
        resp = api_session.get(f"{API_BASE}/rag/search", params=params)
        if resp.status_code == 200:
            return resp.json().get("result", "No result")
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error searching RAG knowledge (Is API Server running?): {e}"

@mcp.tool()
def search_memory(query: str) -> str:
    """
    Search long-term dynamic memories and user preferences from Mem0.
    Use this tool to find user's coding styles, preferred tools, database ports, or past project decisions.
    """
    try:
        resp = api_session.get(f"{API_BASE}/memory/search", params={"q": query})
        if resp.status_code == 200:
            return resp.json().get("result", "No memories found")
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error searching Mem0 memory (Is API Server running?): {e}"

@mcp.tool()
def add_memory(text: str) -> str:
    """
    Add a new fact, project configuration, or developer preference into the Mem0 long-term memory.
    Use this tool when the user shares a personal style, choice, port, or coding rule.
    """
    try:
        resp = api_session.post(f"{API_BASE}/memory/add", json={"text": text})
        if resp.status_code == 200:
            success = resp.json().get("success", False)
            if success:
                return f"Successfully recorded memory: '{text}'"
            return "Failed to save memory on server."
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error adding memory (Is API Server running?): {e}"


def ensure_api_running():
    try:
        resp = requests.get(f"{API_BASE}/ping", timeout=2)
        if resp.status_code == 200:
            return
    except requests.exceptions.RequestException:
        pass
    
    # Not running, start it
    api_script = os.path.join(project_root, "api", "api_server.py")
    # Start process in background
    subprocess.Popen([sys.executable, api_script], cwd=project_root)
    # Wait briefly for it to start
    time.sleep(3)


if __name__ == "__main__":
    ensure_api_running()
    # Start stdio server
    mcp.run()
