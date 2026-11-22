# Critic report: Advanced AI for Market Research (Stage 2 draft)

- Checked on 2026-11-22. Outputs only: `spec.yaml` (v0.1), `outline/development-brief.md`, `case/` (all 22 files).
- Checked against: CLAUDE.md, PRD (decisions 39 to 45, quality bar, lab design rules), `research/gate-1-decisions.md`, `worked-example-row.yaml` (v3), `workflows.yaml`, `platform-matrix.yaml`, `shared/registry/`.
- `workflows.yaml` row 01 is not flagged (stale copy, OI-06).
- I recounted all case data by hand: every interview, deal, feedback item and survey row. Most expected results match the records. The exceptions are listed below.

## Checks

| # | Check | Result | Line that fails |
| --- | --- | --- | --- |
| 1 | Workflow and bottleneck per module | Pass | None |
| 2 | Lab extends the one course agent | Pass | None |
| 3 | 2 to 4 objectives, observable verbs, practiced | Pass | None |
| 4 | Timing | Concern | `agenda.full_day` lunch is 45 minutes. PRD: "Agendas plan for 60 minutes" |
| 5 | Autonomy ladder and error fade | Concern | Fade levels are correct (told, hint, hint, hint, none). Success checks and card step 6 name the error before the lab (S2 below). Rung 2 is not a schedule (OI-02, open with Dan) |
| 6 | Development brief | Pass | 5 questions answered. Develop and Apply. Evidence per lab. No invented standards ("Dan to name") |
| 7 | Gate 1 decisions reflected | Concern | PA-01 says the agent "never labels a pattern". The case log has a Status "Pattern" that the agent fills (M4) |
| 8 | Registry | Pass, 1 note | m3 stretch "urgent, pervasive, willing to pay" is taught in PDW-AI (N3) |
| 9 | Case data | Concern | One company (Larkspan), not a copy of BadgeWorks, Entrilo or FieldPro. All 5 planted errors are in the data. Lab 5 status proposals contradict the case bar (M3) |
| 10 | Monday value | Pass | 4 builds on own work plus kit-final and templates |
| 11 | Platform | Concern | Copilot knowledge files are `.md`. The Copilot no-license fallback fails after module 2 (M5, M6) |
| 12 | One core message per lab | Pass | Card steps often hold 2 actions (S5) |

## Extra points from the caller

| Point | Result |
| --- | --- |
| 1. Case PM bar framed as the PM's choice | Mostly pass. `expected-results.md` says "example only" and "A learner may set a different bar". Two problems: the bar is only in instructor files (M2), and one line makes it a rule again (S1) |
| 2. 3 uploads per lab, labs 1 to 3 | Pass on Claude and ChatGPT Go or Plus (10 files per upload, 80 per 3 hours, cg-01, cg-03). Real count is 4 per lab plus the check sample, because each lab also adds a job card. Copilot: `.md` is not an embedded file type (mb-02). Copilot and Gemini chat upload limits are not in the matrix (S3) |
| 3. Planted errors fade and are in the data | Pass. All 5 errors are in the files named in `planted-errors.md`. Counts before and after the fix match the records |
| 4. CSV comment header | Fail. See M1 |

## Must fix

1. **M1. CSV comment line breaks plain import.** All 4 CSVs start with a `#` line. Excel, Google Sheets and pandas read it as the header row. I tested pandas: `m2-crm-export-q2.csv` loads as 1 column and `m3-feedback-week-1.csv` loads as 2 columns (the comment has a comma), with no error. Agents with code execution can then count deals or accounts wrong, and that hides the planted errors. Fix: remove the line. Put the notice in a `data_note` column or a companion `.md` file. The CSV blocks in the check-sample `.md` files already have no comment line.
2. **M2. Learners on the case path cannot see the case bar.** The bar is only in `expected-results.md` (instructor only). The lab 1 to 4 results depend on it: pattern, emerging, 3 interviewed deals, 3 accounts. `company.md` says the Head of Product "sets the evidence bar" but does not state it. Fix: put the bar in a learner file (`company.md` or `m1-code-book.md`). Label it "the Larkspan Head of Product's bar for this study".
3. **M3. Lab 5 status proposals contradict the case bar.** `expected-results.md` proposes P01 and P02 as "Enough evidence to validate (all three segments)". By segment, P01 in Food service has 1 AI-moderated interview (I-105). P02 has Food service 2 and Pharmacy and lab 1 (I-108). The Q4 check question says that Food service alert evidence is "below the bar". The two results conflict. Fix: give the proposals by segment, for example "P01: Distribution and Pharmacy and lab; Food service below the bar".
4. **M4. "Pattern" label vs Gate 1 PA-01.** The PA-01 decision text says the agent "never labels a pattern". `expected-results.md` and `m4-evidence-pack.md` Part 4 show the agent writing Status "Pattern". Fix: the agent writes "meets the PM's bar", and the PM confirms the pattern. Or get Dan to confirm that the v3 wording lets the agent apply the PM's bar.
5. **M5. Copilot knowledge files are `.md`.** mb-02 lists `.doc`, `.docx`, `.pdf`, `.ppt`, `.pptx`, `.txt`, `.xls`, `.xlsx`. It does not list `.md` or `.csv`. All the knowledge files are `.md`. Fix: ship `.txt` or `.docx` copies for Copilot, or verify `.md` with a dated vendor doc at Gate 2 (P1).
6. **M6. Copilot no-license fallback fails after module 2.** The fallback puts the code book in the instructions (8,000 characters, mb-01). The five knowledge files together are about 11,400 characters (code book 2,380, driver code book 2,207, tag list 1,818, map 2,192, past reports 2,773). That is before the core brief and the job cards. The spec defines the fallback only for lab 1, and Gate 2 tests only P1. Fix: define the fallback for each module, for example by pasting the job card and the code book in chat for each run. Add it to P2 and P3.
7. **M7. Agenda lunch is 45 minutes.** The PRD says agendas plan for 60 minutes, and 45 minutes is the buffer for when class runs long. Teaching time is 375 minutes against the 360 assumed. Fix: cut 15 minutes (for example, m1 from 80 to 70 and m5 from 70 to 65), or get Dan's yes on a 45-minute lunch.

## Should fix

1. **S1. One line makes a rule again.** `expected-results.md`: "One rule holds for any bar: nothing from 1 interview is called a pattern." This is a fixed floor, so it goes against "no magic number". Fix: "In this case, a single interview is labeled single source." Use Dan's test (can you predict that the next buyer of this persona will raise it?) in the m1 debrief.
2. **S2. Success checks give the error away.** PRD rule 7 puts success criteria on the slide before the lab. Lab 5 (no hint) has the success check "the flag report lists the old evidence, and the answer does not say 'buyers want'". This names the error. The lab 3 and lab 4 checks and card step 6 also name it ("Check that the new problem shows up"). Fix: write general pass conditions before the lab. Show the error-specific condition in the debrief only.
3. **S3. File count and log update.** `company.md` says "1 knowledge file and 1 or 2 run files" per lab. The spec adds a job card and logs, so each lab has 4 or more uploads. Copilot and Gemini chat upload limits are not in the matrix. Gemini needs the whole skill uploaded again to update a file (gm-01). No step card has a step to save the updated log back to the agent. Fix: make `company.md` match the spec. Add chat upload rows to the matrix. Say how the log persists on each platform (P2 test).
4. **S4. Spec `fallback_case` is out of date.** It still says `status: placeholder` and `company: TBD`. Fix: name Larkspan Systems and point to `case/`.
5. **S5. Card steps with 2 actions.** m1 steps 1, 5, 6; m2 steps 4, 5, 6; m3 steps 4, 5, 6; m4 steps 4, 5, 6; m5 step 6 each hold 2 actions ("Audit ... Fix the brief"). Fix this before Gate 3, or tell Dan the spec cards are outlines.
6. **S6. Ambiguous m3 check item.** F-1307 ("compressor alarms routed to the contractor ... Today the night lead calls them") fits the P06 definition ("who responds to an alarm at night"). Pass condition 1 says it is not P06. Fix: remove the night reference from F-1307.
7. **S7. Deviation from the approved v3 row needs Dan's yes.** v3 puts "count interviews, not quotes" in the template quality checks. The spec leaves it out so that learners add it after the audit. This is good design, but no OI records it. Add an OI.
8. **S8. m1 stretch edge reasons.** AP-07 meets criterion 3 (11 walk-ins), so "2 sites" is not the edge. The edge is "influences". AP-08 is 7 months since its last interview, so it passes criterion 5. Its real gap is 2 warehouses with no cold-room count. Correct the reasons.

## Notes

1. **N1.** m4 is 55 minutes. The PRD says about 60 to 90 minutes per module. It is acceptable, but tell Dan.
2. **N2.** Lab 2 has 14 decided deals but only 9 interviewed. The m2 check sample has 10 deals and 6 interviewed. Say in the debrief that the PA-04 minimum of 10 counts decided deals.
3. **N3.** m3 stretch tests urgent, pervasive and willing to pay. PDW-AI teaches these tests. Refer to them as known, with no new slide.
4. **N4.** The internal PM (Fleet Data Platform) is in `company.md`, but no lab uses it. Internal PM appears only as a feedback channel and the Support lead question. This is a priority context. Consider one FDP item.
5. **N5.** I-201 quote 2 ("Our insurer now asks for every temperature record") can code as P02. The P07 result still holds, but the agent can split the quotes.
6. **N6.** Lab 5 Q2: feedback items F-1108 and F-1214 (state board monthly report) support the report-pack answer. They are not in the lab 5 inputs. This is acceptable, but the instructor may get the question.
7. **N7.** Larkspan sells through refrigeration contractors. FieldPro is HVAC field service. The domains are near, but Larkspan is not a close copy. No action.
