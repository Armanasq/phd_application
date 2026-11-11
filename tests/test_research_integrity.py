import csv
from pathlib import Path
import sqlite3
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ResearchIntegrityTests(unittest.TestCase):
    def test_repository_review_links(self):
        with (ROOT/"data"/"repositories.csv").open(encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), len({r["repository"].casefold() for r in rows}))
        for r in rows:
            self.assertTrue((ROOT/r["review_path"]).is_file())
            self.assertEqual(len(r["snapshot_sha"]), 40)

    def test_submission_requires_proof(self):
        with sqlite3.connect(":memory:") as db:
            db.executescript((ROOT/"sql"/"schema.sql").read_text(encoding="utf-8"))
            db.execute("PRAGMA foreign_keys = ON")
            db.execute("INSERT INTO countries VALUES ('ch', 'Switzerland')")
            db.execute("INSERT INTO institutions VALUES ('eth', 'ch', 'ETH')")
            db.execute("INSERT INTO sources VALUES ('src', 'https://example.org/vacancy', 'official', '2026-11-11', 'reviewed')")
            db.execute("INSERT INTO opportunities (id,institution_id,source_id,title,kind,status) VALUES ('o','eth','src','Doctoral Position','position','open_verified')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO applications (id, opportunity_id, state) VALUES ('a','o','SUBMITTED')")
            db.execute("INSERT INTO applications (id, opportunity_id, state) VALUES ('b','o','DISCOVERED')")
            self.assertEqual(db.execute("SELECT state FROM applications WHERE id='b'").fetchone()[0], "DISCOVERED")

if __name__ == "__main__":
    unittest.main()
