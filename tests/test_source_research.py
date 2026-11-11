import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class SourceResearchTests(unittest.TestCase):
    def _load(self, name):
        with (ROOT / "data" / name).open(newline="", encoding="utf-8") as stream:
            return list(csv.DictReader(stream))

    def test_only_deep_qualified_have_full_reviews(self):
        reviewed = self._load("repositories.csv")
        deep = [x for x in reviewed if x["review_state"] == "DEEP_REVIEW_DOCUMENTED"]
        self.assertGreaterEqual(len(deep), 5)
        for item in deep:
            path = ROOT / item["deep_review_path"]
            content = path.read_text(encoding="utf-8")
            for n in range(1,9):
                self.assertIn(f"## {n}.", content)

    def test_contradictory_vacancy_not_active(self):
        jobs = {row["id"]: row for row in self._load("opportunities.csv")}
        self.assertEqual(jobs["usn-ai"]["status"], "verification_needed")
        self.assertEqual(jobs["usn-systems"]["status"], "verification_needed")
        self.assertEqual(jobs["oxford-cs"]["funding_verification"], "COMPETITIVE_UNAWARDED")
        self.assertIn("HOME_FEE", jobs["reading-robotics-2027"]["funding_verification"])
        assessments = {row["opportunity_id"]: row for row in self._load("opportunity_assessments.csv")}
        self.assertIn("TOP_RANKED", assessments["monash-distrobot"]["formal_eligibility"])

    def test_source_registers_are_unique_and_traceable(self):
        with (ROOT/"data"/"claim_register.jsonl").open(encoding="utf-8") as stream:
            records = [json.loads(x) for x in stream if x.strip()]
        self.assertEqual(len(records), len({r["id"] for r in records}))
        self.assertTrue(all(r["source_url"].startswith("https://") for r in records))

    def test_explicit_exclusion_reasons(self):
        excluded = self._load("exclusions.csv")
        self.assertGreaterEqual(len(excluded), 8)
        for row in excluded:
            self.assertTrue(row["rationale"] and row["code"])

if __name__ == "__main__":
    unittest.main()
