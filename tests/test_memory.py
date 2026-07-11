from agent_core.memory import MemoryManager

def test_add_memory(mock_mem0):
    """Test adding a memory correctly calls the underlying Mem0 client."""
    mem = MemoryManager(user_id="test_user")
    result = mem.add("I love apples", agent_id="agent123")
    
    assert result is True
    # The add method calls with text, user_id, agent_id, metadata
    mock_mem0.add.assert_called_once_with("I love apples", user_id="test_user", agent_id="agent123", metadata={})

def test_search_memory(mock_mem0):
    """Test searching memory returns the mock data."""
    mem = MemoryManager(user_id="test_user")
    results = mem.search("what do I love?", agent_id="agent123")
    
    assert len(results) == 2
    assert results[0]["memory"] == "User prefers Python async coding."
    # The search method calls with limit=5, filters
    mock_mem0.search.assert_called_once_with("what do I love?", limit=5, filters={"user_id": "test_user"})

def test_format_for_prompt(mock_mem0):
    """Test formatting memory results into a string prompt."""
    mem = MemoryManager(user_id="test_user")
    mock_results = [
        {"memory": "User prefers Python async coding."},
        {"memory": "User runs their database on port 8000."}
    ]
    formatted = mem.format_for_prompt(mock_results)
    
    assert "- User prefers Python async coding." in formatted
    assert "- User runs their database on port 8000." in formatted
    assert "(No relevant memories found)" not in formatted

def test_format_for_prompt_empty(mock_mem0):
    """Test formatting when no memories are found."""
    mem = MemoryManager(user_id="test_user")
    formatted = mem.format_for_prompt([])
    
    assert "(No relevant memories found)" in formatted
