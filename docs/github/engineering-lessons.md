# Engineering transfer plan from repository audits
Date: 2026-11-11. Implement as original components using verified references and compatible licensing.

## Directly adopt as principles
1. Source-first ingestion: site adapter -> raw immutable capture -> canonical URL normalization -> evidence extraction -> human/current official verification -> ranked opportunity.
2. Claim-specific provenance: every deadline, available funding term, international eligibility and PI recruiting statement links to exactly scoped sources. Keep initial retrieval, independent check, and decision state separate.
3. Evidence status: verified / corrected / conflicted / unresolved. URL reachability never equals factual confirmation. Unknown is not auto-false and not verified.
4. Candidate fit: recent research publications, shared methods/datasets, research problem and possible contribution; a general 'robotics' keyword is insufficient.
5. Application lifecycle: only explicit authorized action advances an application to submitted or correspondence to sent.
6. Financial completeness: record international tuition, waiver, 9/12 month stipend, gross salary, contract duration, tax/fees, cost of living and contingent funding separately.

## Do not inherit
- Embedded credentials or unsafe RLS/unauthenticated public read policies.
- Generic scraping without robots/terms assessment, source rate limits and parser drift tests.
- Silently suppressed positions just because a PI could not be resolved.
- Model-generated job data without deterministic source field verification.
- Hardcoded country/timing assumptions or past funding tables as active jobs.
- Reuse of public application material containing private academic/transcript/identity documents.

## Proposed 2027 repository extensions
**P0**: candidate-private local record overlay; time-critical application document templates; official source recheck.
**P1**: normalized repo ingest/audit status, source adapter registry, provenance and freshness checks, author+institution disambiguation, Unicode/multilingual search.
**P1**: controlled program/supervisor matching with recent publication DOIs, evidence-based fit rubric, funding gates.
**P2**: optional local scheduler for source monitoring and draft-only notifications.
**P2**: UI generated from verified SQLite records and testable workflow states.

## Review gate for third-party integration
A library/tool can only move from *reference* to *adopt implementation* after: compatible license, no exposed credentials, documented data protection boundaries, reproducible tests, dependency analysis, current source parser acceptance tests, safe failure modes and external action approvals.
