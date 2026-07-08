# Quy Tắc Hoạt Động Của AI Agent Trong Workspace

Tài liệu này chứa các quy tắc hướng dẫn hành vi cho các AI Agent (Cline, Antigravity,...) khi làm việc trong dự án này.

---

## 1. Cơ Chế Chốt Phiên (Checkpoint Session)
- Khi người dùng yêu cầu **"Chốt phiên"**, **"Checkpoint session"**, hoặc gửi câu lệnh dạng **"Hãy chốt phiên chat này lại với tên session <tên_session>"**:
  - Bạn **bắt buộc** phải kích hoạt và tuân thủ các chỉ dẫn chi tiết trong skill `session-checkpoint` để tự động hóa việc lưu trữ bối cảnh.

---

## 2. Đồng Bộ Hóa Tài Liệu (Documentation Sync Rule)
- Mỗi khi bạn thực hiện **thay đổi tính năng, sửa lỗi lớn hoặc cập nhật cấu trúc thư mục** trong dự án:
  - Bạn **bắt buộc** phải cập nhật các tài liệu hướng dẫn tương ứng (README.md, walkthrough, hoặc tài liệu kỹ thuật có sẵn) trước khi kết thúc phiên. Không được để code chạy một đường và tài liệu mô tả một nẻo.
