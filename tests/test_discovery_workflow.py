import csv
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import discover_repositories, detect_duplicates, validate_sources


class DiscoveryWorkflowTests(unittest.TestCase):
    def test_merges_case_insensitive_ids_and_preserves_review(self):
        existing = {"owner/repo": {"repository": "Owner/Repo", "discovery_queries": "q1", "screening_state": "REVIEW_RECORDED", "review_record": "research/repositories/reviews/owner__repo.md", "discovered_on": "2026-11-11"}}
        added, duplicate = discover_repositories.merge_hits(existing, [{"full_name": "owner/REPO"}, {"full_name": "new/ResearchTool"}], "q2", "2026-11-11")
        self.assertEqual((added, duplicate), (1, 1))
        self.assertEqual(existing["owner/repo"]["screening_state"], "REVIEW_RECORDED")
        self.assertEqual(existing["owner/repo"]["discovery_queries"], "q1 | q2")
        self.assertEqual(existing["new/researchtool"]["screening_state"], "UNTRIAGED")

    def test_records_api_incomplete_flag(self):
        def fake_fetch(query, page, per_page):
            return {"items": [{"full_name": "A/B"}], "total_count": 42, "incomplete_results": True}
        rows, log, incomplete = discover_repositories.discover(["phd"], {}, pages=2, per_page=10, fetcher=fake_fetch)
        self.assertTrue(incomplete)
        self.assertEqual(len(rows), 1)
        self.assertEqual(log[0]["status"], "ok")
        self.assertEqual(log[0]["api_total_count"], 42)

    def test_persist_roundtrip_and_duplicate_check(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "candidates.csv"
            data = {"x/y": {**dict.fromkeys(discover_repositories.COLUMNS, ""), "repository": "x/y", "screening_state": "UNTRIAGED", "discovered_on": "2026-11-11"}}
            discover_repositories.write_candidates(path, data)
            rows = discover_repositories.read_candidates(path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(detect_duplicates.detect(path)["canonical_duplicates"], [])

    def test_current_sources_structural_gate(self):
        errors, warnings, counts = validate_sources.audit()
        self.assertEqual(errors, [])
        self.assertGreaterEqual(counts["leads"], 15)
        self.assertGreaterEqual(counts["claims"], 17)
        self.assertGreater(counts["unrechecked"], 0)


if __name__ == "__main__":
    unittest.main()
