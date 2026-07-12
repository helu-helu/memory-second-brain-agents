"""
second_brain_mcp.py
Model Context Protocol (MCP) Server stdio bridge (Thin-Client).
Acts as a lightweight proxy, sending HTTP requests to api_server.py.
Requires zero heavy ML dependencies (no LlamaIndex, no Mem0, no QdrantClient).

Run: python second_brain_mcp.py
"""

import os
import sys
import subprocess
import time
import requests
import re
from datetime import datetime
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# Add project root to sys.path to import agent_core
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

from agent_core.config import config

API_BASE = config["app"]["api_server"]["base_url"]
API_KEY = os.environ.get("APP_API_KEY", "my-super-secret-key-123")
HEADERS = {config["app"]["api_key_name"]: API_KEY}

api_session = requests.Session()
api_session.headers.update(HEADERS)

# Initialize FastMCP server
mcp = FastMCP("Second-Brain-MCP")

@mcp.tool()
def search_knowledge(query: str, tags: list[str] = None) -> str:
    """
    Search static technical documentation (like Unity 6.3 reference or project manuals) inside the RAG database.
    Use this tool when the user asks questions about APIs, physics, features, or project guidelines.
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

USER_ID = os.environ.get("MEM0_USER_ID")

@mcp.tool()
def search_memory(query: str) -> str:
    """
    Search long-term dynamic memories and user preferences from Mem0.
    Use this tool to find user's coding styles, preferred tools, database ports, or past project decisions.
    """
    try:
        params = {"q": query}
        if USER_ID:
            params["user_id"] = USER_ID
        resp = api_session.get(f"{API_BASE}/memory/search", params=params)
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
        payload = {"text": text}
        if USER_ID:
            payload["user_id"] = USER_ID
        resp = api_session.post(f"{API_BASE}/memory/add", json=payload)
        if resp.status_code == 200:
            success = resp.json().get("success", False)
            if success:
                return f"Successfully recorded memory: '{text}'"
            return "Failed to save memory on server."
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error adding memory (Is API Server running?): {e}"

@mcp.tool()
def save_verified_workflow(title: str, content: str, requires_tier: str = "standard", requires_features: str = "tool_calling", success_rate: str = "100%", task_id: str = "N/A") -> str:
    """
    Lưu trữ một Workflow hoặc Kinh nghiệm đã được xác minh (Verified) sau khi Agent/Người dùng hoàn thành một task khó.
    Tạo file Markdown tại thư mục docs/Workflows/ với YAML Frontmatter chứa metadata Capability (requires).
    Auto-sync watchdog sẽ tự động đưa file này vào Qdrant RAG.
    
    Args:
        title: Tiêu đề ngắn gọn (ví dụ: "setup_fastapi_docker", "fix_cors_error")
        content: Nội dung chi tiết của workflow, các bước giải quyết, code mẫu
        requires_tier: Cấp độ model yêu cầu (nano, standard, reasoning, frontier)
        requires_features: Các tính năng yêu cầu cách nhau bằng dấu phẩy (vd: "tool_calling,structured_output")
        success_rate: Tỷ lệ thành công hoặc điểm tin cậy (mặc định "100%")
        task_id: ID của task hoặc mô tả ngắn gọn về context
    """
    try:
        payload = {
            "title": title,
            "content": content,
            "requires_tier": requires_tier,
            "requires_features": requires_features,
            "success_rate": success_rate,
            "task_id": task_id
        }
        resp = api_session.post(f"{API_BASE}/admin/save_workflow", json=payload)
        if resp.status_code == 200:
            return resp.json().get("message", "Success")
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error saving workflow (Is API Server running?): {e}"

@mcp.tool()
def deprecate_workflow(filename: str, reason: str) -> str:
    """
    Đánh dấu một Workflow là lỗi thời (Deprecated) nếu nó không còn hoạt động tốt hoặc bị sai lệch chất lượng.
    Thay đổi status trong YAML Frontmatter thành 'Deprecated'.
    
    Args:
        filename: Tên file workflow (ví dụ: "setup_fastapi_docker.md")
        reason: Lý do tại sao bị lỗi thời
    """
    try:
        resp = api_session.post(f"{API_BASE}/admin/deprecate_workflow", json={"filename": filename, "reason": reason})
        if resp.status_code == 200:
            return resp.json().get("message", "Success")
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error deprecating workflow (Is API Server running?): {e}"

@mcp.tool()
def search_workflows(query: str) -> str:
    """
    Tìm kiếm các Workflow và Kinh nghiệm đã được xác minh (Verified) trong Second Brain.
    Nên gọi tool này khi bắt đầu một task mới để xem có kinh nghiệm nào từ trước không.
    """
    try:
        # Tương tự search_knowledge nhưng ép tag "Workflows"
        params = {"q": query, "tags": ["Workflows"]}
        resp = api_session.get(f"{API_BASE}/rag/search", params=params)
        if resp.status_code == 200:
            return resp.json().get("result", "No result")
        return f"API Error: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error searching workflows (Is API Server running?): {e}"

@mcp.tool()
def convert_docs_to_md(source_dir: str) -> str:
    """
    Tự động parse thư mục chứa tài liệu HTML/Web (ví dụ: offline documentation) thành Markdown sạch để nạp vào RAG.
    
    Args:
        source_dir: Đường dẫn tuyệt đối đến thư mục chứa tài liệu gốc (vd: "D:/UnityDocs")
    """
    try:
        resp = api_session.post(f"{API_BASE}/admin/convert_docs", json={"source_dir": source_dir})
        if resp.status_code == 200:
            return resp.json().get("output", "Success")
        return f"Conversion Failed: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error running convert_docs (Is API Server running?): {e}"

@mcp.tool()
def build_massive_index(target_dir: str) -> str:
    """
    Kích hoạt Advanced Semantic Chunking và Local Embedding để ép hàng ngàn file vào Qdrant RAG mà không bị OOM (Hết RAM).
    Nên gọi tool này sau khi đã convert tài liệu sang định dạng Markdown.
    
    Args:
        target_dir: Đường dẫn tuyệt đối đến thư mục chứa Markdown (thường là "<project_root>/docs/daily" hoặc source_dir)
    """
    try:
        resp = api_session.post(f"{API_BASE}/admin/build_index", json={"target_dir": target_dir})
        if resp.status_code == 200:
            return resp.json().get("output", "Success")
        return f"Indexing Failed: {resp.status_code} - {resp.text}"
    except Exception as e:
        return f"Error running build_index (Is API Server running?): {e}"

@mcp.tool()
def open_dashboard() -> str:
    """
    Mở giao diện Web Dashboard của Second Brain để người dùng tương tác trực quan.
    Hãy gọi tool này khi người dùng yêu cầu "mở dashboard", "xem giao diện", hoặc muốn trực quan hóa dữ liệu RAG/Memory.
    """
    try:
        resp = api_session.post(f"{API_BASE}/admin/open_dashboard")
        if resp.status_code == 200:
            return "Dashboard is launching. Please tell the user to check their browser or taskbar."
        return f"Failed to open Dashboard: {resp.text}"
    except Exception as e:
        return f"Error opening dashboard (Is API Server running?): {e}"

def ensure_api_running():
    import socket
    def is_port_in_use(port: int) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('127.0.0.1', port)) == 0
            
    if is_port_in_use(8001):
        return
        
    # Not running, start it
    api_script = os.path.join(project_root, "api", "api_server.py")
    # Start process in background
    subprocess.Popen([sys.executable, api_script], cwd=project_root)
    # Wait briefly for it to start
    for _ in range(10):
        if is_port_in_use(8001):
            break
        time.sleep(1)

if __name__ == "__main__":
    ensure_api_running()
    mcp.run()
