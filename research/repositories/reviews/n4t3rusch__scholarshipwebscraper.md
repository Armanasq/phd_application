# n4t3rusch/ScholarshipWebScraper — deep static implementation review

**Reviewed:** 12 November 2026  
**Inspected revision:** [`11f274e8172eae313b48cbbb621a802c411b4e38`](https://github.com/n4t3rusch/ScholarshipWebScraper/commit/11f274e8172eae313b48cbbb621a802c411b4e38)  
**Review state:** DEEP_REVIEW_DOCUMENTED — entire source tree inspected; runtime and upstream website NOT_TESTED  
**Disposition:** Reject for operational PhD funding intelligence; retain only the idea of explicit user preference weighting  
**Scope:** One tracked Python source file (approximately 508 lines), repository metadata, commit history, issue/PR listings, dependencies and licensing inventory.

## 1. Problem definition and scope

The repository describes a Selenium/Tkinter scholarship selector that allows a user to specify gender, location, intended study location, level, award type, desired amount, keyword and preferred deadline month. It aims to rank results by selected preferences. This is not an institutional admission system, an independent funding verification platform, or a global doctoral-vacancy feed.

The actual data source is the United States CareerOneStop scholarship search page, loaded through Selenium. The GUI is predominantly US-oriented, although it offers a generic International location option; it does not include source-specific doctoral funding, international tuition, supervisor recruitment or applicant eligibility verification. The one-file tree contains no external data snapshots.

## 2. Architecture and execution flow

The source file creates a Tkinter UI when imported, then the Submit callback creates a `scraper` instance. Its initializer creates a Chrome WebDriver using a **hard-coded developer-specific Windows executable path**, navigates to CareerOneStop, estimates DOM list lengths and stores filter weights. `enterKeyword` populates a search box, `dynamicExecution` clicks filters sorted by the user's preference weights, `parseScholarships` extracts each `tr` row's first five `td` cells into a `scholarship` record, `rateScholarships` assigns a numeric score, merge-sort orders the rows, and `print` displays results in the Tkinter text widget.

There are no service adapters, configuration files, persistent store, typed evidence contracts, source snapshots, tests or runtime packaging instructions. The UI operates synchronously in the Tk event loop. Chrome navigation and DOM waits can block the interface until Selenium operations finish.

## 3. Confirmed scoring and ranking defects

**Desired award amount is not used in the actual score.** In `rateScholarships`, the code initially increments or decrements `final` based on an exact award amount comparison. It then **unconditionally overwrites** `final` with the sum of filter-result counters and deadline-month difference. Thus the amount-comparison branch cannot influence the final score even when it matches. Additionally, the GUI passes the desired amount as the raw string from `amount_entry.get()`, whereas the extracted amount is converted to an integer, so their exact equality condition would be false for ordinary numeric input.

The score aggregates counters after **every selected filter has already been applied to the website**. Sorting `self.ratings` changes filter-click order, not which filters are included or how many matching scholarships are retrieved. Failed UI interactions decrement counters, so score reflects execution errors as much as user relevance.

`calculateDifference` maps each expected and actual deadline through a month-name dictionary, defaulting to December for unknown strings. CareerOneStop table deadlines are not validated as plain month names; full dates, blanks or unsupported strings silently map to December. Raw month-number subtraction also ignores year and cyclic distance. A later deadline can gain a larger score even if it is after the user's application window.

## 4. DOM parsing and failure behavior

The scraper relies on site-specific XPath IDs such as `collapseLevelofStudy`, `collapseAwardType`, `collapseGenderSpecific` and `collapseWhereYouWillStudy`. It uses broad bare `except` handlers that silently subtract weights or skip filter actions. If no list item matches a selected option, the corresponding `input_xpath` or `raw` variable may never be initialized; the subsequent bare `except` hides that cause.

`parseScholarships` loops through **every** page `tr` except the first, assumes at least five `td` children and indexes them without validation. Other page tables, a different number of columns or empty rows can terminate the run. It stores no row URL or canonical scholarship identifier, making source-level verification and deduplication impossible.

The study-location dropdown contains a missing separator between two adjacent state strings, which Python concatenates into one unintended option. This is visible in the source's UI declaration and can affect user input matching.

## 5. Data model, source trust and eligibility gaps

Each result stores only name, level, type, amount, deadline and a heuristic score. There are no institution names, official award URL per record, sponsor identity, cycle, applicant citizenship class, geographic eligibility evidence, tuition component, stipend amount/duration, salary-versus-stipend type, last checked time or independent verification status. A result from a third-party search interface should be classified as an unverified discovery candidate, not a funded PhD opportunity.

Gender and residence are used as webpage filtering inputs; the software does not validate legal eligibility or explain when filtering is restrictive. The preference score is deterministic once controls respond, but it is not empirically calibrated as a ranking of admission prospects or funding fit.

## 6. Deployment, concurrency, security and licensing

The only tracked file is `selenium web scraper.py`. It imports Selenium and Tkinter without a dependency manifest, does not define a CLI or a `__main__` guard, and launches a GUI at import time. The absolute ChromeDriver path is not portable across machines. `close()` calls `driver.close()`, not a guaranteed full WebDriver session teardown via `quit()`. There is no structured logging, retry policy, task timeout budget, pagination limit, source contract or recovery mechanism.

No license file or license metadata was established in the repository snapshot. GitHub issue and pull-request collections returned no entries; the only observed commit is the July 2024 uploaded script. Current Chrome/Selenium compatibility, website terms, selectors and outputs have not been tested. No credentials or live browser actions were used in this research audit.

## 7. Transfer assessment and minimum repair

The user-weighted preference concept could inform **ranking of already verified** opportunities in a separate applicant-facing layer, provided ranking criteria and unknown values remain explicit.

Do not copy this implementation into an operating admissions service. A workable replacement needs a configurable and approved source adapter, explicit browser lifecycle, bounded waits, stable source IDs, per-field provenance, validated date parsing including year/timezone, typed monetary values and award components, privacy-conscious eligibility gates, clear separation between *filtering* and *ranking*, and a tested scoring function. Add fixtures for malformed table rows and unknown month strings, then regression tests that prove changing the desired award amount changes the ranking as intended.

## 8. Evidence boundaries and research synthesis

The single-file implementation can be completely assessed statically, but no empirical Selenium/Tk run, current CareerOneStop scrape, institution funding confirmation, performance benchmark or admissions outcome validation has been performed. Direct source code supports the specific ranking, initialization, error handling and data-model observations; it does not support claims of working current scholarship search coverage.

This example reinforces a cross-repository distinction: a preference UI and an aggregator search result are **not** evidence that a funded doctoral opening exists or is suitable for a particular applicant. Retain current funding and eligibility verification exclusively in source-backed opportunity records, not this weight heuristic.

**Pinned source:** [full implementation](https://github.com/n4t3rusch/ScholarshipWebScraper/blob/11f274e8172eae313b48cbbb621a802c411b4e38/selenium%20web%20scraper.py), inspected at [commit `11f274e8172eae313b48cbbb621a802c411b4e38`](https://github.com/n4t3rusch/ScholarshipWebScraper/commit/11f274e8172eae313b48cbbb621a802c411b4e38).
