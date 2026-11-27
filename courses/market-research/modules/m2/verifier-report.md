# Verifier report: module 2 (module mode)

Course: `market-research`. Module 2, win/loss and the match rate. Checked 2026-11-27 by the research verifier (Stage 3, step 2b).

Files checked: `modules/m2/module.md`, `modules/m2/kit/lab-2/`, `modules/m2/kit/kit-m3/`, `modules/m2/card-test.md`.

Context applied: Dan's 2026-11-27 changes (commit e78ee77: expected-results phrase, spec module 2 card step 6 and stretch note, matrix rows cl-sc-07, cg-06, mb-06, gm-07) and the case year shift to 2027 (`case/year-shift-map.md`).

## How I checked

1. I checked only claims and features that are new since Gate 1, or that the task named (D11, D13, G2-PF-02).
2. I opened each vendor doc that a step card uses, on 2026-11-27. Claude pages by curl. Other pages by WebFetch (the proxy blocks curl to them).
3. A check date older than 30 days fails. The oldest check date in use is 2026-11-20 (7 days). No date fails.
4. I did not edit `platform-matrix.yaml` or `evidence-ledger.yaml`. Both are fingerprinted. Proposed updates are in the last section.

## Results: claims

| Id | Claim (where) | Result | Note |
| --- | --- | --- | --- |
| C1 | "Two win/loss firms, Clozd and Corporate Visions, both wrote in 2026 that the CRM reason often differs" (2.2 talk track) | partly verified | Both pages say it. Clozd is dated 2026-04-20. Corporate Visions was first published 2024-11-12 and updated 2026-07-30. "Wrote in 2026" is true only for the update. See F3 |
| C2 | "Both also say a manual program is slow" (2.2 talk track) | wrong | Corporate Visions says it ("manual, time-consuming processes that can't scale"). Clozd does not. See F1 |
| C3 | "Manual win/loss is slow and does not scale" (2.2 on-slide line 2) | partly verified | One source only (W2). The rule needs 2 independent sources. A candidate second source exists, with an age flag. See F2 |
| C4 | "CRM loss reasons often differ from buyer reasons" (2.2 on-slide line 1) | verified | W1 and W2, 2 independent vendors, both reopened today. No figure used |
| C5 | "Many teams do not run win/loss at all" (D11, kept off slides) | partly verified | W1 says it, but it rests on an old Pragmatic figure. W3 is the same Pragmatic data. Not 2 independent sources. Keep it off the slides. See F4 |
| C6 | Pragmatic frame: win/loss is about the buyer's experience, not a judgment of sales (2.8 talk track, D13) | verified, age flag | Market visit article, modified 2025-08-27 (15 months). Quotes: "take judgment out of win-loss discussions", "not about the sales team", "that entire experience from the buyer's side". See F5 |
| C7 | Program rules: someone outside sales, 2 to 4 weeks after the decision, "at least 10 deals" (2.3, D12) | verified | Pragmatic Framework 2027 guide, page 7, opened today. Wording on 2.3 and in D12 matches the guide |
| C8 | No published source on win/loss in hardware or internal PM (2.4) | gap confirmed | Recorded gap in `workflows.yaml`. Not a failure |
| C9 | Case years after the shift to 2027 | pass | No 2025 or 2026 year in `kit/`. In `module.md`, 2026 appears only as real build, source and check dates. Slide 2.5 says "Q2 2027" |

## Results: step card screen names and features

| Card | Screen name or feature | Vendor doc (date) | Result | Note |
| --- | --- | --- | --- | --- |
| Claude | **+** in project knowledge | Claude Help Center 9519177 (dateModified 2026-11-06) | verified | Quote: 'Click on the "+" button to add content to the project' |
| Claude | **Save instructions**, project instructions | same | verified | 'click "Save instructions."' |
| Claude | **Code execution and file creation** (or **Create and edit files**), **Settings**, **Capabilities** | Claude Help Center 12111783 (dateModified 2026-11-24) | verified, with a note | Path is for Free, Pro, Max, Ultra. Team and Enterprise owners set it in **Organization settings**. See F11 |
| Claude | New chat in a project | 9519177 | partly verified | Described ("initiate chats with Claude within the project"), no control name. Same as module 1 |
| ChatGPT | **•••** menu, **Project settings** | OpenAI Help Center 10169521 ("Updated: 3 days ago") | verified | Relative date only |
| ChatGPT | Add files to the project's files; Go or Plus minimum | same | verified | No button name on the page; the card names none. 25 files on Go and Plus. 6 knowledge files after module 2 do not fit Free (5) |
| ChatGPT | New project chat (steps 2 and 6) | same | not verified | No steps on the page. G2-PF-03 stays open. Card test covers it |
| Copilot | **All agents**, **...**, **Edit** | Microsoft Learn, Share and manage agents (2026-11-16) | verified | Quotes match |
| Copilot | **Update** | same | verified | "choose Update in the top right corner". Changes save automatically but users see them only after Update |
| Copilot | **Configure** tab, **Upload** | Microsoft Learn, Add knowledge sources (2026-11-16) | verified | "In the Knowledge section ... Upload" |
| Copilot | ".md is not a listed knowledge file type" | same | verified | List: .doc, .docx, .html (SharePoint only), .pdf, .ppt, .pptx, .txt, .xls, .xlsx |
| Copilot | **Instructions**, 8,000 characters | Microsoft Learn, Build agents (2026-11-16) | verified | Fallback text 7,171 characters fits |
| Copilot | No license or billing: agent cannot read knowledge files | Microsoft Learn, prerequisites (2026-11-16) | verified | "Custom knowledge: Embedded file content" is not available with no usage-based billing. Instructions and code interpreter are |
| Copilot | Upload run files in the agent chat (G2-PF-02) | Microsoft Support, File formats supported by Copilot (ms.date 2026-07-28, updated_at 2026-11-10) | partly verified | New doc. .csv and .md are listed for Copilot (Work and School) with a Copilot license. Agents and no-license users are not named. See F6 |
| Copilot | New chat (step 6) | Microsoft Learn, Build agents (2026-11-16) | partly verified | **New chat** is named only for the **Try it** pane. See F12 |
| Copilot | Download in the same session (session-only files) | mb-11 (checked 2026-11-20) | verified | Within 30 days |
| Gemini | **Customize**, **Skills**, click to edit, **Save** | Gemini Apps Help, skills page (no date) | verified labels, undated doc | Same as module 1 F11. Accepted by Dan in module 1 D3 with a check date. See F9 |
| Gemini | **Add**, **files**, **Upload** on an existing skill (step 1, log save card) | same | wrong label for this flow | Create flow: **Add**, then images or files, then **Upload**. Edit flow: "To add a file, click **Add files**". See F7 |
| Gemini | Skill **Instructions** field | same | verified | The page now names the field "Instructions" (module 1 report said no exact label) |
| Gemini | Re-upload the whole skill if adding files fails | same | verified | "To update files in a skill, you need to upload the entire skill with its reference files again" |
| Gemini | **/** (or **@**) to pick the skill | blog.google (2026-09-30); Help page (no date) | verified for **/** | Blog names "/" only. "@" is on the undated page ("if you have the updated shortcut"). Card cites the blog by a wrong title. See F8 |
| Gemini | .md and .csv files in a skill | Help page (no date) | verified, undated | Both listed as supported |
| Gemini | Do not turn on Canvas or Deep Research | gm-06 (checked 2026-11-20) | partly verified | Within 30 days. Page undated |
| Gemini | "Gems are now skills" | gm-02 (verified) | verified for personal accounts | Workspace business Gems stop no sooner than 2027-03-01. Dan decided the line at Gate 1 (PA-09). See F10 |

## Findings and fixes

Numbered most important first. "Fail" means the builder must fix it or Dan must accept it.

| # | Severity | Where | Finding | Fix |
| --- | --- | --- | --- | --- |
| F1 | Fail | Slide 2.2 talk track | "Both also say a manual program is slow." Clozd (W1) does not say it. Only Corporate Visions (W2) says it. The Gate 1 verifier report recorded "Slow, does not scale: W2 only" | Change to: "Corporate Visions also says a manual program is slow." |
| F2 | Fail (Dan decides) | Slide 2.2 on-slide line 2, Sources line | "Manual win/loss is slow and does not scale" is an on-slide claim with one source (W2). The rule needs 2 independent sources. Candidate second source: Klue, "Difficulty running win-loss analysis", Adam McQueen (https://klue.com/blog/difficulty-running-win-loss-analysis), published 2024-05-29, modified 2025-09-04. It is a first-hand account: "This entire process would take so long that by the time I could share results, it was an out-of-date point in time." Vendor, older than 12 months (age flag), independent of W1 and W2. It supports "slow", not "does not scale" | Option A: Dan accepts Klue with its age flag. Change line 2 to "Manual win/loss is slow." Add Klue to the Sources line and the ledger. Option B: move the line to the talk track, attributed to Corporate Visions. Recommended: A |
| F3 | Minor | Slide 2.2 talk track | "both wrote in 2026". Corporate Visions first published its guide on 2024-11-12 and updated it on 2026-07-30 | Change to: "Two win/loss firms, Clozd and Corporate Visions, both say in 2026 pages that ..." |
| F4 | Pass, with a correction to D11 | D11; spec module 2 bottleneck | D11 says only W3 supports "many teams do not run win/loss". W1 also says it: "the majority of companies do not conduct any sort of formal, post-decision deal analysis", and "fewer than 20%", citing Pragmatic Marketing. W3 (2022) says "often underutilized" and "35 percent", from a Pragmatic survey. Both rest on old Pragmatic survey data, so they count as one source, and the figures fail the 2026 rule. W2 does not say it, but the approved spec cites W1 and W2 for it. Gap: no 2026 source found (Klue 2025 Win-Loss Trends Report has no such figure) | Keep D11 option A: off the slides. The talk track line "Win/loss is the data most teams do not get" is Dan's course view (Gate 1 theme f), and it must not be presented as a finding. Correct the D11 text. Tell Dan the spec bottleneck line cites W2 for a claim W2 does not make (spec is fingerprinted, so his yes is needed) |
| F5 | Pass, age flag | Slide 2.8 talk track, D13 | Market visit article (modified 2025-08-27, 15 months old) supports the frame. It is presented as "Pragmatic frames ...", an attribution, not a finding. Dan said yes to the Gate 1 age flags and PA-04 (`gate-1-decisions.md`) | Keep D13 option A. Note in D13 that Dan accepted this age flag at Gate 1. Side note: `alignment-log.yaml` PA-03 says this article says "Ask for permission first" for recording. I did not find that sentence today. Module 2 does not rely on it |
| F6 | Open, card wording is safe | Copilot card notes, D8, card test | G2-PF-02 is now partly verified. A new Microsoft doc lists .csv and .md uploads for Copilot (Work and School) with a Copilot license. It does not name agents or no-license users. The card's "upload, or paste the text" covers both cases | Keep D8 option A. Add the new doc to the D8 note and to the matrix (proposed mb-ui-15). The card test still checks the agent chat, licensed and no license |
| F7 | Fail | Gemini card step 1, log save card row, card test Gemini row | **Add**, **files**, **Upload** is the label path for a new skill. For an existing skill, the page says "To add a file, click **Add files**" | Step 1: "Add `job-card-win-loss` and `driver-code-book` to your skill with **Add files**." Log save row: "In your skill, **Add files**. Select **Save**." Update the card test row to match. Card test confirms the upload dialog |
| F8 | Minor | Gemini card vendor doc line | The blog title is "Let skills in Gemini tackle your most repetitive tasks" (2026-09-30), not "Automate tasks with skills". The blog names "/" only | Fix the title. Keep "/" first, "@" in brackets |
| F9 | Accepted exception | Gemini card | The skills Help page has no date, so it fails the dated vendor doc rule. Dan accepted it in module 1 D3 with a check date | Keep. Recheck before each delivery |
| F10 | Info | Gemini card header | "Gems are now skills" is true for personal accounts now. For Workspace business accounts, Gems stop no sooner than 2027-03-01 (gm-02). Dan chose this line at Gate 1 (PA-09) | No change. Recheck before the first 2027 delivery |
| F11 | Minor | Claude card notes, section 9 | **Settings**, then **Capabilities** is the path for Free, Pro, Max and Ultra. On Team and Enterprise, an owner sets it in **Organization settings**, and it is on by default | Add: "On Team or Enterprise, ask your admin." |
| F12 | Open, card test | Copilot card step 6; ChatGPT and Claude steps 2 and 6 | A new chat with the agent or in a project has no control name in any vendor doc. Copilot names **New chat** only in the **Try it** pane. G2-PF-03 stays open | No change. Card test records how a new chat starts on each platform |
| F13 | Stale text (builder) | `module.md` D1, D2, D5, "Changes needing Dan's yes" rows 1 and 2, case note 5 | Dan said yes on 2026-11-27 (commit e78ee77). Spec card step 6 now says "In a new chat". The spec stretch now says module 3, Claude card only. `expected-results.md` no longer says "(program minimum met)". D2 still says cl-sc-07 and cg-06 are not verified. Now: cl-sc-07 verified (doc), Dan's hands-on test pending; cg-06 verified (doc), not usable for the lab; mb-06 not verified; gm-07 not available for Workspace | Mark D1, D2 and D5 as decided by Dan, 2026-11-27. Update the D2 facts. Remove rows 1 and 2 from "Changes needing Dan's yes". Delete case note 5. Claude and ChatGPT card stretch lines can say "The schedule stretch is in module 3." |
| F14 | Pass | Copilot card and fallback | .md not a knowledge type, 8,000-character Instructions, no-license limit, session-only download: all verified against docs dated 2026-09-28 to 2026-11-16, checked within 30 days | None |

Failures: F1, F2 and F7 need a fix (F2 needs Dan's choice). F13 is stale text from today's decisions. F3, F8 and F11 are small wording fixes.

Gaps (not failures):

1. No 2026 primary source on how many teams run win/loss.
2. No 2026 second source for "manual win/loss does not scale".
3. No win/loss source for hardware or internal PM.

## Proposed platform matrix updates (for Dan's yes)

The matrix is fingerprinted. I made no change. Each row below waits for Dan's yes.

| Row | Change |
| --- | --- |
| cl-ui-09 | checked_on 2026-11-27. Page now says "Updated over 3 weeks ago". dateModified still 2026-11-06. All labels found again |
| cl-ui-10 | checked_on 2026-11-27. dateModified 2026-11-24. Add to limits: Team and Enterprise owners use Organization settings > Capabilities |
| cg-ui-09 | checked_on 2026-11-27. Page still says "Updated: 3 days ago" (relative date only). Labels found again |
| mb-ui-12, mb-ui-13, mb-01 | checked_on 2026-11-27. Same date, 2026-11-16. Labels and the 8,000 limit found again |
| mb-03 | source_date 2026-11-16 (was 2026-11-06). checked_on 2026-11-27. Note: the capability table has no row for file upload in chat |
| mb-ui-14 | checked_on 2026-11-27. Still partly verified. Agent chat and file types not stated |
| mb-ui-15 (new) | Feature: file formats for upload in Copilot (Work and School) with a Copilot license, for Copilot Chat, Pages, Notebooks and Create. .csv, .tsv, .xlsx for data analysis. .md, .txt, .docx, .pdf for documents. No size limit given. Agents not named. URL https://support.microsoft.com/en-gb/topic/file-formats-supported-by-copilot-1afb9a70-2232-4753-85c2-602c422af3a8. source_date 2026-07-28 (ms.date; updated_at 2026-11-10). checked_on 2026-11-27. Status: partly verified (licensed Copilot Chat yes; agent chat and no-license not stated). G2-PF-02 stays open for the agent chat |
| gm-ui-10 | checked_on 2026-11-27. Limits: the page now names the "Instructions" field. For an existing skill the label is **Add files**. Still undated |
| mb-build (note on mb-01) | The Build agents page names **New chat** only in the **Try it** pane |

Proposed ledger addition (for Dan's yes, age flag): Klue, "Difficulty running win-loss analysis", modified 2025-09-04, claim "manual win/loss is slow; results arrive out of date". Vendor. First-hand account, no statistic. Independent of W1 and W2.

## Sources opened on 2026-11-27

- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/prerequisites
- https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-content-to-microsoft-365-copilot-chat-prompts
- https://support.microsoft.com/en-gb/topic/file-formats-supported-by-copilot-1afb9a70-2232-4753-85c2-602c422af3a8
- https://support.google.com/gemini?p=pn_skills
- https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/
- https://www.clozd.com/blog/win-loss-analysis-5-common-mistakes (W1)
- https://corporatevisions.com/blog/how-to-conduct-win-loss-analysis-implementation-guide/ (W2)
- https://www.pragmaticinstitute.com/resources/articles/product/comprehensive-approach-to-win-loss-analysis (W3)
- https://pragmaticinstitute.com/resources/articles/product/how-to-overcome-8-common-market-visit-barriers (PA-04)
- https://klue.com/blog/difficulty-running-win-loss-analysis (candidate)
- https://klue.com/win-loss-trends-report (no figure found)
- Pragmatic Framework 2027 guide, page 7 (project files copy)
