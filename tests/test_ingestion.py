from pathlib import Path

from scripts.build_massive_index import Manifest, file_digest, get_all_valid_files


def test_manifest_tracks_content_hash_and_points(tmp_path):
    source = tmp_path / "doc.md"
    source.write_text("Unity document", encoding="utf-8")
    digest = file_digest(source)
    manifest = Manifest(tmp_path / "manifest.sqlite")

    manifest.put("unity", "doc.md", digest, ["point-1"])

    assert manifest.get("unity", "doc.md") == (digest, ["point-1"])
    assert manifest.entries("unity") == [("doc.md", ["point-1"])]
    manifest.remove("unity", "doc.md")
    assert manifest.get("unity", "doc.md") is None
    manifest.close()


def test_file_scan_is_recursive_and_filtered(tmp_path):
    nested = tmp_path / "nested"
    nested.mkdir()
    (nested / "guide.md").write_text("guide", encoding="utf-8")
    (nested / "ignore.png").write_bytes(b"png")

    files = get_all_valid_files(tmp_path)

    assert files == [str(nested / "guide.md")]
