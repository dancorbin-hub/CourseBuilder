# Card test: module 2 (lab 2)

Course: `market-research`. For Dan (Gate 3). Draft 2026-11-27.

Gate 2 proof P1 covers modules 1 and 2 (spec `gate_2_proof_patterns`). This card test also records the module 2 part of P1, including the Copilot no-license fallback for module 2 (module 1 decision D13).

## How to test

1. Start each platform with the agent in its state after module 1. If you have none, rebuild it from `modules/m1/kit/kit-m2/` and record the minutes.
2. Open the real Word or PDF card for the platform. Follow it with no other help (PRD card test).
3. Do not open `case/planted-errors.md` or `case/expected-results.md` during a run.
4. Record minutes per card, and every place you got stuck. A stuck point is any moment you had to guess, search or ask.
5. Record every screen name on the card that differs from the screen.
6. At least one person who did not write the card tests the Copilot card (module 1 decision D9).

Target times: rebuild from kit-m2 about 5 minutes. Lab 2 core path 32 minutes (half day 34). Check sample 3 minutes. Log save card 1 minute.

## Extra steps for proof P1, module 2 (not on the learner card)

| When | Extra step | Records |
| --- | --- | --- |
| After lab step 2 | Save the output file. Fill the "before the fix" column | P1-m2-a to P1-m2-g, before |
| After lab step 6 | Save the output file. Fill the "after the fix" column | P1-m2-a to P1-m2-g, after |
| After the log save card | In a new chat, ask "List your knowledge files and the number of rows in the driver log." | P1-m2-h |

## Claude

Account or plan: ______ Code execution and file creation on: yes / no Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m2 (if used) | | | n/a | |
| Lab 2, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |

| P1 check, module 2 | Before the fix | After the fix |
| --- | --- | --- |
| P1-m2-a downloadable file, or full tables in one message | | |
| P1-m2-b driver log has 14 deals, each labeled "interview" or "CRM only" | | |
| P1-m2-c **planted error**: D-2214 labeled interview, or a CRM-only deal has a buyer driver, or price shows 2 or more buyer deals | (expected yes) | (expected no) |
| P1-m2-d match rate table counts 9 deals: won 3 (2 match), lost 6 (2 match) | | |
| P1-m2-e flag report lists D-2202, D-2203, D-2207, D-2209, D-2212 (reasons differ) and D-2209 (alternative not in the code book) | | |
| P1-m2-f each driver shows interviewed deals, accounts and segments. No top driver for a segment | | |
| P1-m2-g no "pattern" or "validated". Problem backlog not changed | | |
| P1-m2-h next chat reads the saved driver log | n/a | |

Screen names that differ from the card: ______

## ChatGPT

Account or plan (Go, Plus or higher): ______ Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m2 (if used) | | | n/a | |
| Lab 2, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |

| P1 check, module 2 | Before the fix | After the fix |
| --- | --- | --- |
| P1-m2-a downloadable file, or full tables in one message | | |
| P1-m2-b driver log has 14 deals, each labeled "interview" or "CRM only" | | |
| P1-m2-c **planted error**: D-2214 labeled interview, or a CRM-only deal has a buyer driver, or price shows 2 or more buyer deals | (expected yes) | (expected no) |
| P1-m2-d match rate table counts 9 deals: won 3 (2 match), lost 6 (2 match) | | |
| P1-m2-e flag report lists D-2202, D-2203, D-2207, D-2209, D-2212 (reasons differ) and D-2209 (alternative not in the code book) | | |
| P1-m2-f each driver shows interviewed deals, accounts and segments. No top driver for a segment | | |
| P1-m2-g no "pattern" or "validated". Problem backlog not changed | | |
| P1-m2-h next chat reads the saved driver log | n/a | |

Screen names that differ from the card: ______

## Copilot agent builder

Run this table twice: once with a Microsoft 365 Copilot license (or pay-as-you-go billing), once with Copilot Chat only and no billing (no-license path on the card).

License state: licensed / no license Date tested: ______ Tester: ______ Tester wrote the card: yes / no

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m2 (if used) | | | n/a | |
| Lab 2, steps 1 to 6 | | | | |
| Lab 2, no-license path | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |

| P1 check, module 2 | Before the fix (licensed) | After the fix (licensed) | No-license path |
| --- | --- | --- | --- |
| P1-m2-a downloadable file, or full tables in one message | | | |
| P1-m2-b driver log has 14 deals, each labeled "interview" or "CRM only" | | | |
| P1-m2-c **planted error**: D-2214 labeled interview, or a CRM-only deal has a buyer driver, or price shows 2 or more buyer deals | (expected yes) | (expected no) | |
| P1-m2-d match rate table counts 9 deals: won 3 (2 match), lost 6 (2 match) | | | |
| P1-m2-e flag report lists D-2202, D-2203, D-2207, D-2209, D-2212 (reasons differ) and D-2209 (alternative not in the code book) | | | |
| P1-m2-f each driver shows interviewed deals, accounts and segments. No top driver for a segment | | | |
| P1-m2-g no "pattern" or "validated". Problem backlog not changed | | | |
| P1-m2-h next chat reads the saved driver log | n/a | | n/a (log kept on the computer) |

| Copilot proof item | Result |
| --- | --- |
| G2-PF-02: upload of `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md` in the agent chat, licensed and no license. 2 files in one message | |
| Paste of the CSV as text works when upload fails (1,855 characters) | |
| G2-PF-05: `copilot-fallback-instructions-m2.txt` (7,171 characters) accepted in **Instructions**, and the run works | |
| The fallback still fits after you add your lab 2 rule (about 7,400 characters) | |
| Downloaded driver log kept after the session ends (mb-11 says no) | |

Screen names that differ from the card (note how you send a file in the agent chat): ______

## Gemini

Account: personal / Workspace (test on a Workspace account if you can, gm-03) Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m2 (if used) | | | n/a | |
| Lab 2, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |

| P1 check, module 2 | Before the fix | After the fix |
| --- | --- | --- |
| P1-m2-a downloadable file, or full tables in one message | | |
| P1-m2-b driver log has 14 deals, each labeled "interview" or "CRM only" | | |
| P1-m2-c **planted error**: D-2214 labeled interview, or a CRM-only deal has a buyer driver, or price shows 2 or more buyer deals | (expected yes) | (expected no) |
| P1-m2-d match rate table counts 9 deals: won 3 (2 match), lost 6 (2 match) | | |
| P1-m2-e flag report lists D-2202, D-2203, D-2207, D-2209, D-2212 (reasons differ) and D-2209 (alternative not in the code book) | | |
| P1-m2-f each driver shows interviewed deals, accounts and segments. No top driver for a segment | | |
| P1-m2-g no "pattern" or "validated". Problem backlog not changed | | |
| P1-m2-h next chat reads the saved driver log | n/a | |

| Gemini proof item | Result |
| --- | --- |
| G2-PF-04: `.csv` and `.md` files, 2 in one prompt (lab steps 2 and 6) | |
| **Add**, **files**, **Upload** adds 2 files to an existing skill, then **Save** (or whole-skill re-upload needed), and minutes taken | |
| Log save: driver log added to the skill and read in the next chat | |

Screen names that differ from the card: ______

## Summary for Gate 3

| Platform | Lab 2 minutes | Second sample pass | P1-m2-c before (error shows) | P1-m2-c after (fixed) | Stuck points (count) |
| --- | --- | --- | --- | --- | --- |
| Claude | | | | | |
| ChatGPT | | | | | |
| Copilot (licensed) | | | | | |
| Copilot (no license) | | | | | |
| Gemini | | | | | |

If P1-m2-c is "no" before the fix on 2 or more platforms, the error is too easy to avoid. Tell the course builder. The demo output is the debrief fallback until then.
