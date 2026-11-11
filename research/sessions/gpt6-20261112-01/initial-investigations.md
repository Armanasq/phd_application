# Session research findings — first investigation batch

Session: gpt6-20261112-01
Branch: research/session-gpt6-20261112-01
Baseline: main@c33758e2373e8726ed4d4ba58aaab736d83c43de
Research date: 2026-11-12

## Scope and integrity

These findings were produced from published upstream repository snapshots. No third-party project was executed. No shared canonical inventory or main-branch file was modified. The two repositories classified SCREENED_INCLUDE in the baseline were prioritized, followed by untriaged candidates. Another session's unpublished claims cannot be observed; these assignments remain subject to coordination reconciliation.

## 1. simitii/CS-Grad-School-Applications-Reading-List

- Snapshot: 189be53b9299ded95d7a6517b6d5760d4286df70
- Repository: https://github.com/simitii/CS-Grad-School-Applications-Reading-List
- Tree: one file, README.md.
- Purpose: a 2019 CS graduate-application reading list compiled from the author's application preparation.
- Topics: general application strategy; admissions; SOP writing; successful essay examples; CS rankings; advisor-visit questions.
- Sources include Tim Dettmers, Carnegie Mellon faculty resources, Matt Might, Nelson Liu's NLP PhD applicant perspectives, Berkeley, Maryland, Stanford and CMU essay examples, and CMU's advisor-visit questions.
- Methodological value: combines general strategy, institutional guidance, applicant experience, concrete writing examples and supervisor-evaluation questions. It is a curation/index layer, not a software workflow.
- Limitations: historical and CS-centric; no structured provenance metadata, country-specific validity dates, eligibility model, funding verification, or workflow implementation. Each linked resource requires independent review. Example essays are not reusable text.
- Disposition: relevant curated resource; deep review of the repository itself is bounded by its one-file structure. Linked-source chain review remains outstanding.

## 2. siddu1998/Graduate-Admissions

- Snapshot: 71d1750175b1cca2bca78fe738765b0c42c58c0a
- Repository: https://github.com/siddu1998/Graduate-Admissions
- Tree: 40 entries; university-specific directories with SOP/statement PDFs for Brown, CMU, Columbia, Cornell, EPFL, Imperial, MIT, Oxford, Purdue, UBC, UCSC, UIUC, Maryland, UNC and USC, plus recommendation-letter PDFs.
- README states the documents span MS and PhD applications and cycles 2020 and 2021, with repetition across statements and adaptation to different universities.
- Methodological value: longitudinal comparison of one applicant's documents across institutions, degrees and application cycles; a source for studying tailoring, research-fit framing and document evolution.
- Privacy boundary: recommendation letters and application documents are personal material. Do not reproduce names, contact details, referee identities, or letter content. Extract generalized structure only.
- Evidence limitation: repository presence does not establish submission, admission, scholarship, or causal effectiveness. Outcomes must not be inferred from document quality or institution labels.
- Disposition: relevant primary applicant-artifact collection; PDF-by-PDF content analysis is not completed in this pass. Recommendation PDFs are excluded from content reproduction.

## 3. aditirajnish/scholarship_web_scraper

- Snapshot: 4786fa11d7871e37f78003babd7de5abe82d2c0f
- Repository: https://github.com/aditirajnish/scholarship_web_scraper
- Files inspected: README.md, main.py, verify.py, requirements.txt, LICENSE; full tree has 10 entries.
- Purpose: scrape Schulich Leaders scholar pages by year and university, extract name/program and write a text file.
- Flow: get yearly listing -> parse profile links -> fetch each profile -> filter by selected university -> extract name/program -> write university/year output.
- Scope is hard-coded to 20 Canadian universities and years 2012–2020, with 2020 University of British Columbia as the entry-point example.
- Defects: requests use verify=False; no timeout, status validation, retry/backoff or request error handling; parser assumes required elements exist; brittle CSS selectors; hard-coded source domain, university list, years and output directory; output is unstructured text; dependencies are old pins from 2020.
- License: MIT.
- Transferable pattern: source-specific, bounded extraction can be a small adapter in a larger ingestion system, but requires provenance, typed records, freshness, schema validation, observability and resilient HTTP behavior.
- Disposition: relevant historical scholarship data scraper, preliminary source-level review; not production-grade or a general PhD-position scraper.

## 4. Akshitha-03/Automating_PhD_Group4

- Snapshot: e4ce240b22c5d67c1dc8c1ef2bdbadcb63415298
- Repository: https://github.com/Akshitha-03/Automating_PhD_Group4
- Files inspected: README.md, index.js, script.js, applicant.html, admin.html; tree has 48 entries including applicant/faculty/admin pages, forms, styles, JavaScript, images and a project PDF.
- Intended product: centralized PhD admissions portal for applicants and institutional staff, with applicant registration, personal/educational data capture, faculty/admin functions and application status display.
- Architecture: static HTML/CSS/JavaScript frontend integrated directly with Firebase Authentication and Realtime Database. Applicant data is pushed under ApplicantPersonal; faculty registration/login uses Faculty records.
- Implementation gaps: Firebase client configuration embedded in source; client-side admin login uses hard-coded credentials; no demonstrated server-side authorization or role enforcement; PII fields include phone, guardian phone, address and Aadhaar number; direct database writes; weak validation; global mutable variables; inconsistent/incorrect phone validation; applicant page warns that submitted applications cannot be edited.
- Data integrity concerns: user data is stored directly from the browser; no demonstrated audit trail, consent model, retention/deletion policy, field-level validation, workflow state machine or secure administrative approval boundary.
- Security: Firebase API key in client config is not by itself a private secret, but database rules and backend authorization are decisive and were not verified. The hard-coded admin credential is a severe design flaw. Do not access or test the live Firebase project.
- Disposition: relevant prototype; significant security/privacy deficiencies; not suitable for reuse without redesign.

## 5. AlanWang610/academic-cv-scraper

- Snapshot: 4862fc7cf220efa7bb802f8f452e05c66d3dd7de
- Repository: https://github.com/AlanWang610/academic-cv-scraper
- Metadata: archived, Python, MIT; 12 files.
- README describes scraping academic CVs to identify bachelor's, master's and PhD institutions and academic affiliations.
- `scrape.py` uses browser-use Agent with ChatOpenAI (gpt-4o-mini) to search for CV PDFs and apply finance/economics relevance checks. The prompt includes fallback searches and requests a URL-only output. It parses the agent history by string delimiters and then validates/downloads a URL.
- Additional modules build author lists, parse CV data, and resolve author names using DOI/publication metadata; JSONL/CSV artifacts are included.
- Methodological value: decomposes discovery, document retrieval, extraction, entity resolution and structured export. Could inform supervisor/lab profiling if repurposed with consent and robust source verification.
- Risks: automated browsing can select the wrong person with a common name; prompt-level verification is not deterministic identity resolution; brittle parsing of serialized agent history; CV scraping involves personal data; no evidence in this pass of robust consent, retention, deletion or correction workflows. Archived state and current compatibility are not tested.
- Disposition: adjacent research-intelligence tool, not an admissions application system; privacy and identity-matching risks require major controls.

## 6. AliAIOps/Putting-in-for-a-PhD-and-moving-abroad

- Snapshot: 6f836112c3acc66e2951714fb85b76ea3eec7319
- Repository: https://github.com/AliAIOps/Putting-in-for-a-PhD-and-moving-abroad
- Confirmed fork of Fatemeh-J/Putting-in-for-a-PhD-and-moving-abroad. Related forks by alirezazolanvari and alistvt were also identified in the candidate inventory; this is one upstream experience source, not three independent accounts.
- Inspected README, Find a PhD Position, After being admitted, Immigration affairs and FAQ.
- Farsi-language firsthand guide describes finding European positions, Netherlands-specific job portals, Groningen post-admission administration, documents, immigration steps, MVV/residence process, embassy appointment and relocation.
- Valuable workflow decomposition: position discovery -> supervisor/offer decision -> university registration -> document collection -> immigration desk/IND -> embassy -> arrival -> housing and local administration.
- Concrete operational artifacts mentioned include CV, master's diploma/transcript, passport, English proof, research proposal, TSP (Train and Supervision Plan), Horaf inita registration, Individual Training Budget and university immigration support.
- Temporal limitation: immigration processing times, embassy email, fees, forms, portal routes and COVID-era procedures are historical firsthand observations, not current policy. Must be rechecked against current University of Groningen and Dutch government sources.
- Disposition: relevant firsthand experience with country/institution-specific scope. Forks must be deduplicated and unique contributions compared before counting additional evidence.

## 7. AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo

- Snapshot: 6dd9ad9f9a696f985b0c83877941712d3ad937f4
- Repository: https://github.com/AHS-CS2/ahs-cs3-classroom-cs_sop_demo-CS_SOP_demo
- Tree contains an empty README, Maven project, Calculator.java and CalculatorTest.java.
- Java class is an educational calculator exercise with an unimplemented add method; no PhD statement-of-purpose content or admissions workflow.
- Disposition: false positive caused by the token SOP; exclude with reason unrelated classroom software.

## Cross-repository synthesis

1. Evidence curation and applicant artifacts are distinct evidence types. A curated link list helps discovery; first-person statements provide contextual examples; neither alone establishes outcome effectiveness.
2. Application artifacts should be modeled as versioned, institution-specific, cycle-specific documents, with provenance and privacy boundaries. A single canonical SOP template is insufficient.
3. Scrapers should be implemented as source adapters feeding normalized, provenance-aware records. Source selectors, extraction confidence, timestamps, HTTP failure handling and independent revalidation are required.
4. Supervisor and academic profile enrichment must not rely on name matching alone. CV/person identity resolution is a high-risk entity-linkage problem requiring authoritative identifiers and human review.
5. The applicant journey continues beyond admission. Offer acceptance, university registration, immigration, relocation and onboarding are separate stages with different authoritative owners and evidence requirements.
6. Forks of the same firsthand guide are dependent copies, not independent corroboration.
7. Security and privacy are core system properties: applicant identity data, recommendation letters, credentials and immigration documents must not enter public Git.

## Limitations and next steps

- No third-party code was executed.
- The 17-page/recommendation and SOP PDF contents in Graduate-Admissions were not exhaustively read; personal data limits apply.
- The Akshitha project PDF and remaining HTML/JS pages need further source inspection; no live Firebase access was attempted.
- AlanWang code review was bounded by fetched file outputs; test/runtime behavior not established.
- The Farsi guide requires comparison against the canonical upstream repository and current official Dutch sources.
- The two initially screened-in repositories are now inspected at repository level, but the PDF corpus and linked external sources remain incomplete.
- Reconcile these session results with the canonical inventory only after checking for parallel-session claims. Do not change main or shared indexes from this branch.