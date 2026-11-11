# imsankalp/phD-application-tracker — deep static source audit

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/imsankalp/phD-application-tracker | **Pinned commit:** [`893052837ad68512fcc161f5d0764c420054644f`](https://github.com/imsankalp/phD-application-tracker/commit/893052837ad68512fcc161f5d0764c420054644f) | **Branch:** `main` | **State:** DEEP_REVIEW_DOCUMENTED (static; runtime not executed) | **Decision:** adapt carefully for mailbox-derived application events; reject its current submission and OAuth security semantics.

## 1. Purpose and code inventory

A Node.js/Express 4 + Mongoose 5/MongoDB PhD application tracker with local username/password authentication, Google OAuth for read-only Gmail access, REST CRUD over owner-scoped applications, and manual Gmail sync. The README and API/FLOW diagrams describe an intended mobile frontend, but no mobile frontend code exists in the inspected 33-entry repository tree. The repository last changed 2025-09-02. No issues, pull requests, test suite or GitHub Actions runs were returned. `package.json` declares MIT; no separate LICENSE file was found.

The code has real API and database paths, but the README's “write tests” language is a setup instruction, not evidence of implemented tests: `npm test` executes `echo "No tests specified" && exit 0`.

## 2. End-to-end architecture

**Identity:** `/auth/register` creates a bcrypt-hashed password; `/auth/login` verifies it; both issue 7-day JWTs. `isAuthenticated` verifies the bearer JWT. Application queries use `user: req.user.id` predicates, so reads/deletes are owner filtered.

**Gmail linking:** unauthenticated `GET /auth/google/initiate` generates a Google OAuth URL using `gmail.readonly`, `userinfo.email`, and `userinfo.profile`; the callback exchanges the authorization code, gets Google profile data, finds/creates a local user by Google ID or email and saves access/refresh tokens in the MongoDB User record. It responds with a local JWT.

**Email sync:** authenticated `POST /api/applications/sync` obtains the caller's saved refresh token; `GmailService.listMessages()` requests up to 25 Gmail messages matching `subject:PhD`, retrieves each full message, picks a MIME body and applies a simple regex parser for application ID, status and interview date. The controller upserts one Application per `(user, sourceEmailId)` lookup. Manual CRUD is exposed at `/api/applications`.

**Data model:** Application has owner, applicant name, university, program, application ID, enum state (Submitted/Under Review/Accepted/Rejected), interview and submission dates, notes and sourceEmailId. User contains username, email, optional password, Google ID, and Google access/refresh token data.

## 3. Critical evidence/identity defects

**Unverified submission state:** `src/models/Application.js` defaults `applicationStatus` to `Submitted` and `submissionDate` to the current time. `syncFromGmail()` also defaults any unparsed Gmail status to `Submitted`, and fills submissionDate with current time. Merely finding an email matching `subject:PhD` can therefore create a submitted application without a portal receipt or even a parsed application ID. This is not valid evidence of submission.

**Parser/schema mismatch:** the status regex `/Status: (\w+)/` captures only a single word, so an email line `Status: Under Review` yields `Under`, which is not a valid schema enum. Gmail sync can fail or persist unexpected data depending on update validation settings. The parser does not independently establish the sending institution, applicant, target cycle, legitimate application identifier or source authenticity.

**Gmail incompleteness:** the default mailbox query is a narrow subject phrase with a first page of at most 25 messages. There is no pagination loop, history ID, full-message thread/attachment handling or incremental watermark. It may miss most submissions and relevant replies and can ingest irrelevant PhD-related messages. `getMessageBody()` scans only first-level MIME parts; deeply nested multipart or attached proof can be missed. The extraction result has no field-level provenance or review gate.

**Idempotency gap:** `sourceEmailId` is indexed but not unique, while the controller uses `findOneAndUpdate({ user, sourceEmailId }, ..., { upsert: true })`. Concurrent sync requests can generate duplicates without a compound unique index. It also counts all returned upserts as “synced”, not distinct verified applications.

## 4. Authorization and OAuth risks

- Owner-filtered query predicates are positive, but `updateApplication()` passes the entire client `req.body` to Mongoose `findOneAndUpdate`. Without a strict update allowlist, a user may change server-owned `user` or `sourceEmailId` fields on an owned record; this can transfer/corrupt records across ownership boundaries. Use explicit field schemas and immutable owner fields.
- `googleInitiate()` does not set an OAuth `state` value, and the callback does not verify a state or tie a consent attempt to an authenticated local account. This undermines CSRF and account-linking security. A Google identity is verified via Google's userinfo endpoint, but that does not repair the missing account-linking state.
- Access and refresh tokens are stored directly as MongoDB document fields without an application-level encrypted secret envelope or rotation policy. The Gmail scope is read-only, which limits sending capability but not mailbox disclosure.
- Authentication has no rate limiting or account lockout in the inspected code, and `logout` cannot revoke an unexpired JWT.
- Controllers frequently expose raw `err.message` in HTTP 500 payloads. This can leak implementation or provider details.
- The README claims mobile consumption, but actual client-side secure-token storage and OAuth redirect handling are not implemented in this repository.

These are static trust-boundary findings, not exploit-tested results.

## 5. Operational deficiencies

`server.js` connects to MongoDB on startup and starts Express after the connection resolves; it does not implement structured migrations, indexes beyond Mongoose schema defaults, production config qualification, rate limits, retries or deployment health checks. The config contains legacy Mongo connection options. The `.env.example` uses `DATABASE_URL`, whereas the code requires `MONGODB_URI`, a setup mismatch.

The API reference lists status/interview helper controller methods, but no matching special routes were registered in `src/routes/api.js`. The protocol's “sync” response is not proof of an accepted application.

No runtime test, mailbox authorization, token exchange, database migration, request-level abuse test, or provider interaction was performed by this audit.

## 6. Transferable model for the admissions workspace

The useful ideas are owner-scoped CRUD, Gmail read-only consent, source-message IDs, incremental evidence ingestion, and the separation of manual records from mail observations. Rebuild these with:

1. A distinct `MailObservation` entity keyed by authenticated mailbox + immutable message ID and indexed uniqueness.
2. Verified sender/domain context, original message/thread IDs, received timestamps and raw evidence pointers (private only).
3. A conservative event classifier that yields `UNCONFIRMED` for unrecognized messages; only receipt-backed events may transition an application to `SUBMITTED`.
4. Independent application identity and event history; one email is not necessarily one application.
5. Gmail pagination/history, rate limits, bounded retries, MIME handling and catch-up cursors.
6. OAuth state/PKCE where supported, account-bound consent and encrypted token storage.
7. Immutable ownership and validated field-level mutation allowlists.
8. Privacy retention rules and user-initiated disconnect/deletion.

## 7. Pinned evidence

- [Express router](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/routes/api.js)
- [Application controller and Gmail upsert](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/controllers/applicationController.js)
- [Google OAuth and local login](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/controllers/userController.js)
- [User token model](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/models/User.js)
- [Application state schema](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/models/Application.js)
- [Gmail fetch and parser](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/services/gmailService.js)
- [Regex extraction](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/src/utils/emailParser.js)
- [API documentation](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/docs/API.md)
- [Package and test script](https://github.com/imsankalp/phD-application-tracker/blob/893052837ad68512fcc161f5d0764c420054644f/package.json)

## 8. Disposition and evidence boundary

**DEEP_REVIEW_DOCUMENTED (static)**. The concrete authentication, OAuth, Gmail sync, parsing, data-model, API and operational paths were inspected at the pinned commit. Runtime tests and actual mailbox/source verification were **NOT_PERFORMED**. The existing implementation cannot independently prove an application was submitted or accepted.
