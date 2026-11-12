# Cross-repository synthesis — session gpt6-20261111-2031z

## Scope and disposition
Seven previously unreviewed or untriaged upstream repositories were assigned. Six received substantive static reviews appropriate to their accessible contents; one (DataBizex Power BI) remains preliminary because its native .pbix model and .xlsx dataset were not extracted. No project was executed locally. No admissions outcome, acceptance rate, or source-derived deadline was assumed from README claims.

| Repository | Research disposition | Principal transferable value | Main gap |
|---|---|---|---|
| simitii/CS-Grad-School-Applications-Reading-List | Deep static resource review | Source taxonomy, committee/applicant perspectives | Old, unstructured, US/CS-oriented, no outcomes |
| siddu1998/Graduate-Admissions | Deep static document-corpus review | Research narrative and program-specific statement adaptation | Personal documents, no outcome labels, no license |
| fsuitoal-code/phd-application-command-center | Deep static implementation review | Local-first application tracker, field confirmation, agent research | Official-domain parsing, source provenance, unverified runtime |
| EydlinIlya/BlueSky-PhD-jobs | Deep static implementation review | Opportunity ingestion, staging, dedup, alerts, SEO | LLM verification semantics, social-source authority, unbounded dedup |
| houwei1228/PhD_Fit | Deep static implementation review | Opportunity monitoring, research-fit scoring, local documents | Hard-gate semantics, score calibration, SSRF and evidence |
| Akshitha-03/Automating_PhD_Group4 | Deep static prototype review | Applicant/faculty/admin workflow stages | Authorization, payment validation, tests, reproducibility |
| DataBizex/academic-positions-dashboard | Blocked preliminary | Potential Power BI opportunity analytics | Native .pbix and .xlsx contents not inspected |

## Shared research model

These repositories are complementary, not interchangeable:

1. **Discovery and intake:** PhD Sky finds social leads; PhD Fit adds search-based leads. Each source should be retained as an unverified opportunity until official evidence is obtained.
2. **Official verification:** Command Center's research agent can extract program facts, but its domain guard and provenance need correction. Store exact official URL, content hash, retrieval time, quote, and field-level verification status.
3. **Candidate/position fit:** PhD Fit provides scoring components and supervisor research. Do not confuse keyword retrieval relevance, research fit, eligibility, funding feasibility, and admission probability.
4. **Execution:** Command Center and Automating_PhD_Group4 provide program/application stages, documents, faculty outreach and tracking. The production implementation should use typed state transitions and real access controls.
5. **Communication:** PhD Sky's subscription digest and outbox patterns can notify users when newly verified opportunities or deadlines change. Social lead updates should not be sent as official deadlines.
6. **Evidence and writing:** The reading list supplies expert and applicant perspectives; Graduate-Admissions supplies document structures. Both are qualitative inputs, not success-rate evidence.
7. **Analytics:** The Power BI dashboard might offer geographic or disciplinary distribution views, but its actual dataset, refresh policy and measures remain unverified.

## Proposed canonical data model
- repository_source(repo_id, canonical_url, upstream_sha, reviewed_at, review_depth, coverage, license, evidence_links)
- opportunity(opportunity_id, canonical_official_url, institution_id, degree_level, discipline, title, cycle, status)
- discovery_event(opportunity_id, source_type, source_url, captured_at, raw_snapshot_sha, classifier_version, confidence)
- evidence(evidence_id, source_url, retrieved_at, content_sha256, quoted_span, source_authority, verification_status)
- fact(fact_id, opportunity_id, field_name, value, evidence_id, valid_from, valid_until, human_verified_at)
- faculty(faculty_id, institution_id, profile_url, research_areas, evidence_id)
- fit_assessment(opportunity_id, applicant_profile_version, eligibility_gates, research_fit_components, scoring_policy_version, explanations)
- application(application_id, opportunity_id, stage, owner, due_at, completed_at, document_snapshot_ids)
- notification(notification_id, user_id, opportunity_id, event_type, delivery_idempotency_key, status, sent_at)
- research_session(session_id, assigned_repo_ids, branch, base_sha, files, progress, conflicts, commits)

## State invariants
- A discovered social or search lead is never automatically OFFICIAL_VERIFIED.
- A user-entered fact is not equivalent to a university-confirmed fact.
- A model quote is not verified until the retrieved source contains the quoted span.
- Hard eligibility constraints are evaluated before aggregate fit ranking.
- Deadline status must be cycle-specific, timezone-aware and linked to official evidence.
- Every claim must preserve provenance and retrieval time; stale facts must be rechecked.
- Notification delivery should use an outbox/idempotency key and preserve a retryable state.
- Application workflow stages are explicit, audited and owned; a UI click is not proof of submission.
- Admissions success rates require outcome-labelled, representative data and uncertainty estimates.

## Cross-repository engineering lessons
- **Bounded agent tools:** Command Center's tool-permission callbacks are a good starting point, but registrable-domain checks must use a Public Suffix List and verify redirects/IPs.
- **Fault tolerance:** PhD Sky's staging and row-level completion are reusable, but publish cleanup should be transactional or scoped to one run. Avoid unbounded full-corpus similarity.
- **Deterministic validation:** PhD Fit's date parsing is useful, but scoring and eligibility gates must be deterministic and testable; do not trust LLM totals.
- **Privacy:** Applicant records and recommendation letters are sensitive; avoid copying third-party personal material into the shared repository. Use access-controlled encrypted storage and purpose-specific retention.
- **Source quality:** Reading lists, anecdotes and sample essays should be labelled as perspective/illustration; official university policies should be labelled authoritative only for the named program and cycle.
- **Evidence-backed analytics:** A Power BI dashboard without inspected source data and measures cannot justify opportunity counts or country comparisons.

## Priority integration proposal
1. Introduce a canonical source/evidence/verification schema without rewriting existing inventory rows.
2. Add candidate-specific eligibility gates, funding constraints, and cycle-specific deadlines.
3. Add separate opportunity ingestion and official-verification queues.
4. Version scoring policies and require deterministic aggregate computation.
5. Add an application state machine with immutable submission snapshots.
6. Add deduplication and alerts with idempotent processing.
7. Introduce testable source/quote verification and stale-evidence checks.
8. Reconcile legacy research counts only after reviewing other sessions' pending changes.

## Coordination and research integrity
- All artifacts live under research/sessions/gpt6-20261111-2031z/.
- No canonical inventory, shared review index, issue, PR or main branch was modified in this research session.
- The session owns only the seven upstream repository identities listed above.
- Six deep static reviews are not equivalent to six runtime-validated repositories.
- The Power BI source is explicitly blocked pending native binary extraction.
- The larger 404-candidate corpus remains incomplete; this session does not claim global completion.

## Source reports
See reviews/ under this session directory. Every report includes pinned upstream revision and source paths.