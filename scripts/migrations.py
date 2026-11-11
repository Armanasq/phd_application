from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import sqlite3


class MigrationError(RuntimeError):
    pass


def apply_migrations(db: sqlite3.Connection, directory: Path) -> list[str]:
    db.execute("PRAGMA foreign_keys = ON")
    db.execute(
        "CREATE TABLE IF NOT EXISTS schema_migrations ("
        "version TEXT PRIMARY KEY, "
        "checksum TEXT NOT NULL CHECK(length(checksum)=64), "
        "applied_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP)"
    )
    applied: list[str] = []
    for path in sorted(directory.glob("*.sql")):
        version = path.stem
        content = path.read_text(encoding="utf-8")
        checksum = sha256(content.encode("utf-8")).hexdigest()
        existing = db.execute(
            "SELECT checksum FROM schema_migrations WHERE version = ?", (version,)
        ).fetchone()
        if existing:
            if existing[0] != checksum:
                raise MigrationError(
                    f"Applied migration {version} has changed; add a new migration instead"
                )
            continue
        safe_version = version.replace("'", "''")
        script = (
            "BEGIN IMMEDIATE;\n"
            + content
            + "\nINSERT INTO schema_migrations(version, checksum) VALUES ('"
            + safe_version
            + "', '"
            + checksum
            + "');\nCOMMIT;"
        )
        try:
            db.executescript(script)
        except sqlite3.Error as exc:
            if db.in_transaction:
                db.rollback()
            raise MigrationError(
                f"Migration {version} failed and was rolled back: {exc}"
            ) from exc
        applied.append(version)
    return applied
