# Data Model: Official Docs Acquisition

## AcquisitionManifest

Describes how a corpus is obtained or planned.

**Fields**:

- `manifest_id`: stable id.
- `corpus_id`: linked corpus registry id.
- `method`: manual_import, download, crawl, generated.
- `authority_level`: official, vendor, community, internal, unknown.
- `source`: local path or URL.
- `product`: product name.
- `version`: product version or snapshot label.
- `snapshot_date`: date for refreshable snapshots.
- `status`: planned, dry_run, imported, validated, rejected.
- `file_counts`: total, supported, unsupported.
- `warnings`: validation warnings.
- `ready_for_indexing`: boolean.

## AcquisitionRun

One dry-run or execution record.

**Fields**:

- `run_id`: stable id.
- `manifest_id`: linked manifest.
- `created_at`: timestamp.
- `mode`: dry_run or execute.
- `inputs`: paths or URLs inspected.
- `outputs`: manifest/report files written.
- `status`: passed, failed, warning.
- `summary`: human-readable result.

## CrawlPlan

Planned official website crawl/download policy.

**Fields**:

- `plan_id`: stable id.
- `corpus_id`: target corpus.
- `start_urls`: official starting URLs.
- `allowed_domains`: approved domains.
- `output_path`: local snapshot destination.
- `snapshot_policy`: fixed_snapshot or refreshable_snapshot.
- `rate_limit`: requests or pages limit.
- `max_pages`: crawl ceiling.
- `approval_status`: draft, approved, rejected.
- `notes`: source-specific constraints.

## ImportValidationReport

Deterministic validation output for a local source folder.

**Fields**:

- `path`: local folder.
- `supported_extensions`: extensions counted as docs.
- `total_files`: total files scanned.
- `supported_files`: supported docs found.
- `unsupported_files`: unsupported files found.
- `warnings`: issues to review.
- `ready_for_indexing`: boolean.
