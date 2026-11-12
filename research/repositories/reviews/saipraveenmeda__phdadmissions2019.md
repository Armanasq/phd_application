# saiPraveenMeda/phdAdmissions2019 — pinned source investigation

- Revision: `e33181b3c670b58650c88a4981187ca16d3c7939`
- Inspected on: 2026-11-12
- State: **DEEP_REVIEW_DOCUMENTED — risk-focused static; no runtime or private-file testing**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: RECORDED (source-level, not independently validated)

### Earlier preliminary note 1 — Purpose

Legacy Django 1.11 / Python 2.7 institutional admissions form with payment, registration, recruitment and scrutiny routes.

### Earlier preliminary note 2 — Architecture

Git tree includes a committed virtual environment plus logs and uploaded-record-related directories; those records/logs were NOT read.

### Earlier preliminary note 3 — Data flow

facultyForm/settings.py commits a Django SECRET_KEY and configures DEBUG=True, ALLOWED_HOSTS=['*']; no secret literal is copied into this review.

### Earlier preliminary note 4 — Critical correctness

recruit/models.py defines private applicant, educational, research, disability/category and payment documents; recruit/views.py enforces application stages but file extensions are not content scanning.

### Earlier preliminary note 5 — Identity and state

Project is neither a live PhD job feed nor a safe deployable template. Priorities: secret rotation, modern supported runtime, strict hosts, private storage and authorization review; runtime NOT executed.

## Pinned upstream source paths

- [facultyForm/settings.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/facultyForm/settings.py)
- [recruit/models.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/models.py)
- [recruit/views.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/views.py)

## Deep static investigation — 2026-11-12

**Review status:** DEEP_REVIEW_DOCUMENTED — security- and workflow-focused source review of project code; no runtime testing or applicant records. **Disposition:** BLOCK production reuse without a security redesign.

## 1. Scope and source provenance

The pinned commit [e33181b3c670b58650c88a4981187ca16d3c7939](https://github.com/saiPraveenMeda/phdAdmissions2019/commit/e33181b3c670b58650c88a4981187ca16d3c7939) is a 2019-era institutional admissions implementation, not a source of current recruiting vacancies. The recursive Git tree contains 625 blobs, heavily inflated by a committed Python 2.7 virtual environment, vendored packages and static administration assets. The first-party application consists of Django apps for registration, recruit, scrutiny and payment plus their URL maps, migrations and Django templates. Its README is only a stub. No vendored packages, historical log messages, applicant records, private archival documents or PDF contents were read.

## 2. Architecture, entities and stage transitions

The project uses Django 1.11.4, Python 2-era runtime assumptions and an external `confidential` module for database and payment secrets. `recruit/models.py` defines `Appdata` (applicant, department, post type, verification, shortlisting and submission state), separate `GeneralData`, `Education`, `QualifyingExamDetails`, `Research`, `Experience`, `Other`, annexures, `Document` and `PaymentDetails`; `Flag` holds file/step completeness booleans. Uploaded applicant materials are stored under a per-application path and surfaced through `FieldFile.url`. `registration/views.py` creates a Django user and unique application ID, puts the user in the Applicant group, stores payment information and emails registration acknowledgment. Applicant routes collect personal history, academic qualifications, documents and research experience; after a receipt is uploaded and flags are set, `recruit.submit` marks an application submitted and sends acknowledgment. `scrutiny/views.py` offers Dean verification and HOD shortlisting, plus a staff report.

Relevant source: [models](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/models.py), [registration views](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/registration/views.py), [recruit views](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/views.py), [scrutiny views](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/scrutiny/views.py).

## 3. Critical source-level security and correctness findings

- **Unsafe deployment configuration.** `facultyForm/settings.py` publishes a Django secret value, sets `DEBUG=True` and `ALLOWED_HOSTS=['*']`; secure cookie settings are commented out. The tracked virtual environment and frozen 2017 dependencies are not a supported modern deployment baseline. The actual public service exposure is **unverified**.
- **Unauthenticated password reset by identifier.** `registration.forgotPassword` accepts an application ID, immediately resets the associated Django user's password, creates it with `random.choice` rather than a cryptographically secure reset token, then sends the new password by email. It does not authenticate ownership of the email address or require a single-use expiring confirmation. This facilitates account disruption and account-recovery risk; no attack was attempted.
- **Submission on GET.** `recruit.submit` requires a logged-in Applicant, but lacks a request-method guard. Once completeness flags are satisfied, merely visiting the endpoint causes `submitted=True`, sets a timestamp and sends an email. This is a state-changing GET, inconsistent with CSRF-safe method semantics and explicit applicant approval.
- **Staff scope enforcement is inconsistent.** `scrutiny.viewApplication` enforces department scope for HOD users, but `shortlistApplication` and `unshortlistApplication` check only the HOD role and a supplied application ID, not that `app.post_in` equals the staff member's department. `unshortlistApplication` mutates on GET. `verifyApplication` also mutates on GET (Dean-only). There is no source-supported departmental access control on these write paths.
- **Payment initialization defects.** `payment.views.GoToTransaction` sets `response['txnid'] = uuid4.hex()` even though `uuid4` is an imported **function**, not a UUID object; this appears to raise `AttributeError`. `_get_hash` calls `get_hash`, but that function's import is commented out and no definition is present in the module, so the next step also appears broken. `TransactionSuccess` merely returns a string and does not inspect a verified gateway callback in this module. These are static defects, not runtime-tested failures.
- **Uploaded receipt does not prove payment.** In `registration.paymentDetails`, `paymentUploaded` becomes true after a PDF-shaped receipt appears on disk. Its value is therefore evidence of upload, not confirmation from a bank/payment processor. Treating this as “paid” or “eligible to submit” without verified settlement is a trust-boundary error.
- **Document validation and exposure.** `validateFormat` checks only the filename extension `.pdf`, and `validatePic` only `.jpg`. No content sniffing, antivirus scan, upload size cap or private authenticated download handler was observed. The root URL configuration maps `MEDIA_URL` through Django's static helper; with debug enabled, a direct media URL may bypass per-document view authorization. Do not assume any real server currently exposes these files.
- **Non-atomic application identity.** `registration.createApp` increments `Department.appCount` and saves its value to derive an application ID without an observed row lock or encompassing transaction; concurrent registrations can race on generated identifiers and leave partial related records if a later step fails.
- **Import-time application calendar.** `payment.models.Category` uses `default=datetime.now()` for start and end values, which computes shared defaults at module import rather than independently at instance creation.
- **Sensitive lifecycle without tests.** The code handles identity, contact, education, qualifying scores, disability/caste fields and scanned documents. Existing app test modules are Django skeleton stubs; no proven workflow/regression/security CI was observed. Source-level gate/URL checks cannot substitute for end-to-end authorization tests.

## 4. Trust, evidence and limits

Institutional branding, historical department routes and recorded payment fields do not prove that any 2026/27 doctoral intake exists, remains open, is funded or can produce an offer. There is no evidence that this repository is the active operator-controlled NIT Warangal site in November 2026; the commit is historic. No historic personal records, logs or payments were examined or copied. No credentials or credential values are reproduced in this audit. The source uses Django's built-in password hashing on registration, so its problem is specifically the reset-and-email workflow rather than a blanket claim of plaintext database passwords.

## 5. Interconnections and reuse decisions

Compared with the earlier [tarun14110/system-for-PhD-Admissions](https://github.com/tarun14110/system-for-PhD-Admissions) flat-file Java prototype, this implementation has richer normalized domain models, Django authentication groups, per-application file paths, completion flags, payment objects and staff-review stages. However, these structures coexist with inadequate trust separation in payment verification, reset identity, document access and HOD write authorization. Compared with [syedpeera/Phd-Admissions-NITPY](https://github.com/syedpeera/Phd-Admissions-NITPY), it has more explicit model and role separation but remains unsuitable for deployment.

For an applicant-controlled PhD research workspace, the useful abstractions are a typed evidence/document inventory, stage-specific status transitions and user-visible acknowledgment identifiers. Do **not** import code or any personal data. A modern implementation requires current supported Django/Python, secrets rotation, canonical applicant identity, one-time reset tokens, atomic identifier generation, explicit authenticated file download, content and size validation, per-department object authorization on every read/write, idempotent POST-only transitions, verified processor settlement, append-only review audit logs, and test fixtures using synthetic records.


## 6. Release blockers and remediation sequencing

A safe redesign must start with credential rotation and a supported runtime; remove any published secret, disable debug mode, restrict canonical hosts and require TLS-protected cookies and file access. Next, replace password-by-email resets with cryptographically secure, single-use, short-lived tokens and verify applicant identity before changes. Enforce object-scoped review permissions, POST-only idempotent verification/shortlisting/submit handlers and a permanent audit history. Application IDs should use database-backed unique constraints and atomic transactions, and uploaded document metadata must be independently validated before persistence. Payment-settled state must derive from a verified provider transaction, not a user-supplied receipt. No production approval should be granted based on these sources without deterministic tests for these boundaries.

## 7. Source and transfer controls for PhD application research

The repository's registrar-side stages can inform an applicant workflow only if a locally saved form, a completed portal submission, a received acknowledgment, a verified payment and an actual offer are modeled as different events. The archived 2019 institution rules and example template fields are not valid 2026–27 international funding conditions. An external recommendation system needs institution-controlled pages, valid-cycle checks, source hashes, funding category/currency and approved student-class eligibility before creating an actionable opportunity. The review deliberately preserves the earlier preliminary assessment and does not ingest any archival student record or operational secret.

## 8. Verification coverage

Inspected the pinned 625-blob tree to identify first-party versus vendor/material files; read Django settings and URL routing, requirements, the main registration, recruit, scrutiny and payment models/views, admin configuration, method guards, file validation helpers, payment callbacks, and empty test stubs. Read app code but **not** the included archived logs, historical applicant data, uploaded documents, external institution pages, binary assets or vendored dependencies. No installation, database migration, application execution, payment attempt, penetration test or email action was performed. Findings are statically supported risks and likely defects; runtime behavior and deployment exposure remain unverified.
