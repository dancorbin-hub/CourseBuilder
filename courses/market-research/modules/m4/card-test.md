# Card test: module 4 (lab 4)

Course: `market-research`. For Dan (Gate 3). Builder draft 2026-11-27, revised once 2026-11-27.

Gate 2 proof P3 covers modules 4 and 5 (spec `gate_2_proof_patterns`). This card test records the module 4 part of P3: the hand-off from the win/loss job to the map job, the planted error, the Copilot no-license fallback for module 4 (evidence pack pasted in chat), and the rebuild from kit-m5 in about 5 minutes. It also records your hands-on tests of the second-agent stretch on Claude and ChatGPT (`research/stretch-verification-2026-11.md` section 5, tests 3 and 4). No separate timing check for module 4 (Gate 2 decision 8).

## How to test

1. Start each platform with the agent in its state after module 3. If you have none, rebuild it from `modules/m3/kit/kit-m4/` and record the minutes.
2. Open the real Word or PDF card for the platform. Follow it with no other help (PRD card test).
3. Do not open `case/planted-errors.md` or `case/expected-results.md` during a run.
4. Record minutes per card, and every place you got stuck. A stuck point is any moment you had to guess, search or ask.
5. Record every screen name on the card that differs from the screen.
6. At least one person who did not write the card tests the Copilot card (module 1 decision D9).
7. Run the check sample after the log save card, in a new chat, as the card says ("run after class").
8. For step 2, write the draft rule from the demo ("Pass only lost deals to the map. Won deals stay in the driver log."), so the planted error can appear. Record any other rule you try in a second run.

Target times: rebuild from kit-m4 about 5 minutes. Lab 4 core path 25 minutes. Debrief rerun 3 minutes. Log save card 1 minute. Check sample about 5 minutes. Rebuild from kit-m5 about 5 minutes (P3).

## Extra steps for proof P3, module 4 (not on the learner card)

| When | Extra step | Records |
| --- | --- | --- |
| Before step 1 | Check the Instructions length: brief v4 3,253 characters (after step 2: about 3,350; after step 6: about 3,490) | P3 "under 8,000" |
| After lab step 3 | Save the output file. Fill the "before the fix" column | P3-m4-a to P3-m4-h, before |
| After the debrief rerun | Save the output file. Fill the "after the fix" column | P3-m4-a to P3-m4-h, after |
| Demo rehearsal (Claude, instructor) | Time the run: ______ min (target: done by minute 5 of slide 4.5). Slide 4.14 talk track ______ min (target 2) | Run times |
| After the log save card | In a new chat, ask "List your knowledge files. What alternative does D-3108 show in the driver log? What does Rimecore show in Q3 on the map?" | P3-m4-i |
| Any one platform | Rebuild the agent from `kit-m5` in a new project, agent or skill. Time it | P3 rebuild, target about 5 minutes |

## Claude

Account or plan: ______ Code execution and file creation on: yes / no Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m4 (if used) | | | n/a | |
| Lab 4, steps 1 to 6 | | | | |
| Map job run (run minutes) | | | n/a | |
| Debrief rerun (target 3 minutes) | | | n/a | |
| Log save card (2 files). Record the label to delete a project knowledge file (no Claude doc names it; verifier F11): ______ | | | n/a | |
| Check sample (after class, target 5 minutes) | | | Items 1 to 5: | |
| Rebuild from kit-m5 (P3, target 5 minutes) | | | n/a | |

| P3 check, module 4 | Before the fix (step 3 run) | After the fix (debrief rerun) |
| --- | --- | --- |
| P3-m4-a downloadable file, or full tables in one message. Map and driver log as separate files, or separable | | |
| P3-m4-b each map entry links to a deal ID or interview ID | | |
| P3-m4-c each entry shows its source type (buyer interview or CRM only). CRM only kept apart (Q3: D-3109) | | |
| P3-m4-d each "growing" or "fading" label names Q2 2027 vs Q3 2027 and both counts | | |
| P3-m4-e **planted error**: D-3108 under Rimecore. Rimecore Q2 2, Q3 3, "growing". Do nothing 3 | (expected yes) | (expected no) |
| P3-m4-f after the fix: D-3108 under do nothing. Rimecore Q2 2, Q3 2, no change. Do nothing Q2 2, Q3 4, growing. The flag report lists the D-3108 mismatch (CRM Rimecore, buyer kept the spreadsheet) | (expected no) | (expected yes) |
| P3-m4-g audit pick: the growing or fading entries before the fix are ALT-01 Rimecore, ALT-03 and ALT-04 (so the audit reaches D-3108). Flag: do nothing is the top alternative in Food service (Q3: D-3103, D-3106, D-3108 after the fix) | | |
| P3-m4-h D-3102 under Vantafrost (decoy). Won deals (D-3104, D-3110) not on the map. No "pattern" or "validated". Match rate table not recounted | | |
| P3-m4-i next chat reads the saved files: D-3108 shows do nothing; Rimecore Q3 = 2 | n/a | |

| Claude second-agent stretch (Dan, hands-on; `stretch-verification-2026-11.md` test 3) | Result |
| --- | --- |
| **+ New Project**, **Set project instructions** and **+** in project knowledge match the screen | |
| The first project gives the Q3 driver log as a downloadable file after "Run the win/loss job on the Q3 deals" | |
| The second project runs the map job on that file alone. Each map entry links to a deal ID or interview ID | |
| D-3108 in the second project's map: do nothing, Rimecore, or flagged. Record which | |
| Does the second project ask for the interviews, CRM export or backlog? Record what it does with rule 4 (file-only hand-off, verifier F12) | |
| Minutes for the 6 stretch steps | |
| Your account opens projects as one conversation with a Library (cl-pj-11)? If yes, record the screen names | |

## ChatGPT

Account or plan: ______ Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m4 (if used) | | | n/a | |
| Lab 4, steps 1 to 6 | | | | |
| Map job run (run minutes) | | | n/a | |
| Debrief rerun (target 3 minutes) | | | n/a | |
| Log save card (2 files) | | | n/a | |
| Check sample (after class, target 5 minutes) | | | Items 1 to 5: | |

| P3 check, module 4 | Before the fix | After the fix |
| --- | --- | --- |
| P3-m4-a to P3-m4-d (as on the Claude table) | | |
| P3-m4-e planted error (expected yes before, no after) | | |
| P3-m4-f after the fix (expected no before, yes after) | | |
| P3-m4-g and P3-m4-h | | |
| P3-m4-i next chat reads the saved files | n/a | |

| ChatGPT second-agent stretch (Dan, hands-on; `stretch-verification-2026-11.md` test 4) | Result |
| --- | --- |
| **+** next to **Projects**, **Create project**, **•••**, **Project settings**, **Instructions**, **+** then **Add photos & files** match the screen (verifier F1) | |
| The first project gives the driver log as a downloadable file (cg-08, partly verified). If not, the copy-to-text fallback works | |
| The second project runs the map job on that file alone. Each map entry links to a deal ID or interview ID | |
| Does the second project ask for the interviews, CRM export or backlog? Record what it does with rule 4 | |
| Plan used (Go, Plus, other). Minutes for the 6 stretch steps | |

## Copilot agent builder

Account: licensed / pay-as-you-go / no license (Copilot Chat only). Date tested: ______ Tester (not the card writer): ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m4 (if used) | | | n/a | |
| Lab 4, steps 1 to 6 (`.txt` copies) | | | | |
| Map job run (run minutes) | | | n/a | |
| Debrief rerun (target 3 minutes) | | | n/a | |
| Log save card (2 files, same session download) | | | n/a | |
| Check sample (after class, target 5 minutes) | | | Items 1 to 5: | |

| P3 check, module 4 | Before the fix | After the fix |
| --- | --- | --- |
| P3-m4-a to P3-m4-d | | |
| P3-m4-e planted error | | |
| P3-m4-f after the fix | | |
| P3-m4-g and P3-m4-h | | |
| P3-m4-i next chat reads the saved files | n/a | |

| Copilot no-license fallback, module 4 (P3; G2-PF-02, G2-PF-03, G2-PF-05) | Result |
| --- | --- |
| `copilot-fallback-instructions-m4.txt` pastes into **Instructions** (7,419 characters). With your rule 4: ______ characters, under 8,000 | |
| The evidence pack (15,350 characters) goes in one chat message: upload or paste. Record which | |
| If one message fails: the 2 parts split at "## Part 3" (6,590 and 8,760) work | |
| The run uses the map in Instructions and the driver log and backlog in the pasted pack | |
| The map and the driver log can be downloaded or copied in the same session | |
| `kit-m5/copilot-fallback-instructions-m4-v5.txt` (5,388) pastes into **Instructions**. The map pasted alone first (3,286), then the deals, gives a run | |

The second-agent stretch is not on this card (stretch_scope). Record if a tester asks for it.

## Gemini

Account: personal / Workspace (gm-03). Date tested: ______ Tester: ______

| Card | Minutes | Stuck points | Pass or fail on the second sample | Tester |
| --- | --- | --- | --- | --- |
| Rebuild from kit-m4 (if used) | | | n/a | |
| Lab 4, steps 1 to 6 (**Add files** on the existing skill) | | | | |
| Map job run (run minutes) | | | n/a | |
| Debrief rerun (target 3 minutes) | | | n/a | |
| Log save card (2 files: **More**, **Replace file**, or whole-skill re-upload) | | | n/a | |
| Check sample (after class, target 5 minutes) | | | Items 1 to 5: | |

| P3 check, module 4 | Before the fix | After the fix |
| --- | --- | --- |
| P3-m4-a to P3-m4-d | | |
| P3-m4-e planted error | | |
| P3-m4-f after the fix | | |
| P3-m4-g and P3-m4-h | | |
| P3-m4-i next chat reads the saved files (after the re-upload, if used) | n/a | |

| Gemini check (G2-PF-04) | Result |
| --- | --- |
| The evidence pack (`.md`, 15,350 characters) uploads in chat, or pastes | |
| Skill files after step 1: 10. Replacing 2 files at the log save card fits in 1 minute | |

## Results summary (fill after all 4 platforms)

| Platform | Lab minutes | Planted error appeared before the fix | Pass after the fix | Check sample pass | Stuck points to fix on the card |
| --- | --- | --- | --- | --- | --- |
| Claude | | | | | |
| ChatGPT | | | | | |
| Copilot | | | | | |
| Copilot, no license | | | | | |
| Gemini | | | | | |

If the planted error does not appear on 2 or more platforms, tell the builder. The debrief uses the saved demo output, and the card may need a change (Dan's yes).
