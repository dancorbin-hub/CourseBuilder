# Gaps: Advanced AI for Product Strategy and Planning (Stage 1)

Each researcher appends gaps under its own heading. A gap is not a failure.

## Bond stories

- Internal product management: no strong internal PM strategy story found. Candidate 3 (Commonwealth Bank) is the closest: an internal service operation, not an internal product team.
- Health care and manufacturing: no candidate found that fits the core messages. Not searched in depth (fetch budget).
- Trendslop (candidate 1): per-trade-off percentages are behind the HBR paywall. Not verified.
- Sonos (candidate 6): the "rushed to meet a launch date, staff warned" angle has no source I could open.
- Apple Siri (candidate 2): feature status after May 2026 not checked.

## Track 3: PM needs

Written 2026-11-22. Source ids refer to `needs.md`.

| # | Gap | What we have | Next step |
| --- | --- | --- | --- |
| G3-1 | No 2026 primary source on hours PMs spend on strategy, prioritization, business cases or planning tasks | Shares only: 25% spend most time on strategy (N3); 34% of leaders lack time for strategic thinking (N20) | Open the ProductPlan 2026 PDF (N5) and the Atlassian 2027 report (N7) |
| G3-2 | Business case work: no 2026 source on time, steps or how finance reviews AI-built numbers | Pragmatic method (N1); hardware commit costs (N10, N11) | Search finance and FP&A sources; open Galorath 2026 report |
| G3-3 | Most 2026 survey figures are vendor landing pages with no method (N5, N7, N8, N16, N17) | Product Focus 2026 (N3, N4) is the only primary with a stated sample and fieldwork | Do not put weak figures on slides until the PDFs are checked |
| G3-4 | Hardware (priority): no data on how long roadmap or stage-gate business cases take, or on supplier lead times in plans | 2 independent practitioner sources on commit cost (N10, N11); 47.6% hardware share (N3) | Search PDMA and hardware trade press |
| G3-5 | Internal PM (priority): one strong case (SiriusXM, N12). No second source on internal annual planning or funding cases. No time data | 20% build internal products (N3); internal pricing means funding and cost allocation (N1) | Open airfocus platform PM article; search platform engineering planning |
| G3-6 | Health care: no source on PM strategy, roadmap or business case work | HHS de-identification rules for PHI (N19) | Search health tech PM planning; note Focus 28.01 already uses a health care case |
| G3-7 | Services: no source | none | Open TSIA State of Professional Services 2026 and MIT Sloan productization article |
| G3-8 | Manufacturing: no PM planning task data | Forrester advice only (N15) | Search manufacturing portfolio planning 2026 |
| G3-9 | FinTech: one source per claim (N6, vendor). FINRA guidance not opened | N6, N8 | Open FINRA guidance and a second FinTech PM source |
| G3-10 | MNPI risk in product plans of non-financial public companies: no source. N18 covers financial firms only | Inference flagged in needs.md | Ask Dan or legal before any slide states it |
| G3-11 | Data risks for hardware, internal PM and services are inference only | none | Search supplier confidentiality and employee data in AI tools |
| G3-12 | Carry-over mr-wf-06 (market size model): still no 2026 source on time spent | none | Not researched in this run (budget) |

## Track 4: evidence

Written 2026-11-22. Web fetch budget: 20 of 20 used. Unopened sources are in `evidence-ledger.yaml` under `unopened`.

| Id | Gap | Nearest evidence | Next step |
| --- | --- | --- | --- |
| G4-1 | No 2026 primary statistic on how often PMs use AI for prioritization, business cases, roadmaps or OKRs | E10 (17% rate AI impact on planning and roadmapping as high; perceived impact, not use; Pragmatic competitor) | Open ProductPlan 2026, Product-Led Alliance 2026 and UXCam 2026 reports |
| G4-2 | No 2026 measured impact (time or quality) of AI on any strategy workflow in a named company | E11 (IBM, 2024, no results), E12 (vendor, no results), E13 (unverified) | Search named-company talks and engineering blogs; ask Dan for client stories (decision 43) |
| G4-3 | No 2026 study of LLM false precision in market sizing or business-case numbers | E5 (general overconfidence, abstract only), E4 (LLM anchoring on numbers in the prompt) | Open ConfidenceBench (arXiv 2607.20526); re-open ICAEW article on AI errors in financial models |
| G4-4 | No 2026 study of people anchoring on an AI score in prioritization | E1 (analysts follow an agent's lean 86%; analysis task, not scoring) | Open arXiv 2603.28944, 2603.11821 and J Mgmt Studies 63(2) 2026 |
| G4-5 | Sycophancy toward a stated business strategy: no direct study | E2 (personal advice domain), E3 (trend bias, not agreement with the user) | Search 2026 sycophancy studies with business or expert framing |
| G4-6 | Circular sourcing ("two articles quoting one report"): only case evidence, no rate | E7 (KPMG 55% figure spread through news and LLMs), E6 (link existence only) | Open DeepTRACE (ICLR 2026) for citation-support rates |
| G4-7 | Hardware: no case study of AI in strategy, roadmap or portfolio work | none | Search hardware and semiconductor PM conference talks 2026 |
| G4-8 | Manufacturing and health care: no case of AI in strategy or portfolio work. Health care has only a failure case (E8, Deloitte, secondary) | E8 | Search health system strategy-office and med-device portfolio cases |
| G4-9 | Internal PM: one case only, older than 12 months (E11, IBM 2024) | E11 | Dan decides if E11 stays. Search 2026 internal-platform PM cases |
| G4-10 | OKR tracking and strategy reviews: vendor pages only (Profit.co, Dragonboat); no independent case | E12 | Not a priority unless a module needs it |
| G4-11 | E3 numbers come from a third-party summary; E8 has one secondary source | E3, E8 | Open the HBR article and The Independent investigation before any slide use |

## Track 2: methods and platforms

Written 2026-11-22. Ids refer to `platform-matrix.yaml`. Web fetch budget used: 15 of 15.

| Id | Gap | Related | Next step |
| --- | --- | --- | --- |
| G2-1 | Gemini: no doc says a skill runs code (scripts can be uploaded, but where and if they run is not stated). Scoring and sensitivity math in a Gemini skill is unproven | gm-11 | Gate 2 proof: run a sensitivity test in a Gemini skill on a personal and a Workspace account |
| G2-2 | Gemini: no doc says a skill can use Google Search. Deep Research does not work in skills | gm-06, gm-01 | Gate 2 proof. Fallback: learner uploads the new source |
| G2-3 | Gemini: file output from a skill run is still unproven (carried open item) | gm-09 | Gate 2 proof |
| G2-4 | ChatGPT: spreadsheet output is documented only for ChatGPT Work (paid plans, not Free or Go). Download from plain data analysis in a Project is not documented. Conflicts with the Market Research decision "Go or Plus minimum" for file output labs | cg-09, cg-10, cg-11 | Dan decides: Plus minimum, or on-screen tables for Go. Test Work inside a Project with default memory |
| G2-5 | ChatGPT: plans for data analysis and deep research are not named on the vendor pages | cg-11, cg-12 | Retry the plans comparison page next run |
| G2-6 | ChatGPT skills still Business, Enterprise, Healthcare, Edu only (cg-04 retry). Skills page date did not move since 2026-11-20 ("13 days ago"), so its true date is uncertain | cg-04 | Verifier to confirm the page date |
| G2-7 | Catch-up copy features (retry): still no copy, duplicate or template feature for ChatGPT Projects. Not rechecked for Claude or Copilot | cg-01 | Keep the text catch-up kit (Market Research decision e) |
| G2-8 | Copilot: not documented if code interpreter can read the agent's knowledge files (embedded or SharePoint). Output files last for one session | mb-13, mb-11 | Gate 2 proof with an embedded .xlsx |
| G2-9 | Copilot agent builder scheduled workflows: still no Microsoft-hosted source. The Microsoft roadmap API page returned binary data | mb-06 | Retry with the Microsoft 365 roadmap site or Message Center |
| G2-10 | Claude: two pages disagree on upload size (500 MB chat vs 30 MB) | cl-up-10, cl-fo-06 | Use 30 MB. Verifier to check |
| G2-11 | Claude: web search and Research pages do not say if they work in a skill or a Cowork scheduled task | cl-ws-08, cl-rs-09 | Gate 2 proof (stretch only) |
| G2-12 | Memory isolation for a "blind" second scorer run not checked for Copilot and Gemini | cg-14 | Check vendor memory pages next run |
| G2-13 | No 2026 study found that compares agent-manager methods (sensitivity tests, scorer consistency checks, trace-to-source) for AI-assisted prioritization. Methods are design choices, not findings | methods.md | Evidence track may search. Not a blocker |
| G2-14 | Not opened (budget): ChatGPT scheduled tasks page (can a task use a skill or Work), Gemini in Sheets spreadsheet post, last part of ChatGPT release notes | not_opened list | Next run |

## Track 1: workflows

Written 2026-11-22 by the workflow researcher. File: `research/workflows.yaml` (10 rows). Fetch budget: 25 of 25 used.

### Context gaps (hardware and internal PM)

| Row | Hardware | Internal PM |
| --- | --- | --- |
| sp-wf-01 strategy drift check | Partial (W22, vendor) | gap |
| sp-wf-02 opportunity re-scoring | Partial (W6, vendor, figures not usable) | gap |
| sp-wf-03 market size model | gap | gap |
| sp-wf-04 concept test results | gap | gap |
| sp-wf-05 assumption register | Partial (W15 aged, W6 vendor) | Partial (W23, public sector) |
| sp-wf-06 buy, build or partner pack | gap | Partial (W16, W18, context only) |
| sp-wf-07 roadmap theme refresh | Partial (W19) | Partial (W24, 2023, aged) |
| sp-wf-08 roadmap change notes | Partial (W19) | gap |
| sp-wf-09 portfolio review pack | Partial (W22, W19) | Partial (W1, Expedia anecdote) |
| sp-wf-10 outcome tracking | gap | Partial (W23, public sector) |

### Source gaps

1. Most bottleneck sources are vendor or consultancy blogs with no data. Only W2, W3, W12, W14 and W18 hold survey data, and none is fully verified.
2. W2 (Atlassian strategic portfolio study, 308 leaders): publish date and method not stated. Confirm it is a 2026 study.
3. W3 (Product-Led Alliance State of PM 2026): primary report not opened.
4. W20 (ProdPad): figures come from a "2026 State of B2B Product Management survey". Not opened.
5. sp-wf-04 concept tests: no 2026 source specific to concept test analysis. W12 is about research in general. Weak pass.
6. sp-wf-05 business case: W14 polls valuation practitioners, not PMs. W15 is from 2024 (age flag). No 2026 product-team source.
7. sp-wf-02 scoring: both sources (W4, W5) are unsigned and have no data.
8. Age-flagged sources for Dan to decide: W9 (2025-04-21), W10 (2023), W15 (2024), W21 (2019), W24 (2023).

### Scope questions for Dan

1. sp-wf-04 maps to skill 6.4 (Design course), not Capability 2. Keep, move or drop.
2. sp-wf-01 and sp-wf-09 use the same data for different jobs. Merge or keep both.
3. sp-wf-01 is close to the Focus 28.01 tip "use AI to check roadmap updates against the Strategy Matrix and OKRs".
4. sp-wf-02 tag: the workbook primary box for 2.2 is Market / Competitive Landscape. The row uses Focus / Product Portfolio.
5. sp-wf-07 may overlap the partner course Mastering the Product Roadmap. Not checked.

### Not opened (budget reached)

- Pragmatic Institute, Managing Internal Feature Requests (internal PM lead)
- ideaplan, How to prioritize internal tool requests (internal PM lead)
- Atlassian whitepaper behind W2; Product-Led Alliance State of PM 2026 report behind W3
- Retool 2026 AI build vs buy report (cited in W16)
- TechTarget, Build vs. buy AI: a CIO's decision matrix
- Deloitte, semiconductor product management solutions; Built In, AI hardware product management guide (hardware leads)
- New Zealand Treasury Investment Realisation guidance (cited in W23)
- Market Research ledger E6 to E9 (platform features): not re-verified in this run
