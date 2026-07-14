# Quickstart: MCP Post-Restructure Validation

## Fast Contract Checks

```powershell
pytest tests/test_import_compatibility.py tests/test_mcp_runtime_smoke.py -q
```

Expected:

- MCP entrypoint imports.
- Mocked runtime smoke passes.
- Context pack remains runtime-backed.

## Representative Query

Use this query when running a manual MCP/API validation:

```text
I want to create a separate camera for each user in a Unity 6.3 multiplayer game.
```

Expected:

- Route selects Unity 6.3 or reports a clear clarification/degraded warning.
- Unified context returns bounded memory and knowledge sections.
- Context pack uses runtime mode.

## Full Suite Gate

Only after fast checks pass:

```powershell
pytest -q
```

Do not run full official documentation corpus scans for this feature.
