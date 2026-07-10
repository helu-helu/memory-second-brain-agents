from unittest.mock import MagicMock
from agent_core.knowledge import KnowledgeBase

def test_load_skip_empty_directory(mock_qdrant, mocker, tmp_path):
    """Test loading a directory skips if it's empty."""
    mocker.patch("agent_core.knowledge.KnowledgeBase._setup_settings")
    empty_dir = tmp_path / "empty_docs"
    empty_dir.mkdir()
    
    kb = KnowledgeBase()
    mocker.patch("agent_core.knowledge.DOCS_DIR", str(empty_dir))
    # Should return False because there's no data
    assert kb.load() is False

def test_search_knowledge(mock_qdrant, mocker):
    """Test searching the knowledge base returns properly formatted string."""
    mocker.patch("agent_core.knowledge.KnowledgeBase._setup_settings")
    mock_hyde_cls = mocker.patch("llama_index.core.indices.query.query_transform.HyDEQueryTransform")
    mock_bundle = MagicMock()
    mock_bundle.custom_embedding_strs = ["mock"]
    mock_hyde_cls.return_value.return_value = mock_bundle

    kb = KnowledgeBase()
    
    mock_index = MagicMock()
    mock_retriever = MagicMock()
    mock_index.as_retriever.return_value = mock_retriever
    
    # Mock Node response
    mock_node = MagicMock()
    mock_node.get_content.return_value = "This is a mock document about python."
    mock_node.metadata = {"file_name": "python_guide.txt"}
    
    # Setup response
    mock_retriever.retrieve.return_value = [mock_node]
    
    # We need to manually initialize _index and _ready for testing
    kb._index = mock_index
    kb._ready = True

    result = kb.search("mock query python")
    
    # Verify the formatting
    assert "[Source: python_guide.txt]" in result
    assert "This is a mock document about python." in result
    
    # Verify engine was called
    mock_retriever.retrieve.assert_called_once_with(mock_bundle)

def test_search_knowledge_empty(mock_qdrant, mocker):
    """Test searching returns not found when empty."""
    mocker.patch("agent_core.knowledge.KnowledgeBase._setup_settings")
    mock_hyde_cls = mocker.patch("llama_index.core.indices.query.query_transform.HyDEQueryTransform")
    mock_bundle = MagicMock()
    mock_bundle.custom_embedding_strs = ["mock"]
    mock_hyde_cls.return_value.return_value = mock_bundle

    kb = KnowledgeBase()
    
    mock_index = MagicMock()
    mock_index.as_retriever.return_value.retrieve.return_value = []
    
    kb._index = mock_index
    kb._ready = True

    result = kb.search("unknown")
    assert "(No matching documentation found)" in result
