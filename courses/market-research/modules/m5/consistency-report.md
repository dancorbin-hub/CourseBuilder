# Consistency report: module 5 and course close

Reviewer: consistency-reviewer, 2026-11-27. Inputs: `modules/m5/module.md` (sections 1 to 10), `modules/m5/kit/` (lab-5, kit-m5-draft, kit-m5-expected.md, kit-final), `modules/m5/card-test.md`, `spec.yaml`, `case/` (2027 case, `year-shift-map.md`), `modules/m3/kit/kit-m4/`, `proof/`, CLAUDE.md, `shared/registry/registry.yaml`. Module 1 (approved) and modules 2 and 3 (in review) checked where module 5 refers to them.

## Checks

| # | Check | Result | Where it fails |
| --- | --- | --- | --- |
| 1 | Spec match | Pass, with open items | Title, rung, objectives, minutes, arc, lab goal, PM decision, success check, debrief check, evidence and warning level match. Card step 3 prompt (D5), Copilot fallback split (D3), step order against m5-o3 (D10) and the share stretch (D6) differ from the spec and wait for Dan (changes 2 to 4). Findings 5, 12 |
| 2 | Case match | Pass, 1 gap | Every record id in slides, demo, cards, debrief and kit exists in `case/` (searched each id). Counts match `expected-results.md` lab 5 and `planted-errors.md` lab 5. Year shift is applied (R-2025-07, R-2027-03, 2028 roadmap, about 26 months). Gap: finding 7 |
| 3 | Planted error | Concern | The error is in `m5-past-reports.md` (R-2025-07) and Q2. No warning box. Success check does not name it. Debrief 5.13 reveals it and names the check (opening the citation). But the lab steers the audit to Q2 (finding 1), and kit-final shows the fix (finding 2) |
| 4 | Demo to lab | Pass | Claude demo uses the same job card, past reports, rule 5 text, questions file and prompt form ("...for Q3") as the cards |
| 5 | Cards | Pass, minor | Same 6 core steps on 4 cards. Opening line, save note, check date, data safety, "Start here with sample data", pass condition with Q4. Findings 8, 13, 14 |
| 6 | Kit | Concern | `.txt` copies match (`cmp`). Counts within budget (job card 1,398; past reports 2,773; fallback 5,293 and 5,813). kit-final misses 1 job card (finding 3). Copilot README debrief step is wrong (finding 4) |
| 7 | Timing | Pass | Full day 8 + 9 + 9 + 30 + 9 = 65 (26 / 39, 40%). Half day 7 + 8 + 9 + 28 + 8 = 60 (24 / 36). Lab time guide matches `card_step_minutes`. Course close 15 (5 / 10) and 10 (4 / 6) match `course_close` and the agenda |
| 8 | Notes | Pass | 21 slides, each `POINT:` then `Talk Track:`. No `[AI USE CASE TT]`. Story slot on 5.4 told as heard from executives, with a skip path |
| 9 | Registry | Pass | No second-agent or schedule step or slide. Slide 5.7 is new (decision 33). C.1 and C.2 do not repeat slides 1.7 or 1.14. No CAW-AI exit packet. PDW-AI "not yet validated" tag not retaught |
| 10 | Words | Pass | No em or en dashes. No "exception" or "escalation". No "pattern" or "validated" as agent output. No "intensity", "frequency", "impact" or "emerging" |
| 11 | Carry forward | Concern | Start state agrees with kit-m4 (7 files byte-identical, brief v5 = v4 plus the case lab 4 rule, map = lab 4 table after the fix). Driver log needs a case change (finding 5). End state: kit-final is incomplete (finding 3) |

## Findings

### Blocker

1. **The lab points the audit at Q2 (house rule 13, no audit hint in the last lab).** Slide 5.4 names Q2's stake ("He wants to commit it to the 2028 roadmap"). Slide 5.8 adds "A held answer can save a roadmap commitment." Card step 5 and the 5.12 minute 16 prompt say "Pick the answer you would least like to get wrong". Together they lead most learners to the planted answer. D4 asks Dan about the step 5 rule alone.
   Fix: Delete the 5.8 line "A held answer can save a roadmap commitment." On 5.4, use examples that do not single out Q2 (for example, show only the 3 generic questions, or use Q1 and Q5 only). Then put D4 to Dan with the full set of steering lines, not step 5 only. If Dan keeps the risk rule, record his yes in `gate-3-decisions`.

### Major

2. **kit-final reveals the lab 5 error and fix.** `kit-final/brief-v6.md` rule 6, `kit-final/lab-5-fix-rules.md` and the README table ("Q2 report pack: Hold the roadmap commitment") name the error. Slide 5.14 points to kit-final, and C.4 assumes the learner has the folder. Nothing says when learners get it. If it ships with the workbook before class, lab 5 has a full hint. This is a blocker if kit-final ships before the lab.
   Fix: State in the LD spec (section 7, Materials) and in `lab-5/README.md` that kit-final is released after slide 5.13. Or move the case PM decisions table out of the kit-final README into the instructor notes.

3. **kit-final is not the complete agent.** `kit-final/job-card-alternatives-map.md` (and `.txt`) does not exist. The folder holds 4 job cards and 11 knowledge files. The README says 12, and slide C.3 says "5 job cards". The rebuild card makes an agent without job 4.
   Fix: Copy `proof/job-card-alternatives-map.md` and `.txt` into kit-final now, marked "draft until module 4". Replace it when module 4 sets the final card (`kit-m5-expected.md` choice 4).

4. **The Copilot no-license debrief step in `lab-5/README.md` drops the backlog.** README step 5 says "send messages 2 and 3 again. Then send the questions file". In the README, message 3 is the questions file and the backlog is message 1. The card box (item 5) and module section 8 say "messages 1 and 2". Q4 needs P01 from the backlog, so a learner who follows the README fails the check.
   Fix: README step 5: "Debrief: in a new chat, send `problem-backlog.txt` alone, then the driver log, map and past reports. Then send the questions file with the Q4 prompt."

5. **The start state needs a case change that is not made.** `case/expected-results.md`, kit-m5 row, says "Adds the map after lab 4" only, so the case driver log stays Q2 only (kit-m4, 5,047). `kit-m5-draft/driver-log.md` adds the 10 Q3 rows (7,565). Lab 5 Q1 (D-3105, D-3107) and Q4 (D-3108) need them. D2 and change 1 cover this, but until Dan says yes, module 5 and the case disagree.
   Fix: Put D2 and change 1 first in the Gate 3 doc. Without the change, choose D2 option B and check that Q1 and Q4 still pass from the map rows alone.

6. **The share stretch conflicts with `stretch_scope`.** The spec says Copilot and Gemini cards "stay on the core path". The Copilot card has 5 share steps. All 3 share stretches sit under "Stretch (only where verified)" but say "Not yet tested by the course team". Change 4 edits the module 5 `stretch` line only, not `stretch_scope.copilot_and_gemini_cards`.
   Fix: Add `stretch_scope.copilot_and_gemini_cards` to change 4, or take the share steps off the Copilot card (share plan only, as on Gemini). Rename the heading to "Stretch (vendor doc checked, not yet tested)" until the card test passes, as module 3 B7 did for the Claude schedule step.

### Minor

7. **Q4 expected evidence quotes a line the agent does not have.** `expected-results.md` gives D-3108 as "alerts every lunch rush, interview 2027-09-15". That text is only in WL-3108 (evidence pack Part 3). The kit-m5 driver log has "Rimecore's demo had fewer alerts" and no interview date. Builder note 6 hands this to module 4.
   Fix: In `kit-m5-draft/driver-log.md`, use the WL-3108 quote "Your trial sent alerts every lunch rush, and my managers gave up on it." for the D3 driver. Or ask Dan to change the Q4 line in `expected-results.md` to the driver log quote.

8. **Copilot no-license box, item 2, is unclear.** "Put yours under 'My rules'. Skip step 1 above." reads as "skip box item 1" (the paste). Module 3 says "Do the steps above, but skip step 1".
   Fix: Make it its own line: "Skip card step 1. You cannot add knowledge files."

9. **"Part 4 of m4-evidence-pack.md" is not the same text as the kit backlog.** Section 1 and `kit-m5-expected.md` row 5 say the backlog is Part 4. `kit-m4/problem-backlog.md` has a different layout with the same facts (checked: P01, P02, P03, P06, P08, P10 counts, ids and dates agree).
   Fix: Say "kit-m4 `problem-backlog.md` (same facts as Part 4 of `m4-evidence-pack.md`)".

10. **"Log" is used for knowledge files.** Slide 5.1 ("Each job writes a log"), 5.3 ("Four log tiles", including past reports), section 8 ("a log in module 5" for the map) and `monday-plan.md` (alternatives map as a log). The spec counts 2 logs (backlog and driver log) and 5 case knowledge files, and C.3 uses that count.
   Fix: On 5.3 say "four files". In `monday-plan.md` say "logs and the map". Keep the spec count everywhere.

11. **C.3 (kit-final) sits in the recap segment.** The spec `course_close` segment 1 is "Recap of the manager loop. Theme: there is no magic number". Kit-final belongs to segment 2 ("saves kit-final").
    Fix: Move C.3's minute into the Monday plan segment (C.4 is then 11 minutes, recap 4). Or record it as a builder decision.

12. **Open spec differences need Dan's yes before Gate 3 closes.** D3 (past reports in chat), D5 (prompt names the questions), D10 (decide before audit, against m5-o3 "after you open each citation") and D9 (no log save card, against `module_arc` "ends with the 2-step log save card"). Each is logged. D9 has no spec change listed.
    Fix: Add D9 to "Changes needing Dan's yes": a `module_arc` note that module 5 ends with the course close save, not a log save card.

13. **Card step 5 has 2 actions.** "Open every citation in one answer..." and "Pick the answer you would least like to get wrong." Card rule: 1 action per step. The order is also reversed: you pick before you open.
    Fix: Make it one sentence: "Open every citation in the answer you would least like to get wrong." (or the D4 option B wording). Apply finding 1 first.

14. **Pass condition item 4 is 22 words.** "The flag report lists each source over your age limit, each claim on thin evidence (a fact label) and each disagreement between sources." Card rule: 20 words or fewer.
    Fix: "(4) The flag report lists old sources, thin evidence (a fact label) and sources that disagree."
