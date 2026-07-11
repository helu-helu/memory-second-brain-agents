import os
import sys
import pytest
from unittest.mock import MagicMock

# Ensure the project root is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Set test environment variables
os.environ["APP_API_KEY"] = "test_api_key"
os.environ["GEMINI_API_KEY"] = "test_gemini_key"
os.environ["MEM0_USER_ID"] = "test_user"

@pytest.fixture
def mock_mem0(mocker):
    """Mocks the mem0.Memory class to avoid real API/DB calls."""
    mock_memory_class = mocker.patch("mem0.Memory", autospec=True)
    mock_instance = MagicMock()
    mock_memory_class.from_config.return_value = mock_instance
    
    # Setup default return values
    mock_instance.search.return_value = [
        {"memory": "User prefers Python async coding.", "id": "1"},
        {"memory": "User runs their database on port 8000.", "id": "2"}
    ]
    mock_instance.add.return_value = True
    
    return mock_instance

@pytest.fixture
def mock_qdrant(mocker):
    """Mocks QdrantClient used in KnowledgeBase."""
    mock_qdrant_class = mocker.patch("qdrant_client.QdrantClient", autospec=True)
    mock_instance = MagicMock()
    mock_qdrant_class.return_value = mock_instance
    return mock_instance

@pytest.fixture
def mock_llama_settings(mocker):
    """Mocks LlamaIndex Settings to avoid loading heavy models."""
    mocker.patch("llama_index.core.Settings.embed_model")
    mocker.patch("llama_index.core.Settings.llm")
