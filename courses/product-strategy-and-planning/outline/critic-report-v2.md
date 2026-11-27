# Critic report v2: Advanced AI for Product Strategy and Planning

Scope: spec.yaml v0.3, case/, outline/syllabus.md, outline/capability-mapping.md. Checked against CLAUDE.md, Gate 1 decisions, Gate 2 decisions (1 to 13), registry.

## Checks

| Focus check | Result | Note |
| --- | --- | --- |
| Old ids, old supplier name Corvane | Pass | Corvane appears only in year-shift-map.md and name-check history (spec.yaml line 1440, gate files). Case, syllabus and mapping use Ostrelane. No R-2027, DL-2025 or Q-2026 strings. The "Q4 2025" hits are real survey dates. |
| "no magic number" in learner text | Pass | Syllabus, spec cards and slide text are clean. The spec lists it as a banned phrase. See N5. |
| Connector lane outside the 6 steps | Pass | Each lab has exactly 6 card steps. The lane is a separate card after the data check card. |
| Google Sheet option on all platforms | Concern | See B1. |
| Evidence order, never "priority" | Pass | Spec, syllabus, README and CSV column all say "evidence order, not a priority". |
| No audience drafting | Pass | Spec, mapping and brief agree. One talk track line only. |
| Planted-error fade | Pass | Told, hint, hint, hint, none in spec, syllabus and planted-errors.md. |
| Timing, full day | Pass | 450 minutes total. 25+70+60+70+65+55+15 = 360 teaching. Breaks and lunch 90. Clock times add up. Each module splits 40/60. |
| Timing, half days | Pass | 195 + 195 = 390. The split is after module 2. Each day ends at 12:30. Module arcs add to 80, 75, 65, 60 and 50. |
| Case texts vs check samples and expected-results | Pass | Recomputed. Sums, ranks, gross profit (1,881,200; 1,758,800; 1,718,336; 1,595,936), day counts, gaps, FTE and ordering all match. Shortened .md and .txt copies match. Knowledge file counts are 4, 8, 11, 14 and 16. |
| Gate 2 decisions 1 to 13 | Pass | All are reflected. See B1 for decision 11. |
| Syllabus and mapping agree with spec | Pass | Minutes, objectives, evidence, boxes and skills agree. |

## Must fix (blocking: 1)

- B1. Copilot platform cards in labs 1, 3 and 5 (spec.yaml near lines 413, 660 and 920) omit the Google Sheet option. Decision 11 and the spec rule at line 119 say every platform. The syllabus Copilot row already has it. Add "Google Sheet option, download .xlsx, upload in chat" to the three Copilot cards.

## Consider (non-blocking: 6)

- N1. The spec sample flag report (about line 1189) says the Cloud team is at 95% in Q1. With CR-07 it is 105%, and RP-02 and RP-03 use the team (expected-results.md). It also says "Cloud API change". CR-07 says "Larkspan Cloud interface change".
- N2. m4-check-sample.md: CR-08 cites REQ-116 as the source and says "From Support lead". REQ-116 is a customer request, and the case PM's decision on it is "later" (problem not validated). Change the source or the sender.
- N3. Lab 5 has no hint and the audit step says "2 on track measures". Three measures can read on track (OS-1 wrongly, OS-2, OS-3). A learner can audit OS-2 and OS-3 and miss the error. Add a selection rule to the card, such as "the measure named in the business case".
- N4. The syllabus module 2 example defers PB-02 for build time. The case PM's decision on REQ-112 (PB-02) is "yes" and it becomes CR-07. Use a different problem or say "another PM could".
- N5. The phrase "no magic number" is still in research/methods.md line 102, research-brief.md, stage-1-inputs.md, outline/revision-notes.md and stage-2-inputs.md. Do not copy it into cards. outline/gate-2-changes.md line 41 says the syllabus still has it. That note is stale.
- N6. Two smaller items.
  - Spec lines 1090 and 1374 call the case year "Gate 2 decision 9". In Dan's list, 9 is "no magic number". The case year is Q6.
  - Ostrelane has no name check yet (year-shift-map.md). Dan's decision is open.
  - expected-results.md does not state the gap sign for OS-3 (lower is better).
