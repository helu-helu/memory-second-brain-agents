# Quickstart: Physical Runtime Restructure Validation

## Preconditions

- Work from the repository root.
- Do not restore the deleted root `README.md` as the architecture source of truth.
- Do not move `second-brain/` or `db/`.
- Use small representative tests by default.

## Baseline Checks

```powershell
pytest tests/test_memory.py tests/test_knowledge.py tests/test_context_contract.py
pytest tests/test_runtime_context_pack.py tests/test_mcp_runtime_smoke.py
```

## Import Compatibility Smoke

```powershell
python -c "from agent_core import MemoryManager, KnowledgeBase, ContextBuilder; print('ok')"
python -c "from agent_core.memory import MemoryManager; from agent_core.knowledge import KnowledgeBase; from agent_core.context_builder import ContextBuilder; print('ok')"
python -c "import second_brain_mcp; print('ok')"
```

## After Each Migration Step

Run the focused checks for the moved module family:

```powershell
pytest tests/test_knowledge.py
pytest tests/test_context_contract.py tests/test_runtime_context_pack.py
pytest tests/test_access_tools.py
pytest tests/test_api_server.py tests/test_mcp_runtime_smoke.py
```

Only run the full suite after focused checks pass:

```powershell
pytest
```

## Expected Outcome

- Public imports still resolve.
- API and MCP entrypoints still import.
- Context-pack behavior remains runtime-backed.
- No storage path, route name, or MCP tool name changes.
- No full official-docs corpus scan is needed.
