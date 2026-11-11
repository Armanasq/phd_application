# Eight additional non-admissions source screening decisions

**Inspection date:** 2026-11-12. **Disposition:** eight `SCREENED_EXCLUDE` candidates after checking the live GitHub repository metadata and source tree, README where available, and the pinned revision of nonempty projects. These identities are part of the original 404-candidate search sample; this batch does not add candidates or deep-review records. No third-party code was executed.

## Empty repositories: four checks

For each of the following repositories, the authenticated GitHub repository endpoint returned `size: 0`, and `git/trees/HEAD?recursive=1` returned HTTP **409** with message `Git Repository is empty.` No file-level PhD application guidance, repository data, or commit could be inspected. An empty repository is not a negative judgment about an author's intent; re-screen if new commits appear.

| Repository | Evidence | Classification |
|---|---|---|
| [Hazrat-Ali9/PhD-Application](https://github.com/Hazrat-Ali9/PhD-Application) | Public default `main`, repository size 0; HEAD tree 409 | EMPTY_NO_COMMITS |
| [jlmw19750422-sys/phd-admission-tracker](https://github.com/jlmw19750422-sys/phd-admission-tracker) | Public default `main`, repository size 0; HEAD tree 409 | EMPTY_NO_COMMITS |
| [owenlikecoding/scholarship-scraper](https://github.com/owenlikecoding/scholarship-scraper) | Public default `main`, repository size 0; HEAD tree 409 | EMPTY_NO_COMMITS |
| [Philosohirinism/phd-tracker](https://github.com/Philosohirinism/phd-tracker) | Public default `main`, repository size 0; HEAD tree 409 | EMPTY_NO_COMMITS |

## Content-verified domain mismatches: four checks

### raganmd/touchdesigner-sop-points-to-csv

Pinned revision: [`52d95f9db8dfd303aec63f5d15b736d4cedefa29`](https://github.com/raganmd/touchdesigner-sop-points-to-csv/commit/52d95f9db8dfd303aec63f5d15b736d4cedefa29), 2019-12-09. One-file tree: README states this is a method for exporting **TouchDesigner SOP point clouds** to CSV. The acronym SOP is *surface operator*, not a doctoral statement of purpose. No application essay, scholarship, supervisor, or funded-vacancy content.

### MasonEdgar/DCT-Image-Steganography

Pinned revision: [`20da3e1e4d6b48dbcbe241c776ee156995bb65fe`](https://github.com/MasonEdgar/DCT-Image-Steganography/commit/20da3e1e4d6b48dbcbe241c776ee156995bb65fe), 2024-09-19. Eight-file tree: Python scripts `data_embedding.py`, `extract_stego_image.py`, `image_preparation.py`, `run_stego_algorithm.py`, `zigzag.py`, README and technical PDF research report. It implements DCT image-data hiding, not PhD recruiting, admission guidance or financial support. A generic application keyword referred to a **Python application**, not university applications. PDF internals were not inspected because the README, file roles and scope are unambiguous for corpus screening.

### StudentTraineeCenter/chord-seq-ai-app

Pinned revision: [`92f7d5fd333573c8c405d04d6b150ddc78049412`](https://github.com/StudentTraineeCenter/chord-seq-ai-app/commit/92f7d5fd333573c8c405d04d6b150ddc78049412), 2025-06-15. The archived public repo has 97 tree entries. README identifies the program as a **Next.js web app for music chord suggestions** using ONNX neural models; tracks music-sequence editing, chord recommendations and MIDI export. The author says this was a graduate project and development moved to a new repo. Generic *graduate project* and *AI app* search terms are not PhD admissions relevance. No applicant or vacancy dataset was identified.

### temple-geography/gis-application-development

Pinned revision: [`119b55003dd53b4e2193ff6b143903a95324577f`](https://github.com/temple-geography/gis-application-development/commit/119b55003dd53b4e2193ff6b143903a95324577f), 2026-10-15. Eighty tree entries; README details a **graduate GIS programming course** with Python, Flask, SQLAlchemy, packaging, unit testing and geospatial application workshops. The course trains students in application development; it does not supply graduate admissions applications, doctoral vacancies, PI recruitment, or scholarship criteria. Not reviewed as generic GIS software quality because it is outside the corpus research question.

## Synthesis and reinclusion conditions

The sample search retrieved four genuinely empty repo shells plus four substantive but unrelated projects via acronym ambiguity (`SOP`), generic software use of `application`, and course-level `graduate` references. These are different failure modes from dead hyperlinks or expired funded positions. Corpus screening should require an observed admissions workflow, doctoral vacancy/funding evidence, eligible applicant guidance or firsthand application account—not merely lexical similarity in a name or README.

One GitHub 409 for an **empty Git tree** is not an HTTP failure from an applicant-facing website. A future git commit, project scope change, or discovered relevant evidence justifies re-evaluation. No live recruitment links, user credentials, private files, application actions or runtime tests were involved.
