# Global GitHub research — status and navigation

**Dated research baseline:** 11 November 2026. The earlier 30 files in `docs/github/reviews/` are preserved as inspection-history artifacts. They are not the current authoritative review-state index.

For canonical navigation use **[research/repositories/index.md](../../research/repositories/index.md)**, generated from `data/repositories.csv`.

## Defensible corpus numbers

- **404** distinct raw discovery strings (includes irrelevant and misleading matches)
- **35** individually inspected with dated source-revision records
- **8** source-permalink-linked, eight-section deep *static* reviews; **27** preliminary assessments
- **9** evidence-coded exclusions, **7** screened candidates awaiting deeper review, **353** untriaged
- Global search included first-page GitHub repository and code search plus additional Chinese/Turkish/English query families; **no global recall or saturation guarantee**

[Full query/retrieval log](../../data/discovery_log.jsonl) · [Research method](../../METHODOLOGY.md) · [Exclusions](../../data/exclusions.csv) · [Research status](../../RESEARCH_STATUS.md)

## Key source-dependent judgments

1. [PhD-Seeker deep review](../../research/repositories/reviews/aghababaei__phd-seeker.md): configured scraper disables TLS certificate verification and invokes `eval()` on scraped date-derived strings; executable reuse **rejected**.
2. [Evidence-aware PhD Planner deep review](../../research/repositories/reviews/sihengtao__phd-application-planner.md): strong claim-level structure and source/verification semantics; neither a model's label nor a reachable URL establishes factual truth.
3. [Academic Job Digest deep review](../../research/repositories/reviews/baselayerai__academic-job-digest.md): modular adapters, dedup/persistence and PI enrichment; risk of SQL schema interpolation, TLS relaxation and dropping unresolved-PI jobs.
4. [PhD Atom feed deep review](../../research/repositories/reviews/eparrainage__phd.md): current advertised opportunities, but historical/prohibited nationality or Home-fee constraints are **not checked** by the feed.
5. [Professor outreach CRM](../../research/repositories/reviews/khanshaheb34__profreach.md) and [agentic outreach skill](../../research/repositories/reviews/erikpsw__phd-application-pipeline.md): usable process design, but no automatic source truth or permission for sending.
6. [Supervisor Fit Radar](../../research/repositories/reviews/wenzi-researchlab__phd-fit-radar.md): methodological compatibility rubric; qualitative scores must not be converted to calibrated admission odds.
7. [Multilingual BrainPhD handbook](../../research/repositories/reviews/brainphd-cn__handbook.md): historical firsthand examples include one **rejected misrepresentation recommendation** about applicants' US address.

[Data-quality and security findings](failure-register.md) · [Original engineering design recommendations](engineering-lessons.md) · [Independent source relationships](../../synthesis/source-dependency-crosswalk.md)

## Remaining completion work
Screen the 353 untriaged records, deep-inspect included source sets and their original links, expand GitHub pages/topics/forks/PRs and non-English research, collect and audit more firsthand cross-country cases, verify current employer job portals, and demonstrate an evidence-based diminishing-yield discovery criterion. No review or country workstream is declared complete from an index file alone.
