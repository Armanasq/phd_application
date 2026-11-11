# Local research data importer

This importer materializes the public research **source records** into a local SQLite database. It does not retrieve live jobs, infer eligibility, change GitHub application statuses, create emails or submit applications.

## Command

```sh
python3 scripts/import_research.py --dry-run
python3 scripts/import_research.py --db .local/phd_intelligence.sqlite
```

The dry-run uses `:memory:` and never changes an existing user database. The second command is **idempotent** with explicit stable identifiers and foreign keys. It preserves existing application/workflow records while updating verified-source metadata. All SQL inputs are parameterized and schema/migrations are applied before import.

## Imported objects
- Eight country records and canonical institutional identities.
- 404 discovered GitHub repository identities (plus explicitly reported relation-only reference nodes when needed), 35 version-pinned audits, and five documented dependence edges.
- 26 claim records and their primary source linkages, with no independent verification inferred.
- 20 opportunity/program/scholarship leads with separate tuition, funding, channel and offer-evidence rows. Monetary amounts are left as qualitative evidence strings rather than inventing safely comparable numeric amounts.
- Six public applicant experience observations with source class and survivorship caveats.
- One publisher-verified *Measurement* article DOI/publication record; unrelated preprint/poster claims are not imported as accepted journal papers.

The importer reports import counts and is also run by GitHub Actions against **ephemeral** SQLite data. It never uploads the database to the repository. All candidate-sensitive applications, documents, citizenship details, emails or credentials remain private and **are not imported**.

## Source-of-truth distinction
CSV and JSONL public data remains the research evidence ledger. The SQLite database is a local indexed replica for cross-entity analysis and future private application planning; it is not synchronized with any university or funding provider. Latest primary-source verification is necessary before any application, financial decision, or message.
