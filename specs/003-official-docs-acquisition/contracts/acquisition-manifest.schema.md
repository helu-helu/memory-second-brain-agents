# Contract: Acquisition Manifest

Acquisition manifests are YAML files under:

```text
second-brain/corpora/acquisitions/
```

## Example

```yaml
manifest_id: acquisition-unity-6.3
corpus_id: unity-6.3
method: manual_import
authority_level: official
source: docs/massive/Unity_6_3_Markdown
product: Unity
version: "6.3"
snapshot_date: null
status: validated
file_counts:
  total: 39056
  supported: 39056
  unsupported: 0
warnings: []
ready_for_indexing: true
```

## Required Fields

- `manifest_id`
- `corpus_id`
- `method`
- `authority_level`
- `source`
- `product`
- `version`
- `status`
- `file_counts`
- `warnings`
- `ready_for_indexing`
