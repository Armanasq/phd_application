# Local research data importer

This importer materializes the public research **source records** into a local SQLite database. It does not retrieve live jobs, infer eligibility, change GitHub application statuses, create emails or submit applications.

## Command

```sh
python3 scripts/import_research.py --dry-run
python3 scripts/import_research.py --db .local/phd_intelligence.sqlite
```

The dry-run uses `:memory:` and never changes an existing user database. The second command is **idempotent** with explicit stable identifiers and foreign keys. It preserves existing application/workflow records while updating verified-source metadata. All SQL inputs are parameterized. Bootstrap and import share the same migration runner.

## Imported objects
- Eight country records and canonical institutional identities.
- Discovered repository identities, revision-pinned audits, and documented dependence edges from the canonical CSV registers. Counts are computed at import time and may grow independently; `candidate_repositories`, `repo_audits`, and `repo_relations` represent distinct grains.
- 26 claim records and their primary source linkages, with no independent verification inferred.
- 20 opportunity/program/scholarship leads with separate tuition, funding, channel and offer-evidence rows. Monetary amounts are left as qualitative evidence strings rather than inventing safely comparable numeric amounts.
- Six public applicant experience observations with source class and survivorship caveats.
- One publisher-verified *Measurement* article DOI/publication record; unrelated preprint/poster claims are not imported as accepted journal papers.

The importer reports import counts and is also run by GitHub Actions against **ephemeral** SQLite data. It never uploads the database to the repository. All candidate-sensitive applications, documents, citizenship details, emails or credentials remain private and **are not imported**.

## Source-of-truth distinction
CSV and JSONL public data remains the research evidence ledger. The SQLite database is a local indexed replica for cross-entity analysis and future private application planning; it is not synchronized with any university or funding provider. Latest primary-source verification is necessary before any application, financial decision, or message.

## Migration discipline

`schema_migrations` records each applied SQL migration, its SHA-256 checksum, and application timestamp. Migrations run in an explicit SQLite transaction; a failed migration rolls back both its DDL and version record. Re-running an unchanged migration is a no-op. If an applied migration file changes, the runner stops and requires a new forward migration rather than silently reapplying altered history.

Do not edit an applied migration. Add the next ordered SQL file instead. There are no automatic down migrations: a failed in-flight migration is rolled back transactionally, while recovery from a successfully applied migration requires restoring a pre-migration database backup or applying a reviewed corrective migration. Back up persistent local databases before forward schema changes.
