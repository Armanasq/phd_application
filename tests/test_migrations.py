from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import unittest

from scripts.migrations import MigrationError, apply_migrations

ROOT = Path(__file__).resolve().parents[1]


class MigrationTests(unittest.TestCase):
    def test_migrations_are_recorded_and_idempotent(self):
        with sqlite3.connect(":memory:") as db:
            db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
            first = apply_migrations(db, ROOT / "sql" / "migrations")
            second = apply_migrations(db, ROOT / "sql" / "migrations")
            self.assertEqual(first, ["001_research_evidence", "002_submission_evidence"])
            self.assertEqual(second, [])
            self.assertEqual(db.execute("SELECT count(*) FROM schema_migrations").fetchone()[0], 2)
            self.assertEqual(db.execute("PRAGMA foreign_key_check").fetchall(), [])

    def test_changed_applied_migration_is_rejected(self):
        with TemporaryDirectory() as tmp, sqlite3.connect(":memory:") as db:
            directory = Path(tmp)
            migration = directory / "001_initial.sql"
            migration.write_text("CREATE TABLE sample(id TEXT);", encoding="utf-8")
            apply_migrations(db, directory)
            migration.write_text("CREATE TABLE sample(id TEXT, value TEXT);", encoding="utf-8")
            with self.assertRaises(MigrationError):
                apply_migrations(db, directory)

    def test_failed_migration_rolls_back_schema_and_version(self):
        with TemporaryDirectory() as tmp, sqlite3.connect(":memory:") as db:
            directory = Path(tmp)
            migration = directory / "001_broken.sql"
            migration.write_text("CREATE TABLE transient(id TEXT);\nINVALID SQL;", encoding="utf-8")
            with self.assertRaises(MigrationError):
                apply_migrations(db, directory)
            self.assertIsNone(db.execute("SELECT name FROM sqlite_master WHERE name='transient'").fetchone())
            self.assertEqual(db.execute("SELECT count(*) FROM schema_migrations").fetchone()[0], 0)

    def test_submitted_state_requires_receipt_evidence(self):
        with sqlite3.connect(":memory:") as db:
            db.execute("PRAGMA foreign_keys=ON")
            db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
            apply_migrations(db, ROOT / "sql" / "migrations")
            db.execute("INSERT INTO countries VALUES ('ch','Switzerland')")
            db.execute("INSERT INTO institutions VALUES ('eth','ch','ETH')")
            db.execute("INSERT INTO sources VALUES ('src','https://example.org','official','2026-11-11','reviewed')")
            db.execute("INSERT INTO opportunities (id,institution_id,source_id,title,kind,status) VALUES ('job','eth','src','funded role','vacancy','open_verified')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("INSERT INTO applications (id,opportunity_id,state,submission_reference,submitted_at) VALUES ('direct','job','SUBMITTED','portal','2026-11-12T00:00:00Z')")
            db.execute("INSERT INTO applications (id,opportunity_id,state) VALUES ('a','job','READY')")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("UPDATE applications SET state='SUBMITTED',submission_reference='portal',submitted_at='2026-11-12T00:00:00Z' WHERE id='a'")
            db.execute("INSERT INTO application_events VALUES ('ev','a','APPLICATION_SUBMITTED','2026-11-12T00:00:00Z','private-receipt-ref')")
            db.execute("UPDATE applications SET state='SUBMITTED',submission_reference='portal',submitted_at='2026-11-12T00:00:00Z' WHERE id='a'")
            self.assertEqual(db.execute("SELECT state FROM applications WHERE id='a'").fetchone()[0], "SUBMITTED")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("UPDATE application_events SET evidence_ref='replacement' WHERE id='ev'")
            with self.assertRaises(sqlite3.IntegrityError):
                db.execute("DELETE FROM application_events WHERE id='ev'")


if __name__ == "__main__":
    unittest.main()
