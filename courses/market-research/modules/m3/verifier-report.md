# Verifier report: module 3 (module mode)

Course: `market-research`. Module 3, the weekly feedback run. Checked 2026-11-27 by the research verifier (Stage 3, step 2b).

Files checked: `modules/m3/module.md`, `modules/m3/kit/lab-3/`, `modules/m3/kit/kit-m4/`, `modules/m3/card-test.md`.

## How I checked

1. I checked only claims and features that are new since Gate 1, or that the module 2 verifier did not check on 2026-11-27. Focus from the task: the Claude Cowork schedule stretch, slide 3.2 (W4, W5), talk track claims, and G2-PF-03.
2. Core card screen names for Claude, ChatGPT, Copilot and Gemini are the same as module 2. The module 2 verifier reopened those docs on 2026-11-27. I did not check them again.
3. I opened the 2 Claude Cowork articles by curl and read the page metadata. I opened the other pages by WebFetch (the proxy blocks curl to them).
4. A check date older than 30 days fails. Every doc a module 3 card uses was checked on 2026-11-27. No date fails.
5. I did not edit `platform-matrix.yaml` or `evidence-ledger.yaml`. Both are fingerprinted. Proposed updates are in the last section.

## Results: claims

| Id | Claim (where) | Result | Note |
| --- | --- | --- | --- |
| C1 | "Tagging by hand is slow and inconsistent" (3.2 on-slide line; W4, W5) | verified, with a note | "Slow": W4 "Tagging, categorizing, and interpreting feedback is slow, subjective, and doesn't scale." W5 "Manual tagging creates a queue, and queues have a lag" and its time arithmetic. "Inconsistent": W5 "Two people tag the same complaint differently." W4 says "subjective", which is close but not the same word. 2 independent vendors. See F8 |
| C2 | "Two vendor pages from 2026 say the same thing about that work" (3.2 talk track) | verified | W4 2026-06-02 (Payton Christopher). W5 2026-07-27, no update date. Both 2026 |
| C3 | "ProductPlan ... says tagging feedback is slow and subjective, and insights sit in different tools" (3.2 talk track) | verified | W4 quotes above, and "Insights live in different tools, and no one has the full picture." Correctly attributed to one vendor |
| C4 | "Enterpret ... says tags get applied in different ways, and their meaning drifts over time" (3.2 talk track) | verified | W5: "Two people tag the same complaint differently." Drift: "the taxonomy stops evolving and starts decaying", "the trend lines stop making sense". Correctly attributed to one vendor |
| C5 | "When the tags drift, the trend lines lie" (3.2 talk track) | verified (1 source, attributed context) | Follows the Enterpret line. W5: "every chart built on the label is now unreliable". Acceptable as a paraphrase of the attributed source |
| C6 | "And when the pile grows, people stop reading" (3.2 talk track); POINT "so teams stop reading it" | not verified | Neither W4 nor W5 says people stop reading. It goes past both sources. See F3 |
| C7 | "The team that writes the most gets served first" (3.4 talk track) | partly verified | W18 (2026-11-04): "the most senior advocate or the noisiest channel gets served first" and "The loudest team wins." One source. The talk track states it as a fact, not as Enterpret's view. See F4 |
| C8 | "[IF ASKED FOR A SOURCE] One vendor page, from Enterpret, describes this for platform PMs" (3.4) | verified | W18 is an Enterpret guide on platform PM feedback. Intake, office hours and Slack are all quoted |
| C9 | "Hardware teams have the same issue. Install notes and technician notes hold product feedback" (3.4 talk track) | not verified | Only W17 supports it, and W17 is "not verified" in `workflows.yaml`, one source. See F5 |
| C10 | "Many feedback tools show you only the 'top movers'" (3.8 talk track) | not verified | No source in the module or the ledger. See F6 |
| C11 | "It uses Claude Cowork scheduled tasks, on paid plans" (3.9 talk track) | verified | 13854387: "available on all paid plans (Pro, Max, Ultra, Team, and Enterprise)" |
| C12 | "ChatGPT can schedule tasks, but a task in a project cannot read the project's files" (3.9) | verified (by matrix) | cg-06, checked 2026-11-27. Not new. Not reopened |
| C13 | "Copilot's agent builder schedule has no Microsoft doc we can check yet" (3.9) | verified (by matrix) | mb-06 not verified, only a third-party Message Center mirror (stretch verification, 2026-11-27) |
| C14 | "Gemini's schedule for skills works on personal accounts only" (3.9) | verified (by matrix) | gm-07: Spark tasks can call a skill, personal accounts only. gm-08 (Workspace scheduled actions) does not say it can use a skill. Wording is fair |
| C15 | Support tickets and call notes can hold health data, account or card data (3.11, lab brief, kit READMEs) | pass (data safety teaching point) | From the Gate 1 workflow note (`workflows.yaml` mr-wf-03 industry notes). Not a finding. No change |
| C16 | Paste sizes in D13, section 9 and the card test | verified | `wc -m` today: kit-m3 `problem-backlog.txt` 10,004. Week 1 3,872. Week 2 5,001. Fallback m3 6,856. Fallback m3-v4 7,194. kit-m4 `problem-backlog.txt` 15,176. All match the module |

## Results: step card screen names and features (new in module 3)

Claude Cowork stretch. Docs: "Schedule recurring tasks in Claude Cowork" (13854387, dateModified 2026-11-18T00:24:24Z, page shows "Updated over a week ago") and "Organize your tasks with projects in Claude Cowork" (14116274, dateModified 2026-11-12T18:55:42Z). Both titles on the card are correct. Both opened 2026-11-27.

| Card step | Screen name or feature | Doc | Result | Note |
| --- | --- | --- | --- | --- |
| Header | Paid plan | 13854387, 14116274 | verified | "all paid plans (Pro, Max, Ultra, Team, and Enterprise)" |
| Header | Claude Desktop | 14116274 | verified | "Projects in Cowork require the latest version of Claude Desktop" |
| 1 | **Projects**, **+** | 14116274 | verified | "Find Projects in the left navigation panel and click the "+" button" |
| 1 | Import the chat project | 14116274 | verified, label missing on card | Label is **Import from project**. Then a "Search projects in Chat…" field, pick the project, name it, "choose where to save it on your computer", then **Create**. The card names neither **Import from project** nor **Create**, nor the save location. See F1 |
| 1 | Instructions and files arrive | 14116274 | verified | "Clicking "Create" will transfer the files and instructions from your existing Claude project" |
| 2 | The new project's folder on your computer | 14116274 | partly verified | The import asks where to save the project on the computer. The doc does not say the scheduled task reads new files saved there later. Card test covers it |
| 3 | The project's **Scheduled tasks** | 14116274 | verified | "Each project has its own: ... Scheduled tasks: Set up recurring tasks that are specific to the project" |
| 3 | **New task**, then **Set up manually** inside a project | 13854387 | partly verified | Both labels are verified on the main **Scheduled** page ("Click "Scheduled" in the left sidebar ... Click "New task" in the upper right, then choose "Set up manually""). No doc shows **New task** inside a project. See F2 |
| 4 | Task name, prompt, frequency, folder | 13854387 | verified, one field missing | Fields in the "Create scheduled task" modal: task name, prompt, **approval mode**, frequency (hourly, daily, weekly, on weekdays, manually), model (optional), folder (optional). The card does not name the approval mode. See F1 |
| 4 | **Weekly** | 13854387 | partly verified | The doc writes "weekly" in a list. The exact label case is not shown. Card test records it |
| After 4 | **Save** | 13854387 | verified | "Click "Save" to add a new task to the Scheduled tasks page" |
| After 4 | Runs only while the computer is awake and Claude Desktop is open | 13854387 | verified, conditional | True only if a folder is picked: "If you pick a folder, Require this computer turns on, and the task runs only while your computer is awake and Claude Desktop is open." Without a folder, tasks "run remotely". See F7 |
| After 4 | "Your company must allow Cowork and folder access" | 13854387 | verified | "admins control Cowork access through the admin toggle". "The Require this computer option is only offered to organizations with Computer access turned on" |
| Section 9 row | No **Scheduled tasks** or no folder option: Cowork or Computer access off | 13854387 | verified | Same quotes. Add the new Claude experience as a third cause (F7) |
| Not on card | New Claude experience | 13854387, 14116274 | risk | "rolling out to Pro, Max, and Ultra plans ... some steps in this article may look different." In it, you describe the task in any conversation and click **Schedule**. See F7 |
| Not on card | Tasks move to the cloud | 13854387 | risk | "On Pro, Max, and Ultra plans ... scheduled tasks you created on your computer move to the cloud automatically." Remote tasks use "the files saved to your Claude account". The doc does not say what happens to a task with a local folder. See F7 |

Copilot no-license paste size (G2-PF-03).

| Item | Doc | Result | Note |
| --- | --- | --- | --- |
| Longest message Copilot Chat accepts | Microsoft Support, "Limits for features in Microsoft Copilot Chat" (https://support.microsoft.com/microsoft-365-copilot/limits-for-features-copilot-chat, ms.date 2026-10-31, updated_at 2026-11-18) | gap (no vendor number) | "Because service limits can vary, Microsoft does not publish or share specific numeric limits." The page "applies to Microsoft 365 users without a Copilot license add-on". It does not name agents. Microsoft Learn "Features in Copilot" (ms.date 2026-11-17) gives no prompt limit and links to this page. A doc check cannot close G2-PF-03. Only the card test can. See F9 |
| Forum figures (Microsoft Q&A, Tech Community) | not vendor docs | not used | Q&A answer 12645819 (2026-03-06) is an AI answer and gives only the 8,000-character instructions limit. Do not cite forum figures |

## Findings and fixes

Most important first. "Fail" means the builder must fix it or Dan must accept it.

| # | Severity | Where | Finding | Fix |
| --- | --- | --- | --- | --- |
| F1 | Fail | Claude card, schedule stretch steps 1 and 4 | Step 1 skips 3 doc labels and one choice: **Import from project**, the "Search projects in Chat…" pick, where to save on the computer, and **Create**. Step 2 needs that save location. Step 4 skips the approval mode field, so a learner meets an unnamed field. Step 4 also has 4 actions in one step (house rule 8) | Rewrite to 6 steps or fewer, 1 action each. Proposed: 1. "In Cowork, select **+** next to **Projects**, then **Import from project**." 2. "Pick "Market Evidence Agent". Choose where to save it on your computer. Select **Create**." 3. "Save next week's export in that folder." 4. "In the project's **Scheduled tasks**, select **New task**, then **Set up manually**." 5. "Enter a name, the prompt, **Weekly** and the project folder. Keep the default approval mode." 6. "Select **Save**." Update the card test row to name **Import from project** and **Create** |
| F2 | Open, card test | Claude card stretch step 3; card test row 3 | **New task** and **Set up manually** are documented on the **Scheduled** page in the left sidebar, not inside a project. 14116274 only says each project has "Scheduled tasks" | Keep the project path (it gives the task the project instructions and files). Add a note: "No **New task** in the project? Select **Scheduled** in the left sidebar, then **New task**, and pick the project folder." The card test records which path shows the labels |
| F3 | Fail (wording past source) | 3.2 POINT and talk track | "when the pile grows, people stop reading" and "so teams stop reading it" are not in W4 or W5 | POINT: "Feedback arrives every day, and tagging it by hand is slow and inconsistent." Talk track: cut "And when the pile grows, people stop reading." Or say it as a question to the room: "What happens to your pile when nobody has time to tag it?" |
| F4 | Minor (1 source stated as fact) | 3.4 talk track | "The team that writes the most gets served first" rests on W18 only, but is said as a general fact. The source line for it is only in the "[IF ASKED]" note | Change to: "The risk is that the team that writes the most gets served first." Keep the [IF ASKED] line |
| F5 | Minor (no verified source) | 3.4 talk track | "Hardware teams have the same issue. Install notes and technician notes hold product feedback." W17 is one source and "not verified". Gate 1 recorded a hardware gap for row 03 | Reword as the case design, not a finding: "In hardware, install notes and technician notes can hold product feedback too. The Larkspan export has an "Install note" channel for that reason." |
| F6 | Minor (unsourced claim) | 3.8 talk track | "Many feedback tools show you only the "top movers"" is a claim about the market with no source | Reword as a design choice: "A "top movers" view lets a number decide what you see. This job does not." |
| F7 | Open, card test (Dan's hands-on test) | Claude card stretch notes; card test; section 9 last row | Three doc risks the card does not name. (a) The new Claude experience is rolling out to Pro, Max and Ultra, and "some steps ... may look different". (b) On Pro, Max and Ultra, tasks made on the computer "move to the cloud automatically", and remote tasks use files saved to the Claude account. The doc does not say if a folder task stays local. (c) "Require this computer" is offered only to organizations with Computer access on. The doc does not say what a Pro user sees | Add 3 card test rows: "New Claude experience: yes or no. If yes, which path makes the task", "After **Save**, does the task keep the folder and Require this computer, or move to the cloud?", "Pro plan: is the folder option offered?" Add to section 9 last row: "Or the account has the new Claude experience. Stop the stretch." Keep D1 option A until the test passes |
| F8 | Pass, note | 3.2 on-slide line | "Inconsistent" is W5's word. W4 says "subjective". Both describe the same burden (different people tag differently), so the line passes. "Slow" has both sources | No change needed. Optional: Dan may prefer "slow and subjective", but then only W4 is direct, so keep the current line |
| F9 | Open (gap, not a failure) | D13, Copilot card no-license box, card test | Microsoft does not publish a chat message limit (Support page, 2026-10-31). G2-PF-03 cannot close by doc. The card's "Upload it, or paste the text" and the section 9 recovery (backlog alone first) are the right design | Keep D13 option A. Add the Support page to the D13 note and the matrix (proposed mb-ui-16). Card test decides |
| F10 | Fail (card gap linked to G2-PF-03) | Copilot card no-license box, debrief rerun; card test | The no-license box says to send `problem-backlog.txt` "At step 2". The debrief rerun is a new chat, so a no-license agent has no backlog unless the learner sends it again. The card does not say so. That rerun message is also the largest: backlog 10,004 + week 1 3,872 + week 2 5,001 = 18,877 characters, more than the G2-PF-03 target (15,400). The card test tests only backlog plus week 1 | Add to the no-license box: "At the debrief rerun, send `problem-backlog.txt` first. Then send both exports." Add a card test row: "No-license debrief rerun: backlog, then both exports (18,877 characters in total). Record if one message, or how many" |
| F11 | Minor (date) | ChatGPT card header | Says cg-ui-09 "Updated: 3 days ago" when seen 2026-11-26. The module 2 verifier saw the same text on 2026-11-27 | Change "seen 2026-11-26" to "seen 2026-11-27" |
| F12 | Info (module 4) | kit-m4 `problem-backlog.txt` | It is 15,176 characters. A module 4 no-license learner pastes it in chat. That is near the G2-PF-03 target and is not the evidence pack the spec names | Tell the module 4 builder. No change in module 3 |
| F13 | Pass | Slide 3.9 claims, card source lines, kit counts | C11 to C14 and C16 match the docs and the matrix. Card titles and page dates for 13854387 and 14116274 match the metadata | None |

Failures: F1, F3 and F10 need a fix. F4, F5, F6 and F11 are small wording fixes. F2, F7 and F9 stay open for the card test.

Gaps (not failures):

1. No vendor number for the longest Copilot Chat message (G2-PF-03). Microsoft says it does not publish one.
2. No doc for **New task** inside a Cowork project.
3. No doc on whether a scheduled task with a local folder stays local after the move to the cloud.
4. Hardware and internal PM for row 03: still one source each (W17 not verified, W18).

## Proposed platform matrix updates (for Dan's yes)

The matrix is fingerprinted. I made no change. Each row waits for Dan's yes.

| Row | Change |
| --- | --- |
| cl-sc-07 | source_date 2026-11-18 (dateModified 2026-11-18T00:24:24Z; replace "approx 2026-11-19"). checked_on 2026-11-27. Add screen names: **Scheduled** (left sidebar), **New task**, **Create with Claude** or **Set up manually**, "Create scheduled task" modal (task name, prompt, approval mode, frequency, model, folder), **Save**. Add limits: "Require this computer is offered only to organizations with Computer access turned on"; "On Pro, Max and Ultra, and on Team and Enterprise with Cowork in the cloud, tasks created on the computer move to the cloud automatically"; "New Claude experience: describe the task in any conversation, then **Schedule**". Status stays verified (doc), test pending |
| cl-ui-11 (new) | Feature: Cowork projects screen names. **Projects** (left navigation), **+**, **Start from scratch**, **Import from project**, "Search projects in Chat…", choose where to save on the computer, **Create**, **Use an existing folder**. Each project has Instructions, Scheduled tasks, Context, Memory. Needs the latest Claude Desktop. Paid plans. URL https://support.claude.com/en/articles/14116274-organize-your-tasks-in-claude-cowork. source_date 2026-11-12. checked_on 2026-11-27. Status: verified (doc). Limits: **New task** inside a project not shown |
| mb-ui-16 (new) | Feature: limits for Copilot Chat with no Copilot license. "Microsoft does not publish or share specific numeric limits." Applies to Microsoft 365 users without a Copilot license add-on, work or school account. Agents not named. URL https://support.microsoft.com/microsoft-365-copilot/limits-for-features-copilot-chat. source_date 2026-10-31 (ms.date; updated_at 2026-11-18). checked_on 2026-11-27. Status: verified (doc) that no number is published. G2-PF-03 stays open for the card test |

Proposed ledger updates (for Dan's yes): W4, W5 and W18 in `workflows.yaml`, checked_on 2026-11-27. Quotes found again. No new ledger entry.

## Sources opened on 2026-11-27

- https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork
- https://support.claude.com/en/articles/14116274-organize-your-tasks-in-claude-cowork
- https://www.productplan.com/blog/data-rich-insight-poor-why-customer-feedback-isnt-driving-your-roadmap (W4)
- https://www.enterpret.com/guides/the-6-hidden-costs-of-tagging-customer-feedback-by-hand-in-2026 (W5)
- https://www.enterpret.com/guides/the-6-ways-platform-pms-gather-feedback-from-internal-and-external-customers (W18)
- https://support.microsoft.com/microsoft-365-copilot/limits-for-features-copilot-chat
- https://learn.microsoft.com/en-us/copilot/features
- https://learn.microsoft.com/en-us/answers/a/12645819 (forum, not used)
