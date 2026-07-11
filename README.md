# Memory and Second Brain for Agents

Dự án cung cấp một hệ thống "Bộ não thứ hai" (Second Brain) mạnh mẽ, cung cấp bộ nhớ động dài hạn (Mem0) và kho tri thức tĩnh (LlamaIndex RAG) cho các AI Agents. Trải qua đợt tái cấu trúc toàn diện, hệ thống giờ đây trở nên siêu nhẹ, tập trung và dễ dàng kết nối với bất kỳ Agent nào (như Hermes, Claude, Gemini, Roo Code, Antigravity) thông qua các giao thức tiêu chuẩn.

---

## 💡 Triết Lý Thiết Kế: "API là Tiền Đề" (API-First Approach)

Kiến trúc mới được xây dựng xoay quanh nguyên lý **"API-First"**. Thay vì mỗi Agent phải tự gánh vác các logic xử lý RAG, Vector Database, và Memory phức tạp (như trước đây), giờ đây mọi tác vụ nặng nhọc đều được tập trung xử lý tại `api_server.py`. 

Các Agent (dù là Local LLM nhỏ gọn hay Cloud LLM) chỉ đóng vai trò là "Client" giao tiếp siêu nhẹ qua các API REST hoặc giao thức MCP. Điều này giúp hệ thống dễ dàng mở rộng và tiết kiệm tối đa tài nguyên cho thiết bị của bạn.

---

## ✨ Các Tính Năng Nổi Bật Kể Từ Bản Cập Nhật Mới Nhất

1. **Kiến Trúc Tập Trung (Centralized Architecture):** Máy chủ `api_server.py` đóng vai trò là trái tim của hệ thống, xử lý toàn bộ logic LlamaIndex (RAG) và Mem0 (Memory).
2. **Siêu Nhẹ RAM (No Docker):** Xóa bỏ hoàn toàn sự cồng kềnh của `docker-compose`. Qdrant giờ đây chạy trực tiếp dưới dạng **Local Engine** với dữ liệu lưu ngay tại `./db/qdrant_rag` và `./db/qdrant_mem0`.
3. **Ký Ức Chia Sẻ (Shared Memory):** Khắc phục triệt để tình trạng phân mảnh trí nhớ theo từng `agent_id`. Giờ đây, mọi Agent đều truy cập và đóng góp chung vào một nguồn ký ức duy nhất thông qua định danh `MEM0_USER_ID`. "Một Agent học, mọi Agent đều biết".
4. **Auto-Sync Watchdog:** Tự động lắng nghe thay đổi. Bất kỳ file tài liệu `.md`, `.txt`... nào được thả vào thư mục `docs/` sẽ ngay lập tức được tự động nạp (sync) vào hệ thống RAG mà không cần khởi động lại.
5. **Dashboard Trực Quan:** Cung cấp giao diện Streamlit (`dashboard.py`) để bạn dễ dàng quan sát, tìm kiếm và quản lý cả Ký ức (Mem0) lẫn Tri thức (RAG) một cách trực quan.
6. **Sẵn Sàng Cho MCP:** Cung cấp file `second_brain_mcp.py` cho phép tích hợp "Bộ não thứ hai" này vào mọi MCP Client hiện đại (như Roo Code, Antigravity, Cline) chỉ với vài dòng cấu hình.

---

## 🛠️ Kiến Trúc Dự Án (Project Architecture)

```text
                      [ Antigravity / Cline / Roo Code ]     [ Hermes / Personal Agents ]
                                      │                                  │
                              (Giao thức MCP)                  (Giao thức REST API)
                                      │                                  │
                                      ▼                                  ▼
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 API SERVER & MCP BRIDGE                                │
│                   (api_server.py  &  second_brain_mcp.py)                              │
│                                                                                        │
│       ┌────────────────────────────────┐       ┌────────────────────────────────┐      │
│       │        MEMORY (Mem0)           │       │         KNOWLEDGE (RAG)        │      │
│       │   (Shared: MEM0_USER_ID)       │       │    (LlamaIndex + Watchdog)     │      │
│       └────────────────────────────────┘       └────────────────────────────────┘      │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                      │
                   ┌──────────────────┴──────────────────┐
                   ▼                                     ▼
          ┌─────────────────┐                   ┌─────────────────┐
          │  db/qdrant_mem0 │                   │  db/qdrant_rag  │
          │  (Local Engine) │                   │  (Local Engine) │
          └─────────────────┘                   └─────────────────┘
```

---

## 📂 Cấu Trúc Thư Mục (Directory Layout)

```text
Memory and Second Brain for Agents/
├── .agents/                    ← Cấu hình và kỹ năng tùy chỉnh của Agent
├── api_server.py               ← [NEW] Máy chủ trung tâm API (FastAPI) xử lý RAG & Mem0
├── second_brain_mcp.py         ← [NEW] MCP Server cho các AI IDE (Antigravity, Roo Code)
├── dashboard.py                ← [NEW] Giao diện quản lý trực quan Ký ức & RAG (Streamlit)
├── agent_core/                 ← Code xử lý logic cốt lõi (MemoryManager, KnowledgeBase)
├── db/                         ← [NEW] Dữ liệu Qdrant lưu tại local (qdrant_rag, qdrant_mem0)
├── docs/                       ← Thư mục chứa tài liệu RAG. Có cơ chế Auto-Sync Watchdog
├── config.yaml                 ← File cấu hình tổng (Model, Port...)
├── .env.example                ← File mẫu biến môi trường (API Keys)
└── requirements.txt            ← Danh sách thư viện Python
```

---

## 🚀 Hướng Dẫn Cài Đặt (Installation)

### 1. Cấu hình biến môi trường
Sao chép file `.env.example` thành `.env`:
```bash
copy .env.example .env  # Trên Windows
# hoặc
cp .env.example .env    # Trên Linux/Mac
```
Mở `.env` và cấu hình các API Key cần thiết (ví dụ: `GEMINI_API_KEY`, `OPENAI_API_KEY` tùy theo model bạn sử dụng trong `config.yaml`).

### 2. Cài đặt thư viện
Đảm bảo bạn đang sử dụng Python 3.10 trở lên. Khởi tạo môi trường ảo (tùy chọn) và cài đặt các thư viện:
```bash
pip install -r requirements.txt
```

---

## 📖 Hướng Dẫn Sử Dụng (Usage)

Để hệ thống hoạt động đầy đủ chức năng, bạn cần chạy API Server.

### Chạy API Server (Trái tim của hệ thống)
Mở một terminal và chạy lệnh:
```bash
python api_server.py
```
*API Server sẽ khởi động và tự động kích hoạt **Watchdog**. Bất kỳ tài liệu nào trong thư mục `docs/` sẽ được tự động quét và nạp vào cơ sở dữ liệu `db/qdrant_rag` cục bộ.*

### Chạy Giao diện Quản trị Dashboard (Tùy chọn)
Để xem và quản lý trực quan các ký ức và tài liệu RAG đang có trong hệ thống, mở một terminal thứ hai và chạy:
```bash
streamlit run dashboard.py
```

### Cách Thêm Tài Liệu Vào RAG
Rất đơn giản, bạn chỉ cần thả các file tài liệu (ví dụ: `.md`, `.txt`, `.pdf`) vào thư mục `docs/`. Nhờ cơ chế Auto-Sync (Watchdog), API Server sẽ tự động phát hiện và lập chỉ mục tài liệu vào RAG ngay lập tức mà không cần bạn phải thao tác thêm.

---

## 🔌 Tích Hợp "Bộ Não" Vào AI IDE (MCP Client)

Dự án cung cấp sẵn file `second_brain_mcp.py` tuân thủ chuẩn giao thức MCP, giúp các IDE thông minh kết nối tới API Server.

> **Lưu ý quan trọng:** Bạn **luôn phải để `api_server.py` chạy ngầm** thì MCP mới có thể giao tiếp được với "Bộ não".

### Cách Cấu Hình Trên Antigravity (hoặc Roo Code / Cline)
Trong công cụ quản lý MCP của IDE (ví dụ: nhấn `Ctrl + Shift + P` -> Manage MCP Servers, hoặc cấu hình qua GUI của Antigravity), thêm cấu hình sau:

*   **Name:** `SecondBrain`
*   **Command:** `python`
*   **Arguments:** `["Đường/dẫn/tuyệt/đối/tới/dự/án/second_brain_mcp.py"]` (Thay thế bằng đường dẫn thực tế trên máy bạn)
*   **Environment Variables:** Đảm bảo truyền các biến môi trường cần thiết nếu IDE yêu cầu.

### Cách Chat Với Agent
Sau khi cấu hình MCP, Agent đã được "kết nối não". Bạn cứ chat bình thường:
*   *"Tra cứu trong tài liệu của bạn xem..."* -> Agent sẽ tự gọi RAG.
*   *"Ghi nhớ vào não của bạn rằng tôi rất ghét code thừa..."* -> Agent sẽ tự lưu vào Mem0 (Shared Memory).
*   *"Hãy kiểm tra trí nhớ của bạn xem dự án trước chúng ta dùng thư viện gì?"* -> Agent sẽ tự truy vấn Mem0.

---

*Memory and Second Brain for Agents - Kiến tạo bộ nhớ vượt thời gian cho thế hệ AI tương lai.*
