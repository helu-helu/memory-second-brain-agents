"""
agent_core/memory.py
Wrapper for Mem0 using Gemini Flash as the LLM extractor.
Stores 100% locally: Vector DB (Qdrant local) + SQLite history.
Supports Mem0 v2.0+ filter syntax.
"""

import os
from typing import Optional
from dotenv import load_dotenv

from agent_core.config import MEM0_CONFIG

load_dotenv()


class MemoryManager:
    """
    Manages long-term personal agent memory.
    
    Usage:
        mem = MemoryManager()
        mem.add("I prefer Python async coding")
        facts = mem.search("coding style")
    """

    def __init__(self, user_id: str = None):
        self.user_id = user_id or os.getenv("MEM0_USER_ID", "personal_user")
        self._client = None

    def _get_client(self):
        if self._client is None:
            from mem0 import Memory
            os.makedirs("./db/qdrant_mem0", exist_ok=True)
            os.makedirs("./db", exist_ok=True)
            self._client = Memory.from_config(MEM0_CONFIG)
        return self._client

    def add(self, text: str,
            metadata: Optional[dict] = None) -> bool:
        """
        Record new facts/dialogue history. Mem0 automatically extracts facts.
        """
        try:
            self._get_client().add(
                text,
                user_id=self.user_id,
                metadata=metadata or {}
            )
            return True
        except Exception as e:
            print(f"[MemoryManager.add] Error: {e}")
            return False

    def search(self, query: str, limit: int = 5) -> list[dict]:
        """Search related memories using semantic retrieval with Mem0 v2.0+ filters."""
        try:
            filters = {"user_id": self.user_id}
            
            results = self._get_client().search(
                query=query,
                limit=limit,
                filters=filters
            )
            return results
        except Exception as e:
            print(f"[MemoryManager.search] Error: {e}")
            return []

    def get_all(self) -> list[dict]:
        """Retrieve all facts across the user."""
        try:
            filters = {"user_id": self.user_id}
            
            results = self._get_client().get_all(filters=filters)
            return results
        except Exception as e:
            print(f"[MemoryManager.get_all] Error: {e}")
            return []

    def delete_all(self) -> bool:
        """Clear all stored memories for the user."""
        try:
            self._get_client().delete_all(user_id=self.user_id)
            return True
        except Exception as e:
            print(f"[MemoryManager.delete_all] Error: {e}")
            return False

    def add_execution_log(self, task_id: str, skill: str, success_rate: str) -> bool:
        """
        Record the execution result of a specific skill for capability tracking.
        (Layer 3 of Capability-Based Architecture)
        """
        log_text = f"Execution Log - Task: {task_id} | Skill: {skill} | Result: {success_rate}"
        metadata = {
            "type": "execution_log",
            "task_id": task_id,
            "skill": skill,
            "success_rate": success_rate
        }
        return self.add(log_text, agent_id="evals_system", metadata=metadata)

    def format_for_prompt(self, memories: list[dict]) -> str:
        """Format list of memories into a bulleted string for the System Prompt."""
        if not memories:
            return "(No relevant memories found)"
        lines = [f"- {m.get('memory') or m.get('fact') or str(m)}" for m in memories]
        return "\n".join(lines)
