# Consistency report: module 1 (and course open)

Course `market-research`. Consistency reviewer, 2026-11-26. Files checked: `modules/m1/module.md`, `course-open.md`, `card-test.md`, `kit/` (all files), against `spec.yaml` (m1 and course sections), `outline/gate-2-decisions.md`, `case/` and `research/bond-stories.md`.

How checked: every record id (I-101 to I-114, I-201, I-204, P01 to P09, F-1108, F-1214, A-07, A-29, AP-07/08/10/12) searched in `case/`. Every quoted buyer line in `module.md` and `kit-m2/problem-backlog.md` matched word for word in the case interview files by script. Counts recomputed from the interview files (14 interviews, 11 accounts; P01 7/6 with the Teller Creek duplicate). Characters measured with `wc -m`. `.md` and `.txt` copies compared with `cmp`. Fallback texts checked to contain brief, job card and code book verbatim. Slide minutes summed per arc step.

## Checks

| # | Check | Result | Line that fails (if any) |
| --- | --- | --- | --- |
| 1 | Spec match | Concern | Card step 6 and slide 1.10 step 6 "send batch 1 and batch 2 in a new chat" vs spec `card_steps` "Send batch 2". Brief v1 fact labels drop "AI-moderated only", spec `template_contents.fact_labels` lists it (decision C2 explains it, spec not updated). All else matches: title, objectives, rung 1, 70/80 minutes, arc, goal, PM decision, planted error, told warning text, learner evidence, kit names |
| 2 | Case match | Pass | All ids exist. All quotes word for word. Debrief counts equal `expected-results.md` batch 2 table. Case PM order and segment tops match. Check sample pass items match lab 1 second sample (see Must fix 4 for one dropped condition) |
| 3 | Planted error | Pass, 1 concern | I-104 is in `m1-interviews-batch-1.md` (3 quotes, P05, only P05 source in batch 1). Warning on 1.10 equals spec text. Success check does not name the error. Debrief 1.12 reveals it and names the evidence profile and audit; quote check passes. Concern: the card pass condition, printed on the card the learner holds during the lab, says "P07 shows 1 interview, not 3" and "all 3 quotes from I-201" (Consider 1) |
| 4 | Demo to lab | Pass | Claude demo uses `brief-v1.md`, job card, code book, empty backlog, `m1-interviews-batch-1.md`, prompt "Run the problem backlog job". Same as cards. Demo stops at batch 1, as spec arc |
| 5 | Cards | Concern | Same 6 core steps on all 4. Opening line, save note, check date, data safety, "Start here with sample data", pass condition, stretch all present. Stretch within `stretch_scope`. Sentences over 20 words: pass condition item 4 (21). Data safety sentence (22) is the spec standard text. Step 1 places files in 2 places (builder Q2) |
| 6 | Kit | Pass, 1 concern | Every loaded file has an identical `.txt`. brief v1 2,730 / 3,500; job card 1,194 / 1,500; code book 2,791 / 2,800; fallback 6,973 / 7,800; brief v2 2,878; fallback v2 7,139. Code book equals `case/m1-code-book.md`. Single-source flag rule left out of v1 on purpose, present in v2. Concern: code book backlog header has 3 fact labels, `kit-m2/problem-backlog.md` header has 2 |
| 7 | Timing | Concern | Arc sums: 8 + 11 + 9 + 33 + 9 = 70; half day 9 + 12 + 11 + 38 + 10 = 80; 28/70 = 40%, 32/80 = 40%. Course open 5 + 10 + 10 = 25. Debrief sub-minutes 2 + 3 + 2 + 1 + 1 = 9 match spec. Faults: slide 1.11 time guide vs its notes and section 9; slide 1.16 transition vs agenda |
| 8 | Notes | Pass | 16 module slides and 9 open slides: each has `POINT:` then `Talk Track:`. No `[AI USE CASE TT]`. Story slot (1.4) framed as a client or Pragmatic story, never the instructor's own, with skip path |
| 9 | Registry | Concern | Slide 1.3 puts one-pass synthesis and the quote check on a slide (registry: "no slides on coding interviews or quote checks"). Slide 1.8 talk track re-defines urgency, pervasiveness and willingness to pay (spec `registry_guard`: refer to the three tests as known) |
| 10 | Words | Pass | No em or en dashes. No "exception" or "escalation". "pattern" and "validated" appear in kit files only as the never-write rule |
| 11 | Carry forward | Pass | `kit-m2` = brief v2 + job card + code book + backlog after batch 2 (case PM order, flag decisions), as spec `catch_up_kits` and `growth` m1 `files_after`. Backlog rows match `expected-results.md`. Module 2 Copilot fallback text is deferred to the module 2 builder (Consider 8) |
| + | Bond story | Pass | O.2 figures equal `research/bond-stories.md` S-B1: 122 transcripts, 68%, 20%, 3%, 9%, JAMIA 2026, published 2026-08-06, "analytic partners rather than autonomous coders", HIPAA setup. "Almost 1 in 3" is the file's hook line (talk track only) |

## Must fix

1. **Card step 6 differs from the locked spec.** `module.md` cards and slide 1.10: "In a new chat, send batch 1 and batch 2". Spec m1 `card_steps` 6: "Send batch 2 with the prompt ...". Get Dan's yes (builder Q1) and record it in `gate-2-decisions.md`, or revert. Card test row "Lab step 6" depends on the answer.
2. **Slide 1.11 timing disagrees with itself and section 9.** On-slide guide: "28 to 33: both batches, new chat". Notes: "[AT MINUTE 30: "Send both batches now, in a new chat."]". Section 9 timing flex: "Behind in the lab: at minute 30, tell learners to skip step 6". Pick one cue (for example minute 28 send; minute 30 behind learners skip). Add half-day minute cues (guide adds 5 minutes, notes do not).
3. **Slide 1.16 transition is wrong for the half day.** "[BREAK, OR MODULE 2 IN THE HALF DAY]". Spec agenda has a 15-minute break after module 1 in both formats (full day 10:35, half day 10:45). Change to "[BREAK]".
4. **Card pass condition item 4.** "(4) The flag report says Pharmacy and lab has no PM-held interview (I-204), and lists P07 (all 3 quotes from I-201)." It is 21 words, and it drops the condition in `expected-results.md` ("If the learner added the lab 1 rule, it also lists P07"). A learner with a different valid rule fails. Split into 2 sentences and restore the condition.
5. **"AI-moderated only" is inconsistent inside the kit.** Brief v1/v2 and `kit-m2/problem-backlog.md` header use 2 fact labels. `code-book.md` (kit and case, fingerprinted) header uses 3, so the agent will output 3. `expected-results.md` uses it for P07 and P08; `kit-m2` P07 omits it. Spec `template_contents.fact_labels` still lists 3. Dan decides (builder Q4), then align spec, code book and kit-m2 in one change.

## Consider

1. **Pass condition on the card vs spec.** Spec `planted_error_fade.success_checks`: "The error-specific pass condition is shown only in the debrief". PRD lab rule 7 puts a second sample and pass condition at the end of each card and on the slide before the lab. The PRD wins, so the card is right, but slide 1.10 then lacks the second sample. Tell Dan about the spec and PRD difference (builder Q13).
2. Record sheet audit hint "Include at least one from the top 3" points at the error (builder Q7). Fine for "told"; do not carry to labs 2 to 4.
3. Slide 1.11 note at minute 12 ("If your run is not done, read the flag report while you wait") cannot be done: the flag report comes at the end of the run.
4. Slide 1.3: make the known items a one-line reference, not a column with definitions. Slide 1.8: replace the three definitions with "You know these from Product Discovery with AI and Foundations" plus how the agent reports them.
5. Data safety box is on slide 1.9, not on the lab brief slide 1.10 (spec `data_safety_note.placement`: "Lab brief slide"). Add the box to 1.10 or call 1.9 part of the lab brief.
6. Copilot fallback texts keep the brief line "find that job card in your knowledge files", but in the fallback the job card is in Instructions. Add one line to the fallback header, or reword.
7. Spec wording, not module: `planted_error.error` says "I-104 (persona P05)". P05 is a problem code. Spec `data_safety_note.standard_text` sentence 2 is 22 words, so every card breaks the 20-word rule. Both need Dan's yes to change.
8. `kit-m2` has only the module 1 rerun fallback. Spec `catch_up_kits.copilot_note` says each kit has a fallback per module. Module 2 builder must add the win/loss fallback (about 2,600 characters left, builder Q9).
9. Half-day extra minutes go also to 1.4 (story), 1.5 (demo) and 1.9. Module line 30 says "as in spec `half_day.note`", which names only the evidence profile, the lab and the debrief order. The spec `arc_minutes` allow it; reword the line.
10. Gemini log save uses **Replace file**; spec `platform_minimums.gemini.file_update` (gm-01) says whole-skill re-upload. Needs a dated Google doc (builder Q5).
11. `kit-m2/README.md`: "Each file has a `.txt` copy" is not true for the README and the fallback. Say "Each loaded file".
