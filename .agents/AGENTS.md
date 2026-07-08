# Quy Tắc Hoạt Động Của AI Agent Trong Workspace

Tài liệu này chứa các quy tắc hướng dẫn hành vi cho các AI Agent (Cline, Antigravity,...) khi làm việc trong dự án này.

---

## Quy Tắc Chốt Phiên Tự Động (Auto-Checkpoint Rule)

Khi người dùng yêu cầu bạn **"Chốt phiên"**, **"Checkpoint session"**, hoặc gửi câu lệnh dạng **"Hãy chốt phiên chat này lại với tên session <tên_session>"**:

### 1. Phân tích nội dung và Git:
- **Tóm tắt hội thoại:** Phân tích lịch sử chat của phiên hiện tại để tổng hợp các cột mốc đã thảo luận và thống nhất.
- **Quét Git:** Chạy các lệnh terminal `git status` và `git diff` (hoặc xem danh sách file thay đổi) để thu thập danh sách các file code đã sửa và nội dung thay đổi.

### 2. Ghi file Checkpoint:
Tạo hoặc ghi đè file `./scratch/session_checkpoint_<safe_session_name>.md` (chuyển `<tên_session>` thành chữ thường, không dấu, phân tách bằng dấu gạch dưới).

Nội dung file phải tuân thủ cấu trúc sau:
```markdown
# Session Checkpoint [<tên_session>] — [Thời gian hiện tại]

> Báo cáo chốt phiên tự động được tạo bởi Agent.

## 📂 Các file đã chỉnh sửa trong session này (Git)
- `đường/dẫn/file_1.py`
- `đường/dẫn/file_2.py`

## 📝 Nội dung chốt phiên từ Agent
### 1. Đã hoàn thành (Accomplished tasks)
- [Tóm tắt chi tiết các việc đã làm trong cả code và hội thoại]

### 2. Gợi ý bước tiếp theo (Suggested next steps)
- [Các việc cần làm tiếp theo]

---
## Câu lệnh mở đầu cho phiên chat mới:
```text
Hãy đọc file `./scratch/session_checkpoint_<safe_session_name>.md` để nắm bắt
bối cảnh hiện tại của session '<tên_session>' và tiếp tục công việc.
Không cần đọc lại lịch sử chat cũ.
```
```

### 3. Phản hồi cho người dùng:
- Xác nhận đã tạo file checkpoint thành công (gửi kèm link file).
- In ra câu lệnh mở đầu để người dùng dễ dàng copy-paste sang session mới.
