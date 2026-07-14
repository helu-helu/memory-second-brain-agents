# Contract: Import And Entrypoint Compatibility

## Public Import Contract

The following imports must continue to work during feature 014:

```python
from agent_core import MemoryManager, KnowledgeBase, ContextBuilder
from agent_core.memory import MemoryManager
from agent_core.knowledge import KnowledgeBase
from agent_core.context_builder import ContextBuilder
from agent_core.access_tools import (
    build_active_memory_pack,
    build_agent_bootstrap,
    build_docs_context_pack,
    inspect_corpus_status,
    inspect_second_brain_status,
    list_corpora,
    record_agent_handoff,
    route_docs_query,
)
```

## Stable Adapter Contract

The following surfaces must not be renamed in feature 014:

- `api/api_server.py`
- `second_brain_mcp.py`
- Existing REST route names
- Existing MCP tool names
- Existing script paths under `scripts/`
- Existing `second-brain/` and `db/` paths

## Shim Contract

Every moved module must provide a compatibility path until a future feature removes it with evidence.

Expected shim behavior:

- Importing the legacy module succeeds.
- Existing public symbols are re-exported.
- Internal imports may use the new implementation path.
- Tests verify both legacy and new import paths where practical.

## Validation Contract

Validation must include:

- Import compatibility tests for public exports.
- Focused tests for moved module behavior.
- API server import/start smoke.
- MCP import smoke.
- Runtime-backed context-pack representative test.

Full official-docs corpus scans are explicitly out of scope for this contract.
