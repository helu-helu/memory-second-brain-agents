"""
session_reset.py
Công cụ chốt phiên chat để tiết kiệm token.

Chạy: python session_reset.py

Kết quả: tạo file ./scratch/session_checkpoint.md
Sau đó: đóng cửa sổ chat cũ, mở cửa sổ mới và paste câu lệnh
trong file checkpoint để Agent tiếp tục công việc.
"""

import os
import subprocess
from datetime import datetime


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
    print("  CHỐT PHIÊN CHAT — Tiết Kiệm Token")
    print("=" * 55)

    accomplished = input("\n✅ Những việc đã hoàn thành trong phiên này:\n> ").strip()
    todo_next = input("\n📋 Những việc cần làm tiếp theo:\n> ").strip()
    notes = input("\n📌 Ghi chú thêm (Enter để bỏ qua):\n> ").strip()

    cwd = os.path.dirname(os.path.abspath(__file__))
    modified_files = get_git_changes(cwd)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    os.makedirs("./scratch", exist_ok=True)
    checkpoint_path = "./scratch/session_checkpoint.md"

    content = f"""# Session Checkpoint — {timestamp}

> Đọc file này để tiếp tục công việc trong phiên chat mới.

## ✅ Đã hoàn thành
{accomplished or "(Không có thông tin)"}

## 📋 Việc cần làm tiếp theo
{todo_next or "(Không có thông tin)"}

## 📌 Ghi chú
{notes or "(Không có)"}

## 📂 File đã chỉnh sửa (Git)
"""
    if modified_files:
        content += "\n".join(f"- `{f}`" for f in modified_files)
    else:
        content += "- Không phát hiện thay đổi."

    content += """

---
## Câu lệnh mở đầu cho phiên chat mới:
```
Hãy đọc file `./scratch/session_checkpoint.md` để nắm bắt
bối cảnh hiện tại và tiếp tục công việc từ bước tiếp theo.
Không cần đọc lại lịch sử chat cũ.
```
"""

    with open(checkpoint_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Đã tạo checkpoint tại: {checkpoint_path}")
    print("👉 Bây giờ hãy đóng cửa sổ chat này và mở cửa sổ chat mới.")
    print("   Paste câu lệnh trong file checkpoint để Agent tiếp tục.\n")


if __name__ == "__main__":
    main()
