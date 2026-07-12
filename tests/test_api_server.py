import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from api.api_server import app, get_memory, get_knowledge, _memory_managers

client = TestClient(app)

headers = {"X-API-Key": "test_api_key"}

def test_memory_managers_are_isolated_by_user():
    _memory_managers.clear()
    alice = get_memory("alice")
    bob = get_memory("bob")

    assert alice is get_memory("alice")
    assert alice is not bob
    assert alice.user_id == "alice"
    assert bob.user_id == "bob"

def test_add_memory_auth_failure():
    response = client.post("/memory/add", json={"text": "test memory"})
    assert response.status_code == 403

def test_add_memory_success(mocker):
    mock_mem = MagicMock()
    mock_mem.add.return_value = True
    get_memory = mocker.patch("api.api_server.get_memory", return_value=mock_mem)
    
    response = client.post(
        "/memory/add", 
        json={"text": "I love testing", "user_id": "alice"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["success"] is True
    get_memory.assert_called_once_with("alice")

def test_search_memory_success(mocker):
    mock_mem = MagicMock()
    mock_mem.search.return_value = [{"memory": "User prefers Python async coding."}]
    mock_mem.format_for_prompt.return_value = "- User prefers Python async coding."
    get_memory = mocker.patch("api.api_server.get_memory", return_value=mock_mem)
    
    response = client.get(
        "/memory/search?q=what do I prefer?&user_id=alice",
        headers=headers
    )
    assert response.status_code == 200
    assert "- User prefers Python async coding." in response.json()["result"]
    get_memory.assert_called_once_with("alice")

def test_search_knowledge_success(mocker):
    mock_kb = MagicMock()
    mock_kb.search.return_value = "[Source: test.txt] Mock content"
    mocker.patch("api.api_server.get_knowledge", return_value=mock_kb)
    
    response = client.get(
        "/rag/search?q=test file",
        headers=headers
    )
    assert response.status_code == 200
    assert "[Source: test.txt]" in response.json()["result"]
