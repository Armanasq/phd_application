#!/usr/bin/env python3
import argparse
import pathlib
import sqlite3
ROOT = pathlib.Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--db", default=".local/phd_intelligence.sqlite")
args = parser.parse_args()
target = pathlib.Path(args.db)
target.parent.mkdir(parents=True, exist_ok=True)
with sqlite3.connect(target) as db:
    db.executescript((ROOT/"sql"/"schema.sql").read_text(encoding="utf-8"))
print(target)
