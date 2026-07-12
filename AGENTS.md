# Repository Guidelines

## Project Structure & Module Organization

Core Python code lives in `agent_core/`: `memory.py` wraps Mem0, `knowledge.py` manages LlamaIndex/Qdrant retrieval, and `context_builder.py` combines both sources. The FastAPI service is `api/api_server.py`; `second_brain_mcp.py` is the lightweight MCP bridge, while `dashboard.py` provides the Streamlit UI. Maintenance and ingestion utilities live in `scripts/`. Tests are under `tests/` and mirror the main modules. `docs/` contains raw source material for ingestion; do not bulk-read, reformat, or commit generated derivatives from it. Qdrant runs through `compose.yaml`, with runtime databases and manifests under ignored `db/` paths.

## Build, Test, and Development Commands

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Common commands:

```powershell
docker compose up -d qdrant              # start persistent Qdrant
python api\api_server.py                  # run the FastAPI backend
streamlit run dashboard.py               # launch the administration UI
python second_brain_mcp.py                # run the MCP stdio bridge
python -m pytest -q                       # execute the test suite
python scripts\build_massive_index.py docs\massive --dry-run
```

Use `--limit 1000 --collection unity_benchmark` before a full ingestion run.

## Coding Style & Naming Conventions

Follow PEP 8 with four-space indentation. Use `snake_case` for functions, variables, modules, API parameters, and test names; use `PascalCase` for classes. Keep provider and model names as separate configuration fields. Memory boundaries use `user_id` only—do not reintroduce `agent_id`. Prefer small functions, explicit errors, and standard-library solutions over new dependencies. No formatter is enforced, so keep diffs focused and run `python -m compileall -q agent_core api scripts tests` before submission.

## Testing Guidelines

Pytest discovers only `tests/` via `pytest.ini`. Name files `test_*.py` and tests `test_<behavior>`. Mock Mem0, external model APIs, and Qdrant unless the test explicitly uses a temporary local store. Add regression coverage for API contracts, user isolation, ingestion resume, and deletion behavior.

## Commit & Pull Request Guidelines

History follows concise Conventional Commit-style subjects such as `feat:`, `fix:`, and `chore:`. Keep commits single-purpose and imperative. Pull requests should explain behavior changes, list verification commands, call out configuration or migration effects, and include screenshots only for dashboard changes. Never commit `.env`, API keys, `db/`, raw `docs/`, or model artifacts.
