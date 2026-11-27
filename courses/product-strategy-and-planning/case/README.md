**Fictional data for training.** Larkspan Systems, its people, customers, suppliers and all numbers are invented. Any match with a real company or person is chance. No real personal data and no health data.

# Larkspan Systems case files (Product Strategy and Planning)

This notice covers every file in this folder, including the CSV files. All companies, suppliers, customers, quotes and numbers are invented. No personal names and no health data. Account codes such as A-5120 are invented.

## Why the CSV files have no notice line

A notice line at the top of a CSV file breaks a plain import. Excel, Google Sheets and pandas read the first line as the header row. The CSV files start with the header row. This README carries the notice for them.

The `.xlsx` copies carry the notice in cell A1. Their header row is row 3, and the data starts in row 4. The three formula sheets are different: see below.

## Rules for these files

1. Keep this README with the CSV files when you copy or share them.
2. Every `.md` and `.txt` file starts with the notice line.
3. Each file is under 100 KB. The limit in step cards is 30 MB.
4. Every table has a CSV copy and an `.xlsx` copy (one sheet each). Copilot uses the `.xlsx` copy, because CSV is not allowed as embedded knowledge.
5. Each `.md` knowledge file has a `.txt` copy for Copilot. If you edit a `.md` knowledge file, copy it to the `.txt` file again.
6. Gemini: import the `.xlsx` copy into Google Sheets. The formulas stay.
7. Fictional phone numbers, if any, use the 555-01xx range. This case has none.

## The three formula sheets

| Sheet | Layout | What the agent writes | What the agent reads |
| --- | --- | --- | --- |
| `capacity-sheet.xlsx` | Header row 3. Rows 4 to 14 | Quarter and Alloc_pct for each team and program row | Alloc_FTE and Per_program_check. The sheet checks each program row alone. It has no team total |
| `business-case-sheet.xlsx` | Header row 3. Assumptions rows 4 to 11. Results rows 13 to 19 | Low, Base, High, evidence and owner | Result at Low and High, swing, order by swing, year 1 gross profit, sign change check |
| `outcome-sheet.xlsx` | Range in B3. Header row 5. Measures rows 6 to 9 | Range (the PM), label, Actual Oct, Actual Nov | Gap, Off range, Flag |

The CSV copies of the formula sheets hold the calculated values at the start state.

## Files by lab

K means a knowledge file: it stays in the agent. Run means upload or paste in chat each run. Check means the second sample.

| Lab | File | Use |
| --- | --- | --- |
| All | `company.md`, `strategy-okrs-kpis.md` (+ `.txt`) | K (`strategy-okrs-kpis`). `company.md` is background |
| 1 | `capacity-sheet.xlsx` (+ `.csv`) | K |
| 1 | `m1-submissions-q3.md`, `m1-status-q3.csv` (+ `.xlsx`) | Run 1 |
| 1 | `m1-submissions-q4.md`, `m1-status-q4.csv` (+ `.xlsx`) | Run 2 |
| 1 | `m1-pack-q2.md` | Format example (optional) |
| 1 | `m1-check-sample.md` | Check |
| 2 | `problem-backlog.csv` (+ `.xlsx`), `request-decision-log.csv` (+ `.xlsx`), `roadmap.csv` (+ `.xlsx`) | K |
| 2 | `m2-requests-batch-1.csv` (+ `.xlsx`) | Run |
| 2 | `m2-check-sample.csv` (+ `.xlsx`) | Check |
| 3 | `business-case.md` (+ `.txt`), `business-case-sheet.xlsx` (+ `.csv`) | K |
| 3 | `m3-source-pack.md`, `m3-tooling-quote.md` | Run 1 (sent with the business case) |
| 3 | `m3-evidence-q4.md` | Run 2 |
| 3 | `m3-check-sample.md` | Check |
| 4 | `release-plan.csv` (+ `.xlsx`), `roadmap-decision-log.csv` (+ `.xlsx`) | K |
| 4 | `validated-problem-backlog.csv` (+ `.xlsx`), `evidence-log.csv` (+ `.xlsx`) | Run |
| 4 | `m4-change-request-cr-07.md` | Run |
| 4 | `confidential-terms-list.md` (+ `.txt`) | Paste into the brief |
| 4 | `m4-check-sample.md` | Check |
| 5 | `outcome-sheet.xlsx` (+ `.csv`) | K |
| 5 | `m5-metrics-oct.csv`, `m5-metrics-nov.csv` (+ `.xlsx`) | Run |
| 5 | `m5-check-sample.csv` (+ `.xlsx`) | Check |

## Problem backlog order

`problem-backlog` has the column `evidence_order`. It ranks problems by amount of market evidence (records in 12 months, then accounts). Equal evidence shares a rank. It is not a priority. The PM sets the review cadence, often once a quarter.

## Knowledge file count

The agent ends the course with 16 knowledge files. The limit is 20 on ChatGPT Plus and Copilot.

| Group | Count |
| --- | --- |
| Core instructions | 1 |
| Job cards (portfolio pack, requests, business case, roadmap, outcomes) | 5 |
| Case files: strategy-okrs-kpis, capacity-sheet, problem-backlog, request-decision-log, roadmap, business-case, business-case-sheet, release-plan, roadmap-decision-log, outcome-sheet | 10 |
| Total | 16 |

The source pack, the quote, the evidence log, the validated problem backlog and the confidential terms list are run files or brief text. They do not count.

## Instructor files

`planted-errors.md` and `expected-results.md` are for the instructor only. Do not give them to learners.
