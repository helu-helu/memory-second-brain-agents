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
API_KEY = os.environ["APP_API_KEY"]
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
        workflows_dir = os.path.join(project_root, "docs", "Workflows")
        os.makedirs(workflows_dir, exist_ok=True)
        
        # Sanitize title for filename
        filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', title).lower() + ".md"
        filepath = os.path.join(workflows_dir, filename)
        
        # Parse features
        features_list = [f.strip() for f in requires_features.split(",")]
        features_yaml = "\n  - ".join(features_list)
        if features_yaml:
            features_yaml = f"\n  - {features_yaml}"
            
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        markdown_content = f"""---
title: "{title}"
status: "Verified"
date: "{date_str}"
success_rate: "{success_rate}"
task_id: "{task_id}"
tags: ["Workflows"]
requires:
  tier: "{requires_tier}"
  features:{features_yaml}
---

# {title}

{content}
"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        return f"Successfully saved verified workflow to {filepath}. Auto-sync will index it shortly."
    except Exception as e:
        return f"Error saving workflow: {e}"

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
        workflows_dir = os.path.join(project_root, "docs", "Workflows")
        filepath = os.path.join(workflows_dir, filename)
        
        if not os.path.exists(filepath):
            return f"Error: Workflow file {filename} not found in {workflows_dir}"
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Thay thế status
        if 'status: "Verified"' in content:
            content = content.replace('status: "Verified"', f'status: "Deprecated"\ndeprecation_reason: "{reason}"')
        else:
            return "Could not find 'status: \"Verified\"' in the file."
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
        return f"Successfully deprecated workflow {filename}. RAG will ignore it next sync."
    except Exception as e:
        return f"Error deprecating workflow: {e}"

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
        script_path = os.path.join(project_root, "scripts", "convert_html_to_md.py")
        target_dir = os.path.join(project_root, "docs", "daily")
        result = subprocess.run([sys.executable, script_path, source_dir, target_dir], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Conversion Failed:\n{result.stderr}"
    except Exception as e:
        return f"Error running convert_html_to_md.py: {e}"

@mcp.tool()
def build_massive_index(target_dir: str) -> str:
    """
    Kích hoạt Advanced Semantic Chunking và Local Embedding để ép hàng ngàn file vào Qdrant RAG mà không bị OOM (Hết RAM).
    Nên gọi tool này sau khi đã convert tài liệu sang định dạng Markdown.
    
    Args:
        target_dir: Đường dẫn tuyệt đối đến thư mục chứa Markdown (thường là "<project_root>/docs/daily" hoặc source_dir)
    """
    try:
        script_path = os.path.join(project_root, "scripts", "build_massive_index.py")
        result = subprocess.run([sys.executable, script_path, target_dir], capture_output=True, text=True)
        return result.stdout if result.returncode == 0 else f"Indexing Failed:\n{result.stderr}"
    except Exception as e:
        return f"Error running build_massive_index.py: {e}"

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
    mcp.run()
