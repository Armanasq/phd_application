# daytime001/Bulk-Email-Sender — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [dc910caf400a27a17a7534bdb1bb4b5ad504d227](https://github.com/daytime001/Bulk-Email-Sender/commit/dc910caf400a27a17a7534bdb1bb4b5ad504d227).  
**Review state:** DEEP_REVIEW_DOCUMENTED, static source and test inspection; no email or tests executed.  
**Verdict:** adapt workflow concepts with explicit consent and delivery guarantees; do not reuse send path unchanged.

## 1. Purpose and scope

A cross-platform professor-outreach and bulk personalized email tool, with a Python sending engine, JSON/XLSX recipient import, email templates, attachments, local send history, and a Tauri/Rust/React desktop UI. It is not a professor availability verifier, recommendation generator, or graduate-application submission service. The inspected repository has 89 files, a documented MIT license and multiple unit/integration-test source files.

## 2. Architecture and dataflow

The desktop layer invokes Tauri commands, which spawn a Python worker for actual SMTP transmission. The worker receives a typed `JobConfig`: sender, SMTP configuration, recipients, message template, attachments and options. The Python `SendEngine` renders `teacher_name` and `research_direction` variables, builds multipart email with attachments, connects to SMTP, transmits, appends a sent-history JSONL row, then emits per-recipient events. The desktop code tracks one active child worker through a mutex. Import supports JSON and XLSX, email/name validation, and duplicate detection.

## 3. Deliverability and idempotency analysis

A JSONL `SentStore` records `email`, `teacher_name`, `job_id` and UTC `sent_at`. `is_sent(email)` deduplicates *globally by normalized address*, rather than by campaign or actual recipient/message intent. This can suppress legitimate later follow-ups but is not an auditable conversation history.

There is no atomic transaction across SMTP delivery and local append. If the server accepts an email and the append fails, a subsequent retry can resend it. If the connection breaks after SMTP acceptance but before the client receives confirmation, the `SMTPClient.send` exception-handling path reconnects and attempts transmission again for broad `SMTPException` classes. Such exceptions do not prove non-delivery. A retry or worker restart can therefore duplicate outreach.

The engine's inter-send delays and optional recipient randomization are straightforward operational throttles; they do not establish per-domain rate limits, user consent, provider sending-policy compliance, or email quality.

## 4. Applicant approval and safety boundary

The low-level `SendEngine.send` transmits as soon as a job is passed. No per-recipient verified supervisor identity, explicit approved-draft transition, attachment manifest approval or externally verifiable consent receipt is enforced by that engine. The existence of a desktop UI is not evidence of server-side approval guarantees.

Attachments are arbitrary local files resolved by path and checked for existence. Restrict this to user-confirmed private files and a final attachment preview. Transcripts, visa documents and recommendation letters must never be attached implicitly.

## 5. Configuration and sensitive information

SMTP username/password are passed in a runtime payload. The Tauri desktop implementation also accepts arbitrary app-draft JSON and writes it to local `config/app_draft.json` without evidence of credential-specific filtering or encrypted storage at that boundary. Whether the UI actually persists credentials there needs a separate frontend field audit; treat sensitive content in draft state as a risk, not a confirmed leak.

The desktop supports runtime Python installation through configurable remote manifests and archive downloads; download checksum validation is present for remote bundles, but an attacker-controlled manifest and matching checksum do not by themselves establish publisher authenticity. Verify trusted manifest origin, signing and file extraction guards before deploying auto-install to research applicants.

## 6. Tests, operations and code quality

Test files cover event emission, retries, templating, SMTP integration, worker protocol, recipient loader, sent-record persistence and runtime packaging. These are meaningful positive test designs. The review inspected test source and found code asserting recipient suppression and SMTP retry. No tests were executed, and their presence does not prove the current default branch passes. Tauri event-driven worker management is a useful separation of UI from network side effects.

## 7. Evidence and validation limits

Source-level inspection supports the non-transactional delivery and global-address suppression claims. Actual provider acceptance, duplicate delivery frequency, signed-runtime provenance, credential persistence, UI usability, and production email policy adherence were not established. No email messages were sent or professor identities validated.

Pinned evidence: [engine](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/engine.py), [SMTP client](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/smtp_client.py), [sent store](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/sent_store.py), [models](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/bulk_email_sender/models.py), [Tauri backend](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/apps/desktop/src-tauri/src/lib.rs), [engine tests](https://github.com/daytime001/Bulk-Email-Sender/blob/dc910caf400a27a17a7534bdb1bb4b5ad504d227/tests/test_engine_events.py).

## 8. Transfer decision for PhD Atlas

Keep supervisor identity/evidence discovery, applicant-written drafts, human approval, delivery state and reply tracking as separate stages. Use approved draft and explicit recipient/attachment manifest before send. For irreversible delivery, implement transactional outbox, stable message ID, SMTP outcome categories including `UNKNOWN_DELIVERY`, reconciliation, bounded retries and a complete event trail. A bulk sending application is not proof a supervisor is recruiting or willing to accept an applicant.
