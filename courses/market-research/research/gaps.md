# Gaps


## Track 4: evidence

Written 2026-11-20 by the evidence researcher. Ledger: `evidence-ledger.yaml`. Sources: `sources.yaml`.

| # | Gap | What exists | Effect |
| --- | --- | --- | --- |
| 1 | No non-vendor 2026 study that measures synthesis time for PM or market research work | E13 (preprint, policy researchers, about 10x faster), E14 (nurse interviews, "significantly less time", no figures). E12 found no time saved in a chat workflow | Speed claim in mr-wf-01 rests on vendor data (E1, E2, E10). Partly closed. Say "faster, but the gain depends on the workflow" |
| 2 | No 2026 rate for invented or reworded quotes | E5 has 3 sources for the risk (Torres 2025, JMIR 2026 pilot, Condens 2026 respondents). No rate | Teach the risk and the quote check. Do not state a percentage |
| 3 | Internal product management: no case study found | None | Gap. Dan's own examples fill it |
| 4 | Hardware: only vendor customer stories (E26 CNH, E27 power tools, E29 HP, E28 building products). All undated or self-reported | 4 vendor or consultancy cases | Usable as examples, not as proof. No independent hardware source |
| 5 | Market sizing: no 2026 study on AI accuracy for TAM or market sizing | Vendor blogs only | Gap. Any market-sizing workflow needs its own sources |
| 6 | Win/loss and competitive intelligence: no non-vendor 2026 study | E21 (G2, vendor) on buyer AI use. Crayon 2026 dropped (no sample). Perspective AI win/loss report not opened (same vendor as E1) | Gap. Win/loss workflow rests on practitioner sources from track 1 |
| 7 | Data privacy: no non-vendor 2026 statistic on PMs or researchers pasting customer data into AI | E20 (Cyberhaven, vendor telemetry). E25 shows bank approval process | Data safety note can cite E20 as vendor data, or use no statistic |
| 8 | Survey fraud and bots: no clean 2026 rate | E18 (NORC review, older stats inside), E19 (Prolific, vendor, under 1% on 12 panels, 16% on MTurk) | Teach checks, not a rate |
| 9 | Primary sources not opened: Delight Path full report (gated), E14 paper, E19 preprint, E20 PDF, E13 arXiv PDF | Secondary pages only | Verifier should open these before Gate 1 |
| 10 | FinTech and health care cases are vendor stories (E24 Flatiron Health, E25 bank) | 2 vendor cases, plus E12 and E14 studies in health care settings | Usable as examples only |

Worked-example gaps:
- E3 primary report: closed. Page opened; 80% and 34% confirmed. Full report gated.
- E4 second source: closed (E10 Condens, E23 UKG).
- E5 second source: closed (E12 JMIR 2026, E10 Condens).
- Non-vendor 2026 source for the synthesis bottleneck: partly closed (E13, E14; E12 is a counterweight).
- Hardware and internal PM sources: hardware partly (vendor only); internal PM open.
- Scheduling and triggers on each platform: not track 4. Left to the platform matrix.

## Track 2: methods and platforms

Added 2026-11-20 by the methods and platforms researcher. Details are in `platform-matrix.yaml`.

| # | Gap | Why it matters | Next step |
| --- | --- | --- | --- |
| T2-1 | Gemini skills for Workspace business accounts: two Google sources disagree. The Workspace Updates blog (2026-09-30, updated 2026-11-09) says Gemini app skills are for all Workspace customers now. The Gemini Apps Help pages say work accounts are "coming soon". March 2027 is when business Gems stop | Decides if Workspace learners can do the Gemini core path in 2027 | Dan decides. Test on a Workspace business account at Gate 2 |
| T2-2 | Copilot: Copilot Chat-only users without pay-as-you-go billing cannot use embedded files as knowledge (Learn, 2026-11-06). The same page conflicts on whether unlicensed users can author agents | Some learners may not run the core path as written | Second Copilot tester (PRD open item). Test a fallback: brief in instructions, batch uploaded in chat |
| T2-3 | Template copy for catch-up: no documented copy feature on Claude, ChatGPT or Copilot. Only Gemini documents "save a copy" | Catch-up templates per module (CLAUDE.md rule 12) | Use a text catch-up kit (brief + files) on all platforms. Dan to approve |
| T2-4 | File output not documented for ChatGPT, Copilot agent builder or Gemini skills | The log and flag report as files across batches | Test in Gate 2 proof. Use on-screen tables until then |
| T2-5 | ChatGPT Projects help page (help.openai.com) failed again. Read from help-lb.openai.com. Project file counts conflict (Plus 25 on Projects page, 20 on File uploads FAQ) | E9 status | Verifier to confirm help-lb is official. Use 20 in step cards |
| T2-6 | ChatGPT skills are only on Business, Enterprise, Healthcare and Edu | PRD says "ChatGPT projects and skills". Plus and Pro learners can build only a Project | Dan to confirm the ChatGPT core build is a Project |
| T2-7 | Copilot scheduled workflows in agent builder: source is a third-party Message Center mirror (MC1302906). No Microsoft Learn page found | Copilot stretch path | Find a Microsoft-hosted page after rollout (mid-December 2026) |
| T2-8 | No dated vendor doc says if Copilot scheduled tasks can call an agent builder agent, or if ChatGPT scheduled tasks can use a skill | Stretch path design | Recheck in the monthly platform refresh |
| T2-9 | No trigger feature found for Claude (only schedules) | Stretch path parity | Recheck in the monthly refresh |
| T2-10 | No 2026 study compares agent-manager methods (brief, checks, hand-off rules, audit). Methods in methods.md are design methods, not evidence | Slides cannot claim one method works better | Track 4 (proof) to search. Otherwise teach as practice, not as a finding |
| T2-11 | Several vendor pages show no date (Gemini Apps Help) or only a relative date (Claude, OpenAI Help Centers) | Research rule 3 needs a dated vendor doc | Recorded approximate dates. Dan decides if a relative date is enough |
| T2-12 | Gemini Enterprise (Google Cloud) skills not checked | Some companies use Gemini Enterprise, not the Gemini app | Check in Stage 1 rerun if Dan wants it |

## Track 1: workflows

Run 1, 2026-11-20. Workflow researcher. File: `workflows.yaml` (9 rows).

### Top gaps

1. **No 2026 primary statistic for any new bottleneck (rows 02 to 09).** All figures found are vendor numbers with no method (W1, W5, W16), pre-2026 studies (W3, W7, W12, W13), or secondary reports of a primary not yet opened (W2, W4, W10). Every new bottleneck rests on claims, not statistics.
2. **Hardware and internal PM: no row has 2 sources.** Only row 03 has one source each (W17 maintenance data as design feedback, W18 platform PM intake). Rows 02 and 04 to 09 are "gap" for both contexts.
3. **Weak bottleneck evidence for rows 07 and 08.** Row 07 has one author only (Torres, W14 and W15). Row 08 has one vendor source with no data (W16).

### Other gaps

4. Many bottleneck sources are vendors (Clozd, Corporate Visions, Enterpret, ProductPlan, Lyssna, User Interviews, UserTesting, Conveo). Non-vendor sources: W3 (Pragmatic), W7 (RTI), W9 (PMA), W13 (NN/g), W19 (LogRocket). All five are older than 12 months; Dan decides if they stay.
5. Primary sources to open: ProductPlan State of Product Management 2026 (W4), MRS Global Data Quality initiative (W10), Corporate Visions 150,000-deal analysis (W2).
6. Scope questions for Dan: row 06 is Focus / Market Definition and row 08 is Planning / Ideation. Are they in scope for the Market course?
7. Overlap questions for Dan: row 02 shares inputs with row 01 (win/loss calls); row 03 sits near CAW-AI buyer voice watch (different source and agent); row 07 sits near PDW-AI validation basics.
8. Platform claims in the new rows reuse E6 to E9 from row 01. Track 2 must verify CSV size limits (Copilot), web grounding (row 06) and agent sharing (row 09).
9. Rejected candidates, not written as rows: interview guide prep (PDW-AI teaches it), competitor tracking (CAW-AI), persona drafting (BPW-AI, MKT-2026), distinctive competencies PRIME review (low repetition), customer value realization (Operations category).
10. Industry notes: no sources found for health care, FinTech, manufacturing or services differences. Notes in rows are marked "Not yet researched".

## Track 3: PM needs

Added 2026-11-20 by the PM needs researcher. Sources are in `needs.md`.

| # | Gap | What we have | Next step |
| --- | --- | --- | --- |
| G3-1 | Internal PM (priority): no 2026 source on how internal platform and tool PMs research employee users, or how long it takes | 20% of Product Focus respondents build internal products (N5). Practitioner claims all older than 12 months (N21, N22, N23) | Open the Enterpret platform PM guide. Ask Dan for internal PM contacts or his own cases. Dan decides if the old sources stay |
| G3-2 | Hardware (priority): no source on how hardware PMs run field visits, installer, distributor or service technician interviews, or the time they take | 47.6% of N5 respondents do hardware; firefighting and late-question costs (N5, N6); partner-filtered feedback (N20, 1 source) | Search trade press (Bits&Chips, PDMA, IEEE). Find a second source for N20 |
| G3-3 | No independent 2026 statistic on time spent per task (recruiting, interviews, synthesis, readouts) | Only vendor figures (N15, N16, E1, E2), not verified or weak | Accept as a gap, or use Dan's own estimates marked as assumptions |
| G3-4 | Surveys: no 2026 source on how PMs design, field and analyze surveys, or the time it takes | Only old internal PM mentions (N21, N23) | Search survey vendor 2026 reports with a stated method |
| G3-5 | Market sizing and Distinctive Competencies: no time or frequency data | Pragmatic steps only (N1) | Accept as a gap. Use the Pragmatic steps for the workflow shape |
| G3-6 | Health care, FinTech and services: no source on PM research tasks in these industries | Data risk sources only (N24, N25); HHS page not opened (N26) | Open HHS page. Search health care and FinTech PM discovery practice |
| G3-7 | Manufacturing feedback statistics have small or unknown samples | N17 (n not stated), N18, N19 (secondary) | Find the Interact Analysis primary report |
| G3-8 | Unverified primaries: Wynter CI (N13), Delight Path PDF (N7, N8) | Secondary reports | Open both in the next run (fetch budget ran out) |
| G3-9 | Most surveys skew to software and to researchers, not PMs (N9, N10, N11: PMs are a minority or not stated); N5 skews to Europe (83%) | Stated in each ledger note | Say this limit in the brief |
