# bodzioney/phd-applications — deep static repository review

**Review date:** 2026-11-12  
**Pinned upstream revision:** [054ba05fb75949b8748bc2a583e3da4ffcf3f906](https://github.com/bodzioney/phd-applications/commit/054ba05fb75949b8748bc2a583e3da4ffcf3f906)  
**Review state:** DEEP_REVIEW_DOCUMENTED — data/schema/workflow static review; no live faculty verification.  
**Category:** international programming-languages theory supervisor directory.  
**Verdict:** adapt after adding evidence and freshness controls.  
**Primary risk:** current student-taking status has no claim-level source or verification timestamp.

## 1. Purpose and scope

A community-maintained directory of professors working in programming language theory, organized by university and country, intended to help prospective PhD applicants identify potential supervisors. It is a specialist faculty-discovery resource, not a vacancy or funding database.

The current YAML snapshot contains 21 country sections, 120 universities and 367 professor entries. Of the 367 entries, 24 explicitly say `taking_students: true`, 4 say `false`, and 339 omit the field (unknown). There are 110 profile images. The configured directory cycle is 2026–2027.

The latest main commit is 19 April 2026. An upstream PR to add a University of Canterbury professor has remained open since 2 July 2026. No issue backlog, release or license file was established.

## 2. Data model and semantics

The source of truth is `_data/directory.yml`. University records can include name, URL, deadline and deadline URL; professor records can include name, homepage, Google Scholar, ORCID, DBLP, research areas, `taking_students` and an optional profile image.

The tri-state treatment of `taking_students` is a positive design choice: true, false or omitted/unknown. The observed distribution is heavily weighted toward unknown (339/367). This is more honest than treating a missing statement as a negative or positive hiring signal.

However, the schema does not define a source URL, checked date, evidence excerpt, validity interval or reviewer for each `taking_students` value. University deadlines are free-text strings and may be month/day values without a year or explicit admissions cycle.

## 3. Source lineage and discovery method

The configured credits cite PLGradSchools, CSRankings and SPLI as upstream discovery inputs. The individual records provide faculty homepages and optional Scholar/ORCID/DBLP links. Those links are useful identity and research-discovery anchors, but they do not establish current hiring, funded positions, admission availability or international eligibility.

The repository does not record which upstream source supplied each faculty record or which page supports the current student-taking flag. The directory therefore behaves as a curated index, not an auditable evidence registry.

## 4. Generation and deployment workflow

The YAML file generates both the README and GitHub Pages directory. `scripts/generate_readme.py` loads `_config.yml` and YAML, applies Jinja filters and writes README.md. A GitHub Actions workflow regenerates and commits README when source YAML/config/template changes on main.

The generator performs no explicit schema validation, URL validation, duplicate detection, deadline parsing or evidence checks. Its `domain` filter assumes an absolute URL containing `//`; malformed optional URLs can fail generation. The workflow has write permission and commits generated content, but no separate test/validation job is defined.

## 5. Freshness and verification limits

A directory cycle label does not make each professor's availability current. The `taking_students` field has no checked date or source quote; the 24 true entries must not be treated as current verified openings. Similarly, a department deadline string is not proof that a target program's current cycle is open.

The open PR demonstrates community contributions, but the main branch's last commit is from April 2026 and the PR has remained open for over four months. This is evidence of contribution workflow, not evidence that all records are current.

## 6. Privacy, licensing and image provenance

No repository license file was found. The directory includes many professor profile images. Publicly reachable images and profile pages do not automatically grant permission to redistribute images in a commercial application. Do not copy the image corpus without confirming image rights and licensing.

Faculty professional information is generally public, but the Atlas should still preserve source URLs and avoid presenting an unverified interest flag as a confirmed hiring statement.

## 7. Findings and limitations

**Strengths**
- Focused research-area directory with 367 faculty entries across 120 institutions and 21 countries.
- Tri-state student-taking semantics.
- Useful identity links to homepages, Scholar, ORCID and DBLP.
- Simple, transparent YAML source of truth and generated presentation layer.
- Community PR workflow.

**Gaps**
- No claim-level source/evidence/freshness for availability.
- No funding, stipend, tuition, project, position or applicant-class model.
- No source validation, schema tests, duplicate checks or automated link checks.
- No confirmed license for code/data or profile images.
- Highly specialized to programming language theory; it is not a universal CS directory.

## 8. Transfer decision for PhD Atlas

Use the directory as a discovery seed for faculty and research-area taxonomy. Do not import `taking_students: true` as a verified opening. Atlas should model faculty identity separately from hiring signals, with each hiring claim carrying:
- exact faculty/university/program scope;
- official source URL and content snapshot;
- evidence excerpt;
- checked date and validity interval;
- cycle and applicant class;
- reviewer and verification state.

Keep `Unknown` as the default for missing availability. Add schema validation, URL checks, duplicate detection, link freshness checks and license review before using any dataset at scale.

**Overall decision:** valuable specialist supervisor-discovery reference; not an opportunity or funding authority.

## Pinned implementation evidence

- [Directory data](https://github.com/bodzioney/phd-applications/blob/054ba05fb75949b8748bc2a583e3da4ffcf3f906/_data/directory.yml)
- [Contribution schema](https://github.com/bodzioney/phd-applications/blob/054ba05fb75949b8748bc2a583e3da4ffcf3f906/CONTRIBUTING.md)
- [README generator](https://github.com/bodzioney/phd-applications/blob/054ba05fb75949b8748bc2a583e3da4ffcf3f906/scripts/generate_readme.py)
- [README template](https://github.com/bodzioney/phd-applications/blob/054ba05fb75949b8748bc2a583e3da4ffcf3f906/scripts/readme.md.j2)
- [Generation workflow](https://github.com/bodzioney/phd-applications/blob/054ba05fb75949b8748bc2a583e3da4ffcf3f906/.github/workflows/generate-readme.yml)
- [Open upstream contribution](https://github.com/bodzioney/phd-applications/pull/6)

**Validation boundary:** all YAML rows were counted from the pinned source, and generator/workflow files were inspected. Individual professor URLs, hiring claims, program deadlines and image rights were not live-verified.
