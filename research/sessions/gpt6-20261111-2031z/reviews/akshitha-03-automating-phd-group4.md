# Repository review: Akshitha-03/Automating_PhD_Group4

## Review disposition
- Depth: deep static source review of an educational prototype; not runtime-tested.
- Pinned upstream commit: e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298.
- Tracked files: 48; mostly HTML/CSS/JavaScript plus PDF project report; no automated tests or CI.
- Last pushed: 2022-06-15. No issues, pull requests, or declared license.

## Purpose
An educational PhD-admissions workflow prototype for applicants, faculty, and administrators. Its reported goal is to automate applicant registration, document submission, faculty selection, payment, review, and admission-related communication. The PDF report was inspected for stated requirements and architecture; code was examined to distinguish those claims from actual implementation.

## Implemented architecture
The project is a multi-page client-side web application with Firebase Realtime Database and Firebase Authentication. The JavaScript is embedded in HTML pages and separate script files. There is no server-side API layer, no repository-visible database rules, and no deployment configuration proving production security.

Main flows:
1. Applicant and faculty registration/login through Firebase Authentication.
2. Applicant personal and educational detail collection.
3. Application/request submission, including faculty preference.
4. Payment page with UI controls.
5. Faculty/admin views that query applicant data and display/sort records.
6. Applicant and faculty status pages.

Data is written to Firebase Realtime Database paths from browser code. The UI includes personal and educational records; their confidentiality depends on Firebase rules that are not present in the repository.

## Source-level findings

### 1. Client-side role trust
The reviewed code relies on browser-side navigation and Firebase-authenticated sessions. It does not demonstrate server-side enforcement that an authenticated faculty user can only view or modify authorized applicants, or that an administrator is actually authorized for privileged operations. Without restrictive Firebase rules, role-based UI alone is not a security boundary.

### 2. Missing database security rules
No database.rules.json or equivalent deployable Firebase Realtime Database policy was found. The repository therefore cannot establish whether applicant data is protected by owner, faculty assignment, or administrative role. This is a verification gap with potentially high impact, not proof that the deployed database is publicly readable.

### 3. Payment UI is not payment verification
The payment-related HTML/JS presents fields and submission behavior, but no verified payment gateway integration, server-side webhook, signed transaction validation, or payment reconciliation workflow was found. It should not be classified as a production payment implementation.

### 4. Incomplete validation and transactional workflow
Applicant and faculty data is written across separate browser operations. No database transaction protocol, explicit application state machine, idempotency key, or reliable resume/retry semantics were identified. The interface can present progress without a durable, auditable admission-stage transition.

### 5. Evidence and admissions decisions are not traceable
The project does not store official-source provenance for program deadlines, requirements, funding, or faculty research claims. It also lacks structured decision explanations and versioned review criteria. Its workflow should not be used to infer admission likelihood or institutional policy.

### 6. Tests and reproducibility
There is no test suite, dependency lockfile, automated CI, reproducible deployment manifest, or evidence of successful integration testing in the repository. The PDF report describes intended behavior but is not runtime evidence.

## Reusable patterns
- Applicant, faculty, and administrator roles as distinct actors.
- Separate application stages for profile, education, document collection, review, and decision.
- Role-specific views and faculty preference workflow.
- Form-level collection of structured applicant information.

## What should not be reused
- Browser-side authorization assumptions.
- Unverified payment collection.
- Direct access to sensitive application records without auditable policies.
- State changes without transaction, ownership, and provenance controls.

## Recommended architecture for a serious system
Use a typed backend API with authenticated identities, enforced RBAC/ABAC, audited state transitions, scoped document storage, verified payment-provider webhooks, immutable submission snapshots, and separate official-source evidence for each program requirement. Applicant and faculty data must be access-controlled and retained under a documented privacy policy.

## Evidence and coverage
- Repository: https://github.com/Akshitha-03/Automating_PhD_Group4/tree/e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298
- Source inspected: index.js, sindex.js, script.js, script1.js, registration/login, personal/education, applicant, faculty/admin, payment, request, sorting, and detail pages; project PDF examined for architecture and intended workflow.
- Static review completed; Firebase rules, actual deployed database, runtime behavior, and payment processing could not be verified.