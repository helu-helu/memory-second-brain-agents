---
name: session-checkpoint
description: Tự động phân tích và tạo báo cáo chốt phiên chat (checkpoint) khi được người dùng yêu cầu để tiết kiệm token và chuyển bối cảnh sang session mới.
---

# Kỹ Năng Tự Động Chốt Phiên (Session Checkpoint Skill)

Sử dụng skill này khi người dùng yêu cầu chốt phiên hoặc checkpoint session (ví dụ: "Hãy chốt phiên này lại", "Lưu checkpoint session này").

## Hướng Dẫn Thực Hiện Cho Agent

### Bước 1: Thu thập thông tin thay đổi code
1. Chạy lệnh `git status` và `git diff` trong workspace để xem danh sách các file đã chỉnh sửa và nội dung thay đổi.
2. Tóm tắt nhanh các mốc quan trọng đã thống nhất hoặc thảo luận trong cuộc trò chuyện hiện tại.

### Bước 2: Tự động chạy script hoặc tự viết báo cáo
- Bạn có thể chạy trực tiếp script trợ giúp nằm trong skill này:
  `python .agents/skills/session_checkpoint/scripts/auto_checkpoint.py [tên_session]`
- Hoặc tự tạo file `./scratch/session_checkpoint_<safe_session_name>.md` với cấu trúc:

```markdown
# Session Checkpoint [<tên_session>] — [Thời gian]

> Báo cáo chốt phiên tự động được tạo bởi Agent.

## 📂 Các file đã chỉnh sửa trong session này (Git)
- `đường/dẫn/file`

## 📝 Nội dung chốt phiên từ Agent
### 1. Đã hoàn thành (Accomplished tasks)
- [Tóm tắt chi tiết việc đã làm]

### 2. Gợi ý bước tiếp theo (Suggested next steps)
- [Các việc cần làm tiếp theo]

---
## Câu lệnh mở đầu cho phiên chat mới:
```text
Hãy đọc file `./scratch/session_checkpoint_<safe_session_name>.md` để nắm bắt bối cảnh hiện tại của session '<tên_session>' và tiếp tục công việc.
```
```

### Bước 3: Phản hồi người dùng
1. Thông báo đã ghi file checkpoint thành công.
2. In ra câu lệnh mở đầu để người dùng dễ dàng sao chép sang session chat mới.
