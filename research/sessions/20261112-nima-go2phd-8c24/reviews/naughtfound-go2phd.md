# NaughtFound/Go2Phd — deep static source audit

**Checked:** 2026-11-12  
**Upstream:** https://github.com/NaughtFound/Go2Phd  
**Pinned commit:** [6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b](https://github.com/NaughtFound/Go2Phd/commit/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b)  
**Review depth:** DEEP_STATIC_SOURCE_REVIEW; tests and OAuth/Google Sheets integration **NOT_EXECUTED**.  
**Verdict:** Reference only; do not adopt its sheet parser or authentication/data model unchanged.  
**Scope:** all Go source files, dependency manifest, README, root tree, Git history, issues/PRs and license inventory. The historical commit diffs, Go module installation, live OAuth and network calls were not reproduced.

## 1. Actual purpose and architecture

A 23-file, MIT-licensed Go/Gin REST backend for **reading** a personal academic application spreadsheet, enriching university countries and calculating status/priority/tag aggregates. Routing is `main.go` -> handlers -> services -> repositories. Google OAuth exchanges authorization codes and obtains a refresh token; the client supplies that refresh token and the spreadsheet ID in HTTP headers for each positions request. `repositories/sheets.go` requests the `spreadsheets.readonly` scope, so the implementation is **read-only**, even though the README describes application management. The API exposes GET routes for positions, grouped statistics, university lookup and OAuth login/callback; it has no application create/update/submit route.

## 2. Confirmed P0: documented sheet schema is incompatible with parser

README specifies nine columns in this order: `Title, Priority, Tags, Status, University Name, Country, Due Date, Rolling Based, Links`.

The source-level parser `services/position.go:parseRowToPosition` instead expects eight positions:
- 0-4: title, priority, tags, status, university name (these align).
- 5: `DueDate`, but in the documented sheet column 5 is **Country**.
- 6: `RollingBased` parsed as boolean, but column 6 is **Due Date**; parse typically fails and silently produces false.
- 7: `Links` split on spaces, but column 7 is **Rolling Based**; the actual links column 8 is never read.

Consequently a README-compliant sheet can render a country name as the deadline, lose the real deadline, mark rolling openings as fixed and show `true`/`false` as a link. This directly corrupts application planning. The source lacks header-name mapping or schema-version checks. **Required fix:** resolve columns by validated header names (or explicitly migrate to a strictly versioned schema); add table-driven tests for nine-column rows, null/short rows, date formats, and missing fields.

Evidence: [README](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/README.md), [parser](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/position.go).

## 3. Confirmed P1: OAuth callback configuration mismatch

The README's .env example declares `GOOGLE_REDIRECT_URI`; `main.go` actually reads `GOOGLE_REDIRECT_URL`, which is passed to `oauth2.Config.RedirectURL` via `services/auth.go`. A user following the documented setup supplies the wrong environment variable, leaving the configured redirect URL empty. The login/auth-code exchange therefore cannot be assumed to operate as documented. **Fix:** normalize one variable name, fail startup for missing OAuth settings, and integration-test the actual callback route `/auth/google/callback`.

Evidence: [README](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/README.md), [main.go](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/main.go), [auth service](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/auth.go).

## 4. Data correctness and security risks

- `repositories/university.go` calls `http://universities.hipolabs.com/search?name=...` over plaintext HTTP and takes the **first fuzzy match** as the canonical university/country. This creates both transport-integrity and incorrect-entity-matching risks; there is no identity disambiguation, source snapshot or verification step.
- `models/position.go` stores `DueDate` as an unvalidated string and `ID` as the row index. Sorting or inserting spreadsheet rows changes IDs; there is no timezone, admission cycle, stable application identity, funding component or submission receipt.
- The callback returns OAuth access and refresh tokens in the HTTP JSON response, and the user-facing data routes require `X-Refresh-Token`. Treat these as private credentials; the architecture should not be copied into a public-client application without secure credential custody and transport.
- `generateStateToken` uses `crypto/rand` but discards its error; callback verifies matching state against an HttpOnly cookie. The cookie is configured without `Secure` for local HTTP. These are operational hardening issues, not evidence of a demonstrated compromise.
- `services/stats.go` counts arbitrary status/priority strings without enum validation, accepts unknown `group_by` values into the `Other` bucket instead of rejecting them, and computes analytics from the entire read on each request. There is no evidence-backed application lifecycle or independent proof for `Applied`, `Interview`, and `Accepted`.

Evidence: [university repository](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/repositories/university.go), [auth handler](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/handlers/auth.go), [stats service](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/stats.go), [model](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/models/position.go).

## 5. Maintenance, tests and external validity

Latest inspected upstream commit: 2026-10-05; six latest commits cover documentation, grouped statistics, dates, auth and Sheets. No upstream issues or PRs, no `*_test.go` files or GitHub Actions workflow appeared in the complete 23-file tree. `go.mod` declares Go 1.27.0 and Gin 1.12.0; module installation and compilation have not been attempted. There is no packaged dataset or observable application success metric.

## 6. Transfer decision and interconnections

**Adaptable:** small read-only HTTP layer over personal spreadsheet, basic statistics grouping, OAuth state concept, separable repository/service/handler architecture.

**Do not transfer:** positional spreadsheet parsing, bearer refresh-token headers, unaudited fuzzy university enrichment, row-index IDs or a mutable text-only application status. A production PhD application platform needs a schema-checked import, stable identity, explicit provider/cycle fields, structured deadline + timezone + uncertainty, normalized opportunity references, private encrypted credentials, and immutable receipt-based state changes. This is an applicant **workspace**, not a vacancy-discovery source, and must not independently increase verified vacancy coverage.

## 7. Evidence status

Findings above are static comparisons between the pinned README and implementation. No real Google account, spreadsheet, OAuth token, university API, runtime build or network call was used; no exploit was run. The completeness of third-party university search results and production deployability are **UNKNOWN**.
