import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts import import_research


class ImportResearchTests(unittest.TestCase):
    def test_idempotent_import_preserves_application_state(self):
        with TemporaryDirectory() as tmp:
            path = Path(tmp) / "project.sqlite"
            with sqlite3.connect(path) as db:
                first = import_research.run(db)
                self.assertEqual(first["candidate_repositories"], 404)
                expected_repo_audits = len(import_research.read_csv("repositories.csv"))
                self.assertEqual(first["repo_audits"], expected_repo_audits)
                self.assertEqual(first["claims"], 26)
                self.assertEqual(first["opportunities"], 20)
                self.assertEqual(first["applicant_cases"], 6)
                self.assertEqual(first["repo_relations"], len(import_research.read_csv("repository_relations.csv")))
                self.assertEqual(first["verified_publication_records"], 1)
                db.execute("INSERT INTO applications (id,opportunity_id,state) VALUES ('local-state','eth-robotx','PREPARING')")
                db.commit()
                second = import_research.run(db)
                self.assertEqual(second, first)
                self.assertEqual(db.execute("SELECT count(*) FROM opportunities").fetchone()[0], 20)
                self.assertEqual(db.execute("SELECT count(*) FROM claim_register").fetchone()[0], 26)
                self.assertEqual(db.execute("SELECT count(*) FROM repository_audits").fetchone()[0], expected_repo_audits)
                self.assertEqual(db.execute("SELECT count(*) FROM applications").fetchone()[0], 1)
                self.assertEqual(db.execute("SELECT state FROM applications WHERE id='local-state'").fetchone()[0], "PREPARING")
                self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])

    def test_source_proof_and_eligibility_are_not_inferred(self):
        with sqlite3.connect(":memory:") as db:
            import_research.run(db)
            row = db.execute(
                "SELECT individual_funding_status,offer_date_evidence FROM opportunity_verification WHERE opportunity_id='oxford-cs'"
            ).fetchone()
            self.assertEqual(row[0], "COMPETITIVE_UNAWARDED")
            self.assertNotEqual(row[1], "GUARANTEED_2026_OFFER")
            row = db.execute(
                "SELECT review_state,empirical_execution FROM repository_audits "
                "WHERE repository_key='aghababaei/phd-seeker'"
            ).fetchone()
            self.assertEqual(row, ("DEEP_REVIEW_DOCUMENTED", "NOT_TESTED"))
            self.assertEqual(db.execute("SELECT count(*) FROM communication_actions").fetchone()[0], 0)

    def test_sensitive_data_is_not_imported(self):
        with sqlite3.connect(":memory:") as db:
            import_research.run(db)
            self.assertEqual(db.execute("SELECT count(*) FROM applications").fetchone()[0], 0)
            self.assertEqual(db.execute("SELECT count(*) FROM application_events").fetchone()[0], 0)
            self.assertEqual(db.execute("SELECT count(*) FROM communication_actions").fetchone()[0], 0)


if __name__ == "__main__":
    unittest.main()
