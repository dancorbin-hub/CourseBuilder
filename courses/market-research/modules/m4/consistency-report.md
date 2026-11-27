# Consistency report: module 4

Consistency reviewer, 2026-11-27. Inputs: `modules/m4/module.md`, `modules/m4/kit/` (lab-4, kit-m5), `card-test.md`, `example-oi-05.md`, `spec.yaml` (module 4 and course rules), `case/`, `modules/m3/kit/kit-m4/`, `modules/m5/kit/kit-m5-expected.md`, `modules/m5/kit/kit-m5-draft/`, `modules/m5/kit/kit-final/`, modules 1, 2, 3 and 5, `shared/registry/registry.yaml`, `research/stretch-verification-2026-11.md`, CLAUDE.md house rules.

Result: 0 blockers, 2 major, 7 minor. The lab, the case data, the planted error and the kit agree. The open items are spec changes that wait for Dan, the module 5 side of the hand-over, and small wording fixes.

## Checks

| # | Check | Result | Evidence |
| --- | --- | --- | --- |
| 1 | Spec match | Pass, with 4 deviations listed for Dan (F1) | Title, workflow, category, Capability Standards, rung 3, 55 minutes, 22 / 33, arc 7 / 8 / 7 / 25 / 8, goal, core message, PM decision, 6 card steps, quality checks, success check, warning "hint" and learner evidence match the spec. Learner evidence adds flag decisions (additive) |
| 2 | Case match | Pass | Every id in slides, demo, cards and debrief is in `m4-evidence-pack.md` or `m4-check-sample.md`: D-3101 to D-3110, WL-3101 to WL-3110, D-2205, D-2209, D-4101 to D-4105. Quotes are word for word (see F9). Counts match `expected-results.md` lab 4: Rimecore 2 / 2, Vantafrost 1 / 1, controller alarms 1 / 0, do nothing 2 / 4, CRM only 3 / 1. Before the fix: Rimecore 2 / 3 "growing", do nothing 3. Split at "## Part 3" measured: 6,590 and 8,760 |
| 3 | Planted error | Pass, with a minor risk (F5) | D-3108 is blank in Part 1, "Rimecore" in Part 2, do nothing in WL-3108. D-3102 decoy is in the data. Warning: only "Audit before you approve." (4.10). No audit hint on slides, cards or record sheet. The success check does not name the error. 4.14 reveals it and names the link check (passes) and the interview audit (finds it). The card pass condition names D-4102 and D-4104 with no reason text |
| 4 | Demo to lab | Pass | Claude demo uses `kit/lab-4/` files, `m4-evidence-pack.md` and "Run the alternatives map job", same as the cards. Demo rule is neutral (B16) |
| 5 | Cards | Pass, with minor items (F4, F6) | Same 6 core steps on 4 cards, 1 action each. Opening line, save note, check date (2026-11-26 or 27), data safety, "Start here with sample data", pass condition with second sample. Only the spec standard data safety sentence is over 20 words (22). Second-agent stretch on Claude and ChatGPT only, headed "not yet tested". Copilot and Gemini have the exact `stretch_scope` line. Agrees with `stretch-verification-2026-11.md` section 4 |
| 6 | Kit | Pass | All card files are in `kit/lab-4/`. Every `.md` knowledge file has a byte-identical `.txt` (`cmp`). `lab-4/alternatives-map.md` equals `case/m4-alternatives-map.md`. Counts measured with `wc -m` match section 8. Lab 4 Copilot fallback 7,419 (holds brief v4, job card and map verbatim). kit-m5 fallback 5,388. Brief v5 3,491, job card 1,497 |
| 7 | Timing | Pass | 7 + 8 + 7 + 25 + 8 = 55. 40% / 60%. 4.12 is 25 minutes in slide, notes and LD spec. 4.13 is 3 minutes. Agenda in course open: "Module 4. Break. Module 5" matches the 4.17 transition |
| 8 | Notes | Pass, with F3 | 17 slides, 17 `POINT:` and 17 `Talk Track:`. No `[AI USE CASE TT]`. OI-05 is told as Pragmatic's story, client not named, no dates, values, product names or people. Notes are complete for another instructor |
| 9 | Registry | Pass | Not CAW-AI or the Competitive Intel Watchdog. No public sources, no scheduled task, no setup slide. 4.4 (types) and 4.7 (rung 3) have no match in modules 1 to 3 or the registry |
| 10 | Words | Pass | No em or en dashes. No "exception" or "escalation". "Pattern" and "validated" only in the "never write" rules |
| 11 | Carry forward | Start: pass. End: pass for kit-m5, open for module 5 (F2) | Start: the cards assume brief v4 and 8 files, which is `modules/m3/kit/kit-m4/`. End: kit-m5 holds all 14 contract files. 7 knowledge files are identical to kit-m4. Brief v5, driver log and map are identical to `kit-m5-draft/`. Brief v5 = brief v4 plus rule 4, the `planted-errors.md` text word for word |

## Findings

### Must fix

| # | Level | Finding | Fix |
| --- | --- | --- | --- |
| F1 | Major | Module 4 does not match its locked spec entry in 4 places until Dan says yes: the job card holds 2 of the 3 spec hand-off rules (D2); stretch item 1 (schedule) is dropped (D6); stretch item 2 is reworded to a manual hand-off (D5); the check sample comes from a tuned project, not "the demo run" (D9). The module lists all 4 as changes 1 to 4 | Get Dan's yes on D2, D5, D6 and D9 at Gate 3. Apply changes 1 to 4 to `spec.yaml` before module 4 is approved. If any is no, revert that part of the module |
| F2 | Major | The hand-over to module 5 is only half done. (a) `m5/kit/kit-final/job-card-alternatives-map.md` is still the Gate 2 proof placeholder ("The PM adds one hand-off rule here"), so it differs from the kit-m5 card. (b) `kit-m5-expected.md` row 14 says the fallback holds "Brief v5, map job card, map". The delivered file has no map (D7). (c) `m5/module.md` still says "Module 4 is not built" (lines 5, 22) and tells the demo and card test to use `kit-m5-draft/` with `proof/job-card-alternatives-map.md` (lines 519, 738, 755 to 756). Change 6 names only section 8 | Widen change 6: replace the kit-final job card and its `.txt` with the kit-m5 card, update the kit-final README count, edit contract row 14 to "Brief v5 and map job card. Map in chat (module 4 D7)", and point `m5/module.md` lines 5, 22, 28, 519, 738 and 755 to 756 to `modules/m4/kit/kit-m5/`. Module 5 owner applies it after Dan's yes |

### Consider

| # | Level | Finding | Fix |
| --- | --- | --- | --- |
| F3 | Minor | Slide 4.3 headline "We built it ourselves." is in quote marks, so it reads as the client's words. `example-oi-05.md` has no such quote | Show it as a label with no quote marks, or ask Dan to confirm the words |
| F4 | Minor | Slide 4.9 footer is "Full steps: your step card in the workbook." Modules 2, 3 and 5 say "...in the workbook (Pragmatic Learning Hub)." | Add "(Pragmatic Learning Hub)" |
| F5 | Minor | The audit can miss the error. Step 5 picks 3 of 4 entries, so 1 learner in 4 does not audit ALT-01 (Rimecore). The record sheet audit table has 6 rows for 3 entries, but ALT-01 alone lists 3 Q3 rows plus 2 Q2 rows | Add one line to the 4.14 talk track: "If your 3 entries did not include Rimecore, your audit could not find it. That is what a random sample can miss." Give the audit table 9 rows |
| F6 | Minor | Stretch (Claude, ChatGPT): the second project gets no `problem-backlog`, so job card output 4 ("the backlog problem behind each reason") cannot be met. The win/loss run in project 1 will also recount the match rate table (win/loss job step 4), which section 9 calls wrong for lab 4. Stretch step 1 holds 2 actions | Add `problem-backlog` to stretch step 3, or say output 4 has no backlog links. Add: "Do not save project 1's driver log back. It has a recount." Split step 1 or accept, as the stretch is outside the 6-step core |
| F7 | Minor | The 4.12 room prompt "Where did the map's answer come from?" points at the source of the alternative. The module 2 and 3 prompts are more neutral | Use "Which evidence rows did you open? What do they say?" |
| F8 | Minor | Fixed rule 4 says "If the CRM field and the buyer differ, send the deal to the flag report." D-3103, D-3106, D-3107 and D-4103 have CRM competitor "None" and a do nothing buyer. A strict agent may flag them. Expected results list only D-3108 and D-4102 | Add a section 9 row: flags on CRM "None" deals with a do nothing buyer are fine, not a failure. Pass item 2 is still met |
| F9 | Minor | Section 9 note 2 quotes WL-3102 as ("We went with Vantafrost."). In the case that sentence is outside the quote marks, so it is not word for word | Write: WL-3102 says they went with Vantafrost |

## Not a finding (checked)

- Copilot fallback sums: 463 + 3,253 + 1,497 + 2,192 + 14 = 7,419. Measured headers include line breaks, so the parts differ by 1 to 2 characters from the stated split. Totals match `wc -m`.
- `kit-m5/alternatives-map.md` (3,286) is over the 2,800 per-file fallback budget. The contract allows it, and it is not in any fallback Instructions.
- Three lab brief slides (4.9 to 4.11) differ from the two-slide pattern in modules 2 and 3. D12 asks Dan.
- "Is Rimecore growing?" on 4.2 is the case question in `case/company.md` (question 4). It is not a module hint.
