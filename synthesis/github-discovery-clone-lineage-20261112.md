# GitHub discovery false-positive lineage — 2026-11-12

**Scope:** 20 source-inspected repository identities and their linked commit/tree metadata, not a census of all forks. **Classification:** screening exclusions, not scientific research audits or claims of comprehensive source discovery. All inspected repositories remain in the 404-identity discovery register.

## Exact commit reuse: MIT 6.S191 deep learning course

Ten separately named candidate repositories point to the **identical Git commit `2c4966842d8efceeab2916b49d57e8177f6fb2c3`**, originally authored January 16, 2022, with identical tracked README and course directory. A static Git SHA match is stronger evidence of content identity than matching repo names or descriptions. The README and course subtree are instructional MIT deep-learning content; they are not PhD vacancies, applicant evidence, financial-award offers or application workflows. The eleventh fork-like copy shares that instructional core but adds a Spark transformations notebook and points to `43edc824e00d9b40c09a9f540bf365f06fbacd7f`. Screening both groups out does **not** imply the course or its authors are scientifically low quality; they are unrelated to PhD admissions intelligence.

| Repository | Pinned HEAD | Relationship |
|---|---|---|
| [BillyGareth/6S191_MIT_DeepLearning](https://github.com/BillyGareth/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [h000072/6S191_MIT_DeepLearning](https://github.com/h000072/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [knockshore/6S191_MIT_DeepLearning](https://github.com/knockshore/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [NegarMirgati/6S191_MIT_DeepLearning](https://github.com/NegarMirgati/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [Prernamishra08/6S191_MIT_DeepLearning](https://github.com/Prernamishra08/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [Ruib2021/6S191_MIT_DeepLearning](https://github.com/Ruib2021/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [sainathss97/6S191_MIT_DeepLearning](https://github.com/sainathss97/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [tzsh1007/6S191_MIT_DeepLearning](https://github.com/tzsh1007/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [Upsjyq/6S191_MIT_DeepLearning](https://github.com/Upsjyq/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |
| [yazabat/6S191_MIT_DeepLearning](https://github.com/yazabat/6S191_MIT_DeepLearning/tree/43edc824e00d9b40c09a9f540bf365f06fbacd7f) | `43edc824e00d` | COURSE_MIRROR_WITH_EXTRA_NOTEBOOK |
| [yi212212/6S191_MIT_DeepLearning](https://github.com/yi212212/6S191_MIT_DeepLearning/tree/2c4966842d8efceeab2916b49d57e8177f6fb2c3) | `2c4966842d8e` | EXACT_COURSE_TREE_MIRROR |

## GitHub Classroom C# assignments: surname/term collision

Nine independent C# lab projects under the VLazorykOOP classroom organization contain `Lab*.sln`, `Program.cs`, geometry/UI/class exercises and, in several repos, only an assignment deadline-button README. The contributor surname **Soproniuk** contains the string 'Sop', an apparent false match for SOP (Statement of Purpose); the content is unrelated to graduate admissions. Each tree and selected source file was inspected; no third-party binaries were executed. The projects are independently versioned, unlike the ten exact-copy 6S191 forks.

| Repository | Commit | Primary verified subject |
|---|---|---|
| [VLazorykOOP/csharplab1-SoproniukAnna](https://github.com/VLazorykOOP/csharplab1-SoproniukAnna/tree/c62a5843e849803d32f2ccfbc9d38c7acf00377c) | `c62a5843e849` | Lab 1: Lab1Charp, Console project |
| [VLazorykOOP/csharplab2-SoproniukAnna](https://github.com/VLazorykOOP/csharplab2-SoproniukAnna/tree/d430400309d0b45fdacb20f8866ff9aa47cf611b) | `d430400309d0` | Lab 2: array operations, console calculations |
| [VLazorykOOP/csharplab3-SoproniukAnna](https://github.com/VLazorykOOP/csharplab3-SoproniukAnna/tree/2f205b3861e0083d970d32c3ec320f17e2503041) | `2f205b3861e0` | Lab 3: Employee, Engineer, Trapeze and Worker model exercises |
| [VLazorykOOP/csharplab4-SoproniukAnna](https://github.com/VLazorykOOP/csharplab4-SoproniukAnna/tree/07c7430c929876717b6d6f4e5e9265efbcccb681) | `07c7430c9298` | Lab 4: operator overloads, trapeze and vector calculations |
| [VLazorykOOP/csharplab6-SoproniukAnna](https://github.com/VLazorykOOP/csharplab6-SoproniukAnna/tree/0a1da3379aecd1782706dc54da133387af3c1c05) | `0a1da3379aec` | Lab 6: interfaces, products, class hierarchy exercises |
| [VLazorykOOP/csharplab7-SoproniukAnna](https://github.com/VLazorykOOP/csharplab7-SoproniukAnna/tree/580a69ffeaae1f5c8ac555b7c4d96d15d9e46f15) | `580a69ffeaae` | Lab 7: WinForms UI and random shape drawing |
| [VLazorykOOP/csharplab8-SoproniukAnna](https://github.com/VLazorykOOP/csharplab8-SoproniukAnna/tree/85fc0959aeb320a76ff79b18143f3f8d7a9b9838) | `85fc0959aeb3` | Lab 8: C# task files and WinForms project |
| [VLazorykOOP/csharplab9-SoproniukAnna](https://github.com/VLazorykOOP/csharplab9-SoproniukAnna/tree/0ba02bad634b2421b3bb633a09222d1d06ae595f) | `0ba02bad634b` | Lab 9: MusicDisc/Song classes and assignment solutions |
| [VLazorykOOP/csharplab10-SoproniukAnna](https://github.com/VLazorykOOP/csharplab10-SoproniukAnna/tree/033534aad9d45c818b5a67bb20b33d8b41b05456) | `033534aad9d4` | Lab 10: student/trapeze class and console assignment |

## Lessons for discovery and quality gates

- Preserve **raw repository identity** and exclusion evidence; never silently remove a discovered repo to inflate coverage.
- Deduplicate **code lineage** by Git blob/tree SHA and source provenance, separately from institutional opportunities and application IDs. Exact derivative copies are not independent corroboration.
- Use contextual review of source paths, README and code, not substring-only filtering of `SOP`, `PhD`, `scholarship` or a person who happens to be a doctoral researcher.
- Do not treat exclusions as full eight-part source investigations. Re-screen an excluded identity only on a substantive source change (new commit, evidence or scope), not a title match.
- Canonical states after this set: 99 review records (24 deep static and 75 preliminary); 46 evidence-coded exclusions; 259 untriaged; 0 screened included. These counts are historical at this commit.
