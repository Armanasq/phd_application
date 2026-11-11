# D2Simon/PhDHub — supplemental implementation investigation

- Existing canonical pin: `45a1c666b7d9712a96f1b712c276e2c47d3595f2`
- Additional files inspected: `phdhub/storage.py`, `docker-compose.yml`, and the previously cited email sync and AI service paths.
- Status: supplemental static security/privacy review; no runtime or security test performed.

## Storage semantics

The storage helper reads and writes whole JSON files for configuration, applicant database, manually entered Lite-mode emails, templates, interview reviews and verbal offers. This is simple and inspectable for a single-user desktop workflow, but it lacks transactional updates, concurrent-write protection, schema migrations, indexed queries and durable event history. A crash during a whole-file write can corrupt the only copy unless writes are made atomic and backed up.

The Compose configuration publishes the Streamlit service on a configurable host port and binds it to `0.0.0.0`; the data directory is a named volume. Persistence is therefore present, but network exposure is not restricted by the compose file itself.

## Email and AI trust boundary

The application combines private applicant documents and mailbox contents with AI processing. Email bodies and fetched web pages must be treated as untrusted data. Prompt instructions inside those materials must never be allowed to change agent policy or trigger external communication. Email classification should distinguish sender identity/authentication from message content; a model instruction to assume all messages are legitimate is not an adequate security policy.

## Transfer to Atlas

Keep the integrated outreach/email/interview workflow as a product concept, but separate:
- public opportunity evidence;
- private applicant profile and documents;
- mailbox content and message metadata;
- generated drafts;
- externally sent communication and submission proof.

Use encrypted secret storage, authenticated access, atomic database transactions, immutable send/submission events, explicit AI-data consent and a safe URL fetcher. Require user confirmation before any outbound email or application submission.

## Outstanding validation

No file-locking, crash recovery, backup/restore, prompt-injection, SSRF, auth bypass, or live IMAP tests were executed. The four closed GitHub issues do not establish these controls.
