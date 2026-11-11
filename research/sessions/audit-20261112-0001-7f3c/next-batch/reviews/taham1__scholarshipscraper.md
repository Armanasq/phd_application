# TahaM1/ScholarshipScraper — screened outside PhD admissions scope

**Repository:** https://github.com/TahaM1/ScholarshipScraper  
**Pinned commit:** fea43b4a4a4771ac9dfc5a9a98a1b57a1eeff543  
**Repository ID:** 897473171  
**Checked:** 2026-11-12  
**Disposition:** SCREENED_EXCLUDE — LOCAL_BUSINESS_SCHOLARSHIPS_NOT_DOCTORAL

The README describes a tool for checking whether a small business offers a local scholarship. The React form presents Yellow Pages (Canada) and a disabled US-directory choice, asks for a business category and location, and submits these to Flask /api/scrape. The Python backend uses YellowPages directories to identify business websites, crawls their pages using aiohttp/requests, searches anchors for scholarship or bursary substrings, and returns matching links to the UI. It does not search graduate schools, PhD vacancies, departmental admissions, employer-funded doctoral contracts, research supervisors or scholarship eligibility.

Relevant implementation files inspected: README.md, app.py, asyncRequests.py, main.py, scrape.py, react-frontend/src/App.js, components/Form.js, components/FoundTable.js, About.js and frontend/package.json. The recursive tree includes built React assets; no relevant doctoral data model was found. No upstream code was executed or live scholarship claim verified.

An implementation defect in scrape.py is that the secondary directory branch is not implemented, while XpathForDirectorys contains one selector despite two base URLs. The index can therefore be out of range for directory 1; the UI disables that option. This technical observation does not change the relevance decision.

**Source evidence:** [README](https://github.com/TahaM1/ScholarshipScraper/blob/fea43b4a4a4771ac9dfc5a9a98a1b57a1eeff543/README.md), [directory scraper](https://github.com/TahaM1/ScholarshipScraper/blob/fea43b4a4a4771ac9dfc5a9a98a1b57a1eeff543/scrape.py), [frontend form](https://github.com/TahaM1/ScholarshipScraper/blob/fea43b4a4a4771ac9dfc5a9a98a1b57a1eeff543/react-frontend/src/components/Form.js).
