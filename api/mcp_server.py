"""
mcp_server.py
Model Context Protocol (MCP) Server stdio bridge (Thin-Client).
Acts as a lightweight proxy, sending HTTP requests to api_server.py.
Requires zero heavy ML dependencies (no LlamaIndex, no Mem0, no QdrantClient).

Run: python mcp_server.py
"""

import os
import requests
import yaml
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(project_root, "config.yaml")
with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

API_BASE = config["app"]["api_server"]["base_url"]
API_KEY = os.getenv("APP_API_KEY", "my-super-secret-key-123")
HEADERS = {config["app"]["api_key_name"]: API_KEY}

# Initialize FastMCP server
mcp = FastMCP("Memory-Second-Brain-Bridge-Thin")

@mcp.tool()
def search_knowledge(query: str) -> str:
    """
    Search static technical documentation (like Unity 6.3 reference or project manuals) inside the RAG database.
    Use this tool when the user asks questions about Unity 6.3 APIs, physics, features, or project guidelines.
    """
    try:
        resp = requests.get(f"{API_BASE}/rag/search", params={"q": query}, headers=HEADERS)
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
        resp = requests.get(f"{API_BASE}/memory/search", params={"q": query}, headers=HEADERS)
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
        resp = requests.post(f"{API_BASE}/memory/add", json={"text": text}, headers=HEADERS)
        if resp.status_code == 200:
            success = resp.json().get("success", False)
            if success:
                return f"Successfully recorded memory: '{text}'"
            return "Failed to save memory on server."
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error adding memory (Is API Server running?): {e}"


if __name__ == "__main__":
    # Start stdio server
    mcp.run()
