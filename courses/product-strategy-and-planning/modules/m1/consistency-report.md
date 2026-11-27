# Consistency report: module 1 (product-strategy-and-planning)

Reviewer: consistency reviewer, 2026-11-27. Files read: `module.md`, `course-open.md`, `card-test.md`, `kit/` (both kits), `spec.yaml`, `case/` (planted-errors, expected-results, m1 files, capacity-sheet, company, README, strategy file), `outline/gate-2-decisions.md`, `outline/syllabus.md` (agenda only), `shared/registry/registry.yaml`, the evidence rows the slides cite. The build log was not read.

## Checks

| # | Check | Result | Detail |
| --- | --- | --- | --- |
| 1 | Spec match | Pass | Title, rung 1, 70/80 minutes, arc steps, goal, PM decision, card steps, planted error, fix text, "told" warning text, learner evidence and kit match `modules.m1`. Small differences: the story slot moved to 1.14 (B4, question 5). `m1-status-q4` is used for run 2 but is missing from spec `inputs.fallback_case` (the module is right, the spec line is short) |
| 2 | Case match | Pass | Rechecked from the case files: Q3 total 4,550, O1 910, O2 3,000, O3 0, no link 640; Firmware 200% (24 against 12 FTE); other teams 90. Q4 total 4,750, Firmware 150% (18 against 12), Test lab exactly 100, Cloud 95, O2 KR 3,400, O2 tag 590. Check sample Test lab 130% (7.8 against 6), Hardware design 95. P-03 (Q3) and P-02 (Q4) status flags, P-04 links. Dates 2027-11-16 to 2027-11-24. All ids exist. Kit copies of the strategy file and capacity sheet are byte-identical to `case/` |
| 3 | Planted error | Pass, 1 concern | Error is in `m1-submissions-q3.md`; the sheet `Per_program_check` passes each row; the template has no team total. 1.10 uses the spec text. Success check is general. 1.12 reveals it and names the audit. Concern: the card pass condition, which learners hold during the lab, names "cross-program total". Spec `planted_error_fade.rule` says the error-specific pass condition is in the debrief only. PRD lab rule 7 wants it on the card and on the slide before the lab. See Should fix 1 |
| 4 | Demo to lab | Pass | Claude only. Same brief v1, job card, strategy file, capacity sheet, run files and prompt as the cards. Demo step 2 says "replace the starter text". Card step 1 does not say replace (Should fix 5) |
| 5 | Cards | Concern | Same 6 core steps on all 4 cards. Opening line, save note, check date, data safety, data check card, "Start here with sample data", pass condition with the second sample all present. Stretch within `stretch_scope`. Step sentences are 20 words or fewer. Over 20: data check question 2 (22) and the data safety text, both spec text (question 12). Fails: Copilot step 1 (Must fix 1). Google Sheet line is a shared block, not on each card (Should fix 3). Copilot step 2 runs "in the agent chat", not a new chat as B2 says |
| 6 | Kit | Concern | Every loaded `.md` has a `.txt` copy. Counts measured: brief v1 2,164 and v2 2,469 (budget 3,500), job card 1,365 (1,500), strategy `.txt` 2,770 (2,800), fallback 6,673 and 6,997 (8,000). `template_contents` checks and hand-off rules match word for word. The team total is left out of the job card, brief and sheet, as planned. Fails: the Google Sheet template the cards name does not exist (Must fix 2). `kit-m2/job-card-requests.md` is listed but missing (Should fix 2) |
| 7 | Timing | Pass, 1 concern | Full day 8 + 11 + 9 + 33 + 9 = 70 (28/42, 40%). Half day 9 + 12 + 11 + 38 + 10 = 80 (32/48, 40%), equal to spec `arc_minutes`. Open 5 + 10 + 10 = 25. Lab time guides add to 33 and 38 and match spec `minute_by_minute_lab_1`. 1.11, 1.13 and 1.16 match their notes and the syllabus agenda. Concern: O.7 is 3 minutes, but its talk track says "Two minutes" (Should fix 4) |
| 8 | Notes | Pass | 24 slides, 24 `POINT:` then `Talk Track:`. No `[AI USE CASE TT]`. The story slot says "never as your own". Cues, expected answers and recoveries are complete enough for another instructor |
| 9 | Registry | Pass | No Strategy Matrix, box mapping or "peanut butter" count. The PRW-AI brief structure is named as known (1.5), not retaught. Boundaries and guardrails get a new slide (1.8). No scheduled task. Headlines 1.12, 1.13, 1.15, 1.16 and O.4 have the same text as in the Market Research module 1. The content is different (Consider 1) |
| 10 | Words | Pass | No em or en dashes in any module or kit file. No "exception", "escalation" or "no magic number". The agent output in the kit has no "pattern" or "validated" |
| 11 | Carry forward | Pass | `kit-m2` = brief v2 (the fix text plus the "more than 100 percent" choice), unchanged job card and strategy file, capacity sheet filled with the Q4 asks (Q1 2028), and the case PM's calls. This matches the module 1 end state and `expected-results.md`. The m2 job card is open (Should fix 2) |

### Dan's extra rules

| Rule | Result |
| --- | --- |
| Trendslop in words only, no HBR figures | Pass. O.2 and its notes have no numbers, and a cue says not to quote them. Consider 2 is about the model names |
| No W1 or W3 figures on slides | Pass. 1.2 states them in words. N21 (72.2%) is in the talk track only. N21 is verified, but rule 4 is still open (question 1) |
| Every slide number has a verified ledger id or is case data | Pass. Slide numbers are case data only |
| Lab brief slide is short and points to the workbook | Pass (1.10) |
| Case set in 2027, plan year 2028 | Pass. No case date in 2026 |
| The agent never sets, ranks or recommends strategy or funding | Pass. Core rule in brief v1 and v2, hand-off rule 3, pass condition item 4, recovery rows |
| No "no magic number", "exception", "escalation", or dashes | Pass |
| No connector lane in module 1 | Pass (section 4 says so; O.7 says "none needed") |
| Google Sheet option on every platform, no live-write claim | Concern. There is no live-write claim. But the template does not exist, and the option is only a shared block (Must fix 2, Should fix 3) |

## Must fix

1. **Copilot card step 1 loads the wrong file.** "the other `.txt` files with **Upload**" also takes `copilot-fallback-instructions-m1.txt`. That file has the whole brief v1 with "My rules: None yet." A licensed learner then has 2 conflicting briefs, and the step 5 fix can lose. Name the files: "`job-card-portfolio-pack.txt` and `strategy-okrs-kpis.txt` with **Upload**".
2. **The Google Sheet template does not exist.** Every card, the kit README and the Gemini core path ("Check the sums in your Google Sheet copy") need it. It is not in `kit/`, and no share link is given. Make it, and put the link in the kit README and on each card before the card test (question 10). If Dan picks question 10 option B, remove the Gemini sums check too, and give Gemini the `.xlsx` or CSV path.

## Should fix

1. **Pass condition on the card against the spec.** This spec still says the error-specific pass condition is "in the debrief only". PRD lab rule 7 wins (Market Research Gate 3 D7: keep it on the card, update the spec). Add this as a question for Dan, and update `planted_error_fade.rule`. PRD rule 7 also puts the second sample on the slide before the lab. 1.10 has no second sample line. Add "Second sample: `m1-check-sample.md`, in the debrief", or record Dan's choice.
2. **`kit-m2` is not complete.** `job-card-requests.md` and its `.txt` are listed in the kit-m2 README and in spec `catch_up_kits` (8 files), but they are not there. The module 2 builder must add them before the module 2 card test (question 11).
3. **Put the Google Sheet line on each card.** It is now one block "(every card)" above the cards. A renderer can drop it. Copilot: say `.xlsx` only, as spec `platform_cards.copilot` says ("download .xlsx"). The block says "`.xlsx` or CSV". The block says "The agent does not write live". The Gemini note says "not verified". Use "not verified" on all cards, as spec `never_say` asks.
4. **O.7 timing.** The slide is 3 minutes, but the talk track says "Two minutes". Change it to "Three minutes", or say the data check part only takes two.
5. **Card step 1 does not say "replace".** The build check put the 3-line starter in the instructions. Step 1 on all 4 cards should say "Replace the starter instruction with `brief-v1`". The demo step 2 already says this.
6. **Copilot card step 2.** It says "In the agent chat". B2 and the other cards use a new chat. The build check chat is still open. Change it to "In a new chat".

## Consider

1. Rename the 1.12, 1.13, 1.15, 1.16 and O.4 headlines so they do not repeat the Market Research headlines word for word (house rule 9). Or ask Dan if arc slides with the same headline are allowed.
2. O.2 talk track: "including ChatGPT, Gemini and Claude". E3 takes the model names from a third-party full-text copy (zby.github.io). Fortune confirms only that 7 models were tested. Check that S-T2 or S-T3 names the models, or say "models from the big vendors, including the one some of you use today".
3. 1.14 has a lot in 2 minutes: 3 flags, 1 minute of writing, the case PM's calls, and an optional 30-second story. Record the time in the card test, or move the story to the half day only.
4. O.6: "you read only the flags". Spec rung 3 plus says the PM also audits 2 measures. Add "and audit a sample".
5. Spec `data_safety` for m1 says "The pack log keeps totals and decisions". The module uses the capacity sheet as the log, and decisions are on the record sheet. Align the wording, or tell the planner.
6. Claude card note on the "new version of projects" (Library). The row is in the Market Research matrix but not in the verifier list in section 1. Add it.
7. Copilot sends `.md` run files in chat. There are no `.txt` or `.xlsx` copies of `m1-submissions-q3/q4.md` or `m1-check-sample.md`. The card test row covers this. If the upload fails, ask the case builder for `.txt` copies.
8. `Team_capacity_pct` = 100 is fixed in the template sheet. Spec `pm_sets_the_rules` says the template leaves thresholds blank. Label it in the kit README as the case PM's choice that the learner can change.
