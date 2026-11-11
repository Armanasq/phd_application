# Janjs/Web-Scraping-PhD-positions — historic source audit

- Reviewed: 2026-11-12; pinned commit [429a7761f34bfd4b1d69de125cefe39dc1922d01](https://github.com/Janjs/Web-Scraping-PhD-positions/commit/429a7761f34bfd4b1d69de125cefe39dc1922d01).
- State: PRELIMINARY_FOCUSED (entire sole script read; current official site and runtime not checked).
- Category: 2021-era MSCA European doctoral job listing scraper.
- Verdict: reject as-is, historical conceptual reference only.

## 1. Actual source behavior

The repository contains only [webScrapingMarieCuriePhDs.py](https://github.com/Janjs/Web-Scraping-PhD-positions/blob/429a7761f34bfd4b1d69de125cefe39dc1922d01/webScrapingMarieCuriePhDs.py). The script opens an older European Commission Marie Skłodowska-Curie job URL with Selenium and a **machine-specific absolute ChromeDriver path**, sleeps two seconds, parses browser HTML using BeautifulSoup/lxml, locates divs with class starting "jobOp views-row", assumes at least two p.jobField/strong elements, then retains only postings where the first parsed label equals "Computer science" and the next equals "First Stage Researcher (R1)". It stores matching raw HTML nodes, builds an HTML email and sends it through Gmail SMTP over TLS using author-specific sender and recipient addresses. The SMTP password is supplied interactively via input() at runtime, not embedded as a literal credential in the inspected file.

The script's main block **performs live web crawling and sends email**; none of that behavior was executed as part of this review. The code is an alerting prototype, not a normalized, reproducible opportunity dataset or a modern applicant workflow.

## 2. Evidence-quality and reliability concerns

The upstream history contains only two commits dated October 3, 2021, and no README, requirements lockfile, CI, tests, license file, or issue/PR entries at inspection. The historic URL, HTML class names and driver API are not verified as compatible with 2026 upstream systems. The job_types[0] and job_types[1] indexing would fail if the markup has fewer elements; exact case-sensitive string matching can omit relevant postings. A fixed sleep is not proof the required elements loaded. There is no pagination or stable vacancy identity, retry/backoff, duplicate suppression, source hash, checked_at or monitoring cadence; an empty match set still reaches the email path.

The only eligibility filter is field plus R1 role. It does not establish employer offer terms, funded doctoral enrollment, country, international applicant class, salary/stipend, tuition coverage, application deadline or vacancy validity. The EURAXESS/MSCA regulatory environment and live portal changes require primary official-source verification before adopting any downstream records.

## 3. Methodological transfer

The useful pattern is discipline + European researcher-stage classification. A credible EU vacancy adapter must use current authorized official portals, record query/pagination coverage, inspect full current notices, normalize identity/deduplication, preserve exact quoted funding and eligibility statements with a cycle and verification timestamp, and avoid sending email or contacting employers without user authorization. A 2021 prototype cannot verify a November 2026 vacancy or an incoming offer.

## 4. Review boundary

Read the entire single source file and repository tree, inspected Git metadata, commit chronology, issues and PR history. No browser/driver was launched, no source website accessed with Selenium, no SMTP authentication/send was attempted and no modern academic job posting was checked. Full code-file coverage is not a runtime or security validation claim.
