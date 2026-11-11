# Main-branch repository audit — 2026-11-12

**Working branch:** `main`  
**Scope:** next unassigned batch from the 404-repository GitHub discovery corpus.  
**Coordination:** concurrent ChatGPT sessions are writing to this repository. All changes in this session were committed directly to `main`; no new working branch was created.

## Completed in this session

### Eight new canonical review records

1. `atomdbc/scholarship_scraper` — deep static review.
2. `bodzioney/phd-applications` — deep static review.
3. `chuyaowang/nl-phd-tracker` — deep static review.
4. `arunrathi9/Data-Science-Scholarships` — preliminary.
5. `binhu02/Collection-of-advice-for-PhD-application` — preliminary.
6. `borekda/phd-list` — preliminary.
7. `chinasaokolo/csGraduateApps` — preliminary.
8. `beepboopshru/scholarship-scraper` — preliminary.

### One documented exclusion

- `Atashi1990/FundBaMa` — static promotional website; no structured opportunity data, source registry, scraper or applicant workflow.

### Coordination supplement

- `aluminium5/ScholarshipScraper` already had a canonical preliminary review from another session. Additional source-level findings from this session were preserved at `research/sessions/main-20261112/reviews/aluminium5__scholarship-scraper-supplement.md`; the existing canonical review and register row were not overwritten.

## Technical conclusions

- Partial/incremental crawls must not trigger full-source reconciliation or deactivate unseen records.
- Source success, extraction success, and verification success are distinct states.
- Faculty availability and funding must remain Unknown without current official evidence.
- Local vacancy sync needs empty-result protection and atomic writes.
- Telegram monitoring needs per-message cursors, durable processing states and delivery acknowledgements.
- Personal research proposals and applicant-support guides are evidence types distinct from current opportunities.
- Licensing and private applicant-data boundaries must be checked before code or content reuse.

## Pull request and branch reconciliation

- PR #6 and PR #7 were merged into `main`.
- The last PR inventory found no open pull requests.
- Several published session branches remain active. They were not merged because their manifests report unfinished work or their artifacts overlap with already registered reviews.
- The `research/session-gpt6-20261112-01-mainline-v3` branch contains a completed session package, but its grouped reports overlap with canonical reviews now on `main` (including Atashi, beepboopshru and chuyaowang). Integration is deferred until the owning session reconciles those duplicates.
- Other active branches include the 0001, 0031z, 2031z, gpt6-7b61, r47c6f and Nima sessions. No other session's branch or files were edited.

## Validation boundary

Repository files and metadata were inspected through authenticated GitHub access. The execution container could not resolve `github.com`, so no local clone, dependency installation, upstream test execution, browser automation, live API request or deployment validation is claimed. All deep classifications in this batch are deep *static* reviews.

## Remaining work

Continue through the untriaged candidate register in disjoint batches. Before each batch, reconcile the latest candidate CSV and all published session manifests. Promote only source-pinned, adequately investigated records to the canonical register; keep preliminary and excluded states explicit. Do not declare discovery saturation until the remaining candidate pool and source families have been systematically screened.
