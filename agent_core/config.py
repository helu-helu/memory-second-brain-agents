import os
import yaml
from dotenv import load_dotenv

# Đọc file .env một lần duy nhất
load_dotenv()

# Tính toán đường dẫn tới config.yaml (luôn nằm ở thư mục gốc của project)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT_DIR, "config.yaml")

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Export các biến dùng chung cho RAG (KnowledgeBase)
DOCS_DIR = os.path.join(ROOT_DIR, config["rag"]["docs_dir"].replace("./", ""))
QDRANT_PATH = os.path.join(ROOT_DIR, config["rag"]["db_path"].replace("./", ""))
COLLECTION_NAME = config["rag"]["collection_name"]

# Export cấu hình cho Mem0 (MemoryManager)
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
            "path": os.path.join(ROOT_DIR, config["memory"]["qdrant"]["path"].replace("./", "")),
            "embedding_model_dims": config["memory"]["qdrant"]["embedding_model_dims"]
        }
    },
    "history_db_path": os.path.join(ROOT_DIR, config["memory"]["history_db_path"].replace("./", "")),
    "version": config["memory"]["version"]
}

if MEM0_CONFIG["embedder"]["provider"] != "huggingface":
    MEM0_CONFIG["embedder"]["config"]["api_key"] = os.getenv("GEMINI_API_KEY")
