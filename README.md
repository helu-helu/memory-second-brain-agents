# Memory and Second Brain for Agents

Dự án cung cấp một hệ thống "Bộ não thứ hai" (Second Brain) mạnh mẽ, cung cấp bộ nhớ động dài hạn (Mem0) và kho tri thức tĩnh (LlamaIndex RAG) cho các AI Agents. Trải qua đợt tái cấu trúc toàn diện, hệ thống giờ đây trở nên siêu nhẹ, tập trung và dễ dàng kết nối với bất kỳ Agent nào (như Hermes, Claude, Gemini, Roo Code, Antigravity) thông qua các giao thức tiêu chuẩn.

---

## 💡 Triết Lý Thiết Kế: "API là Tiền Đề" (API-First Approach)

Kiến trúc mới được xây dựng xoay quanh nguyên lý **"API-First"**. Thay vì mỗi Agent phải tự gánh vác các logic xử lý RAG, Vector Database, và Memory phức tạp (như trước đây), giờ đây mọi tác vụ nặng nhọc đều được tập trung xử lý tại `api_server.py`. 

Các Agent (dù là Local LLM nhỏ gọn hay Cloud LLM) chỉ đóng vai trò là "Client" giao tiếp siêu nhẹ qua các API REST hoặc giao thức MCP. Điều này giúp hệ thống dễ dàng mở rộng và tiết kiệm tối đa tài nguyên cho thiết bị của bạn.

---

## ✨ Các Tính Năng Nổi Bật Kể Từ Bản Cập Nhật Mới Nhất

1. **Kiến Trúc Tập Trung (Centralized Architecture):** Máy chủ `api_server.py` đóng vai trò là trái tim của hệ thống, xử lý toàn bộ logic LlamaIndex (RAG) và Mem0 (Memory).
2. **Qdrant Server Cục Bộ:** Corpus lớn chạy trên Qdrant single-node bằng Docker named volume. Server chỉ bind vào `127.0.0.1`; local embedded mode vẫn dành cho test và corpus nhỏ.
3. **Ký Ức Theo Người Dùng:** Memory được phân vùng duy nhất bằng `user_id`. Các Agent dùng cùng `MEM0_USER_ID` sẽ chia sẻ một nguồn ký ức; các `user_id` khác nhau được lưu và truy xuất độc lập.
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
          │ personal_agent_ │                   │ personal_knowle │
          │ memory          │                   │ dge_base       │
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
├── db/                         ← Manifest/checkpoint ingestion; vector data nằm trong Docker volume
├── compose.yaml                ← Qdrant 1.18.2, localhost-only, persistent named volume
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
Mở `.env` và cấu hình `APP_API_KEY`, `MEM0_USER_ID` cùng API key tùy chọn. MCP client nên truyền các giá trị này qua trường `env`; MCP server chỉ đọc process environment và không ghi secret xuống `.env`.

### 2. Cài đặt thư viện
Đảm bảo bạn đang sử dụng Python 3.10 trở lên. Khởi tạo môi trường ảo (tùy chọn) và cài đặt các thư viện:
```bash
pip install -r requirements.txt
```

---

### 3. Chạy Qdrant

```bash
docker compose up -d qdrant
```

Dashboard Qdrant: `http://127.0.0.1:6333/dashboard`.

## 📖 Hướng Dẫn Sử Dụng (Usage)

Để hệ thống hoạt động đầy đủ chức năng, bạn cần chạy API Server.

### Chạy API Server (Trái tim của hệ thống)
Mở một terminal và chạy lệnh:
```bash
python api_server.py
```
*API Server kết nối Qdrant tại `127.0.0.1:6333` và kích hoạt Watchdog để cập nhật file thay đổi.*

### Chạy Giao diện Quản trị Dashboard (Tùy chọn)
Để xem và quản lý trực quan các ký ức và tài liệu RAG đang có trong hệ thống, mở một terminal thứ hai và chạy:
```bash
streamlit run dashboard.py
```

### Cách Thêm Tài Liệu Vào RAG
Với cập nhật nhỏ, thêm file `.md`, `.txt` hoặc `.json` vào `docs/` để Watchdog đồng bộ. Với corpus lớn như Unity, dùng pipeline resumable:

```bash
python scripts/build_massive_index.py docs/massive
```

Pipeline lưu manifest trong `db/ingestion_manifest.sqlite`, bỏ qua file không đổi, batch embedding trên GPU và bulk-upload vào Qdrant. Dùng `--dry-run` để kiểm tra corpus hoặc `--limit 1000 --collection unity_benchmark` để benchmark collection riêng.

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
