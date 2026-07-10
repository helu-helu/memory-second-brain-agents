# Memory and Second Brain for Agents

Hệ thống bộ nhớ động dài hạn (Mem0) kết hợp kho tri thức tĩnh (LlamaIndex RAG) chạy cục bộ (local) kết hợp với Gemini AI Studio.

---

## 🛠️ Kiến Trúc Dự Án (Project Architecture)

Dự án được thiết kế theo mô hình **Second Brain (Bộ não thứ hai)** với kiến trúc trung tâm (Centralized) nhằm hỗ trợ đa Agent cùng lúc:

```
                      [ Antigravity / Cline ]      [ Hermes / Personal Agents ]
                               │                                │
                       (Giao thức MCP stdio)            (Giao thức HTTP REST)
                               │                                │
                               ▼                                ▼
                      ┌───────────────────────────────────────────────┐
                      │            API Bridge & MCP Server            │
                      │       (api/mcp_server.py & api/api_server.py)         │
                      └───────────────────────────────────────────────┘
                                              │
                         ┌────────────────────┴────────────────────┐
                         ▼                                         ▼
               ┌──────────────────┐                      ┌──────────────────┐
               │  Bộ nhớ động     │                      │  Tri thức tĩnh   │
               │  (MemoryManager) │                      │ (KnowledgeBase)  │
               └──────────────────┘                      └──────────────────┘
                         │                                         │
                         └────────────────────┬────────────────────┘
                                              ▼
                              ┌──────────────────────────────────┐
                              │     Qdrant Server (Docker)       │
                              │     localhost:6333 / 6334        │
                              └──────────────────────────────────┘
```

---

## 📂 Cấu Trúc Thư Mục (Directory Layout)

```
Memory and Second Brain for Agents/
├── .agents/                    ← Cấu hình và kỹ năng của Agent
├── agent_core/                 ← Code xử lý trung tâm (memory.py, knowledge.py kết nối Docker)
├── db/                         ← Thư mục lưu DB (Volume của Docker)
├── docs/                       ← Thư mục tài liệu RAG
├── docker-compose.yml          ← Script chạy Qdrant Server qua Docker
├── config.yaml                 ← [NEW] File cấu hình tập trung (model, port, db path)
├── .env.example                ← [NEW] Mẫu cấu hình API Keys
├── api/                        ← [NEW] Thư mục chứa các API entrypoints
│   ├── api_server.py           ← Máy chủ FastAPI trung tâm cho các Agent nhẹ
│   └── mcp_server.py           ← Máy chủ MCP cho các AI IDE (Cline, Roo Code)
├── tests/                      ← [NEW] Thư mục chuẩn bị cho Unit Tests
├── logs/                       ← [NEW] Thư mục lưu log hệ thống
└── session_reset.py            ← Công cụ chốt phiên chat
```

---

## 🚀 Hướng Dẫn Cài Đặt (Installation)

### 1. Khởi chạy Qdrant Server (Docker)
Bắt buộc phải cài đặt Docker Desktop và chạy lệnh sau để khởi động cơ sở dữ liệu Vector:
```bash
docker-compose up -d
```

### 2. Cấu hình biến môi trường
Sao chép `.env.example` thành `.env`:
```bash
copy .env.example .env
```
Mở `.env` và điền khóa Gemini API của bạn:
```env
GEMINI_API_KEY=your_actual_api_key_here
GOOGLE_API_KEY=your_actual_api_key_here
```
*(Lấy API Key miễn phí tại: [Google AI Studio](https://aistudio.google.com/app/apikey))*

### 2. Cài đặt các thư viện cần thiết
Dự án được tối ưu hóa cho Python 3.13. Chạy lệnh sau để cài đặt:
```bash
pip install -r requirements.txt
```

### 3. Chạy xác minh hệ thống
Lệnh này sẽ tự động kiểm tra kết nối API, cài đặt thư viện, cấu trúc thư mục và chạy kiểm tra ghi/đọc trên database cục bộ:
```bash
python setup_phase1.py
```
Nếu tất cả hiển thị `[OK]`, hệ thống của bạn đã sẵn sàng hoạt động!

---

## 📖 Hướng Dẫn Sử Dụng (Usage)

### 1. Sử dụng Bộ nhớ và RAG trong Code
```python
from agent_core import MemoryManager, KnowledgeBase, ContextBuilder

# 1. Khởi tạo bộ nhớ động và nạp tri thức tĩnh RAG
memory = MemoryManager()
knowledge = KnowledgeBase()
knowledge.load()  # Tự động lập chỉ mục tài liệu từ thư mục ./docs/

# 2. Tạo Prompt Builder
builder = ContextBuilder(memory, knowledge)

# 3. Khi nhận được yêu cầu từ người dùng
user_query = "Tôi muốn viết script Unity để cấu hình database"
system_prompt = builder.build(user_query)
# -> system_prompt này sẽ tự động chứa các ký ức liên quan từ Mem0 
#    và các đoạn tài liệu liên quan từ thư mục ./docs/
```

### 2. Thêm tài liệu vào RAG (Unity 6.3)
1. Thả các file tài liệu định dạng `.md`, `.html`, `.json`, hoặc `.txt` vào thư mục `./docs/`
2. Khởi động lại ứng dụng hoặc gọi `knowledge.reload()` trong code để cập nhật cơ sở dữ liệu vector.

---

## ⏱️ Cơ Chế Tiết Kiệm Token & Chốt Phiên (Session Reset)

Để tránh cạn kiệt token sau các phiên chat dài (5h+), dự án hỗ trợ hai cơ chế chốt phiên và lưu trữ bối cảnh:

### Cách 1: Yêu cầu AI Agent tự làm (Khuyến nghị)
Bạn chỉ cần nhắn vào ô chat của Agent:
> *"Hãy chốt phiên này lại dưới tên session `db_setup`. Việc tiếp theo tôi muốn làm là cấu hình API."*

AI Agent (Cline, Antigravity) sẽ tự động chạy Git, phân tích cuộc gọi và ghi file checkpoint tương ứng vào thư mục `scratch/`.

### Cách 2: Chạy thủ công qua Command Line
Nếu bạn muốn tự kiểm soát quy trình chốt phiên:
```bash
python session_reset.py
```
*   Nhập tên session gợi nhớ (ví dụ: `database_setup`).
*   Trả lời nhanh các câu hỏi về việc đã hoàn thành và việc cần làm tiếp theo.

### Cách tiếp tục công việc ở Session mới:
Mở cửa sổ chat mới tinh, copy và gửi câu lệnh mở đầu được sinh ra ở cuối file checkpoint:
```text
Hãy đọc file `./scratch/session_checkpoint_db_setup.md` để nắm bắt bối cảnh hiện tại của session 'db_setup' và tiếp tục công việc.
```

---

## 🔌 Cấu Hình Vào AI Agent (Antigravity / Cline / Roo Code)

Dự án này cung cấp một máy chủ local MCP (`api/mcp_server.py`) chạy qua giao thức stdio. Khi cấu hình vào các AI IDE (như Antigravity, Cline, hoặc Roo Code), AI Agent sẽ tự động được trang bị các kỹ năng "ngoại cảm" để tra cứu tri thức và đọc trí nhớ ngầm (under the hood) khi chat với bạn.

> [!IMPORTANT]
> Vì hệ thống đã chuyển sang kiến trúc Lock-Free ở Giai đoạn 3, bạn **bắt buộc phải khởi chạy Qdrant Docker** (`docker-compose up -d`) trước khi sử dụng tính năng này trong Agent.

### Cách 1: Cấu hình nhanh trên Antigravity IDE (Khuyến nghị)
1. Trong cửa sổ chat của Antigravity, gõ lệnh `/mcp` (hoặc nhấn `Ctrl + Shift + P` -> "Antigravity: Manage MCP Servers").
2. Chọn **"Add new server"**.
3. Điền thông tin:
   * **Name:** `SecondBrain`
   * **Command:** `python api/mcp_server.py` (Hoặc đường dẫn tuyệt đối tới python.exe của bạn nếu dùng venv)
   * *(Nhớ trỏ Working Directory tới thư mục dự án này và cấu hình biến môi trường `GEMINI_API_KEY` nếu UI yêu cầu).*

### Cách 2: Cấu hình thủ công qua file JSON (Cline / Roo Code)
Mở file cấu hình MCP của Cline (`clinedesktop_config.json`) hoặc Roo Code (`mcpConfig.json`) và thêm block sau:

```json
{
  "mcpServers": {
    "memory-second-brain-bridge": {
      "command": "python",
      "args": ["<ABSOLUTE_PATH_TO_PROJECT>/api/mcp_server.py"],
      "env": {
        "GEMINI_API_KEY": "your_actual_api_key_here",
        "APP_API_KEY": "my-super-secret-key-123"
      },
      "disabled": false
    }
  }
}
```

---

## 🗣️ Cách Sử Dụng Khi Trò Chuyện (How to Chat with Agent)

Sau khi kết nối MCP thành công, bạn **không cần viết code** để gọi RAG. Hãy giao tiếp tự nhiên với AI Agent như một người trợ lý thực thụ:

*   **Để tìm kiếm tài liệu (RAG):**
    > *"Tra cứu trong tài liệu RAG xem cấu hình vật lý 2D của Unity 6.3 nằm ở port nào?"*
    *(Agent sẽ tự động gọi tool `search_knowledge`)*

*   **Để lưu trữ sở thích (Mem0):**
    > *"Hãy ghi nhớ vào não bộ của bạn rằng tôi luôn thích viết tên biến theo chuẩn camelCase nhé."*
    *(Agent sẽ tự động gọi tool `add_memory`)*

*   **Để truy xuất ký ức (Mem0):**
    > *"Kiểm tra trí nhớ xem lần trước tôi đã nói tôi thích dùng database gì?"*
    *(Agent sẽ tự động gọi tool `search_memory`)*

