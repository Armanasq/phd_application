# Akshitha-03/Automating_PhD_Group4 — deep static admissions workflow audit

**Review:** 2026-11-12 | **Upstream:** https://github.com/Akshitha-03/Automating_PhD_Group4 | **Pinned revision:** [`e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298`](https://github.com/Akshitha-03/Automating_PhD_Group4/commit/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298) | **State:** DEEP_REVIEW_DOCUMENTED (static inspection only) | **Verdict:** reject implementation as-is; model distinct applicant/faculty/admin stages only.

## 1. Objective and provenance

A 2022 student software-engineering prototype intended to automate PhD admissions for educational institutes using registration, applicant identity, academic details, faculty selection, payment and stage-status views. The 48-entry repository includes HTML, CSS, JavaScript, graphics and a project PDF. The README names student team responsibilities, but this is not evidence of production institutional adoption. No deployable Firebase security rules, automated tests, CI or license file appear in the inspected tree.

A parallel research session's [static findings](https://github.com/Armanasq/phd_application/blob/main/research/sessions/gpt6-20261111-2031z/reviews/akshitha-03-automating-phd-group4.md) were reconciled against this session's independent inspection of the repository tree, README, applicant/faculty auth scripts, admin entry, payment form and personal information writer. The PDF's claimed design was reported by the earlier session; its contents were **not re-opened** here.

## 2. Architecture and dataflow

The browser pages load Firebase v8 client SDK and use Firebase Authentication and Realtime Database. `sindex.js` registers student applicants and writes account-linked data beneath `Applicant/{uid}`; `index.js` writes faculty account data to `Faculty/{uid}`. `script.js` collects personal information and writes new entries under `ApplicantPersonal` using `.push().set(...)` from client code. Other HTML pages present education, faculty, request, sorting and application status flows.

There is no separate server API in the tracked source to enforce action authorization or issue server-verifiable admission receipts. The database itself may have external rules, but their deployed configuration is not bundled in this repository.

## 3. Identity and administrator authorization

The `admin.html` login UI compares entered username/password against **hardcoded credentials in a client-side inline script**, then redirects to `admin2.html`. These values can be read by anyone with the HTML source; a redirect is not an authorization boundary. For any real privileged data operation, access must be enforced by backend/Realtime Database rules using authenticated identities, not navigation hiding or a JavaScript predicate. No evidence was found that source-level administrator access rules are enforced.

The Firebase student/faculty login establishes authentication, but not an institution-verified faculty role, assigned applicant scope, or administrator permission. A lack of published database rules is an **unknown deployment protection state**, not proof that the live database is readable by anonymous users.

## 4. Sensitive applicant form handling

The inspected `script.js` captures personal contact details, family contact and a government identity number field and writes them directly to a general-purpose `ApplicantPersonal` collection. The source does not demonstrate a server-owned document ID/keyed owner link, data minimization, access control, encryption-at-rest policy, retention or privacy consent enforcement. The UI reports form success without awaiting an authoritative, independently verifiable completion event.

Sensitive fields should not be copied into a public Git corpus, nor should this code be adapted without a privacy/legal basis and owner-authorized data storage. No real applicant data was accessed or copied during this review.

## 5. Payment implementation and receipt evidence

The `payment_f.html` page contains card number, expiry and CVV inputs with a cosmetic card flip and a “pay” submit button. The inspected HTML/JavaScript mirrors entered payment values in DOM elements; it does **not** show a provider-backed tokenization, 3-D Secure, verified charge, signed webhook or immutable payment receipt. It must never be treated as validated fee collection. Direct card-data handling has substantial compliance implications.

Do not execute or deploy this UI for actual card collection. A production admissions system should use a compliant payment processor with server-side reconciliation and no raw card/CVV storage.

## 6. State machine, evidence and tests

Applicant, faculty, administrator, request and decision states are only loosely coupled across client-side operations. No immutable admission event stream, concurrency control, document submission confirmation, fee receipt gating or formal program/degree requirement register is provided. Changes can appear to progress in the UI without an auditable institution-signed decision.

Repository tests, CI, deployment manifests, database migrations and incident response documentation were not located. The source does not establish acceptance rates, funded doctoral vacancies, actual institutional approval or current eligibility policy.

## 7. Reusable architecture after redesign

Retain only the actor/stage decomposition and the explicit document/education form sequence. A production version requires authenticated and authorized staff identities; strict server-side RBAC/ABAC and applicant row scoping; object storage for private files; exact-stage state transitions tied to signed institution evidence; audit logs, idempotency and retry semantics; payment-provider webhooks and signed receipts; explicit consent and data-retention controls; program criteria grounded in current official rules.

An application being filled, stored, or routed to an administrator is not proof of admission, submission, fee payment or offer.

## 8. Evidence and verification limits

- [README](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/README.md)
- [Student account Firebase path](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/sindex.js)
- [Faculty account Firebase path](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/index.js)
- [Personal information writer](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/script.js)
- [Client-side administrator entry](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/admin.html)
- [Payment UI](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/payment_f.html)
- [Source project report path](https://github.com/Akshitha-03/Automating_PhD_Group4/blob/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298/PhD_Admission_Grp4.pdf)

**DEEP_REVIEW_DOCUMENTED — static source only.** Critical code paths and all relevant tracked source types were inspected; no live authentication, payment, Firebase database access, PDF re-render, card submission, or runtime test was performed. Actual external database rules/hosting remain unknown. No credential literals or applicant records are reproduced.
