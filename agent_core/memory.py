"""
agent_core/memory.py
Wrapper for Mem0 using Gemini Flash as the LLM extractor.
Stores 100% locally: Vector DB (Qdrant local) + SQLite history.
Supports Mem0 v2.0+ filter syntax.
"""

import os
import yaml
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.yaml")
with open(config_path, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

MEM0_CONFIG = {
    "llm": {
        "provider": config["memory"]["llm"]["provider"],
        "config": {
            "model": config["memory"]["llm"]["model"],
            "api_key": os.getenv("GEMINI_API_KEY"),
            "temperature": config["memory"]["llm"]["temperature"],
        }
    },
    "embedder": {
        "provider": config["memory"]["embedder"]["provider"],
        "config": {
            "model": config["memory"]["embedder"]["model"]
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "collection_name": config["memory"]["qdrant"]["collection_name"],
            "host": config["memory"]["qdrant"]["host"],
            "port": config["memory"]["qdrant"]["port"],
            "embedding_model_dims": config["memory"]["qdrant"]["embedding_model_dims"]
        }
    },
    "history_db_path": config["memory"]["history_db_path"],
    "version": config["memory"]["version"]
}

if MEM0_CONFIG["embedder"]["provider"] != "huggingface":
    MEM0_CONFIG["embedder"]["config"]["api_key"] = os.getenv("GEMINI_API_KEY")


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

    def add(self, text: str, agent_id: Optional[str] = None,
            metadata: Optional[dict] = None) -> bool:
        """
        Record new facts/dialogue history. Mem0 automatically extracts facts.
        """
        try:
            self._get_client().add(
                text,
                user_id=self.user_id,
                agent_id=agent_id,
                metadata=metadata or {}
            )
            return True
        except Exception as e:
            print(f"[MemoryManager.add] Error: {e}")
            return False

    def search(self, query: str, limit: int = 5,
               agent_id: Optional[str] = None) -> list[dict]:
        """Search related memories using semantic retrieval with Mem0 v2.0+ filters."""
        try:
            filters = {"user_id": self.user_id}
            if agent_id:
                filters["agent_id"] = agent_id
                
            results = self._get_client().search(
                query, limit=limit, filters=filters
            )
            return results if isinstance(results, list) else results.get("results", [])
        except Exception as e:
            print(f"[MemoryManager.search] Error: {e}")
            return []

    def get_all(self, agent_id: Optional[str] = None) -> list[dict]:
        """Retrieve all stored memories for the user with Mem0 v2.0+ filters."""
        try:
            filters = {"user_id": self.user_id}
            if agent_id:
                filters["agent_id"] = agent_id
                
            results = self._get_client().get_all(
                filters=filters
            )
            return results if isinstance(results, list) else results.get("results", [])
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

    def format_for_prompt(self, memories: list[dict]) -> str:
        """Format list of memories into a bulleted string for the System Prompt."""
        if not memories:
            return "(No relevant memories found)"
        lines = [f"- {m.get('memory') or m.get('fact') or str(m)}" for m in memories]
        return "\n".join(lines)
