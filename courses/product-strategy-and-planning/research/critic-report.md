# Research critic report: Advanced AI for Product Strategy and Planning (Stage 1, run 1)

- Course id: `product-strategy-and-planning`
- Written 2026-11-22 by the research critic.
- Files checked: workflows.yaml (sp-wf-01 to 10), needs.md, evidence-ledger.yaml, sources.yaml, methods.md, platform-matrix.yaml, bond-stories.md, gaps.md.
- Scope: coverage and depth only. The Verifier checks if each claim is true.
- Web use: 2 searches, no page fetches.

## 1. Answers to the 12 questions

| # | Question | Result | Why |
| --- | --- | --- | --- |
| 1 | Can the inventory support 4 to 6 distinct workflows, each with input, bottleneck, output and PM decision? | Pass | 10 rows, each with all four parts. After merges (section 3) about 6 distinct workflows stay. That is enough for 5 modules |
| 2 | Are key workflows missing? | Concern | 3 gaps between track 3 and track 1. (a) Request intake and triage against the plan (needs.md T7, ranked 5th by time pain) has no row. (b) The hardware stage-gate commit check (T10, N10 and N11 verified, a priority context) has no row. (c) Workbook 2.4 names "simulate sequencing and dependency scenarios". No row does this; methods.md S3 has the method but no workflow uses it. Annual planning (T4, T8) is covered only in part by sp-wf-09 |
| 3 | Do sources lean on vendor marketing? | Concern | Most bottleneck sources are vendor or consultancy blogs with no data: W1/W2 (Atlassian on its own study), W4 and W5 (unsigned vendor sites), W6, W7, W8, W16, W20, W22. Only N3 (Product Focus 2026) has a stated sample and method. No survey statistic in workflows.yaml is fully verified. Track 4 is better: E1 to E6 and E9 are studies |
| 4 | Does each workflow show a real bottleneck, not only an AI feature? | Pass, with 3 weak rows | sp-wf-01, 02, 07, 08, 09 describe a recurring human burden. Weak: sp-wf-06 (W16 and W17 argue a cost view, not a recurring PM burden; repetition is low to medium). sp-wf-03 (both sources sell market data; one market, quantum). sp-wf-10 (W23 is public sector benefits review, not product teams) |
| 5 | Did research look for hardware and internal PM examples, and record gaps? | Pass, with a link gap | Gaps are recorded per row and per track. But track 1 did not use what track 3 found: N12 (SiriusXM platform team, prioritization, verified) is a strong internal PM source for sp-wf-02, which says "gap". N10 and N11 (hardware commit cost, verified) are not linked to sp-wf-05 or sp-wf-06. E11 (IBM, internal, 2024, aged) is not linked to sp-wf-02 |
| 6 | Does each row have one specific AI error that the agent's own checks miss and the audit finds? | Concern on 3 rows | Each row names one error. In sp-wf-07, 08 and 09 the row's own hand-off rule should catch the planted error, so the audit is not needed. sp-wf-09: rule "a shared team asked for more than its capacity across programs" finds the 200%. sp-wf-08: rule "any note that needs a date the roadmap does not hold" finds "Q2". sp-wf-07: rule "an item whose evidence is below the validated rule" finds the weak item. Fixes in section 2 |
| 7 | Does any row repeat a registry item or reteach a workshop module? | Pass, 3 risks for Dan | No row reuses a CAW-AI agent, the Competitive Intel Watchdog or a workshop exercise. Risks: sp-wf-01 is close to the Focus 28.01 tip "check roadmap updates against the Strategy Matrix and OKRs". sp-wf-08 audience notes are close to Focus "one roadmap, two audiences" and Build 28.01 AI stakeholder updates. The brief template is close to PRW-AI "JOB AND CONTEXT, RULES, OUTPUT" (registry note: refer to it, do not reteach) |
| 8 | Is a no-connector core lab plausible on all four platforms? | Concern | Text-only rows (05 red-team, 07, 08) are plausible on all four. Numeric rows (01 totals, 02 sensitivity, 03, 06, 09 sums) need code. No doc says a Gemini skill runs code (gm-11). ChatGPT file output needs Plus or higher (cg-09). Every row's platform line cites Market Research ledger E6, E8, E9, which this run did not re-verify |
| 9 | Does each row start where Focus 28.01 one-pass AI activities stop, and is it stronger than CAW-AI and AI Agents? | Pass, with 2 concerns | All rows add checks, hand-off rules, an audit and runs over time, so they start where Focus stops. All are stronger than CAW-AI (no competitor watch, real numeric checks). Concerns: (a) the AI Agents course maps to skill 2.2, and no file checks if its labs score opportunities (sp-wf-02 says "check"; not done). (b) sp-wf-01 and sp-wf-08 need Dan's call (question 7) |
| 10 | Do the rows cover skills 2.1 to 2.4 for 4 to 6 modules, and is any row out of scope? | Concern | 2.1: rows 01, 09. 2.2: row 02 only. 2.3: rows 03, 05, 06, 10 (heavy). 2.4: rows 07, 08. Skill 2.2 is thin: one row, weak sources, and its primary box (Market / Competitive Landscape) is not covered. That is deliberate (CAW-AI overlap), but the gate packet must say so. Out of scope: sp-wf-04 (skill 6.4, Framework "Planning / Ideation"). sp-wf-08 is tagged with the Framework "Planning" category (Stakeholder Management). Its skill (2.4E) is in scope, so the tag is fine, but the packet must explain the name collision |
| 11 | Which rows overlap enough to merge? | Concern | sp-wf-01 and sp-wf-09: same inputs (work export, capacity, strategy choices), same cadence, same audience. Merge. sp-wf-03 feeds sp-wf-05: the size model is the market assumption set of the case. Merge into one business case module. Optional: sp-wf-05 and sp-wf-10 close one loop (case to outcomes), and sp-wf-07 and sp-wf-08 share the roadmap. Keep those apart unless the course needs fewer modules |
| 12 | Does each planted error live in the data, so a case builder can plant it and the audit finds it? | Pass on 7 rows, concern on 3 | In data: 01 (epics with theme tags and maintenance descriptions), 02 (one request cited under two attributes), 03 (two layer-mismatched estimates in the source pack), 04 (test plan n=12, notes for 7), 05 (stated-interest survey as adoption evidence), 07 (one sales request in a strong theme), 10 (output metrics named like the key result). Concern: 06 depends on agent behavior (costing from a prototype). Plant a prototype effort log and leave run-cost rates out of the vendor pack. 08 depends on agent behavior (copying dates from past notes). Plant past sales notes with quarter dates in the decision log. 09 is in data but the hand-off rule finds it (question 6) |

## 2. View per row

| Row | Workflow (short) | View | Why (one line) |
| --- | --- | --- | --- |
| sp-wf-01 | Quarterly strategy drift check | Merge into sp-wf-09 | Same data and cadence as 09. Keep "label laundering" as the planted error of the merged row: it lives in the data and the checks miss it |
| sp-wf-02 | Re-score opportunity backlog with sensitivity and consistency | Retain | Only 2.2 row and the clearest agent-manager lab. Bottleneck sources are weak (W4, W5 unsigned); link N12 and rerun track 1 |
| sp-wf-03 | Sourced market size model (from mr-wf-06) | Merge into sp-wf-05 | The size model is the market input of the business case. Alone, it repeats the Market Research shape and has data-vendor sources only |
| sp-wf-04 | Concept test results per hypothesis (from mr-wf-08) | Reject for this course (defer to the Design course) | Skill 6.4 and Planning / Ideation are out of scope. The bottleneck is a weak pass |
| sp-wf-05 | Assumption register and red-team before each decision | Retain | Exact fit with the 2.3 AI text. Lead row of the business case module with 03. Needs a 2026 product-team bottleneck source (W14 is valuation staff, W15 is 2024) |
| sp-wf-06 | Buy, build or partner option pack | Defer | Low repetition and high judgment make it a weak agent workflow. The bottleneck is a cost argument. Could be a stretch inside the 05 module |
| sp-wf-07 | Quarterly roadmap theme refresh with trace to evidence | Retain, fix the error | Exact fit with the 2.4 AI text. Fix: the hand-off rule finds the planted item. Make the weak item cite a problem id that is validated but unrelated, so the trace looks valid |
| sp-wf-08 | Roadmap change impact and audience notes | Retain, fix the error | Highest repetition and tests the 2.4 "false commitment" line. Fix: plant "early Q2" inside a quoted customer line, or "Next (targeting spring)", so the date check passes. Dan must confirm the Focus and Build overlap |
| sp-wf-09 | Quarterly portfolio review pack | Retain as lead of the 01 and 09 merge, fix the error | Strong bottleneck with hardware detail (W19, W22). Fix: name the shared firmware team two ways ("FW Platform" and "Firmware Core") in the submissions, so the per-team sum misses it and the audit finds it |
| sp-wf-10 | Monthly outcome tracking against the business case | Retain | Clear error in the data and closes the loop with 05. Needs a product-team source (W23 is public sector) |

Result: 5 module candidates. Portfolio and drift review (09 + 01), opportunity rescoring (02), living business case (05 + 03), roadmap refresh and change (07, 08), outcome tracking (10). This meets the Gate 1 test 7 (at least 4 rows earn retain).

## 3. Other findings for the Synthesizer

1. Every row's data safety note says "Get consent before you record an interview. Agree confidentiality for win/loss." That text comes from Market Research and does not fit these labs. Use the strategy data risks in needs.md (unreleased roadmaps, forecasts, MNPI, supplier costs, employee data).
2. W1 and W2 give different wording for the 11% figure. W2 has no publish date. A search shows a second Atlassian report ("State of Strategy report") on the same site. It is the same vendor, so it does not count as an independent source.
3. W14 polls valuation practitioners, not PMs. Do not present it as a PM statistic.
4. Bond story candidate 1 (trendslop) also appears as E3 in the ledger. If a lab slide uses E3, the opening cannot use it again (house rule 9).
5. Hours split check: four of ten rows map to 2.3. After the merges, each skill has at least one module. Skill 2.2 still has only one.

## 4. Gaps for rerun

Each ask fits about 10 web fetches. Each track reruns one time only.

| Track | Ask |
| --- | --- |
| 1 | For sp-wf-02, find 2 independent, dated 2026 sources (not unsigned vendor pages) that describe scoring inconsistency or overrides as a recurring burden. Link N12 (SiriusXM) as the internal PM context. Leads: Mind the Product "Product People on Prioritisation", Product-Led Alliance "4 prioritization challenges", Pragmatic "Managing Internal Feature Requests" |
| 1 | Draft one new row sp-wf-11: the hardware stage-gate commit check (needs.md T10). Use N10 and N11 as 2 bottleneck sources. Map it to skill 2.3 or 2.4, name a planted error in the data, and fill the hardware and internal PM fields |
| 2 | Find one dated Google doc that says if a Gemini app skill can run code or produce a file. If none exists, record the gap and name the Gate 2 fallback (sheet with formulas) |
| 2 | Re-verify the 3 Market Research ledger features that every row cites (E6 Copilot embedded files, E8 Gemini skill, E9 ChatGPT Project) with current dated vendor pages. Add mb-13: can Copilot code interpreter read an embedded .xlsx |
| 3 | Open the ProductPlan State of Product Management 2026 report (N5) and the Product-Led Alliance State of Product Management 2026 survey (primary for W3). Record sample, dates and method, the "three hidden time sinks", and any figure on prioritization overrides or roadmap change frequency |
| 3 | Find 1 second internal PM source on annual planning or funding of internal platforms, and 1 hardware source on how long stage-gate business cases or roadmap updates take. Leads: airfocus platform PM article, PDMA, Deloitte semiconductor PM lead |
| 4 | Find one 2026 named-company case of AI in quarterly portfolio or roadmap planning with a measured result. Find the original publisher of E13 (SAP) or confirm it cannot be traced. Open the Dragonboat Fortune 500 bank story and mark it vendor |
| 4 | Open arXiv 2603.28944, arXiv 2603.11821 and Journal of Management Studies 63(2) 2026. Record if any shows people anchoring on an AI score or ranking (supports sp-wf-02 and the trace-to-source method) |
