from pathlib import Path

import yaml

from scripts.route_query import route


ROOT = Path(__file__).resolve().parents[1]


def test_unity_query_fixtures_route_to_project_bound_corpus():
    fixture = yaml.safe_load((ROOT / "tests" / "fixtures" / "unity_queries.yaml").read_text(encoding="utf-8"))
    for item in fixture["queries"]:
        result = route(item["query"])
        assert result["detected_product"] == item["expected_product"]
        assert result["selected_corpora"] == [item["expected_corpus"]]
