# Research brief: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`
- Stage 1, run 1, with one rerun of tracks 1 to 4. Written by the Synthesizer on 2026-11-22.
- Inputs: all files in `courses/product-strategy-and-planning/research/`: workflows, rerun tracks 1 to 4, needs, methods, platform matrix, evidence ledger, sources, bond stories, gaps, critic report, alignment log, verifier report (both sections), stage 1 inputs.
- Rule for this brief: each claim cites an id with status "verified" (V) or "partly verified" (PV). Items with status "not verified" (NV) are named only as gaps or exclusions. Each source keeps its limits.
- The Gate 1 decision table and the decision list are in `gate-1-packet.md`.
- Hold: Stage 2 does not start until Pragmatic reviews the Market Research syllabus. Its feedback can change structure or skill mapping for every course (`status.yaml`).

## 1. Summary

1. The research supports 6 distinct workflows for 5 modules: portfolio review pack with drift (09 + 01), opportunity rescoring (02), living business case (05 + 03, with a hardware path from 11), roadmap refresh and change (07 + 08), and outcome tracking (10). Each maps to Capability 2, Strategic Direction, skills 2.1 to 2.4.
2. Bottleneck evidence is thin and leans on vendors. Rows 01, 02, 03, 06, 07, 08 and 09 pass the 2-source rule (02 after the rerun; 07 and 08 weak). Rows 04, 05, 10 and 11 pass only in part. No row fails. No retained row has a non-vendor 2026 bottleneck source with data.
3. The strongest 2026 evidence is about AI risks, not AI gains: people follow an agent's lean (E1, vendor), prefer agreeing answers (E2, Science), and pull their own numbers toward an AI number (E16, E17). No named company shows a measured gain from AI in strategy work (gap G4-2).
4. A no-connector core lab is possible on all four platforms on paper, but numeric steps carry risk. Gemini skills have no dated doc for code, files or search. ChatGPT spreadsheet output with formulas is documented only for ChatGPT Work. Copilot code output lasts for one session only.
5. Three high alignment conflicts need Dan's call: the drift row repeats a Focus 28.01 demo agent (PS-01), change notes repeat a Build 28.01 demo agent (PS-02), and the scoring model must not differ from Focus (PS-03). The data safety note for strategy work changes the PA-03 note Dan approved (PS-12), so it needs his yes.

## 2. Recommended workflows and why

The critic's view and this brief agree on the set. Dan decides each row.

| Row | Recommendation | Why |
| --- | --- | --- |
| sp-wf-09 Quarterly portfolio review pack | Retain. Lead row of module 1, with 01 folded in | Passes on 2 independent 2026 sources (W1, W22). Hardware detail (W19, W22). Focus 28.01 does not cover portfolio packs. Fix the planted error so the agent's own hand-off rule does not catch it (critic) |
| sp-wf-01 Quarterly strategy drift check | Fold into 09 | Same data and cadence as 09 (critic). Close to a Focus 28.01 demo agent (PS-01). Drift by Strategy Matrix box becomes one section of the 09 pack (PS-16) |
| sp-wf-02 Rescore the opportunity backlog | Retain as its own module | Only skill 2.2 row. Passes after the rerun on W25 and W26 (both signed, 2026, vendor or vendor-run). Internal PM context N12. Planted error lives in the data |
| sp-wf-05 Assumption register and red-team | Retain with a condition. Lead row of module 3 | Exact fit with the 2.3 AI text. Bottleneck partly passes: W15 is from 2024 (age flag) and W14 is not a PM source. Dan decides if W15 stays |
| sp-wf-03 Market size model (from mr-wf-06) | Fold into 05 | The size model is the market input of the business case (critic). Use the 4 Focus bubbles (PS-06) |
| sp-wf-11 Hardware gate package check (new) | Fold into 05 as its hardware path | Same agent job as 05: check the case before a commit point. Partly passes (N10, N11). Hardware is a priority context |
| sp-wf-07 Roadmap theme refresh with trace | Retain. Share module 4 with 08 | Exact fit with the 2.4 AI text. Passes, weak (W19, W3). Only the per-item evidence audit and the refresh are new against Focus (PS-09) |
| sp-wf-08 Roadmap change impact and audience notes | Retain. Core of module 4 | Highest repetition. Tests the 2.4 rule on false delivery commitments. Passes, weak (W20, W19). Rescope per PS-02, PS-05 and PS-10 |
| sp-wf-10 Monthly outcome tracking | Retain with a condition | Closes the loop with 05. Planted error lives in the data. Bottleneck partly passes (W23 is public sector). Retitle per PS-14 |
| sp-wf-04 Concept test results (from mr-wf-08) | Out of scope as a lab | Skill 6.4 and Planning / Ideation belong to the Design course (PS-08). Bottleneck partly passes. Its denominator check can be one quality check in 05 |
| sp-wf-06 Buy, build or partner pack | Defer | Bottleneck passes (W16, W17), but repetition is low to medium and judgment is high (critic). Possible stretch step in module 3 |

Why this set works as one course:

- It follows the Focus 28.01 order (Strategy, Score, Propose, Communicate) and then measures results. Focus graduates see where each module starts.
- Each module reads from or writes to the same agent. Module 5 reads the business case baseline from module 3. This fits the one-agent rule (PRD decision 38).
- Each module has a planted error in the data, not in agent behavior.
- If Dan rejects 05 and 10 (both partly pass), rows 09, 02, 07 and 08 still give 4 retained rows. That meets Gate 1 check 7.

Design note from Dan's Market Research themes: no magic number. The rows and methods give example ranges (for example "scores differ by 2 or more", "moved more than 2 places", "plus or minus 10 points"). In this course the PM sets every range, tolerance and threshold in the brief. The agent reports the evidence against it.

## 3. Evidence strength

### Plain verdict

| Topic | Strength | Ids | Limits to keep |
| --- | --- | --- | --- |
| PMs give little time to strategy | Moderate. Two surveys, one vendor-sponsored | N21 (V), N3 (V, Market Research) | N21: nearly 250 product professionals, 43.3% leaders, fieldwork Q4 2025, published 2026, sponsored by ProductPlan, no method or response rate. 72.2% spend 25% or less of their time on product strategy. N3: 677 respondents, 83% Europe; 25% spend most time on strategy |
| Prioritization gets overridden | Moderate. One survey plus signed vendor essays | N21 (V), W25 (V), W26 (V), W27 (V) | Use this wording only: 60.2% of respondents name leadership escalations or new directives as a factor that most often overrides their prioritization framework (multi-select). It is not a share of frameworks. W25 and W27 repeat N21 figures, so they are not independent for numbers. W26 figures are illustrative |
| Strategy is not linked to the work | Moderate. One vendor survey and one vendor-sponsored survey | W1 (V), W3 (PV) | W1: Atlassian, 308 leaders, period not stated, primary whitepaper (W2) not opened. W3 is the N21 survey. Open the primary reports before a slide |
| Portfolio reviews take weeks of preparation | Weak. One quote | W1 (V) | Expedia "weeks of preparation" is one anecdote. W22 (V, vendor) adds stale decks and manual stitching, with no data |
| Business cases go stale | Weak | W15 (V, 2024, age flag), W14 (PV) | W14 is a KPMG webinar poll of valuation practitioners, not PMs, with no sample or date. It is not a PM statistic. Do not use it as a statistic |
| Hardware commits cost more at each stage | Moderate. Two signed 2026 practitioner sources | N10 (V), N11 (V), N24 (V, single) | No data on hours or cost. No source says the gate package check is manual cross-document work. N24 is one source on gate preparation burden |
| Internal platform funding is hard to win | Moderate. Three independent sources | N12 (V), N22 (V, vendor blog), N23 (V, age flag) | No time data. No source on the internal annual planning calendar |
| People follow an AI agent's lean | Strongest design evidence, vendor | E1 (V) | Anthropic RCT, 50 analysts, one task, one model, period not stated. Analysts chose the agent's lean on 86% of analytical decisions. Final recommendation: 54% vs 36%. Say "54% vs 36%", not "17 points" (raw gap is 18). The authors made the lean stronger than in real use |
| People prefer AI that agrees with them | Strong, peer reviewed | E2 (V) | Cite the Science version only (Science 391, eaec8352, 2026-03-26), not the preprint. 11 models, AI affirmed users' actions 49% more often than humans; 3 experiments, N 2,405. Domain is personal advice, not business strategy. Use for strategy only as an inference, and say so |
| LLMs give trend-aligned strategy advice ("trendslop") | Moderate, numbers not usable yet | E3 (PV) | Seven LLMs almost always picked trend-aligned options. The 11% context shift and "often recommended doing both" are ChatGPT results only: say "In tests on ChatGPT, ...". The under 2% result applies to the 2 strongest tensions only. Numbers come from a third-party copy. No number on a slide until a licensed copy of the HBR article is read |
| People pull their own numbers toward an AI number | Moderate, not PM tasks | E16 (V, abstract), E17 (V, abstract) | E16: 28 pathology experts, preprint. Moderate anchoring on the AI estimate, larger under time pressure. 7% is the automation bias rate: cases where wrong AI advice overturned a correct first judgment. Time pressure did not make this happen more often, but it made the errors worse. E17: peer reviewed (JMS), credit ratings drift toward the AI rating over repeated sessions; no sample or effect size in the abstract |
| LLMs anchor on numbers in the prompt | Moderate, abstract only | E4 (V) | ACL 2026. Open-weight Llama and Qwen models, not the chat products learners use. No effect size. Supports a "no target numbers in the brief" check |
| AI invents or breaks citations | Moderate | E6 (V, abstract), E7 (V) | E6: 3% to 13% of citation URLs were hallucinated; link existence only. E7: counts come from GPTZero (vendor) only. Say "KPMG said it removed the report" |
| AI ranks options better than experts | Not usable now | E9 | The arXiv paper is a draft. Its first page asks readers not to circulate or cite it without the authors' permission. Do not cite it or put it on a slide. Ask the authors, or wait for a published version |
| Measured AI gain in a named company | None | none | E11 (IBM, 2024, NV), E12 and E18 (Dragonboat, vendor, NV), E13 (SAP, untraceable, do not use). Gap G4-2 |

### Wording fixes applied (from the verifier)

| Id | Fix |
| --- | --- |
| E1 | Use "54% vs 36%". Do not write "17 points" or "18 points" |
| E2 | Cite Science only. Do not cite the arXiv preprint for these figures |
| E3 | ChatGPT-only results say "In tests on ChatGPT". Bond story hook says "thousands of runs", not "15,000 times" |
| E7 | "KPMG said it removed the report". GPTZero is named as the source of the counts |
| E9 | Draft. Not cited, not on a slide |
| E13 | Original publisher cannot be traced. Dropped for any use |
| E16 | 7% is the automation bias rate, with its definition. Time pressure made errors worse, not more frequent |
| N5, N21 | 60.2% is the share of respondents who name leadership escalations or new directives as an override factor |
| N5, W3 | One survey (N21). They never count as 2 sources |
| W14 | Not a PM statistic. Not used as a statistic |
| W5 | "Undocumented reasoning" is not on the page. Not used |
| N13 | Page title is now "Product Strategy Matters More In An AI-First World" (Xebia, updated 2026-11-05) |

### Excluded from claims

| Ids | Why |
| --- | --- |
| E9 | Draft, permission needed |
| E13 | Untraceable |
| E8, E11, E12, E15, E18, E19 | Not verified (budget). E11 is also from 2024 |
| W6, W13, W18, W21, W24, W28 | Not verified (budget). W21, W24 are also older than 12 months |
| W20 figures (41%, 27%) | No link or sample for the cited survey |
| W26 figures | Illustrative, unsourced |
| N2, N4 to N9, N14 to N19 | Not reopened by this verifier. N5, N7, N8, N16, N17 are weak vendor or analyst figures: keep off slides |
| E10 | Verified, but Product Institute is a Pragmatic competitor. Not on a slide (PS-15) |

## 4. Platform readiness

Core build with no connectors. Each line cites a platform matrix id and its status.

| Platform | Core build | Math in code | Spreadsheet out | Web search (market size refresh) | Main risk |
| --- | --- | --- | --- | --- | --- |
| Claude | Project or skill (cl-pj-01 V, cl-cl-03 V) | Code execution on all plans (cl-fo-06 V) | .xlsx, 30 MB (cl-fo-06 V). The page does not state formulas | All plans, inferred (cl-ws-08 PV). Team and Enterprise owners must turn it on | An org owner can turn off code execution. XLSX upload then fails (cl-up-10 V): ship a CSV copy. Upload size conflict: use 30 MB |
| ChatGPT | Project (cg-01 V) | Data analysis runs Python on uploads (cg-11 V). Plans not named | Documented only through ChatGPT Work (cg-09 V, cg-10 V). Work is not on Free or Go, and not in a project with project-only memory (cg-14 V) | All plans, Free to Edu (cg-13 V). Citations "may" be included | Download of data analysis output is not documented (cg-11). Default project memory can leak run 1 into a "blind" run 2 (cg-14) |
| Copilot agent builder | Agent with instructions (8,000 characters) and embedded files (mb-01 V, mb-02 V). License or pay-as-you-go billing (mb-03 V) | Code interpreter on files uploaded in chat (mb-13 V, mb-15 V) | Excel and other files, session only (mb-11 V) | 4 URLs or "Search all websites", all license states (mb-12 V) | No doc says code interpreter reads embedded knowledge files. One page says code interpreter is "always enabled" in Agent Builder (mb-15); another describes a toggle (mb-04). CSV is not allowed as embedded knowledge; one sheet per workbook (mb-14 V) |
| Gemini | Gemini skill in the Gemini app (gm-01 PV, gm-03 V, gm-13 V) | Not documented. Code files can be uploaded, but no doc says they run (gm-11 PV, gm-15 NV gap) | Gemini app makes files (gm-09 V, gm-14 V). From a skill: not documented | Not documented for skills. Deep Research does not work in skills (gm-06 PV) | Undated Help pages do not meet the dated vendor doc rule. Fallback for numeric steps: a Google Sheet with formulas |

What this means for the labs:

1. Text steps (red-team, trace, change notes, commitment guard) are plausible on all four platforms.
2. Numeric steps (sensitivity, sums, unit cost) need code on 3 platforms and a sheet with formulas on Gemini. One pattern can serve all four: the course sheet holds the formulas, and the agent writes the inputs and reads the results. This keeps calculations auditable (workbook 2.3).
3. The market size refresh is a stretch step on all platforms. The core path uses a source pack from the case.
4. Schedules are stretch only. All schedule features are not verified (cl-sc-07, cg-06, mb-06, gm-07). CAW-AI already teaches scheduled tasks.
5. The pre-class checklist (decision 44) adds: code execution on (Claude), web search on (Claude Team and Enterprise), Copilot license or billing, ChatGPT plan.

## 5. Pragmatic conflicts

Sources used by the alignment agent: Framework 2027 guide (created 2026-11-11), Capability Standards Workbook 2027 (modified 2026-11-22), Focus 28.01 draft v6 and Build 28.01 draft v1 (both 2026-11-19, project files root), the two Pragmatic course design docs, and two pragmaticinstitute.com pages. Focus and Build are not yet on Dan's named source list (packet decision i).

| Id | Severity | Conflict | Alignment recommendation | Packet item |
| --- | --- | --- | --- | --- |
| PS-01 | High | Drift row repeats the Focus 28.01 Strategy Alignment demo agent (slides 25 to 28) | Keep the new agent-manager parts; Dan compares his Focus demo agent with the row before Gate 2 | b |
| PS-02 | High | Change notes repeat the Build 28.01 Stakeholder Update agent and the Focus Roadmap Translator demo | Make the change assessment the core; per-audience notes are one short step | c |
| PS-03 | High | methods.md S1 says use criteria different from Focus | Use the 4 Focus attributes and the 1 to 5 scale | d |
| PS-04 | Medium | Agent scores could become final scores (Focus RED) | Label agent scores "draft scores"; final scores stay with the PM | d |
| PS-05 | Medium | "Now, Next, Later" and the "Q2" planted error | Use the commitment guard against the release plan | Quick table |
| PS-06 | Medium | Market size method and the word "layer" differ from the Focus bubbles | Build on the 4 Focus bubbles; rename the error | Quick table |
| PS-07 | Medium | Course title word "planning" vs Framework category "Planning" | Keep the title; add one line; ask Pragmatic | g |
| PS-08 | Medium | sp-wf-04 maps to skill 6.4, outside Capability 2 | Fold into 05 as one check, no lab | a |
| PS-09 | Medium | Roadmap trace repeats a Focus AI use case; non-Pragmatic input names | Use "Market Problems Table" and "strategy filters" | Quick table |
| PS-10 | Medium | sp-wf-08 overlaps skill 3.4 (Build) | Scope to roadmap changes; release plan changes go to a hand-off rule | Quick table |
| PS-11 | Medium | E9 "augmentation trap" vs human-owned priorities | Overtaken: E9 cannot be cited now (draft) | Quick table |
| PS-12 | Medium | Data safety note is the Market Research text | Strategy data note; changes approved PA-03 note | e |
| PS-13 to PS-17 | Low | Box tag for 02, title of 10, other scoring methods and a competitor source, Strategy Matrix as input, issues inside Pragmatic decks | See packet quick table | Quick table |

Not re-raised (Dan decided in Market Research): PA-01, PA-02, PA-03 core lines, PA-07, PA-08, PA-09, and the move of mr-wf-06 and mr-wf-08 to this course.

## 6. Capability mapping proposal

Capability 2, Strategic Direction: "how an organization turns market evidence into product strategy, prioritized opportunities, business cases, and roadmaps." Skill and competency names are the workbook names, as quoted in `stage-1-inputs.md` and `workflows.yaml`. No new standard or skill name is proposed.

| Skill (workbook name) | Primary box (workbook) | Rows | Competencies the rows name | Suggested module |
| --- | --- | --- | --- | --- |
| 2.1 Strategy Alignment | Product Strategy | 09 (skill objective: portfolio direction and resource allocation), 01 (2.1B Explicit vs. Implicit Strategy Analysis) | 2.1B | 1 |
| 2.2 Opportunity Prioritization | Competitive Landscape | 02 | 2.2C Weighting and Priority Logic, 2.2D Calibration and Consistency | 2 |
| 2.3 Business Case Development | Business Plan | 05 (2.3C Cost, Profit, and Resource Logic; 2.3F Stakeholder Argumentation), 03 (2.3B Market Value and Sizing), 11 (2.3C), 10 (2.3E Success Definition and Measurement) | 2.3B, 2.3C, 2.3E, 2.3F | 3 and 5 |
| 2.4 Product Vision and Roadmap | Product Roadmap | 07 (2.4B Roadmap Structuring and Framing; 2.4D Alignment to Market Problems and Strategy), 08 (2.4C Assumption and Uncertainty Transparency; 2.4E Stakeholder Communication and Alignment) | 2.4B, 2.4C, 2.4D, 2.4E | 4 |

Notes:

1. The Market Research mapping left skill 2.2 Opportunity Prioritization (Competitive Landscape box) to this course (`status.yaml`, gap 1). Row 02 covers 2.2. Its box tag is Focus / Product Portfolio, a listed 2.2 secondary box (PS-13). The Competitive Landscape box enters only as a scoring attribute. That is deliberate: CAW-AI owns competitor watch agents, and Dan rates them as weak builds.
2. Skill 2.3 gets 2 modules (3 and 5). Skills 2.1, 2.2 and 2.4 get 1 module each. Every skill has at least one module.
3. Workbook AI text with no row: "AI unit economics" (2.3), "pressure-test moats" (2.1 and Capability 2) and pricing. The Price core course owns Pricing. Dan decides if a talk track line covers the other two.
4. The 2.4 AI text names "simulate sequencing and dependency scenarios". Row 08's impact assessment covers dependency hits. No row simulates sequencing (critic). Gap.
5. Offering intent is Develop and Apply (decision 41). The development brief at Stage 2 answers the 5 questions per module (decision 40).

## 7. Gaps

Gaps left after the one-time rerun. A gap is not a failure. The packet, section 6, has the full table.

| # | Gap | Effect |
| --- | --- | --- |
| 1 | No 2026 named-company case with a measured AI result in strategy work (G4-2) | No impact slide. Dan's client stories fill the story slots (decision 43) |
| 2 | No non-vendor 2026 bottleneck source with data for any row | PRD decision 37 accepts thin evidence for now |
| 3 | Row 05: no 2026 product-team source on stale business cases | Rests on W15 (2024). Dan decides |
| 4 | Row 10: no product-team source on outcome tracking (W23 is public sector) | Reword to "warning signs include ..." |
| 5 | Row 11: no source says the gate package check is manual cross-document work | That sentence becomes an assumption |
| 6 | Hardware: no data on how long gate reviews take (G3-4) | Gate 2 designs the lab without a time figure |
| 7 | Internal PM: annual planning calendar and time data (G3-5) | Funding side is closed (N12, N22, N23) |
| 8 | People anchoring on an AI score in a PM prioritization task (G4-4) | Partly closed by E16, E17 (not PM tasks) |
| 9 | Gemini skill code, file output and search not documented | Gate 2 proof. Sheet with formulas as fallback |
| 10 | Copilot code interpreter on embedded files; toggle vs "always enabled" | Gate 2 proof |
| 11 | No study compares agent-manager methods (G2-13) | Teach as practice, not as a finding |
| 12 | Health care, services, manufacturing: no PM task data. FinTech: one vendor source (N6) | Data safety notes only |

## 8. Open questions for Dan

The packet lists each with options and a recommendation.

1. Rows: merge 01 into 09 and 03 into 05; 04 out of scope; 06 deferred; 11 as the hardware path of 05; 07 and 08 in one module (decision a)?
2. Did you build the Focus 28.01 Strategy Alignment agent, the Build 28.01 Stakeholder Update agent and the Focus Roadmap Translator? If yes, house rule 11 applies to rows 01 and 08 (decisions b, c).
3. Scoring model: Focus 4 attributes and 1 to 5 scale as the default, with draft scores only (decision d)?
4. Data safety note for strategy data: change the approved PA-03 note for this course (decision e)?
5. Platform risks: ChatGPT minimum plan, Gemini sheet fallback, Copilot upload in chat, live web search as stretch (decision f)?
6. Course title and the Framework category "Planning" (decision g)?
7. Which row is this course's model row (decision h)?
8. Sources: add Focus 28.01 and Build 28.01; age-flagged sources; N21 fieldwork in Q4 2025 (decision i)?
9. Fallback case: reuse Larkspan Systems or a new company (decision j)?
10. Bond story: pick now or hold (decision k)?
