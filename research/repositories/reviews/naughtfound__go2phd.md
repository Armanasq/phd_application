# NaughtFound/Go2Phd — deep static Google Sheets application tracker audit

**Date:** 2026-11-12 | **Upstream:** https://github.com/NaughtFound/Go2Phd | **Pinned commit:** [`6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b`](https://github.com/NaughtFound/Go2Phd/commit/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b) | **State:** DEEP_REVIEW_DOCUMENTED (static) | **Decision:** adapt read-only spreadsheet/analytics separation only; reject positional parser and token transport as-is.

## 1. Product and source identity

A 23-file MIT-licensed Go/Gin service for reading and summarizing application rows from an applicant's Google Sheet. It uses Google OAuth and the `spreadsheets.readonly` scope, enriches university metadata, and provides list/group statistics. The README describes managing application data, but the routed API provides reading and analytics rather than authoritative create/update/submit operations. The latest observed upstream commit is 2026-10-05, and the repository has no `*_test.go` suite or CI workflow.

A parallel session previously published a [source-pinned implementation review](https://github.com/Armanasq/phd_application/blob/main/research/sessions/20261112-nima-go2phd-8c24/reviews/naughtfound-go2phd.md). This report integrates that investigation with independent README, parser, main-entry and tree checks. No new third-party code execution is claimed.

## 2. Architecture and dataflow

`main.go` configures Gin and registers `/auth`, `/universities`, and `/positions`. Handlers call position/university/stat services. The Sheets repository reads user-supplied spreadsheet and OAuth refresh token context; the position service skips headers, maps remaining rows to `Position`, enriches institutions via a separate university repository and provides summary statistics.

Application states, priorities, tags and due dates are imported as strings from the private Google Sheet. A spreadsheet row is a mutable observation; it is not a portal receipt or verified admission decision.

## 3. Confirmed P0 header–parser contract break

README prescribes nine spreadsheet columns in order: `Title, Priority, Tags, Status, University Name, Country, Due Date, Rolling Based, Links`. `services/position.go:parseRowToPosition` instead reads eight zero-based fields and ignores the ninth:
- `DueDate=getCol(5)`, which is the documented **Country**.
- `RollingBased=parseBool(getCol(6))`, which is the documented **Due Date**.
- `Links=getCol(7)`, which is the documented **Rolling Based** flag; real links in column 8 are never read.

This can yield country names as deadlines, missing rolling flags and boolean strings as hyperlinks. Insertion/removal of a header breaks all values silently; there is no header-name validation or schema version. This is a reproducible **source-level contract defect**, not a runtime claim.

Repair with named-column mapping, exact required column validation and table-driven cases for nine columns, reordered columns, empty/null rows, date formats and malformed values.

## 4. OAuth configuration and private token handling

The documented `.env` variable is `GOOGLE_REDIRECT_URI`, while `main.go` reads `GOOGLE_REDIRECT_URL` for the actual OAuth config. Copying the README setup produces an empty redirect config unless another variable is set. Fail startup on missing mandatory OAuth settings and test the same callback path used in documentation.

The service returns refresh/access credentials to the client at callback and accepts refresh tokens via `X-Refresh-Token` request headers for future calls. This spreads long-lived secrets into application traffic and logs/clients; a user-scoped encrypted token vault or short-lived authorized credential proxy is preferable. OAuth state is tied to an HttpOnly cookie but its generator drops entropy-read errors and local cookie settings are not production-hardening evidence. No real OAuth exchange was executed during the audit.

## 5. University/entity matching and status semantics

`repositories/university.go` uses a plaintext HTTP university-name search endpoint and takes the first fuzzy match without disambiguating city, domain, country or institutional identifier. This can misattribute countries and makes queries vulnerable to untrusted transport alterations. A row-index ID changes when the Sheet is sorted or rows inserted. Date text lacks timezone and cycle normalization.

Analytics group arbitrary status and priority strings, without an independently confirmed application stage. `Applied` and `Accepted` from a spreadsheet are a user's assertions, not official submission or award evidence.

## 6. Validation and operational boundaries

No unit tests, Go build, module install, Google Sheets authorization, API network access or security execution was performed. README says Go 1.20+, while `go.mod` at the reviewed snapshot declares a newer Go version; runtime compatibility should be assessed rather than assumed. The service is intentionally lightweight and read-only, not a synchronized database or opportunity crawler; it cannot independently increase verified open-vacancy coverage.

Credential handling, status provenance, fuzzy institution matching, header drift and idempotency are the primary blockers to reuse.

## 7. Transfer into a research-grade application workflow

Reusable: separable handler/service/repository modules, read-only Google Sheets adapter, explicit priorities and tags, and descriptive application metrics. Required changes:
1. Use owner-approved OAuth, encrypted refresh-token custody and row-level data boundaries.
2. Normalize input headers, stable application keys, institution IDs, degree/cycle, and deadline timezone.
3. Preserve spreadsheet source revisions and user-authored status as evidence tier `SELF_REPORTED`.
4. Store application submissions as immutable receipt-backed events in a private workspace.
5. Maintain distinct eligibility/funding facts supported by employer or award-owner sources.
6. Add parser-contract, OAuth-config, date and university-ID unit tests.

## 8. Source references and evidence status

- [README sheet contract](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/README.md)
- [Parser](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/position.go)
- [Entrypoint and OAuth config](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/main.go)
- [OAuth service](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/auth.go)
- [OAuth route](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/handlers/auth.go)
- [University metadata adapter](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/repositories/university.go)
- [Status statistics](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/services/stats.go)
- [Position model](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/models/position.go)
- [Sheets read-only integration](https://github.com/NaughtFound/Go2Phd/blob/6c8eaa03b69e8d2c8e546516e0d4d1e8f830924b/repositories/sheets.go)

**DEEP_REVIEW_DOCUMENTED — static code and README comparison only.** No real Google Sheet, OAuth token, API call, personal document or downstream source was fetched or changed.
