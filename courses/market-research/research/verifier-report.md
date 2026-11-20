# Verifier report: market-research, Stage 1, Mode 1 (claims)

- Course: Advanced AI for Market Research (`market-research`)
- Verifier run: 2026-11-20
- Files checked: `workflows.yaml`, `evidence-ledger.yaml`, `sources.yaml`, `needs.md`, `platform-matrix.yaml` (core-lab features and features named by a proposed lab)
- Files changed: `evidence-ledger.yaml` (status + `verifier_note`), `platform-matrix.yaml` (status + `verifier_note`), `workflows.yaml` (evidence `status` lines only). All three parse with `python3 yaml.safe_load`.
- Not changed: `worked-example-row.yaml`, `needs.md`, `sources.yaml`.

## Limits of this run

1. The shared web fetch budget (100 per hour, all agents) ran out early in this run. I then fetched one page at a time as the budget refilled.
2. Direct `curl` reached only `support.claude.com`. I used it for the Claude features.
3. I marked "not verified" every item I did not open myself. I did not copy a researcher's status.
4. `needs.md` has no status fields for me to edit. Its results are in this report only.

## Counts

| Result | Ledger E | Workflow W | needs.md N | Platform | Total |
| --- | --- | --- | --- | --- | --- |
| Verified | 18 | 14 | 10 | 12 | 54 |
| Partly verified | 6 | 1 | 2 | 2 | 11 |
| Not verified | 4 | 5 | 13 | 0 | 22 |
| Wrong | 2 | 0 | 0 | 0 | 2 |

Twenty other platform features (stretch, sharing, schedules) stay "not verified" (PRD decision 25).

## Failures and items Dan must see

### Wrong

| Id | Claim | What the source says | Action |
| --- | --- | --- | --- |
| E8 | "Workspace business accounts get skills in March 2027" | The Gemini Help page gives March 2027 as the date when business **Gems are removed**. It says work accounts get skills "soon". The Workspace Updates blog (2026-09-30, updated 2026-11-09) says all Workspace customers get Gemini app skills now, with rollout done by mid-November 2026. | Fix the wording in the ledger. The same wrong text is in `workflows.yaml` rows mr-wf-01 and mr-wf-02 (Gemini platform line), in `worked-example-row.yaml` and in the gm-03 note. I did not edit those. Dan to approve a fix. |
| E13 | LLM workflow "recovered 88.6% of the themes in six published reports" | 88.6% is 31 of 35 themes across **all** sources that appeared in Reddit or interview outputs. Of the 22 report themes, Reddit found 16 and interviews found 16 (73% each). The speed claim is a figure caption ("an order of magnitude faster") in 10 to 15 minute timed phases, with no exact times. | Do not use 88.6% as stated. Use "16 of 22 report themes per source". |

### Partly verified (statistics)

| Id | Gap |
| --- | --- |
| E1 | The 4 hours is labeled "2026 median" (Jan to Apr 2026), not "Q1 2026". Vendor. 2024 baseline method not stated. |
| E14 | The paper did not open (doi.org and Sage both failed). News item gives no figures. |
| E18 | NORC PDF not opened. |
| E19 | Primary preprint (OSF) did not render. Figures confirmed only through Retraction Watch. Prolific-funded. |
| E21 | 82% and 61% confirmed. "Mostly for evaluation" is not supported. Top uses: TCO 51%, shortlists 51%, research 49%, evaluating vendors 46%. |
| E30 / N8 | 49%, 45%, 42% appear only in the Lyssna article. The Delight Path preview page does not show them. Full report is behind a download form. |
| W10 | Primary for the 95% fraud figure (MRS Global Data Quality) not found. Do not use the figure. |
| N24 | IT Brief gives 42% and 32% but names no report and gives no link. Primary not found. |

### Corrections to researcher notes

1. E10: the "21% vs 5%" conflict is not a conflict. 21% agree they can trust AI output with little review. 5% name "trust with minimal review" as their validation practice. Different questions. 65% disagree is confirmed.
2. E5: "hallucinates quotes that weren't there" is the Condens authors' summary, not a respondent quote.
3. E20: the report page says 222 companies and data "through 2025". It says "AI interactions", where the press release says "data movements". Published 2026, so it passes the 2026 rule.
4. N13: the primary (Wynter, May 2026, survey 2026-04-27 to 28, 101 PMMs) is now opened. All figures confirmed. Top source is sales calls at 44%.
5. N26: HHS page opened. Two methods confirmed. Page modified 2026-03-20.
6. W12: the User Interviews page footer says "Copyright 2026 UserTesting". If one company owns both, W12 and W20 are one publisher. They support different rows, so no row fails because of it.

## Bottleneck check: 2 independent sources per row

| Row | Sources | Result | Note |
| --- | --- | --- | --- |
| mr-wf-01 | E1, E3, E5 (as listed) | **Partly passes** | "Work moves to checking": E4 (Lyssna) and E10 (Condens) are independent and verified. "Synthesis takes days": only Perspective AI (E1, E2), 1 vendor. E3 is an adoption figure and does not describe a burden. E12 (non-vendor) found no time saved. The row's `sources` list needs a fix. |
| mr-wf-02 | W1, W2, W3 | **Partly passes** | "CRM reasons differ from buyer reasons": W1 and W2, verified, independent vendors. "Slow, does not scale": W2 only. W3 not reopened. |
| mr-wf-03 | W4, W5 | Passes | Two independent vendors. |
| mr-wf-04 | W7, W8 | Passes | Both older than 12 months. Dan decides. |
| mr-wf-05 | W10, W11, W12 | Passes | W11 and W12. W10 partly verified. W12 figures are 2025. |
| mr-wf-06 | W9, W19 | Passes | Both older than 12 months. Dan decides. |
| mr-wf-07 | W14, W15 | **Fails** | Same author (Torres), so 1 source. Not reopened. |
| mr-wf-08 | W16 | **Fails** | 1 vendor source, no primary data. Not reopened. |
| mr-wf-09 | W13, W20 | Passes | W13 is 2024. Dan decides. |

## Platform verdicts (core-lab features)

| Id | Feature | Result | Note |
| --- | --- | --- | --- |
| cl-pj-01 | Claude Projects | Verified | All users. Free: 5 projects. Help Center shows relative dates only. |
| cl-cl-03 (E7) | Claude custom skills | Verified | All plans. Code execution required. |
| cl-fo-06 | Claude file output | Verified | All plans, 30 MB. Org owners can turn it off. |
| cg-01 (E9) | ChatGPT Projects | Verified | Files: Free 5, Go and Plus 25, Pro and business 40. |
| cg-03 | ChatGPT file limits | Verified | Conflict is real: Plus 20 here, 25 in cg-01. New: Free users get 3 uploads per day. That can block a Free learner in a lab. |
| mb-01 (E6) | Copilot instructions | Verified | 8,000 characters. Updated 2026-11-16. |
| mb-02 | Copilot embedded files | Verified | 20 files, 512 MB docs, 30 MB spreadsheets. Not in GCC. |
| mb-03 | Copilot license states | Verified | Embedded files need a license or usage billing. The page conflicts with itself on unlicensed authoring. |
| mb-04 | Copilot code interpreter | Verified | No output formats or downloads stated. |
| gm-01 | Gemini skills | Partly verified | Page undated, so no dated vendor doc. "100 active skills" not found. |
| gm-02 | Gems to skills dates | Verified | Business Gems stop no sooner than 2027-03-01. |
| gm-03 | Workspace skills | Verified | Gemini app skills for all Workspace customers now. This resolves the conflict against "March 2027". The blog says no age limit in the Gemini app; the Help page says 18+. |
| gm-06 | Tools not in skills | Partly verified | Content confirmed. Page undated. |
| mb-08 | Copy to Copilot Studio | Verified | Not a core feature. Checked because it was on the same page. |

### help-lb.openai.com

- Verdict: an OpenAI-controlled host. It is a subdomain of `openai.com`, so only OpenAI (or its help-desk vendor) can serve it. The page is branded OpenAI. It uses the same article ids and content as `help.openai.com`.
- Limit: I could not confirm it through DNS or a link from `help.openai.com`. The name suggests a load-balancer mirror, not the public address.
- Rule: accept it as the dated vendor doc. In learner materials, cite the `help.openai.com` URL. Recheck at the Gate 2 proof.

## Not opened (for the next run)

E25, E26, E27, E29 (Dovetail and Discuss.io stories), W3, W14, W15, W16, W17, NORC PDF (E18), E14 paper, E19 preprint, Cyberhaven full PDF (E20), and needs.md N2, N3, N4, N6, N12, N16, N18, N19, N20, N21, N22, N23, N25.

## Full results table

| Id | Claim (short) | Result | Note |
| --- | --- | --- | --- |
| E1 | Synthesis 14 days to 4 hours | Partly verified | Label is "2026 median". Vendor |
| E2 | 12.1 to 1.1 days, QA 0.6 days | Verified, weak | Vendor customer data |
| E3 | 80% / 34% leaders use AI | Verified | Primary preview page |
| E4 | Work moves to checking | Verified | 3 sources confirmed |
| E5 | AI rewords quotes, loses context | Verified | JMIR and Condens |
| E6 | Copilot 8,000 characters | Verified | |
| E7 | Claude skills all plans | Verified | |
| E8 | Gems to skills, business March 2027 | **Wrong** | See above |
| E9 | ChatGPT Projects | Verified | help-lb host |
| E10 | Condens 71% / 71% / 65% / 12% | Verified, vendor | |
| E11 | Maze 69% / 82% | Verified, vendor | |
| E12 | JMIR over-coding, alpha | Verified | |
| E13 | Policy LLM study, 88.6% | **Wrong** | See above |
| E14 | Nurse LLM study time | Partly verified | Paper not opened |
| E15 | ACL firearm study | Verified (abstract) | |
| E16 | Pew synthetic polls | Verified | |
| E17 | NIM digital twins | Verified | |
| E18 | Panel bot risk | Partly verified | NORC not opened |
| E19 | Prolific under 1% / 16% | Partly verified, weak | Primary not rendered |
| E20 | Cyberhaven 39.7% | Verified, vendor | Data through 2025 |
| E21 | G2 82% / 61% | Partly verified, vendor | "Mostly evaluation" unsupported |
| E22 | Azure GEM 95% | Verified, single source | |
| E23 | UKG clusters | Verified, single source | |
| E24 | Flatiron 4x4 to 1x1 | Verified, single source | |
| E25 to E27 | Dovetail stories | Not verified | Not opened |
| E28 | AMS siding 3,900 to 103 | Verified, single source | |
| E29 | HP Discuss.io | Not verified | Not opened |
| E30 | 49% / 45% / 42% | Partly verified | Secondary only |
| W1, W2, W4 to W9, W11 to W13, W18 to W20 | Bottleneck claims | Verified | See bottleneck table |
| W10 | 95% fraud | Partly verified | Primary not found |
| W3, W14 to W17 | Bottleneck claims | Not verified | Not opened |
| N1 | Pragmatic Framework 2027 | Verified | Local PDF; win/loss 2 to 4 weeks, 10 deals, verify AI output |
| N5 | Product Focus 2026 | Verified | All figures confirmed. Fieldwork Oct 2025 to Jan 2026 |
| N7 | Delight Path | Verified | Primary preview |
| N8 | Credibility figures | Partly verified | Same as E30 |
| N9 | Maze user research | Verified | |
| N10 | Maze market research | Verified | |
| N11 | Condens | Verified | |
| N13 | Wynter CI | Verified | Primary opened |
| N15 | Perspective win/loss | Verified, weak | Data May 2025 to May 2026. Year labels inconsistent |
| N17 | Manufacturers Alliance survey | Verified, weak | Informal, no sample size |
| N24 | Finance workers 42% | Partly verified | No primary |
| N26 | HHS de-identification | Verified | |
| N2 to N4, N6, N12, N16, N18 to N23, N25 | Various | Not verified | Not opened |

## Rerun items

Mode 1 check of the items added in the rerun (gaps.md, "Rerun (2026-11-20)"). Checked 2026-11-20. I opened each source myself. 14 web fetches. One fetch failed (help.openai.com, client error).

| Id | Claim | Result | Note |
| --- | --- | --- | --- |
| W21 | CI done by hand in many tabs; documents age quickly; positioning shifts quarterly | Verified, weak | Wording confirmed. Byline "Feb 10", no year (2026 is sound). Author promotes Seeto. No figure has a source link. Claim only |
| N13 | Wynter CI: 52%, 21%, sales calls top, 21% LLMs, 14% CI tools | Verified | Primary opened. May 2026, survey 2026-04-27 to 28, 101 PMMs. Sales calls 44%. No time data |
| N27 | Platform PM intake channels, two streams, loudest served first | Verified, vendor | Enterpret, 2026-11-04. Salesforce quote is not about intake. No time figures |
| N28 | Internal tool feedback: ask what they do today, 3-person pilot, usage after a week | Partly verified | Centercode, 2026-07-15. Two parts go past the source (see failures) |
| mb-11 | Copilot code interpreter downloadable files, session only | Verified | Learn page 2026-09-28. CSV is input only. License line is verbatim |
| gm-09 | Gemini app file output, 11 formats, one file per prompt | Verified (app only) | Blog 2026-04-27. No mention of skills or Gems |
| cg-08 | ChatGPT downloadable outputs | Partly verified | Academy 2026-09-04: "spreadsheets or PDFs" only. No plans, no Projects. Help article 20001278 failed again |
| Dropped: Corporate Visions tourial | 50 to 70% different loss reasons | Drop confirmed | No method. Correction below |
| Dropped: Clozd | Buyer and CRM data match 15% | Drop confirmed | Vendor, no date, sample or method |

### Failures and items Dan must see

1. N28 wording goes past the source. The post does not call adoption "the hard part". It says the fix is "smaller than you think". It says ad hoc loops "strain", not "break down". Fix the claim before the brief uses it.
2. cg-08 stays unproven for the core lab. The only dated doc names spreadsheets and PDFs. It names no plans and no Projects. The ChatGPT step card cannot rely on .csv or .docx output yet.
3. gm-09 proves file output in the Gemini app only. File output from a skill run is not proven. Test it at the Gate 2 proof.
4. Corporate Visions correction: the page ties its 150,000-deal analysis to the 53% "winnable" claim, not to the 50 to 70% figure. The ledger note says "same 150,000-deal analysis". The drop stands.

### Bottleneck check: mr-wf-10

| Source | Independent | Describes the burden | Result |
| --- | --- | --- | --- |
| N13 (Wynter primary) | Yes | CI is a side task for 52%; 24% say CI "goes stale fast"; 28% say the market moves faster than the CI cycle | Supports a generic CI upkeep burden |
| W21 (DEV Community) | Yes, from Wynter | Manual work in many tabs; documents age quickly | Weak, vendor-adjacent |

Result: 2 independent sources for a generic "keeping CI current" burden. Neither source describes an alternatives map built from own deal evidence, or workarounds and "do nothing". That part stays a gap.

### Format fix

needs.md N17 `note` did not parse as YAML. I put the value in single quotes. The text is unchanged. The needs.md YAML block now parses.

## Trace check (Mode 2)

- Run: 2026-11-20, after the Synthesizer. No web use. Trace against `evidence-ledger.yaml`, `workflows.yaml`, `needs.md`, `platform-matrix.yaml`, `alignment-log.yaml`, `methods.md`, `gaps.md` and this report.
- Files checked: `research-brief.md`, `gate-1-packet.md`.
- Claims checked: about 110 (brief about 60, packet about 50). Each cited id was found. No claim cites a "wrong" or "not verified" entry as support. "Wrong" and "not verified" ids appear only as exclusions, gaps or labelled NV risks.
- Dashes: none in the brief or the packet (checked for U+2012 to U+2015).
- YAML parse claim (packet b2): confirmed on a scratch copy. Quotes on line 76 only make `worked-example-row.yaml` parse. The file was not changed.
- Fixes: 17 wording fixes (9 brief, 8 packet). No recommendation or decision was changed.

### Fixes made

| Location | Claim | Problem | Fix |
| --- | --- | --- | --- |
| Brief 1.2 | "no bottleneck source is both recent and non-vendor" for rows 02 to 09 | True only for verified sources. W14 and W15 (Torres, 2026, practitioner) are not verified | Added "verified" |
| Brief 1.5 | "Three items touch the approved worked example row" | Packet b3 (sources list) and PA-03 (data safety note, "Yes (row 01)" in brief section 6) also touch row 01 | Changed to five items and named them |
| Brief 2, row 09 | W13, W20 as two sources | W13 age flag (2024) not stated in this row | Added the age flag |
| Brief 4, quotes row | E5 "3 sources" | Limits missing: JMIR is one reworded quote; Condens line is the authors' summary; Torres is 2025, not reopened | Added the limits |
| Brief 4, E12 row | "Strongest non-vendor item" | One study, newspaper corpus, not interviews | Added the limit |
| Brief 4, E3 row | Leaders use AI | Ledger marks vendor "partly" (Lyssna co-produced) | Added the limit |
| Brief 4, internal PM | "No second 2026 source" | N28 is a second 2026 source, partly verified | Changed to "no second verified 2026 source (N28 is partly verified)" |
| Brief 4, excluded | Partly verified list | E21 and N24 are partly verified and were not listed | Added E21 and N24 |
| Brief 5, catch-up | Text kit "works the same way on all four platforms (M10)" | M10 is a method, not a tested result | Softened to "should work", "not tested yet" |
| Packet 1, row 10 | "N13 V (Wynter, April 2026)" | April is the survey date. Primary published May 2026 | Added both dates |
| Packet 2b1 | "Apply the same fix to rows 02 to 10" | Only row 02 has the wrong date. Rows 03 to 09 cite E8. Row 10 cites gm-01 | Named the scope per row |
| Packet 2d | Market course "covers Market Definition, Buyer Personas and Buyer Journey" | Guide pages 21, 22 also name Measurement and Marketing Plan | Gave the full list and pages |
| Packet 2e1 | ChatGPT skills only on business plans, stated as fact | cg-04 is not verified | Said "the skills page says ... (not verified). If true ..." |
| Packet 2e2 | "A full day of batches will pass 3 uploads" | Inference, not a source | Changed "will" to "is likely to" |
| Packet 2e6 | "file output proven on Claude only" | mb-11 (Copilot, verified) proves output for the session | "Fully proven on Claude only. Copilot proven for the session only" |
| Packet 4 | E12 "no time saved" | Corpus limit missing | Added "newspaper articles, not interviews" |
| Packet 4 | E16 and E17 "flatten opinion and skew positive" | Positive skew is E17 only. E16 says bias direction is inconsistent | Split the claim by source |

### Flags for Dan (not changed)

| Location | Claim or recommendation | Problem | Flag |
| --- | --- | --- | --- |
| Brief 2, packet 1f, row 10 | Retain with condition | The specific bottleneck (map from own deal evidence) has no source. Packet check 7 says no retained row may depend on an open question that could break its bottleneck. The recommendation conflicts with that check | Dan decides (decision f). Option 2 or 3 avoids the conflict |
| Brief 5, packet 2e | Gemini skill as core build (instructions plus 100 MB of files) | gm-01 is partly verified (undated). E8 is "wrong". No dated vendor doc supports the 100 MB and file features. Research rule 3 is not met | Find a dated Google doc before Gate 2, or record the risk |
| Brief 5 | Claude and ChatGPT core features | cl-pj-01, cl-cl-03, cg-01, cg-03 show relative dates only. Verifier accepted them, but no fixed date is on record | Record the access date (2026-11-20) as the date at Gate 2 proof |
| Packet 1, row 01 (approved) | Bottleneck "synthesis takes days" | Only one vendor (E1, E2). Half of the approved row's bottleneck fails the 2-source rule | Dan decides if the row keeps "takes days" or rests on "work moves to checking" only |
| Packet 1, row 09 | Retain | If Dan drops W13 (2024, age flag), the row has 1 bottleneck source and fails the 2-source rule | Already in open question 7. Dan decides |
| workflows.yaml rows 03 to 09 | Gemini platform lines cite E8 | E8 status is "wrong". The lines do not repeat the wrong date, but cite a wrong entry | Re-cite to gm-01 and gm-03 with the decision b fix |
