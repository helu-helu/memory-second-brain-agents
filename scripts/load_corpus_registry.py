"""Load and validate the corpus registry."""

from __future__ import annotations

import sys

import yaml

try:
    from scripts.route_query import REGISTRY, load_yaml
    from scripts.validate_second_brain import validate_registry
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import REGISTRY, load_yaml
    from validate_second_brain import validate_registry


def main() -> int:
    errors = validate_registry(REGISTRY)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(yaml.safe_dump(load_yaml(REGISTRY), sort_keys=False).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
