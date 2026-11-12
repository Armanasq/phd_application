# DataBizex/academic-positions-dashboard — bounded Power BI source inventory

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/DataBizex/academic-positions-dashboard | **Pinned revision:** [`7472058b0c0e704c676eb4be45de207fcc5f1f43`](https://github.com/DataBizex/academic-positions-dashboard/commit/7472058b0c0e704c676eb4be45de207fcc5f1f43) | **Review state:** PRELIMINARY_FOCUSED; binary dataset/model content NOT_INSPECTED | **Disposition:** unresolved, potentially useful analytics pattern; no validated 2026 vacancy metric.

## 1. Repository and advertised claims

A 2026 Power BI dashboard advertised as containing more than 3,000 academic PhD/postdoc vacancies from more than 20 countries. These numbers are **README assertions**, not externally reproduced source counts. The five tracked files are `README.md`, a preview `screenshot.png`, an MIT `LICENSE`, `Academic Positions Dashboard.pbix`, and `Academic Positions Power BI Dataset.xlsx`. Latest observed commit: 2026-10-05.

## 2. What was and was not verified

The complete tree, file identities and README summary were inspected. The source spreadsheet's contents, schemas, row count, origin URL, date range, duplicates, salary/funding fields and license compliance were **not extracted**. The PBIX file's Power Query M, relationships, refresh configuration and DAX measures were likewise **not inspected**; the available GitHub text-file integration cannot establish them. A screenshot cannot validate the model's figures.

A parallel session previously recorded the same [binary access limitation](https://github.com/Armanasq/phd_application/blob/main/research/sessions/gpt6-20261111-2031z/reviews/databizex-academic-positions-dashboard.md); this canonical note preserves the explicit incomplete status rather than promoting it to a deep review.

## 3. Scientific data risks

The advertised 3,000+ postings and 20+ countries are unverified, and the data may mix PhD and postdoc employment, old and open positions, source duplicates, reposted listings, paid tuition programs, employer contracts and scholarship competitions. Before computing any current vacancy counts, establish row grain, collection timestamp, official source URLs, position type, unique identity, country authority, closed status, funding components and missingness. Dashboard charts and coverage claims are not a verified census.

## 4. Follow-up for deep audit

Download/read the pinned XLSX and PBIX binaries in a supported isolated environment; inspect full dataset, source connections, query transformations, DAX and model relationships; verify raw vacancy counts and duplicated sources; stratify source/cycle/open status; independently recheck a sample of official employer pages; and reproduce visual aggregations. Check for embedded credentials or private local paths without redistributing them. Only then assign `DEEP_REVIEW_DOCUMENTED` or establish a source-backed metric.

## 5. Transfer and boundary

The transferable concept is an exploratory operational dashboard for validated opportunity observations, with separate country, domain, deadline and funding facets. No advertised number, job-opening claim or chart metric from this source has been inserted into the PhD corpus as truth.

## Pinned evidence

- [README](https://github.com/DataBizex/academic-positions-dashboard/blob/7472058b0c0e704c676eb4be45de207fcc5f1f43/README.md)
- [Power BI model](https://github.com/DataBizex/academic-positions-dashboard/blob/7472058b0c0e704c676eb4be45de207fcc5f1f43/Academic%20Positions%20Dashboard.pbix)
- [Dataset XLSX](https://github.com/DataBizex/academic-positions-dashboard/blob/7472058b0c0e704c676eb4be45de207fcc5f1f43/Academic%20Positions%20Power%20BI%20Dataset.xlsx)

**PRELIMINARY_FOCUSED**: binary extraction and source verification remain open; no CI, Power BI execution, spreadsheet calculation or independent source validation was performed.
