"""Append a corpus record to the file-first registry."""

from __future__ import annotations

import argparse
import sys

import yaml

try:
    from scripts.route_query import REGISTRY, load_yaml
    from scripts.validate_second_brain import validate_registry
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import REGISTRY, load_yaml
    from validate_second_brain import validate_registry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-id", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--vendor", required=True)
    parser.add_argument("--product", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--authority-level", default="official")
    parser.add_argument("--mutability", default="refreshable")
    parser.add_argument("--update-policy", default="refreshable_snapshot")
    parser.add_argument("--refresh-cadence", default="manual")
    parser.add_argument("--acquisition", default="manual")
    parser.add_argument("--status", default="planned")
    parser.add_argument("--snapshot-date")
    parser.add_argument("--root-path")
    args = parser.parse_args()

    registry = load_yaml(REGISTRY)
    corpora = registry.setdefault("corpora", [])
    if any(item.get("corpus_id") == args.corpus_id for item in corpora):
        print(f"{args.corpus_id}: already registered", file=sys.stderr)
        return 1

    corpora.append(
        {
            "corpus_id": args.corpus_id,
            "category": args.category,
            "vendor": args.vendor,
            "product": args.product,
            "version": args.version,
            "authority_level": args.authority_level,
            "mutability": args.mutability,
            "update_policy": args.update_policy,
            "snapshot_date": args.snapshot_date,
            "refresh_cadence": args.refresh_cadence,
            "root_path": args.root_path,
            "acquisition": args.acquisition,
            "status": args.status,
        }
    )

    REGISTRY.write_text(yaml.safe_dump(registry, sort_keys=False), encoding="utf-8")
    errors = validate_registry(REGISTRY)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"registered {args.corpus_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
