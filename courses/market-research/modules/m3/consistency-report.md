# Consistency report: module 3 (The weekly run)

Course: `market-research`. Checker: consistency reviewer, 2026-11-27. Inputs: `modules/m3/module.md`, `modules/m3/kit/`, `modules/m3/card-test.md`, `spec.yaml` (module 3, `stretch_scope`, `planted_error_fade`, `copilot_no_license_fallback`, `catch_up_kits`), `case/` (2027 case year), `shared/registry/registry.yaml`, `research/stretch-verification-2026-11.md`, `modules/m1/` (approved) and `modules/m2/` (in review, `kit/kit-m3/`). Dan's rules of 2026-11-27 applied: short lab brief slides, complete cards; schedule stretch on the Claude card only; ChatGPT no schedule stretch; Copilot and Gemini core path only; hint level, no audit hint.

## Checks

| # | Check | Result | Note |
| --- | --- | --- | --- |
| 1 | Spec match | Pass, with concerns | Title, rung, 60 minutes, 24/36 split, arc, goal, PM decision, 6 card steps, planted error, hint and kit match. Three spec wordings differ and are not all on the "Changes needing Dan's yes" list (finding 5) |
| 2 | Case match | Pass, 2 minor | All record ids searched in `m3-feedback-week-1.csv`, `m3-feedback-week-2.csv`, `m3-check-sample.md`: F-1104, F-1108, F-1124, F-1201 to F-1205 (A-05), F-1207, F-1209, F-1214, F-1215 to F-1219, F-1221, F-1222, F-1229, F-1232, F-1305 to F-1307, F-1312. Quotes on 3.6 and 3.14 are word for word. 24 and 32 items, 5 channels, 3 segments: correct. Week 2 table and flag report match `expected-results.md`. Findings 8 and 9 |
| 3 | Planted error | Pass, 1 minor | F-1215 to F-1219 are in week 2 and use "inspection report", "audit", "inspector". Warning is "Audit before you approve." Success check does not name the error. 3.14 reveals it and names the reason check that passes and the audit that finds it. Finding 10 |
| 4 | Demo to lab | Pass | Claude only. Same 2 files, same 2 exports, same prompt, same chat pattern as the cards |
| 5 | Cards | Pass, 3 minor | 6 core steps, identical on 4 cards. All headers present. Over-20-word sentences are only the spec data safety text (fixed wording, m1 D15) and the Claude code-execution note (as approved in m1). Schedule stretch on Claude only, ChatGPT reason line, standard line on Copilot and Gemini. Findings 4, 7, 11 |
| 6 | Kit | Pass | Every card file is in `kit/lab-3/` or `kit/kit-m4/`. Every `.txt` copy equals its `.md` (`cmp`). `lab-3/tag-list.md` equals `case/m3-tag-list.md`. Fallback texts contain brief, job card and tag list exactly. Counts: job card 1,496 (1,500), tag list 1,828 and v2 2,038 (2,800), brief v3 3,094 and v4 3,253 (3,500), fallbacks 6,856 and 7,194 (7,800). The job card and tag list hold no meaning rule, so the error is not pre-fixed |
| 7 | Timing | Concern | Slides add to 8 + 8 + 8 + 28 + 8 = 60. 40/60 exact. 3.12 time guide, minute cues and 28-minute timer agree. Agenda rows (full day 13:00, half day 2 09:10) are 60. Run times disagree (finding 3) |
| 8 | Notes | Pass | All 17 slides have `POINT:` then `Talk Track:`. No `[AI USE CASE TT]`. Story slot on 3.4 is told as Pragmatic's or a client's, with a skip path |
| 9 | Registry | Pass | No scheduled-task setup slide (CAW-AI slide 9). Own feedback into own backlog, not public reviews. Pervasiveness is referred to as known (PDW-AI). Survey wave stretch has no slide (critic S8). No repeated slide titles across m1 to m3 |
| 10 | Words | Pass | No em or en dashes (one ellipsis in a quoted screen name only). No "exception" or "escalation". "Pattern" and "validated" appear only in "never write" rules and log headers, as in m1 and m2 kits |
| 11 | Carry forward | Concern | Start state: kit-m3 (brief v3, 6 files) matches the cards, demo and fallback. kit-m4 files not touched in lab 3 equal kit-m3 (`cmp`). Brief v4 = brief v3 plus the case fix rule. End state does not equal kit-m4 (finding 1). Module 2 card text disagrees with module 3 (finding 2) |

## Findings

| # | Severity | Where | Problem | Fix |
| --- | --- | --- | --- | --- |
| 1 | Major | `kit/kit-m4/tag-list.md` (v2, P10), `kit-m4/problem-backlog.md` (P10 row), slide 3.17, section 6 log save card, B11, D6 | A learner who finishes lab 3 has tag list v1 and a backlog with no P10 row. No step, card line or log save line adds P10. The agent does not make a problem code from a "no fit" group. So the learner end state is not kit-m4 | Choose one, and say it in D6: (A) keep kit-m4 v2, and add one line to the kit-m4 README and the 3.17 talk track: "kit-m4 also holds the case PM's decision: P10 added to the tag list and the backlog. On your own work, add your own new tag the same way." Or (B) keep kit-m4 tag list at v1 and P10 in the backlog only (D6 option B) |
| 2 | Major | `modules/m2/module.md` ChatGPT card Stretch line (line 579), section 1 "Decided by Dan" D2 Applied column, LD spec row | Module 2 ChatGPT card says "The schedule stretch is in module 3." Module 3 ChatGPT card says the schedule stretch is not available. Dan's rule: schedule stretch on the Claude card only | Module 2 builder: change the ChatGPT card line to "No stretch step in module 2." Keep the Claude card line. Update the D2 Applied text to match |
| 3 | Major | Slide 3.5 (6 minutes), 3.12 time guide, slide 3.13 (3 minutes), D2 | Three run-time assumptions disagree. The demo adds 2 files and runs 24 and 32 items in 6 minutes. The lab gives 11 minutes for the same two runs (3 to 9, 9 to 14). The debrief rerun does both weeks in 3 minutes | Send week 1 at the start of 3.5 and talk over it. Add a cut-over cue to the demo script: "If week 2 is not done at minute 6, show the rehearsal output." Add a card test row for demo run time. Keep the card test rule for the rerun (D2 option B if over 3 minutes on 2 platforms) |
| 4 | Minor | Section 6 "Check sample" pass, section 7 "5-item pass condition", card pass condition | The card has 5 pass items. Section 6 lists 3, as in `expected-results.md`. Items 4 (F-1312 "no fit") and 5 (no trend) come from the case table and the spec `no_threshold` | Make section 6 list the same 5 items, with the source of items 4 and 5 |
| 5 | Minor | Section 1 "Changes needing Dan's yes" | Three spec wordings differ from the module and are not listed: module 3 `arc` and `debrief_check` say "Rerun week 2" (module reruns both weeks, D2); `planted_error_fade.success_checks` says "run this in the debrief" (card says after class, D12); `stretch_scope` and `stretch_verification.rule` need "a dated vendor doc and a test" (Claude card ships before the test, D1) | Add 3 rows, each conditional on D2, D12 and D1 |
| 6 | Minor | D1 option B and "If your test fails" | If Dan's Claude test fails, the card uses the standard line, but slide 3.9 on-slide text, its talk track, section 7 "Steps per platform" and the section 9 stretch row also name the Claude schedule | List these 4 places in D1 so the B path is complete |
| 7 | Minor | Copilot card, "No Copilot license" box; `lab-3/README.md` | The box tells learners to send `problem-backlog.txt` at step 2. The debrief rerun is in a new chat, and the box does not say to send the backlog again | Add to the box: "Debrief rerun: send your `problem-backlog.txt` again with both exports." Same line in the README |
| 8 | Minor | `kit-m4/problem-backlog.md`, P04 "Willingness to pay clues" | Says "Staff time (I-112). No buyer named a price". `case/m4-evidence-pack.md` Part 4 says "1 account asks about a battery swap service (A-11, feedback)". B12 says the kit uses Part 4 facts | Use the Part 4 text. Recount characters in section 8 and the kit-m4 README |
| 9 | Minor | Slide 3.2 talk track | "The Head of Product asks: 'Which new problems show up in weekly feedback?'" `case/company.md` lists it as current market question 3, with no owner | Say "One of Larkspan's current market questions is ..." |
| 10 | Minor | Slide 3.7 talk track | "It is short, and it is where new things show up" points learners at the "no fit" group as the place of the error, before the lab. Dan's rule: no audit hint in a middle lab. The reveal on 3.14 already gives this clue | Cut the clause. Keep "And every item in the 'no fit' group." |
| 11 | Minor | Claude card, schedule stretch step 4 | One step enters a name, a prompt, a frequency and a folder, and **Save** is only in the note | Split into "Enter a name and the prompt ..." and "Choose **Weekly** and the project folder. Select **Save**." (5 stretch steps, still 6 or fewer) |

## Must fix

1. Finding 1: make the module 3 end state equal kit-m4 (README and 3.17 line, or D6 option B).
2. Finding 2: module 2 ChatGPT card stretch line.
3. Finding 3: demo cut-over cue and a run-time row in the card test.
4. Findings 4 to 11: minor text fixes, each listed above.

## Consider

- Survey wave stretch is on the Copilot and Gemini cards. This matches `stretch_scope` (it limits only schedule and second agent) and the approved module 1 screening stretch. Confirm with Dan that "core path only" means no schedule or second-agent step.
- Slide 3.14 holds the reveal, the fix rule, 2 secondary checks and a clue in 2 minutes with 2 or 3 answers. Card test or rehearsal should time it. Move A-05 and F-1221 to 3.15 if it runs long.
- Slide 3.8 "Many feedback tools show you only the 'top movers'" is a factual claim with no source. Verifier to check, or say it as the course view.
- `kit-m4/problem-backlog.md` is 15,176 characters. Copilot no-license learners paste it in module 4 (G2-PF-03 not verified). Tell the module 4 builder; the spec split plan for the evidence pack may apply here too.
- The spec core message, slide 3.1 bullet and card step 6 all name the "no fit" rule before the lab. This is spec text, so no change, but it is a strong hint for a forced-fit error.
