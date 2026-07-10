"""
session_reset.py
Công cụ chốt phiên chat để tiết kiệm token.
Hỗ trợ quản lý nhiều session song song bằng tên gợi nhớ hoặc Git Branch.

Chạy: python session_reset.py
"""

import os
import subprocess
from datetime import datetime


def get_git_branch(cwd: str) -> str:
    """Lấy tên branch hiện tại để tự động đặt tên session."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, cwd=cwd
        )
        return result.stdout.strip().replace("/", "_").replace("-", "_")
    except Exception:
        return "default"


def get_git_changes(cwd: str) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, cwd=cwd
        )
        return [line.strip().split()[-1] for line in result.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def main():
    print("=" * 55)
    print("  CHỐT PHIÊN CHAT - Hỗ Trợ Đa Session Song Song")
    print("=" * 55)

    cwd = os.path.dirname(os.path.abspath(__file__))
    current_branch = get_git_branch(cwd)

    # Hỏi tên session để tránh ghi đè chéo giữa các luồng công việc khác nhau
    session_name = input(
        f"\n🏷️ Nhập tên Session này (Ấn Enter để lấy theo Git Branch '{current_branch}'):\n> "
    ).strip()
    
    if not session_name:
        session_name = current_branch

    # Chuẩn hóa tên file
    safe_session_name = "".join(c for c in session_name if c.isalnum() or c in ("_", "-")).lower()

    accomplished = input("\n✅ Những việc đã hoàn thành trong phiên này:\n> ").strip()
    todo_next = input("\n📋 Những việc cần làm tiếp theo:\n> ").strip()
    notes = input("\n📌 Ghi chú thêm (Enter để bỏ qua):\n> ").strip()

    modified_files = get_git_changes(cwd)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    os.makedirs("./scratch", exist_ok=True)
    checkpoint_path = f"./scratch/session_checkpoint_{safe_session_name}.md"

    content = f"""# Session Checkpoint [{session_name}] — {timestamp}

> Đọc file này để tiếp tục công việc trong phiên chat mới.

## ✅ Đã hoàn thành
{accomplished or "(Không có thông tin)"}

## 📋 Việc cần làm tiếp theo
{todo_next or "(Không có thông tin)"}

## 📌 Ghi chú
{notes or "(Không có)"}

## 📂 File đã chỉnh sửa trong session này (Git)
"""
    if modified_files:
        content += "\n".join(f"- `{f}`" for f in modified_files)
    else:
        content += "- Không phát hiện thay đổi."

    content += f"""

---
## Câu lệnh mở đầu cho phiên chat mới:
```
Hãy đọc file `./scratch/session_checkpoint_{safe_session_name}.md` để nắm bắt
bối cảnh hiện tại của session '{session_name}' và tiếp tục công việc.
Không cần đọc lại lịch sử chat cũ.
```
"""

    with open(checkpoint_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Đã tạo checkpoint cho session '{session_name}' tại: {checkpoint_path}")
    print("👉 Bây giờ bạn có thể đóng cửa sổ chat này và mở cửa sổ chat mới.")
    print("   Paste câu lệnh dưới đây để bắt đầu phiên làm việc mới:")
    print("=" * 55)
    print(f"Hãy đọc file `./scratch/session_checkpoint_{safe_session_name}.md` để nắm bắt bối cảnh hiện tại của session '{session_name}' và tiếp tục công việc.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()
