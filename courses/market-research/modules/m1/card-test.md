# Card test: module 1 (lab 1 and the opening build check)

Course: `market-research`. For Dan (Gate 3). Draft 2026-11-26.

Decision 13: this card test of lab 1 doubles as Gate 2 proof P1. So each platform run records the card test and the P1 checks P1-a to P1-i (`proof/README.md`).

## How to test

1. Open the real Word or PDF card for the platform. Follow it with no other help (PRD card test).
2. Start with the opening build check card (`course-open.md`, section 3). Then the lab 1 card (`module.md`, section 5).
3. Do not open `case/planted-errors.md` or `case/expected-results.md` during a run.
4. Record minutes per card, and every place you got stuck. A stuck point is any moment you had to guess, search or ask.
5. Record every screen name on the card that differs from the screen.
6. At least one person who did not write the card tests the Copilot card (PRD card test, proposed).

Target times: build check 10 minutes. Lab 1 core path 33 minutes (half day 38). Check sample 3 minutes. Log save card 1 minute.

## Extra steps for proof P1 (not on the learner card)

| When | Extra step | Records |
| --- | --- | --- |
| After the build check | Close the browser tab. Reopen the agent before lab step 2 | P1-i (structure after reopen) |
| After lab step 2 | Save the output file. Record the "before the fix" column | P1-a to P1-g, before |
| After lab step 5 | In a new chat, send batch 1 only with "Run the problem backlog job". Save the output | P1-a to P1-h, after (batch 1) |
| Lab step 6 | Run as on the card (both batches, new chat) | Debrief check (P05 flag in batch 1, P06 disagreement in batch 2) |

Decision 2 rule: if P1-d is "no" before the fix on 2 or more platforms, the error is too easy to avoid. Tell the course builder, who brings option B back with your results.

## Claude

Account or plan: ______ Code execution and file creation on: yes / no Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: answers after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |
| Stretch: screening | | | Edge cases to the PM: AP-07, AP-08, AP-10, AP-12? | |
| Stretch: custom skill | | | n/a | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a downloadable file, or full tables in one message | | |
| P1-b evidence profile with interview count, accounts and segments | | |
| P1-c proposed ranking with a reason for each rank | | |
| P1-d **planted error**: P05 (I-104) in the top 3, or first in Food service | (expected yes) | (expected no) |
| P1-e P05 shows 1 interview, 1 account, "single source" | | |
| P1-f P01 and P02 show 4 interviews and 4 accounts each | | |
| P1-g no "pattern" or "validated" | | |
| P1-h P05 in the flag report, ranked last or near last | n/a | |
| P1-i same structure after reopen | | n/a |

Screen names that differ from the card: ______

## ChatGPT

Account or plan (Go, Plus or higher): ______ Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: answers after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |
| Stretch: screening | | | Edge cases to the PM: AP-07, AP-08, AP-10, AP-12? | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a downloadable file, or full tables in one message | | |
| P1-b evidence profile with interview count, accounts and segments | | |
| P1-c proposed ranking with a reason for each rank | | |
| P1-d **planted error**: P05 (I-104) in the top 3, or first in Food service | (expected yes) | (expected no) |
| P1-e P05 shows 1 interview, 1 account, "single source" | | |
| P1-f P01 and P02 show 4 interviews and 4 accounts each | | |
| P1-g no "pattern" or "validated" | | |
| P1-h P05 in the flag report, ranked last or near last | n/a | |
| P1-i same structure after reopen | | n/a |

Screen names that differ from the card (note the real label for adding project files): ______

## Copilot agent builder

Run this table twice: once with a Microsoft 365 Copilot license (or pay-as-you-go billing), once with Copilot Chat only and no billing (no-license path on the card).

License state: licensed / no license Date tested: ______ Tester: ______ Tester wrote the card: yes / no

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: answers after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Lab 1, no-license path | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |
| Stretch: screening | | | Edge cases to the PM: AP-07, AP-08, AP-10, AP-12? | |

| P1 check | Before the fix (licensed) | After the fix (licensed) | No-license path |
| --- | --- | --- | --- |
| P1-a downloadable file, or full tables in one message | | | |
| P1-b evidence profile with interview count, accounts and segments | | | |
| P1-c proposed ranking with a reason for each rank | | | |
| P1-d **planted error**: P05 (I-104) in the top 3, or first in Food service | (expected yes) | (expected no) | |
| P1-e P05 shows 1 interview, 1 account, "single source" | | | |
| P1-f P01 and P02 show 4 interviews and 4 accounts each | | | |
| P1-g no "pattern" or "validated" | | | |
| P1-h P05 in the flag report, ranked last or near last | n/a | | |
| P1-i same structure after reopen | | n/a | |

| Copilot proof item | Result |
| --- | --- |
| G2-PF-01: does Knowledge take `code-book.md`? (the card uses `.txt`) | |
| G2-PF-02: upload of `.md` batch files in the agent chat, licensed and no license. 2 files in one message (lab step 6) | |
| G2-PF-05: `copilot-fallback-instructions-m1.txt` (7,111 characters) accepted in **Instructions** and the run works | |
| Paste of a batch as text works when upload fails | |
| Downloaded file kept after the session ends (mb-11 says no) | |

Screen names that differ from the card (note how you send a file in the agent chat): ______

## Gemini

Account: personal / Workspace (test on a Workspace account if you can, gm-03) Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Build check | | | n/a (pass: answers after reopen: yes / no) | |
| Fast-start (if used) | | | n/a | |
| Lab 1, steps 1 to 6 | | | | |
| Check sample (debrief) | | | Items 1 to 5: | |
| Log save card | | | n/a | |
| Stretch: screening | | | Edge cases to the PM: AP-07, AP-08, AP-10, AP-12? | |

| P1 check | Before the fix | After the fix |
| --- | --- | --- |
| P1-a downloadable file, or full tables in one message | | |
| P1-b evidence profile with interview count, accounts and segments | | |
| P1-c proposed ranking with a reason for each rank | | |
| P1-d **planted error**: P05 (I-104) in the top 3, or first in Food service | (expected yes) | (expected no) |
| P1-e P05 shows 1 interview, 1 account, "single source" | | |
| P1-f P01 and P02 show 4 interviews and 4 accounts each | | |
| P1-g no "pattern" or "validated" | | |
| P1-h P05 in the flag report, ranked last or near last | n/a | |
| P1-i same structure after reopen | | n/a |

| Gemini proof item | Result |
| --- | --- |
| G2-PF-04: 2 batch files in one prompt (lab step 6) and 3 files added to the skill (lab step 1) | |
| Log save: **More**, then **Replace file**, then **Save** works (or whole-skill re-upload needed), and minutes taken | |
| The skill runs with **/** in a new chat after reopen | |

Screen names that differ from the card (note the skill name field and how you open an existing skill to edit it): ______

## Summary for Gate 3

| Platform | Build check pass | Lab 1 minutes | Second sample pass | P1-d before (error shows) | P1-h after (fixed) | Stuck points (count) |
| --- | --- | --- | --- | --- | --- | --- |
| Claude | | | | | | |
| ChatGPT | | | | | | |
| Copilot (licensed) | | | | | | |
| Copilot (no license) | | | | | | |
| Gemini | | | | | | |
