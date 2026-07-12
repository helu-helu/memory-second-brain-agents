# Memory and Second Brain for Agents

Dự án cung cấp một hệ thống "Bộ não thứ hai" tự host cho AI agent, kết hợp bộ nhớ dài hạn theo người dùng (Mem0) với kho tri thức tài liệu (LlamaIndex RAG). Một API FastAPI trung tâm phục vụ cả REST và cầu nối MCP, trong khi Qdrant lưu vector cục bộ.

> **Phạm vi hiện tại:** đây là lớp memory + retrieval dùng chung cho nhiều client, không phải một agent runtime hoàn chỉnh. Dự án chưa quản lý vòng đời agent, thread/checkpoint thực thi hay quan hệ tri thức có hiệu lực theo thời gian.

---

## 💡 Triết Lý Thiết Kế: "API là Tiền Đề" (API-First Approach)

Kiến trúc mới được xây dựng xoay quanh nguyên lý **"API-First"**. Thay vì mỗi Agent phải tự gánh vác các logic xử lý RAG, Vector Database, và Memory phức tạp (như trước đây), giờ đây mọi tác vụ nặng nhọc đều được tập trung xử lý tại `api_server.py`. 

Các Agent (dù là Local LLM nhỏ gọn hay Cloud LLM) chỉ đóng vai trò là "Client" giao tiếp siêu nhẹ qua các API REST hoặc giao thức MCP. Điều này giúp hệ thống dễ dàng mở rộng và tiết kiệm tối đa tài nguyên cho thiết bị của bạn.

---

## ✨ Các Tính Năng Nổi Bật Kể Từ Bản Cập Nhật Mới Nhất

1. **Kiến Trúc Tập Trung (Centralized Architecture):** Máy chủ `api/api_server.py` đóng vai trò là trái tim của hệ thống, xử lý toàn bộ logic LlamaIndex (RAG) và Mem0 (Memory).
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
│                (api/api_server.py  &  second_brain_mcp.py)                             │
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
├── api/api_server.py           ← Máy chủ trung tâm API (FastAPI) xử lý RAG & Mem0
├── second_brain_mcp.py         ← MCP Server cho các AI IDE (Antigravity, Roo Code)
├── dashboard.py                ← Giao diện quản lý Ký ức & RAG (Streamlit)
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
python api/api_server.py
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

> **Lưu ý quan trọng:** Bạn **luôn phải để `api/api_server.py` chạy ngầm** thì MCP mới có thể giao tiếp được với "Bộ não".

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

## Đối chiếu với các dự án cộng đồng

Đối chiếu ngày **2026-07-12**, dựa trên tài liệu và repository chính thức. Các dự án dưới đây giải quyết những phần giao nhau nhưng không hoàn toàn cùng phạm vi.

| Dự án | Trọng tâm | Điểm tương đồng | Khác biệt chính / bài học cho dự án này |
|---|---|---|---|
| [Mem0](https://github.com/mem0ai/mem0) | Lớp memory phổ dụng cho agent | Đây là engine memory đang được dự án dùng; cùng hỗ trợ memory dài hạn và phân vùng theo người dùng | Mem0 hỗ trợ mô hình user/session/agent và retrieval đa tín hiệu. Wrapper hiện tại mới công khai `user_id`; nên chỉ mở rộng scope khi có use case đa phiên hoặc đa agent rõ ràng. |
| [Letta](https://github.com/letta-ai/letta) | Nền tảng xây agent stateful | Cùng hướng tới agent có ký ức bền vững và có API | Letta sở hữu cả agent runtime, memory blocks và vòng đời agent. Dự án này nhẹ hơn vì chỉ cung cấp memory/RAG service; không nên mô tả như một framework agent đầy đủ. |
| [Graphiti](https://github.com/getzep/graphiti) | Temporal knowledge graph cho context thay đổi liên tục | Cùng ingest tăng dần, truy xuất context và có MCP/REST | Graphiti lưu provenance, quan hệ và validity theo thời gian, dùng hybrid graph search. RAG hiện tại là vector retrieval trên tài liệu tĩnh; temporal graph chỉ đáng thêm khi phải trả lời “đúng tại thời điểm nào” hoặc xử lý mâu thuẫn lịch sử. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Điều phối agent stateful, durable execution | Cùng quan tâm tới state/memory lâu dài | LangGraph quản lý checkpoint, luồng thực thi và human-in-the-loop; dự án này không điều phối workflow. Có thể dùng nó như client của API, không cần đưa vào lõi. |

### Vị trí phù hợp của dự án

Dự án phù hợp nhất khi cần một **dịch vụ second-brain tự host, local-first, dùng chung qua REST/MCP**, tách khỏi runtime của agent. Thiết kế hiện tại ưu tiên vận hành đơn giản: Mem0 cho ký ức cá nhân, LlamaIndex + Qdrant cho tài liệu, Watchdog cho cập nhật nhỏ và pipeline manifest cho corpus lớn.

### Khoảng trống đã xác định

- Memory mới được phân vùng công khai theo `user_id`; chưa có contract riêng cho session/agent scope.
- Kết quả RAG có nguồn file nhưng chưa có provenance cấp fact, version lịch sử hay temporal validity.
- Chưa có durable execution/checkpoint cho workflow; đây chủ ý là trách nhiệm của agent runtime bên ngoài.
- Chưa có benchmark retrieval/memory cố định trong repo để đo recall, latency và chất lượng sau mỗi thay đổi.

Ưu tiên hợp lý tiếp theo là bổ sung một bộ eval nhỏ, có dữ liệu và câu hỏi chuẩn, trước khi thêm graph database hoặc orchestration framework. Đây là cách kiểm chứng khoảng trống thực tế mà không làm kiến trúc phình to sớm.

---

*Memory and Second Brain for Agents - Kiến tạo bộ nhớ vượt thời gian cho thế hệ AI tương lai.*
