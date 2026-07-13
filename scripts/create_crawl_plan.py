"""Create a crawl/download policy file without crawling."""

from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

import yaml

try:
    from scripts.route_query import ROOT
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import ROOT


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def build_plan(args: argparse.Namespace) -> dict:
    domains = args.domain
    for url in args.url:
        host = urlparse(url).netloc
        if host and host not in domains:
            raise ValueError(f"{url}: domain {host} is not in allowed domains")
    return {
        "plan_id": args.plan_id,
        "corpus_id": args.corpus_id,
        "start_urls": args.url,
        "allowed_domains": domains,
        "output_path": args.output,
        "snapshot_policy": args.snapshot_policy,
        "rate_limit": {"requests_per_minute": args.requests_per_minute},
        "max_pages": args.max_pages,
        "approval_status": args.approval_status,
        "notes": args.notes or "",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan-id", required=True)
    parser.add_argument("--corpus-id", required=True)
    parser.add_argument("--url", action="append", required=True)
    parser.add_argument("--domain", action="append", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--snapshot-policy", choices=["fixed_snapshot", "refreshable_snapshot"], default="refreshable_snapshot")
    parser.add_argument("--requests-per-minute", type=int, default=30)
    parser.add_argument("--max-pages", type=int, default=500)
    parser.add_argument("--approval-status", choices=["draft", "approved", "rejected"], default="draft")
    parser.add_argument("--notes")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    plan = build_plan(args)
    out = args.out or ROOT / "second-brain" / "corpora" / "crawl-plans" / f"{args.corpus_id}.yaml"
    if not out.is_absolute():
        out = ROOT / out
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(plan, sort_keys=False), encoding="utf-8")
    print(display_path(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
