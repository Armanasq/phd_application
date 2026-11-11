# saiPraveenMeda/phdAdmissions2019 — pinned source investigation

- Revision: `e33181b3c670b58650c88a4981187ca16d3c7939`
- Inspected on: 2026-11-12
- State: **PRELIMINARY_PRIVACY_BOUNDED**
- Tests/builds/deployments/third-party integration: NOT_EXECUTED
- Canonical registration: RECORDED (source-level, not independently validated)

## 1. Purpose

Legacy Django 1.11 / Python 2.7 institutional admissions form with payment, registration, recruitment and scrutiny routes.

## 2. Architecture

Git tree includes a committed virtual environment plus logs and uploaded-record-related directories; those records/logs were NOT read.

## 3. Data flow

facultyForm/settings.py commits a Django SECRET_KEY and configures DEBUG=True, ALLOWED_HOSTS=['*']; no secret literal is copied into this review.

## 4. Critical correctness

recruit/models.py defines private applicant, educational, research, disability/category and payment documents; recruit/views.py enforces application stages but file extensions are not content scanning.

## 5. Identity and state

Project is neither a live PhD job feed nor a safe deployable template. Priorities: secret rotation, modern supported runtime, strict hosts, private storage and authorization review; runtime NOT executed.

## Pinned upstream source paths

- [facultyForm/settings.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/facultyForm/settings.py)
- [recruit/models.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/models.py)
- [recruit/views.py](https://github.com/saiPraveenMeda/phdAdmissions2019/blob/e33181b3c670b58650c88a4981187ca16d3c7939/recruit/views.py)
