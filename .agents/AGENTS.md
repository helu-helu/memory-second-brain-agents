# Quy Tắc Hoạt Động Của AI Agent Trong Workspace

Tài liệu này chứa các quy tắc hướng dẫn hành vi cho các AI Agent (Cline, Antigravity,...) khi làm việc trong dự án này.

---

## 1. Cơ Chế Chốt Phiên (Checkpoint Session)
- Khi người dùng yêu cầu **"Chốt phiên"**, **"Checkpoint session"**, hoặc gửi câu lệnh dạng **"Hãy chốt phiên chat này lại với tên session <tên_session>"**:
  - Bạn **bắt buộc** phải kích hoạt và tuân thủ các chỉ dẫn chi tiết trong skill `session-checkpoint` để tự động hóa việc lưu trữ bối cảnh.
