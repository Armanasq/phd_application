# Canonical source and relationship crosswalk — 2026-11-11
This is an **evidence dependency graph**, not an admissions-rate or trustworthiness ranking.

Source ledger [data/sources.jsonl](../data/sources.jsonl) groups **21 distinct canonical URLs** supporting **26 recorded claims**. The ledger is generated deterministically from [data/claim_register.jsonl](../data/claim_register.jsonl). All items remain `independent_recheck: NOT_PERFORMED` until a separate researcher actually verifies the claim against the *relevant section*, not merely opens its URL.

Cross-repository relationships [data/repository_relations.csv](../data/repository_relations.csv) include:
- **Explicit derivative:** PhD-Hunter credits PhD-Seeker and Joeyism LinkedIn scraper (source in PhD-Hunter README). Sharing source code/approaches means they are **not independent validation**.
- **Shared origin:** ScholarshipScout and PhD-Seeker both consume ScholarshipDB and FindAPhD, so their vacancy counts may be the same job twice.
- **Original faculty advice recycled:** JedYang/PaulLiang and Shaily/PoloClub source collections overlap; the original CMU/Stanford essay has one underlying author, no matter how many Awesome Lists cite it.
- **No direct relationship asserted:** independent applicant narratives on Reddit are single cases; similar descriptions cannot be assumed corroboration.

## Causal/independence cautions
A website URL supplied by two repositories is one evidence source, not two admissions cases. A survey of successful SoPs without applicant denominator has survivorship bias. A place marked `Fully funded` in an aggregator cannot be treated as a signed award unless original employer proves international tuition/contract and the candidate qualifies.

## Outstanding
Automated reciprocal link extraction, repository rename normalization by GitHub numeric ID, full fork graph, source snapshots and host-permissioned reproducibility test. Do not call these relations an exhaustive citation network.
