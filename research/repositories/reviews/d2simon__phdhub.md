# D2Simon/PhDHub — focused source and deployment review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [45a1c666b7d9712a96f1b712c276e2c47d3595f2](https://github.com/D2Simon/PhDHub/commit/45a1c666b7d9712a96f1b712c276e2c47d3595f2); latest commit observed 2026-07-23.
- **Category:** local-first Streamlit applicant CRM, email intelligence and interview workspace.
- **Review state:** DEEP_REVIEW_DOCUMENTED. Core static source audit of private document, email, network and deployment boundaries; not exhaustive line-by-line review or independent runtime validation.
- **GitHub issues:** four issues observed, all closed. No test suite was executed or established by this review.
- **License:** no explicit license metadata or license file confirmed in this pass.

## 1. Problem and product scope

PhDHub joins CV/RP PDF management, supervisor records, outreach tracking, IMAP email retrieval, AI email classification, interview preparation and application follow-up in one local workspace. It is one of the more complete applicant-workflow concepts in the screened set.

## 2. Architecture and data flow

A Streamlit application reads/writes local JSON-backed storage under a configurable data directory. Docker persists that directory in a named volume. IMAP over SSL retrieves inbox messages; the background worker stores message bodies and classification results in a JSON cache. AI services analyze email text, CV/RP content, supervisor pages and interview context through configured model endpoints.

Relevant files: [storage.py](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/storage.py), [email_sync.py](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/email_sync.py), [ai_services.py](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/ai_services.py), [Dockerfile](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/Dockerfile), [docker-compose.yml](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/docker-compose.yml).

## 3. Useful implementation ideas

- A unified professor/outreach/email/interview workflow reduces fragmented applicant records.
- Local data directory and Docker volume provide a simple self-hosting path.
- IMAP uses SSL and the sync worker preserves previously computed classification metadata.
- CV/RP-specific analysis and interview preparation can be linked to the applicant's actual research materials.
- The README documents a Lite mode that avoids email credentials and AI calls.

## 4. Security and privacy blockers

The Docker image binds Streamlit to `0.0.0.0` and Compose publishes port 8501. No application-level login or per-user authorization was observed in the inspected entry path. Do not expose this deployment to an untrusted network without an authenticated reverse proxy and explicit network restrictions.

Configuration persistence stores email credentials and AI API keys in the local JSON configuration without an application-level encryption layer. Resume/RP files and cached email bodies are also stored locally. This may be acceptable for a tightly controlled single-user workstation, but the current design does not provide a multi-user security boundary or encrypted-at-rest guarantee.

The homepage verification functions fetch user-supplied URLs through server-side `urllib` requests. The inspected code does not show a robust allowlist/private-address/redirect policy. If the app is network-exposed, this creates an SSRF surface and needs DNS/IP validation on every redirect.

The email classifier's system prompt tells the model to assume messages are legitimate rather than assess malicious intent. Email bodies are untrusted input; prompt injection, spoofed instructions and misleading sender metadata need to be treated as hostile content. Email, CV and RP text is sent to the configured external model endpoint; this must be an explicit user-consent and data-governance decision.

## 5. Correctness and product gaps

The inspected email client implements IMAP retrieval; SMTP configuration is collected but an end-to-end outbound email workflow was not demonstrated in the inspected client. The background sync reads up to 100 messages and classifies only a bounded number of new items per pass, which is sensible for cost control but needs visible backlog state. Cache writes and background-thread lifecycle require concurrency and recovery tests.

## 6. Testing and operational maturity

The repository has Docker health checks and closed issue history, but no passing automated test suite was established in this pass. No live IMAP connection, AI provider, backup/restore, SSRF or prompt-injection test was executed. Four closed issues are evidence of maintenance activity, not proof that all deployment risks are resolved.

## 7. Adoption judgment

**ADAPT THE WORKFLOW; DO NOT DEPLOY AS-IS ON A PUBLIC NETWORK.** The integrated local applicant workflow is valuable. PhD Atlas should separate private email/document data from public opportunity evidence, use encrypted secret storage, provide per-user authorization, sandbox URL fetching, label email content as untrusted and require confirmation before any external communication.

## 8. Unresolved work

Run a threat model; inspect every user-controlled URL fetch and redirect; implement authentication and authorization; encrypt credentials and sensitive files; add prompt-injection fixtures; verify model-provider retention/region policies; test sync concurrency, mailbox limits, backup restore and data deletion; pin dependencies and add CI tests.
## Additional pinned implementation source audit — 2026-11-12

At [45a1c666b7d9712a96f1b712c276e2c47d3595f2](https://github.com/D2Simon/PhDHub/commit/45a1c666b7d9712a96f1b712c276e2c47d3595f2), the 5,296-line `app.py` was inspected for the import and access-control surfaces, with original `phdhub/storage.py` (83 lines), `phdhub/email_sync.py` (114), `phdhub/email_client.py` (121), `phdhub/ai_services.py` (1,289), `phdhub/resume_store.py` (92), `phdhub/rp_store.py` (88), `constants.py`, Dockerfile and docker-compose.yml. The root app uses Streamlit and page-level session state but shows **no authentication boundary** protecting the professor records, uploaded CV/RP PDFs or mail settings. `Dockerfile` runs Streamlit at `--server.address=0.0.0.0` and Compose maps host port `8501:8501` by default. A private localhost-only deployment and a public network deployment have radically different confidentiality risks; no externally reachable live instance was inspected.

**Private-data storage:** `constants.py` defines plain JSON config with email/provider credential fields, file paths and PDF directories. `storage._write_json()`, `email_sync.fetch_once()`, and the resume/proposal index writers directly overwrite JSON paths with `open(...,'w')` and `json.dump`, without temp-file/fsync/atomic replacement or locks. IMAP SSL fetches up to 100 latest emails, merges prior AI classifications by ID, and writes cached messages; individual outreach statuses do not prove actual email receipt, PI hiring or scholarship offer. Such mutable JSON with concurrent background sync can lose updates or be corrupted on interrupted write; failure scenario is source-inferred, not runtime reproduced.

**Network boundary:** `ai_services.verify_professor_homepage(url, prof_email,...)` directly calls `urllib.request.urlopen` on the supplied URL; `verify_homepage_reality(url,prof_name)` checks only `http://` or `https://`, fetches up to 600,000 bytes with `urlopen`, then marks `ok` if the page includes name tokens. Neither function enforces trusted academic hosts, public-IP/DNS checks, safe redirects or institution identity. These are SSRF/identity-spoofing risks if untrusted values are processed on a service reachable by other users. The LLM-based verifier sends extracted page text and associated professor email to an external provider. An HTML page mentioning a name does **not** prove that a researcher is an appointed supervisor currently recruiting or funding PhD students.

**Adoption:** a useful single-user PhD CRM concept—researcher directory, email categorization, manual follow-up notes, research statement storage and interview preparation—but **BLOCK** multiuser/public deployment until identity/authorization, secret custody, encrypted applicant files, safe outbound HTTP, atomic storage/migrations, audit events and consent to external CV/PI-email processing are demonstrated. No controlled sandbox run, authentication penetration test, provider call, live university check or applicant action was performed. Upstream GitHub shows zero *open* issues/PRs at inspection; historical closed PRs/issues are not proof of deployment safety.

Pinned evidence: [app](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/app.py), [JSON custody](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/storage.py), [IMAP/cache](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/email_sync.py), [URL access and model](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/phdhub/ai_services.py), [container deployment](https://github.com/D2Simon/PhDHub/blob/45a1c666b7d9712a96f1b712c276e2c47d3595f2/docker-compose.yml).
