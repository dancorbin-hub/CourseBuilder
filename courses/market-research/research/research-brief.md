# Research brief: Advanced AI for Market Research

- Course id: `market-research`
- Stage 1, run 1. Written by the Synthesizer on 2026-11-20.
- Inputs: all files in `courses/market-research/research/` (workflows, needs, methods, platform matrix, evidence ledger, sources, gaps, verifier report, critic report, alignment log, worked example row, run log).
- Rule for this brief: each claim cites a ledger id with status "verified" or "partly verified". Items with status "not verified" or "wrong" are named only as gaps or exclusions. Each source keeps its limits.
- Next step (PRD): the Verifier runs a trace check on this brief before Dan approves Gate 1.
- The Gate 1 decision table is in `gate-1-packet.md`.

## 1. Summary

1. The research supports 4 strong workflow rows and 1 conditional row: 01 interviews, 02 win/loss, 03 weekly feedback, 09 stakeholder answers, and 10 alternatives map (conditional). Together they feed one market evidence agent that keeps one problem log.
2. Bottleneck evidence is thin and leans on vendors. Rows 02, 03, 09 and 10 each have 2 independent sources. For rows 02 to 09, no verified bottleneck source is both recent and non-vendor. Row 10 has one 2026 survey (N13), but it covers CI work in general. Rows 07 and 08 fail the 2-source rule.
3. The speed claim ("AI makes synthesis faster") rests on vendor data (E1, E2, E10, E22). The strongest non-vendor 2026 evidence is about AI risks: over-coding and low agreement (E12), and synthetic respondents that flatten opinion (E16, E17).
4. A no-connector core lab is possible on all four platforms on paper. Four platform conditions need Dan's decision: ChatGPT plan level, Copilot license, Gemini Workspace status, and how the log moves between modules.
5. Five items touch the approved worked example row (mr-wf-01) and need Dan's yes: the "2 or more interviews per insight" rule (PA-01), the wrong Gemini date (E8), a YAML quote fix, the row's sources list, and the data safety note (PA-03). The Pragmatic alignment log has 2 high conflicts (PA-01, PA-02).

## 2. Recommended workflows and why

The critic's view and this brief agree on the set. Dan decides each row.

| Row | Recommendation | Why |
| --- | --- | --- |
| mr-wf-01 Interview batches to insight log | Retain (approved worked example). Fold row 05 in as a lab step | The burden shifts to checking AI output (E4, E10). Strong PM decision. Base of the course agent |
| mr-wf-02 Win/loss decision-driver log | Retain as its own module | Two independent vendor sources say sales-entered loss reasons differ from buyer reasons (W1, W2). Own Pragmatic focus area (N1). New input type (CRM export) and a new error |
| mr-wf-03 Weekly feedback into the problem log | Retain. Merge row 04 as an optional second input (a survey wave) | Two independent vendor sources on slow, inconsistent hand tagging (W4, W5). High volume moves the PM from reading each item to reading flags |
| mr-wf-09 Answer stakeholder questions | Retain. Fold row 07 status proposals in | Two independent sources on lost and unused past research (W13, W20). W13 is from 2024 (age flag). Different trigger and decision. The agent faces other people |
| mr-wf-10 Alternatives map from own evidence | Retain with a condition (decision f in the packet) | Gives the course the "where can we win" half of the Market question. Generic CI upkeep burden has 2 sources (N13, W21). The specific workflow (map built from own deal evidence) has no source |
| mr-wf-04 Survey open-text coding | Merge into 03 | Same mechanic and output as 03. No source shows PMs do this task. Both sources are older than 12 months (W7, W8) |
| mr-wf-05 Participant screening | Fold into 01 as a lab step | Real burden (W11, W12). Weak PM decision. Fits as a step, not a module |
| mr-wf-07 Evidence register | Fold into 09 | Fails the 2-source rule (W14 and W15 are one author, not verified) |
| mr-wf-06 Market size model | Defer | Focus category, not Market. Sources older than 12 months (W9, W19). MKT-2026 teaches market definition |
| mr-wf-08 Concept test results | Defer | Planning category. Fails the 2-source rule (W16, one vendor, not verified) |

Why this set works as one course:

- It avoids 5 coding labs in a row. Rows 01 to 03 code text. Row 10 keeps a model across the log. Row 09 answers other people.
- Each later row reads from or writes to the module 1 log. This fits the one-agent rule (PRD decision 38).
- If Dan rejects row 10, rows 01, 02, 03 and 09 still give 4 rows. That meets Gate 1 check 7 (at least 4 rows earn retain).

## 3. Suggested module order on the autonomy ladder (suggestion only)

PRD decision 35: hand-run batch, then a scheduled agent with a flag report, then agents that hand work to other agents. Dan tries the ladder at Gate 2.

| Module | Row | Rung | What the PM gives up | Planted error warning (house rule 13) |
| --- | --- | --- | --- | --- |
| 1 | 01 (+ 05 step) | Run by hand on a batch. PM reads every flag and audits | Coding and quote checks | Told |
| 2 | 02 | Run by hand. Joins two sources. PM audits the source labels | Matching deals to interviews | Hint |
| 3 | 03 (+ 04 input) | High volume. PM reads only flags and a sample. Schedule as stretch only | Reading each item | Hint |
| 4 | 10 | Reads the outputs of modules 1 and 2. First hand-off between agent parts | Keeping the alternatives map | Hint |
| 5 | 09 (+ 07 status proposals) | Faces other people. Hand-off rules guard what it may say | First draft of answers to stakeholders | None |

Limits of this ladder:

1. Rung 2 (schedule) is not proven. All schedule features are "not verified" (cl-sc-07, cg-06, mb-06, mb-07, gm-07, gm-08). A schedule with no new input does nothing in a no-connector lab (methods.md M8). So the core path stays a hand-run batch. The schedule is a stretch step.
2. Rung 3 (agent to agent) with one course agent means a hand-off between skills or files of the same agent. Gate 2 must define what "hand-off to another agent" means in this course.
3. Module count depends on course length, set at Gate 2. With 4 modules, drop row 10 or fold it into module 2.

## 4. Evidence strength

### Plain verdict

| Topic | Strength | Ledger ids | Limits to keep |
| --- | --- | --- | --- |
| AI makes synthesis faster | Weak. Vendor data only | E1 (partly verified, weak), E2 (verified, weak), E10 (verified, vendor), E22 (verified, single source, self-reported) | E1 and E2 are one vendor (Perspective AI). E1 baseline method not stated; "4 hours" is a 2026 median (Jan to Apr 2026), not Q1. Do not put E1 or E2 on a slide. E22 baseline hours conflict on the page |
| Counterweight on speed | Moderate, non-vendor | E12 (verified) | Peer reviewed, 2026. A chat-based workflow saved no time. Corpus is 317 newspaper articles on nurses (2020 to 2023), not interviews |
| Work moves to checking AI output | Moderate. 3 sources, 2 are vendors | E4 (verified), E10 (verified, vendor) | 71% of 332 practitioners say validating AI output still takes significant time (E10). Survey period not stated. PMs are 9% of that sample |
| AI rewords quotes and loses context | Moderate. 3 sources | E5 (verified) | No 2026 source gives an error rate. Do not state a rate. JMIR shows one reworded quote in a pilot. The Condens line is the authors' summary. Torres is 2025 (age flag) and was not reopened |
| AI over-codes and agrees less than humans | Strongest non-vendor item | E12 (verified) | GPT-5 and Gemini 2.5 Pro: Krippendorff alpha 0.487 and 0.507, against 0.703 for two humans. One study. Newspaper articles on nurses, not interviews |
| Synthetic respondents flatten opinion | Strong, 2 independent non-vendor sources | E16 (verified), E17 (verified) | E16: public opinion, not B2B buyers; respondent count not on page. E17: sample size not on page; authors say synthetic data fits early concept tests, not decisions that need precise insight |
| LLM coding can erase sensitive narratives | Moderate, abstract only | E15 (verified, abstract only) | 21 survivors of firearm violence. Not PM |
| PMs lack time with customers | Moderate, non-vendor | N5 (verified) | n = 677, 83% Europe. 71% do not spend enough time with customers or the market. Shows the lack of time, not which workflow causes it |
| Leaders use AI for research | Moderate | E3 (verified) | 107 senior product leaders, Q2 2026. Sample is likely more AI-aware than average. Full report gated. Co-produced by Lyssna, a research-tool vendor |
| Bottlenecks for rows 02 to 10 | Thin. Mostly claims, not statistics | W1, W2, W4, W5, W11, W12, W13, W20, N13, W21 | Vendor or vendor-adjacent sources, or older than 12 months (W13). N13 is a 2026 survey of 101 PMMs with figures on CI work in general, not on an alternatives map |
| Hardware examples | Example only | E28 (verified, single source), N5 (verified) | E28 is a consultancy case (composite siding concept tests). E26, E27 and E29 fit rows 01 and 09 but are not verified, so they are not used |
| Internal PM | Gap | N27 (verified, vendor) | One vendor on how platform PMs take in feedback. No time data. No second verified 2026 source (N28 is partly verified) |

### Excluded from claims

| Id | Why |
| --- | --- |
| E13 | Status "wrong". The 88.6% figure is not what the paper says. Preprint. If a later run fixes the wording, the verifier gives "16 of 22 report themes per source" |
| E8 | Status "wrong" on the Workspace date. See decision b in the packet |
| W2 figure "50 to 70%" | No method. Drop confirmed by the Verifier |
| W10 figure "95%" | Primary not found |
| E14, E18, E19, E21, E30, N24 | Partly verified. Use only with the limits in the ledger. No figure from E14 or E19 goes on a slide |
| E25, E26, E27, E29, W3, W14 to W17, N2 to N4, N6, N12, N16, N18 to N23, N25 | Not verified. Not used for claims |

## 5. Platform readiness

Core build with no connectors. Each line cites a platform matrix id.

| Platform | Core build | Evidence | Status | Main risk |
| --- | --- | --- | --- | --- |
| Claude | Project with instructions and knowledge, or a custom skill. All plans | cl-pj-01, cl-cl-03 (E7) | Verified. Help Center shows relative dates only | Code execution must be on for skills and file output. An org owner can turn file output off (cl-fo-06) |
| ChatGPT | Project with instructions and files | cg-01 (E9), cg-03 | Verified on help-lb.openai.com (OpenAI subdomain). Relative dates only | Files per project: Free 5, Go and Plus 25, Pro and business 40 (cg-01). The upload FAQ says Plus 20 (cg-03). Free: 3 uploads per day (cg-03). Skills only on business plans (cg-04, not verified) |
| Copilot agent builder | Agent with instructions (8,000 characters) and up to 20 embedded files | mb-01 (E6), mb-02, mb-03 | Verified, dated 2026-11-06 and 2026-11-16 | Embedded files need a Microsoft 365 Copilot license or pay-as-you-go billing (mb-03). The same page conflicts with itself on unlicensed authoring. Not in GCC (mb-02) |
| Gemini | Gemini skill with instructions and up to 100 MB of files | gm-01, gm-02, gm-03 | gm-01 partly verified (page undated). gm-03 verified (blog 2026-09-30, updated 2026-11-09) | Two Google pages disagree on Workspace accounts: the blog says skills are available now; the Help page says "soon". Canvas and Deep research do not work in skills (gm-06, partly verified) |

Moving the log from module to module (file output):

| Platform | Downloadable file output | Status |
| --- | --- | --- |
| Claude | .xlsx, .docx, .csv and more, 30 MB, all plans | Verified (cl-fo-06) |
| ChatGPT | "Spreadsheets or PDFs". No plans, formats or Projects named | Partly verified (cg-08) |
| Copilot | Code interpreter files (Word, Excel, PowerPoint, PDF), session only | Verified (mb-11) |
| Gemini | 11 formats in the Gemini app. Skills not named | Verified for the app only (gm-09) |

Catch-up kit: no copy feature is verified on any platform. All sharing features are "not verified" (cl-pj-02, cl-cl-05, cg-05, mb-05, gm-04). A text kit (brief as text plus knowledge files) needs no sharing feature, so it should work on all four platforms (methods.md M10). It is not tested yet. It can also carry the log forward on platforms where file output is not proven.

## 6. Pragmatic conflicts

Sources used by the alignment agent match the list in `status.yaml` (Pragmatic Framework 2027 guide, PDW-AI 26.09, MKT working deck, CAW-AI, two pragmaticinstitute.com articles plus one older article with an age flag). BPW-AI, PRC and PRW-AI were not opened.

| Id | Severity | Conflict | Alignment recommendation | Touches approved row? |
| --- | --- | --- | --- | --- |
| PA-01 | High | Row 01 fix rule "2 or more interviews per insight" against PDW-AI: a low-frequency, high-intensity signal can be the real insight | Keep a rule, but flag a single-interview insight as "single source". Do not drop it. The PM decides | Yes |
| PA-02 | High | AI-moderated interviews and synthetic respondents against PDW-AI "AI never replaces talking to a real person". Pragmatic sources disagree with each other | Follow PDW-AI. Ask Pragmatic which position is current before Gate 2 | No |
| PA-03 | Medium | Data safety note missing on rows 01, 06, 07, 08. No row asks for consent before recording | Add one standard note to every row, plus a point on how a running log keeps sensitive data longer | Yes (row 01) |
| PA-04 | Medium | Row 02 "truth rate" frames sales as untruthful | Rename to "match rate". Default minimum 10 deals. Interviews by someone outside sales (N1) | No |
| PA-05 | Medium | Course scope against the Pragmatic Market course map | Keep scope. Map the course to focus areas in the Gate 2 spec | No |
| PA-06 to PA-09 | Low | Validation tests, old Framework names in the MKT deck, field name `pdlc_stage`, Gems in PDW-AI | See the packet, section 2 | PA-08 touches the approved schema |

## 7. Gaps

Gaps left after the one-time rerun. A gap is not a failure.

| # | Gap | Effect |
| --- | --- | --- |
| 1 | No non-vendor 2026 source on synthesis time for PM work | Say "practitioners report faster analysis (E10, vendor)" and give the E12 counterweight. No speed figure on slides |
| 2 | No recent non-vendor bottleneck source for rows 02 to 10 | PRD decision 37 accepts thin evidence. Dan's own cases fill the gap |
| 3 | Row 10: no source on keeping an alternatives map from own deal evidence | The row rests on a generic CI burden (N13, W21) |
| 4 | Win/loss: no 2026 primary on the gap between seller and buyer reasons (rerun ask 4, open) | Use W1 and W2 as claims only, no figure |
| 5 | Internal PM (priority): one 2026 vendor source (N27). N28 partly verified, and its wording goes past the source | Dan's internal PM examples fill the gap |
| 6 | Hardware (priority): one verified case (E28). Three more cases not verified (E26, E27, E29) | Verify E26 and E27 in the next run, then link them to rows 01 and 09 |
| 7 | File output for ChatGPT Projects and Gemini skills not proven | Gate 2 proof. Text catch-up kit as fallback |
| 8 | Schedule features not verified on any platform | Schedule rung is a stretch step until verified |
| 9 | No study compares agent-manager methods (brief, checks, hand-off rules, audit) | Teach them as practice, not as a finding |
| 10 | Health care, FinTech and services: no source on PM research tasks | Data safety notes only |

## 8. Open questions for Dan

The packet lists each with options and a recommendation.

1. PA-01: change the approved row 01 rule from "drop" to "flag as single source"?
2. E8 and the YAML parse error: correct the approved row 01 Gemini line and add quotes to the line that breaks the parse (line 76; the run log says 2 values)?
3. PA-02 and PA-03: which Pragmatic position on AI-moderated interviews? Standard data safety and consent note on every row?
4. Rows 06 and 08: defer to a later course?
5. Platform risks: ChatGPT Project as core build, minimum plans, Copilot license as a prerequisite, text catch-up kit?
6. Row 10: retain on a generic CI bottleneck, or defer until a better source exists?
7. Age-flagged sources: keep W13 (NN/g 2024) for row 09? If not, row 09 has 1 bottleneck source.
