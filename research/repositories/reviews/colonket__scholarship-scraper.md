# colonket/scholarship-scraper — preliminary source review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [master](https://github.com/colonket/scholarship-scraper/tree/master) (archived repository; commit SHA not independently captured in this session).  
**Classification:** PRELIMINARY_FOCUSED; full single-script static inspection, no live execution.  
**Disposition:** historical educational reference only.

The 2019 Python script `schol-scra.py` reads one user-supplied Scholarships.com directory URL; extracts scholarship title, due date, amount and application link from three aligned CSS selector lists (`td.scholtitle`, `td.scholdd`, `td.scholamt`); and writes `db.csv`. A separate initial GET against the Scholarships.com scholarship-directory index does not feed its discovered URLs into the main worklist. Source tree contains the script, README, pinned bs4/lxml dependencies and Git ignore configuration. The repository is archived.

**Implementation observations:** the script requests pages without a timeout or retry; URL construction concatenates `getDomain(url)` with extracted href instead of robust URL resolution; `zip(t,d,a,t)` silently truncates if selector counts differ, making the later list-length consistency check ineffective; the user URL is accepted as the requested starting page, but no stable normalized opportunity ID, source snapshot, cycle, eligibility, award-period decomposition, checked timestamp or provenance ledger is recorded. It covers historical undergraduate/engineering scholarships, not verified funded international PhD openings.

**PhD Atlas transfer:** no direct code reuse. The four-field CSV is a toy extraction baseline; a serious adapter requires structured source policy, bounded requests, parser fixtures, URL normalization, field-level citations, explicitly unknown funding/eligibility states and deduplicated snapshots. Archive status and page-age make live content validation mandatory before treating any listing as current.

**Evidence:** [archived repository](https://github.com/colonket/scholarship-scraper), [scraper source](https://github.com/colonket/scholarship-scraper/blob/master/schol-scra.py), [requirements](https://github.com/colonket/scholarship-scraper/blob/master/requirements.txt).

**Validation boundary:** static source inspection only; external source pages and tests were not run.
