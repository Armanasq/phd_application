# EdZLau/scholarship-scraper — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [b69e3c6e07290e81744d87d8b316f3c94e307ea0](https://github.com/EdZLau/scholarship-scraper/commit/b69e3c6e07290e81744d87d8b316f3c94e307ea0).  
**Review state:** DEEP_REVIEW_DOCUMENTED; static source inspection, no tests or live applications.  
**Verdict:** adapt eligibility uncertainty/tri-state concepts, reject probabilistic presentation.

## 1. Purpose

A Python scholarship discovery and ranking workflow with curated award seeds, a Bold.org crawler, detail-page enrichment, a profile-sensitive eligibility filter, heuristic ranking, Anthropic-generated essays and summaries, local JSON backup and Google Sheets export. It targets a specific US undergraduate/STEM applicant profile, not globally accessible funded PhD positions. The tree has 23 source files, no dedicated automated test suite and no CI workflow.

## 2. Pipeline and domain model

`main.py` runs `CuratedScraper` and optionally `BoldScraper`, deduplicates by normalized **scholarship name only**, enriches detail pages, filters/ranks records, optionally generates AI text, saves JSON and overwrites a Google Sheet. `Scholarship` stores name, URL, source, amount, parsed amount, a deadline type (`exact`, `annual_month`, `unknown`), user eligibility text, `needs_review`, tags, generated essay and four score fields.

The central model is useful as a simple enrichment boundary, but name-only deduplication can collapse distinct sponsors/cycles or fail to match aliases across sites. Funding duration, international tuition coverage and applicant nationality class are not structured as verifiable independent claims.

## 3. Evidence and source adapters

The curated list hardcodes scholarship amounts, applicant-class conditions, deadlines such as “April (annual),” and essay prompts. The Bold.org scraper uses source-specific detail URL checks, CSS selectors, and keyword-based amount/date inference. Detail enrichment caches raw HTML for seven days and marks absent eligibility as requiring review. These are reasonable defensive touches, but cached HTML has no extracted-source evidence span or version audit.

Historical curated attributes must not be interpreted as current official requirements. The crawler does not independently verify university funding eligibility, official doctoral vacancies or active deadlines.

## 4. Probability and scientific validity

`ranker._win_probability` computes `0.55 * alignment_score + 0.35 * competitiveness_score + 0.10 * amount_bonus`, capped at 95. Alignment uses manually assigned tag weights and keyword substring hits; competitiveness begins at 50 and changes with arbitrary award-size and demographic specificity bonuses and an unvalidated override dictionary. No observed labeled admissions/award outcomes, calibration dataset, confidence interval, error model or probability calibration appears in this source.

Thus the field called **`win_probability` is not a calibrated probability**. The UI and exported spreadsheet display an apparently quantitative “XX%” chance, which risks misleading applicants. Rename as `heuristic_priority_score` with transparent features and no probability semantics until evaluated on held-out award decisions.

## 5. Eligibility and temporal status

The rule engine explicitly distinguishes missing profile facts from proven mismatch by setting `needs_review` when information is unknown. It handles citizen/resident disjunctions, demographic eligibility, degree/class standing, GPA, residency, school and program keywords, and exact vs annual-month deadlines. This is better than deterministic “unknown = eligible” behavior but still relies on fragile natural-language regex, incomplete identity definitions and hardcoded profile assumptions. Regex-driven exclusion can create false negatives when official eligibility language changes.

Deadline comparison uses server-local `date.today()`, without award-specific source timezone or precise cutoff time. It cannot establish whether an annually recurring award has opened in the current cycle.

## 6. Side effects and privacy

The essay engine sends user profile attributes—including education, career goals, GPA, and possibly demographic-sensitive context—to Anthropic. This deserves explicit informed consent, data minimization, storage retention and redaction controls. It generates first-person sample essays that require user authorship review and factual verification before submission.

The Google Sheets writer **clears `Scholarships!A1:Z10000` before writing**. A mid-operation API failure can leave a previously populated sheet empty; source snapshots and human annotations in that tab are overwritten. Use staged sheet updates, versioned snapshots or an append-only change feed. Service-account scopes include full Drive; least-privilege review is warranted.

## 7. Tests and limitations

Inspected main orchestration, base and Bold/curated source adapters, detail enrichment/cache, ranker, profile template, essay generator, sheet writer, data model, dependency manifest and tree. No automated tests, calibration benchmark, live scholarship source response, sheet write or model call was performed. The README describes workflow, not evidence that scholarship opportunities are currently open.

Pinned evidence: [ranker](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/ranker/ranker.py), [orchestrator](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/main.py), [data model](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/data/models.py), [detail enricher](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/scrapers/detail_enricher.py), [essay generator](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/essay_engine/generator.py), [sheet writer](https://github.com/EdZLau/scholarship-scraper/blob/b69e3c6e07290e81744d87d8b316f3c94e307ea0/sheets/writer.py).

## 8. Transfer to PhD Atlas

Adapt source-specific adapters, cached enrichment, explicit `needs_review`, and three-state deadline handling, with official-source evidence and source-cycle metadata. Replace arbitrary “win probability” with a validated prioritization score. Store non-sensitive user matching separately from private demographics and applicant writing. Stage Google Sheets writes to avoid data destruction, require explicit preview before external model calls, and never conflate funding-eligibility judgment with unknown facts.
