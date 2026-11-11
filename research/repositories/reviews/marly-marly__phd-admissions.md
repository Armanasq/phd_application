# marly-marly/phd-admissions — deep static admissions workflow and privacy audit

**Reviewed:** 2026-11-12. **Pinned upstream:** [4a09e4fe5293310986b6b68ceb8b9cbba263f3ca](https://github.com/marly-marly/phd-admissions/commit/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca).  
**State:** DEEP_REVIEW_DOCUMENTED — code/models/roles/API/download/email/test source inspected; runtime NOT_TESTED.  
**Verdict:** valuable admissions-admin domain model, unsafe for production deployment as-is due to serious document-authorization defects.

## 1. Scope and domain

A 2017-era Django/DRF administrative PhD admissions web application, built around applications, research subjects, academic years, supervisor assignments, comments, file attachments, funding options/status, application decisions, user roles, administrator emails and CSV/ZIP exports. It is an internal institution workflow implementation, **not** a program discovery or live funding opportunity directory. The source tree includes many API tests and a bare one-line README.

## 2. Models and event flow

`Application` has unique registry reference, academic year, supervisor relationships, demographics, origin, field, funding paths (self/DTP/CDT/project etc.), status (pending/accepted/rejected/withdrawn/deferred), admin and PhD admission tutor comments. `Supervision` links staff to applicants, and `Documentation` links files to supervision records. This separation offers a mature admissions domain decomposition and department-specific funding options.

Application create/update/delete methods require JWT authentication plus administrator role; tests exercise basic CRUD, supervision and searching. No explicit immutable decision audit log, evidence for funding award, optimistic versioning or lifecycle rule engine was established.

## 3. High-severity applicant document authorization defect

`FileView.post` requires **any authenticated user** but does **not** check whether the user is an administrator or is assigned to the target `Supervision`. It accepts any valid `supervision_id` and creates file objects under that supervision. This allows an authenticated staff account to attach unrelated documents to other applicants, at least at the source-authorization level.

`ApplicationView.get` returns any application by numeric ID for an authenticated user without checking the requesting user's supervision membership or admin role. It returns application demographics/comments and serialized supervision/document metadata. The route's authentication does not establish applicant-level authorization.

`DownloadView` and ZIP/CSV export endpoints declare DRF `AllowAny` and accept a JWT supplied in the URL query string. The file download validates only token decode and username, then serves **any** supplied document ID; it does not check that the token owner is assigned to that document or has an authorized role. ZIP/CSV similarly verify token validity but not row-level authorization for requested application IDs. Signed JWT URLs can also leak through logs, browsing history and referrer handling. This is an implementation-level broken object authorization/IDOR risk; no live exploitation was attempted.

## 4. Authentication and configuration risks

`assets/settings.py` commits a literal Django `SECRET_KEY`, enables `DEBUG=True`, uses `ALLOWED_HOSTS=['*']`, and sets `JWT_VERIFY_EXPIRATION=False`. Hardcoded database credentials and a plaintext SMTP configuration also appear in the inspected settings. These are significant security defects for a system handling reference letters and transcripts; secret values are **deliberately not reproduced** in the review.

JWT expiry disabled means a leaked token can persist until another revocation mechanism (if any) invalidates it; no such mechanism was established in the examined paths. An authenticated-token requirement alone does not justify returning all applicants' confidential records.

## 5. Email and notification semantics

`SendEmailView.post` requires an admin role, constructs supervisor emails from a template plus applicant details and uses Django SMTP to transmit. There is no durable transactional outbox, per-message send receipt or visible idempotency key; a retry after ambiguous SMTP acceptance can send duplicates. The email template may incorporate HTML content, and a supervisor/recipient approval preview flow is implemented in other routes, but the send method accepts a caller-supplied template directly.

The source preserves no explicit confirmed applicant consent to emailing their identifying details. A production solution needs a policy boundary and an event history for admissions decisions and notifications.

## 6. File and export integrity

The document upload path includes a registry reference, file type and submitted filename, with collision-based numeric suffixes. It does not show a modern content-type/size policy, antivirus scanning or private object-store signing. ZIP exports iterate all requested applications and add document file contents in-memory; large selections can exhaust memory and the lack of row authorization can expose third-party files. The CSV renderer accepts caller-selected fields and sorts, and should validate the allowed field list.

The ORM's `possible_funding` multiselect has pending/awarded statuses, but no amount, currency, stipend duration, tuition coverage or award official-source evidence. Department-specific funding route != verified fully funded international position.

## 7. Verification boundary

Inspected core model, supervision, permissions, application CRUD, email, documents, settings and application tests. Test files demonstrate expected workflows, but no unit/integration tests, old Django dependencies, upload, email, LDAP authentication or live endpoint were executed. Thus risk statements describe source-level authorization and deployment misconfiguration, not confirmed current exploitability or a presently hosted service.

Pinned evidence: [settings](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/assets/settings.py), [document routes](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/phdadmissions/views/documentations.py), [application routes](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/phdadmissions/views/applications.py), [application model](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/phdadmissions/models/application.py), [email service](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/phdadmissions/views/email.py), [tests](https://github.com/marly-marly/phd-admissions/blob/4a09e4fe5293310986b6b68ceb8b9cbba263f3ca/website/phdadmissions/tests/test_applications.py).

## 8. Transfer to PhD Atlas

Adopt separate admission application, department/year, supervisor relationship, document type, award pathway and decision states. Do not copy the authentication or file APIs. Require per-applicant object-level authorization for **all read/write/export endpoints**, short-lived scoped download tokens, encrypted/private file storage, secure secrets, audited retention, immutable status transitions, and idempotent outbox before any institutional deployment.
