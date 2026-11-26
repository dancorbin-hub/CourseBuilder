**Fictional data for training.** Larkspan Systems, its people, customers, suppliers and all numbers are invented. Any match with a real company or person is chance. No real personal data and no health data.

# Year shift map (Gate 2, Q6 and cadence decisions)

Use this file to update the spec, the briefs and the cards. Apply every row in one pass. Do not run the rows one after another: old and new ids overlap (old DL-2026-06 is not the same record as new DL-2026-06).

## Rules

1. Every case year moves forward one year. The case date is now late November 2027. The plan year is 2028.
2. Relative gaps are the same. Every day count in `expected-results.md` is unchanged (245 days, 33 days).
3. Real-world dates (research statistics, vendor doc dates) are not in the case files and did not change.
4. Replace the pattern `20YY` with `20YY+1` inside case dates, quarters ("Q1 2027" to "Q1 2028"), halves ("2027 H1" to "2028 H1") and ids.

## Supplier rename

| Old | New |
| --- | --- |
| Corvane Tooling | Ostrelane Tooling |
| Corvane (short form in the Lab 3 debrief) | Ostrelane |

The name Ostrelane is invented. A quick web search from the build tool was not available. Dan or the planner should run a name check like the one in Gate 2 before the name is final.

## Ids that held a year

| Old id | New id |
| --- | --- |
| DL-2025-06 | DL-2026-06 |
| DL-2025-11 | DL-2026-11 |
| DL-2025-12 | DL-2026-12 |
| DL-2026-02 | DL-2027-02 |
| DL-2026-04 | DL-2027-04 |
| DL-2026-05 | DL-2027-05 |
| DL-2026-06 | DL-2027-06 |
| DL-2026-07 | DL-2027-07 |
| DL-2026-08 | DL-2027-08 |
| DL-2026-09 | DL-2027-09 |
| DL-2026-10 | DL-2027-10 |
| DL-2026-11 | DL-2027-11 |
| Q-2026-0417 | Q-2027-0417 |
| R-2027.1 | R-2028.1 |
| R-2027.2 | R-2028.2 |

Other ids (REQ-xxx, PB-xx, RM-xx, RP-xx, INT, FB, WL, A-nnnn, P-0x, KR) did not change.

## Key dates

| Old | New |
| --- | --- |
| Case date, late November 2026 | Late November 2027 |
| Planning year 2027 | Planning year 2028 |
| Hard tooling commit, 2026-12-15 | 2027-12-15 |
| Quote date 2026-09-30, valid until 2026-12-31 | 2027-09-30, valid until 2027-12-31 |
| Release R-2027.1 date 2027-02-15 | R-2028.1 date 2028-02-15 |
| Release R-2027.2 date 2027-05-17 | R-2028.2 date 2028-05-17 |
| Q3 run (plan quarter Q4 2026) | Plan quarter Q4 2027 |
| Q4 run (plan quarter Q1 2027) | Plan quarter Q1 2028 |
| Lab 1 check sample, plan quarter Q2 2026 | Q2 2027 |
| `extracted_on` 2026-11-30 (m5-metrics-nov) | 2027-11-30 |
| `extracted_on` 2026-11-03 (m5-metrics-oct) | 2027-11-03 |
| Run 1 date, lab 3, 2026-11-02 | 2027-11-02 |
| Run 2 date, lab 3, 2026-11-23 | 2027-11-23 |
| CR-07 date 2026-11-18, contract signature 2027-01-31 | 2027-11-18, signature 2028-01-31 |
| Limited release since June 2026 | Since June 2027 |

## File names

| Old file | New file |
| --- | --- |
| `m2-requests-week-47.csv` | `m2-requests-batch-1.csv` |
| `m2-requests-week-47.xlsx` | `m2-requests-batch-1.xlsx` |

`m2-check-sample.csv` and `.xlsx` keep their names. Their text is now "request batch 2". Other file names did not change.

## Text renames

| Old text | New text |
| --- | --- |
| week 47 requests, week 47 result, week 47 decisions | request batch 1 |
| week 48 (check sample) | request batch 2 |
| "Which of this week's requests" (company.md) | "Which requests in this batch" |

## Other case changes in the same pass

| File | Change |
| --- | --- |
| `m3-tooling-quote.md` | Plain words: the supplier gives the lower price per set only above a minimum yearly order. The plan buys less. Numbers and error unchanged. "First article" is now "first sample" |
| `planted-errors.md`, `expected-results.md` | Lab 3 text uses the same plain words. Numbers unchanged (unit cost 52.30 to 59.10, year 1 gross profit 1,881,200 to 1,758,800) |
| `problem-backlog.csv`, `.xlsx` | New last column `evidence_order`. It ranks by evidence records, then accounts. Equal evidence shares a rank. It is not a priority |
| `company.md`, `README.md` | One line each on evidence order. README file table uses the new batch file name |

## Not changed (planner to decide)

1. `m3-evidence-q4.md` title still says "Q4 refresh". `expected-results.md` still says "Lab 4: roadmap refresh and change". Check them against the cadence wording (no recurring reorder, PM sets the cadence).
2. Market Research case: `courses/market-research/case/company.md` says "November 2026" and "the 2027 plan". It has no founding year. Larkspan is in 2026 there and in 2027 here. Dan asked for one year in both courses. The Market Research case needs its own shift (not done here).
