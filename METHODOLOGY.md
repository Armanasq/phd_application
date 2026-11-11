# Research protocol — preregistered operational standard
Date: 2026-11-11. Status: **protocol established; execution incomplete**. This is a systematic *mapping* exercise adapted to public repositories, university records and applicant experiences. It is **not** a completed PRISMA-compliant systematic literature review.

## Research questions
- RQ1: Which open GitHub projects provide generalizable, source-supported practices for finding, preparing and managing funded doctoral applications?
- RQ2: Which tools *actually implement* vacancy discovery, eligibility screening, supervisor matching, provenance, tracking and authorization gates?
- RQ3: Which claims are historical, anecdotal, unsupported, geographically constrained or contradicted?
- RQ4: Among eight priority countries, what formal route, current funding conditions and deadline could yield a credible funded offer soonest?
- RQ5: How should first-party evidence and reviewed software designs be integrated without copying unsafe credentials or private applicant artifacts?

## Units and boundaries
The discovery unit is a canonical GitHub repository (owner/repo, same ID across renames when known). The evidence unit is a claim supported by a specific versioned file/line, official announcement, or identified firsthand public account. The admissions opportunity unit is a funded *call or program route*, NOT a search-hit, laboratory profile, or guaranteed offer. The operational unit is an application with action evidence. Code, policies and applicant experience must never be blended as independent replications.

## Source hierarchy and conflicts
For governing requirements, use current official program/vacancy/funding and government immigration sources. For software behavior, inspect source at a pinned commit, configuration, tests and issue tracker. For experiential outcomes, prefer first-person accounts; a single story has no population-level inference. Search snippets, LLM suggestions and aggregators are retrieval leads, not verification. Scope and year outrank generic institutional claims. If primary sources disagree, retain both and mark CONFLICT rather than choose the favorable claim.

## Discovery query matrix
Persist every exact query and page in `data/discovery_query_matrix.csv` / `data/discovery_log.jsonl`. Coverage blocks:
1. Admissions: phd application, grad admissions, doctoral application, supervisor outreach, research proposal, statement of purpose, recommendation letter.
2. Operations: phd application tracker, scholarship monitor, academic vacancy scraper, doctoral positions, university admissions dashboard, advisor matching.
3. Research field: AI/ML, robotics, perception, SLAM, autonomous systems, visual localization, sensor fusion, embodied AI.
4. International and language: Canada, UK, Ireland, Luxembourg, Switzerland, Norway, NZ, Australia; 博士申请/套磁, Doktorand/Doktorandin, doctoral researcher, doctorat, stipendiat, doktora başvurusu.
5. Independent surfaces: GitHub repositories, code search, topics, maintainers, forks, source references and university pages, general search engines, public applicant experience forums.
Search engine and API results can be noisy: count returned records separately from *screened eligible* projects.

## Candidate triage and eligibility
- DISCOVERED_UNSCREENED: only identity/query proven.
- SCREENED_INCLUDE: repository exists, identifiable directly applicable resources (admissions guidance, research preparation, scholarship discovery, doctoral vacancy/PI tools, empirical applicant accounts).
- SCREENED_EXCLUDE: metadata/documentation proves non-admissions subject, advertising-only service or duplicate mirror; record exclusion reason and proof.
- PRELIMINARY_FOCUSED: some relevant documents/code read, but mandatory review fields or substantive checks missing.
- DEEP_REVIEW_DOCUMENTED: specified core files inspected, issue/PR/release and license status evaluated, direct evidence links for important findings, comparisons and limitations recorded; independent execution separately marked NOT_TESTED if absent.
- INDEPENDENTLY_VALIDATED: a different evidence pass actually rechecks governing claims and code behavior as necessary. No current source should be assumed at this gate.
Deep review does **not** mean security-certified or fully code-audited.

## Individual extraction contract
Identity (owner, URL, snapshot SHA, license, recent meaningful commit); geographic/disciplinary/recruitment scope; intended audience and assumptions; actual artifacts/code and data flow; input and output source provenance; maintenance/issue/release evidence; security/privacy/license; bias/conflicts; comparison against alternative; candidate-specific action; direct deep links; uninspected scope; final verdict and quality/confidence. A template may deserve full contents review; a large system deserves risk-focused architecture and code paths plus limits clearly stated.

## Inclusion / exclusion
Include methodological source material when its insights can apply to admissions even if historic, flag current applicability. Exclude or quarantine commercial placement marketing, unrelated software that matches "SOP" (e.g. Houdini SOP), irrelevant degree/thesis artifacts, forks without novel changes and unsafe claims as adoption candidates. No dismissal solely on age, stars, location or language. Retain historical-only sources with explicit status, rather than silently dropping.

## Snowballing / independence
For each curated guide, record its linked *original* sources; resolve common links across lists and preserve cited_by edges. Forks/clones/derivative scrapers do not count as independent support. Trace predecessor and successor implementations and maintainer statements. Produce source crosswalk rather than assume two repos linking one blog count as two observations.

## Quality appraisal
Do not apply spurious numeric scores. Grade each dimension with specific supporting links: (i) relevance, (ii) provenance, (iii) implementation corroboration, (iv) currency/applicable cycle, (v) transferability, (vi) technical and ethical risk, (vii) reproducibility. Unknown is distinct from adverse.

## Search saturation and stop rule
Track new eligible primary projects per independent query-family and successive page (not total raw hits); after at least two novel independent channels and two consecutive expansion rounds yield negligible relevant unique records, characterize *observed diminishing yield*, never global completeness. CURRENT STATUS: 12 earlier first-page broad repo searches, 8 additional focused/multilingual first-page repo searches, 6 code-search families, and selected source chaining; 404 unique *raw* candidates including noise. Because concurrent sessions are adding evidence, compute live review depth and screening counts from `data/repositories.csv`, `data/github_discovery_candidates.csv`, and `data/exclusions.csv`, not from historical text snapshots. PRs #6–#11 and additional independent-agent reports have been integrated selectively; only explicit canonical review rows count, while duplicated branch history and session notes do not establish independent coverage. Saturation is **not established**. See `data/discovery_log.jsonl` for recorded first-page query counts. Use `scripts/discover_repositories.py` for bounded paginated future searches, retaining errors/quotas.

## QA and release
Validate schema, unique repository IDs, exclusions and tracked reviews, required deep review sections, historical/verified flags, source URL/date, conflicts and tests. Review candidate-facing priorities against first-party calls immediately before external action. CI passing structural checks does not prove semantic truth, successful applicant actions or reproducibility of third-party source. No emails/applications without explicit applicant authorization.

## Research ethics
Public GitHub repository: no passports, identifying immigration information, individual grades, referee contacts, private conversation or API credentials. Do not execute foreign network crawlers with credentials, copy publicly leaked secrets, or republish personal application documents. Observe third-party content and license constraints. Published candidate-specific positions remain conditional on verified qualifications and visa eligibility.


## GitHub API retrieval controls
For large repository-screening passes, record exact query, page/cursor, timestamp, response status and result count. GitHub documents a 60-request/hour unauthenticated REST primary limit, 5,000/hour for ordinary authenticated user requests, and stricter limits for search endpoints. Secondary limits also apply. Use authenticated read access where authorized, serialize discovery requests, inspect `x-ratelimit-remaining` and `x-ratelimit-reset`, honor `Retry-After`, and use exponential backoff after secondary-limit responses. Do not treat a rate-limited or truncated query as a completed search. See [REST rate limits](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) and [REST API best practices](https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api).
