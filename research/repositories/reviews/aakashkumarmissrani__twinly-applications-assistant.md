# AakashKumarMissrani/Twinly-Applications-Assistant — document-only architecture review

- **Review date:** 2026-11-11
- **Pinned upstream commit:** [405f9c5cd2f68f662caed976afead9f1980892db](https://github.com/AakashKumarMissrani/Twinly-Applications-Assistant-/commit/405f9c5cd2f68f662caed976afead9f1980892db); latest commit observed 2026-07-18.
- **Category:** planned local-first PhD application companion.
- **Review state:** PRELIMINARY_FOCUSED. Reviewed PRD, architecture, design, phases, memory and rules documents. No runnable application code was present in the inspected tree.
- **License:** no explicit license metadata or license file confirmed.

## 1. Problem and intended user

The project specifies a personal PhD application workspace combining application tracking, supervisor matching, outreach drafting, document status, deadlines and future discovery agents. The PRD is explicitly personalized to its author and research profile; it is not yet a multi-user product specification.

## 2. Proposed architecture

The architecture document proposes a browser dashboard, Python automation layer, SQLite database, local Ollama inference, Crawl4AI, Browser-Use, scholarly, SMTP and optional Firecrawl. The proposed domain tables include applications, research profile/interests, professor research, email templates, activity log, deadline alerts, supervisor contacts and application documents. The roadmap divides implementation into database/models, dashboard, email, alert agents, discovery/matching agents and polish.

## 3. Useful design ideas

- Keep a local SQLite system of record and portable JSON export.
- Separate research profile, professor evidence, application records and contacts.
- Treat email drafting and sending as different operations; the planned UX includes preview/copy and sent-state tracking.
- Put newly discovered opportunities into a user-review queue rather than silently creating applications.
- Keep deadlines, follow-ups, documents and outreach connected to a single application lifecycle.

## 4. Specification gaps and contradictions

The PRD requires a fully free, local-first, no-cloud system, while the architecture lists external services and remote integrations such as Firecrawl, Scholar search and Gmail SMTP. These may be optional or free-tier services, but they are not offline dependencies and require explicit data-flow and cost boundaries.

The requirements describe a weighted Twinly Score but do not define calibrated feature semantics, source evidence, confidence, negative evidence, missing-data behavior or validation fixtures. The architecture names tables and modules but does not provide executable schema migrations, transaction rules, idempotency, source provenance or failure-state semantics. The roadmap still contains unchecked deliverables and testing tasks.

## 5. Security and privacy assessment

The documents acknowledge local storage and credential handling only at a high level. No threat model, secret-storage design, encryption-at-rest plan, backup encryption, retention/deletion policy, browser automation permission boundary, email consent model or prompt-injection handling specification was demonstrated. A personal applicant profile is present in the planning material; it should not be copied into a generic template.

## 6. Verification status

This is a document-only repository at the pinned snapshot. No backend, dashboard, database schema, agent, tests or release artifact was available to execute. The roadmap's checkboxes are plans, not proof of implementation.

## 7. Adoption judgment

**REFERENCE ONLY.** The domain decomposition and review-queue principle are useful. Do not treat this as an implemented product or transplant code. For PhD Atlas, add explicit source/evidence entities, applicant-specific eligibility, funding terms and application state transitions before implementing autonomous agents.

## 8. Unresolved work

Inspect any later branches or linked implementation repositories; reconcile local-only requirements with external services; define the schema and migrations; add threat modelling, secrets and consent boundaries; define scoring calibration; build executable acceptance tests.