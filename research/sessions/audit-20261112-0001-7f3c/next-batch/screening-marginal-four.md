# Four source-verified out-of-scope/unsupported candidates

**Screened:** 2026-11-12. These exclusions are based on pinned repository source and do not constitute claims of fraud or a comprehensive third-party software security assessment.

## kumawatvinit/Scholarship-Management-System

Pinned revision: [493e7e118250447a55fb987753208061eba3921b](https://github.com/kumawatvinit/Scholarship-Management-System/commit/493e7e118250447a55fb987753208061eba3921b). The README expressly describes an attendance, guide approval and scholarship-stipend system for enrolled PG/PhD students. Code/app.py implements student login, attendance, guide approval and stipend views. Code/database/schema.sql defines student, attendance, scholarship and guide entities, but no external doctoral vacancy, research-fit, university selection or new-student admissions workflow. Security concerns in this distinct post-matriculation product include global session identifiers, plaintext password comparisons, and a placeholder Flask secret in source. None of this is suitable as an application engine.

**Disposition:** SCREENED_EXCLUDE — POST_MATRICULATION_SCHOLARSHIP_ATTENDANCE. [README](https://github.com/kumawatvinit/Scholarship-Management-System/blob/493e7e118250447a55fb987753208061eba3921b/README.md); [Flask handlers](https://github.com/kumawatvinit/Scholarship-Management-System/blob/493e7e118250447a55fb987753208061eba3921b/Code/app.py).

## NaichuanLuo/PhDAdmission

Pinned revision: [1d74b499ff076388cceed5e079031bb91a98fea1](https://github.com/NaichuanLuo/PhDAdmission/commit/1d74b499ff076388cceed5e079031bb91a98fea1). The five-file tree comprises a personal Jemdoc page, stylesheet, personal profile image and CV, and a small readme. index.html labels itself a personal homepage; its About Me and Research Interests placeholders do not implement PhD program recruiting or an admissions methodology. A publicly accessible personal CV does not authorize mirroring private content. Binary personal files were not downloaded or inspected.

**Disposition:** SCREENED_EXCLUDE — PERSONAL_HOMEPAGE_NO_ADMISSIONS_WORKFLOW. [Personal page source](https://github.com/NaichuanLuo/PhDAdmission/blob/1d74b499ff076388cceed5e079031bb91a98fea1/index.html).

## royrada/scholarship-scraper

Pinned revision: [0cca50d95aa9f1ec743785984851fba9857a5327](https://github.com/royrada/scholarship-scraper/commit/0cca50d95aa9f1ec743785984851fba9857a5327). The README describes an exploratory scrape of CareerOneStop listings as input to a downstream **donor/endowment opportunity** analysis. The author says a recovered CSV of scholarships was used to identify frequent 501(c)(3) sponsors and their endowment thresholds. scraper.py implements Selenium, scholarship row recovery, checkpoint state, delays and URL-detail extraction. There is no dedicated PhD fellowship filter, international/visa eligibility check or official funded research opening classifier. The advertised 10,000-row historical output has not been independently verified.

**Disposition:** SCREENED_EXCLUDE — DONOR_ENDOWMENT_RESEARCH_NOT_PHD_RECRUITMENT. [README](https://github.com/royrada/scholarship-scraper/blob/0cca50d95aa9f1ec743785984851fba9857a5327/README.md); [script](https://github.com/royrada/scholarship-scraper/blob/0cca50d95aa9f1ec743785984851fba9857a5327/scraper.py). The checkpointed extraction technique is an adjacent reusable pattern but the dataset is not a doctoral admissions source.

## Samaritan735/Samaritan-purse-scholarship-

Pinned revision: [599ec3e90ee2aeeba7568170b6a7cab4139e034b](https://github.com/Samaritan735/Samaritan-purse-scholarship-/commit/599ec3e90ee2aeeba7568170b6a7cab4139e034b). The four-file tree contains static landing/application HTML, a short README and a static-site deployment workflow. index.html advertises generic full scholarships for bachelor/master/PhD applicants; application.html presents a general registration form. No independently verified award sponsor, accrediting institution, official funder terms, selection timeline, signed call, international tuition coverage or verifiable offer is established by the repository itself. Nothing in this review establishes that the advertised funding exists or that the site is fraudulent. Do not submit applicant data based on the repo's claims without independent official verification.

**Disposition:** SCREENED_EXCLUDE — UNVERIFIED_GENERIC_SCHOLARSHIP_FORM_NO_OFFICIAL_EVIDENCE. [Landing page](https://github.com/Samaritan735/Samaritan-purse-scholarship-/blob/599ec3e90ee2aeeba7568170b6a7cab4139e034b/index.html); [application form](https://github.com/Samaritan735/Samaritan-purse-scholarship-/blob/599ec3e90ee2aeeba7568170b6a7cab4139e034b/application.html).

## Verification boundary

No code, third-party applications, network service, forms or applicant personal files were executed or submitted. Classification rests on source content, repository shape and supported applicant-workflow scope. Revisit only if authoritative evidence of funded PhD recruiting becomes available.
