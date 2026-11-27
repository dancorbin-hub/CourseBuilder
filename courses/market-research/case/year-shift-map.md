# Year shift map: case moves to 2027 (2026-11-27)

Dan chose option B on 2026-11-27: move the fictional Larkspan case from 2026 to 2027 before module 2 is final.

## Rules

1. Every case year moves forward 1 year, in one pass (2024 to 2025, 2025 to 2026, 2026 to 2027, 2027 to 2028). The case date is now November 2027. The plan year is 2028.
2. Relative gaps do not change. Report R-2025-07 is still about 26 months old, so the module 5 planted error (older than 18 months) still works.
3. Real dates do not change: statistics, studies, vendor doc dates and check dates stay 2026. They are not in the case files.
4. Ids that hold a year move too: R-2024-07 is now R-2025-07. R-2026-03 is now R-2027-03.
5. Weekdays: a date moves 1 weekday later (2027-11-09 is a Tuesday). One ticket (F-1201) names "Monday night". It now reads as a ticket logged the next day. No change needed.

## Files changed

| Area | Files |
| --- | --- |
| Case | All case files that held a year (26 files). New fingerprints in status.yaml |
| Module 1 | kit-m1-template and kit-m2 (code book, Copilot fallback text, problem backlog). module.md, course-open.md and slides.json did not change |
| Module 2 | lab-2 and kit-m3 files; module.md slide 2.5 ("Q2 2027") |
| Spec | 2 lines that name R-2025-07. New fingerprint |
| Proof kit | README.md and results.md (R-2025-07), plus the project files copy of the case |
| Build | Module 1 workbook re-rendered as v2. Deck and LD specs did not change |
