# seanxuu/PhD-Seeker — source-pinned preliminary review

**Upstream revision:** `00b09d06f1996d0f5fd4292602f39f04525ab8e3`; **inspected:** 2026-11-12; **review:** PRELIMINARY_FOCUSED; **runtime validation:** NOT_PERFORMED; **source action:** READ_ONLY.

## Purpose and source genealogy

This PhD-Seeker Python CLI advertises gathering allegedly fully funded PhD positions from ScholarshipDB and FindAPhD into CSV/XLSX. The README contains live links to the project at Aghababaei/PhD-Seeker rather than presenting unique source ownership. Git blob comparison against the original upstream found identical README, LICENSE, __init__, __main__, .gitignore, MANIFEST and requirements-independent common files, but modified scraper/main.py, constants, CLI, setup.py and dataframe formatting, plus missing repo.yaml. **It is related but not byte-identical**, so do not count it as an independent scientific evidence source or blindly exclude a possible implementation delta.

## Implementation inspection and risk

phdseeker/main.py uses an asyncio/httpx+http3 fetcher with fixed site-specific selectors. For the ScholarshipDB path it explicitly sends verify=False while also suppressing InsecureRequestWarning. TLS authenticity is therefore not established for that source. The HTML attributes for FindAPhD are fixed, and the scraper zips title, country, date and link vectors: mismatch can misassociate records. Source data are not official funding contracts, nor does the code establish international applicant eligibility. The README itself lists cross-source dedup as unfinished.

## Transfer verdict

PRELIMINARY_FOCUSED. Retain a version-specific source note, but collapse original/fork as dependent evidence for opportunity claims; compare code diffs separately if considering reuse. Require TLS verify, bounded requests, selector fixtures, exact official vacancy URLs, true cross-portal dedup and explicit funding status unknown. No runtime or live job fetch performed.

Pinned [README](https://github.com/seanxuu/PhD-Seeker/blob/00b09d06f1996d0f5fd4292602f39f04525ab8e3/README.md), [main scraper](https://github.com/seanxuu/PhD-Seeker/blob/00b09d06f1996d0f5fd4292602f39f04525ab8e3/phdseeker/main.py), [original project](https://github.com/Aghababaei/PhD-Seeker).
