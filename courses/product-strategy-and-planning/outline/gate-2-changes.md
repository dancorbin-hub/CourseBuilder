# Gate 2 changes applied: spec v0.3

By the course planner, 2026-11-26. Source: `outline/gate-2-decisions.md` (rows 1 to 13). Files changed: `spec.yaml`, `outline/development-brief.md`. New file: `outline/proof-kit-drafts.md`. Not touched: `case/`, `research/`, `syllabus.md`, `gate-2-packet.md`, `capability-mapping.md`, `status.yaml`.

## Changes by decision

| Decision | What changed | File and section |
| --- | --- | --- |
| Year shift (Q6) | One pass by script (one regex, one dict). DL, RL, Q and R ids, release dates, `m2-requests-batch-1`, "2028 H1", "Larkspan 2028 strategy overview", CR-07 date 2027-11-18. 9 hits in spec, 0 in brief. Real-world dates (source dates, vendor dates) not changed. Grep after: no old id, no old file name. Numbers rechecked against `case/expected-results.md` (200%, 150%, 190%, 105%, 50,000 and 18,000 sets, 52.30 to 59.10, 1,881,200 to 1,758,800, 16 files, counts 4/8/11/14/16) | spec `gate_2_designs.ps_10.sample_flag_report`, `fallback_case`, m2 inputs |
| Request batch wording | "week 47/48", "this week's requests", "weekly" became "request batch 1/2" in module 2. Old DD-09 option B (weekly) removed with the options | spec m2, `fallback_case`; brief module 2 |
| 1 | Option A kept. Options table removed. Rule text now says "PM and release plan owner" (the Delivery lead in the Larkspan case) | spec `gate_2_designs.ps_10.handoff_rule`, m4, rung 3 |
| 2 | Option B. Confidential terms list moved to lab 4. Lab 1 data line and the minimum term count removed. Lab 4 talk track: second check, not the control, misses paraphrases. Take-home Production readiness checklist (7 items, what to test, who signs off). 3-question data check card kept | spec `data_safety_note`, `gate_2_designs.decision_e`, m1 and m4 data safety, course close, glossary, `monday_value`; brief module 4 |
| 3 | Title and planning line kept. Question for Pragmatic kept as OI-02 | spec `course.title_note`, `open_items` |
| 4 | Half-day minutes 65, 60, 50 were already in v0.2. Notes now cite the decision. Script check: full day 450 total, 360 teaching, 90 breaks. Each half day 210 total, 195 teaching. Module arcs sum to module minutes | spec `agenda`, m3 to m5 half_day notes |
| 5 | Module 3 error in plain words (minimum yearly order, plan buys less). Fix rule, debrief check and check sample reworded. Glossary "minimum yearly order". `plain_words` and `card_test_item` (a non-hardware PM understands it) | spec m3; glossary; brief module 3 |
| 6 | No grouping. Removed from m4 `agent_never` and ps_10 step 4. Talk track lines added (product backlog on merit and impact; epics and user stories; themes help, not required). Glossary: epic, user story, product backlog | spec m4, ps_10, glossary; brief module 4 |
| 7 | Module 1 aha is decided. Module 5 is the echo | spec `course.aha_moment`; brief |
| 8 | Module 2 rung 1 plus decided. Ladder 1, 1 plus, 2, 3, 3 plus | spec `autonomy_ladder` |
| Cadence and evidence order | PM sets every cadence. Intake frequent, agent logs and flags. Problem backlog at the PM's cadence, often quarterly. Agent may order by evidence (`evidence_order`, never priority). Talk track: one input, other factors, E1 "54% vs 36%". No "never reorders" wording found. Module 5 monthly run changes no priority. m3 "refresh" reworded to "rerun" or "update"; m4 "quarterly refresh at the PM's cadence" | spec core_rule, ladder, m2, m3, m4, m5, glossary |
| Bond story | Trendslop (E3). Moved to `decided`. No HBR figures until a licensed copy is read | spec `decided`, course open |
| Q1 to Q7 | Agent name final. Mapping, intent, module 4 box confirmed. Decision c option 1. sp-wf-13 stays in module 1 | spec status fields, `gate_2_decisions_applied` |
| Open items | open_items cut to what is open. Answered items moved to `gate_2_decisions_applied`. `decisions_for_dan` keeps DD-10 (proof kit) and DD-11 (names) | spec end |
| Proof kit | Three proof briefs, five job cards, a core brief and a Copilot test checklist. Counts by script | `outline/proof-kit-drafts.md` |
| Late 9 | "No magic number" removed from learner text and themes. Rule kept: PM sets the rules in the brief. Lead: AI gathers evidence and filters first, PM decides | spec themes, close, voice; brief |
| Late 10 | Worked example (PB-02 ranks first on evidence, may be deferred for build time and dependencies) | spec m2 `weigh_other_factors_example`; brief |
| Late 11 | Google Sheet option on every platform. Core path: download .xlsx or CSV, upload in chat. Drive connector stretch only with a dated vendor doc. No live-write claim | spec `google_sheet_option`, platform cards, readiness checklist |
| Late 12 | "Know before you design" in the pre-class email and repeated in the course open | spec `readiness_checklist`, `data_access_limits`, `course_open` |
| Late 13 | One optional connector lane per lab, outside the 6 steps and the pass condition. No connector named | spec `module_arc.connector_lane_rule`, each lab `connector_lane` |

## Not applied, or needs follow-up

| Item | Reason |
| --- | --- |
| Research file fixes (decision 14) | I do not edit `research/`. OI-04 stays "approved, not applied". Fingerprints need the session |
| `status.yaml` bond story record | Not in my task. OI-16 |
| `case/m3-evidence-q4.md` title "Q4 refresh" and `expected-results.md` "roadmap refresh and change" | I do not edit `case/`. Spec uses "Q4 evidence" and "update". OI-17 |
| RL ids missing from the year shift map | The map lists DL, Q and R ids only. The case already uses RL-2027-xx. I applied the same shift to RL in the spec (RL-2026-05 to RL-2027-05). Add RL to the map |
| Case says "PM and Delivery lead" (`expected-results.md`) | Decision 1 says "release plan owner". The spec says owner, with Delivery lead as the case role. Case wording can stay |
| Knowledge text sizes | `strategy-okrs-kpis.txt` 3,639 and `business-case.txt` 3,214 characters. Both exceed the 2,800 budget for the no-license path. Case builder shortens, or Dan raises the budget |
| Market Research case year | Still 2026. Needs its own shift (OI-15). Ostrelane name not searched (OI-14) |
| Syllabus, packet, capability mapping | Done in v0.4. The syllabus has no "no magic number" text. The old note was stale |

## Conflicts between decisions

1. Decision 2 moves the terms list to lab 4. Lab 4 is the tightest numeric lab. The list adds about 2 minutes and uses the 2 minutes of slack. The card test must check it.
2. The core rule says the agent never ranks. Dan's evidence order allows one order (amount of market evidence). The spec names this exception and bans the word "priority".
3. Decision 11 (late): Gemini live write to a Sheet (Gate 1 decision f2) is not verified. The Gemini card now also tells learners to upload or paste.

## v0.4 changes (critic report v2, late items 14 to 16)

By the course planner, 2026-11-26. Files changed: `spec.yaml` (v0.4), `development-brief.md`, `syllabus.md`, `gate-2-packet.md` (v3). `capability-mapping.md` needed no change. Not touched: `case/`, `research/`.

| Item | What changed |
| --- | --- |
| B1 | Copilot cards in labs 1, 3 and 5 now say "Google Sheet option, download .xlsx, upload in chat" |
| N1 | Sample flag report: Cloud team 95% before CR-07 and 105% with it. Wording "Larkspan Cloud interface change". RP-02 and RP-03 named |
| N3 | Lab 5 audit step and objective m5-o3: audit the outcome the business case names, and one other. Syllabus follows |
| N4 | PB-02 example: the case PM says yes (REQ-112 becomes CR-07). "Another PM could defer it". Spec, syllabus, packet |
| N5 | Stale note above fixed. Phrase "no magic number" stays only in internal research and input files. It is not in learner text |
| N6 | Case year label is Gate 2 Q6, not decision 9. Ostrelane name check stays open (OI-14, packet O12) |
| Late 14 | Connector lane only in labs 3 to 5. Removed from modules 1 and 2 in spec, brief, syllabus, packet. Packet O9 closed |
| Late 15 and 16 | Funding scenario stretch stays in module 1. Packet O1 closed. OI-03 not needed |

## Case changes needed (case builder)

| File | Change |
| --- | --- |
| `case/m4-check-sample.md` (N2) | CR-08 cites REQ-116 and says "From Support lead". REQ-116 is a customer ticket from the Operations manager (A-3306), and the PM decision is "later". Change the source to a request the PM approved with yes, or change the sender and the source note. Update the lab 4 check sample lines in `expected-results.md` to match |
| `case/expected-results.md` (N6) | State the gap sign for OS-3: lower is better, so a negative gap means worse than target |
