# Memory and Second Brain for Agents

Hệ thống bộ nhớ thông minh cho AI Agent cá nhân.  
**Phase 1:** Mem0 (bộ nhớ động) + LlamaIndex RAG (tri thức tĩnh) chạy hoàn toàn cục bộ.

---

## Cấu trúc dự án

```
.
├── agent_core/
│   ├── __init__.py         ← Package chính
│   ├── memory.py           ← Mem0 wrapper (Gemini Flash + Qdrant local)
│   ├── knowledge.py        ← RAG wrapper (LlamaIndex + Qdrant local)
│   └── context_builder.py  ← Tự động xây System Prompt từ Mem0 + RAG
├── docs/                   ← Đặt file tài liệu vào đây (.md, .html, .json, .txt)
├── db/                     ← Dữ liệu vector DB & SQLite (tự động tạo)
├── scratch/                ← File tạm & checkpoint (tự động tạo)
├── requirements.txt
├── .env.example            ← Sao chép thành .env và điền API key
├── setup_phase1.py         ← Kiểm tra toàn bộ hệ thống
└── session_reset.py        ← Chốt phiên để tiết kiệm token
```

---

## Cài đặt nhanh

### 1. Cấu hình API Key
```bash
copy .env.example .env
# Mở .env và điền GEMINI_API_KEY
# Lấy key miễn phí: https://aistudio.google.com/app/apikey
```

### 2. Cài thư viện
```bash
pip install -r requirements.txt
```

### 3. Kiểm tra hệ thống
```bash
python setup_phase1.py
```

---

## Cách sử dụng trong code

```python
from agent_core import MemoryManager, KnowledgeBase, ContextBuilder

# Khởi tạo
mem = MemoryManager()                   # Bộ nhớ động (Mem0)
kb = KnowledgeBase(); kb.load()         # Tri thức tĩnh (RAG từ ./docs)
ctx = ContextBuilder(mem, kb)           # Bộ xây System Prompt

# Khi user gửi tin nhắn:
user_query = "Tôi muốn cấu hình database cho dự án mới"
system_prompt = ctx.build(user_query)   # Lấy context từ Mem0 + RAG
# → Dùng system_prompt này khi gọi LLM

# Khi user chia sẻ thông tin mới:
mem.add("User thích dùng PostgreSQL thay vì SQLite cho production")
```

---

## Tiết kiệm token: Dùng session_reset.py

Cứ sau 30-45 phút làm việc hoặc khi xong một task:
```bash
python session_reset.py
```
Đóng cửa sổ chat cũ → mở chat mới → paste câu lệnh trong `./scratch/session_checkpoint.md`.

---

## Thêm tài liệu vào RAG

1. Chép file `.md`, `.html`, `.json`, hoặc `.txt` vào thư mục `./docs/`
2. Chạy lại `kb.reload()` trong code hoặc restart chương trình
