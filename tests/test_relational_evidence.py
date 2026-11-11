import sqlite3
from pathlib import Path
import unittest

from scripts.migrations import apply_migrations

ROOT = Path(__file__).resolve().parents[1]


def make_database():
    db = sqlite3.connect(":memory:")
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript((ROOT/"sql"/"schema.sql").read_text(encoding="utf-8"))
    apply_migrations(db, ROOT / "sql" / "migrations")
    return db


class RelationalEvidenceTests(unittest.TestCase):
    def test_relational_entities_exist(self):
        with make_database() as db:
            tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
            for name in ("research_repositories","repository_audits","repository_findings","repository_relations","claim_register","claim_sources","research_publications","supervisor_publications","opportunity_verification","applicant_experience_cases","communication_actions","recorded_discovery_searches"):
                self.assertIn(name,tables)

    def test_acceptance_cannot_be_advanced_without_proof(self):
        with make_database() as db:
            db.execute("INSERT INTO countries VALUES ('ch','Switzerland')")
            db.execute("INSERT INTO institutions VALUES ('eth','ch','ETH')")
            db.execute("INSERT INTO sources VALUES ('src','https://example.org','official','2026-11-11','reviewed')")
            db.execute("INSERT INTO opportunities (id,institution_id,source_id,title,kind,status) VALUES ('job','eth','src','funded role','vacancy','open_verified')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO applications (id,opportunity_id,state) VALUES ('first','job','ACCEPTED')")
            db.execute("INSERT INTO applications (id,opportunity_id,state) VALUES ('a','job','PREPARING')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("UPDATE applications SET state='ACCEPTED' WHERE id='a'")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO application_events VALUES ('ev','a','ACCEPTANCE_RECEIPT','2026-11-11',NULL)")
            db.execute("INSERT INTO application_events VALUES ('ev','a','ACCEPTANCE_RECEIPT','2026-11-11','private-acceptance-confirmation')")
            db.execute("UPDATE applications SET state='ACCEPTED' WHERE id='a'")
            self.assertEqual(db.execute("SELECT state FROM applications WHERE id='a'").fetchone()[0], "ACCEPTED")

    def test_external_email_cannot_be_recorded_sent_without_authorization(self):
        with make_database() as db:
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO communication_actions(id,state,delivery_reference) VALUES('m','SENT','proof')")
            db.execute("INSERT INTO communication_actions(id,state) VALUES('draft','DRAFTED')")
            db.execute("INSERT INTO communication_actions(id,state,delivery_reference,authorized_by,authorized_at,sent_at) VALUES('sent','SENT','private-receipt','explicit_user_approval','2026-11-11','2026-11-11')")
            self.assertEqual(db.execute("SELECT count(*) FROM communication_actions").fetchone()[0], 2)

    def test_migration_idempotent_for_fresh_local_db(self):
        with make_database() as db:
            self.assertEqual(apply_migrations(db, ROOT / "sql" / "migrations"), [])
            self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])


if __name__=="__main__":
    unittest.main()
