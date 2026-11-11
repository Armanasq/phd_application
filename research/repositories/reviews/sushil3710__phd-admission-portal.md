# sushil3710/PHD_Admission_Portal — institutional admissions system static audit

**Review date:** 2026-11-12  
**Repository:** https://github.com/sushil3710/PHD_Admission_Portal  
**GitHub repository ID:** 689627108  
**Pinned upstream commit:** [7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e](https://github.com/sushil3710/PHD_Admission_Portal/commit/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e)  
**Review state:** DEEP_REVIEW_DOCUMENTED — risk-focused static implementation review, upstream tests/runtime NOT_TESTED.  
**Verdict:** BLOCK deployment/reuse as-is due to missing authorization on sensitive actions, credential exposure, document handling and SQL/OS command boundaries.

## 1. Scope and intended audience

A 2023 full-stack institutional PhD and MTech admissions portal branded for IIT Ropar. It exposes applicant registration and OTP flows, personal/academic records, program offerings and admission cycles, uploaded evidence documents, fee and application status, departmental administration, Excel uploads, merit lists and selection/notification emails. It is a software-design example rather than a verifiable current 2026 recruitment or funding source. The README references an internal-network deployment, but that is not proof of present service availability, authorization, security or institutional endorsement.

## 2. Source inventory and architecture

The pinned recursive tree contains 192 files in 11 directories, including React 17 client pages and many applicant/admin form components, Express 4 server routes, a PostgreSQL schema and per-cycle table generation, mail templates, admin/application DB modules, merit-list and Excel import/export code, and npm lockfiles. A repository MIT license exists. The root server build scripts use separate client/server installs and inconsistent historical Node engine ranges.

The major path is **React client -> Express route -> handler-level JWT verification -> PostgreSQL tables -> status/merit workflow -> email/Excel output**. Express registers dozens of distinct CRUD and bulk-result endpoints directly in server/app.js, with no centralized authentication middleware. Most individual applicant and admin handlers check JWT signatures and user roles, which is positive, but that pattern does not cover every route and cannot ensure object-level ownership globally.

Primary inspected sources: [README](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/README.md), [router](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/server/app.js), [admin backend](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/server/admin-db.js), [applicant backend](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/server/applicant-db.js), [auth](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/server/auth.js), [schema](https://github.com/sushil3710/PHD_Admission_Portal/blob/7983a67b51d3b6e9926fc3a67dc3f8edc879dd0e/server/database.sql).

## 3. Identity, access control and secret-management defects

- **Public administrative bootstrap credential:** The README gives default administrator sign-in instructions, and database.sql inserts a matching seeded administrator record with a plaintext password. The auth module explicitly special-cases that account using direct password-string comparison rather than bcrypt. Do not reuse, attempt sign-in with, or reproduce the credential values. There is no evidence of production credential rotation.
- **Committed environment files:** server/.env and client/.env.local exist in the source tree. Their contents were deliberately not opened; public committed environment files require owner-led secret inventory and rotation where applicable.
- **Unprotected mail handler:** app.js routes POST /send-mail to admin-db.send_mail. The send_mail implementation reads an Excel file and transmits selection/rejection emails but has no JWT verification or role authorization block, unlike neighboring handlers. Under an exposed configuration, that is a serious authorization boundary.
- **Unprotected external-process handler:** app.js routes POST /view-excel to admin-db.view_mail. That function passes a path derived from a user request into child_process.exec() without the authentication/authorization checks used by adjacent admin handlers. This is a shell-command and filesystem trust boundary; no payload or exploit was executed.
- **Sensitive OTP logging:** The OTP signup/sign-in/password-reset paths log OTP values to the server console. OTP database writes are initiated via async bcrypt callbacks whose completion is not awaited before responses or outgoing email; state can race verification requests. Password reset does not demonstrate comprehensive rate limits or brute-force protection in the inspected code.
- **Development and production TLS posture:** server/db.js sets rejectUnauthorized: false for production PostgreSQL TLS connections. This weakens server-certificate verification.

These are static source findings, not a claim that any current deployment remains vulnerable or has been compromised.

## 4. Data model, application transitions and consistency

The base schema defines applicant and admin users, credential-verification tables, admission-cycle registry, spreadsheet templates, and cycle state. Each new cycle causes the server to construct separate phd_offerings_<id> and applications_<id> tables dynamically. This spreads schema evolution, uniqueness and relational integrity across per-cycle tables instead of one normalized cycle-keyed table.

- Several admin routes construct SQL table identifiers by string-concatenating cycle_id read directly from req.body. Bound parameters protect value slots but not those identifiers. The request-derived identifier must be strictly validated or resolved by server-side lookup before SQL construction.
- Applicant save_application_info inserts an application, copies applicant PII into the per-cycle table, stores uploaded documents, and emails confirmation. These effects are not enclosed in one auditable transaction; partial success is possible.
- In the personal-details copy query, the permanent_city and permanent_state columns are populated from the opposite source columns, a confirmed data-integrity defect.
- Upload-result ingestion removes the last spreadsheet row unconditionally with xlData.pop(), risking data loss for ordinary files without a footer row. It then changes application decision states row by row, with no explicitly observed bulk-transaction rollback.

The architecture separates applicant, offering and cycle entities, but status changes and applicants' sensitive records require transactional, role-checked audit events.

## 5. File, network and privacy boundaries

The server handles profile photographs, degree records, category/eligibility certificates, identity-related fields, SOPs, signatures, payment confirmations, publications, CVs, and other applicant materials. Several handlers build filesystem paths using user-provided original names and write uploaded buffers under server/public without explicit per-file size/type validation in the route setup. Express also registers static file serving; security depends on actual launch working directory and web-server mapping, which were not independently verified. Do not assume those personal files are access-controlled.

The administrator's send_mail/view_mail operations construct paths from request-provided strings without a demonstrated canonicalized safe-root or extension policy. The current code therefore fails to establish robust path traversal, command injection and sensitive-file privacy boundaries.

The React/Express CORS configuration is permissive; no global request-rate limiting, per-user upload quota, MFA/session revocation, or user-initiated data retention/deletion controls were established in the inspected core.

## 6. Implementation fidelity and test coverage

Some claims are implemented in code: registration, OTP email, JWT role checks for many routes, PostgreSQL persistence, cycles/offerings, enrollment applications, export, Excel selection processing and email notification. However, no current institutional vacancy or funding status is verified from these files.

The repository contains no substantive automated test suite: server/package.json's test command exits with an error, and no tests/CI workflow were present in the inspected tree. Its last observed code revision is from 2023; issues/PRs returned empty. The inconsistent Node engine definitions, older dependency ranges, undocumented environment handling and hardcoded bootstrap account complicate reproducible deployment.

No packages were installed; the API, SMTP, database migrations, file uploads and deployment URL were not accessed.

## 7. Comparison, remediation priorities and transferable methods

Unlike a scraper or applicant-only tracker, this repository models the institution-side admissions lifecycle. Its reusable product concepts include admission cycles, offering eligibility, departmental review, application artifacts, configurable result imports and communication templates.

Before considering any code reuse:
1. Remove all published default credentials and audit/rotate any committed secrets; make bootstrap accounts one-time setup operations with strong hashing.
2. Apply authentication and role/row-level authorization centrally to every sensitive endpoint, especially bulk mail, file access and result publication.
3. Replace shell-executed spreadsheet viewing with safe server-side parsing and explicit file allowlists.
4. Normalize cycle/application/offer tables; use validated identifiers and parameterized values, transactional state transitions, immutable audit logs and idempotent notifications.
5. Move uploads to private object storage with scoped authorization, random server-generated names, antivirus/content validation, quota limits, encryption and lifecycle controls.
6. Repair the field swap, Excel row truncation and async callback/response races; add integration tests and CI.
7. Preserve per-claim source provenance. Institution-specific administrative software is not itself independent evidence of a currently open PhD position, international eligibility, or guaranteed funding.

## 8. Decision and verification boundary

**DEEP_REVIEW_DOCUMENTED — BLOCK executable reuse as-is.** The complete recursive tree, README, server routes, authentication, applicant/admin database modules, application submission, SQL schema, dashboard, Excel/result import, merit handling, file paths and package manifests were inspected selectively by risk and dataflow. The private contents of .env files and personal documents were intentionally not read or reproduced.

Unverified: runtime exploitability, credential validity, network deployment reachability, source ownership or institutional endorsement, production controls, hidden services, live PhD advertisements, admissions results or funding, browser/API builds, and any upstream tests. The static audit is not a security penetration test.
