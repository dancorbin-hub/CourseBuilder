# Development brief: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`. Stage 2 v0.4 by the course planner, 2026-11-26. It applies Dan's Gate 2 answers and the 2027 case year (late November 2027, plan year 2028). v0.2 followed the critic report.
- Purpose: answer the 5 questions from "How the Capability Standards Drive Learning Development" (PRD decision 40) for the course and for each module.
- The 5 questions: (1) What capability, and which skills? (2) What can the learner do? (3) How far: Introduce, Develop, Apply or Validate? (4) What evidence shows it? (5) What experience gets them there?
- Capability, skill and competency names come from the Capability Standards Workbook 2027 (project files, `reference/pragmatic-sources/`, read-only, read 2026-11-26), sheets Skill Standards, Skill Navigator and Framework Reference. Names are copied exactly. No name was missing, so no "Dan to name" is needed. Status: **confirmed by Dan, Gate 2 Q2, 2026-11-26**. Gaps go to the Pragmatic reviewer.
- Offering intent for every module: **Develop and Apply** (decision 41, confirmed by Dan, Gate 2 Q3). The workshops Introduce. Validate stays with the instructional designers (decision 29).
- Inputs: `outline/stage-2-inputs.md`, `research/gate-1-decisions.md` (wins if files differ), `research/worked-example-row.yaml` (sp-wf-09, approved), `research/workflows.yaml` (rows 03, 05, 07, 08, 10), `research/rerun-replacement-02.yaml` (row 12), `research/rerun-track-1.yaml` (row 11), `research/research-brief.md`, `research/platform-matrix.yaml`, `research/bond-stories.md`, `research/alignment-log.yaml`, `shared/registry/registry.yaml`.
- Companion files: `spec.yaml` (module plan, minutes, agenda, Gate 2 designs, decisions for Dan). The syllabus writer makes `outline/syllabus.md` later, in the structure of `outline/reference-mr-syllabus-approved.md`.

## 1. Course level

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** Capability 2, Strategic Direction: "how an organization turns market evidence into product strategy, prioritized opportunities, business cases, and roadmaps." Skills: 2.1 Strategy Alignment, 2.2 Opportunity Prioritization (AI text only, not 2.2A to 2.2D), 2.3 Business Case Development, 2.4 Product Vision and Roadmap. Supporting skill: 1.1 Market Problem Identification (module 2, light). Pragmatic Framework 2027 boxes: Focus / Product Portfolio, Market / Market Problems, Business / Business Plan, Focus / Product Roadmap, Business / Business Outcomes |
| 2. What the learner can do | Build one agent from a template. Write and tune its brief. Set every range, tolerance and threshold in the brief. Set quality checks and hand-off rules that stop the agent before any strategy, priority, funding or release plan call. Decide each flag report item. Audit a sample of output against its sources and its numbers. Connect jobs so one output feeds the next. Make and record each strategy, request, business case, roadmap and investment decision, with a reason that cites evidence |
| 3. How far | Develop and Apply. Develop: in each module the learner sees a demo, runs a lab, finds a planted error and gets feedback in the debrief, with richer input each time. Apply: learners use their own planning inputs first and make every judgment call themselves. The planted error warning fades: told in module 1, a hint in modules 2 to 4, no hint in module 5 |
| 4. Evidence | Per lab (decision 42): the tuned brief, the flag report decisions and the audit findings. Plus one PM decision record per lab: fund, pause or stop calls (module 1), yes, no or later with a reason on each flagged request (module 2), the gate recommendation and the next assumption to test (module 3), the decision log entry for a roadmap change (module 4), and the investment review note (module 5). At the end: the saved agent with five jobs and a Monday plan with an audit date |
| 5. Experience | One course agent, the Strategy Evidence Agent (name final, Dan, Gate 2 Q1), that grows in each module (house rule 12). The agent gathers, totals, traces and flags. It never sets, proposes, ranks or rewrites strategy, and it never fills a decision field. An autonomy ladder: hand-run batch, hand-run batch with a decision checkpoint, refresh with a "what changed" report, hand-off between jobs, a monthly run across jobs. 40% instructor-led and 60% hands-on per module. Own work first, one fallback case company (Larkspan Systems). Same core steps on Claude, ChatGPT, Copilot agent builder and Gemini. Breakout rooms by platform. Catch-up kit per module |

### What the workbook text confirms

Quotes are from `research/stage-1-inputs.md` and the rerun files. No new names.

| Workbook text | Course design |
| --- | --- |
| 2.1 AI text: "Strategy stays a forced-choice human decision" | Module 1 consistency check reports evidence only. A hand-off rule stops the agent before any funding, ranking or strategy change |
| 2.2 AI text: "analyze evidence, surface inconsistencies". "Weights and final priorities stay human-owned" | Module 2 decision card links each request to the problem backlog, the strategy and past decisions. The decision field stays blank for the PM |
| 2.3 AI text: "Assemble evidence, model market size, costs ... find assumptions and risks, red-team the case. Data and calculations stay auditable" | Module 3 assumption register, red team and a course sheet that holds the formulas. One link per market size number |
| 2.4 AI text: "Cluster validated problems into outcome themes ... Must not turn uncertain direction into false delivery commitments" | Module 4 trace to the validated problem backlog, and a standing commitment guard against the release plan |
| 2.3E Success Definition and Measurement | Module 5 tracks outcomes against the module 3 business case baseline |

### Course themes (from Dan)

1. Strategy is where product judgment is essential. The agent gathers evidence. The PM uses product sense, experience and judgment (Dan, 2026-11-26).
2. The AI gathers evidence and filters first. The PM decides. The PM sets the rules in the brief: every range, tolerance, threshold and cadence. The agent reports evidence against them. Do not use the phrase "no magic number" with learners (Dan, 2026-11-26).
3. Be great at product management before you are great at AI.
4. The roadmap is direction. The release plan is the promise. The agent never turns one into the other.

Note: Dan's Market Research theme "win/loss is the big aha" belongs to the Market Research course. This course has no win/loss lab. The aha is module 1, decided by Dan (Gate 2 decision 7): the shared Firmware team is planned at 100% in two programs, every per-program check passes, and the total is 200%. Module 5 (units shipped against active paid sites) is the closing echo. Same effect, different topic.

Pre-class and connectors (Gate 2 decisions 11 to 14): the "know before you design" check goes in the pre-class email and repeats in the course open. The Google Sheet template is an option on every platform. The core path is download .xlsx or CSV and upload in chat. Labs 3 to 5 each have one optional connector lane card, outside the 6 steps. Labs 1 and 2 have none (Dan, late item 14). No connector is needed to pass. No connector is named until a dated vendor doc exists. Data safety check comes first.

Cadence and evidence order (Gate 2): intake can be frequent, and the agent only logs and flags. The PM reviews the problem backlog at the PM's own cadence, often once a quarter. Reviewing too often causes whiplash. The agent may order the problem backlog by amount of market evidence. The column is "evidence order", never "priority". It is one input. The PM also weighs strategy, capacity, dependencies and other factors, because people follow an agent's lean (E1, "54% vs 36%"). A problem can rank high on evidence and impact and still be deprioritized for strategy, risk, investment level, build time, customer relations, dependencies or resource allocation.

### Where the course starts and stops

| Not taught here (known from elsewhere) | Taught here |
| --- | --- |
| Strategy Matrix, box mapping, "peanut butter" count, strategic drift as Focus frames it | A strategy consistency check against the stated strategy, OKRs and KPIs. Evidence only. No Strategy Matrix in any lab |
| Opportunity scoring attributes, weights, 1 to 5 scores, rescoring (Focus). Do not teach or mention | Request decisions: the agent builds a card, the PM decides yes, no or later |
| Tagging and counting weekly feedback by account (Market Research module 3) | The link from a request to the problem backlog, referred to as known. No slides on tagging or counting |
| One-pass Value and Cost Snapshot, market sizing as a one-pass exercise (Focus) | A living business case: register, red team, sensitivity in a sheet, refresh with "what changed" |
| One roadmap for two audiences, roadmap criteria, audience versions (Focus). Stakeholder updates (Build) | Per-item evidence trace, change impact, decision log and a commitment guard. No audience drafting (decision c, option 1) |
| Release planning and estimates (Build, skill 3.4) | A hand-off rule: a change that touches the release plan stops the agent and goes to the PM and the release plan owner. No new date (Gate 2 decision 1; spec `gate_2_designs`) |
| Success measures and the metrics story (Focus, Build) | Monthly tracking against the business case baseline, outcomes kept apart from outputs |
| Boundaries and guardrails as first taught (AI Agents course) | "Stop before a recommendation" hand-off rules, with new slides (house rule 14) |
| Prompt structure JOB AND CONTEXT, RULES, OUTPUT (PRW-AI) | Referred to as known. The brief adds checks, hand-off rules, audits and decision fields |
| Scheduled tasks (CAW-AI slide 9) | Stretch only, on platforms where verified, with new slides |

Core courses are not prerequisites (Dan, PS-06). Use the Pragmatic terms and define each one in this course. No "as in Focus" callbacks. No Focus examples.

## 2. Module level

Minutes: full day, then half days in brackets.

### Module 1. The quarterly portfolio pack: is the work consistent with the strategy? (row sp-wf-09, folds 01)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** 2.1 Strategy Alignment. Competency 2.1B Explicit vs. Implicit Strategy Analysis. Workbook text: "comparing what leaders say the organization is prioritizing with where resources, products, and attention are really being invested". This is the consistency check. Not taught: 2.1C Strategy Matrix Application. Box: Focus / Product Portfolio (the workbook gives it no primary skill; 2.1 is secondary) |
| 2. What the learner can do | Build the agent from the template. Add the strategy overview, OKRs and KPIs. Run the pack on team submissions. Decide each flag. Audit capacity by team and 3 linked items. Add a quality check and rerun. Make fund, pause or stop calls |
| 3. How far | Develop and Apply. First build, so a fast-start card per platform supports new builders. Planted error warning: **told** |
| 4. Evidence | Tuned brief (v1 to v2: the learner adds "total each shared team across all programs"). Flag report decisions for Q3. Audit findings for 2 shared teams and 3 linked items. The PM's fund, pause or stop calls on the flagged programs, and a note on whether the work or the stated strategy needs to change |
| 5. Experience | Course open and build check, then a live demo on one platform, then the lab on own plans or the Larkspan Q3 and Q4 submissions. The agent shows where capacity goes by objective and lists work with no clear link. It does not judge it. Planted error: the shared firmware team is at 100% in two programs. Each per-program check passes. The audit sums by team and finds 200%. Debrief: the aha, then each learner runs the check sample (3 minutes). Rung 1, hand-run batch. 70 minutes (80) |

### Module 2. Requests: the agent builds the case, you make the call (row sp-wf-12)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** 2.2 Opportunity Prioritization, through its AI text ("analyze evidence, surface inconsistencies") and competency 2.2E Opportunity Comparison and Decision Support, light form, with no scoring. Supporting: 1.1 Market Problem Identification, competency 1.1A Problem vs. Opinion Discrimination; 2.1D Opportunity-to-Strategy Fit Evaluation, which the PM does (the agent only quotes strategy or OKR text that may relate, or says none found, and makes no fit statement). Gap: 2.2A to 2.2D are written around scoring and are not covered. Box: Market / Market Problems (primary 1.1 and 1.3; 2.2 is secondary). The reply step touches Planning / Stakeholder Management |
| 2. What the learner can do | Add a request job. Read decision cards with a blank decision field. Audit 3 cards and 2 cited decision log entries. Add a matching rule. Write yes, no or later and a reason on each flagged card. Have the agent draft replies only after the decision |
| 3. How far | Develop and Apply. First decision checkpoint: the agent stops and waits for the PM. Planted error warning: **hint** ("Audit before you approve") |
| 4. Evidence | Tuned brief (matching rule: match on the problem and the user, not on feature words). Flag report decisions. Audit findings for 3 cards and 2 cited log entries. Decision cards with the PM's yes, no or later and reason. Reply drafts that match each decision |
| 5. Experience | Why this matters uses E1 ("54% vs 36%": people follow an agent's lean), which is why the decision field stays blank. Lab on own requests or Larkspan request batch 1, with internal requests to the Fleet Data Platform PM (internal PM, required). Planted error: a false duplicate. Two "offline mode" requests describe different problems (no signal for field installers, and a pharmacy and lab customer that cannot send data off site). The agent merges them and attaches last year's "no". Intake can be frequent. The agent only logs and flags. The problem backlog has an evidence order column; it is one input, not a priority (see the cadence note). Debrief: each learner runs the check sample (request batch 2, 3 minutes). Rung 1 plus, hand-run batch with a decision checkpoint. 60 minutes (75) |

### Module 3. The living business case: assumptions, red team and what changed (row sp-wf-05, folds 03 and 11; 04 as one check)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** 2.3 Business Case Development. Competencies 2.3B Market Value and Sizing, 2.3C Cost, Profit, and Resource Logic. Not taught: 2.3A Product Canvas Development, 2.3D Distribution and Solution Delivery Fit, 2.3F Stakeholder Argumentation (no lab step practices it). Box: Business / Business Plan (primary 2.3) |
| 2. What the learner can do | Add a business case job. Keep an assumption register with evidence, date, owner and effect. Run sensitivity in a course sheet that holds the formulas. Check market size inputs from a source pack (market, market segment, evaluator adoption, projected share). Audit the 2 assumptions with the largest effect. Add a hand-off rule. Rerun with new evidence at the PM's cadence and read "what changed". The update changes no priority. Decide the gate recommendation |
| 3. How far | Develop and Apply. First numeric module. Second run on new evidence. Planted error warning: **hint** |
| 4. Evidence | Tuned brief (hand-off rule: "a price that needs a minimum yearly order above the plan volume goes to the flag report"). Flag report decisions. Audit findings for 2 assumptions. The PM's gate recommendation (go, hold or stop to recommend) and the next assumption to test |
| 5. Experience | Hardware path (Larkspan Probe X, a cellular sensor with no hub, before the hard tooling commit). Market size from a case source pack, one link per number; live search is stretch. Projected share comes only from internal data. One quality check is the denominator check: each share or rate names its denominator. Planted error, in plain words: the supplier gives the lower price per set only above a minimum yearly order of 50,000 sets. The plan buys 18,000 sets in year 1 and uses the lower price. Every number has a source and a date, so the checks pass. The audit reads the quote terms. Core steps use no hardware terms. Card test: a PM with no hardware background understands it (Gate 2 decision 5). Debrief: the instructor shows the check sample result (1 minute); learners run it after class. Rung 2, refresh with a "what changed" report. 70 minutes (65) |

### Module 4. Roadmap refresh and change: trace every item, guard every promise (rows sp-wf-07 and sp-wf-08)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** 2.4 Product Vision and Roadmap. Competencies 2.4B Roadmap Structuring and Framing, 2.4C Assumption and Uncertainty Transparency, 2.4D Alignment to Market Problems and Strategy. 2.4C workbook text: "Distinguishes between roadmap direction, assumptions, dependencies, and committed delivery". Not taught: 2.4A Strategic Vision Articulation, 2.4E Stakeholder Communication and Alignment (no audience drafting, decision c). Box: Focus / Product Roadmap (primary 2.4). The release plan hand-off touches 3.4 Release Planning and Delivery Management (3.4B, 3.4D); the course does not claim it |
| 2. What the learner can do | Add a roadmap job in two parts: refresh the trace (at the PM's own cadence, often each quarter), then assess a change. Write the hand-off rule for release plan changes. Audit 3 roadmap items against the evidence log and add a rule for what the audit finds. Decide each flag. Write the decision log entry |
| 3. How far | Develop and Apply. First hand-off between jobs: an approved request from module 2 becomes a change request; the module 1 capacity table shows what it displaces. Planted error warning: **hint** |
| 4. Evidence | The release plan hand-off rule as written. Tuned brief (the learner writes the rule "judge each item by its own evidence, not its theme's" in lab step 4; the template does not hold it). Flag report decisions. Audit findings for 3 items. The decision log entry with the PM's decision and reason |
| 5. Experience | The full design is in spec `gate_2_designs.ps_10` for Dan's decision. A standing commitment guard runs on every change: any date, "will ship" or "committed" not on the release plan goes to the flag report (PS-05). The PM writes a confidential terms list in this lab, and one guard line checks it (decision e, Gate 2 decision 2). Talk track: the agent is a second check, not the control, and it misses paraphrases. A take-home Production readiness checklist says to test the agent with data science, privacy and compliance teams before production use. No grouping of untraced validated problems. Talk track lines: a one-off problem can reach the product backlog on its merit and impact; one problem can become several epics and many user stories; themes help focus and coordination with marketing and sales but are not required. The lab has one core message: the roadmap is direction, the release plan is the promise. Planted error: validation by association. A roadmap item backed by one sales request sits in a strong theme, so the trace shows it as linked. Debrief: the instructor shows the check sample result (1 minute); learners run it after class. Rung 3, hand-off between jobs. 65 minutes (60) |

### Module 5. Outcomes, not output: the monthly check against the business case (row sp-wf-10, retitled per PS-14)

| Question | Answer |
| --- | --- |
| 1. Capability and skills | **Confirmed by Dan (Gate 2 Q2).** 2.3 Business Case Development, competency 2.3E Success Definition and Measurement. Box: Business / Business Outcomes (the workbook gives it no primary skill; 2.3 is secondary) |
| 2. What the learner can do | Add an outcome tracking job that reads the module 3 baseline and the module 1 OKRs. Write the off-target range. Decide each flag. Audit 2 "on track" measures, starting with the outcome the business case names. Write the outcome-or-output rule for what the audit finds. Write an investment review note: keep, change or stop, with a reason |
| 3. How far | Develop and Apply. The agent runs across jobs each month and the PM reads only the flag report and a sample. Planted error warning: **none** |
| 4. Evidence | The off-target range and hand-off rules, and the outcome-or-output rule written in the debrief. Flag report decisions. Audit findings for 2 measures. Tuned brief after the debrief. The investment review note |
| 5. Experience | Lab on own metrics exports or the Larkspan October and November exports for Probe X. The agent never recommends an investment change (PS-14). Planted error: units shipped to resellers reported as the outcome "active paid sites" because the metric names match. Debrief: fix the brief, each learner runs the check sample (3 minutes). Close: Monday plan and kit-final. The monthly run measures results and changes no priority. Rung 3 plus, monthly run across jobs. 55 minutes (50) |

## 3. Notes for an instructor who did not build the course (decision 45)

1. Demo on one platform only. Step cards in the workbook carry each platform. Breakout rooms group learners by platform.
2. Say "flags", "flag report", "hand-off rules", "quality checks", "brief" and "audit". Do not say "exceptions" or "escalations".
3. Say "problem backlog" and "validated problem backlog". Never "opportunity backlog" or "Market Problems Table".
4. The agent never sets, proposes, ranks or rewrites strategy, and never fills a decision field. If a learner's agent does, that is a finding for the audit, not an answer.
5. The PM sets the rules in the brief. Every range, tolerance, threshold and cadence is the PM's choice. Do not say "no magic number" to learners. Numbers in the case are "the Larkspan PM's choice for this rule".
6. Do not teach or mention scoring attributes, weights or rescoring. Do not use the Strategy Matrix in any lab. No RICE.
7. Tell each story as one heard from client teams, executives or Pragmatic's work with companies. Never as your own experience (decision 43).
8. Reveal the planted error only in the debrief. Ask which check or audit found it.
9. A learner who falls behind rebuilds from the module's catch-up kit in about 5 minutes.

## 4. Open items for this brief

Dan answered the Gate 2 items on 2026-11-26. They are in `outline/gate-2-changes.md`. These items stay open.

| # | Item | Owner |
| --- | --- | --- |
| 1 | Tell the Pragmatic reviewer the mapping gaps: 2.2A to 2.2D are not covered (scoring is out), 2.2E text says "uses scoring outputs", 2.1C, 2.3A and 2.4E are not covered by design. Two module boxes (Product Portfolio, Business Outcomes) have no primary skill in the workbook | Dan, Pragmatic reviewers |
| 2 | Pragmatic reviewers and the ID team check that the learner evidence list can be scored in beta (decision 29) | Pragmatic reviewers, ID team |
| 3 | Title question for Pragmatic: does "planning" conflict with the Framework category Planning? | Pragmatic reviewers |
| 4 | Run the platform proof with the drafts in `outline/proof-kit-drafts.md` | Dan |
| 5 | Overlap checks (workshops, Mastering the Product Roadmap) and the Focus recheck (house rule 11) | Dan |
| 6 | Evidence before slides: W1, W3 and the licensed HBR copy for Trendslop. Bond story is Trendslop, in words only until then | Research rerun |
