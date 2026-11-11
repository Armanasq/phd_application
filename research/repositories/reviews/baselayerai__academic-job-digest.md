# Deep review — BaseLayerAI/academic-job-digest

## 1. Identity and scope
- **Canonical:** https://github.com/BaseLayerAI/academic-job-digest
- **Owner:** BaseLayerAI; GitHub API reports MIT license, non-fork, last source commit 2026-07-23 and post-commit push Aug2026. Snapshot `fec14470cf708784698865cbbfc48ec41d44c3a1`; verified 2026-11-11. No GitHub releases in inspected API.
- **Audience:** job applicants/research assistants interested in US biomedical academic research posts; not PhD scholarships or eight-country coverage per se.
- **Assessment type:** static review README, `src/db.ts`, `src/pi.ts`, repository architecture and PR/release status. No runtime execution.

## 2. Problem and assumptions
Monitor six US career sites for new entry-level research jobs; extract PI/lab, enrich via commercial LLM, rank, persist, and send email digest. Assumes Playwright access to each site, a database, valid Anthropic/Resend accounts, and professional networking consent.

## 3. Actual implemented pipeline
- [README / declared flow](https://github.com/BaseLayerAI/academic-job-digest/blob/fec14470cf708784698865cbbfc48ec41d44c3a1/README.md) names six adapters (Weill Cornell, Columbia, NYU Langone, Mount Sinai, Einstein, Northwestern), a job type/title heuristic, Postgres, PI research, email digest and optional Sheet webhook.
- [Database code](https://github.com/BaseLayerAI/academic-job-digest/blob/fec14470cf708784698865cbbfc48ec41d44c3a1/src/db.ts) creates / evolves jobs table, deduplicates observations and stores PI evidence/recency fields, with retry/backoff for cold DB connection.
- [PI code](https://github.com/BaseLayerAI/academic-job-digest/blob/fec14470cf708784698865cbbfc48ec41d44c3a1/src/pi.ts) contains explicit JSON extraction prompt for posting-named PI, separate web-assisted resolution and confidence output using Anthropic SDK. A named PI inferred by the model may still need source validation.
- Code tree includes site adapters, `src/email.ts`, `src/filter.ts`, `src/parse.ts`, `src/index.ts`, `src/profile.ts` and test-email runner. The README documents scheduled Railway execution and optional Google Sheet export, but those runtime paths have not all been inspected.
- [PR #5](https://github.com/BaseLayerAI/academic-job-digest/pull/5) is open for dependency updates; no other substantive maintainer issue cases were observed in the limited API pull.

## 4. Strengths and methodological risks
Strengths: adapter modularity, stored state/novelty detection instead of repeating search hits, extra content enrichment and reviewable PI confidence. More defensible for monitoring than a one-file, one-off scraper.

**Source-level security:** `src/db.ts` uses `ssl: {rejectUnauthorized:false}` for certain database URL patterns: susceptible to losing TLS peer verification. It also interpolates an environment-supplied `DB_SCHEMA` into SQL: ensure strict identifier allowlisting rather than raw interpolation. This assessment does NOT establish remote exploitability.
**Selection bias:** README says positions where a named PI cannot be resolved are dropped from digest for up to 14 days; this can systematically miss legitimate jobs and bias the opportunity set.
**Model verification:** web-result-assisted PI association and research-specific networking angles must be distinguished from officially named supervisors; unsourced LLM output is not confirmation.
**Side effects/privacy:** Resend digest sends external email, private candidate history loaded locally, third-party LLM receives posting/candidate info. Requires explicit opt-in and data minimization; no automatic emails in current admissions project.
**Transferability:** US biomedical institutions only, research jobs not guaranteed doctoral training/admission, six adapter sites cannot be relabeled as Swiss/Irish/UK employment opportunities.
**Reproducibility:** no dataset or tested precision/recall for PhD calls identified. Latest snapshot is static.

## 5. Application relevance
Architecture is reusable for **new PhD job source adapters**, but user should require at least one confirmed current employer vacancy page, exact full-funding and nationality/tuition facts, deduplicated URL, cross-source disagreement log and manual action approval. Unresolved PI must still remain discoverable rather than vanish.

## 6. Comparators and uniqueness
Compared with [PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker), job-digest persists incremental state and separates adapters; however, it is not a turnkey PhD finder. Compared with [Profreach](https://github.com/KhanShaheb34/profreach), this system is scheduled ingestion plus digest rather than applicant CRM/outreach UI; a future architecture can combine concepts but not licenses/credentials blindly.

## 7. Decision
**ADAPT ARCHITECTURE ONLY**, subject to TLS, identifier, error handling, privacy and source semantics hardening. Do not copy operational settings or assume the model's PI match is correct. Current reproducibility for eight-country PhD admissions: UNDEMONSTRATED.

## 8. Evidence limits
Sources: pinned README, `src/db.ts`, `src/pi.ts`, PR #5 (observed 2026-11-11). Remaining: site adapter and email internals, CI/real test run, deployment reproduction, full licenses of transitive dependencies, sample output validation and fresh source-site consent. This is a bounded risk-based deep review, not full repository security sign-off.
