"""
auto_checkpoint.py
AI-driven automatic session checkpoint tool.
This script will:
1. Read Git Diff to inspect modified code files in the workspace.
2. Call Gemini API to automatically analyze changes, summarize work, and suggest next steps.
3. Write the checkpoint report directly to ./scratch/session_checkpoint_<name>.md.

Run: python auto_checkpoint.py [optional_session_name]
"""

import os
import sys
import subprocess
from datetime import datetime
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_git_branch() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True
        )
        return result.stdout.strip().replace("/", "_").replace("-", "_")
    except Exception:
        return "default"


def get_git_diff() -> str:
    """Read git diff for AI analysis."""
    try:
        result = subprocess.run(
            ["git", "diff", "HEAD"],
            capture_output=True, text=True, errors="ignore"
        )
        diff = result.stdout.strip()
        if not diff:
            result = subprocess.run(
                ["git", "diff", "--cached"],
                capture_output=True, text=True, errors="ignore"
            )
            diff = result.stdout.strip()
        return diff[:15000]
    except Exception as e:
        return f"Error reading git diff: {e}"


def get_git_changes() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, errors="ignore"
        )
        return [line.strip().split()[-1] for line in result.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def generate_ai_summary(diff_content: str, changes_list: list[str]) -> str:
    """Call Gemini API to summarize changes from git diff."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Warning: GEMINI_API_KEY not found. AI summary skipped."

    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    You are a professional software engineering AI assistant.
    Analyze the list of modified files and the Git Diff below from the developer,
    then write a checkpoint report in Vietnamese summarizing what was accomplished and suggesting next steps.

    Modified files: {changes_list}

    Git Diff:
    ```diff
    {diff_content}
    ```

    Format your output strictly using these headers (do not add extra greeting or text):
    ### 1. Đã hoàn thành (Accomplished tasks)
    - [Task 1 summarized from changes]
    - [Task 2 summarized from changes]

    ### 2. Gợi ý bước tiếp theo (Suggested next steps)
    - [Next task based on current code status]
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Warning: Failed to call Gemini API: {e}\n(Please write summary manually)"


def main():
    print("=" * 55)
    print("  AI AUTO-CHECKPOINT - Creating Checkpoint using AI")
    print("=" * 55)

    # 1. Determine session name
    session_name = sys.argv[1] if len(sys.argv) > 1 else get_git_branch()
    safe_session_name = "".join(c for c in session_name if c.isalnum() or c in ("_", "-")).lower()

    # 2. Analyze code changes
    print("  -> Scanning Git changes...")
    diff_content = get_git_diff()
    changes_list = get_git_changes()

    if not changes_list:
        print("  [WARN] No modified files detected in Git.")
        ai_summary = "### 1. Đã hoàn thành\n- Không phát hiện thay đổi code nào trong phiên này.\n\n### 2. Gợi ý bước tiếp theo\n- Bắt đầu công việc mới."
    else:
        print(f"  -> Found {len(changes_list)} modified files. Calling Gemini AI...")
        ai_summary = generate_ai_summary(diff_content, changes_list)

    # 3. Write checkpoint file
    os.makedirs("./scratch", exist_ok=True)
    checkpoint_path = f"./scratch/session_checkpoint_{safe_session_name}.md"

    checkpoint_content = f"""# Session Checkpoint [{session_name}] — {datetime.now().strftime('%Y-%m-%d %H:%M')}

> AI automatically generated this checkpoint based on git diff.

## 🛠️ Kiến Trúc Dự Án & Xác Minh (Project Stack & Verification)
- **AI Models:** Gemini 2.5 Flash (Trích xuất Mem0) + Gemini Embedding 2 (Vector)
- **Cơ sở dữ liệu:** Qdrant local (`./db/qdrant_mem0`) + SQLite (`./db/mem0_history.db`)
- **Tài liệu RAG:** Nạp từ thư mục `./docs/` (chứa tài liệu Unity 6.3)
- **Lệnh xác minh hệ thống:** `python setup_phase1.py` (chạy bằng Python 3.13)

## 📂 Các file đã chỉnh sửa trong session này (Git)
"""
    if changes_list:
        checkpoint_content += "\n".join(f"- `{f}`" for f in changes_list) + "\n\n"
    else:
        checkpoint_content += "- No changes detected.\n\n"

    checkpoint_content += "## 📝 AI Analysis\n"
    checkpoint_content += ai_summary

    checkpoint_content += f"""

---
## Opening command for the new session:
```
Hãy đọc file `./scratch/session_checkpoint_{safe_session_name}.md` để nắm bắt
bối cảnh hiện tại của session '{session_name}' và tiếp tục công việc.
Không cần đọc lại lịch sử chat cũ.
```
"""

    with open(checkpoint_path, "w", encoding="utf-8") as f:
        f.write(checkpoint_content)

    print(f"\n[SUCCESS] Checkpoint saved successfully for '{session_name}' at: {checkpoint_path}")
    print("=" * 55)
    print("Please copy the command below and paste it in your new session chat window:")
    print(f"Please read the file `./scratch/session_checkpoint_{safe_session_name}.md` to capture context and continue.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
