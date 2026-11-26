# Stage 2 inputs: Advanced AI for Product Strategy and Planning

Written by the thread session on 2026-11-26 before Stage 2 starts. All Stage 2 agents read this file first. It collects what Gate 1 approved and what the Market Research course taught us. It does not replace `research/gate-1-decisions.md`. If they differ, `gate-1-decisions.md` wins.

## 1. Why Stage 2 can start

1. Gate 1 is approved (Dan, 2026-11-26, `status.yaml`).
2. The hold is lifted. Pragmatic reviewed the Market Research syllabus and said "looks great, keep moving forward" (Dan, 2026-11-26).
3. Pattern to mirror: `outline/reference-mr-syllabus-approved.md` (the Market Research syllabus that Pragmatic approved). Keep its structure, section order, tone and level of detail.

## 2. The five modules (Gate 1, final)

| Module | Rows | Core of the lab | Skill (workbook) |
| --- | --- | --- | --- |
| 1 | sp-wf-09 (model row, `research/worked-example-row.yaml`), with sp-wf-01 folded in | Quarterly portfolio review pack with a strategy consistency check: the agent compares planned work and spend with the stated strategy, OKRs and KPIs, and reports gaps as evidence. No Strategy Matrix, no box mapping, no "peanut butter" count | 2.1 Strategy Alignment |
| 2 | sp-wf-12 (`research/rerun-replacement-02.yaml`) | Request decision and response: the agent builds a decision card with the decision field blank. It drafts the reply only after the PM writes the decision and the reason. No tagging or counting (Market Research module 3 owns that). sp-wf-13 is a possible stretch | 2.2 Opportunity Prioritization (AI text only, not 2.2A to D) |
| 3 | sp-wf-05, with sp-wf-03 (market size) and sp-wf-11 (hardware path) folded in. sp-wf-04 denominator check becomes one quality check | Living business case: assumption register, red-team, sensitivity in a course sheet with formulas, market size inputs from a case source pack | 2.3 Business Case Development |
| 4 | sp-wf-07 and sp-wf-08 | Roadmap refresh with a per-item evidence trace to the validated problem backlog, then a change impact assessment: what the change displaces, dependency hits, decision log, and a standing commitment guard against the release plan | 2.4 Product Vision and Roadmap |
| 5 | sp-wf-10 (retitle per PS-14) | Monthly outcome tracking against the business case baseline from module 3 | 2.3 (2.3E) |

Out of the course: sp-wf-02 (scoring, rescoring, Focus attributes: do not teach or mention), sp-wf-04 as a lab, sp-wf-06 (stretch in module 3 only if time allows), sp-wf-14.

## 3. Rules from Gate 1 that the spec must show

1. **AI never sets strategy.** The agent gathers and reports evidence. It never proposes, ranks or rewrites strategy, and never makes the priority call. The PM decides with product sense, experience and judgment. Make each hand-off rule explicit (Dan, decision b and course theme).
2. **No magic number.** The PM sets every range, tolerance and threshold in the brief. The agent reports evidence against it. "Be great at product management before you are great at AI."
3. **Core courses are not prerequisites.** Use Pragmatic names (problem backlog, validated problem backlog, market, market segment, evaluator adoption, projected share) and define each in this course. No "as in Focus" callbacks. No Focus examples.
4. **No audience drafting** in the roadmap lab (decision c, option 1, working choice). One commitment guard, run on every change against the release plan.
5. **Terms:** "problem backlog" (feeds the product backlog), "validated problem backlog" for row 07 input. Never "opportunity backlog" or "Market Problems Table". Skill names exactly as the workbook writes them. Agent-manager terms: brief, quality checks, hand-off rules, flag report, audit. Never "exceptions" or "escalations".
6. **Platforms (decision f):** ChatGPT Plus is the minimum plan and a prerequisite. ChatGPT Work file output with formulas is the ChatGPT core path for numeric steps. Gemini numeric steps use a Google Sheet template with formulas. Copilot learners upload the sheet in chat each run and download output in the same session; Copilot case files are .xlsx, one sheet each. Market size refresh core path uses a case source pack; live search is stretch (Claude, ChatGPT, Copilot); one link per number; Gemini learners upload the new source. Second blind run in a new ChatGPT chat outside the project. Ship a CSV copy of each sheet. 30 MB limit in step cards. Code execution and web search on the pre-class checklist.
7. **Case (decision j):** reuse Larkspan Systems (`courses/market-research/case/company.md`). Add a short strategy overview, OKRs, and KPIs or business metrics with targets. The Strategy Matrix may get one mention in the overview; no lab uses it. No scored backlog. A problem backlog with evidence and a request log.
8. **Bond story:** held to the module 1 deck (lean Trendslop, E3). E3 numbers stay off slides until a licensed copy is read. Do not reuse Juicero, WeWork, Jitterbug or "maxed out employees".
9. **Evidence limits:** no E9, no E10 on a slide, no RICE (PS-15). E1 wording "54% vs 36%". E2 Science version only. See `research/research-brief.md` section 3.
10. **Title (decision g):** keep the title. Add: "Planning here means annual and quarterly product planning. The course maps to Capability 2, Strategic Direction." Ask Pragmatic the title question.
11. **PS-05:** the brief names the PM's own timeframes. Flag any date or promise not on the release plan.

## 4. Parked for Gate 2 (surface for Dan's decision, with a concrete design)

1. **PS-10, release plan hand-off rule (module 4).** Dan: "I'm having a hard time visualizing this, so I'll have to see it in full." Show the whole roadmap module: inputs, agent steps, the hand-off rule for release plan changes, a sample flag report, and what the PM does. Give options and a recommendation.
2. **Decision e, data safety design.** Dan: "I'm having trouble envisioning how this is gonna work in the classroom." Provisional: strategy lines replace the interview and win/loss lines; a teaching point on confidential content; a running log point. Since no audience drafting is in the labs, the teaching point shrinks to one check in the commitment guard. Show what a learner sees and does in a lab, minute by minute. Give options and a recommendation.

## 5. What Market Research Stage 2 taught us (apply here)

| Lesson | Apply as |
| --- | --- |
| Timing (Dan, 2026-11-22) | Full day 09:00 to 16:30, 60-minute lunch, two 15-minute breaks: 360 teaching minutes. Two half days: 3.5 hours each with one 15-minute break: 195 teaching minutes per day, 390 total. Never plan a 45-minute lunch |
| Opening | Course open about 25 minutes: opening story slot, build check (create, save and reopen a starter agent), course frame, "know before you design" data check |
| Check sample | Each lab has a second sample and a pass condition. Say which modules run it in the debrief and which run it after class |
| Catch-up kit | Each module has a catch-up kit; rebuild in about 5 minutes |
| Fast-start card | Module 1 has a fast-start card per platform for learners new to the builders |
| Stretch | Stretch steps only on platforms whose step card supports them. Copilot Studio, Power Automate and Google Antigravity are not used |
| Copilot Chat only | Learners with Copilot Chat only use a reduced path that runs one job at a time |
| Agent proposes, PM decides | The agent may propose an order of items with a reason (for example a request decision card). The PM decides. In this course, the agent never proposes strategy |
| Internal PM | Use the internal platform team in at least one lab (Market Research decision 9) |
| Module 4 length | Times can flex in delivery; 55 minutes is acceptable for a short module |
| Capability mapping | Put a proposed mapping (capability, skills, competencies per module) in the packet for the Pragmatic reviewer document. Use workbook names exactly |

## 6. Files to read

- `CLAUDE.md`, `docs/PRD.md` (Organize and outline stage; Module, slide and exercise design; decisions 34 to 45)
- `courses/product-strategy-and-planning/research/`: `gate-1-decisions.md`, `research-brief.md`, `worked-example-row.yaml`, `workflows.yaml` (rows 01, 03, 05, 07, 08, 09, 10), `rerun-track-1.yaml` (row 11), `rerun-replacement-02.yaml` (row 12), `platform-matrix.yaml`, `bond-stories.md`, `alignment-log.yaml` (PS items)
- `shared/registry/registry.yaml`
- Format model: `courses/market-research/spec.yaml`, `courses/market-research/outline/development-brief.md`, `courses/market-research/case/`
- Pragmatic workbook (skill and competency names): `research/stage-1-inputs.md` quotes them
