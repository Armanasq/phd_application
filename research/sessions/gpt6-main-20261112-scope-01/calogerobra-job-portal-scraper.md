# calogerobra/job_portal_scraper_simple_2 — evidence-based scope exclusion

- Checked: 2026-11-12.
- Upstream revision: `119629b141a00ff88cdeaefec26e387103e5b3b1`; tree `c6cc2b7407f4e8d40217786751683cf0ec23ee68`.
- Disposition: SCREENED_EXCLUDE — general labour-market scraper, not a doctoral recruitment, academic funding, or admissions tool.
- Source and README review only; scraper was not executed and bundled historic listing contents were not reproduced.

## Scope

The README explicitly calls the project a requests/BeautifulSoup job-market scraper built for an academic project monitoring employment trends during COVID-19. The script targets the generic Albanian-language `ofertapune.com` recruitment site. Its extracted fields concern employer, contract, job location, wage, work experience, skills, posting date and phone number, not doctoral programme conditions, research group, stipend, tuition, supervisor fit or applicant eligibility.

Tree inspection found one Python scraper, README, a file named requirements.txt containing informal dependency notes, a historical XLSX listing export, and a stored HTML listing sample. There is no package manifest, tests, scheduled CI, research-funding ontology or documented university vacancy provider. No license file appears in the nine-entry tree.

## Implementation inspection

The scraper constructs provider-specific query URLs, fetches list and detail HTML via `requests.get` with a 60-second timeout, extracts HTML table rows, stores individual page snapshots as text, builds pandas records and writes an XLSX export. The script specifies a fixed Windows user path, a generic HTTP base URL and static search parameters.

Source-level defects include:
- `except sqlalchemy.exc.DatabaseError or requests.exceptions.SSLError` catches only the first exception class, not both; Python evaluates `or` before exception matching.
- `pd.concat(frames)` has no empty-result guard.
- Hardcoded local paths, fixed session-like query parameters, brittle selectors and a large fixed page range compromise portability and repeatability.
- The saved HTML snapshot can contain employer/contact material; no retention, consent or privacy boundary is documented.
- The code globally disables urllib3 warning messages although HTTPS verification is configured on the request helper; the configured site URL uses HTTP.
- The output is an employment listing catalogue, not independently verified doctoral vacancies.

There are no upstream issues or pull requests in the inspected results. The last inspected commit dates to 5 August 2021.

## Transferability

Requests/BeautifulSoup extraction and snapshot retention are generic patterns but add no unique PhD-domain evidence. The corpus should not carry this into the doctoral-admissions review count. Retain the negative-screening decision to prevent future retrieval noise. Generic scraping patterns, if needed, should come from maintained, licensed and properly tested sources.

Evidence: [README](https://github.com/calogerobra/job_portal_scraper_simple_2/blob/119629b141a00ff88cdeaefec26e387103e5b3b1/README.md); [full Python scraper](https://github.com/calogerobra/job_portal_scraper_simple_2/blob/119629b141a00ff88cdeaefec26e387103e5b3b1/scraper_ofertapune.py).
