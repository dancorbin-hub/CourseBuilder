# Gate 1 packet: Advanced AI for Market Research

- Course id: `market-research`. Stage 1, run 1. Written by the Synthesizer on 2026-11-20.
- For: Dan. You mark each row retain, defer or reject, and answer decisions a to f.
- Reading time: about 20 minutes. Spot checks (section 5): about 45 minutes.
- Full detail: `research-brief.md`. Rows in full: `workflows.yaml`. Evidence ids: `evidence-ledger.yaml` (E, W) and `needs.md` (N). Platform ids: `platform-matrix.yaml`.
- Evidence labels: V = verified, PV = partly verified, NV = not verified. "Vendor" = the publisher sells a product in this area.

## 1. Workflow rows: your decision per row

The "Critic" column is the research critic's view. The "Synthesizer" column is this packet's recommendation. You decide.

| Row | Workflow | Bottleneck (2-source result) | Category / focus area | Evidence (ids, strength) | PM decision | AI error to catch | Proposed lab | Open gaps | Critic | Synthesizer | Dan's decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mr-wf-01 (approved) | Turn each interview batch into an updated, checked insight log | Synthesis is slow; the work moves to checking AI output. Partly passes: "checking" has 2 independent sources; "takes days" has 1 vendor | Market / Market Problems | E4 V (3 sources, 2 vendor), E10 V vendor, E5 V. "Days": E1 PV weak, E2 V weak (one vendor). Counter: E12 V non-vendor | Which market problems go forward, for which segment | One vocal buyer counted as a pattern (data-based) | Build the course agent from a template. Batch 1, flag report, audit, tune the brief, batch 2 | Non-vendor time source. Hardware, internal PM. Decisions a, b, c | Retain. Fold 05 in as a lab step | Retain | |
| mr-wf-02 | Run win/loss on each batch of decided deals into a checked decision-driver log | CRM reasons differ from buyer reasons: passes (W1, W2). "Slow, does not scale": W2 only | Market / Win/Loss Analysis | W1 V vendor, W2 V vendor (no figure), N1 V Pragmatic guide. W3 NV | Which problems, pricing, positioning and sales gaps to act on and share | A CRM-only deal leaks into buyer findings, so "price" looks like a top driver (data-based) | Extend the agent: join a CRM export with interview notes; label the source of each deal | 2026 primary on reason gap (rerun open). PA-04. Own check may catch the planted error (fix at Gate 2) | Retain, separate module | Retain | |
| mr-wf-03 | Route each week's feedback into the market problem log | Hand tagging is slow, inconsistent and drifts. Passes (W4, W5) | Market / Market Problems | W4 V vendor, W5 V vendor. Examples: E22 V self-reported, E24 V vendor. Internal PM: N27 V vendor | Which problems gain or lose weight; which need discovery interviews | Forced fit: a new problem is tagged to the nearest old tag (model-based) | Extend the agent: tag a week of feedback (CSV), count by accounts, report what moved | Non-vendor source. Hardware (W17 NV). Prefer a data-based planted error | Retain. Take 04 as optional input | Retain, with 04 merged | |
| mr-wf-04 | Code open-text survey answers by segment | Passes on 2 sources, both older than 12 months. No source shows PMs do this task | Market / Market Problems | W7 V (2025, age flag), W8 V (2025, age flag) | Is a problem pervasive and urgent enough to go forward | Negation and sarcasm coded wrong (model-based) | Optional second input in the row 03 lab | 2026 source. PM evidence. PA-06 | Merge into 03 | Merge into 03 | |
| mr-wf-05 | Screen and shortlist research participants | Passes (W11, W12, both vendors) | Market / Market Problems | W11 V vendor, W12 V vendor (2025 figures not used). W10 PV (figure not used) | Who the PM talks to | Job title read as buying role | Lab step: the agent screens the next interview list | Weak PM decision. Hardware, internal PM | Fold into 01 or 02 | Fold into 01 | |
| mr-wf-06 | Build and refresh a sourced market size model | Passes, but both sources older than 12 months | Focus / Market Definition | W9 V (2025, age flag), W19 V (2023, age flag) | Which segment to pursue or drop | Fake triangulation (two articles quote one report) | Needs a source pack; web search is stretch | Out of Market category. MKT-2026 overlap | Defer | Defer | |
| mr-wf-07 | Keep the evidence register current | Fails: W14 and W15 are one author, both NV | Market / Market Problems | W14 NV, W15 NV | Which problems count as validated | Wrong-segment evidence (blank segment field) | Fold status proposals into row 09 | Second source | Fold into 09 | Fold into 09 | |
| mr-wf-08 | Score concept tests per hypothesis | Fails: 1 vendor source, NV, no data | Planning / Ideation | W16 NV | Which concept goes forward, changes or stops | Stated preference read as a pass | Session notes from the case | Out of Market category. Design course overlap | Defer | Defer | |
| mr-wf-09 | Answer stakeholder questions from past research | Passes (W13, W20). W13 is from 2024: if you drop it, the row has 1 source | Market / Market Problems | W13 V (2024, age flag, non-vendor), W20 V vendor | Answer now or start new research; what to tell the stakeholder | Old research for another segment presented as current (data-based) | Extend the agent: answer from the research store; hand-off rules limit what it may say | 2026 statistic. Hardware example E27 NV. Sharing the agent NV (stretch) | Retain, with 07 folded in | Retain, with 07 folded in | |
| mr-wf-10 | Keep the alternatives map current from own evaluator and deal evidence | Generic "keeping CI current" passes (N13, W21). The specific burden (map from own deal evidence) has no source | Market / Competitive Landscape | N13 V (Wynter, survey April 2026, published May 2026, 101 PMMs), W21 V weak, vendor-adjacent | Which alternatives to beat, by segment; what goes to positioning, pricing, roadmap | CRM competitor field trusted where the buyer chose "do nothing" (data-based) | Extend the agent: read the logs from modules 1 and 2; map competitors, substitutes, workarounds, "do nothing" | Specific bottleneck. Hardware, internal PM. Own check may catch the error (fix at Gate 2) | Retain (new row) | Retain with condition (decision f) | |

Result if you accept the Synthesizer column: 5 retained rows (01, 02, 03, 09, 10), 3 folded or merged (04, 05, 07), 2 deferred (06, 08). Without row 10: 4 rows, which still meets check 7.

## 2. Decisions for Dan

Each decision has options and one recommendation. Items marked "approved row" change the approved worked example (mr-wf-01). I do not change them without your yes.

### a) PA-01: "2 or more interviews per insight" (approved row)

- The approved row says: the fix for the planted error is a rule in the brief, "2 or more interviews per insight". The success check says "no insight rests on one interview".
- PDW-AI (slides 27, 28) says AI buries the low-frequency, high-intensity signal, and that signal is often the real insight. A strict rule repeats that failure, and PDW-AI graduates will notice.

| Option | What changes |
| --- | --- |
| 1. Align with PDW-AI | Remove the rule. Teach saturation and frequency against intensity only. The planted error loses its clear fix |
| 2. Flag, not filter (recommended) | Keep a rule, reworded: an insight from 1 interview gets the label "single source" and goes to the flag report. It does not count as a pattern and is not dropped. The PM decides if it is a high-intensity signal. Success check becomes "no single-source insight is counted as a pattern" |
| 3. Keep as written | Explain in class that PDW-AI is about finding signals and this lab is about counting patterns |

Why option 2: the planted error and the audit lesson stay. It agrees with PDW-AI. It teaches a better agent-manager habit: a flag, not a filter.

### b) E8 Gemini date, YAML fix and sources list (approved row)

1. **E8 is wrong.** The approved row says "Workspace business accounts get skills in March 2027". The source says March 2027 is when business Gems are removed. The Workspace Updates blog (2026-09-30, updated 2026-11-09) says Gemini app skills are available to all Workspace customers now (gm-03, V). The Gemini Help page still says work accounts get skills "soon".
   - Recommended: replace the Gemini line with "Gemini skill with the brief and code book. Workspace: skills available per the Workspace blog (gm-03); test on a Workspace account at Gate 2." Apply the same fix to row 02 (same wrong date), to the E8 cite in rows 03 to 09, to the ledger entry E8 and to note gm-03. Row 10 already cites gm-01.
   - Other options: keep the line and add a note; or remove the date with no new claim.
2. **`worked-example-row.yaml` does not parse as YAML.** The run log reports 2 unquoted values. My parse test (no file change) finds one line that breaks the parse: line 76, `registry_check`, which holds ": " inside the text. With quotes on that line, the file parses. The fix adds quotes only. No text changes.
   - Recommended: yes, quote-only fix.
3. **Sources list.** The Verifier says row 01 lists E1, E3, E5, but E3 is an adoption figure, not a burden. E4 and E10 support "the work moves to checking".
   - Recommended: change the list to E4, E10, E5, and keep E1 as a vendor note. Option: leave as is.

### c) PA-02 and PA-03: Pragmatic messaging

**PA-02. AI-moderated interviews and synthetic respondents.** PDW-AI says "AI never replaces talking to a real person". A Pragmatic article (Will Scott, modified 2026-11-02) says synthetic profiles can support early concept tests. No row uses AI-moderated interviews today. The only source that points that way is N15 (vendor, weak).

| Option | What changes |
| --- | --- |
| 1. Follow PDW-AI (recommended) | Module 1 states that the agent works only on conversations a person held. Do not cite N15 as a model. Ask Pragmatic which position is current before Gate 2 |
| 2. AI changed the work | Say AI-moderated interviews and synthetic profiles exist. Teach them as inputs to check, never as a replacement for a market visit |
| 3. Show both | Show both Pragmatic positions and let learners discuss |

Note: E16 and E17 (both V, non-vendor) show that synthetic respondents flatten the range of opinion. They support a caution point under any option.

**PA-03. Data safety and consent on every row.** Rows 01, 06, 07 and 08 have no general data safety note. No row asks for consent before recording. House rule 7 needs a note in every lab.

| Option | What changes |
| --- | --- |
| 1. Standard note | One note on every row: approved tool only; no client data, PHI or PII in an unapproved tool; consent before you record; agree confidentiality for win/loss |
| 2. Standard note plus log point (recommended) | Option 1, plus one teaching point: an agent that keeps a log stores sensitive data longer than a one-off prompt |
| 3. One slide only | Leave rows as they are. One data safety slide in module 1 |

Row 01 is approved, so adding the note there needs your yes. Recommended: no statistic in the note. E20 (Cyberhaven, V) is vendor telemetry with data through 2025.

### d) Rows outside the Market category

| Row | Category | Recommendation | Options |
| --- | --- | --- | --- |
| mr-wf-06 Market size model | Focus / Market Definition | Defer to a later Focus or Strategy course | Retain as a stretch lab; reject |
| mr-wf-08 Concept test results | Planning / Ideation | Defer. It also fails the 2-source rule | Retain if no other course claims Ideation; reject |

Related (PA-05): Pragmatic's Market course emphasizes Market Definition, Measurement, Buyer Journey, Buyer Personas and Marketing Plan (guide pages 21, 22). This course covers Market Problems, Win/Loss and Competitive Landscape. Recommended: keep the scope, and map the course to its focus areas in the Gate 2 spec. Consider a subtitle such as "market and buyer research".

### e) Platform risks

| # | Risk | Evidence | Recommendation | Other options |
| --- | --- | --- | --- | --- |
| 1 | The skills page says ChatGPT skills are only on Business, Enterprise, Healthcare and Edu (not verified). If true, Plus and Pro learners can build a Project only | cg-04 (NV). cg-01 (V): Projects on all plans | ChatGPT core build is a Project. A skill is an option for business plans. Verify cg-04 before Gate 2 | Require a business plan |
| 2 | ChatGPT Free: 5 project files, 3 uploads per day | cg-01 (V), cg-03 (V) | State a minimum of Go or Plus for ChatGPT learners. A full day of batches is likely to pass 3 uploads | Design each lab to fit 3 uploads; pair Free learners |
| 3 | Plus file count conflicts: 25 (cg-01) against 20 (cg-03) | cg-01, cg-03 (V) | Use 20 in step cards | None |
| 4 | Copilot embedded files need a Microsoft 365 Copilot license or pay-as-you-go billing. The page conflicts with itself on unlicensed authoring | mb-02, mb-03 (V) | Make a license or billing a stated prerequisite. Test the fallback at Gate 2: code book in the instructions, batch uploaded in chat | Fallback as the default Copilot path |
| 5 | Catch-up kit: no copy feature is verified on any platform | cl-pj-02, cl-cl-05, cg-05, mb-05, gm-04 (all NV) | A text kit per module on all four platforms: brief as text plus knowledge files. It also carries the log where file output is not proven | Gemini "save a copy" as an extra, after it is verified |
| 6 | Moving the log between modules: file output fully proven on Claude only (cl-fo-06). Copilot proven for the session only (mb-11). Gemini app only (gm-09). ChatGPT partly (cg-08) | As listed | Same text kit. Gate 2 proof tests file output on each platform | On-screen tables only |
| 7 | Gemini Workspace status: two Google pages disagree | gm-03 (V), Help page | Test on a Workspace business account at Gate 2 | None |

### f) Row 10: retain on a generic bottleneck?

- N13 and W21 show that keeping competitive intelligence current is a recurring burden. Neither describes a map built from the team's own deal evidence, or workarounds and "do nothing".
- Check 7 says no retained row may depend on an open question that could break its bottleneck.

| Option | What changes |
| --- | --- |
| 1. Retain with a condition (recommended) | Retain. Record the specific bottleneck as a gap (PRD decision 37). Your own win/loss cases fill it. Verify at Gate 2 that the lab is clearly not a CAW-AI agent |
| 2. Fold into row 02 | The alternatives map becomes a later step of the win/loss lab. 4 modules |
| 3. Defer | Wait for a better source in the monthly refresh |

### Other alignment items (quick yes or no)

| Id | Item | Recommendation |
| --- | --- | --- |
| PA-04 | Row 02 "truth rate" | Rename to "match rate". Default minimum 10 deals. Interviews by someone outside sales (N1) |
| PA-06 | Row 04 validation tests | Name all three tests: urgent, pervasive, willing to pay |
| PA-07 | Old Framework names on MKT deck slide 7 | Use only the 2027 guide terms. Tell Pragmatic the slide is out of date |
| PA-08 | Field name `pdlc_stage` (approved schema) | Keep the field name in the repo. Write "category" in all learner text |
| PA-09 | PDW-AI slide 3 recommends Gems | One line on the Gemini step card: Gems are now skills |
| Age flags | W13 (2024), W7, W8, W9 (2025), W19 (2023), E5 Torres (2025, updated 2026-09-27) | Keep W13 and E5. The others belong to merged or deferred rows |

## 3. Suggested module order (autonomy ladder, suggestion only)

| Module | Row | Rung | Warning on planted error |
| --- | --- | --- | --- |
| 1 | 01 (+ 05 step) | Run by hand on a batch | Told |
| 2 | 02 | Run by hand, two sources joined | Hint |
| 3 | 03 (+ 04 input) | High volume, PM reads flags and a sample. Schedule as stretch | Hint |
| 4 | 10 | Reads outputs of modules 1 and 2 | Hint |
| 5 | 09 (+ 07) | Answers other people, under hand-off rules | None |

Two limits: all schedule features are NV, so the schedule rung is a stretch step. "Agents that hand work to other agents" needs a Gate 2 definition, because the course has one agent.

## 4. Evidence strength in plain words

- The speed claim rests on vendor data: E1 (PV, weak) and E2 (V, weak) are one vendor; E10 (V) is a vendor survey; E22 (V) is self-reported. Do not put E1 or E2 on a slide.
- One peer-reviewed 2026 study found no time saved in a chat workflow (E12, V). Its corpus is newspaper articles, not interviews.
- The strongest non-vendor 2026 items are on AI risks: E12 (over-coding, low agreement with humans), E16 and E17 (synthetic respondents flatten opinion). E17 also found a positive skew on well-known brands. E16 found no consistent direction.
- Bottlenecks for rows 02 to 10 rest on claims from vendors, vendor-adjacent sources or sources older than 12 months. PRD decision 37 accepts this for now.
- E13 (status "wrong") and E8 (status "wrong") are not used for claims.

## 5. The 7 checks of the Gate 1 acceptance test

| # | Check | Synthesizer view | Files to open |
| --- | --- | --- | --- |
| 1 | Research supports a full course | 4 to 5 distinct rows, each with input, bottleneck, output, PM decision. Hardware and internal PM gaps recorded per row | `workflows.yaml`, `critic-report.md` section 1, `gaps.md` |
| 2 | Bottlenecks are real (pick 2 rows) | Suggest rows 02 and 03 (each passes with 2 independent vendor sources) | `workflows.yaml` (W1, W2, W4, W5), `verifier-report.md` "Bottleneck check" |
| 3 | Each row teaches PM judgment (same 2 rows) | Each row names agent work, PM decision and one AI error | `workflows.yaml` fields `split` and `ai_error_to_catch` |
| 4 | Brief kept the evidence | Suggest statistic E3 (80% and 34%, 107 leaders, Q2 2026), claim E4 (3 sources), tool claim E6 (Copilot 8,000 characters, Learn page 2026-11-16) | `research-brief.md` section 4, `evidence-ledger.yaml`, `sources.yaml` |
| 5 | Lab possible on all four platforms | Plausible on paper. Copilot license, ChatGPT plan and Gemini Workspace are open and recorded (decision e) | `platform-matrix.yaml`, `methods.md`, `research-brief.md` section 5 |
| 6 | Alignment used the right Pragmatic material | Sources match `status.yaml`. Traced example: row 01 `pragmatic_fit` against guide pages 4 and 6. BPW-AI, PRC, PRW-AI not opened | `alignment-log.yaml` (`sources_used`, `traced_example`), `status.yaml` |
| 7 | Decision possible from the packet | At least 4 rows earn retain. Row 10 depends on decision f | This packet, section 1 |

## 6. Gaps left after the rerun

| # | Gap | Status |
| --- | --- | --- |
| 1 | Non-vendor 2026 source on synthesis time | Open. E12 is a counterweight |
| 2 | Recent non-vendor bottleneck source for rows 02 to 10 | Open |
| 3 | Row 10 specific bottleneck (alternatives map from own evidence) | Partly closed (generic CI only) |
| 4 | 2026 primary on seller against buyer loss reasons | Open (rerun ask 4) |
| 5 | Internal PM (priority) | Partly closed: N27 (V, vendor). N28 (PV) goes past its source |
| 6 | Hardware (priority) | One verified case (E28). E26, E27, E29 not verified |
| 7 | File output for ChatGPT Projects and Gemini skills | Open. Gate 2 proof |
| 8 | Schedule features on all platforms | Not verified |
| 9 | Evidence that one agent-manager method works better | Open. Teach as practice |
| 10 | Health care, FinTech, services PM research tasks | Open |

## 7. After you decide

1. You mark each row and answer a to f in the doc.
2. Claude Code applies your answers to the repo files, not to the doc.
3. Approved-row changes (a, b, c) happen only after your yes.
4. You say "Gate 1 approved". Claude Code updates `status.yaml`.
