# Second-batch canonical integration proposal

**Status:** session proposal only; canonical CSVs and generated indexes were not modified.

## Current mainline baseline

As last inspected, main reports:
- 404 candidate identities;
- 67 review records (9 deep static, 58 preliminary);
- 18 documented exclusions;
- 319 untriaged;
- 0 screened-in awaiting first review.

The candidate rows for all four repositories in this batch were UNTRIAGED before this review.

## Proposed dispositions

| Repository | Proposed state | Rationale |
|---|---|---|
| atomdbc/scholarship_scraper | DEEP_REVIEW_DOCUMENTED | Full-stack scholarship scraper; complete static architecture/source review, runtime NOT_TESTED |
| dhcoders/JobsACUK-WebScraper | DEEP_REVIEW_DOCUMENTED | Complete static review of the only Python source file, runtime NOT_TESTED |
| evamaxfield/phd | PRELIMINARY_FOCUSED | Firsthand personal archive; application PDFs intentionally not inspected |
| D4vidHuang/PhD_scanner | SCREENED_EXCLUDE | Repository size zero, no branches/content |

If no other session changes the canonical inventory, the projected totals after these four dispositions are:
- 70 review records: 11 deep static and 59 preliminary;
- 19 exclusions;
- 315 untriaged;
- 0 screened-in awaiting first review.

Check: 70 + 19 + 315 = 404.

Recompute from the live CSVs at integration time. Do not apply these totals blindly.

## Existing documentation drift

The current mainline inventory and README/coverage snapshot are newer than some consolidated research documents:
- METHODOLOGY.md still reports an older 53-review / 340-untriaged baseline.
- synthesis/repository-systematic-review.md still contains older review and screening totals.
- RESEARCH_STATUS.md and synthesis/source-dependency-crosswalk.md report five repository relations while data/repository_relations.csv now contains six.

These are shared documents. No update is proposed here while other sessions are active. Reconcile them with the canonical CSVs in one coordinated change after checking current branches and mainline commits.
