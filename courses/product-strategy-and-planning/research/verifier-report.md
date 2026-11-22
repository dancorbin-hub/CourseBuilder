# Verifier report: product-strategy-and-planning, Stage 1, Mode 1 (claims)

- Course: Advanced AI for Product Strategy and Planning (`product-strategy-and-planning`)
- Verifier run: 2026-11-22
- Files checked: `workflows.yaml` (sp-wf-01 to sp-wf-10, W1 to W24), `evidence-ledger.yaml` (E1 to E14), `needs.md` (N1, N12, N13 opened; others by carried status), `platform-matrix.yaml` (features the proposed labs use), `bond-stories.md` (4 recommended candidates).
- Files changed: `workflows.yaml` (evidence `status` and new `verifier_note` lines only), `evidence-ledger.yaml` (same), `platform-matrix.yaml` (same; on 7 carried entries I put the 2026-11-22 recheck in front of the old `verifier_note`). All three parse with `python3 yaml.safe_load`. A diff shows no other line changed.
- Not changed: `needs.md`, `bond-stories.md`, `sources.yaml`, all `rerun-*` files. Their results are in this report only.

## Limits of this run

1. Fetch budget: 48 of 50 page fetches used. Searches were used only for trendslop.
2. I marked "not verified" every item I did not open myself, also when the researcher opened it. I did not copy a researcher's status. Items that the Market Research verifier opened on 2026-11-20 keep that status, with a note.
3. Help Center pages for Claude and ChatGPT show only relative dates ("updated 3 days ago"). I accept them as dated vendor docs with the fetch date, as the Market Research verifier did. Google Gemini Help pages show no date at all, so they do not meet the dated vendor doc rule.

## Counts

| Result | Ledger E | Workflow W | needs.md N | Platform | Bond facts | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Verified | 9 | 14 | 3 | 16 | 2 | 44 |
| Partly verified | 1 | 5 | 0 | 5 | 2 | 13 |
| Not verified | 4 | 5 | 17 | 0 | 0 | 26 |
| Wrong | 0 | 0 | 0 | 0 | 0 | 0 |

- Ledger "verified" includes E14 (Market Research verifier status, not reopened). Workflow "verified" includes W9 and W10 (same).
- needs.md "not verified" includes N3, N11 and N20. The Market Research verifier opened them on 2026-11-20. I did not reopen them.
- Platform counts cover the 14 new lab features plus 7 carried entries that I reopened. Other new features (cl-rs-09, cg-12) and stretch features stay "not verified" (PRD decision 25).
- No item is "wrong". Several claims go past what the source says. See "Wording that goes past the source".

## Failures and items Dan must see

### Must fix before a slide

| Id | Problem | Action |
| --- | --- | --- |
| E9 | The arXiv PDF is a draft. Its first page asks readers not to circulate or cite it without the authors' permission. | Ask the authors for permission, or wait for a published version. Until then, use E9 in the talk track only, with no slide. |
| E3 | The numbers (under 2%, 11%, 19%) are not on hbr.org (paywall). I found them in a full-text snapshot of the HBR article on a third-party site (zby.github.io). The 11% context shift and "recommended doing both" are ChatGPT results only. The ledger says "models". The under-2% result applies to the 2 strongest tensions only. The other 5 tensions moved about 22%, mostly from option order. | Fix the wording: "In tests on ChatGPT, ...". Get the HBR article through a licensed copy before a number goes on a slide. |
| E2 | The ledger figures (49%, 3 studies, N 2,405, 13%) match the Science article. The arXiv preprint in `secondary_url` has different figures (50%, 2 studies, N 1,604, no 13%). The PDF I opened is a copy on a MediaPost server, not science.org. | Cite only the Science version (DOI). Do not cite the preprint for these figures. |
| W14 | KPMG webinar poll. No sample size, no poll date, no publish date. Respondents are valuation practitioners, not PMs. | Do not use as a statistic. It is the only source for "forecasts lean optimistic, few back-test" in sp-wf-05. |
| W2, W3 | Atlassian (308 leaders) and Product-Led Alliance (about 250) figures are confirmed on the pages. Neither page gives method or field dates. Primary reports not opened. | Open the Atlassian whitepaper and the PLA report before a slide. |
| W20 | 41% and 27% cite a "2026 State of B2B Product Management survey" with no link or sample. | Do not use the figures. |
| E7 | Error counts come from GPTZero only (vendor). The Register repeats them. Removal is confirmed only by the KPMG quote in The Register. The Register also says (citing the FT) that KPMG removed it from "some" of its websites. | Say "KPMG said it removed the report". Name GPTZero as the source of the counts. |

### Wording that goes past the source

1. W5: "reasoning behind priorities is often undocumented" is not on the page. The page only advises teams to document criteria. The page says a sales rep "escalated" a deal, not "pushed".
2. W12: the exact phrase is "the infrastructure hasn't kept up with the demand". The page gives no publish date.
3. W8: "the buyer must align definitions before comparing" is implied ("compare like for like"), not stated as a rule.
4. W15: "review at least quarterly" is the author's advice, not a finding.
5. E1: the ledger says 17 points. 54% minus 36% is 18. The source chart says 17, likely from unrounded figures. Use "54% vs 36%".
6. E7 note: GPTZero's 16 and 28 are not a mismatch. 16 is "at least 16 hallucinations" (strict). 28 is the wider "paraphrased or fake component" group.
7. N13: the page title is now "Product Strategy Matters More In An AI-First World" (Xebia, updated 2026-11-05). The quotes are confirmed. Update the source title.
8. cl-ws-08: the Claude page does not list plans. "All plans" is an inference from Free and Team or Enterprise text.
9. cg-09: the latest release note entry I saw was 2026-10-01, not 2026-11-19. The Work facts (2026-07-09 entry) are confirmed.
10. mb-11 and mb-13: the code interpreter page now says "Last updated on 2026-11-16", not 2026-09-28. The facts did not change.

### Market Research ledger ids that the rows cite (E6, E8, E9)

The rows' `platforms` lines cite Market Research ledger E6 (Copilot), E8 (Gemini) and E9 (ChatGPT). I rechecked them on the current vendor pages.

| MR id | Platform entry | Result 2026-11-22 |
| --- | --- | --- |
| E6 | mb-01 | Still true. 8,000 / 30 / 1,000 characters. Page updated 2026-11-16. |
| E8 | gm-03, gm-13 | The Market Research verifier marked MR-E8 "wrong" (March 2027 date). The current Workspace Updates post (2026-10-13, updated 2026-11-09) says Gemini app skills are for all Workspace customers and personal accounts, all ages, with no admin controls. The rows' Gemini line is fine if it does not repeat the March 2027 date. |
| E9 | cg-01 | Still true. Projects: Free 5, Go and Plus 25, Pro and business plans 40 files. Plus 20 in cg-03 is still a conflict. |

## Bottleneck check: 2 independent sources per row

| Row | Sources | Result | Note |
| --- | --- | --- | --- |
| sp-wf-01 | W1 (= W2), W3 | **Pass** | Atlassian (vendor) and Product-Led Alliance are independent. Both describe the burden: work not linked to strategy, manual status updates (W1), little time on strategy (W3). Both statistics need their primary reports before a slide. |
| sp-wf-02 | W4, W5 | **Pass, weak** | Independent, both 2026, both unsigned with no data. "Weights change each cycle" is W4 only. "Loudest stakeholder wins" is W5 only. |
| sp-wf-03 | W7, W8 | **Pass** | Independent, both verified, both 2026. Both are data vendors that sell reports. |
| sp-wf-04 | W11, W12 | **Partly passes** | Two independent, verified 2026 sources. But each supports a different half. "Demand outgrows capacity" is W12 only, and W12 is about research in general. "Concepts test well then fail" is W11 only. No half has 2 sources. W13 not verified. |
| sp-wf-05 | W14, W15 | **Partly passes** | "Business cases go stale, teams rarely recheck" is W15 only (2024, older than 12 months). "Forecasts lean optimistic, few back-test" is W14 only (partly verified, no sample, not PMs). W23 supports "no comparison to baseline" for public sector only. Needs a second 2026 source on stale business cases. |
| sp-wf-06 | W16, W17 | **Pass** | Independent, verified, 2026. Both describe the burden (cost beyond the first invoice, fast prototype vs finished capability, vendor changes). |
| sp-wf-07 | W19, W3 | **Pass, weak** | Independent, 2026. W19 verified. W3 partly verified (primary not opened). "Manual work each cycle" is an inference from both, not a stated finding. |
| sp-wf-08 | W20, W19 | **Pass, weak** | Independent, 2026. W20 states the burden (de facto commitments, roadmap debt). W19 states what material changes need (change process, versioning). "Bad news in different words to each audience" is W21 only (2019, not reopened). |
| sp-wf-09 | W1, W22 | **Pass** | Independent vendors, both 2026, both verified. Expedia "weeks of preparation" is one quote (W1). Stale decks and the "human integration layer" are W22. |
| sp-wf-10 | W23, W1 | **Partly passes** | Independent and verified. W23 lists warning signs, not how often they occur. "Few teams compare results with the business case baseline" has no source. W1 and W2 support manual status updates (83%) and outcome funding (8%, W2 partly verified). Reword to "warning signs include..." or find a 2026 source with a rate. |

Rows that do not fully pass: sp-wf-04, sp-wf-05, sp-wf-10. No row fails outright.

## Results table: workflow evidence (W)

| Id | Claim (short) | Result | Note |
| --- | --- | --- | --- |
| W1 | 80% clear, 11% linked, 83% manual, 72% overstretch; Expedia weeks of prep | Verified | Atlassian blog 2026-09-28. 308 leaders. Period not stated. Same study as W2 |
| W2 | Atlassian SPM report: 11%, 8%, two thirds a month or more | Partly verified | No publish date, field dates, method or base |
| W3 | Alignment 3.6 and 3.5 of 5; 49.2%, 47.5%, 43.9%; 72.2% | Partly verified | PLA 2026-03-11. About 250 leaders. Method not stated. Primary not opened |
| W4 | Criteria read differently; weights negotiable; fragile rubric | Verified | fitgap 2026-01-19, no author |
| W5 | Loudest stakeholder wins | Partly verified | "Undocumented reasoning" not stated |
| W6 | Hardware kill discipline | Not verified | Not reopened |
| W7 | Quantum estimates 4B to 20B+ by layer | Verified | 2026-09-15, updated 2026-09-30 |
| W8 | Why market sizes differ | Verified | October 2026 |
| W9 | TAM research challenges | Verified (MR 2026-11-20) | Not reopened. Aged |
| W10 | Market sizing desk research | Verified (MR 2026-11-20) | Not reopened. Aged |
| W11 | Stated intent vs behavior | Verified | Quirk's 2026-05-01 |
| W12 | Research demand 66% vs 55%, 69% AI | Verified | About 500, fielded 2025-12-23 to 2026-01-13. Vendor |
| W13 | Qual research takes 6 weeks | Not verified | Not reopened |
| W14 | KPMG poll: 86%, 67%, 37%, 46% | Partly verified | No sample or date |
| W15 | Business cases go stale | Verified | 2024-02-12. Aged |
| W16 | Real build vs buy cost | Verified | Gong 2026-08-05 |
| W17 | Build vs buy as cost question | Verified | Product School 2026-01-04 |
| W18 | 56% build in-house preference | Not verified | Not reopened. Context only |
| W19 | Roadmap governance and hardware | Verified | Umbrex, modified 2026-09-20 |
| W20 | Roadmaps become de facto commitments | Partly verified | Figures unsourced |
| W21 | Communicating roadmap changes | Not verified | Not reopened. 2019 |
| W22 | Stale portfolio reviews, hardware | Verified | Gocious 2026-05-05 |
| W23 | Benefits realisation warning signs | Verified | NZ Treasury, October 2026 |
| W24 | Internal platform PM | Not verified | Not reopened. 2023 |

## Results table: evidence ledger (E)

| Id | Claim (short) | Result | Note |
| --- | --- | --- | --- |
| E1 | Analysts follow agent lean 86% | Verified | 2026-10-27. All figures confirmed. Study period not stated. Vendor. 18 vs 17 point note above |
| E2 | Sycophancy: 49% more, N 2,405, 13% return | Verified | Science 2026-03-26. Cite Science, not the preprint |
| E3 | Trendslop | Partly verified | Numbers from a third-party copy. ChatGPT-only results worded as all models |
| E4 | LLM anchoring | Verified (abstract) | ACL 2026 |
| E5 | LLM overconfidence | Verified (abstract), weak | Preregistered. No numbers |
| E6 | 3 to 13% hallucinated citation URLs | Verified (abstract) | arXiv 2026-04-03 |
| E7 | KPMG report citation errors | Verified | Counts from vendor only. Removal from KPMG quote |
| E8 | Deloitte Canada and Australia | Not verified | Not reopened |
| E9 | LLM venture ranking 0.74 vs experts 0.45 | Verified | Draft: do not cite without permission |
| E10 | 85% use AI, 17% high impact on planning | Verified (page) | Self-selected, directional. Competitor |
| E11 | IBM watsonx prioritization | Not verified | Not reopened |
| E12 | Dragonboat FinTech | Not verified | Not reopened |
| E13 | SAP article | Not verified | Not reopened. Do not use |
| E14 | Cyberhaven sensitive data | Verified (MR) | Not reopened |

## Results table: needs.md (N)

`needs.md` has no status fields that I may edit. Results are here only.

| Id | Result | Note |
| --- | --- | --- |
| N1 | Verified | Checked in the local framework text (fw.txt): verify outputs, protect sensitive information, stay accountable; fund, delay or stop; internal products |
| N12 | Verified | DX Annual 2026-04-16, SiriusXM. Also: over 200 platform investments for about 700 internal developers |
| N13 | Verified | Quotes confirmed. Page title differs from the ledger (see above) |
| N3, N11, N20 | Not verified (this run) | Opened by the Market Research verifier 2026-11-20 |
| N2, N4 to N10, N14 to N19 | Not verified | Not opened (fetch budget). N5, N7, N8, N16, N17 are weak vendor or analyst figures: keep off slides |

## Results table: platform features used by proposed labs

| Id | Feature | Result | Note |
| --- | --- | --- | --- |
| cl-ws-08 | Claude web search | Partly verified | Plans not listed on the page |
| cl-up-10 | Claude upload CSV and XLSX | Verified | 2026-07-23. 30 MB project files; XLSX needs code execution |
| cl-fo-06, cl-cl-03, cl-pj-01 | Claude file output, skills, projects | Verified (MR) | Not reopened |
| cg-01 | ChatGPT Projects (MR E9) | Verified | Reopened. Unchanged |
| cg-09 | ChatGPT Work plans | Verified | Not Free or Go |
| cg-10 | Spreadsheet output with formulas | Verified | Plans not named on the page |
| cg-11 | Data analysis (Python) | Verified | Output download not stated |
| cg-13 | ChatGPT web search | Verified | Citations "may" be included |
| cg-14 | Project memory; Work not in project-only memory | Verified | |
| mb-01 | Agent builder limits (MR E6) | Verified | Reopened. Unchanged |
| mb-02 | Embedded files | Verified | Reopened. Unchanged |
| mb-04 | Code interpreter toggle | Verified | Reopened |
| mb-11 | Code interpreter file output | Verified | Session-only download. Page date now 2026-11-16 |
| mb-12 | Public websites and Search all websites | Verified | |
| mb-13 | Code interpreter input files | Verified | Reading knowledge files not documented |
| mb-14 | Excel as embedded knowledge | Verified | CSV not allowed. One sheet per workbook |
| gm-01 | Gemini skills | Partly verified | Reopened. Undated page |
| gm-03 | Skills for Workspace accounts (MR E8) | Verified | Reconfirmed by gm-13 post |
| gm-10 | Gemini file upload and analysis | Partly verified | Undated. No code execution or export stated |
| gm-11 | Code files in a skill | Partly verified | Allowed, but no doc says they run. Key risk stands |
| gm-12 | Name a skill in a task | Partly verified | Undated |
| gm-13 | Skills in Gemini app vs Workspace apps | Verified | 2026-10-13, updated 2026-11-09 |

Platform risks for the labs:

1. Gemini: no dated Google doc says a skill runs code for math, uses Google Search or outputs a file (gm-09, gm-10, gm-11). Scoring and sensitivity labs must not depend on these on Gemini until the Gate 2 proof.
2. ChatGPT: spreadsheet output with formulas needs ChatGPT Work. Work is not on Free or Go, and not in a project with project-only memory (cg-09, cg-14). Data analysis output download is not documented (cg-11).
3. Copilot: code interpreter output is session-only, and no doc says it reads the agent's knowledge files (mb-11, mb-13). Learners upload the sheet in chat for each run.
4. Claude: web search plans are not listed on the page (cl-ws-08). Team and Enterprise owners must turn it on.

## Bond story facts (4 recommended candidates)

| Candidate | Result | Note |
| --- | --- | --- |
| 1. Trendslop | Partly verified | Authors, date (2026-03-16), 7 models (Fortune 2026-04-10) confirmed. Affiliations: Esade (Fortune) and NYU Stern (Levina) confirmed; University of Sydney not checked. The hook "asked seven models 15,000 times" goes past the source. The HBR text gives 15,000+ trials for each of two GPT-5 experiments; Fortune says "15,000 simulations and scenarios". Say "thousands of runs". The file says no percentages are open; a full-text copy has them (see E3), but it is a third-party copy |
| 2. Apple Siri | Partly verified | MacRumors 2026-05-05: 250 million USD, 25 to 95 USD per device, no wrongdoing, preliminary approval, March 2025 delay and ads pulled confirmed. "Features still not shipped as of May 2026" is not in MacRumors. AppleInsider (S-S2) not opened |
| 3. Commonwealth Bank | Verified | Information Age 2025-08-21: 45 roles, "voice bot", bank quote "did not adequately consider ... not redundant", union account confirmed. The Register 2025-08-22 confirms the reversal and union claim (it says "chatbot"). Aged 15 months: Dan decides |
| 4. Intel memory exit | Verified (one source opened) | NPR: "What would the new guy do?" and "Get out of the memory business", 1985, Japanese competition confirmed. NPR page shows only copyright 2012. Stanford case (S-I2) not opened, so the second source is not checked by me |

## Not opened (budget)

- W6, W13, W18, W21, W24; E8, E11, E12, E13; N2 to N11 and N14 to N20 (except as noted).
- Atlassian SPM whitepaper (W2), PLA 2026 State of Product Management report (W3), AppleInsider (bond 2), Stanford GSB case (bond 4), Anthropic full PDF (E1).

## Rerun entries (second pass)

Checked 2026-11-22. Fetch budget: 15 pages, 15 used. Statuses are set in the rerun files. The Synthesizer merges them.

| Id | Claim | Result | Note |
| --- | --- | --- | --- |
| W25 | PLA: inconsistent weighing, decisions easy to reopen, escalations reset roadmap | Verified | Text confirmed. Figures are N21. Page promo "250 product leaders" is wrong. Author is on the N21 team |
| W26 | ITONICS: averages hide gaps, unrecorded overrides, rescoring fatigue | Verified | Text confirmed. All numbers illustrative, unsourced. Vendor |
| W27 | ProductPlan: escalations are the top override force | Verified | Text confirmed. Figures are N21, not independent. Satav paraphrase only |
| W28 | Product Coalition: frameworks launder opinion | Not verified | Not opened (budget) |
| N10 | Hardware commits in stages; cost near vertical after steel tooling | Verified | Reopened. Also: advance on evidence, "not because the calendar demands it" |
| N11 | Hardware: skipped customer and budget questions; late misalignment costs | Verified | Reopened. AI quote is from Xaviera Reynhout, quoted in the article |
| N21 | State of Product Management 2026: 60.2% override, 3.3 of 5, 49.2%, 47.5%, 72.2% | Verified | Primary PDF opened. Nearly 250 professionals (43.3% leaders), fieldwork Q4 2025. 60.2% is a multi-select answer share, not a share of frameworks. PLA wrote it, ProductPlan sponsored it, p. 6 calls it ProductPlan's report. No method or response rate. Rule 4: Dan decides |
| N22 | airfocus: platform value illegible, budget reviews hard | Verified | No statistics. Vendor blog |
| N23 | Microsoft: platform work not costed or planned at stage 1 | Verified | en-us page opened. ms.date 2025-10-21: age flag, Dan decides |
| N24 | Cooper and Zhao: gate preparation consumed time without value | Verified | No durations. 30% figure too old. Single source |
| E15 | Deference to AI predictions (Newcomb) | Not verified | Not opened (budget) |
| E16 | Pathologists anchor on AI estimate, more under time pressure | Verified (abstract) | n = 28. Correct the 7%: automation bias rate. Time pressure made errors worse, not more frequent. Preprint |
| E17 | Credit ratings drift toward AI advice over time | Verified (abstract) | JMS 63(2), DOI 10.1111/joms.70009. 6 studies, 3 sessions each. No sample or effect sizes in the abstract |
| E18, E19 | Dragonboat bank story; trendslop replication | Not verified | Not opened (budget). Not for slides in any case |
| E3, E12, E13 updates | Researcher findings | Not verified | Not reopened |
| gm-14 | Gemini app creates files (Sheets, decks, PDF) | Verified | 2026-10-29. No .xlsx, no skills, no code execution |
| gm-15 | Gemini skill runs code | Not verified | Gap stands (not found) |
| mb-15 | Copilot code interpreter inputs | Verified | 2026-11-16. Uploads only; knowledge files not named. Page says code interpreter is "always enabled" in Agent Builder: conflicts with the toggle in mb-04 and MR-E6. Test at Gate 2 |
| mb-16 | Copilot Studio code interpreter on structured knowledge (preview) | Verified | 2026-08-04. SharePoint knowledge, not embedded files. Not core |
| MR-E6, MR-E8, MR-E9 | Carried platform entries | Not verified | Not reopened. First pass covers mb-01, gm-02, cg-01 |

### Two-source check for the bottlenecks

| Row | Sources | Result | Reason |
| --- | --- | --- | --- |
| sp-wf-02 | W25, W26 | Pass | Independent publishers and authors, both signed, both 2026. Both describe the burden: inconsistent weighing, reopened decisions, unrecorded overrides, rescoring fatigue. No usable time or cost data. Both are vendor or vendor-run. Dan decides if that is strong enough |
| sp-wf-11 | N10, N11 | Partly pass | Independent, signed, 2026. They support staged commits, steep cost after tooling, advancing on the calendar, and late misalignment costs. Neither says the gate package check is manual cross-document work done late or not at all. Reword that sentence as an assumption or find a source. N24 adds one source on gate preparation burden |

### Failures and actions

1. N5 and W3 are one survey (N21). Any claim that uses both as 2 sources needs a new second source.
2. The N5 claim "over 60% of frameworks are overridden" is wrong. Use: 60.2% of respondents name leadership escalations or new directives as a factor that most often overrides their framework.
3. sp-wf-11 bottleneck text goes past its sources (see above).
4. E16 "7% of cases" wording needs the automation bias definition.
5. Copilot code interpreter toggle: docs conflict (mb-15 vs mb-04). Test at the Gate 2 proof.
