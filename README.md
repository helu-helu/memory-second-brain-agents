# Memory and Second Brain for Agents

Hệ thống bộ nhớ động dài hạn (Mem0) kết hợp kho tri thức tĩnh (LlamaIndex RAG) chạy cục bộ (local) kết hợp với Gemini AI Studio.

---

## 🛠️ Kiến Trúc Dự Án (Project Architecture)

Dự án được thiết kế theo mô hình **Second Brain (Bộ não thứ hai)** để tối ưu hóa token và bối cảnh hoạt động cho AI Agent:

```
                      ┌────────────────────────┐
                      │    AI Coding Agent     │
                      │ (Cline, Antigravity...)│
                      └────────────────────────┘
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
┌──────────────────┐                            ┌──────────────────┐
│  Bộ nhớ động     │                            │  Tri thức tĩnh   │
│  (MemoryManager) │                            │ (KnowledgeBase)  │
└──────────────────┘                            └──────────────────┘
   Mem0 + Qdrant local                             LlamaIndex RAG
   SQLite History                                  docs/ (Unity 6.3)
   Dimension: 768                                  Dimension: 768
```

*   **Bộ nhớ động (Dynamic Memory - Mem0):** Tự động ghi nhớ sở thích, thói quen và quyết định thiết kế của lập trình viên qua các phiên làm việc.
*   **Tri thức tĩnh (Static Knowledge - RAG):** Kho tài liệu tra cứu kỹ thuật cục bộ (mặc định cấu hình cho tài liệu Unity 6.3).

---

## 📂 Cấu Trúc Thư Mục (Directory Layout)

```
Memory and Second Brain for Agents/
├── .agents/
│   ├── AGENTS.md               ← Quy tắc chung & Hướng dẫn cho AI Agent
│   └── skills/
│       └── session_checkpoint/ ← Skill tự động chốt phiên của Agent
│           ├── SKILL.md
│           └── scripts/
│               └── auto_checkpoint.py  ← Script AI tự động phân tích Git Diff
├── agent_core/
│   ├── __init__.py             ← Package interface chính
│   ├── memory.py               ← Wrapper Mem0 (Gemini 2.5 Flash + Qdrant local 768d)
│   ├── knowledge.py            ← Wrapper LlamaIndex RAG (Gemini Embedding 2)
│   └── context_builder.py      ← Bộ xây dựng System Prompt tích hợp
├── docs/                       ← Thư mục chứa tài liệu RAG (.md, .html, .json, .txt)
├── db/                         ← Thư mục lưu trữ database cục bộ (Qdrant & SQLite)
├── scratch/                    ← Thư mục lưu trữ file checkpoint tạm thời
├── requirements.txt            ← Các thư viện Python cần thiết
├── .env.example                ← Mẫu cấu hình biến môi trường
├── setup_phase1.py             ← Script kiểm tra và xác minh hệ thống
└── session_reset.py            ← Công cụ CLI chốt phiên chat thủ công
```

---

## 🚀 Hướng Dẫn Cài Đặt (Installation)

### 1. Cấu hình biến môi trường
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
