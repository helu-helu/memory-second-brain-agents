"""
auto_checkpoint.py
Tự động hóa 100% việc chốt phiên chat bằng AI.
Script này sẽ:
1. Đọc Git Diff để xem bạn đã sửa những gì trong code.
2. Gọi Gemini API để tự động phân tích code và tóm tắt những gì đã làm, đồng thời gợi ý việc cần làm tiếp theo.
3. Ghi trực tiếp vào file checkpoint tương ứng.

Chạy: python auto_checkpoint.py [optional_session_name]
"""

import os
import sys
import subprocess
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
    """Lấy chi tiết các thay đổi code chưa commit để gửi cho AI phân tích."""
    try:
        # Lấy diff của cả file đã add (staged) và chưa add (unstaged)
        result = subprocess.run(
            ["git", "diff", "HEAD"],
            capture_output=True, text=True
        )
        diff = result.stdout.strip()
        if not diff:
            # Nếu chưa có commit nào, lấy diff của các file untracked
            result = subprocess.run(
                ["git", "diff", "--cached"],
                capture_output=True, text=True
            )
            diff = result.stdout.strip()
        return diff[:15000]  # Giới hạn độ dài tránh quá tải token
    except Exception as e:
        return f"Error reading git diff: {e}"


def get_git_changes() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True
        )
        return [line.strip().split()[-1] for line in result.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def generate_ai_summary(diff_content: str, changes_list: list[str]) -> str:
    """Gọi Gemini API để tự động viết báo cáo checkpoint từ code thay đổi."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "Warning: GEMINI_API_KEY not found. AI summary skipped."

    client = genai.Client(api_key=api_key)
    
    prompt = f"""
    Bạn là một trợ lý AI phát triển phần mềm chuyên nghiệp.
    Hãy phân tích danh sách file thay đổi và nội dung Git Diff dưới đây của lập trình viên,
    sau đó viết một báo cáo chốt phiên (session checkpoint) bằng tiếng Việt.

    Danh sách file thay đổi: {changes_list}

    Nội dung Git Diff:
    ```diff
    {diff_content}
    ```

    Yêu cầu đầu ra chỉ trả về nội dung Markdown với cấu trúc chính xác như sau:
    ### 1. Đã hoàn thành (AI tự động tóm tắt chi tiết dựa trên code thay đổi)
    - [Tóm tắt việc 1]
    - [Tóm tắt việc 2]

    ### 2. Gợi ý bước tiếp theo
    - [Gợi ý việc cần làm tiếp theo dựa trên logic code hiện tại]
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
    print("  AI AUTO-CHECKPOINT - Tự Động Chốt Phiên Bằng AI")
    print("=" * 55)

    # 1. Xác định tên session
    session_name = sys.argv[1] if len(sys.argv) > 1 else get_git_branch()
    safe_session_name = "".join(c for c in session_name if c.isalnum() or c in ("_", "-")).lower()

    # 2. Đọc thay đổi code
    print("  -> Đang quét thay đổi từ Git...")
    diff_content = get_git_diff()
    changes_list = get_git_changes()

    if not changes_list:
        print("  [WARN] Không tìm thấy file nào thay đổi trong Git.")
        print("  -> AI sẽ tạo checkpoint trống hoặc giữ nguyên.")
        ai_summary = "### 1. Đã hoàn thành\n- Không phát hiện thay đổi code nào trong phiên này.\n\n### 2. Gợi ý bước tiếp theo\n- Bắt đầu công việc mới."
    else:
        print(f"  -> Tìm thấy {len(changes_list)} file thay đổi. Đang gọi Gemini AI phân tích...")
        ai_summary = generate_ai_summary(diff_content, changes_list)

    # 3. Ghi file checkpoint
    os.makedirs("./scratch", exist_ok=True)
    checkpoint_path = f"./scratch/session_checkpoint_{safe_session_name}.md"

    checkpoint_content = f"""# Session Checkpoint [{session_name}] — {datetime.now().strftime('%Y-%m-%d %H:%M')}

> AI tự động tạo báo cáo này dựa trên thay đổi code trong Git.

## 📂 Các file đã chỉnh sửa trong session này (Git)
"""
    if changes_list:
        checkpoint_content += "\n".join(f"- `{f}`" for f in changes_list) + "\n\n"
    else:
        checkpoint_content += "- Không phát hiện thay đổi.\n\n"

    checkpoint_content += "## 📝 Nội dung phân tích từ AI\n"
    checkpoint_content += ai_summary

    checkpoint_content += f"""

---
## Câu lệnh mở đầu cho phiên chat mới:
```
Hãy đọc file `./scratch/session_checkpoint_{safe_session_name}.md` để nắm bắt
bối cảnh hiện tại của session '{session_name}' và tiếp tục công việc.
Không cần đọc lại lịch sử chat cũ.
```
"""

    with open(checkpoint_path, "w", encoding="utf-8") as f:
        f.write(checkpoint_content)

    print(f"\n[THÀNH CÔNG] Đã tạo checkpoint tự động tại: {checkpoint_path}")
    print("=" * 55)
    print(f"Hãy đọc file `./scratch/session_checkpoint_{safe_session_name}.md` để nắm bắt bối cảnh hiện tại của session '{session_name}' và tiếp tục công việc.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
