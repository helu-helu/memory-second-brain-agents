from __future__ import annotations

import functools
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import pytest
import yaml

from scripts.crawl_official_docs import crawl, load_plan, main as crawl_main, normalize_url


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture()
def local_site():
    site = ROOT / "tests" / "fixtures" / "crawl-site"
    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(site))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        thread.join(timeout=5)


def plan(base_url: str, tmp_path: Path, approval_status: str = "approved", max_pages: int = 10) -> dict:
    return {
        "plan_id": "crawl-local-docs",
        "corpus_id": "local-docs",
        "start_urls": [base_url],
        "allowed_domains": [base_url.split("/")[2]],
        "output_path": str(tmp_path / "snapshot").replace("\\", "/"),
        "snapshot_policy": "refreshable_snapshot",
        "rate_limit": {"requests_per_minute": 999},
        "max_pages": max_pages,
        "approval_status": approval_status,
        "notes": "local test only",
    }


def test_normalize_url_drops_fragments_and_queries():
    assert normalize_url("http://example.test/a?x=1#top") == "http://example.test/a"


def test_refuses_draft_plan_without_dry_run(local_site, tmp_path):
    with pytest.raises(ValueError):
        crawl(plan(local_site, tmp_path, approval_status="draft"))


def test_dry_run_allows_draft_plan(local_site, tmp_path):
    result = crawl(plan(local_site, tmp_path, approval_status="draft"), dry_run=True)
    assert result["status"] == "dry_run"
    assert result["fetched"]


def test_crawl_saves_allowed_pages_and_skips_off_domain(local_site, tmp_path):
    result = crawl(plan(local_site, tmp_path))
    paths = [item["path"] for item in result["fetched"]]
    skipped = {item["reason"] for item in result["skipped"]}
    assert any(path.endswith("index.html") for path in paths)
    assert any(path.endswith("guide.html") for path in paths)
    assert "off_domain" in skipped
    assert result["markdown_output_path"].endswith("-markdown")


def test_crawl_respects_max_pages(local_site, tmp_path):
    result = crawl(plan(local_site, tmp_path, max_pages=1))
    assert len(result["fetched"]) == 1
    assert result["warnings"]
    assert any(item["reason"] == "max_pages" for item in result["skipped"])


def test_crawl_main_writes_manifest(local_site, tmp_path, monkeypatch):
    plan_path = tmp_path / "plan.yaml"
    out = tmp_path / "run.yaml"
    plan_path.write_text(yaml.safe_dump(plan(local_site, tmp_path)), encoding="utf-8")
    monkeypatch.setattr("sys.argv", ["crawl_official_docs.py", str(plan_path), "--out", str(out)])
    assert crawl_main() == 0
    data = yaml.safe_load(out.read_text(encoding="utf-8"))
    assert data["status"] == "completed"
    assert data["fetched"]
