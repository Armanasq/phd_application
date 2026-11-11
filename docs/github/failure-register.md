# Repository risk and data-quality findings
**Date:** 2026-11-11. These are **source observations**, not executed exploit attempts, credential validations, or legal conclusions. Exact secret strings are deliberately omitted.

## Critical — credential exposure in upstream code
1. [zxcgzx/phd-application-tracker — Supabase sync](https://github.com/zxcgzx/phd-application-tracker/blob/8826e96755f4d76854e00725226ff92fed59af18/crawler/database/supabase_sync.py) contains a hardcoded service-role token fallback. [Database schema](https://github.com/zxcgzx/phd-application-tracker/blob/8826e96755f4d76854e00725226ff92fed59af18/database/schema.sql) includes broadly permissive read policies. Validity/exploitability were **not** assessed. Do not execute or copy. Remedy for owner: revoke/rotate and restrict secret/configuration, audit RLS. No external disclosure was sent.
2. [you27-mohamed/PhD-Hunter — LinkedIn scraper](https://github.com/you27-mohamed/PhD-Hunter/blob/1054afc3258eb909a2faad42bba17d9c548c36aa/phd_hunter/linkedin_scraper.py) contains hardcoded login data in its script's example entrypoint. Treat as exposed credential-like text and never attempt login. The scraper's claimed legal compliance was not independently verified. No external action was taken.

## High — material data integrity flaws
3. [ScholarshipScout notebook](https://github.com/danielhafezi/ScholarshipScout/blob/1fcd85b17b08f564c3d8a8d13d790f0c79419b07/ScholarshipScout.ipynb): the structured extract_info helper is a placeholder that returns empty data, while README describes fully funded PhD discovery. Therefore not an authoritative funding extractor.
4. [MaryleenAmaizu/ML-AI-Scholarships README](https://github.com/MaryleenAmaizu/ML-AI-Scholarships/blob/1fdcbdea5db48594e087c6b20c3fe7cb36afdd04/README.md): the opening table lists Munich Center for Machine Learning as UK and misassigns a separate Oxford program to Germany/Intl. Multiple historical deadlines appear; current vacancy status must be checked independently.
5. [mcnuttandrew/vis-phd-positions](https://github.com/mcnuttandrew/vis-phd-positions/tree/1f784d7b74091954db90840c7215108d7a3a46e8): last commit indicates deprecation; displayed underlying TSV represents 2024–2025 recruiting. Do not surface as 2026/27 open vacancies.

## Moderate — code and operational concerns
6. [BaseLayerAI/academic-job-digest Postgres](https://github.com/BaseLayerAI/academic-job-digest/blob/fec14470cf708784698865cbbfc48ec41d44c3a1/src/db.ts): TLS configuration sets rejectUnauthorized:false on some database URLs and a configurable DB_SCHEMA is interpolated in SQL. Requires parameter safety and TLS review before reuse.
7. [Aghababaei/PhD-Seeker](https://github.com/Aghababaei/PhD-Seeker/blob/93ad22ea8bc0a04bbf566613650b36a58ff2c063/phdseeker/repo.yaml): relies on target-site HTML selectors and acknowledges missing deduplication. Third-party pages can change without notice.
8. [KaiserWhoLearns/CS-PhD-Application-fee-waivers](https://github.com/KaiserWhoLearns/CS-PhD-Application-fee-waivers/blob/4a7b9401d37356badb038eacb6255e3b914214ea/README.md): contains at least one explicitly old 2021 deadline; never treat directory entries as current waiver eligibility.
9. [rednaxela2018/Application_Materials_For_PhD](https://github.com/rednaxela2018/Application_Materials_For_PhD/tree/f26d8bb0b444f40be415a5e1702c42d9bc5ee000): tree includes transcripts, degree papers and exam-result scans. Do not mirror sensitive material as public research examples.

## Evidence discipline
Risk severity describes the **observed source issue or apparent exposure**, not proven incidents. Adoption policy must distinguish static inspection, executed tests, field tests, security audits, and production suitability. No third-party code copied into this research repository.
