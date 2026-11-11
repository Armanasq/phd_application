# ravishchawla/GraduateRecommendationSystem — deep static repository review

**Reviewed:** 2026-11-12. **Pinned upstream:** [8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d](https://github.com/ravishchawla/GraduateRecommendationSystem/commit/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d).  
**State:** DEEP_REVIEW_DOCUMENTED — main training, inference, data collection and Flask API code inspected; no source/data execution.  
**Verdict:** reject any probabilistic admission advice; retain historical preprocessing and selection-bias lessons.

## 1. Goal and project provenance

A 2018-era graduate school ranking recommender for international applicants to US universities. It scrapes 1point3acres discussion forums containing self-reported GRE, TOEFL, GPA, university and offer/rejection outcomes, trains per-(major,university) SVM classifiers, then ranks schools by a mixture of predicted “chance”, QS-style score and living cost. It is not a current PhD-only admissions database and does not verify individual outcomes.

## 2. Architecture and dataflow

`scraper/scraper.py` recursively requests forum pages and individual threads using ten Python threads; cleaning scripts extract/normalize columns into TSV. `site/training/classification.py` trains a separate `sklearn.svm.SVC(probability=True)` per major/university, pickles a model dictionary, and the Flask API `/api/classify` passes user-supplied scores/weights to `api/create_list.py`, which loads the pickled file and creates a university shortlist.

The features are GRE verbal/quantitative/analytical, GPA, TOEFL, top-15/top-30 institution indicators and a sum of GRE Q/V. Data sources and dataset versions are not preserved per predictions, and no admission cohort/cycle is supplied to the API.

## 3. Label construction and sample-size defect

The training code maps `acceptance` through `str(x).lower() in {'ad','offer'}` first. This converts **all non-admit labels** (including missing, pending or unrecognized) to False, rather than isolating real rejection outcomes. Subsequent maps that look for original `'rej'` strings cannot recover those distinctions.

The guard `if dt.size > 18 & np.unique(dt['acceptance']).size >1` uses **bitwise `&` without parentheses**, so it does not mean “more than 18 records and two classes.” It also uses `dt.size`, the DataFrame **element count**, not the number of applications. This can permit sparse, unreliable per-university models. The shuffled DataFrame expression `dt.iloc[np.random.permutation(len(dt))]` is not assigned, so does not actually reorder the training records.

## 4. Probability and scientific validity

The model is trained on self-selected public forum reports, whose missing/incorrect records, cohort selection, reporting bias and cross-school applicant duplication can be severe. The probability output from an SVC does not establish calibration against a current target applicant population. No per-school held-out evaluation, reliability diagram, Brier/log loss, class prevalence, confidence intervals, leakage control, nationality/program/cycle stratification, or future-cohort test was found.

The inference treats “no trained model for school/major” as a **zero admission chance**, converting missing evidence into a false rejection claim. It then combines probabilities and costs via user weights with a fixed `acceptance_preference=0.5` rather than an estimated utility model.

## 5. Inference implementation problems

`create_list.py` passes a **one-dimensional list** to `predict_proba` for an eight-feature classifier; current scikit-learn expects a 2D array shaped (1,8). The source uses obsolete Pandas `convert_objects` and `DataFrame.sort` methods, and old scikit-learn `cross_validation` paths. Runtime compatibility with a present Python environment is not established.

The code computes maximum values by grouping all rows per university, which can combine cost, rank, source link and related metadata originating from **different** records and artificially create a composite university row. The final ranked shortlist therefore needs independent source reconciliation.

## 6. Privacy and security

The scraper extracts forum usernames and academic test/GPA facts. Public posts do not necessarily permit persistent profiling or reuse for predictive screening; retention/consent and platform terms require review. `pickle.load` on a local `trained_models` file executes Python deserialization and is only safe for authenticated trusted model files. The Flask route enables permissive CORS and `debug=True` in the local entry point; it has no authentication or input range/type validation and should not be exposed as a public production recommender.

## 7. Evidence and test boundary

The tree includes saved TSV data and pickled model artifact, which were **not executed** or independently validated against original forum posts. Static inspection covered README, Flask API, inference, training, scraper and an exploratory logistic-regression test script. The latter is not a validated system-wide benchmark, and the current live admissions outcome/policy/cycle data are not present. No third-party code, model deserialization, forum crawl or accuracy evaluation was run.

Pinned evidence: [README](https://github.com/ravishchawla/GraduateRecommendationSystem/blob/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d/README.md), [training](https://github.com/ravishchawla/GraduateRecommendationSystem/blob/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d/site/training/classification.py), [inference](https://github.com/ravishchawla/GraduateRecommendationSystem/blob/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d/api/create_list.py), [Flask API](https://github.com/ravishchawla/GraduateRecommendationSystem/blob/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d/api/app.py), [forum scraper](https://github.com/ravishchawla/GraduateRecommendationSystem/blob/8eb0a9bb48b88ca241c9fda88b63f37ad0b3d54d/scraper/scraper.py).

## 8. Transfer to PhD Atlas

Treat self-reported admissions data as historical observations with unknown selection mechanism, never authoritative acceptance probabilities. A fit framework needs applicant cohort, verified program/country/cycle, consent and outcome evidence, label semantics, missingness flags, group-aware holdouts, calibration metrics and uncertainty. For now output evidence-backed research fit and “Insufficient data” for unknown admission chance rather than a fake percentage or zero.
