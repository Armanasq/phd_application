# renzoe/positions_internships_phd_postdoc — historical group recruitment archive

**Reviewed:** 2026-11-12 | **Upstream:** https://github.com/renzoe/positions_internships_phd_postdoc | **Pinned default-branch commit:** [`3b2cf283e34d0b47ebdd567f0b07de7b67e93885`](https://github.com/renzoe/positions_internships_phd_postdoc/commit/3b2cf283e34d0b47ebdd567f0b07de7b67e93885) | **State:** PRELIMINARY_FOCUSED (repository and provenance inventory; PDF text not inspected) | **Decision:** historically useful lab-specific posting source, not a verified open position feed.

## 1. Actual repository and timeline

The README identifies the maintainer as an associate professor at IMT Atlantique, Rennes, France, and says the repository publishes proposals for master's internships, doctoral theses, postdoctoral and engineering contracts. The repository contains five tracked files (README plus four PDFs) across 2022, 2023 and 2025:
- `2022/2023_StageMaster_PQuantumKEMIoT-NAVAS.pdf` (173,247 bytes);
- `2023/2023_PhD_Sujet_thesis_IETR_security_IoT.pdf` (158,614 bytes);
- `2025/5GMetaverse-en.pdf` (112,650 bytes);
- `2025/5GMetaverse-fr.pdf` (113,575 bytes);
- `README.md` (436 bytes).

The latest commit is 2025-09-24, documenting an engineering/5G position update. Earlier commits added an IoT-security doctoral offer in 2023 and a master's internship in 2022. The repository has no executable crawler, data model, tests, releases, issues, PRs, CI workflows or LICENSE file.

## 2. Recruitment-source model

This is a faculty-maintained *posting archive*, not a generalized application platform. The research subjects visible from filenames and repository history include IoT security, 5G/metaverse, and master-level IoT security internships. Such faculty-maintained repositories can be useful supplemental discovery sources, especially if a current official laboratory or university page points to them.

The same project may have multilingual English and French PDFs. These should be modeled as alternative-language source documents for one underlying opportunity **only after** comparing offer identity, date, and terms. Their existence does not establish two independent opportunities or two independent confirmations of funding.

The README identifies a research role and university affiliation; no current vacancy status, funding commitment, eligibility, formal application instructions, salary or deadline is established from the README alone.

## 3. External institutional cross-check

The current IMT Atlantique [5G METAVERS project page](https://www.imt-atlantique.fr/fr/recherche-innovation/collaborer/projet/5g-metavers) describes a 2024–2027 research initiative involving 5G/metaverse technologies and an industrial/academic consortium. It supports that the named research topic is part of an institutional research program. It does **not** verify that any particular 2025 PDF is a currently open 2026 recruiting offer, nor confirm a vacancy's salary, application deadline, or availability.

Project duration and recruiting-window duration are separate facts. An active funded research project is not equivalent to an open funded PhD position for a new applicant.

## 4. Incomplete binary-source validation

The GitHub API provided complete file paths, file sizes, blob identifiers and commit history. The binary PDFs were not rendered or text-extracted because the local runtime could not resolve GitHub and direct raw-PDF access was unsuccessful. Their content, language parity, supervisor, exact funding and degree eligibility, posted deadlines and employer submission process are **NOT_VERIFIED**. No confidential data were redistributed.

This is therefore a bounded preliminary investigation, not a deep content audit.

## 5. Application to the PhD research schema

Model the repository as a `LAB_POSTING_CHANNEL` with a dated owner/affiliation claim. Maintain each file's immutable source identity and a separate canonical opportunity key. Capture publication cycle, position type (internship, PhD, engineer or postdoc), source language, official hiring-channel URL where verified, last checked, and current status. Do not infer recruiter availability from the repository's last push date.

Important controls:
1. Preserve original multilingual PDFs and avoid counting translations as separate vacancies.
2. Treat initial institute/project identity as lead-level until a current official job advert or institutional hiring page validates recruitment.
3. Track project dates separately from actual individual offer dates and funding decisions.
4. Keep unknown salary, international eligibility, admission/contract route, and deadlines explicitly unknown.
5. Avoid extrapolating historical 2022/2023/2025 postings to a 2026/27 intake.

## 6. Evidence references

- [README and maintainership statement](https://github.com/renzoe/positions_internships_phd_postdoc/blob/3b2cf283e34d0b47ebdd567f0b07de7b67e93885/README.md)
- [2023 IoT-security PhD archive](https://github.com/renzoe/positions_internships_phd_postdoc/blob/3b2cf283e34d0b47ebdd567f0b07de7b67e93885/2023/2023_PhD_Sujet_thesis_IETR_security_IoT.pdf)
- [2025 English 5G document](https://github.com/renzoe/positions_internships_phd_postdoc/blob/3b2cf283e34d0b47ebdd567f0b07de7b67e93885/2025/5GMetaverse-en.pdf)
- [2025 French 5G document](https://github.com/renzoe/positions_internships_phd_postdoc/blob/3b2cf283e34d0b47ebdd567f0b07de7b67e93885/2025/5GMetaverse-fr.pdf)
- [IMT institutional 5G METAVERS project description](https://www.imt-atlantique.fr/fr/recherche-innovation/collaborer/projet/5g-metavers)

**Disposition: PRELIMINARY_FOCUSED**. Complete repository topology, history, and institutional topic cross-check recorded. PDF-body analysis and current employer-source availability validation remain outstanding.
