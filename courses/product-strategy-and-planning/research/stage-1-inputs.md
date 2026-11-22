# Stage 1 inputs: Advanced AI for Product Strategy and Planning

Written 2026-11-22 before the researchers start. Every Stage 1 agent reads this file after `CLAUDE.md`.

## 1. Scope

- PRD topic area: "Strategy, roadmaps, planning".
- Standalone course. No prerequisite. Dan delivers it (decision 45). Talk track must work for a part-time instructor later.
- Offering intent: Develop and Apply (decision 41). Learners are agent managers (house rule 12): one course agent, built in module 1, extended in each lab.
- Format: one day, 360 teaching minutes, or two half days of 195 minutes. 4 to 6 modules.

## 2. Pragmatic home for this course (from the Capability Standards Workbook 2027)

Capability 2, Strategic Direction: "how an organization turns market evidence into product strategy, prioritized opportunities, business cases, and roadmaps." Core product course: Focus.

| Skill | Primary framework box | Secondary boxes | AI-embedded text (workbook, short) |
| --- | --- | --- | --- |
| 2.1 Strategy Alignment | Product Strategy | Distinctive Competencies, Market Definition, Product Roadmap, Product Portfolio | Synthesize strategic context, expose implicit strategy, run scenarios. Strategy stays a forced-choice human decision |
| 2.2 Opportunity Prioritization | Competitive Landscape | Distinctive Competencies, Business Outcomes, Market Problems, Product Portfolio | Draft scoring criteria, analyze evidence, run sensitivity tests, surface scoring inconsistencies. Weights and final priorities stay human-owned |
| 2.3 Business Case Development | Business Plan | Pricing, Business Outcomes, Distribution Strategy, Buy Build or Partner | Assemble evidence, model market size, costs and AI unit economics, find assumptions and risks, red-team the case. Data and calculations stay auditable |
| 2.4 Product Vision and Roadmap | Product Roadmap | Product Strategy, Stakeholder Management, Measurement | Cluster validated problems into outcome themes, simulate sequencing and dependency scenarios, tailor narratives. Must not turn uncertain direction into false delivery commitments |

Full competency text: workbook sheet "Skill Standards" (copy in project files `course-builder/reference/pragmatic-sources/`). Use workbook names exactly. Do not invent standards.

Other offerings the workbook maps to capability 2 (check for overlap): Focus Implementation Playbook; workshops Strategic Transformation and Implementation, Action Planning Workshop; AI courses Vibe Coding for Problem Validation (2.2), AI Agents for Product Professionals (2.2, Dan's course), AI in Your Product (2.3), Intro to AI (2.3); live AI workshop Competitive Analysis with AI (2.1, 2.2); partner courses Mastering the Product Roadmap, Demystifying Finance, Accelerate Your Subscription Business, Mastering B2B Product Innovation, Executive Briefing.

## 3. Candidate framework boxes (Framework 2027, 37 boxes)

Most likely: Market / Product Strategy, Market / Distinctive Competencies, Market / Competitive Landscape, Focus / Market Definition, Focus / Product Portfolio, Focus / Product Roadmap, Business / Business Plan, Business / Buy, Build or Partner, Business / Business Outcomes, Business / Measurement, Planning / Ideation, Planning / Stakeholder Management.

Name collision to flag: the Framework has a category called "Planning" (Positioning, Buyer Journey, Buyer Personas, User Personas, Requirements, Ideation, Stakeholder Management). The course title uses "planning" in the everyday sense (annual and quarterly planning, roadmaps). Tag rows with the correct Framework category.

## 4. What Pragmatic core courses already teach with AI (no-repeat check)

Source: Focus draft `FCS_28.01_DRAFT_v6_Full.pptx` and Build draft `BLD_28.01_DRAFT_v1.pptx` (project files root). Not yet in Dan's named source list; used here for the no-repeat check only.

Focus 28.01 (Strategy, Score, Propose, Communicate; Product Canvas; case DeepView AI, a health care MRI company; also PulseVision and internal case FieldAssist):
- Strategy Matrix; explicit vs implicit strategy; strategic drift; "peanut butter" strategy.
- Activity: AI drafts the Alignment to Strategy box; learner checks it against criteria.
- Opportunity scoring: 4 attributes (Distinctive Competencies, Competitive Landscape, Impact to Buyers and Users, Investment Level), 1 to 5 scoring, weights, scoring table.
- Activity: AI builds a first-pass competitive landscape; learner checks sources.
- Market sizing (TAM, segment, projected share); value types; buy, build or partner decision tree.
- Activity: AI drafts a one-page Value and Cost Snapshot.
- Activity: interview an AI persona (Phil, CMO; Emily, radiologist) on how they buy, receive and use.
- Success measures; full canvas review; risks stakeholders raise.
- Roadmap: outcome not output, timeframe not date, problems not features; one roadmap, two audiences (optional AI activity); "the roadmap is the vision, the release plan is the promise".
- AI Capability Map per module. Tip: "Use AI to check new PRDs, project plans, and roadmap updates against the Strategy Matrix and OKRs."

Build 28.01: stakeholder mapping and updates drafted by AI; estimates from past performance; metrics story; release planning.

Rule for this course: do not reteach any of the above as one-pass AI activities. Start where Focus stops: an agent the PM manages over time, with checks, hand-off rules, a flag report and an audit. Same principle is allowed; same exercise with the same case is not.

Fallback case names to avoid: BadgeWorks, Entrilo, FieldPro, DeepView AI, PulseVision, FieldAssist. Larkspan Systems is the Market Research case (reuse is a Dan decision).

## 5. Inputs carried over from Market Research (Dan, Gate 1, 2026-11-22)

| Row | Workflow | Status | Notes |
| --- | --- | --- | --- |
| mr-wf-06 | Build and refresh a sourced market size and segment evidence model | Candidate row | Bottleneck sources W9 (2025) and W19 (2023) both age-flagged. Needs a 2026 source. Planted error was "fake triangulation" |
| mr-wf-08 | Turn each round of concept or prototype tests into a result per hypothesis | Candidate row | Fails the 2-source rule (W16, vendor, not verified). Needs new research. Planted error was "stated preference read as a pass" |

Full rows: `courses/market-research/research/workflows.yaml`. Give new ids in this course (`sp-wf-NN`) and record the old id.

## 6. Themes Dan set in Market Research that carry over

- There is no magic number. The agent reports evidence; the PM's judgment sets the bar.
- Be great at product management before you are great at AI.
- A relative backlog (urgency, pervasiveness, willingness to pay) beats a fixed bar.
- AI personas only from data the team collected. Synthetic respondents never replace real conversations (workbook skill 1.3 says the same).

## 7. Model row

No course-specific worked example row exists. Use the approved Market Research row `courses/market-research/research/worked-example-row.yaml` (mr-wf-01, v3) as the model for depth and format. Do not copy its content. Row ids: `sp-wf-01` to `sp-wf-12`.

## 8. Web fetch budget

About 100 fetches per hour, shared by all agents. Shares for run 1: workflows 25, methods and platforms 15, PM needs 20, evidence 20, bond story 15. Search results do not count as fetches; opening a page does. Stop at your share and record what you did not open.

Extracted text of the Pragmatic files (scratch, this session only): `/tmp/claude-0/-home-user/08608aad-ff27-5b34-985a-6dbdbd4499d3/scratchpad/` files `fw.txt` (framework guide), `wb.txt` (workbook), `fcs.txt` (Focus 28.01), `bld.txt` (Build 28.01).
