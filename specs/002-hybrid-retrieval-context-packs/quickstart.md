# Quickstart: Validate Hybrid Retrieval Context Packs

## Scenario 1: Generate a Unity Context Pack

```bash
python scripts/build_context_pack.py "How do I use the Unity Input System?" --limit 8 --out second-brain/demo/runs/hybrid-unity-input.md
```

Expected result:

- Selected corpus is `unity-6.3`.
- Excluded corpus includes `unity-6.5`.
- Top sources include Input-related Unity docs.
- Applied sources do not exceed 8.

## Scenario 2: Generate a Missing-Corpus Pack

```bash
python scripts/build_context_pack.py "How should Codex skills use MCP?" --limit 5 --out second-brain/demo/runs/hybrid-codex-mcp.md
```

Expected result:

- Selected corpus is `codex-docs`.
- Pack reports no local root path or degraded/no-source warning.

## Scenario 3: Run Retrieval Eval

```bash
python scripts/evaluate_retrieval.py tests/fixtures/retrieval_eval.yaml
```

Expected result:

- Eval prints pass/fail per case.
- Process exits non-zero if any required case fails.

## Scenario 4: Run Tests

```bash
.venv\Scripts\python.exe -m pytest -q
```

Expected result:

- Full test suite passes.
