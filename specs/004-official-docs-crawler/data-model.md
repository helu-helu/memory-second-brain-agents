# Data Model: Official Docs Crawler

## CrawlRun

Represents one crawler execution.

**Fields**:

- `run_id`: stable id.
- `plan_id`: crawl plan id.
- `corpus_id`: target corpus.
- `started_at`: timestamp.
- `status`: dry_run, completed, failed, partial.
- `output_path`: snapshot output path.
- `fetched`: list of fetched page records.
- `skipped`: list of skipped URL records.
- `warnings`: crawl warnings.

## FetchedPage

Represents one saved HTML page.

**Fields**:

- `url`: source URL.
- `status_code`: HTTP response code.
- `path`: saved local file path.
- `content_type`: response content type when available.

## SkippedUrl

Represents one skipped URL.

**Fields**:

- `url`: skipped URL.
- `reason`: off_domain, duplicate, non_http, max_pages, fetch_error.

## CrawlFrontier

In-memory queue of normalized URLs.

**Fields**:

- `pending`: URLs to fetch.
- `seen`: normalized URLs already considered.
- `allowed_domains`: allowed hostnames.
