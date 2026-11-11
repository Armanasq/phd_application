# Research log
## 2026-11-11 — Phase 1 baseline
Initialized research workspace, country dossiers and first official-source opportunity leads. Time-critical ETH/EPFL/Oxford sources were considered. See executive strategy and opportunity inventory. Application actions remain unperformed.

## 2026-11-11 — GitHub discovery and focused audit pass
- Repeated 12 GitHub repository search query families (English plus Chinese; first page only, max 35 per query).
- Deduplicated search hits and included qualified repositories identified independently. The resulting discovery CSV contains **392** distinct candidate names; **30** were source-reviewed, **362** remain UNTRIAGED. Irrelevant names may remain in the raw candidate set.
- For each of the 30 selected repositories, captured HEAD snapshot SHA, reviewed README and relevant code/docs when possible, and wrote a per-repository file. Review depth explicitly varies; no source is represented as fully audited.
- Compared scraper/monitoring tools, prompt-driven workflows, application data models, statement examples, country/field advice and scholarship directories.
- Identified two published credential-like exposures, placeholder structured extraction, factually incorrect geographic scholarship rows, deprecated recruitment data, and TLS/schema hardening gaps. Did not attempt to authenticate with any third-party credential or execute third-party scrapers.
- Persisted a current reviewed register, discovery backlog, full query log and engineering adoption design.

## Explicit remaining gaps
- GitHub code search, issues/discussions chains for all qualified resources, alternative-language search coverage, pagination beyond first results, full linked-resource audits, and measurable discovery saturation.
- Missing PDF content review for some historical statement/experience resources; incomplete portions of exceptionally large READMEs.
- No execution of remote code, benchmarked scraper recall or verified current vacancy output from third-party tools.
- Eight country dossiers still need project-level vacancy search, supervisor publication matching, individual eligibility and funding confirmation.
- No applications submitted, emails sent, supervisors contacted, offers issued or accepted.

## Next prioritized pass
1. Finish actual deadline-sensitive application requirements and candidate document gates.
2. Deep-audit top two tooling comparators using sandboxed execution and a fixed validation fixture if useful; no running credential-bearing projects.
3. Expand code search and next GitHub result pages; compute marginal yield of newly qualified repositories.
4. Follow one-hop external original sources from curation hubs and deduplicate across them.
5. Extend official Canada/Australia/New Zealand/Ireland/Luxembourg/Norway job searches with evidence and 2027 round dates.
