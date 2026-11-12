# wijayantoap/scholarship-scraper — deep static source audit

**Date:** 2026-11-12. **Pinned upstream:** [400d6b14cf21d1abfab311e9aecb53559568c2cd](https://github.com/wijayantoap/scholarship-scraper/commit/400d6b14cf21d1abfab311e9aecb53559568c2cd).  
**State:** DEEP_REVIEW_DOCUMENTED, full custom JS source inspection, NOT runtime-tested. **Verdict:** reject exposed API; reference list/category/detail separation only.

## 1. Goal

A 2021 Node/Express/Puppeteer API extracting scholarship article listings, posts, categories and sitemaps from Scholars4Dev and Indonesian Indbeasiswa. Neither source class establishes an authoritative current PhD award for a specific applicant.

## 2. Execution

server.js exposes eight GET routes and one root route. Dedicated modules launch a separate headless Chromium browser for each listing/post/sitemap/category call; selectors extract title, article text, date and links, sometimes raw innerHTML. Browser requests abort images and stylesheets; the stealth plugin is enabled. The package uses Express 4, Puppeteer 5 and Node 12-era engine metadata, with no real npm test script.

## 3. Unbounded external URLs

Post and category endpoints accept an arbitrary request.query.url passed directly to page.goto, without approved-host restrictions, DNS/private-IP filtering or redirect checks. server.js listens on 0.0.0.0 by default and has no authentication. A reachable deployment could fetch private-network URLs through Chromium. This is a source-level SSRF exposure, not an executed exploit. Chromium is launched with --no-sandbox, reducing isolation for untrusted pages.

## 4. Error and resource hazards

Routes chain promises with .then but no .catch or error middleware. A navigation or CSS timeout can leave requests unresolved or trigger an unhandled rejection. All source modules close the browser only on normal return: errors before browser.close risk orphaned browser processes. There are no server-side per-request budgets, browser-concurrency limits, rate limits or upper pagination bounds.

## 5. Parser correctness and source truth

The scraper assumes fixed CSS children, e.g. heading anchors and exactly two post_column_1 paragraphs; a null/moved selector may crash extraction. The post routes return raw innerHTML; downstream clients must sanitize rather than assign it directly into a DOM. Output strings contain article titles/body/dates, not normalized award IDs, official deadlines, award cycle, nationality, full funding components, applicant eligibility or field-level quoted evidence.

## 6. Persistence, scheduling and licensing

No durable queue, stable identity/upsert, snapshot archive, retry state, deduplication or crawler coverage proof is implemented. The server declares an ISC license in package.json, but code reuse must consider individual dependencies and portal terms. Stealth mode does not establish permission to scrape. Old pinned dependencies and Node engines require fresh compatibility and security review before any deployment.

## 7. Pinned evidence

[server.js](https://github.com/wijayantoap/scholarship-scraper/blob/400d6b14cf21d1abfab311e9aecb53559568c2cd/server.js), [scholars4DevPost.js](https://github.com/wijayantoap/scholarship-scraper/blob/400d6b14cf21d1abfab311e9aecb53559568c2cd/scholars4DevPost.js), [indbeasiswaCategory.js](https://github.com/wijayantoap/scholarship-scraper/blob/400d6b14cf21d1abfab311e9aecb53559568c2cd/indbeasiswaCategory.js), [puppeteerConfig.js](https://github.com/wijayantoap/scholarship-scraper/blob/400d6b14cf21d1abfab311e9aecb53559568c2cd/puppeteerConfig.js), [package.json](https://github.com/wijayantoap/scholarship-scraper/blob/400d6b14cf21d1abfab311e9aecb53559568c2cd/package.json). All custom JavaScript scraper/list/sitemap modules were read. No browser, build, source fetch, site authorization or tests were executed.

## 8. Transfer

Keep separate list/category/post/sitemap source adapters. Require authenticated bounded worker pool, private-host blocking, redirect validation, explicit timeouts, try/finally cleanup and typed HTTP errors. Store immutable source snapshots, checksums and per-claim citations. Separate discovery articles from independently verified funded PhD calls and never use a partial source crawl as evidence to retire previously validated awards.
