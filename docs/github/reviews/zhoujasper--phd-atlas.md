# zhoujasper/phd-atlas

- **Assessment date:** 2026-11-11
- **Canonical repository:** https://github.com/zhoujasper/phd-atlas
- **Inspected snapshot:** 8f4318eda901020b61d91abfc82411943200c70f
- **Category:** APPLICATION_WORKSPACE
- **Review depth:** focused repository inspection (not a complete audit)
- **Inspected material:** README.md; DEPLOYMENT.md; package.json; TODO.md; recursive tree (~1961 entries)
- **Verdict:** ARCHITECTURE_REFERENCE

## Distinct practical value
Substantial self-hostable application system covering application dossiers, documents, correspondence, funding, personal profiles, backup and export; supports SQLite and multiple database backends. Documentation includes desktop/HTTPS deployment and upgrade/backup caveats.

## Verified limitations and risks
A 1961-entry repository cannot be truthfully classified fully audited based on a README and a few docs. Product claims, auth design, release safety and backup restore have not been tested. The available public edition is personal-only; advertised options depend on runtime and edition.

## Candidate-specific action
Benchmark domain objects, backups and lifecycle against this project, while retaining a lean evidence-first workspace. Do not transplant server code or claim tested equivalence.

## Not inspected or demonstrated
No dependency audit, setup, live auth/restore tests, or exhaustive source inspection.

**Evidence rule:** Never treat a historical scholarship, applicant guide, or last-update timestamp as proof of 2026-27 policy. The repository's documented behavior is not a substitute for runtime validation.
