# PM needs: Advanced AI for Product Strategy and Planning (track 3)

- Course: product-strategy-and-planning
- Researcher: Stage 1, track 3 (PM needs)
- Date: 2026-11-22
- Question: what do PMs and product leaders do in product strategy, opportunity prioritization, business cases, roadmaps and annual or quarterly planning? How often? Where does the time go? Where does AI help or hurt? Which decisions must stay with the PM?
- Scope: Pragmatic capability 2, Strategic Direction (skills 2.1 to 2.4). Framework boxes: Market / Product Strategy, Focus / Product Portfolio, Focus / Product Roadmap, Business / Business Plan, Business / Business Outcomes and nearby boxes.

## How to read this file

1. Source ids are `N<n>`. The ledger is at the end of the file.
2. "Weak" means a vendor source, an unknown sample or an unclear method. Do not put a weak statistic on a slide.
3. Statistics from studies before 2026 are dropped. The dropped list is at the end.
4. Sources older than 12 months have `age_flag: true`. Dan decides if they stay.
5. N3, N11 and N20 were opened and checked in the Market Research run on 2026-11-20. This run did not open them again. The ledger says so.
6. Name collision: "planning" in this file means annual and quarterly planning. It is not the Framework category "Planning". Tags use the Framework names.
7. Limit of this run: the 20-fetch budget is used. Many 2026 reports show only a landing page. Their full PDFs are listed under "Not opened".

## Summary in 7 points

1. Strategy gets little time. Only 25% of 677 product people spend most of their time on strategy, and about 60% often do unplanned work (N3). 34% of 107 product leaders say finding time for strategic thinking is a challenge (N20).
2. Prioritization gets overridden. A vendor survey of 250 leaders says over 60% of prioritization frameworks are overridden by leadership escalations (N5, weak). Atlassian says gut instinct still overrides customer data (N7, weak). SiriusXM platform PMs say teams used different assumptions, which caused roadmap conflicts (N12).
3. Plans break because they are treated as contracts. Practitioners say annual plans are over-detailed, made in a leadership bubble and not used in weekly work (N9). Pragmatic and Forrester say: plan outcomes, use flexible timeframes, update as priorities change (N1, N2, N15).
4. The replanning loop costs the most repeated time. Named time sinks: status collection meetings, "what happened to my request?" emails, realignment meetings after a shift (N9). Capacity constraints are the top cause of roadmap misalignment for 49% of teams (N6, secondary report of a vendor survey).
5. AI is used for drafts, not decisions. 72% of respondents use AI for content, 48% for data analysis, but only 18% trust it for decision support or prioritization (N8, weak). 97% say AI improved their own productivity, but only 64% say it improved product outcomes (N4). PMs say AI helps teams ship faster, but customers do not see value sooner (N7, weak).
6. PMs and leaders keep the choices. Strategy is a set of choices that AI does not make (N13). 86% of PMs say deciding what to build matters more than ever (N7, weak). Pragmatic: teams verify AI output and stay accountable (N1).
7. Hardware is a priority and has real but thin evidence: the cost of a wrong commit becomes almost vertical after tooling (N10, N11). Internal PM has one strong 2026 practitioner case (N12). Services and health care have no task or time data for this topic (gap).

## Task table

Frequency is the cadence that sources state or advise. "Assumption" means no source states it.

| # | Task | Who | How often | Time pain | Pragmatic 2027 tag | Sources |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Write and refresh the product strategy: the choices on who to serve, which problems, what sets us apart, what we say no to | Product leader, senior PM | Yearly in annual planning (N9). Revisit when the market changes (N1) | Only 25% spend most time on strategy (N3). 34% of leaders lack time for strategic thinking (N20). Strategy often ends up as a vision slide, a roadmap or a feature list, not choices (N13). ProductPlan names "three hidden time sinks" in strategy work but does not say what they are on its page (N5, weak) | Market: Product Strategy | N1, N3, N5, N13, N20 |
| T2 | Score and rank opportunities against strategy (criteria, weights, evidence, sensitivity) | PM, product leader | Each planning cycle. Quarterly in most sources (N9). Assumption: also ad hoc for big requests | Over 60% of frameworks are overridden by leadership escalations (N5, weak). Gut instinct overrides customer data (N7, weak). Teams score on different assumptions, so roadmaps conflict (N12). Only 18% trust AI for prioritization (N8, weak) | Market: Competitive Landscape; Focus: Product Portfolio | N5, N7, N8, N12 |
| T3 | Build the business case or business plan (problem, market, costs, value, risks), then keep it current | PM, with finance | Per new product or major release. Pragmatic: "present your findings early and keep the plan current" (N1) | Gap: no 2026 source on hours spent. Leaders now ask for proof of value in outcome terms (N15, N16). Hardware: a late wrong commit turns into tooling and stock write-offs (N10, N11) | Business: Business Plan; Business: Buy, Build or Partner | N1, N10, N11, N15, N16 |
| T4 | Annual planning: set outcomes and themes, allocate budget and capacity | Product leader, PMs, finance, engineering | Yearly, with a mid-year check (N9). Budget planning season for 2027 started by July 2026 (N15) | Plans fail when they are a 12-month contract, built in a leadership bubble and not used in weekly work (N9). More than half of chief strategy officers have too many priorities and too little time (N14, not PMs). Many firms still plan by features, not outcomes (N15) | Focus: Product Portfolio; Focus: Product Roadmap; Business: Business Outcomes | N9, N14, N15 |
| T5 | Quarterly replanning and roadmap update after a change (new request, slip, market shift) | PM | Quarterly reset, weekly progress review (N9). Pragmatic: regular review cycles; update as priorities change (N1, N2) | Repeated time sinks: status collection meetings, realignment meetings, request follow-up emails (N9). About 60% often do unplanned work (N3). 49% name capacity constraints as the top cause of roadmap misalignment (N6, secondary, weak) | Focus: Product Roadmap | N1, N2, N3, N6, N9 |
| T6 | Tailor the roadmap and plan story for each audience (executives, sales, engineering, customers) | PM | Each roadmap update | Under-communicating silos key people (N2). Strategy does not land with Sales and Customer Success, a "confidence gap" (N5, weak). AI already does much content work: 72% use it for content generation (N8, weak). No-repeat flag: Focus 28.01 already has "one roadmap, two audiences" as an AI activity | Focus: Product Roadmap; Planning: Stakeholder Management | N2, N5, N8 |
| T7 | Take in and triage requests (sales, customers, internal teams) against the plan | PM, product ops | Continuous | Vendor case: Autodesk merged 70 or more request channels into one system (N9, weak). Unplanned escalations and sales commitments break plans (N9). Internal platform teams get conflicting asks on developer pain, reliability and cost (N12) | Focus: Product Roadmap; Planning: Stakeholder Management | N9, N12 |
| T8 | Allocate the portfolio across horizons (core, emerging, new bets; legacy vs AI features vs AI innovation) | Product leader, CPO | Yearly, in annual planning. Assumption: checked mid-year | Gap: no time data. Gartner advises CPOs to balance three investment areas (N16, weak). Pragmatic: map each offer by lifecycle stage and allocate by strategy (N1) | Focus: Product Portfolio | N1, N16 |
| T9 | Track outcomes against the plan and the business case | PM, product leader | Monthly or quarterly. Assumption | 66% say measuring success is their biggest unresolved challenge (N8, weak). Teams ship faster with AI, but customers do not see value sooner (N7, weak). Forrester: success is still judged by launches and features, not outcomes (N15) | Business: Business Outcomes; Business: Measurement | N7, N8, N15 |
| T10 | Hardware: set commit points (prototype, soft tooling, hard tooling, production) and test the riskiest assumption before each one | Hardware PM, engineering | Each stage gate | Cost of error is "nearly vertical" after steel tooling is cut (N10). Late answers to customer and budget questions cost tooling, certification and unsold stock (N11) | Focus: Product Roadmap; Business: Business Plan | N10, N11 |
| T11 | FinTech: keep risk and compliance work visible on the roadmap and score it by regulatory exposure | PM, engineering leader | Each planning cycle | One source only. Risk work competes with features for capacity (N6, weak). Gap: no second source | Focus: Product Roadmap | N6 |
| T12 | Refresh the market size and segment model for the plan (carry-over of mr-wf-06) | PM | Yearly or per business case. Assumption | Gap: no 2026 source on time spent. Not researched in this run (budget) | Focus: Market Definition | none |

## Top 8 tasks by time pain

Rank is by repeated time cost and the strength of the evidence. It is a judgment, not a measure.

| Rank | Task | Why |
| --- | --- | --- |
| 1 | T5 Quarterly replanning and roadmap update | Most frequent. Named, repeated time sinks (N9). Unplanned work for about 60% (N3) |
| 2 | T2 Score and rank opportunities | Work is wasted when it is overridden (N5) or based on different assumptions (N12) |
| 3 | T4 Annual planning | Large, once a year. Plans break by Q2 (N9). Leaders short of time (N14) |
| 4 | T1 Write and refresh the strategy | Least time given to it (N3, N20). Output often not a strategy (N13) |
| 5 | T7 Take in and triage requests | Continuous. Many channels (N9). Conflicting internal asks (N12) |
| 6 | T6 Tailor the roadmap story | Each update. Overlaps Focus 28.01, so use with care |
| 7 | T9 Track outcomes against the plan | Top unresolved challenge in one weak survey (N8) |
| 8 | T3 Build the business case | High stakes, low frequency. No time data (gap) |

## Where AI helps or hurts (what PMs say)

| Finding | Figure or claim | Sources | Status |
| --- | --- | --- | --- |
| Frequent AI use by product people rose | 49% (2025) to 69% (2026) | N4 | partly verified (publisher's own article on its survey) |
| AI helps the person more than the product | 97% say productivity improved; 64% say product outcomes improved | N4 | partly verified |
| AI use is mostly drafting | Content 72%, workflow automation 52%, data analysis 48% | N8 | weak (sample unknown) |
| Low trust for prioritization | 18% trust AI for decision support or prioritization | N8 | weak |
| Faster shipping, not faster value | Headline claim, no figure | N7 | weak |
| Messy input gives "confident nonsense" | Practitioner quote (Payoneer director) | N8 | practitioner view, 1 source |
| AI exposes a weak strategy; it does not fix it | Practitioner claim | N13 | practitioner view |
| AI can surface the assumptions behind past decisions | SiriusXM platform team uses AI to synthesize signals and expose assumptions | N12 | practitioner case |
| Leaders see AI as a strategy partner | 51% of chief strategy officers; 16% use AI to reimagine business lines | N14 | partly verified (press release, sample not stated) |
| Few teams set goals for AI | 6% set AI OKRs; 70% use AI 5 or more hours a week | N17 | weak (vendor, 157 people) |

## Tasks PMs want to keep, and why

| Kept task | Why | Sources |
| --- | --- | --- |
| Make the strategy choices (who, which problems, what sets us apart, what we say no to) | AI "does not decide what they should build". Product leaders own product strategy | N13, N1 |
| Decide what to build | 86% of PMs say this matters more than ever | N7 (weak) |
| Set weights and final priorities | Only 18% trust AI for prioritization (N8). At SiriusXM, platform leaders keep "context and governance" while AI synthesizes (N12). Workbook skill 2.2 says the same (stage-1 inputs) | N8, N12 |
| Keep the roadmap a direction, not a promise | Plans used as contracts fail (N9). Pragmatic: flexible formats, update as priorities change (N1, N2). Workbook skill 2.4: do not turn uncertain direction into false delivery commitments | N1, N2, N9 |
| Own the business case numbers and stay accountable | Pragmatic: verify AI output, protect sensitive information, stay accountable (N1). Workbook skill 2.3: data and calculations stay auditable. Gap: no 2026 practitioner source on business case review | N1 |
| Make irreversible hardware commits | Advance a stage "only when evidence supports it", not when the calendar says so (N10). "AI can produce work; it can't carry the outcome" (N11) | N10, N11 |
| Choose the outcome measures | Leaders must pick the measures that prove value (N15). Payoneer picks the KPIs that show impact (N8) | N8, N15 |

Course implication (for the Synthesizer, not a finding): the PM keeps the choices, the weights, the commitments and the sign-off. The agent can take the repeated loop: gather signals, re-score against the PM's stated criteria, flag scoring that does not match the strategy, draft the replan impact note and keep the assumption log. T5, T2 and T7 together are the strongest repeated-time case. This starts where Focus 28.01 stops (one-pass drafts).

## Findings by industry

| Context | What we found | Sources | Gap? |
| --- | --- | --- | --- |
| Hardware (priority) | 47.6% of Product Focus respondents work on hardware or physical products (N3). Hardware PMs commit in stages: paper, prototype, soft tooling, hard tooling, production. The cost of a wrong decision is "nearly vertical" after tooling. Examples of early commits that failed: Better Place, Humane AI Pin, Rabbit R1 (N10). Late answers cost tooling, certification and stock (N11) | N3, N10, N11 | Partial. No 2026 data on how long hardware roadmaps or stage-gate business cases take. No source on long supplier lead times in plans |
| Manufacturing | Forrester: portfolios get more complex and ad hoc launch processes will not scale (N15). No source on manufacturing PM planning tasks | N15 | Yes. No task or time data |
| Internal PM, internal platforms (priority) | 20% of Product Focus respondents build internal products (N3). SiriusXM platform PMs treated prioritization "like a product problem". They score developer pain, reliability risk and executive cost concerns, keep a "living artifact" of validated assumptions, and use AI to synthesize signals. Leaders keep governance. Lessons from 200 or more decisions (N12). For internal products, distribution means access and rollout, and pricing means funding and cost allocation (N1) | N1, N3, N12 | Partial. One strong case, no time data. No second source on internal annual planning |
| Software (B2B SaaS) | Most sources describe software teams (N5, N7, N8, N9) | N5, N7, N8, N9 | No. But most figures are vendor surveys with no method |
| FinTech | Roadmaps carry risk work beside features, scored by likelihood, impact, regulatory exposure and effort. DORA applies to EU financial firms. The article reports FINRA advice to block sensitive data from vendor AI tools by contract (N6). Payoneer: track outcome KPIs to show a tool pays for itself (N8) | N6, N8 | Partial. 1 source per claim. FINRA primary not opened |
| Health care | No source on health care PM strategy, roadmap or business case work in this run. HHS de-identification rules apply to PHI in business case data (N19) | N19 | Yes. No task or time data. Focus 28.01 already uses a health care case (DeepView AI) |
| Services | No source found. Leads not opened: MIT Sloan on turning services into products, TSIA State of Professional Services 2026 | none | Yes |
| Leaders outside product | Chief strategy officers: more than half have too many priorities and too little time; 35% co-lead or own strategic decisions; 51% see AI as a strategy partner (N14) | N14 | Context only. Not PMs |

## Data risks by industry

| Industry | Data in strategy, business cases and plans | Risk | Sources |
| --- | --- | --- | --- |
| All | Unreleased roadmaps, revenue forecasts, pricing, cost models, buy, build or partner targets, customer names in request logs | Confidential company data and client data in an unapproved AI tool. Pragmatic: protect sensitive information | N1 |
| Public companies, all industries | Revenue forecasts, guidance inputs, acquisition targets in business cases and annual plans | Material non-public information. Skadden covers financial firms and advises data walls, access limits and audit trails for AI models. Applying this to product plans in other public firms is an inference. Check with legal | N18 (inference beyond its scope) |
| FinTech, banking | Customer account data in sizing, risk registers, vendor contracts | PII, payment data (PCI), DORA controls. FINRA advice on contract terms that stop sensitive data going to vendor AI tools (reported by N6) | N6, N18 |
| Health care | Patient volumes, claims, outcomes data used for market size and value | PHI under HIPAA. De-identify first (Safe Harbor removes 18 identifier types). Small cell counts can still identify people | N19 |
| Hardware and manufacturing | Supplier quotes, bill of materials costs, OEM and channel partner contracts, tooling costs | Partner and supplier confidential data, contract terms | Gap: no source. Inference |
| Internal PM | Headcount plans, cost allocation, employee survey data, internal tool usage by person | Employee PII and HR data | Gap: no 2026 source. Inference |
| Services | Client names, fees, engagement data in a productization case | Client confidential data | Gap: no source. Inference |

## Evidence ledger

```yaml
- id: N1
  claim: >-
    Product strategy sets long-term direction and the choices that guide decisions; revisit it when the market changes and use it to
    say no. Portfolio: map offers by lifecycle and allocate by strategy, with a horizon view. Roadmap: gather input, set goals and
    measures, prioritize, choose a flexible format, tailor detail per audience, update as priorities change. Business plan: helps
    leaders fund, delay or stop; present early and keep current. For internal products, distribution is access and rollout and
    pricing is funding and cost allocation. AI: verify outputs, protect sensitive information, stay accountable
  type: claim
  source: Product Professionals' Guide to the Pragmatic Framework, refreshed for 2027, Pragmatic Institute
  url: /mnt/project-files/course-builder/reference/pragmatic-sources/Pragmatic-Framework-2027-Guide.pdf (pages 4, 6, 8, 9, 10; read from extracted text fw.txt)
  source_date: 2026-11-11
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: Pragmatic primary source. Framework guidance, not a study
- id: N2
  claim: >-
    Roadmap steps: plan, gather requirements, choose a dated, undated or hybrid format, prioritize (MoSCoW, Kano, RICE, cost of delay,
    OKR alignment), communicate with tailored versions, maintain and update. Set regular review cycles. Under-communicating silos key
    contributors. No mention of AI
  type: claim
  source: How to Build a Product Roadmap, Pragmatic Institute Editorial Team
  url: https://www.pragmaticinstitute.com/resources/articles/product/how-to-build-a-product-roadmap/
  source_date: 2024-07-30 (last modified)
  checked_on: 2026-11-22
  age_flag: true
  status: verified
  note: Pragmatic material. Older than 12 months. Use for method only
- id: N3
  claim: >-
    25% spend most time on strategy; about 60% often do unplanned work; 47.6% work on hardware or physical products; 20% build
    internal products; 71% do not spend enough time with customers or the market
  type: statistic
  source: Survey of the Product Management Profession 2026, Product Focus
  url: https://www.productfocus.com/wp/wp-content/uploads/2026/03/Product-Focus-Industry-Survey-Report-2026.pdf
  source_date: 2026-03 (URL path)
  checked_on: 2026-11-20 (Market Research run, ledger N5 there). Not reopened 2026-11-22
  age_flag: false
  status: verified (2026-11-20)
  note: >-
    Primary. 677 respondents, 40 countries, 83% Europe, 8% US. Fieldwork Oct 2025 to Jan 2026, published 2026. Online survey.
    Skews European. Check the 47.6% figure in the PDF before a slide
- id: N4
  claim: >-
    Frequent AI use among product people rose from 49% (2025) to 69% (2026). 97% say AI improved personal productivity; 64% say it
    improved product outcomes (the "33-point gap"). 8% have all five organisational conditions in place
  type: statistic
  source: Product Management, Amplified Part 1, The 33-Point Gap, Shivany Ria, Product Focus
  url: https://www.productfocus.com/product-management-amplified-part-1-the-33-point-gap/
  source_date: 2026-04-08 (modified 2026-06-05)
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified
  note: >-
    Article by the survey publisher on its own 2026 survey (same data as N3: 677 respondents, 40 countries). These AI figures were not
    checked in the PDF. Comparison group for the 44% vs 9% figure is not defined, so it is not used
- id: N5
  claim: >-
    Over 60% of prioritization frameworks are overridden by leadership escalations. Three hidden time sinks drain PMs in strategy
    work (not named on the page). A confidence gap stops strategy landing with Sales and Customer Success. Roadmap misalignment has one
    dominant cause (not named on the page)
  type: statistic
  source: The State of Product Management Report 2026, ProductPlan
  url: https://www.productplan.com/ebooks/the-state-of-product-management-report-2026
  source_date: 2026 (no exact date on page)
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: >-
    Vendor (roadmap software). 250 product leaders. Population detail, period and method not on the landing page. Gated PDF not opened.
    Do not put on a slide until the PDF is checked
- id: N6
  claim: >-
    FinTech teams keep technical and regulatory risk on the roadmap beside features and score it by likelihood, impact, regulatory
    exposure and effort. 49% of teams name capacity constraints as the top cause of roadmap misalignment (citing ProductPlan 2026
    research). DORA applies to EU financial entities from 2025-01-17. FINRA advises contract terms that stop sensitive data going
    into vendor AI tools
  type: claim
  source: How to Navigate Technical Risk Management in FinTech Product Delivery, Jennifer Haley, ProductPlan blog
  url: https://www.productplan.com/blog/how-to-navigate-technical-risk-management-in-fintech-product-delivery
  source_date: 2026-08-18
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: >-
    Vendor blog. The 49% figure is a secondary report of N5 data (same vendor); primary not opened, so it is weak. FINRA guidance
    reported, primary not opened. Only FinTech source in this run
- id: N7
  claim: >-
    86% of PMs agree deciding what to build matters more than ever. PMs say AI helps teams ship faster but customers do not see value
    sooner. Gut instinct still overrides customer data
  type: statistic
  source: The State of Product 2027, Atlassian
  url: https://www.atlassian.com/software/jira/product-discovery/resources/state-of-product-2027 (also https://www.atlassian.com/sop)
  source_date: 2026 (page copyright 2026; no exact date)
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: >-
    Vendor. 1,000 product professionals. Countries, period, firm and method not stated on the page. Full report not opened. The
    State of Product 2026 edition was dropped in Market Research because its data was from 2025; check the fieldwork year of this one
- id: N8
  claim: >-
    66% say measuring success is their biggest unresolved challenge. AI use: 72% content generation, 52% workflow automation, 48%
    data analysis, 18% trust AI for decision support or prioritization. Practitioners: messy inputs give "confident nonsense";
    Payoneer tracks outcome KPIs to show a tool pays for itself
  type: statistic
  source: How product workflows drive strategic decisions in 2026, Productboard blog (webinar with Ross Webb and Elena Levi, Payoneer)
  url: https://www.productboard.com/blog/how-product-workflows-drive-strategic-decisions-in-2026/
  source_date: 2026-02-18
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: Vendor. Survey sample, population, period and method not stated. Use the figures only as a lead. Quotes are fine as practitioner views
- id: N9
  claim: >-
    Planning cadence: annual vision and bets, mid-year check, quarterly reset, weekly review. Time sinks: firefighting, unplanned
    escalations and sales commitments, status collection meetings, request follow-up emails, realignment meetings. Plans fail when
    treated as a 12-month contract, built in a leadership bubble and not embedded in work. Autodesk case: 70 or more request channels
    merged; assignment rate 6% to 100%
  type: claim
  source: Why your product plans fall apart by Q2, Product-Led Alliance (sponsored by Productboard)
  url: https://www.productledalliance.com/why-your-product-plans-fall-apart-by-q2/
  source_date: 2026-01-07 (modified 2026-03-13)
  checked_on: 2026-11-22
  age_flag: false
  status: verified, vendor
  note: >-
    Sponsored vendor article, no named author. No survey data. Autodesk figures are a vendor case, not audited. The "plans as
    contracts" claim is backed by N2 and N15 (independent), so it meets the 2-source rule
- id: N10
  claim: >-
    Hardware decisions commit in stages (paper, prototype, soft tooling, hard tooling, production). Advance only when evidence
    supports it. Cost of error is nearly vertical after steel tooling. Better Place, Humane AI Pin and Rabbit R1 committed too early
  type: claim
  source: Learn early, commit late, de-risking hardware in a software world, Yoel Frischoff, Mind the Product
  url: https://www.mindtheproduct.com/learn-early-commit-late-de-risking-hardware-in-a-software-world/
  source_date: 2026-10-08
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: Practitioner (product strategist, 35+ years in industrial design and engineering). No data. Independent of N11
- id: N11
  claim: >-
    In high-tech hardware, customer and budget questions get skipped; late misalignment costs tooling, certification and unsold
    stock; "AI can produce work; it can't carry the outcome"
  type: claim
  source: Here's why systems architects love product managers with no blah blah, Howard Lettinga, Bits&Chips
  url: https://bits-chips.com/magazine/bc202607/?pagenr=15
  source_date: 2026-10-23
  checked_on: 2026-11-20 (Market Research run, ledger N6 there). Not reopened 2026-11-22
  age_flag: false
  status: verified (2026-11-20)
  note: Trade magazine (Netherlands). Do not use its statistics (they seem to come from N3)
- id: N12
  claim: >-
    SiriusXM platform PMs treated prioritization as a product problem. Teams used different assumptions about users and data, which
    caused roadmap conflicts. The framework scores developer pain, reliability risk and executive cost concerns, links the roadmap to
    strategy, and keeps validated assumptions in a living artifact. AI synthesizes signals and surfaces past assumptions; platform
    leaders provide context and governance
  type: claim
  source: Prioritization as Code, an AI-supported framework for platform engineering, Mina Tawadrous and Eleanor Millman (SiriusXM), DX Annual 2026
  url: https://getdx.com/dxannual/sessions/prioritization-as-code/
  source_date: 2026-04-16
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: Conference session abstract by practitioners. No time data. Rubric and lessons from 200+ decisions are in the talk, not the page
- id: N13
  claim: >-
    Asked for strategy, leaders show a vision, a roadmap, a feature list or a pillar slide. Strategy is the choices on who to serve,
    which needs, what differentiates and how value is created. AI "does not decide what they should build"; "AI will not fix a weak
    strategy. It will expose it"
  type: claim
  source: Ten Product Leaders, Ten Documents, No Strategy, Robbin Schuurman with Hamza El Uamari (KLM), Xebia
  url: https://xebia.com/articles/ten-product-leaders-ten-documents-no-strategy/
  source_date: 2026-11-05 (updated; original date not shown)
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: Consultancy article (Xebia sells training). Practitioner view. "AI does not decide" is backed by N1 and N7 as well
- id: N14
  claim: >-
    More than half of chief strategy officers manage too many priorities with too little time; 35% co-lead or own strategic decisions;
    28% co-lead AI decisions; 51% see AI as a strategic partner; 16% use AI to reimagine lines of business
  type: statistic
  source: Deloitte 2026 Chief Strategy Officer Survey, press release
  url: https://www.deloitte.com/us/en/about/press-room/deloitte-2026-chief-strategy-officer-survey.html
  source_date: 2026-02-12
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified
  note: >-
    Sample, countries, period and method not on the press release. Full report found, not opened:
    https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/programs/2026/us-2026-global-cso-survey-report.pdf. CSOs, not PMs
- id: N15
  claim: >-
    Product and portfolio teams must move from feature-centric planning to customer-outcome value delivery for 2027 budgets. 62% of
    portfolio marketing decision-makers report cookie-cutter, ad hoc or no launch processes. Leaders must pick outcome measures and
    which agent pilots to start
  type: claim
  source: Budget Planning 2027, Portfolio Marketing And Product Management Must Be Primed For AI-Era Innovation, Amy Hayes, Forrester blog
  url: https://www.forrester.com/blogs/budget-planning-2027-portfolio-marketing-and-product-management-must-be-primed-for-ai-era-innovation/
  source_date: 2026-07-10 (modified 2026-08-04)
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified
  note: Analyst blog. The 62% has no sample or period on the page; do not use it on a slide. Advice is analyst opinion
- id: N16
  claim: >-
    Half of CPOs say under 30% of their customers use AI features; nearly half attribute revenue growth to non-AI features. CPOs
    should balance investment across legacy products, revenue-generating AI features and AI innovation, and co-create AI use cases
    with customers so the roadmap matches real needs
  type: statistic
  source: Top priorities for chief product officers 2026, Gartner
  url: https://www.gartner.com/en/product-management/insights/top-priorities-for-chief-product-officers-2026/unlocked
  source_date: unknown (2026 by title)
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: No date, sample or method on the page. Analyst firm. Use the advice, not the figures
- id: N17
  claim: 99% of product professionals use AI at work; 70% spend 5 or more hours a week with AI; 6% set AI OKRs; access is the top blocker (30%)
  type: statistic
  source: The State of AI in Product Management 2026, UXCam
  url: https://uxcam.com/resources/ebooks/ai-in-product-management-2026/
  source_date: 2026-06-24
  checked_on: 2026-11-22
  age_flag: false
  status: partly verified, weak
  note: Vendor (product analytics). 157 product professionals in 34 countries. Period and sampling not stated. Not about strategy tasks
- id: N18
  claim: >-
    Financial firms face MNPI risk when AI models can reach nonpublic information. Advised controls: data walls by deal team or
    issuer, limit which users and models reach restricted data, approval steps, audit trails, explainability. Written instructions
    alone may not be enough
  type: claim
  source: When AI Models Access Nonpublic Information, MNPI Risks for Financial Firms, Skadden (Daniel Michael and others)
  url: https://www.skadden.com/insights/publications/2026/07/when-ai-models-access-nonpublic-information
  source_date: 2026-07-21
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: >-
    Law firm client alert. Written for broker-dealers and investment advisers. Use for other public companies is an inference; Dan
    or legal must confirm before a slide says it
- id: N19
  claim: >-
    HIPAA de-identification has two methods: Expert Determination and Safe Harbor (remove 18 identifier types). Aggregation does not
    always make data safe; small cell counts are a concern
  type: claim
  source: Guidance regarding methods for de-identification of PHI, US HHS
  url: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
  source_date: 2012-09-07 (last modified 2026-03-20)
  checked_on: 2026-11-22
  age_flag: false
  status: verified
  note: Government primary. First issued 2012 but modified 2026-03-20, so not flagged. Last 9% of the page not read
- id: N20
  claim: 34% of senior product leaders say finding time for strategic thinking is a challenge
  type: statistic
  source: The State of Product Leadership 2026, Delight Path
  url: https://www.delightpath.com/product-leadership-report-2026
  source_date: 2026 (Q2 2026 survey)
  checked_on: 2026-11-20 (Market Research run, ledger N7 there). Not reopened 2026-11-22
  age_flag: false
  status: partly verified
  note: 107 leaders, 64% director or above, 50% North America. Report page preview only; full PDF not opened. Skews to AI-engaged leaders
```

### Not opened (fetch budget used)

| Item | URL | Why it matters |
| --- | --- | --- |
| ProductPlan State of PM 2026 full PDF (N5) | https://www.productplan.com/ebooks/the-state-of-product-management-report-2026 | Names the 3 strategy time sinks and the top cause of roadmap misalignment. Verify the 60% and 49% figures |
| Atlassian State of Product 2027 full report (N7) | https://www.atlassian.com/sop | Method, fieldwork year, AI and prioritization figures |
| Deloitte 2026 Global CSO Survey report (N14) | https://www.deloitte.com/content/dam/assets-zone3/us/en/docs/programs/2026/us-2026-global-cso-survey-report.pdf | Sample and method; strategy process data |
| California Management Review, When AI joins the product team (2026-02) | https://cmr.berkeley.edu/2026/02/when-ai-joins-the-product-team-will-leadership-still-drives-innovation/ | Academic view on what leaders keep |
| Productboard, CPO blueprint for annual planning | https://productboard.com/blog/the-cpos-blueprint-for-annual-planning-part-1 | Second source on annual planning steps (vendor, check date) |
| airfocus, platform PM strategic investment | https://airfocus.com/blog/platform-product-management-strategic-investment/ | Second internal PM source |
| Mind the Product, launch a FinTech product with compliance | https://www.mindtheproduct.com/how-to-launch-a-fintech-product-in-alliance-with-compliance/ | Second FinTech source (check date) |
| TSIA State of Professional Services 2026 | https://www.tsia.com/ebooks/state-of-professional-services-2026 | Services gap |
| MIT Sloan, How to turn professional services into products | https://sloanreview.mit.edu/article/how-to-turn-professional-services-into-products | Services gap |
| Lenny's Newsletter AI productivity survey | https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results-c08 | Check date; may have PM task-level AI time data |
| Galorath 2026 State of the Industry (estimation) | https://galorath.com/soti. | Possible business case cost estimate data |
| Pragmatic, Four methodologies for prioritizing roadmaps | https://www.pragmaticinstitute.com/resources/articles/product/four-methodologies-for-prioritizing-roadmaps | Pragmatic material on prioritization |

### Dropped

| Source | Reason |
| --- | --- |
| Productboard AI in Product Management report (379 enterprise product professionals; 4 hours saved per task; roadmap creation a top time-saver) | Published 2025-10-22. 2025 study |
| General Assembly AI and product management survey (117 PMs), reported by Dice | Published 2025-11-13. 2025 study |
| Atlassian State of Product 2026 | Data from 2025 (dropped in Market Research). Use the 2027 edition (N7) |
| Deloitte State of Product Survey 2026 | Not published yet ("coming soon" page) |
