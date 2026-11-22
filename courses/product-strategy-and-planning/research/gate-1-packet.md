# Gate 1 packet: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`. Stage 1, run 1, with one rerun of tracks 1 to 4. Written by the Synthesizer on 2026-11-22.
- For: Dan. You mark each row retain, defer or reject, and answer decisions a to k.
- Reading time: about 25 minutes. Spot checks (section 5): about 45 minutes.
- Full detail: `research-brief.md`. Rows in full: `workflows.yaml` (sp-wf-01 to 10) and `rerun-track-1.yaml` (sp-wf-11, W25 to W28). Evidence ids: `evidence-ledger.yaml` and `rerun-track-4.yaml` (E), `workflows.yaml` and `rerun-track-1.yaml` (W), `needs.md` and `rerun-track-3.md` (N). Platform ids: `platform-matrix.yaml` and `rerun-track-2.yaml`. Checks: `verifier-report.md` (both sections), `critic-report.md`, `alignment-log.yaml`.
- Evidence labels: V = verified, PV = partly verified, NV = not verified. "Vendor" = the publisher sells a product or service in this area.
- Stage 2 is on hold until Pragmatic reviews the Market Research syllabus, also after you approve Gate 1.

## Read this first (Claude Code, run lead)

1. Overlap with Focus 28.01 is the biggest risk. The Focus draft demos three agents (Strategy Alignment, Roadmap Translator, Market Sizing) "built and maintained by the SME". If Dan built them, house rule 11 applies to rows 01, 03 and 08. Answer decisions b and c first.
2. Evidence is thin. Every retained bottleneck rests on vendor or vendor-run sources with no time or cost data. The strongest 2026 evidence is about AI risk (E1, E2). No "AI saves X hours" slide.
3. Disagreement with the Synthesizer on decision f, row 1: "Go or Plus" makes Go learners copy numbers from an on-screen table into the sheet, so the learner becomes the middleman between AI steps. Recommendation: Plus minimum for this course; Go learners pair with a Plus learner.

Gate 1 doc: https://claude.ai/artifact/3eUhFMaL5rhUiJSgsWNrsk

## 1. Workflow rows: your decision per row

The "Critic" column is the research critic's view. The "Synthesizer" column is this packet's recommendation. You decide.

| Row | Workflow | Bottleneck (2-source result, verifier) | Category / focus area | Workbook skill | Evidence (ids, strength) | PM decision | AI error to catch | Proposed lab | Open gaps | Critic | Synthesizer | Dan's decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sp-wf-01 | Check each quarter where work and money go against the stated strategy (drift check) | Passes (W1, W3). W3 figures come from the N21 survey | Market / Product Strategy | 2.1 Strategy Alignment (2.1B Explicit vs. Implicit Strategy Analysis) | W1 V vendor (308 leaders, period not stated). W3 PV (= N21 V). W2 PV is the same study as W1 | Where the implicit strategy differs from the explicit one; change the work or the stated strategy | Label laundering: maintenance epics tagged with a strategic theme, so the mapping looks aligned | Drift report by Strategy Matrix box (PS-16), trend, flags, audit of 5 items | Internal PM and hardware sources. Repeats a Focus demo agent (PS-01) | Merge into 09 | Fold into 09 (decisions a, b) | |
| sp-wf-02 | Rescore the opportunity backlog each cycle, with sensitivity and consistency checks | Passes after rerun (W25, W26: signed, 2026, both vendor or vendor-run). No time or cost data | Focus / Product Portfolio (2.2 primary box is Competitive Landscape, PS-13) | 2.2 Opportunity Prioritization (2.2C Weighting and Priority Logic, 2.2D Calibration and Consistency) | W25 V, W26 V (figures illustrative), W27 V (figures = N21), N21 V (60.2% override factor), N12 V internal PM. Old pair: W4 V, W5 PV | Which opportunities advance, pause or stop. Weights. Final scores (PS-04) | One customer request cited as evidence under two attributes, so one sales push lifts the score twice | Agent drafts scores in the course sheet, runs the sensitivity test, lists scorer gaps, logs overrides. PM audits 3 items | Hardware partial. Scoring model and who sets final scores (PS-03, PS-04) | Retain | Retain. Model row candidate (decision h) | |
| sp-wf-03 | Build and refresh a sourced market size and segment model (from mr-wf-06) | Passes (W7, W8: 2026, both data vendors). W9, W10 kept with age flags | Focus / Market Definition | 2.3 Business Case Development (2.3B Market Value and Sizing) | W7 V, W8 V. W9 V (2025, age flag), W10 V (2023, age flag) | Which segment is large and reachable enough for the business case | Layer mixing: two estimates of different scope reported as agreeing (rename per PS-06) | Step in module 3: market input of the case from a source pack. Web search refresh is stretch | Hardware and internal PM sizing. Non-vendor source. Focus bubbles (PS-06) | Merge into 05 | Fold into 05 | |
| sp-wf-04 | Turn each round of concept tests into a result per hypothesis (from mr-wf-08) | Partly passes. W11 and W12 each support a different half. W13 NV | Planning / Ideation | 6.4 Ideation, Evaluation, and Prototyping (outside Capability 2) | W11 V, W12 V vendor | Go, change or stop for each concept | Denominator drift: success counted as 6 of 7, not 6 of 12 in the plan | None in this course | Concept-test source. Scope (PS-08) | Reject here (Design course) | Out of scope as a lab. Keep its denominator check as one quality check in 05 | |
| sp-wf-05 | Keep the business case assumption register current and red-team it before each decision point | Partly passes. "Cases go stale" is W15 only (2024, age flag). W14 is a poll of valuation practitioners, not PMs | Business / Business Plan | 2.3 Business Case Development (2.3C Cost, Profit, and Resource Logic; 2.3F Stakeholder Argumentation) | W15 V aged. W14 PV (not a PM statistic). Hardware: N10 V, N11 V | Which assumptions to accept. Continue, change or stop | Adoption assumption backed by a survey of stated interest, not a pilot with real use | Module 3 core: register, low, base and high values in the sheet, red-team note, audit of the 2 top assumptions | 2026 product-team source. Keep W15 (decision i) | Retain | Retain with condition: keep W15, record the gap | |
| sp-wf-06 | Keep a buy, build or partner option pack current | Passes (W16, W17) | Business / Buy, Build or Partner | 2.3 Business Case Development (secondary box) | W16 V, W17 V. W18 NV (context) | Build, buy, partner or combine; when to revisit | Build option costed from a quick prototype, with placeholder run costs | Stretch only | Low repetition. Hardware gap | Defer | Defer. Optional stretch step in module 3 | |
| sp-wf-07 | Refresh roadmap themes each quarter and trace each item to a validated problem and strategy | Passes, weak (W19, W3). "Manual work each cycle" is inferred | Focus / Product Roadmap | 2.4 Product Vision and Roadmap (2.4B Roadmap Structuring and Framing; 2.4D Alignment to Market Problems and Strategy) | W19 V, W3 PV. W24 NV (2023) | Which themes the roadmap shows; which items leave | Validation by association. Critic fix: the weak item cites a validated but unrelated problem id, so the trace looks valid | First step of module 4: refresh the trace from the Market Problems Table (PS-09) | Second 2026 source. Internal PM. Mastering the Product Roadmap overlap not checked | Retain, fix the error | Retain. Share module 4 with 08 | |
| sp-wf-08 | Assess each roadmap change and send consistent notes to each audience | Passes, weak (W20, W19). W21 (2019) NV | Planning / Stakeholder Management (name collision, PS-07) | 2.4 Product Vision and Roadmap (2.4C Assumption and Uncertainty Transparency; 2.4E Stakeholder Communication and Alignment) | W20 PV (figures unsourced), W19 V | Accept, defer or reject the change. What each audience hears | Revised (PS-05): the sales note says "ships in Q2" for an item that is on the roadmap but not on the release plan | Module 4 core: impact note, decision log, commitment guard against the release plan. Audience notes are one short step (PS-02) | Primary for W20. Internal PM. Build and Focus demo overlap (PS-02) | Retain, fix the error | Retain with PS-02, PS-05, PS-10 changes | |
| sp-wf-09 | Assemble the quarterly portfolio review and planning pack | Passes (W1, W22: both 2026, both vendor) | Focus / Product Portfolio | 2.1 Strategy Alignment (skill objective: portfolio direction and resource allocation) | W1 V, W22 V. Hardware: W19 V, W22 V | Fund, pause or stop. Capacity trade-offs. What goes to leaders | Critic fix: one shared firmware team named two ways ("FW Platform", "Firmware Core") and planned at 100% in two programs, so the per-team sum misses it | Module 1: build the agent from a template. Pack with capacity by team and a drift section from 01 | Data on review effort. Internal PM beyond one anecdote. Workshop overlap not checked | Retain as lead of 01 + 09 | Retain. Lead of module 1 | |
| sp-wf-10 | Track outcomes each month against the business case and OKRs; flag measures off track for the PM's investment review (title per PS-14) | Partly passes. W23 lists warning signs (public sector). "Few teams compare results with the baseline" has no source | Business / Business Outcomes | 2.3 Business Case Development (2.3E Success Definition and Measurement) | W23 V (public sector), W1 V, W2 PV | Keep, change or stop investment | Output counted as outcome: "guide shipped" reported as the key result "reduce onboarding time" | Module 5: monthly run reads the module 3 baseline. Schedule is stretch | Product-team source. Hardware gap | Retain | Retain with condition: reword to "warning signs include ..." | |
| sp-wf-11 (new) | Check a hardware gate package against the business case before each commit point | Partly passes (N10, N11: independent, 2026). "Manual cross-document work" goes past the sources. N24 adds one source on gate preparation burden | Business / Business Plan | 2.3 Business Case Development (2.3C); secondary 2.4 | N10 V, N11 V, N24 V (single). W6 NV | Go, hold or stop to recommend. Which assumption to test before money is committed | Tooling quote priced at 50,000 units a year; the case plans 18,000 in year 1 | Hardware path of module 3, with the fallback case or own hardware work | Gate review time. Internal PM. Overlap with 05 | Not reviewed (rerun row). Rerun proposes the hardware variant of 05 | Fold into 05 as its hardware path | |

Result if you accept the Synthesizer column: 6 rows retained (02, 05, 07, 08, 09, 10), 3 folded in (01 into 09; 03 and 11 into 05), 1 out of scope (04), 1 deferred (06). This gives 5 modules, because 07 and 08 share one module. Without the 2 conditional rows (05, 10), 4 rows stay (02, 07, 08, 09). That still meets check 7.

## 2. Decisions for Dan

Each decision has facts, options and one recommendation. Items marked "approved item" change something you approved in Market Research. I do not change them without your yes.

### a) Row merges and scope

Facts:

- 01 and 09 use the same inputs (work export, capacity, strategy), the same cadence and the same audience (critic).
- 03 is the market input of the 05 business case (critic). Alone it repeats the Market Research shape.
- 04 maps to skill 6.4 and Planning / Ideation. The Design course owns them (PS-08). You moved the row here; this does not reopen the move.
- 06 passes the 2-source rule, but repetition is low to medium (critic).
- 11 (new in the rerun) has the same agent job as 05: check the case against new evidence before a commit. It is the only row with a hardware core.

| Item | Option 1 | Option 2 | Option 3 | Recommendation |
| --- | --- | --- | --- | --- |
| 01 and 09 | Fold 01 into 09: drift becomes one section of the pack | Keep 01 as its own module | Drop 01 | Option 1 |
| 03 and 05 | Fold 03 into 05: the size model is the market input of the case | Keep 03 as its own module | Defer 03 again | Option 1 |
| 04 | Out of scope as a lab. Its denominator check becomes one quality check in 05 when evidence is a concept test | Own row tagged 6.4 | Reject; record for a future Design-aligned course | Option 1 |
| 06 | Defer | Stretch step in module 3 | Retain as a module | Option 1 (stretch is fine if module 3 has time at Gate 2) |
| 11 | Hardware path of 05: learners with hardware work, and the fallback case if it is a hardware company, run the gate check | Own module | Defer | Option 1 |
| 07 and 08 | One roadmap module: refresh the trace, then assess a change | Two modules (6 in total) | Fold 07 into module 1 so drift is taught once | Option 1 |

Recommendation: option 1 on each line. Reason: it gives 5 distinct modules inside the 4 to 6 range and teaches each Focus-adjacent idea once.

### b) PS-01: drift check against the Focus 28.01 Strategy Alignment demo agent

Facts:

- Focus 28.01 slides 25 to 28 show the same job: map work to show where investment goes, flag drift, and a Strategy Alignment agent demo. Slide 28 notes: the agent is "built and maintained by the SME. Instructors run it; it is not shared with learners."
- You are the named Focus instructor, so the demo agent is likely yours. House rule 11: course labs must be clearly stronger builds than your existing agents.
- New in this course: quarterly trend, totals that must reconcile, a "must do" category, flags for tag-only mappings, and an audit.

| Option | What changes |
| --- | --- |
| 1. Align with Focus | Drop 01 as a lab. One sentence refers to the Focus drift check |
| 2. Fold and strengthen (recommended) | Fold 01 into 09 (decision a). The 09 pack is the lab core; drift by Strategy Matrix box is one section. You compare your Focus demo agent with the merged row before Gate 2 |
| 3. Keep as written | Keep 01 as its own lab. Tell Focus graduates the data is different |

Recommendation: option 2. Reason: the portfolio pack is new against Focus, and the drift section keeps the 2.1B fit without a repeat lab.

Question for you: did you build the Focus Strategy Alignment agent? If yes, the Gate 2 spec lists how the course agent differs.

### c) PS-02: change notes against the Build 28.01 Stakeholder Update agent and Focus "one roadmap, two audiences"

Facts:

- Build 28.01 shows a Stakeholder Update agent that drafts one update per stakeholder, with approve, spot-check and stop rules. Build also shows an agent that drafts the roadmap update while a person checks dates and commitments.
- Focus 28.01 has "One Roadmap, Two Audiences" (optional AI activity) and a Roadmap Translator demo.
- New in row 08: impact on displaced items and dependencies, a decision log, and the commitment guard (methods S8).

| Option | What changes |
| --- | --- |
| 1. Align with Pragmatic | Remove per-audience drafting. Keep only the impact note and decision log. Point to Build |
| 2. Change assessment as the core (recommended) | Core: what the change displaces, dependency hits, decision log, commitment guard against the release plan. Audience notes become one short step that names the Build idea. New slides only for hand-off rules (house rule 14) |
| 3. Keep as written | Add one talk track line on how it differs from Build and Focus |

Recommendation: option 2. Reason: impact analysis and the decision log are in neither core course, and the 2.4 AI text supports them.

Related, same row: PS-05 (planted error) and PS-10 (scope) are in the quick table below. Question for you: did you build the Build Stakeholder Update agent or the Focus Roadmap Translator?

### d) PS-03 and PS-04: scoring model and who sets the final scores

Facts:

- Focus 28.01 uses 4 attributes: Distinctive Competencies, Competitive Landscape, Impact to Buyers and Users, Investment Level. It uses a 1 to 5 scale. Workbook 2.2 names the same 4.
- methods.md S1 says to use different criteria. Row 02 writes "Impact to buyers". The files disagree.
- Focus Score AI Capability Map marks "Set the attribute weights" and "Agree on the final opportunity scores" RED. Workbook 2.2: weights and final priorities stay "transparent, calibrated, and human-owned".
- methods.md S4 counts 2 fresh agent runs as a scorer pair. That is a model consistency test, not team calibration (2.2D).

| Option | What changes |
| --- | --- |
| 1. Same model, different job (recommended) | Template and case use the 4 Focus attributes with exact names and the 1 to 5 scale. Learners with their own model use it. Agent scores are "draft scores". "Agree on the final scores" moves to pm_decides. Core consistency pair: agent and PM, or 2 stakeholders. Two agent runs are an extra test |
| 2. New attributes | Use agent-friendly attributes (for example evidence freshness) and explain why |
| 3. Map both | Different attributes in the case, plus one slide that maps them to the Focus 4 |

Recommendation: option 1. Reason: the no-repeat rule is met by the agent job (rescoring over time, sensitivity, consistency, override log), not by new criteria. Your theme applies: the PM sets the ranges in the brief; there is no magic number.

### e) PS-12: data safety note for strategy work (approved item: PA-03)

Facts:

- Every row now carries the PA-03 note you approved for Market Research. Its interview consent and win/loss lines do not fit strategy labs.
- Strategy inputs are confidential plans, unreleased roadmaps, forecasts, pricing, cost models and supplier terms (needs.md data risks; N1 V: "protect sensitive information").
- New risks in this course: external versions of a roadmap or change note can carry confidential content, and web search sends the query outside the company (methods S7).
- MNPI advice (N18, not opened by the verifier) is written for financial firms. Using it for other public companies is an inference. Do not state it on a slide without legal review.

| Option | What changes |
| --- | --- |
| 1. Strategy lines in place of interview lines | Keep the PA-03 core lines. Replace the interview and win/loss lines with: "No confidential plans, unreleased roadmaps, forecasts, pricing, supplier terms or non-public financial data in a tool the company has not approved. Check every external version for confidential content. Do not put confidential names in web search queries." |
| 2. Option 1 plus a teaching point (recommended) | Option 1, plus: an agent that drafts for several audiences can move confidential content from an internal note into an external one. The commitment guard also checks for confidential terms. Keep the PA-03 point that a running log keeps sensitive data longer. If the tool is not approved, use the fallback case or remove names and prices first |
| 3. Keep the Market Research note | No change |

Recommendation: option 2. Reason: it keeps your PA-03 rule and adds the risks Focus already names ("nothing confidential is in the customer version"). No statistic in the note.

### f) Platform risks

| # | Risk | Evidence | Recommendation | Other options |
| --- | --- | --- | --- | --- |
| 1 | ChatGPT spreadsheet output with formulas is documented only through ChatGPT Work. Work is not on Free or Go, and not in a project with project-only memory. Your Market Research minimum was "Go or Plus" | cg-09 V, cg-10 V, cg-14 V. Data analysis download not documented, plans not named (cg-11 V) | Keep "Go or Plus" for the core path. Math runs in data analysis and shows as an on-screen table; the learner pastes values into the course sheet with formulas. Work file output is a stretch for Plus and up. Test data analysis on Go at Gate 2 | Plus minimum with Work as core; business plan minimum |
| 2 | Gemini: no dated Google doc says a skill runs code, outputs a file or uses Google Search | gm-11 PV, gm-15 NV (gap), gm-14 V (app only, no .xlsx), gm-10 PV (undated), gm-06 PV | Gemini numeric steps use a Google Sheet template with formulas. The skill writes the inputs as a table and reads back the results. Gate 2 tests one skill run that asks for a Sheet; if it works, it becomes a stretch step | Leave numeric steps out of the Gemini card |
| 3 | Copilot: the docs name only files uploaded in chat as code interpreter input; output lasts for the session. One page says code interpreter is "always enabled" in Agent Builder; another shows a toggle | mb-13 V, mb-15 V, mb-11 V, mb-04 V. CSV not allowed as embedded knowledge; one sheet per workbook (mb-14 V) | Learner uploads the sheet in chat for each run and downloads the output in the same session. Case files for Copilot are .xlsx, one sheet each. Gate 2 tests the toggle and the embedded copy. License or billing stays a prerequisite (your Market Research decision) | Fallback as the default Copilot path |
| 4 | Web search for the market size refresh differs by platform | Claude cl-ws-08 PV (owner turns it on for Team and Enterprise). ChatGPT cg-13 V (all plans; citations "may" be included). Copilot mb-12 V (4 URLs or Search all websites). Gemini skill: not documented | Core path uses a source pack from the case. Live search is stretch on Claude, ChatGPT and Copilot. The brief requires a link per number. Gemini learners upload the new source | Live search as core on 3 platforms |
| 5 | ChatGPT default project memory can leak run 1 into a "blind" second scorer run | cg-14 V | Second scorer run in a new chat outside the project | Use project-only memory (then no Work) |
| 6 | Claude: XLSX upload needs code execution, which an org owner can turn off. Upload size pages disagree | cl-up-10 V, cl-fo-06 V | Ship a CSV copy in the case pack. Use 30 MB in step cards. Add code execution and web search to the pre-class checklist (decision 44) | None |

### g) PS-07: the word "planning" in the course title

Facts:

- The Framework has a category "Planning": Positioning, Buyer Journey, Buyer Personas, User Personas, Requirements, Ideation, Stakeholder Management (guide page 12). Other core courses own those boxes.
- The course title uses "planning" in the everyday sense: annual and quarterly planning, roadmaps. Only row 08 (retained) sits in the Planning category.
- The workbook names Capability 2 "Strategic Direction".

| Option | What changes |
| --- | --- |
| 1. Rename | For example "Advanced AI for Product Strategy and Roadmaps" or "... for Strategic Direction". Changes the PRD topic name |
| 2. Keep and explain (recommended) | Keep the title. Add one line to the spec and description: "Planning here means annual and quarterly product planning. The course maps to Capability 2, Strategic Direction." Learner text tags rows by box |
| 3. Keep with no note | No change |

Recommendation: option 2. Reason: the PRD uses the title and the meaning is common. Add the question to the Pragmatic review that already holds Stage 2; a rename is cheap before Stage 3.

### h) Model row for this course

Facts:

- No course-specific worked example row exists. mr-wf-01 (v3) was the model for depth and format (`status.yaml`: "Dan to confirm at Gate 1").
- Stage 2 needs an anchor row from this course.

| Candidate | For | Against |
| --- | --- | --- |
| sp-wf-02 rescoring (recommended) | Passes on 2 signed 2026 sources (W25, W26). Internal PM context (N12). Planted error lives in the data. Uses the numeric methods (S1 sheet, S2 sensitivity, S4 consistency) that modules 3 and 5 reuse. No merge pending | Needs decision d applied first. Sources are vendor or vendor-run |
| sp-wf-09 with 01 folded in | Strongest bottleneck (W1, W22). Module 1 row | Merge and PS-01 open. Planted error needs the critic fix |
| sp-wf-05 with 03 and 11 | Richest row; hardware path | Bottleneck only partly passes (W15, 2024) |

Recommendation: approve sp-wf-02, with decision d applied, as this course's model row at Gate 1. Reason: it is the cleanest row that exercises the numeric checks every later lab reuses. Claude Code drafts it as `worked-example-row.yaml` for your approval; mr-wf-01 stays the format model.

### i) Sources: Pragmatic list, age flags and N21 fieldwork

| Item | Facts | Recommendation |
| --- | --- | --- |
| Focus 28.01 draft v6 and Build 28.01 draft v1 (project files root, both 2026-11-19) | Used for the no-repeat and alignment checks. "Proposed, Dan to confirm" in `status.yaml` | Add both to the Pragmatic source list, pinned to these versions. Recheck when the final versions arrive |
| N21 State of Product Management 2026 | Published 2026, fieldwork Q4 2025. Rule 4 says "published in 2026 or later". N3 (Product Focus, fieldwork Oct 2025 to Jan 2026) was accepted the same way in Market Research | Accept under rule 4. Always state "fieldwork Q4 2025" with the figure |
| W15 (2024-02-12) | Only source for "business cases go stale" (row 05) | Keep, with the age flag shown |
| N23 (ms.date 2025-10-21) | One of 3 internal platform funding sources | Keep |
| W9 (2025-04-21), W10 (2023) | Row 03, now folded into 05. W7 and W8 carry the bottleneck | Drop |
| W21 (2019), W24 (2023) | Not verified. Not needed for a bottleneck | Drop |
| N2 (Pragmatic roadmap article, 2024-07-30) | Method only. Lists RICE and other methods Focus does not teach (PS-15) | Keep for method only. Not on a slide |
| E11 (IBM, 2024-05-14) | NV, vendor, no results | Talk track baseline only, no RICE on a slide (PS-15) |
| E8 (Deloitte Canada 2025-11-25; Australia part October 2025) | NV, one secondary source | Do not use until a second source is opened |
| Bond facts: Commonwealth Bank (2025-08, 15 months), Apple Siri delay (2025-03), Intel (1985; NPR page 2012) | Story sources, not statistics | Your call with decision k |

Recommendation: as in the table. Reason: keep only aged sources that carry a claim no 2026 source covers.

### j) Fallback case company

Facts:

- House rule 4: one fallback case company serves the whole course. The course is standalone, so the case must work without Market Research.
- Larkspan Systems (Market Research case) makes wireless temperature sensors and hubs (hardware), sells Larkspan Cloud (SaaS) and has an internal platform team (Fleet Data Platform). Its pharmacy segment has no patient data in the product.
- That fits the priority contexts here: hardware gates (row 11), shared firmware capacity (row 09 planted error) and an internal PM.
- Names to avoid: BadgeWorks, Entrilo, FieldPro (workshops); DeepView AI, PulseVision, FieldAssist (Focus 28.01).

| Option | What changes |
| --- | --- |
| 1. Reuse Larkspan Systems (recommended) | New strategy-year data: Strategy Matrix, backlog with scores, business case, gate package, roadmap and release plan, metrics export. Learners who took Market Research see continuity. No repeated exercise |
| 2. New company | More build time. Must avoid the 6 names and be hardware-capable for row 11 |
| 3. Larkspan, renamed | Same data shape, new name. Loses the continuity |

Recommendation: option 1. Reason: it already holds hardware, software and internal PM, and it saves case build time at Stage 2.

### k) Bond story (decision 39)

| # | Candidate | Sets up | Verifier status | Limits |
| --- | --- | --- | --- | --- |
| 1 | "Trendslop": LLMs give strategy advice that steers every company to the same trends (HBR, 2026-03-16) | Strategy stays a forced, human choice | PV | Esade and NYU Stern confirmed; University of Sydney not checked. Hook must say "thousands of runs", not "15,000 times". Percentages only in a third-party copy |
| 2 | Apple's personal Siri: shown, advertised, delayed, 250 million USD settlement | The roadmap is direction, not a promise | PV | "Still not shipped as of May 2026" is not in the source. Settled with no admission of wrongdoing. AppleInsider not opened |
| 3 | Commonwealth Bank: 45 roles cut on an AI business case, then reversed | A business case claim needs a check against operating data | V (2 sources) | 15 months old: your call. Job cuts and a union: keep to the assessment error |
| 4 | Intel leaves memory chips: "What would the new guy do?" | A forced choice against the business you love | V (NPR only opened) | 1985. Stanford case not opened by the verifier |

Facts: Trendslop is also ledger E3. House rule 9 forbids a repeated slide, so it cannot be both the bond story and a module slide.

| Option | What changes |
| --- | --- |
| 1. Hold the pick (as in Market Research) | Candidates stay in `bond-stories.md`. You pick before the module 1 deck (Stage 3). Stage 2 keeps E3 off module slides until you pick |
| 2. Pick Trendslop now (recommended if you pick now) | Bond story with no numbers. No module slide uses E3; module labs use E1, E2, E16, E17 for the risk points |
| 3. Pick another candidate | E3 is free for a module slide, numbers only after a licensed HBR read |

Recommendation: option 1, with a lean to Trendslop. Reason: the pick is not needed until Stage 3, and holding it keeps E3 free until the module plan is set.

### Other alignment items (quick yes or no)

| Id | Item | Recommendation |
| --- | --- | --- |
| PS-05 | Row 08 uses "Now, Next, Later" and treats "Q2" as a false commitment. Pragmatic allows dated roadmaps; the test is the release plan | The brief names the PM's own timeframes. Check: flag any date, "will ship" or "committed" not on the approved release plan. New planted error: "ships in Q2" for an item not on the release plan |
| PS-06 | Row 03 uses "layer" and "bottom-up" with meanings that clash with the Focus bubbles; Focus has a Market Sizing demo agent | Build the model on the 4 Focus bubbles. Projected share comes only from the PM's internal data (hand-off rule). Rename the error "scope mismatch". You confirm how it differs from the Focus demo agent |
| PS-09 | Row 07 trace repeats a Focus one-pass use case and says "validated problem backlog" | Use "Market Problems Table" and "strategy filters". The lesson is the per-item evidence audit and the refresh |
| PS-10 | Row 08 overlaps skill 3.4 (Build) | Keep the 2.4 tag. Scope to roadmap changes. Hand-off rule: a change to the release plan goes to the PM and the delivery team |
| PS-11 | E9 "a human override made the AI worse" vs human-owned priorities | Do not cite E9 (draft, permission needed). Ask the authors. If they agree, revisit for the override log talk track |
| PS-13 | Row 02 box tag: Product Portfolio vs 2.2 primary box Competitive Landscape | Keep Product Portfolio. Record "skill 2.2, primary box Competitive Landscape" in the spec |
| PS-14 | Row 10 title reads as if the agent recommends investment changes | Retitle as in section 1 |
| PS-15 | RICE (E11, N2) and a competitor report (E10) | No RICE and no E10 on a slide. Focus model is the default |
| PS-16 | Row 01 maps work to generic "strategic choices" | Strategy Matrix boxes (or the learner's equivalent) and OKRs are the inputs. More than 4 funded boxes goes to the flag report as "peanut butter" risk |
| PS-17 | Issues inside Pragmatic decks (two names for the third bubble, "[AI USE CASE TT]" blocks, dated vs undated roadmaps) | Use the 2027 guide and workbook for terms. You pass the issues to the Focus owner. Do not edit Pragmatic files |
| Verifier wording | E1, E2, E3, E7, E9, E13, E16, N5/N21, W14 | Applied in the brief (section 3). Yes to keep them in all later stages |

## 3. Suggested module order (autonomy ladder, suggestion only)

PRD decision 35: hand-run batch, then a scheduled agent with a flag report, then agents that hand work to other agents. You try the ladder at Gate 2. The order also follows Focus 28.01: Strategy, Score, Propose, Communicate, then results.

| Module | Rows | Skill | Rung | What the PM gives up | Planted error | Warning | Learner evidence (decision 42) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 09 (+ 01 drift section) | 2.1 | Build the agent from a template. Hand-run on one quarter. PM reads every flag | Stitching team submissions and capacity sums | Shared team under two names, 200% across programs | Told | Tuned brief, flag report decisions, audit of 2 shared teams |
| 2 | 02 | 2.2 | Hand-run each cycle. Reruns with new evidence. PM reads flags and audits 3 items | Drafting scores, sensitivity math, override log | One request counted under two attributes | Hint | Brief with PM-set ranges, override log, audit trace |
| 3 | 05 (+ 03 input, + 11 hardware path; 06 stretch) | 2.3 | Event-driven reruns. Market size refresh by web search is stretch | Keeping the register and the arithmetic | Stated-interest survey used as adoption evidence (or quote volume tier on the hardware path) | Hint | Assumption register, red-team flags, audit of 2 top assumptions |
| 4 | 07 + 08 | 2.4 | Output faces other people under hand-off rules | First drafts of the impact note and audience notes | "Ships in Q2" for an item not on the release plan | Hint | Decision log, commitment guard flags, side-by-side audit |
| 5 | 10 | 2.3 | Monthly run. Reads the module 3 baseline: one agent part hands work to the next. Schedule is stretch | Pulling and comparing measures | Output metric reported as the key result | None | Outcome report, flags for the investment review, audit of 2 "on track" measures |

Limits:

1. Schedule features are not verified on any platform, so the scheduled rung is a stretch step. CAW-AI already teaches scheduled tasks: use new slides.
2. With one course agent, "agents that hand work to other agents" means a hand-off between parts of the same agent (module 3 to module 5). Gate 2 must define it.
3. Planted errors for modules 3 and 4 need one choice each at Gate 2. Each lives in the case data, not in agent behavior.

## 4. Evidence strength in plain words

- PMs give little time to strategy. N21 (V; nearly 250 product professionals, fieldwork Q4 2025, vendor-sponsored): 72.2% spend 25% or less of their time on product strategy. N3 (V by the Market Research verifier, not reopened; 677, mostly Europe): 25% spend most of their time on strategy.
- Priorities get overridden. N21: 60.2% name leadership escalations or new directives as a factor that most often overrides their prioritization framework. That is a share of respondents, not of frameworks. W25, W26, W27 (V) describe the burden in words; their numbers are not independent or are illustrative.
- Bottlenecks rest on vendor or vendor-run sources with little data. No retained row has a non-vendor 2026 bottleneck source with data. PRD decision 37 accepts this for now.
- The strongest 2026 evidence is about AI risks. E1 (V, vendor RCT, one task): analysts chose the agent's lean on 86% of analytical decisions; final recommendation 54% vs 36%. E2 (V, Science, personal advice domain): AI affirmed users 49% more often than humans, and users trusted the agreeing answers more. E16 and E17 (V, abstracts, not PM tasks): people pull their own numbers toward an AI number.
- Trendslop (E3, PV) is a strong idea with weak numbers. In tests on ChatGPT, adding context shifted biased answers by about 11% (from a third-party copy of the article). No number goes on a slide until a licensed copy of the HBR article is read.
- No named company shows a measured AI gain in strategy work. E13 cannot be traced. E9 is a draft that may not be cited.
- Hardware has real but qualitative evidence (N10, N11 V). Internal platform funding has 3 sources (N12, N22, N23 V). Health care, services and manufacturing have no PM task data.

## 5. The 7 checks of the Gate 1 acceptance test

| # | Check | Synthesizer view | Files to open |
| --- | --- | --- | --- |
| 1 | Research supports a full course | Pass. 6 distinct rows for 5 modules, each with input, bottleneck, output and PM decision. Hardware: row 11 core, rows 09, 07, 08 partial. Internal PM: row 02 (N12), funding sources N22, N23. Gaps recorded per row | `workflows.yaml`, `rerun-track-1.yaml`, `critic-report.md` section 1, `gaps.md` |
| 2 | Bottlenecks are real (pick 2 rows) | Suggest rows 09 (W1, W22) and 02 (W25, W26). Both pass with 2 independent 2026 sources. All four are vendor or vendor-run | `workflows.yaml` (W1, W22), `rerun-track-1.yaml` (W25, W26), `verifier-report.md` "Bottleneck check" and "Two-source check for the bottlenecks" |
| 3 | Each row teaches PM judgment (same 2 rows) | Pass. Each names agent work, the PM decision and one AI error in the data | `workflows.yaml` fields `split`, `pm_decides`, `ai_error_to_catch` |
| 4 | Brief kept the evidence | Suggest: statistic N21 72.2% (p. 39; check population "nearly 250 product professionals" and period "fieldwork Q4 2025"); claim "hardware commit cost rises steeply after tooling" (N10, N11, independent); tool claim cg-09 "ChatGPT Work is not on Free or Go" (release notes, 2026-07-09 entry) | `research-brief.md` section 3, `rerun-track-3.md` (N21), `rerun-track-1.yaml` (N10, N11), `platform-matrix.yaml` (cg-09), `verifier-report.md` |
| 5 | Lab possible on all four platforms | Plausible on paper. Open and recorded: Gemini code, file and search in skills; Copilot embedded files and toggle; ChatGPT file output plan (decision f). Proof at Gate 2 | `platform-matrix.yaml`, `rerun-track-2.yaml`, `methods.md`, `research-brief.md` section 4 |
| 6 | Alignment used the right Pragmatic material | Sources and versions are in `alignment-log.yaml` `sources_used`. Focus and Build drafts need your yes (decision i). Traced example: row 08 `pragmatic_fit` against workbook 2.4 AI text and Focus slide 112 notes (match). Gate 2 follow-ups: Mastering the Product Roadmap syllabus, Focus Implementation Playbook and two workshops (not in the project folder) | `alignment-log.yaml` (`sources_used`, `traced_example`, `sources_not_read`), `status.yaml` |
| 7 | Decision possible from the packet | Pass. 4 rows earn retain with a passing bottleneck (02, 07, 08, 09). 05 and 10 are conditional (decisions a, i). No retained row depends on an open question that breaks its bottleneck, PM decision or platform path | This packet, section 1 |

## 6. Gaps left after the rerun

| # | Gap | Status |
| --- | --- | --- |
| 1 | 2026 named-company case with a measured AI result in strategy work (G4-2) | Open. Your client stories fill story slots (decision 43) |
| 2 | Non-vendor 2026 bottleneck source with data, any row | Open |
| 3 | Row 05: 2026 product-team source on stale business cases | Open. Rests on W15 (2024) |
| 4 | Row 10: product-team source on outcome tracking against the baseline | Open. W23 is public sector |
| 5 | Row 11: source that the gate package check is manual cross-document work | Open. Sentence becomes an assumption |
| 6 | Hardware: time for gate reviews or hardware roadmap updates (G3-4) | Open. N24 is one qualitative source |
| 7 | Internal PM: funding of internal platforms (G3-5) | Closed (N12, N22, N23) |
| 8 | Internal PM: annual planning calendar and time data | Open |
| 9 | People anchoring on an AI score in a PM prioritization task (G4-4) | Partly closed (E16, E17, not PM tasks, no effect sizes) |
| 10 | Roadmap update frequency figure (G3-1) | Open. Proxy: priorities change after agreement, 3.3 of 5 (N21) |
| 11 | E3 trendslop numbers (G4-11) | Open. HBR paywall |
| 12 | E9 permission to cite | Open. Ask the authors |
| 13 | Gemini skill code, file output and search (G2-1 to G2-3, gm-15) | Open. Gate 2 proof, Sheet fallback |
| 14 | Copilot code interpreter on embedded files; toggle vs "always enabled" (mb-15) | Open. Gate 2 proof |
| 15 | ChatGPT Project file count (25 in cg-01, 20 in cg-03); MR-E9 not rechecked | Open. Use 20 |
| 16 | Schedule features on all platforms | Not verified. Stretch only |
| 17 | Workbook AI text with no row: AI unit economics, pressure-test moats, sequencing scenarios | Open. Talk track or Gate 2 |
| 18 | Health care, services, manufacturing PM task data; FinTech single vendor source (N6) | Open |
| 19 | MNPI outside financial firms (G3-10) | Open. Legal review before any slide |
| 20 | Request intake and triage (needs T7) has no row | Open. Not a lab candidate in this run |
| 21 | Primary reports not opened: Atlassian whitepaper (W2), Anthropic full paper (E1) | Open. Open before a slide |
| 22 | No study compares agent-manager methods (G2-13) | Open. Teach as practice |

## 7. After you decide

1. You mark each row and answer a to k in the doc.
2. Claude Code applies your answers to the repo files, not to the doc. It records them in `research/gate-1-decisions.md`.
3. Changes to an approved item (decision e, the PA-03 note) happen only after your yes.
4. If your answers change the brief, the Verifier runs its trace check again on the changed parts.
5. You say "Gate 1 approved". Claude Code updates `status.yaml`.
6. Stage 2 still waits. It starts only after Pragmatic's feedback on the Market Research syllabus, even with Gate 1 approved.
7. Before Gate 2, these items need an owner: your comparison of the Focus and Build demo agents with rows 01 and 08; the Mastering the Product Roadmap syllabus; a licensed HBR copy for E3; the E9 authors' permission; the W2 and E1 primary reports.
8. Add a row to `logs/hours-log.csv` for this session.

## 8. Trace check flags (Verifier, after the Synthesizer)

The Verifier checked about 140 claims in this packet and the brief. It made 8 wording fixes. No recommendation changed. These 7 items need your eye:

| # | Flag | What it means for you |
| --- | --- | --- |
| 1 | Row 05 rests on W15 (2024) for "cases go stale" | If you drop W15 in decision i, the row 05 bottleneck fails check 7 |
| 2 | Row 10: "few teams compare results with the baseline" has no source | Retain only with the reworded bottleneck ("warning signs include ...") |
| 3 | Gemini skill limits come from an undated page (gm-01) | The dated vendor doc rule is met only in part. Gate 2 proof covers it |
| 4 | Claude help pages show only relative dates | Record the access date at Gate 2 |
| 5 | rerun-track-1.yaml marks W6 "verified", but the Verifier did not open it | The packet and brief treat W6 as not verified |
| 6 | All 4 bottleneck sources for rows 02 and 09 are vendor or vendor-run, with no time or cost data | You decide if this is enough (PRD decision 37 accepts thin evidence) |
| 7 | The brief calls E1 the strongest design evidence, but only the summary page was opened | Open the full paper before any slide uses E1 |
