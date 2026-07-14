import second_brain_mcp


class FakeResponse:
    def __init__(self, data, status_code=200, text="OK"):
        self._data = data
        self.status_code = status_code
        self.text = text

    def json(self):
        return self._data


class FakeSession:
    def get(self, url, params=None):
        if url.endswith("/rag/search"):
            return FakeResponse({"result": "[Source: unity.md]\nUnity Input System docs"})
        if url.endswith("/memory/search"):
            return FakeResponse({"result": "- User prefers project-bound docs."})
        if url.endswith("/context/build"):
            return FakeResponse(
                {
                    "context": {
                        "trace_id": "ctx-mcp-smoke",
                        "query": params["q"],
                        "memory_hits": [{"id": "m1", "source": "mem0", "text": "Project-bound docs."}],
                        "knowledge_hits": [{"id": "k1", "source": "unity.md", "snippet": "Unity docs"}],
                        "warnings": [],
                    }
                }
            )
        if url.endswith("/second-brain/route"):
            return FakeResponse(
                {
                    "data": {
                        "query": params["q"],
                        "selected_corpora": ["unity-6.3"],
                        "excluded_corpora": ["unity-6.5"],
                    }
                }
            )
        return FakeResponse({}, status_code=404, text="not found")

    def post(self, url, json=None):
        if url.endswith("/second-brain/context-pack"):
            return FakeResponse(
                {
                    "ok": True,
                    "data": {
                        "path": "second-brain/demo/runs/runtime-context-pack.md",
                        "selected_corpora": ["unity-6.3"],
                        "applied_sources": json["limit"],
                        "retrieval_mode": json["mode"],
                    },
                    "warnings": [],
                    "error": None,
                }
            )
        return FakeResponse({}, status_code=404, text="not found")


def test_mocked_mcp_runtime_smoke(monkeypatch):
    monkeypatch.setattr(second_brain_mcp, "api_session", FakeSession())

    query = "I want to create a separate camera for each user in a Unity 6.3 multiplayer game."

    assert "unity-6.3" in second_brain_mcp.route_docs_query(query)
    assert "[Source: unity.md]" in second_brain_mcp.search_knowledge(query)
    assert "project-bound docs" in second_brain_mcp.search_memory("retrieval policy")
    assert "ctx-mcp-smoke" in second_brain_mcp.build_unified_context(query)
    pack = second_brain_mcp.build_docs_context_pack(query, limit=2, mode="runtime")
    assert "runtime-context-pack.md" in pack
    assert "'retrieval_mode': 'runtime'" in pack
