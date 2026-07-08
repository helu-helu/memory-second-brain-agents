"""
setup_phase1.py
Script kiểm tra và xác nhận toàn bộ hệ thống Phase 1 hoạt động.
Chạy: python setup_phase1.py
"""

import os, sys


def step(n, total, label):
    print(f"\n[{n}/{total}] {label}...")


def check_env():
    step(1, 5, "Kiểm tra GEMINI_API_KEY")
    from dotenv import load_dotenv
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY", "")
    if not key or "your_gemini" in key:
        print("  ❌ Chưa cấu hình GEMINI_API_KEY")
        print("  → Sao chép .env.example thành .env rồi điền key vào")
        print("  → Lấy key miễn phí: https://aistudio.google.com/app/apikey")
        return False
    print(f"  ✅ Key đã cấu hình ({key[:8]}...)")
    return True


def check_libs():
    step(2, 5, "Kiểm tra thư viện Python")
    libs = {
        "mem0ai": "mem0",
        "llama_index": "llama_index.core",
        "qdrant_client": "qdrant_client",
        "dotenv": "dotenv",
    }
    import importlib
    missing = [pkg for pkg, mod in libs.items() if importlib.util.find_spec(mod) is None]
    if missing:
        print(f"  ❌ Chưa cài: {', '.join(missing)}")
        print("  → Chạy: pip install -r requirements.txt")
        return False
    print("  ✅ Tất cả thư viện đã sẵn sàng")
    return True


def check_dirs():
    step(3, 5, "Kiểm tra cấu trúc thư mục")
    for d in ["./docs", "./db", "./scratch", "./agent_core"]:
        os.makedirs(d, exist_ok=True)
    print("  ✅ Các thư mục: docs/, db/, scratch/, agent_core/")

    # Tạo file mẫu nếu docs/ trống
    docs = [f for f in os.listdir("./docs")
            if f.endswith((".md", ".html", ".json", ".txt"))]
    if not docs:
        sample = "./docs/00_coding_preferences.md"
        with open(sample, "w", encoding="utf-8") as f:
            f.write("""# Quy Chuẩn & Sở Thích Lập Trình

## Ngôn ngữ & phong cách
- Ngôn ngữ chính: Python 3.11+
- Luôn viết async/await cho các tác vụ I/O
- Xử lý ngoại lệ bằng try/except, không để raise thô

## Database & Cấu hình
- Vector DB: Qdrant (local path ./db/qdrant_mem0)
- History DB: SQLite (./db/mem0_history.db)
- Cổng mặc định khi chạy local: 8000

## Cấu trúc thư mục dự án
- Tài liệu: ./docs/
- Database cục bộ: ./db/
- File tạm: ./scratch/
""")
        print(f"  📄 Đã tạo file mẫu: {sample}")
    else:
        print(f"  📄 docs/ có sẵn {len(docs)} file: {docs[:3]}")
    return True


def check_memory():
    step(4, 5, "Kiểm tra Mem0 (ghi + tìm kiếm)")
    try:
        from agent_core.memory import MemoryManager
        mem = MemoryManager(user_id="setup_test")
        test = "Người dùng thích viết code Python async và chạy database trên cổng 8000"
        ok = mem.add(test)
        if not ok:
            print("  ❌ Không ghi được vào Mem0")
            return False
        results = mem.search("coding style database port", limit=3)
        if results:
            print(f"  ✅ Mem0 OK — tìm thấy {len(results)} ký ức:")
            for r in results[:2]:
                fact = r.get("memory") or r.get("fact") or str(r)
                print(f"     · {fact[:80]}")
        else:
            print("  ⚠️  Mem0 ghi được nhưng chưa có kết quả search (thử lại)")
        return True
    except Exception as e:
        print(f"  ❌ Lỗi Mem0: {e}")
        return False


def check_knowledge():
    step(5, 5, "Kiểm tra RAG LlamaIndex (lập chỉ mục + tìm kiếm)")
    try:
        from agent_core.knowledge import KnowledgeBase
        kb = KnowledgeBase()
        ok = kb.load()
        if not ok:
            print("  ❌ Không lập chỉ mục được (docs/ trống hoặc lỗi)")
            return False
        result = kb.search("database port cấu hình", top_k=1)
        if "(Không tìm" in result or "(Lỗi" in result or "(chưa được" in result:
            print(f"  ⚠️  RAG: {result[:100]}")
        else:
            print("  ✅ RAG OK — kết quả tìm kiếm mẫu:")
            print(f"     {result[:150]}...")
        return True
    except Exception as e:
        print(f"  ❌ Lỗi RAG: {e}")
        return False


def report(results: dict):
    print("\n" + "=" * 55)
    print("  BÁO CÁO KIỂM TRA HỆ THỐNG PHASE 1")
    print("=" * 55)
    for name, passed in results.items():
        print(f"  {'✅' if passed else '❌'} {name}")
    print("=" * 55)
    if all(results.values()):
        print("  🎉 Hệ thống sẵn sàng!\n")
        print("  Bước tiếp theo:")
        print("  1. Chép tài liệu .md/.html/.json vào ./docs/")
        print("  2. Dùng agent_core trong code của bạn:")
        print("     from agent_core import MemoryManager, KnowledgeBase, ContextBuilder")
        print("  3. Chạy session_reset.py khi muốn chốt phiên để tiết kiệm token")
    else:
        print("  ⚠️  Xem chi tiết lỗi ở trên để khắc phục.")
    print("=" * 55)


if __name__ == "__main__":
    print("=" * 55)
    print("  SETUP PHASE 1: Mem0 + LlamaIndex RAG + Gemini Flash")
    print("=" * 55)

    results = {}
    if not check_env():
        results["Cấu hình .env (GEMINI_API_KEY)"] = False
        report(results); sys.exit(1)
    results["Cấu hình .env (GEMINI_API_KEY)"] = True

    if not check_libs():
        results["Thư viện Python (requirements.txt)"] = False
        report(results); sys.exit(1)
    results["Thư viện Python (requirements.txt)"] = True

    results["Cấu trúc thư mục & tài liệu mẫu"] = check_dirs()
    results["Mem0 (Bộ nhớ động)"] = check_memory()
    results["RAG LlamaIndex (Tri thức tĩnh)"] = check_knowledge()

    report(results)
