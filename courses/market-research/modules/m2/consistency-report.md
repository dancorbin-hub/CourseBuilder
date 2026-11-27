# Consistency report: module 2 (Win/loss and the match rate)

- Course: `market-research`. Reviewer: consistency-reviewer (Stage 3, step 2a). Date: 2026-11-27.
- Inputs: `modules/m2/module.md`, `modules/m2/kit/`, `modules/m2/card-test.md`, `spec.yaml`, `case/`, `CLAUDE.md`, `shared/registry/registry.yaml`, `research/stretch-verification-2026-11.md`, `modules/m1/` (approved) and `modules/m1/kit/kit-m2/`.
- Read after 2 changes on 2026-11-27: (1) the case moved from 2026 to 2027 (`case/year-shift-map.md`), and (2) Dan approved 3 items (commit e78ee77): the `expected-results.md` phrase, spec card step 6, and the spec m2 stretch line. All case and kit files were checked again after these changes.
- Dan's rule (2026-11-27): lab brief slides show a short version and point to the workbook. Step cards stay complete.

## Checks

| # | Check | Result | Note |
| --- | --- | --- | --- |
| 1 | Spec match | Pass, with 1 concern | Title, objectives, rung, minutes (70 / 75), arc, goal, PM decision, planted error, hint, evidence and kit match. Card step 6 now matches the spec ("In a new chat"). Section 1 decisions are out of date: see finding 1 |
| 2 | Case match | Pass | Every deal id, WL id, quote, account name, amount and count was searched in `case/`. All match `expected-results.md` and `planted-errors.md` after the year shift. Slide 2.5 says "Q2 2027". No quote holds a year |
| 3 | Planted error | Pass, with 1 concern | The error is in the run data (WL-2214, D-2204, D-2210). Brief v2, the job card and the code book do not block it. The warning is the hint. The success check does not name the error. Slide 2.14 reveals it and names the audit. Concern: finding 5 |
| 4 | Demo to lab | Pass | Claude only. Same 2 agent files, same 2 run files, same prompt "Run the win/loss job", new chat |
| 5 | Cards | Pass, with 2 concerns | Same 6 core steps on 4 cards. 1 action per step. Opening line, save note, check date (2026-11-26, inside 30 days), data safety, "Start here with sample data", pass condition with second sample: all there. Only the spec standard data safety sentence is over 20 words (accepted in module 1). Concerns: findings 2 and 7 |
| 6 | Kit | Pass | Each named file is in `kit/lab-2/` with a `.txt` copy (`cmp` same). Driver code book equals the case file. Budgets met: job card 1,483 / 1,500, driver code book 2,284 / 2,800, brief v3 3,094 / 3,500, fallbacks 7,171 and 7,314 / 7,800. Fallback text holds brief v2 from kit-m2 word for word. The fix rule is left out of brief v2 and the job card, as intended. Concern: finding 8 |
| 7 | Timing | Pass | Full day 8 + 10 + 10 + 32 + 10 = 70 (28 / 42, 40%). Half day 8 + 11 + 11 + 34 + 11 = 75 (30 / 45, 40%). Debrief 3 / 2 / 3 / 1 / 1 matches the spec. Lab time guide, room cues and timers agree (full and half day). Agenda: 10:50 for 70, half day 11:00 for 75 |
| 8 | Notes | Pass, with 1 concern | Every slide has `POINT:` then `Talk Track:`. No `[AI USE CASE TT]`. The story slot is optional, with a skip path, and is not told as the instructor's own. Concern: finding 6 |
| 9 | Registry | Pass | No CAW-AI build, no scheduled task slide, no own sources against public reviews, no quote check or synthesis taught again (PDW-AI). "Match rate" only. Module 1 is not yet in the registry, so the module 1 overlap was checked by hand: slide 2.9 refers back to module 1 and applies it to a new job (allowed) |
| 10 | Words | Pass | No em or en dashes in `modules/m2/`. No "exception", "escalation" or "truth rate". "Pattern" and "validated" show only as rules the agent must follow, or in instructor text |
| 11 | Carry forward | Pass | kit-m3 = kit-m2 + lab 2 files + the driver log + rule 2. Problem backlog, code book and job card 1 are the same bytes as in kit-m2. `driver-log.md` matches `m4-evidence-pack.md` Part 1, Q2 rows. 6 knowledge files, as in spec `growth` |
| 12 | Module 1 match | Pass | Card headers, save notes, Copilot no-license box, log save card and debrief order follow module 1. The kit-m2 README says module 2 adds its own fallback text: it does (`lab-2/copilot-fallback-instructions-m2.txt`) |
| 13 | Dan's lab brief rule | Pass | Slide 2.10 has the goal, 5 key actions and a workbook pointer. Slide 2.11 has the pass check, the hint and the data safety box. The full 6 steps are only on the step cards |

## Findings

| # | Severity | Where | Finding | Fix |
| --- | --- | --- | --- | --- |
| 1 | Major | `module.md` section 1: D1, D2, D5, "Changes needing Dan's yes" rows 1 and 2. Section 9, case note 5 | These items still ask Dan to decide things he approved on 2026-11-27 (commit e78ee77). Case note 5 says `expected-results.md` still has "(program minimum met)". It does not now. D2 says cl-sc-07 is not verified. It is now "verified (doc)", and the schedule stretch moved to module 3, Claude card only | Mark D1, D2 and D5 as decided (Dan, 2026-11-27). Delete rows 1 and 2 of "Changes needing Dan's yes". Delete case note 5. Update the D2 text to the stretch verification result |
| 2 | Minor | Claude and ChatGPT cards, "Stretch" line | "It is not yet verified for this course" is now out of date. The spec says the schedule stretch moved to module 3 | Change to: "No stretch step in module 2. The schedule stretch is in module 3." |
| 3 | Minor | Slide 2.14 talk track. Section 6, error reveal | "On the template brief" is not correct. Learners run brief v2 from kit-m2 in lab 2, not the module 1 template | Change to "On brief v2" |
| 4 | Minor | Slide 2.13 talk track | "the 9 deals with a buyer interview" comes 2 lines before "7 of 9 lost deals". These are 2 different groups of 9. Learners can mix them up | Say "7 of all 9 lost deals in the CRM" and "1 of the 6 interviewed lost deals" |
| 5 | Minor | `kit/lab-2/lab-2-record-sheet.md`, section 2 | "For each deal labeled 'interview', find its interview in the notes" goes past the spec step ("including the deal source column"). It leads the learner straight to WL-2214. For the "hint" level this is close to a told warning. D6 covers the card wording only, not this line | Shorten to "Then read the deal source column for every deal." Or add it to D6 for Dan to decide |
| 6 | Minor | Slide 2.11 talk track | Spec `voice.talk_track`: Activity talk tracks start "The goal of this activity is". Slide 2.11 (Activity layout) starts "Done when:". Slide 2.3 also says "one change Dan made". An instructor who is not Dan reads this to learners | 2.11: start "The goal of this activity is to know what done looks like before you start." 2.3: say "with one change for this course" |
| 7 | Minor | Slide 2.10 key actions | 5 key actions. Card step 6 (run again in a new chat) is missing. Learners who read only the slide may skip the rerun | Add "Run again in a new chat." as a 6th short action, or accept it as the short version (Dan's rule) |
| 8 | Minor | `module.md` section 8, fallback sum check | "6,687 plus a 470-character header and separators = 7,171". 6,687 + 470 = 7,157. The real header and separators are 484 characters | Change 470 to 484 |
| 9 | Minor | `card-test.md`, P1-m2-e (all 4 platforms) | The expected flag list leaves out D-2214 (no interview, CRM only). `expected-results.md` flag report item 4 and section 6 of the module have it | Add "and D-2214 (no interview)" to P1-m2-e, for the "after the fix" column |

## Must fix

1. Finding 1: update the decided items in `module.md` before the Gate 3 doc. If you do not, Dan sees 3 decisions he has already made, and an instructor note that is no longer true.

## Consider

1. Findings 2, 3, 4, 6 and 8: small text fixes in `module.md`.
2. Finding 5: a decision for Dan on how strong the lab 2 hint may be.
3. Finding 7: add the rerun to slide 2.10, or accept it.
4. Finding 9: complete the card test row.

No blockers. No case or kit numbers disagree.
