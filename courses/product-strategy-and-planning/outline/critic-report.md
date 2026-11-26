# Critic report: Stage 2, Product Strategy and Planning (spec v0.1)

Checked: spec.yaml, outline/development-brief.md, case/, research/gate-1-decisions.md, registry, workbook. Not read: stage-2-inputs.md, planner notes.

## Checks

| # | Check | Result | Note |
| --- | --- | --- | --- |
| 1 | One workflow and bottleneck per module | Pass | Rows 09, 12, 05, 07 (with 08), 10. Bottlenecks name their sources |
| 2 | Lab extends the one agent | Pass | One agent, one job per module, kit per module |
| 3 | 2 to 4 objectives, practiced | Concern | m4-o2 and m4-o3 point to steps that do not practice them (Must fix 5) |
| 4 | Timing | Pass | Script: 70+60+70+65+55+25+15 = 360. Day 1 195, day 2 195. Per module arcs add up. 40 percent per module. 148 of 360 overall (41 percent). Clock times add to 450 and 2 x 210 |
| 5 | Ladder and fade | Concern | Ladder climbs. Fade is told, hint, hint, hint, none. Module 4 template removes the error (Must fix 1). Card text leaks the error in modules 2 and 5 (Consider) |
| 6 | Development brief | Pass | 5 questions at course and module level. Develop and Apply. Evidence per lab. No invented standards |
| 7 | Gate 1 decisions | Pass | a to k, PS-05, 06, 09, 10 (deferred to Gate 2), f1 to f6 all reflected |
| 8 | Registry | Pass | No CAW-AI agent, no persona, no synthesis basics, no Strategy Matrix lab, canon referred to. Schedule is stretch with new slides |
| 9 | Case data | Concern | One company (Larkspan, Gate 1 j). Numbers pass. Errors 1, 2, 3, 5 are in the data. Error 4 is defused by the template (Must fix 1) |
| 10 | Monday value | Pass | Agent plus job builds plus templates. Roadmap job is missing from the build list (Consider) |
| 11 | Platform | Pass | No-connector core path on all four. Decision f risks handled. Patterns P1 to P3 named with tests. Gate 2 proof items G2-PF-01 to 06 |
| 12 | One core message per lab | Concern | Module 4 has two (Consider) |

## Extra checks

| Item | Result | Note |
| --- | --- | --- |
| (a) AI never sets, proposes, ranks or rewrites strategy | Concern | Module 2 check "serves strategy" conflicts with agent_never (Must fix 2). Module 3 "ranks assumptions" wording (Consider) |
| (b) No scoring, weights or Focus callbacks | Pass | Grep of spec and case: none. Strategy Matrix has one mention in strategy-okrs-kpis.md |
| (c) Timing by script | Pass | 360 full day. 195 and 195 half days. Half-day module minutes 80, 75, 65, 60, 50 (DD-05) |
| (d) Expected results recomputed | Pass | 30+ numbers by script, all match. Samples: team totals 200, 150, 95, 100, 130 percent and FTE 24, 18, 7.8. Ask totals 4,550 and 4,750. Gross profit 1,881,200, 1,758,800, 1,718,336, 1,595,936, low and high 1,391,360 and 2,312,272. Margin 36.9 of 96. Evidence days 245. Validated problems 10 of 14 from the evidence log. RM-14 1 account and 1 source type. OS-1 gaps -25.5 and -31.5. Shipped minus active 590 and 910. Trials +56.1 percent. Quote check numbers 12,000 and 46,200 |
| (e) Planted errors in the data | Pass with Must fix 1 | All five exist in the records. Lab 4 template defeats its own error |
| (f) 18 files vs 16 limit | Fail | Must fix 3 |
| (g) Validated problem backlog in module 4 | Concern | File exists as a run file. The spec describes it wrongly (Must fix 4) |
| (h) No em or en dashes | Pass | Python scan of spec, brief, all case files (md, txt, csv, xlsx) and research files: 0 |
| (i) gate_2_designs concrete | Pass | PS-10: inputs, 12 agent steps, 3 rule texts, sample flag report, timing. Decision e: 3 options, minute by minute lab 1. Fix the two small errors in Consider |
| (j) Capability names | Pass | All competency and skill names match the workbook (read only). 2.1B, 2.4D split cells joined as the spec says. Box notes match Framework Reference |

## Must fix

1. **Module 4 template already holds the fix for the planted error.** Spec lines: quality_checks "Each item shows its own evidence and its date"; handoff_rules "An item ... whose own evidence is below the PM's 'validated' rule"; ps_10 steps 3 and 5. The error fix is "Judge each item by its own evidence, not its theme's." With these in the template, the agent flags RM-14 on run 1 and the audit finds nothing. Remove own evidence from the template checks and rules. Keep "traces to a theme, a validated problem and an objective". Show evidence per trace only after the PM adds the rule.
2. **Module 2 quality check contradicts the core rule.** Line "Each 'serves strategy' line quotes the strategy or OKR text it relies on" asserts fit, while agent_never says it never judges strategic fit. The glossary has the same wording ("the strategy text it serves"). Change to "Strategy or OKR text that may relate to this request, quoted, or 'none found'. No fit statement."
3. **Knowledge files: spec lists 18, budget says 16.** Spec growth.files_after count: 5, 9, 13, 16, 18. Two causes: it lists strategy-overview and okrs-kpis as two files (case has one, strategy-okrs-kpis), and it lists source-pack as knowledge in m3 (case README: run file). Align spec growth, kit-m3 and fallback_case to case/README.md (16 files). Check: ChatGPT Plus and Copilot limit is 20, so 18 would also fit, but the stated budget and G2-PF-06 say 16.
4. **Module 4 inputs are wrong.** fallback_case says the validated problem backlog is "in the agent from module 2". Module 2 holds problem-backlog.csv. The validated backlog is a module 4 run file. Also evidence-log.csv is a module 4 run file (README) but is not in the card steps or inputs, and the audit of "own evidence" needs it. Card step 2 sends the roadmap, which is already in the agent from module 2. Fix: step 2 sends the validated problem backlog and the evidence log. Add evidence-log to inputs and kit-m4 run list.
5. **Module 4 objectives are not practiced where they say.** m4-o3 (write the release plan hand-off rule) says "lab step 1 and step 4". Step 4 is "Send change request CR-07". m4-o2 and the learner evidence "tuned brief with the own-evidence rule" need a step where the learner adds the rule. No card step does it. The fix happens only in "Rerun the refresh with the fixed brief" in the debrief. Add the brief edit as a card step (merge steps 5 and 6, or move the rerun into the lab) and point m4-o3 to the step where the learner writes or reviews the rule.

## Consider

- Module 5, card step 5 "Audit 2 'on track' measures against the business case outcome" and step 2 (the learner writes the outcome-or-output rule before the run) tell the learner where the error is. Fade level is none. Use "Audit 2 'on track' measures" and move the rule write after the first run, or leave the rule as an output of the audit.
- Module 2 card step 3 "open every merge" and the success check "every merge cites a log id" point at the error. A hint level is "Audit before you approve." Use "Audit 3 cards and 2 cited log entries."
- Module 3 agent_never "ranks assumptions only by their arithmetic effect" is close to the core rule "never ranks". Say "orders by the sheet's swing column".
- DD-07 (candidate clusters) is the agent grouping problems into themes. Dan said the agent does not propose strategy. ps_10 step 4 depends on it. Dan must decide before the lab is final. Option B is safer.
- ps_10 sample flag report: DL-2026-09 is in the request decision log, not the roadmap decision log (that log has RL-2026-05). The sample says the note is "marked internal only". The case marks it "Share with the Delivery lead and the Support lead". Fix both so Dan sees the real case.
- Rung 3 says "a hand-off rule says what passes and what stops" between the request job and the roadmap job. No rule text is written (for example, only a request with a recorded PM decision passes). Add the text and an objective, or Dan cannot judge the hand-off.
- m3-o4 (gate recommendation) is practiced only in a 2 minute debrief item. 2.3F Stakeholder Argumentation is claimed for module 3, but no step practices it. Drop the competency or add a step.
- 2.2E is claimed "light form, no scoring". The workbook text says "Uses scoring outputs". The brief tells the Pragmatic reviewer. Keep the note in the packet.
- Module 4 has two core messages (own evidence; change is not a promise) and about 12 agent steps in a 30 minute lab. Pick one message for the lab brief. Watch the card test.
- Module 5 lab is 25 minutes (23 in half days) for 6 steps and two monthly runs. Tightest lab. Watch the card test.
- Case date: company.md says late November 2026. m5-metrics-nov.csv is extracted 2026-12-02. Change to 2026-11-30 or move the case date.
- Lab 1 flag report has a "data line" in the decision e design (minute 6 to 10). The template_contents do not hold it. Add it if Dan picks option B.
- monday_value.builds_taken_home omits the roadmap job.
- Dan to decide (already listed in the spec): PS-10 (A recommended), decision e (B recommended), DD-05 shorter half-day modules 3 to 5.
