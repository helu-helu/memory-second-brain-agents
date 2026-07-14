import pytest
import asyncio
import httpx
from unittest.mock import MagicMock

from api.api_server import app, get_memory, get_knowledge, _memory_managers

headers = {"X-API-Key": "test_api_key"}


async def _request(method: str, url: str, **kwargs):
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        return await client.request(method, url, **kwargs)


def request(method: str, url: str, **kwargs):
    return asyncio.run(_request(method, url, **kwargs))

def test_memory_managers_are_isolated_by_user():
    _memory_managers.clear()
    alice = get_memory("alice")
    bob = get_memory("bob")

    assert alice is get_memory("alice")
    assert alice is not bob
    assert alice.user_id == "alice"
    assert bob.user_id == "bob"

def test_add_memory_auth_failure():
    response = request("POST", "/memory/add", json={"text": "test memory"})
    assert response.status_code == 403

def test_add_memory_success(mocker):
    mock_mem = MagicMock()
    mock_mem.add.return_value = True
    get_memory = mocker.patch("api.api_server.get_memory", return_value=mock_mem)
    
    response = request(
        "POST",
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
    
    response = request(
        "GET",
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
    
    response = request(
        "GET",
        "/rag/search?q=test file",
        headers=headers
    )
    assert response.status_code == 200
    assert "[Source: test.txt]" in response.json()["result"]


def test_second_brain_list_corpora():
    response = request("GET", "/second-brain/corpora", headers=headers)
    assert response.status_code == 200
    assert response.json()["ok"] is True
    assert any(item["corpus_id"] == "unity-6.3" for item in response.json()["data"])


def test_second_brain_route_query():
    response = request("GET", "/second-brain/route?q=How do I use the Unity Input System?", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["selected_corpora"] == ["unity-6.3"]


def test_second_brain_context_pack():
    response = request(
        "POST",
        "/second-brain/context-pack",
        json={"query": "How do I use the Unity Input System?", "limit": 2, "out": "second-brain/demo/runs/api-context-pack.md"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["data"]["applied_sources"] <= 2


def test_second_brain_corpus_status():
    response = request("GET", "/second-brain/corpora/codex-docs/status", headers=headers)
    assert response.status_code == 200
    assert response.json()["data"]["ready_for_retrieval"] is False


def test_second_brain_memory_pack():
    response = request(
        "POST",
        "/second-brain/memory-pack",
        json={"query": "Unity Input System", "limit": 2, "out": "second-brain/memory/packs/api-memory-pack.md"},
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["data"]["applied_items"] <= 2


def test_second_brain_status():
    response = request("GET", "/second-brain/status", headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert "memory" in data
    assert "reviews" in data
    assert "corpora" in data
