# ishaanbahl6200/scholarship-scraper — deep Auth0/Gumloop scholarship security audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/ishaanbahl6200/scholarship-scraper | **Pinned revision:** [`f9995a91c835f572baf903bff56d1e63dddb8718`](https://github.com/ishaanbahl6200/scholarship-scraper/commit/f9995a91c835f572baf903bff56d1e63dddb8718) | **State:** DEEP_REVIEW_DOCUMENTED (static code audit) | **Decision:** reject deployment as-is until webhook authentication, PII access and admin authorization are corrected.

## 1. Purpose and implementation layers

A Canadian scholarship discovery/matching web product with Next.js, Auth0 login, MongoDB records, Gemini embeddings and Gumloop external scraping/matching flows. The roughly 143-entry tree contains a current `src/app` tree and a second substantial `src/frontend/app` tree, which have overlapping route paths and may represent different deployment roots. It includes test files and user-facing scholarship, saved, profile and dashboard components. The pinned source was last observed 2026-01-18.

This is primarily a scholarship aggregation and matching application, not a verified current funded PhD position or doctoral admissions engine.

## 2. Acquisition and matching dataflow

The authenticated frontend can trigger a Gumloop external workflow. A webhook receives structured scholarship fields including title, amount, deadline, eligibility, source URL, embedding and optionally `auth0_user_id`. It looks for existing records by exact title + source URL, inserts into MongoDB, and optionally creates a match to a specified user. A separate endpoint returns a user's profile and embedding for the external matcher. The matching route can generate Gemini embeddings and score candidates by cosine similarity, heuristic program filters and special Canadian/universal-award rules.

These are model-generated **discovery candidates**, not issuer-verified awards. The code stores scholarship statuses and applicant savings separately, but the system does not require official source snapshots, live award dates or legal eligibility before creating a match.

## 3. P0 webhook secret fail-open and personal-data disclosure

`src/frontend/app/api/gumloop/webhook/route.ts` and `.../gumloop/users/route.ts` authenticate only if `process.env.GUMLOOP_WEBHOOK_SECRET` is set. Their logic is effectively `if (expectedSecret && suppliedSecret !== expectedSecret) reject`. If the deployment lacks this environment variable, **both endpoints accept requests without that shared secret**.

The `users` endpoint accepts a caller-provided `auth0_user_id` and returns email, school, program, GPA, location, ethnicity and profile embedding. This is a sensitive data-disclosure boundary, particularly under missing-secret configuration. It also relies on a shared integration secret instead of per-subject authorization; any holder of that shared secret can request any user ID. Require fail-closed startup validation, authenticated service identity, scoped access and minimal data projection without sensitive demographic fields unless strictly necessary and consented.

The webhook similarly becomes a public insertion/match trigger if the secret is unset. Input fields are not guarded by a tight schema, freshness policy or verified issuer URL; an attacker or misconfigured integration could flood fraudulent records.

## 4. P0 destructive “admin” route accessible to any logged-in user

The `src/frontend/app/api/admin/cleanup-duplicates/route.ts` GET/POST handlers check only `getSession()`, not an admin role or permission. An ordinary authenticated user can invoke the POST route that globally loads scholarship records, groups them by normalized **title alone**, rewrites `matches` and `saved_scholarships` references, and deletes duplicate scholarship rows from the shared MongoDB collection.

The operation has no explicit operator approval, dry-run transaction, per-tenant authorization, or rollback. Two distinct programs with the same generic title can be merged and deleted; references may be corrupted during concurrent operations. This is a source-level authorization and data-integrity risk, not exploit-tested deployment behavior.

## 5. False matching and financial semantics

The webhook defaults `match_score` to **0.8** whenever the Gumloop payload omits it, implying high numerical confidence without measured fit or formal eligibility. `amount` is normalized by removing nonnumeric characters into a single number and defaults to 0, losing currency, stipend period, tuition/fee category, partial funding and award-cycle context. A missing/invalid date can create an undefined or invalid `deadline`.

The matching rules infer Canadian eligibility from presence of a `province` field or citizenship strings, and classify some “easy entry” keywords as universal. These are unreliable for legal residency, student enrollment, citizenship, degree level and target year. Program-specific substring exclusions can overreject interdisciplinary awards while accepting others with no explicit match. A cosine similarity score cannot establish award entitlement, funded doctoral offers, or actual acceptance probability.

## 6. Privacy and source/failure accounting

The User schema stores academic profile, citizenship, ethnicity/demographics and numerical embeddings. Those fields are subject to data minimization and explicit consent; they must remain in an access-controlled private store and never be copied to GitHub. No per-field provenance from official scholarship owner pages is required by the current webhook path.

Scholarship dedup is exact on title and source during ingest, but destructive cleanup is fuzzy by normalized title only, a contradictory identity contract. Concurrent ingestion without a unique compound database index can create duplicates despite initial findOne. The source tree includes tests, but inspected tests are not comprehensive security, role, source-truth or adversarial matching benchmarks. No running site or actual identity provider was accessed.

## 7. Transfer and required controls

Useful ideas: separate applicant profile, scholarship observation, matched opportunity, saved record and authenticated workflow trigger. Required before adoption:
1. Fail closed if webhook signature/secret missing; use service authentication, replay resistance and limited scopes.
2. Remove broad user-profile lookup; provide only consented, minimized, purpose-specific fields.
3. Enforce administrative authorization, explicit confirmation, transaction and reversible dedup operations.
4. Use stable scholarship issuer ID, intake cycle, currency/period, coverage, deadline/timezone and exact official source evidence.
5. Separate heuristic semantic similarity from formal eligibility and funding verification.
6. Preserve immutable evidence spans and a source-to-claim verification ledger.
7. Add security/regression tests for missing secrets, arbitrary user IDs, role bypass, duplicate cleanup, cross-user writes and false 0.8 matching.
8. Determine authoritative deployed source root, including whether legacy `src/frontend` routes are active.

## 8. Pinned evidence and limitations

- [Webhook ingestion and fail-open guard](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/app/api/gumloop/webhook/route.ts)
- [User-profile service endpoint](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/app/api/gumloop/users/route.ts)
- [Any-auth destructive dedup route](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/app/api/admin/cleanup-duplicates/route.ts)
- [Matching heuristics and embeddings](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/app/api/gumloop/trigger-matching/route.ts)
- [Data model](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/lib/db-schema.ts)
- [Personal saved status](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/app/api/saved/route.ts)
- [Auth0 session middleware](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/middleware.ts)
- [Gemini provider](https://github.com/ishaanbahl6200/scholarship-scraper/blob/f9995a91c835f572baf903bff56d1e63dddb8718/src/frontend/lib/gemini.ts)

**DEEP_REVIEW_DOCUMENTED — static conditional-risk analysis only.** Whether a deployment actually omits the integration secret or exposes the nested `src/frontend` root was **NOT_VERIFIED**. No application ran, no user profile was retrieved, no admin cleanup was triggered, and no third-party scholarship was independently validated.
