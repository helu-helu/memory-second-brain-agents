"""Crawl an approved docs crawl plan into a local HTML snapshot."""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

import yaml

try:
    from scripts.route_query import ROOT
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from route_query import ROOT


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for name, value in attrs:
            if name == "href" and value:
                self.links.append(value)


def load_plan(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT)).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def normalize_url(base_url: str, href: str | None = None) -> str:
    url = urljoin(base_url, href or "")
    url, _fragment = urldefrag(url)
    parsed = urlparse(url)
    path = parsed.path or "/"
    return parsed._replace(path=path, query="").geturl()


def allowed(url: str, domains: list[str]) -> bool:
    return urlparse(url).scheme in {"http", "https"} and urlparse(url).netloc in domains


def output_file(output_root: Path, url: str) -> Path:
    parsed = urlparse(url)
    clean_path = parsed.path.strip("/") or "index.html"
    if clean_path.endswith("/"):
        clean_path += "index.html"
    if "." not in Path(clean_path).name:
        clean_path = str(Path(clean_path) / "index.html")
    safe = re.sub(r"[^A-Za-z0-9._/ -]", "_", clean_path).replace(" ", "-")
    return output_root / safe


def extract_links(html: str, base_url: str) -> list[str]:
    parser = LinkParser()
    parser.feed(html)
    return [normalize_url(base_url, href) for href in parser.links]


def fetch(url: str) -> tuple[int, str, str]:
    request = Request(url, headers={"User-Agent": "second-brain-docs-crawler/0.1"})
    with urlopen(request, timeout=10) as response:
        content_type = response.headers.get("content-type", "")
        body = response.read().decode("utf-8", errors="replace")
        return response.status, content_type, body


def crawl(plan: dict, *, dry_run: bool = False) -> dict:
    if plan.get("approval_status") != "approved" and not dry_run:
        raise ValueError("crawl plan must be approved unless --dry-run is used")

    output_root = ROOT / plan["output_path"]
    max_pages = int(plan.get("max_pages", 100))
    allowed_domains = plan.get("allowed_domains", [])
    pending = deque(normalize_url(url) for url in plan.get("start_urls", []))
    seen: set[str] = set()
    fetched = []
    skipped = []
    warnings = []

    while pending and len(fetched) < max_pages:
        url = pending.popleft()
        if url in seen:
            skipped.append({"url": url, "reason": "duplicate"})
            continue
        seen.add(url)

        if not allowed(url, allowed_domains):
            skipped.append({"url": url, "reason": "off_domain"})
            continue
        if dry_run:
            fetched.append({"url": url, "status_code": 0, "path": "", "content_type": "dry-run"})
            continue

        try:
            status, content_type, body = fetch(url)
        except Exception as exc:
            skipped.append({"url": url, "reason": "fetch_error", "error": str(exc)})
            continue

        target = output_file(output_root, url)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        fetched.append(
            {
                "url": url,
                "status_code": status,
                "path": display_path(target),
                "content_type": content_type,
            }
        )

        if "html" in content_type.lower() or target.suffix.lower() in {".html", ".htm"}:
            for link in extract_links(body, url):
                if link not in seen:
                    pending.append(link)

    if pending:
        warnings.append(f"max_pages reached with {len(pending)} URLs still pending")
        for url in pending:
            skipped.append({"url": url, "reason": "max_pages"})

    status = "dry_run" if dry_run else "completed"
    return {
        "run_id": f"{plan['plan_id']}-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
        "plan_id": plan["plan_id"],
        "corpus_id": plan["corpus_id"],
        "started_at": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "output_path": plan["output_path"],
        "markdown_output_path": str(Path(plan["output_path"]).with_name(Path(plan["output_path"]).name + "-markdown")).replace("\\", "/"),
        "fetched": fetched,
        "skipped": skipped,
        "warnings": warnings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    plan_path = args.plan if args.plan.is_absolute() else ROOT / args.plan
    run = crawl(load_plan(plan_path), dry_run=args.dry_run)
    output = yaml.safe_dump(run, sort_keys=False)
    if args.out:
        out = args.out if args.out.is_absolute() else ROOT / args.out
    else:
        out = ROOT / "second-brain" / "corpora" / "acquisitions" / f"{run['run_id']}.yaml"
    if not args.dry_run or args.out:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(output, encoding="utf-8")
    print(output.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
