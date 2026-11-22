# Research critic report: Advanced AI for Market Research

- Course: market-research
- Stage 1, run 1. Checker: Research critic (coverage and depth, not single-claim truth)
- Date: 2026-11-20
- Files read: workflows.yaml, needs.md, methods.md, platform-matrix.yaml, evidence-ledger.yaml, sources.yaml, gaps.md, run-log.md. Also CLAUDE.md, PRD "Research stage", shared/registry/registry.yaml, Pragmatic Framework 2027 guide (pages 3 to 8)

## Verdict in one table

| # | Question | Result | Short reason |
| --- | --- | --- | --- |
| 1 | Can the inventory support 4 to 6 distinct workflows? | Pass, with concern | 9 rows give 5 to 6 distinct workflows after merges. 5 rows use the same mechanic (code text against a list, then audit) |
| 2 | Are key workflows missing? | Concern | No Competitive Landscape row. The "where can we win" half of the Market question has no row |
| 3 | Do sources lean on vendor marketing? | Concern | Bottlenecks for rows 02 to 09 rest mostly on vendor blogs. All non-vendor bottleneck sources are older than 12 months |
| 4 | Does each workflow show a real bottleneck? | Concern | Rows 07 and 08 fail the 2-source test. Row 04 has no evidence that PMs do the task |
| 5 | Hardware and internal PM searched, gaps recorded? | Pass, with concern | Gaps are recorded. But track 4 hardware cases (E26, E27, E28) are not linked to the rows, so rows show "gap" where examples exist. Internal PM has no 2026 source |
| 6 | One specific AI error per row that checks miss and the audit finds? | Pass, with concern | Each row has one. Two errors depend on the model, not the data. Random audits of 3 items can miss a planted error |
| 7 | Repeats of the registry or a workshop? | Pass, with concern | Rows 01 and 02 are clear. Rows 04, 06 and 07 sit close to PDW-AI or MKT-2026 |
| 8 | No-connector core lab on all four platforms? | Pass, with concern | Upload-and-run works on paper for 8 of 9 rows. All 34 platform features are still "not verified". Carrying the log between modules is not proven off Claude |

## 1. Coverage: 4 to 6 distinct workflows

Each row names an input, a recurring bottleneck, an output and a PM decision. Gate 1 check 1 counts two variations of one task as one workflow. Applied to the 9 rows:

| Row | Distinct? | Note |
| --- | --- | --- |
| 01 Interview batches to insight log | Yes | Approved worked example |
| 02 Win/loss driver log | Yes | New input (CRM export) joined to interviews. New decision (positioning, sales gaps). Own Pragmatic focus area |
| 03 Weekly feedback into the problem log | Yes | High volume, continuous, counted by account |
| 04 Survey open-text coding | Weak | Same mechanic and same output as 03 (tag text to the problem log, "no fit" group). Different input only |
| 05 Participant screening | Yes, but support | Real pain (N2, N16, W11, W12). Weak PM decision. Fits as a lab step, not a module |
| 06 Market size model | Yes | Focus category, not Market |
| 07 Evidence register | Weak | Consumes the outputs of 01 to 04. Close to 09 and to the 01 log ("new, growing, fading") |
| 08 Concept test results | Yes | Planning / Ideation, not Market |
| 09 Answer stakeholder questions | Yes | Different trigger (a question), different decision (answer now or research) |

Concern: rows 01, 02, 03, 04 and 08 all teach "code text against a list, check quotes, audit". A course of those 5 would feel like one lab done five times. The course needs at least 2 modules where the agent does a different kind of work (join sources, keep a model, answer others).

### Merges recommended

| Merge | Why | How |
| --- | --- | --- |
| 01 and 02: do NOT merge | 02 adds a second source type (CRM), a source label per deal, and a different decision. Its error (CRM reason leaks into buyer findings) is new. Pragmatic names Win/Loss Analysis as its own focus area | Remove "win/loss calls" from the 01 trigger so the two rows do not share input |
| 04 into 03 | Same mechanic, same log, same "no fit" rule. Row 04 also lacks proof that PMs code surveys (gaps.md track 1) | Make a survey wave an optional second input in the 03 lab |
| 07 into 09 | Both run on the accumulated log. 07 has only one author for its bottleneck (Torres, W14 and W15) | 09 answers from the log and also lists stale or untested assumptions. The PM still decides each status |
| 05 into 01 or 02 | Support workflow. Weak PM decision | Use it as a lab step: the agent screens the next interview list |

### Rows outside the Market category

| Row | Category | Recommendation |
| --- | --- | --- |
| 06 Market size model | Focus / Market Definition | Defer. The brief says Market category. MKT-2026 core course already teaches market definition and segment evaluation. Good candidate for a later Focus or Strategy course |
| 08 Concept test results | Planning / Ideation | Defer. Solution validation, not market discovery. Bottleneck has one vendor source with no data (W16). Check fit with a Product Discovery or Design course |

## 2. Missing workflows

Market category focus areas (guide page 5 to 7): Market Problems, Product Strategy, Distinctive Competencies, Win/Loss Analysis, Competitive Landscape.

| Focus area | Rows | Critic view |
| --- | --- | --- |
| Market Problems | 01, 03, 04, 05, 07, 09 | Over-covered |
| Win/Loss Analysis | 02 | Covered |
| Competitive Landscape | None | Gap. The researcher rejected "competitor tracking" because of CAW-AI. That rejection is too broad. CAW-AI covers public reviews, positioning proof and a weekly signal watch. It does not cover an evidence-based map of the alternatives buyers actually use, including workarounds and "do nothing" (guide page 7). The course agent can build this from its own log and the win/loss "alternative chosen" field. This is a different agent, a different input and a stronger build, so rule 11 allows it |
| Distinctive Competencies | None | Acceptable gap. Low repetition (yearly), so a poor AI candidate under the systems-thinking spine |
| Product Strategy | None | Acceptable gap. High judgment, low repetition |

Also missing: the Market question has two halves, "what problems" and "where can we win". All retained rows answer the first half. A Competitive Landscape row would answer the second.

## 3. Vendor lean

| Row | Bottleneck sources | Non-vendor and recent? |
| --- | --- | --- |
| 01 | Perspective AI (E1, E2, one source), Torres, Condens, JMIR 2026 (E12), preprint (E13) | Partly. E12 and E13 are the best non-vendor items in the packet |
| 02 | Clozd, Corporate Visions (vendors), Pragmatic 2022 | No. The only non-vendor source is from 2022 |
| 03 | ProductPlan, Enterpret (vendors) | No |
| 04 | RTI 2025, Savanta 2025 | Non-vendor but old, and not about PMs |
| 05 | Lyssna, User Interviews (vendors), TechRadar opinion | No |
| 06 | PMA 2025, LogRocket 2023 | Non-vendor but old |
| 07 | Torres x2 (one source) | Fails 2-source test |
| 08 | Conveo (vendor, no data) | Fails 2-source test |
| 09 | NN/g 2024, UserTesting (vendor) | Partly |

The PRD accepts 2 independent practitioner or vendor sources for a bottleneck, and decision 37 accepts thin evidence. So vendor lean alone does not block a row. But no bottleneck for rows 02 to 09 has a recent non-vendor source. Track 3 does have one strong non-vendor primary (Product Focus 2026, N5). It shows PMs lack customer time, not which workflow causes it.

## 4. Real bottleneck per row

| Row | Bottleneck real? | Reason |
| --- | --- | --- |
| 01 | Yes, thin | Several independent sources on the burden and on the shift to checking |
| 02 | Yes | 3 independent sources plus the Pragmatic guide and N2 ("sales resists win/loss") |
| 03 | Yes, thin | 2 independent vendors (W4, W5), plus a manufacturing source (N17, weak) |
| 04 | Unclear | Burden is real for research teams. No source shows PMs do it |
| 05 | Yes | W11, W12, N2, N16 |
| 06 | Yes, old | W9 and W19, both age-flagged |
| 07 | No | One author. W15 does not say tracking is the burden (the row's own note) |
| 08 | No | One vendor with no data |
| 09 | Yes | NN/g and UserTesting are independent |

## 5. Hardware and internal PM

- Search effort is visible in all tracks. Gaps are recorded per row and per track. This meets the PRD rule.
- Concern: rows show "gap, no source" while the ledger holds hardware cases that fit them. E26 (CNH field interviews) fits row 01. E27 (power-tool maker asks cited questions across years of jobsite studies) is row 09 in a hardware setting. E28 (building products concept tests) fits rows 01 and 08. E29 (HP) fits row 01. All are vendor stories, so they are examples, not proof. The Synthesizer should link them to the rows.
- Internal PM: no 2026 source in any track. W18 (Enterpret, 2026-11-04) is one vendor. N21 to N23 are all older than 12 months. This is the largest priority gap.

## 6. Planted AI error per row

Each row names one error that passes the agent's own check and that an audit finds. Good. Concerns for Stage 2:

1. Data-based errors are reliable on all four platforms: 01 (one vocal buyer), 02 (CRM-only deal leaks in), 07 (blank segment field), 09 (old study for another segment). Model-based errors may not appear: 04 (negation and sarcasm) and 03 (forced fit) depend on how each model behaves. Strong 2026 models often handle simple negation. Prefer data-based errors.
2. Row 02: the quality check "each deal is marked interview or CRM only" could catch the planted error itself. Then the audit has nothing to find. Reword the check or the error.
3. A random audit of 3 items can miss one planted error. The lab data must plant it often enough, or the audit must be stratified, so every learner finds it.

## 7. Registry and workshop repeats

| Row | Risk | Note |
| --- | --- | --- |
| 01 | Resolved | Dan, 2026-11-20. Lab starts where PDW-AI stops |
| 02 | Low | Not a CAW-AI agent. Keep CAW-AI module 4 content out |
| 03 | Low to medium | Own feedback, not public reviews. Must not use a scheduled-task slide (CAW-AI slide 9) |
| 04 | Medium | Close to PDW-AI validation bridge (pervasiveness) |
| 06 | Medium | MKT-2026 teaches market definition and segment evaluation |
| 07 | Medium | PDW-AI "NOT YET VALIDATED" tags and the skeptic bridge to validation |
| New Competitive Landscape row | Medium | Must not be a signal watch, a review watch or a positioning proof check. Base it on the team's own evaluator evidence |
| All | Note | The AI Agents course teaches "evaluate and iterate". Method M6 (tune the brief from the audit) must teach only the new part: tuning a running agent across batches |

## 8. No-connector core lab on four platforms

- Rows 01 to 05 and 07 to 09: upload files and run. Plausible on all four platforms on paper.
- Row 06: needs web search or a source pack. Weaker.
- All 34 features in platform-matrix.yaml are "not verified". The Verifier must check the features the retained rows use.
- Biggest risk for the growing agent: the log must move from module to module. Only Claude documents downloadable file output (T2-4). On ChatGPT, Copilot and Gemini the learner may have to copy a table by hand. This affects every module after module 1.
- Other open risks: Copilot embedded files need a license or pay-as-you-go (T2-2). Gemini Workspace skills timing conflicts (T2-1). ChatGPT Free holds 5 project files.

## One coherent growing agent

The 9 rows can support one agent: a market evidence agent that keeps one problem log. Rows 02, 03, 07 and 09 all read from or write to that log. That is a strength.

Concerns:

1. No row is mapped to an autonomy rung. The ladder is a Stage 2 task, but the inventory should show that the rows give distinct rungs. A proposed ladder from the recommended rows:

| Module | Row | Rung | What the PM gives up |
| --- | --- | --- | --- |
| 1 | 01 Interview batches | Runs on demand. PM reads every flag and audits | Coding and quote checks |
| 2 | 02 Win/loss | Joins two sources. PM trusts source labels and audits them | Matching deals to interviews |
| 3 | 03 Weekly feedback (+ survey wave) | High volume. PM reads only flags and a sample. Stretch: a schedule (new slides, not CAW-AI) | Reading each item |
| 4 | New Competitive Landscape row | Builds a model across the log. PM reviews changes only | Maintaining the alternatives map |
| 5 | 09 Stakeholder answers (+ register) | Faces other people. Hand-off rules guard what it may say | First draft of answers to stakeholders |

2. Too many coding labs in a row (01, 02, 03, 04) gives the agent more work of the same kind, not more autonomy.

## Recommended rows (critic view; Dan decides)

| Choice | Rows |
| --- | --- |
| Recommended 5 | 01, 02, 03 (with 04 as optional input), new Competitive Landscape row, 09 (with 07 status proposals folded in) |
| If the Competitive Landscape row fails the rerun | 4 rows: 01 (with 05 as a lab step), 02, 03, 09 |
| Defer | 06 (Focus), 08 (Planning) |
| Merge or fold | 04 into 03, 07 into 09, 05 into 01 or 02 |

## Gaps for rerun

One ask per track. Each can be closed by web research.

| Track | Ask |
| --- | --- |
| 1 | Write one Competitive Landscape row (Market category): the agent keeps an alternatives map (competitors, substitutes, workarounds, "do nothing") from the team's own evaluator evidence (insight log, win/loss "alternative chosen"). Not a public-review watch, signal watch or positioning check (CAW-AI). Find 2 independent sources that describe keeping the competitive landscape current as a recurring PM burden |
| 2 | Find dated vendor docs on whether ChatGPT Projects, Copilot agent builder and Gemini skills can output a downloadable .csv or .xlsx file, so the learner can carry the log to the next module with no connector |
| 3 | Find 2 independent sources dated 2025-11-20 or later on how internal platform or tool PMs gather and synthesize employee user feedback, and where the time goes. Start with the unopened Enterpret platform PM guide |
| 4 | Find one non-vendor source, or the primary study, dated 2026, on the gap between seller-entered and buyer-stated win/loss reasons, or on how few deals get a win/loss interview. Start with the Corporate Visions 150,000-deal analysis (W2) |
