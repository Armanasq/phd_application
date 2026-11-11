# Lukas-Vasionis/PhD_Positions — deep static source investigation

**Original:** https://github.com/Lukas-Vasionis/PhD_Positions
**Pinned master revision:** [4a8e8616f72584901a3be20c62b71adced4da39a](https://github.com/Lukas-Vasionis/PhD_Positions/commit/4a8e8616f72584901a3be20c62b71adced4da39a)
**As inspected:** 2026-11-12. **License:** Apache-2.0. **Last upstream push:** 2025-05-18.
**Review:** DEEP_REVIEW_DOCUMENTED — static only. No live scraping, database inspection, install/build, browser interaction, or tests.
**Verdict:** **adopt the primary-university adapter pattern only after substantial data-integrity repairs**.

## 1. Purpose, architecture and evidence

This is a biomedical-oriented PhD vacancy collector focused primarily on Norway and Switzerland, with additional experimental German and Luxembourg modules. README describes a local workflow: install dependencies, run each university scraper, process raw records into SQLite tables and view/label positions in Streamlit.

Execution path: `scripts/scrape.py` -> `phdfinder.scraping.runner.run_all_scrapers()` -> source-specific HTTP/Selenium adapters -> `save_to_db_as_tbl()` -> raw SQLite tables -> `phdfinder.processing.processor.main()` -> processed tables + global labels table -> Streamlit app (university-specific views, free-form labels, optional Excel export).

Source files read: README, LICENSE metadata, pyproject, three script entrypoints, `config.py`, `scraping/runner.py`, `scraping/scraping_utils.py`, university adapters for ETHZ, NTNU, UZH, TUM, UNIL and UNILU, `processing/processor.py`, `processing/utils.py`, `app/viewer.py`, `app/streamlit_app.py`. The recursive tree has 41 entries. All adapter files were inventoried, but not all were opened. The bundled binary SQLite database and screenshot were deliberately not inspected.

The source registry knows institutions and country codes, but adapter execution is a separate hard-coded list of ten functions. There is no tracked test suite or scheduled workflow in the inspected tree. Upstream pull-request history exists (31 closed PRs); no open upstream issues/PRs at snapshot.

## 2. Source-confirmed correctness defects

**P0 — inconsistent processed-table identity causes loss of historic records.**

- `ScrData.update_scraper_tbl()` looks up and reads `processed_{self.tbl_name}` for a raw table e.g. `raw_ethz`, producing `processed_raw_ethz`.
- `ScrData.save_to_db()` instead writes `processed_{self.tbl_name.replace("raw_","")}`, i.e. `processed_ethz`, with `if_exists="replace"`.
- Consequently, the intended history-preserving merge checks the wrong table and does not recover records from the actual processed table. New partial crawls can replace previously known vacancies instead of merging them.
- Similarly, `create_or_update_tbl_labels()` reads old labels under `processed_raw_ethz` but writes new label identities under `processed_ethz`. Prior user decisions (Interesting, Applied, Rejected) are not recovered as designed on processing. This is not merely a display bug: it undermines application history.

Evidence: [processing/utils.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/utils.py), [processing/processor.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/processor.py).

**P0 — an empty/failing crawl becomes destructive or fabricated data.** `save_to_db_as_tbl()` substitutes a fake empty-title record when passed an empty list, then replaces the raw source table. Some adapters also create their own placeholder records. An unavailable university page or parser regression can therefore become an authoritative-looking empty result and overwrite a previously useful raw snapshot. Distinguish completed zero-result snapshots from failures; never synthesize a vacancy row for emptiness.

Evidence: [scraping/scraping_utils.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/scraping_utils.py), [universities/ethz.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/ethz.py), [universities/ntnu.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/ntnu.py).

**P1 — Excel export calls function with incompatible signature.** `download_filtered_tables(selected_tables, conn)` calls `fetch_data(conn, table, columns)`, but `fetch_data` is defined with only `(_conn, table_name)`. Export on a selected table raises an argument-count error under Python function semantics. No browser execution was performed.

Evidence: [app/viewer.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/app/viewer.py), [app/streamlit_app.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/app/streamlit_app.py).

**P1 — filtering silently fails.** `ScrData.filter_CH_unil_PhD()` evaluates `self.df.loc[...]` but does **not assign** the selected rows back to `self.df`. It therefore does not actually filter by PhD/research position type, despite its name and `processor.py` calling it.

Evidence: [processing/utils.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/utils.py).

**P1 — incomplete adapter pipeline.** The runner executes UIO, NTNU, UIB, Nord, NMBU, Basel, Bern, Lausanne, Zurich and ETHZ. The processing pipeline also assumes `raw_unilu`, `raw_dkfz` and `raw_tum` exist, while those sources are not run by that runner; DKFZ scraper is not present in the inspected source tree. A fresh database without historical tables can fail in `load_tbl_to_pd()` before other processed records are produced.

Evidence: [scraping/runner.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/runner.py), [processing/processor.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/processor.py).

**P1 — Selenium lifecycle leak and executable browser risk.** `get_page_through_selenium(..., return_driver=False)` returns page HTML without `driver.quit()`. NTNU uses this path. Repeating crawls can leave browser processes running. The helper also launches Chrome with `--no-sandbox`, which removes a browser security boundary, and installs ChromeDriver dynamically.

Evidence: [scraping/scraping_utils.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/scraping_utils.py), [universities/ntnu.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/ntnu.py).

**P1 — parser and pagination fragility.** UZH requests a single API page capped at `limit=9999`, drops a fixed set of columns, and assumes JSON shape without explicit HTTP error handling. TUM retry logic assigns `attempts=-1` instead of decrementing to a real retry; it is effectively a single attempt after a failure. `parse_date_columns_scandinavian` returns from inside its loop, so when given multiple columns it processes only the first. The UNIL part-time filter checks whether strings contain `90` or `100` rather than comparing parsed numeric percent.

Evidence: [universities/uzh.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/uzh.py), [universities/tum.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/scraping/universities/tum.py), [processing/utils.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/processing/utils.py).

**P2 — packaging and schema hygiene.** `pyproject.toml` describes Python using a caret `requires-python = "^3.10"` under PEP 621's `[project]`, whose field expects a standard version specifier; install/build compatibility has not been tested. `config.py` uses `LX` for Luxembourg, whereas ISO 3166-1 alpha-2 is `LU`. Academic-job records have no cycle, timezone-specific deadline, funding evidence, closure provenance, source snapshot digest or application receipt.

Evidence: [pyproject.toml](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/pyproject.toml), [config.py](https://github.com/Lukas-Vasionis/PhD_Positions/blob/4a8e8616f72584901a3be20c62b71adced4da39a/src/phdfinder/config.py).

## 3. Data lineage and tradeoffs

This repository captures **primary institutional job pages**, unlike the general board aggregator [NimaaaAI/Position-Aggregator](https://github.com/NimaaaAI/Position-Aggregator) reviewed in the preceding session. Primary-page extraction is potentially stronger evidence, but it still needs preserved exact source URL, fetched timestamp, retrieval completeness, raw HTML hash, claim-level evidence span and explicit deadline-status provenance. The current raw/processed/labels design attempts a useful separation of source records and user state but implements inconsistent keys that break persistence.

The embedded `data/phd_jobs_in_schengen.db` is a historical snapshot, not proof the listed opportunities are open today. No contact information, applicant private records or DB contents were copied into this report.

## 4. Transfer decision and validation plan

Adopt: institution-specific adapters; first-party vacancy URLs; local-first applicant label capture; separate source acquisition, normalization, and interface layers.

Reject until fixed: replace-on-scrape ingestion, fabricated empty records, misaligned processed names, title-type filtering that does not assign, fixed scraper coverage, unclosed Selenium sessions, unverified dates, and exported datasets without working tests.

Minimum tests: raw/processed/labels round trip with two overlapping crawls; transient empty-source failure preserving old records and labels; new database bootstrap when optional adapters do not run; multi-column Scandinavian dates; Lausanne PhD-only filtering; complete export via Streamlit; driver closure in both return modes; 429/404/HTML layout drift; job deadline extension; duplicate URL across universities. Static findings only; runtime reproduction pending.
