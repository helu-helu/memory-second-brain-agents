"""
agent_core/context_builder.py
Tự động xây dựng System Prompt bằng cách kết hợp:
  - Ký ức cá nhân từ Mem0
  - Tài liệu kỹ thuật liên quan từ RAG
Kết quả được chèn vào System Prompt trước mỗi lần gọi LLM.
"""

from agent_core.memory import MemoryManager
from agent_core.knowledge import KnowledgeBase

SYSTEM_PROMPT_TEMPLATE = """\
Bạn là một AI Agent cá nhân thông minh và hữu ích.

## Thông tin cá nhân & Sở thích đã ghi nhớ về người dùng:
{memories}

## Tài liệu kỹ thuật liên quan từ kho tri thức:
{knowledge}

---
Hãy sử dụng các thông tin trên để trả lời chính xác và phù hợp nhất với ngữ cảnh của người dùng.
Nếu thông tin từ tài liệu mâu thuẫn với sở thích cá nhân đã lưu, hãy ưu tiên sở thích cá nhân.
Trả lời ngắn gọn, tập trung vào điều người dùng đang cần.
"""


class ContextBuilder:
    """
    Kết hợp Mem0 + RAG để tạo System Prompt hoàn chỉnh trước mỗi lần gọi LLM.
    
    Cách dùng:
        mem = MemoryManager()
        kb = KnowledgeBase(); kb.load()
        ctx = ContextBuilder(mem, kb)
        system_prompt = ctx.build(user_query)
    """

    def __init__(self, memory: MemoryManager, knowledge: KnowledgeBase):
        self.memory = memory
        self.knowledge = knowledge


    async def build_async(self, user_query: str) -> str:
        """
        Tạo System Prompt hoàn chỉnh bằng cách chạy Song Song (Parallel)
        tìm kiếm trên cả RAG và Mem0. Tăng tốc độ gấp đôi.
        """
        import asyncio
        
        # Chạy 2 hàm search blocking trong các thread riêng biệt cùng lúc
        memories_task = asyncio.to_thread(self.memory.search, user_query, limit=5)
        knowledge_task = asyncio.to_thread(self.knowledge.search, user_query, top_k=3)
        
        memories, knowledge_text = await asyncio.gather(memories_task, knowledge_task)
        memory_text = self.memory.format_for_prompt(memories)

        return SYSTEM_PROMPT_TEMPLATE.format(
            memories=memory_text,
            knowledge=knowledge_text
        )

    def save_interaction(self, user_message: str, agent_response: str):
        """
        Lưu cuộc tương tác vào Mem0 để Agent học từ phản hồi.
        CHỈ gọi khi phát hiện user cung cấp thông tin cá nhân/sở thích mới.
        Không gọi sau mỗi câu chat thông thường (tốn token).
        """
        text = f"User: {user_message}\nAssistant: {agent_response}"
        self.memory.add(text)
