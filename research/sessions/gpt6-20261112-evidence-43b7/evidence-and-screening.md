# Source inspection and classification handoff — 2026-11-12

Five source-inspected repositories have standalone source-pinned investigations in this directory. Three are eight-section source-level audits; two are privacy-bounded preliminary reviews. None is independently verified as an official funded PhD source. No third-party code, email, uploaded CSV, private applicant record, or account was executed or read.

## Three additional discovery candidates for documented exclusion

| Repository | Revision | Observed disposition |
|---|---|---|
| [ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER](https://github.com/ATULPANDEYIITR/CAREER_ACADEMIC_APPLICATION_AND_TRACKER/tree/18b4c4a163bbd908ff434d47a7cf570686962e83) | `18b4c4a163bbd908ff434d47a7cf570686962e83` | Both advertised /api/phd/cs and /api/phd/management endpoints always return empty lists; corresponding PhD data JSONs are zero-byte placeholders. No inspectable live collector. |
| [merlick-netsi/netsi-phd-admissions-review](https://github.com/merlick-netsi/netsi-phd-admissions-review/tree/85a4818cbd4b59a061801436bec9dd8cc5f2663c) | `85a4818cbd4b59a061801436bec9dd8cc5f2663c` | Entire tracked root tree is one 29-byte README; no application, admissions research or faculty opportunity data. |
| [hqtang02/full-scholarship-phd](https://github.com/hqtang02/full-scholarship-phd/tree/021aa3bf729245fa0910e3ab367d24a08c445bb0) | `021aa3bf729245fa0910e3ab367d24a08c445bb0` | Latest published Git commit deletes README; source tree retrieval for HEAD is unavailable. Candidate could be re-screened after a new accessible commit. |

## Canonical integration rule

Reconcile each file independently against the latest `data/github_discovery_candidates.csv`, `data/repositories.csv` and `data/exclusions.csv` on `main`, using a non-forced Git compare-and-swap. Register only still-UNTRIAGED candidates, preserve other agents' work, regenerate research index and coverage summaries, and keep preliminary/deep classifications distinct. This directory is supplemental until explicit canonical rows exist.

Important findings: source-claimed official PhD funding is unproved; Firestore inline applicant-document fallback; Gmail multiword status and 25-message pagination defects; legacy deployment secrets and applicant data exposure risks. Do not reproduce exposed credential values.
