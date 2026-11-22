# Critic report: Advanced AI for Market Research (recheck after rework 2)

- The v0.1 report is in git history (commit e63bdbd).
- Checked on 2026-11-22. Outputs only: `spec.yaml` (v0.3), `outline/development-brief.md`, `outline/syllabus.md`, `outline/capability-mapping.md`, `case/` (all files).
- Checked against: CLAUDE.md, PRD, `outline/rework-brief-2.md`, `outline/gate-2-decisions.md`, `research/gate-1-decisions.md`, `worked-example-row.yaml` (v3), `shared/registry/`, and the Capability Standards Workbook 2027 extract.
- I recounted every interview, deal, feedback item, survey row and applicant by hand. All counts match the records except one (M3).

## Checks

| # | Check | Result | Line that fails |
| --- | --- | --- | --- |
| 1 | Workflow and bottleneck per module | Pass | None |
| 2 | Lab extends the one course agent | Pass | None |
| 3 | 2 to 4 objectives, observable verbs, practiced | Pass | None |
| 4 | Timing | Pass, 1 concern | All sums are correct (see table below). Lab 5 has no time for Q4 (M2) |
| 5 | Ladder and error fade | Pass | Told, hint, hint, hint, none. Success checks are general |
| 6 | Development brief | Pass, 1 concern | 5 questions answered. Develop and Apply. Evidence per lab. Skill names exact. Module 4 box claim is wrong (S4) |
| 7 | Gate 1 and Gate 2 decisions | Pass, 1 concern | Decisions 6, 8, 9, 10, 12 applied. Decision 4 still "waiting for Dan yes" (N7). v3 row still has a bar (S9) |
| 8 | Registry | Concern | Urgency, pervasiveness and willingness to pay are now core in every lab. PDW-AI teaches them (S8) |
| 9 | Case data | Concern | One company. Errors are in the data. Spec and case disagree on module 3 hand-off rules (M1). One count is wrong (M3) |
| 10 | Monday value | Pass | None |
| 11 | Platform | Pass, 2 notes | m1 code book is over the fallback budget (N1). Evidence pack size is out of date (N2) |
| 12 | One core message per lab | Pass | None |

## Caller focus points

| Point | Result |
| --- | --- |
| 1. Spec and case agree | Mostly. Backlog model, fact labels, file names, Q numbering (Q1, Q2, Q3, Q5 run; Q4 check) and upload counts (6, 5, 5, 4, 3; 12 knowledge files) agree. Disagree: module 3 hand-off numbers (M1), module 2 one-segment driver rule (S2), module 5 age rule wording (S3), lab 1 fix text (S1) |
| 2. No fixed evidence threshold | Pass. No "bar", "meets", "emerging" or truth threshold in spec, syllabus or case. Agent never writes "pattern" or "validated". Numbers left: 18-month age limit (hand-off rule, case PM's choice), PA-04 minimum of 10 decided deals (program rule, OI-22). One case sentence reads as a rule (N6) |
| 3. Counts | All match except "3 other interviews" (M3) |
| 4. Timing | Pass. Full day: 320 + 40 = 360 teaching, + 90 = 450. 148 instructor-led (41%). Half days: 210 each, 195 teaching each, 390 total, 161 instructor-led (41%). Agenda clock times add up. Every module is 40/60 in both formats |
| 5. Capability names and ids | Names and ids are exact. No invented skill. Two mapping errors (S4, S5) |
| 6. Lab 5 timing with 5 questions | Concern (M2) |
| 7. Syllabus internal notes | Pass. No decision numbers, OI ids, Dan, Gate or rework notes. "(proposed)" on the Capability Standards row is a status (N8) |

## Must fix

1. **M1. Module 3 hand-off rules: spec and case disagree.** Spec m3 `handoff_rules` says "The PM writes how many accounts in the brief (case PM's choice; see case/company.md)" for no-fit repeats and for account changes. `debrief_check` says "No problem gets a false change flag under the case PM's change rule (case: P02)". `fallback_case.learner_files` says company.md shows a "feedback change rule" and a "no-fit repeat rule". The development brief module 3 row says the same. But `company.md` rule 4 has no number: "Report the change in accounts for every tag. Send every 'no fit' group to the flag report". `expected-results.md` flags F-1232 (1 account), which a repeat rule would not flag. Fix (planner): make the spec match the case. Report every change and flag every no-fit group. Drop the two numbers. This also fits "no threshold" better.
2. **M2. Lab 5 has no time for Q4, and 4 run questions fill the lab.** Q4 is the check question and the decision 3 test (I-105). No card step and no arc minutes run it. The m5 debrief (9 minutes, 8 in half days) also holds the reveal, the brief fix, the segment rule and the Monday close. The lab (30 minutes, 28 in half days) now has 4 answers to decide (Q5 added), citation audit and 3 segment decisions. My estimate is 27 to 29 minutes with no slack, before Copilot fallback learners paste 4 files. Fix (planner): add "Run Q4 and compare" to the m5 debrief with its minutes. Give a minute budget per card step. If it does not fit, make Q3 optional on the case path (Q5 must stay, decision 9).
3. **M3. One count is wrong.** `expected-results.md`, lab 1, "Why P05 should not be near the top", point 5: "Inside Food service, 3 other interviews do not raise P05." Batch 1 Food service has I-103, I-104 and I-105, so there are 2 other interviews. `planted-errors.md` correctly says "The other 2 Food service interviews". Fix (case builder): change 3 to 2.

## Should fix

1. **S1. Lab 1 fix text differs.** Spec: the learner adds one *ranking rule* ("Rank by interviews, accounts and segments. Quote count is not evidence of pervasiveness"). `planted-errors.md` fix repeats template rules ("Count interviews, not quotes", "Propose a ranking") and adds a *flag* rule ("If all quotes for a problem come from 1 interview, send it to the flag report"). `expected-results.md` batch 1 flag 3 and check sample pass condition 4 depend on that flag rule. Fix: use the spec's ranking rule as the example fix. Keep the flag rule as an optional second rule.
2. **S2. Module 2 one-segment rule is not in the case.** Spec m2 hand-off rule: "A driver that rests on deals from one segment only". `company.md` rule 3 and the lab 2 expected flag report do not have it. Every lost driver in the case is 1 deal in 1 segment, so this rule flags all 6. Fix: drop it from the spec (rule 3 counts by segment already), or add the expected flags to the case.
3. **S3. Module 5 age rule wording.** Spec: "The only evidence is older than the age limit". `company.md`: "Send any source older than 18 months". Q2 and Q4 expected flags list R-2024-07 even though newer evidence exists. Fix: spec says "any source older than the age limit".
4. **S4. Module 4 box mapping is wrong in `capability-mapping.md`.** Workbook box 05 Competitive Landscape: primary 2.2 Opportunity Prioritization; secondary 1.2 Market Segmentation and 4.2 Buyer Understanding and Persona Development. 1.3 is not mapped to this box. Gap 1 says "No Market Intelligence skill anchors it", but 1.2 is a capability 1 skill on this box. Fix: correct gap 1. Tell Dan that 1.3 is not a box 05 skill, and let him choose 1.3 (competency 1.3A, win/loss) or 1.2.
5. **S5. Module 5 has no 8.4 competency.** `capability-mapping.md` module map puts "8.4" (a skill id) in the competency column. Spec m5 lists skill 8.4 but only competencies 1.1C and 1.1D. Fix: name one, for example 8.4B Clear and Actionable Recommendation Framing (send, change or hold), or drop 8.4 from module 5.
6. **S6. Old term in `capability-mapping.md`.** Module map row 1 is "1. Insight log". Rework brief 2 item 1 says rename everywhere. Fix: "1. Problem backlog".
7. **S7. "Dan's test" in instructor text.** Spec m1 debrief arc, development brief module 1 and `expected-results.md` say "Dan's test". Gate 1 says Pragmatic teaches it. Decisions 43 and 45: another instructor delivers it. Fix: "the Pragmatic test: can you predict that the next buyer of this persona will raise it?"
8. **S8. Registry overlap with PDW-AI.** PDW-AI teaches urgency, pervasiveness and willingness to pay, and a planted outlier. The evidence profile now uses these terms in every lab, but the m1 `registry_guard` does not say "refer as known". The m3 stretch still says "Add urgency, pervasiveness and willingness to pay clues to the evidence profile", which the core already has. Fix: add the three tests to the m1 registry guard (known from PDW-AI; new slides only on how the agent reports them). Reframe the m3 stretch as "add the survey wave as a source for the evidence profile".
9. **S9. Approved row v3 still has a bar.** `worked-example-row.yaml` v3 lines 43 and 79 say "below the PM's bar" and "emerging". The spec says it follows v3. OI-06 covers only `workflows.yaml`. Fix: add an open item for Dan's yes to update v3 when decision 4 is final.
10. **S10. Check samples have no slot.** Labs 1 to 4 count a check file in chat, and each has a pass condition. No card step and no arc minutes run it. Fix: say where each check sample runs (debrief, homework or demo).
11. **S11. Wrong heading in `expected-results.md`.** Lab 1 batch 2 "Success check (spec)" holds the error-specific condition (P05 rank). The spec moved that to `debrief_check`. Fix: rename to "Debrief check (spec)".

## Notes

1. **N1.** `m1-code-book.md` is 2,906 characters. The spec fallback budget is 2,800 per knowledge file and 7,800 in total. G2-PF-05 will measure it.
2. **N2.** `m4-evidence-pack.md` is now 15,366 characters. The spec `gate_2_risk` still says about 12,400. Update the figure for G2-PF-03.
3. **N3.** Spec `knowledge_file_budget`: "12 (5 job cards, 5 case knowledge files, 2 logs, the problem backlog and the driver log)" reads as 14. Write "2 logs: the problem backlog and the driver log".
4. **N4.** Lab 5 segment tables are uneven. Pharmacy and lab omits P09 (feedback A-34, A-35, no interviews). Distribution omits P05 (feedback A-33). Food service lists P10. Add them as "not ranked" or say the tables list interview problems only.
5. **N5.** Part 4 of `m4-evidence-pack.md`: P10 fact label "No interviews" is not one of the 3 fact labels. Write "0 interviews" in the profile instead.
6. **N6.** `expected-results.md` lab 5: "Feedback counts alone do not move a problem to validation" reads as a fixed rule. Frame it as the case PM's decision.
7. **N7.** Decision 4 is still "waiting for Dan yes" (OI-20). The whole v0.3 and the case depend on it.
8. **N8.** Syllabus "Capability Standards (proposed)". Correct for review. Remove "(proposed)" when Dan confirms.
9. **N9.** `capability-mapping.md` quotes the 1.3 objective in quotation marks but shortens it. Workbook: "Distinguish a single strong opinion (n=1) from a pattern across multiple sources (N=many)". Quote it exactly.
10. **N10.** Q5 (FDP PM) adds no data and changes no planted error or lab 1 to 4 count. Its expected answer matches the records (P03: 3 interviews, 2 accounts, Food service only; feedback A-04, A-30; D-2203). Pass.
