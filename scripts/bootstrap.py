#!/usr/bin/env python3
import argparse
import pathlib
import sqlite3

if __package__:
    from .migrations import apply_migrations
else:
    from migrations import apply_migrations

ROOT = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--db", default=".local/phd_intelligence.sqlite")
args = parser.parse_args()
target = pathlib.Path(args.db)
target.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(target) as db:
    db.execute("PRAGMA foreign_keys = ON")
    db.executescript((ROOT / "sql" / "schema.sql").read_text(encoding="utf-8"))
    apply_migrations(db, ROOT / "sql" / "migrations")
    if db.execute("PRAGMA foreign_key_check").fetchall():
        raise RuntimeError("SQLite foreign-key verification failed")
    if db.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
        raise RuntimeError("SQLite integrity verification failed")
print(target)
