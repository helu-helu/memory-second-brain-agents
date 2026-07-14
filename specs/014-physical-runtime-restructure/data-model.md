# Data Model: Physical Runtime Restructure

## RuntimePackage

Represents a package under `agent_core/` that owns runtime behavior.

Fields:

- `name`: Package name such as `rag`, `context`, `access`, `memory`, or `mcp`.
- `owner_scope`: Runtime concern owned by the package.
- `status`: `planned`, `active`, `shimmed`, `deferred`, or `blocked`.
- `public_exports`: Symbols exposed for callers.
- `validation`: Focused tests or import smoke commands that prove the package works.

## CompatibilityShim

Represents a legacy import path that forwards to the new implementation path.

Fields:

- `legacy_path`: Existing import path.
- `replacement_path`: New implementation path.
- `symbols`: Public symbols that must remain available.
- `status`: `planned`, `active`, `deprecated`, or `removable-later`.
- `risk`: `low`, `medium`, or `high`.
- `removal_rule`: Evidence required before future deletion.

## AdapterEntrypoint

Represents an access surface that should remain stable while internals move.

Fields:

- `path`: Entrypoint path.
- `type`: `api`, `mcp`, `script`, or `package-export`.
- `stable_contract`: Route names, tool names, CLI arguments, or public imports that must not change.
- `runtime_dependency`: Package that should own the underlying behavior.
- `validation`: Smoke test or focused test proving the entrypoint still loads.

## FileFirstWorkspace

Represents a stable file workspace that should not move in this feature.

Fields:

- `path`: Workspace path.
- `artifact_classes`: Registry, review, memory, skill, audit, generated context pack, or handoff evidence.
- `status`: `stable`.
- `move_policy`: `do-not-move-in-feature-014`.

## MigrationStep

Represents one bounded move in the restructure.

Fields:

- `id`: Sequential step id.
- `scope`: Module family moved.
- `preconditions`: Tests or decisions required before the step.
- `actions`: File moves, shim creation, import updates, and docs updates.
- `validation`: Commands or tests required after the step.
- `rollback_policy`: Stop and leave shim/old path intact; do not delete behavior.
