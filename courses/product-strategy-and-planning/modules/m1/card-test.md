# Card test: module 1 (lab 1 and the opening build check)

Course: `product-strategy-and-planning`. For Dan (Gate 3). Draft 2026-11-27.

This card test of lab 1 can double as Gate 2 proof pattern P1 (spec `platform_matrix_summary.gate_2_proof_patterns`, open item OI-08; question 3 in `module.md`). Each platform run then records the card test and the P1 checks P1-a to P1-h below.

## How to test

1. Open the real Word or PDF card for the platform. Follow it with no other help (PRD card test).
2. Start with the opening build check card (`course-open.md`, section 3). Then the lab 1 card (`module.md`, section 5).
3. Do not open `case/planted-errors.md` or `case/expected-results.md` during a run.
4. Record minutes per card, and every place you got stuck. A stuck point is any moment you had to guess, search or ask.
5. Record every screen name on the card that differs from the screen.
6. At least one person who did not write the card tests the Copilot card (PRD card test).

Target times: build check 10 minutes. Data check card 2 minutes. Lab 1 core path 33 minutes (half day 38). Check sample 3 minutes. Log save card 1 minute.

## Extra steps for proof P1 (not on the learner card)

| When | Extra step | Records |
| --- | --- | --- |
| After the build check | Close the browser tab. Reopen the agent before lab step 1 | P1-h (same structure after reopen) |
| After lab step 2 | Save the output. Fill the "before the fix" column | P1-a to P1-g, before |
| After lab step 5 | In a new chat, send the Q3 files again with "Run the portfolio pack job". Save the output | P1-a to P1-g, after (Q3) |
| Lab step 6 | Run as on the card (Q4 files, new chat) | Debrief check: Firmware team 150 percent, 3 flags |
| Copilot only | Run the no-license path once with `copilot-fallback-instructions-m1.txt` | G2-PF-05 |

Rule: if P1-d is "no" before the fix on 2 or more platforms, the error is too easy to avoid. Tell the course builder before Gate 3.

## P1 checks (use in every platform table)

| Id | Check | Expected before the fix (brief v1, Q3) | Expected after the fix (brief v2) |
| --- | --- | --- | --- |
| P1-a | A downloadable file, or every table in full in one message | yes | yes |
| P1-b | Pack shows status, capacity and link per program (5 programs) | yes | yes |
| P1-c | Totals come from the sheet formulas (Alloc_FTE, Per_program_check), or each sum is shown in full | yes | yes |
| P1-d | **Planted error**: the Firmware team shows "inside" for P-01 and P-02, and no flag names the Firmware team at 200 percent | yes | no |
| P1-e | Flags: P-03 status differs; P-04 no stated link (Q3). After the fix the Q3 rerun adds the Firmware team at 200 percent | 2 flags | 3 flags (Q3 rerun) |
| P1-f | Strategy consistency section: O1 USD 910 thousand, O2 USD 3,000 thousand, O3 USD 0, no link USD 640 thousand | yes | yes |
| P1-g | No funding, ranking, strategy or "pause" line | yes | yes |
| P1-h | Same structure after reopen | yes | n/a |

## Claude

Account or plan: ______ Code execution and file creation on: yes / no Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: lists the columns after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Data check card | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 4: | |
| Log save card | | | n/a | |
| Stretch: funding scenarios | | | No recommendation line: yes / no | |
| Stretch: custom skill | | | n/a | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a | | |
| P1-b | | |
| P1-c | | |
| P1-d (expected yes, then no) | | |
| P1-e | | |
| P1-f | | |
| P1-g | | |
| P1-h | | n/a |

Screen names that differ from the card: ______

## ChatGPT

Account or plan (Plus or higher): ______ Project memory mode: default / project-only Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: lists the columns after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Data check card | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief, new chat outside the project) | | | Items 1 to 4: | |
| Log save card | | | n/a | |
| Stretch: funding scenarios | | | No recommendation line: yes / no | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a | | |
| P1-b | | |
| P1-c | | |
| P1-d (expected yes, then no) | | |
| P1-e | | |
| P1-f | | |
| P1-g | | |
| P1-h | | n/a |

| ChatGPT proof item | Result |
| --- | --- |
| G2-PF-02: ChatGPT Work returns the capacity sheet with formulas on Plus. Which memory mode allows it? | |
| Check sample outside the project: minutes to paste the brief and attach 3 files (question 4) | |
| Label of the memory setting at project creation | |

Screen names that differ from the card (note the real label for adding project files and for the memory setting): ______

## Copilot agent builder

Run this table twice: once with a Microsoft 365 Copilot license (or pay-as-you-go billing), once with Copilot Chat only and no billing (no-license path on the card).

License state: licensed / no license Date tested: ______ Tester: ______ Tester wrote the card: yes / no

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: lists the columns after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Data check card | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Lab 1, no-license path | | | | |
| Check sample (debrief) | | | Items 1 to 4: | |
| Log save card | | | n/a | |
| Stretch: funding scenarios | | | No recommendation line: yes / no | |

| P1 check | Before the fix (licensed) | After the fix (licensed) | No-license path |
| --- | --- | --- | --- |
| P1-a | | | |
| P1-b | | | |
| P1-c | | | |
| P1-d (expected yes, then no) | | | |
| P1-e | | | |
| P1-f | | | |
| P1-g | | | |
| P1-h | | n/a | |

| Copilot proof item | Result |
| --- | --- |
| G2-PF-01: Knowledge takes the `.txt` copies and `capacity-sheet.xlsx` (one sheet) | |
| G2-PF-03: code interpreter toggle (**Create documents, charts, and code**) shown or always on? Does it read the embedded sheet, or only the one sent in chat? | |
| G2-PF-05: `copilot-fallback-instructions-m1.txt` (6,673 characters) accepted in **Instructions** and the run works | |
| Upload of `.md`, `.xlsx` in the agent chat (3 files in one message, steps 2 and 6). Paste works when upload fails | |
| Output file kept after the session ends (mb-11 says no) | |

Screen names that differ from the card (note how you send a file in the agent chat): ______

## Gemini

Account: personal / Workspace (test on a Workspace account if you can, gm-03) Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: lists the columns after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Data check card | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 4: | |
| Log save card | | | n/a | |
| Stretch: funding scenarios | | | No recommendation line: yes / no | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a | | |
| P1-b | | |
| P1-c | | |
| P1-d (expected yes, then no) | | |
| P1-e | | |
| P1-f | | |
| P1-g | | |
| P1-h | | n/a |

| Gemini proof item | Result |
| --- | --- |
| `.xlsx` accepted as a skill file (question 9). If not, CSV works | |
| G2-PF-04: one skill run that asks for a Google Sheet with formulas. What came back? | |
| Log save: **More**, then **Replace file**, then **Save** works (or whole-skill re-upload needed), and minutes taken | |
| The skill runs with **/** in a new chat after reopen | |

Screen names that differ from the card (note the skill instructions field and how you open an existing skill to edit it): ______

## Summary for Gate 3

| Platform | Build check pass | Lab 1 minutes | Second sample pass | P1-d before (error shows) | P1-d after (fixed) | Stuck points (count) | Tester |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude | | | | | | | |
| ChatGPT | | | | | | | |
| Copilot (licensed) | | | | | | | |
| Copilot (no license) | | | | | | | |
| Gemini | | | | | | | |
