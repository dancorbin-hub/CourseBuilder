# Verifier report: module 4 (module mode)

Course: `market-research`. Module 4, the alternatives map and the first hand-off. Checked 2026-11-27 by the research verifier (Stage 3, step 2b).

Files checked: `modules/m4/module.md`, `modules/m4/kit/lab-4/`, `modules/m4/kit/kit-m5/`, `modules/m4/card-test.md`, `modules/m4/example-oi-05.md`.

## How I checked

1. I checked only claims and features that are new since Gate 1, or that the module 2, 3 and 5 verifiers did not check on 2026-11-27. Focus from the task: the second-agent manual hand-off stretch on Claude and ChatGPT, the bottleneck claims (N13, W21), slide and talk track claims, and the OI-05 story.
2. Core card screen names for Copilot and Gemini, and the log save labels for Copilot (mb-ui-12) and Gemini (gm-ui-10), are the same as modules 2, 3 and 5. Those verifiers reopened the docs on 2026-11-27. I did not check them again.
3. I opened the Claude pages by curl and read the page metadata. I opened the OpenAI, Wynter and DEV Community pages by WebFetch.
4. A check date older than 30 days fails. The oldest check date a module 4 card uses is 2026-11-20 (mb-01, mb-02, mb-11, gm-01, gm-06; 7 days). No date fails.
5. I did not edit `platform-matrix.yaml` or `evidence-ledger.yaml`. Both are fingerprinted. Proposed updates are in the last section.

## Results: claims (slides, talk track, summary)

| Id | Claim (where) | Result | Note |
| --- | --- | --- | --- |
| C1 | "Hand-built competitor documents age fast" (4.2 on-slide line; N13, W21) | partly verified | "Age fast": 2 independent sources. Wynter (N13 primary, May 2026): battlecards "go stale within 3 months" (47%), CI "goes stale fast" (24%). W21: "internal documents that age quickly". "Hand-built": W21 only ("manually reconstructing this context by opening dozens of tabs"). Wynter has no wording on manual work. See F3 |
| C2 | "A 2026 Wynter survey of B2B SaaS product marketers found that for many, competitive work is one task among many" (4.2 talk track) | verified, wording note | Wynter primary: "PMM owns it on the side" (52%); "product marketing runs CI as a side job". "One task among many" is the MarketingProfs wording, not Wynter's. Published May 2026, survey 2026-04-27 to 28, 101 B2B SaaS PMMs. No figure on the slide. See F6 |
| C3 | "The same survey, and a 2026 article ..., say the same thing: hand-built competitive documents go stale fast" (4.2 talk track) | partly verified | The survey says battlecards go stale. It does not say "hand-built". Only W21 does. See F3 |
| C4 | "a 2026 article by the maker of a competitive analysis tool" (4.2 talk track) | partly verified | W21 says "Originally published at seeto.ai". The username is yl_seeto. No sentence says the author makes Seeto. The page shows "Posted on Feb 10" with no year (2026 inferred at Gate 1). See F6 |
| C5 | POINT 4.2: a competitor list "rarely shows what lost buyers really chose" | not verified | No source. Gate 1 recorded this as a gap (mr-wf-10 open_gaps). The module itself keeps the claim off the slides (B10), but the POINT states it as a fact. See F2 |
| C6 | "Most teams answer from a competitor list. Somebody built it by hand, a while ago." (4.2 talk track) | not verified | "Most teams" has no source. Wynter surveyed PMMs about CI, not how teams answer "lost to whom". See F2 |
| C7 | "We found no published study on how often that happens" (4.2 talk track) | verified (gap) | Matches mr-wf-10 open_gaps. Wynter's "do nothing explicitly" (23%) is the PMM response to copied messaging, not a buyer choice, so it does not fill the gap |
| C8 | Summary row: "Teams track named competitors and miss the workarounds and "do nothing" that buyers choose" (section 1) | not verified | Copied from the Gate 1 bottleneck text. No source. Not on a slide. See F10 |
| C9 | Hardware and internal platform alternatives are "examples, not findings" (4.4 talk track) | verified (gap) | `workflows.yaml` mr-wf-10 contexts: both "gap, no source found". Labeled correctly |
| C10 | "No platform documents one agent calling another automatically for this setup" (4.8 talk track) | verified (by stretch file) | `stretch-verification-2026-11.md` (2026-11-27): automatic hand-off "not verified" on Claude and ChatGPT, "not available" on Copilot and Gemini. Claude plugin agents can delegate, but no doc shows agent 2 reading agent 1's output file. "For this setup" keeps it accurate |
| C11 | "The course team checked the vendor docs. A hands-on test is still open" (4.8 talk track) | verified, note | True. ChatGPT file download is only partly verified (cg-08). See F5 |
| C12 | "A scheduled task in a project cannot read project files" (ChatGPT card stretch) | verified (by matrix) | cg-06, checked 2026-11-27. Not reopened |
| C13 | OI-05 story (4.3) | pass, one note | See "OI-05 story check" below and F4 |
| C14 | Kit character counts (section 8, READMEs, card test) | verified | `wc -m` today: job card 1,497, lab-4 map 2,192, fallback m4 7,419, record sheet 1,944, brief v5 3,491, driver log 7,616, kit-m5 map 3,286, fix rules 1,016, fallback m4-v5 5,388, problem backlog 15,194, evidence pack 15,350 (split at "## Part 3": 6,590 and 8,760), check sample 2,290, brief v4 3,253. All 14 `.txt` copies match their `.md` (`cmp`). The 7 "no change" kit-m5 files match kit-m4. Brief v5, driver log and map match `modules/m5/kit/kit-m5-draft/` |
| C15 | Case claims on 4.6, 4.14, 4.15 and in section 6 (record ids, counts, quotes) | pass (case data) | From `case/`, not external. Not a verifier check |

## OI-05 story check (`example-oi-05.md`, slide 4.3)

| Check | Result | Note |
| --- | --- | --- |
| Told as Pragmatic's story, not the instructor's own (decision 43) | pass | Talk track opens "This is a story from Pragmatic's own work with a client." Stage direction: "TELL IT AS PRAGMATIC'S STORY, NEVER AS YOUR OWN" |
| Not presented as a sourced statistic or study | pass | No number, no percentage, no study. Sources line says "Pragmatic client story, from Dan". The lessons are framed as lessons for the map |
| Guardrails (no client name, dates, values, product names, people) | pass | "a large global technology and consulting company" (guardrail wording). The contract and the "principles Pragmatic first taught them" line in Dan's notes are not used. Good |
| Story matches Dan's words | pass | Every talk track fact is in `example-oi-05.md`: long relationship, own training center, long set-up and norms, different team needs, came back for private and tailored core and AI classes, a mix worked best |
| Slide headline "We built it ourselves." shown as a quote | note | Dan's notes hold no direct quote from the client. The visual intent sets it "as a quote in large type". A learner can read it as the client's own words. See F4 |
| Pragmatic permission | open | D11. Dan must confirm before Gate 3 approval. Not a verifier check |

## Results: step card screen names and features

### Claude second-agent stretch

Docs: Claude Help Center, "How can I create and manage projects?" (9519177, dateModified 2026-11-06T18:06:37Z). "Create and edit files with Claude" (12111783, dateModified 2026-11-24T22:57:06Z). "What are projects?" (9517075, dateModified 2026-10-30, unchanged). All opened 2026-11-27.

| Step | Screen name or feature | Result | Note |
| --- | --- | --- | --- |
| 1 | **Projects**, **+ New Project** | verified | "click "Projects"" ... "Click "+ New Project" in the upper right corner." Then a name and description |
| 2 | **Set project instructions** | verified, save missing | "Click on "Set project instructions."" Then "click "Save instructions."" The step does not name **Save instructions**. The card header does. See F7 |
| 3 | **+** in project knowledge | verified | "Click on the "+" button to add content to the project." |
| 4 | Run the win/loss job in the first project | n/a (prompt) | Job card input matches the evidence pack (CRM export, interviews) |
| 5 | Download the driver log file from the chat | verified | "Claude will generate the file, which you can then download directly from the conversation." "Claude can make plain text files (such as .csv, .md, and .html)". 30 MB per file. Needs **Code execution and file creation** on (core card note covers it). No "no file" fallback on this card. See F7 |
| 6 | Send the file in a new chat in the second project | verified | "You can also upload CSV, TSV, and other files" (12111783). New chat in a project: described, no control name (cl-ui-09 limits; m2 F12) |
| Header | Plan | note | All plans have projects. "Free users can create a maximum of five projects." A Free learner with 5 projects cannot add a second project. See F9 |
| Risk | New version of projects (cl-pj-11) | not verified (kept) | 9517075 unchanged. The core card note ("one conversation with a Library? Tell the instructor") covers it |

### ChatGPT second-agent stretch

Docs: OpenAI Help Center, "Projects in ChatGPT" (10169521, page shows "Updated: 19 hours ago" on 2026-11-27, so about 2026-11-26). "Uploading files and audio to ChatGPT" (8555545, "Updated: 19 hours ago"). "Creating and editing documents, spreadsheets and presentations with ChatGPT" (20001278, "Updated: 19 hours ago"). OpenAI Academy, "Working with files" (published 2025-08-06, last updated 2026-09-04). All opened 2026-11-27.

| Step | Screen name or feature | Result | Note |
| --- | --- | --- | --- |
| 1 | "In the sidebar, select **New project**" | partly verified, label path changed | Page now: "hover over **Projects** in the sidebar and select the plus icon (+) for **New project**." Then name, optional icon and color, then **Create project**. The page changed since cg-ui-09 (2026-11-26). See F1 |
| 2 | Paste the brief into **Project settings** | verified, field missing | "select the more options menu (•••) in the upper-right corner," then "Project settings". Enter text in the "Instructions field". See F1 |
| 3 | Add files to the project's files | verified | "uploading PDFs, spreadsheets, docs, images, or by pasting text". No button name (same as cg-ui-09). Go and Plus 25 files per project |
| 4 | Run the win/loss job in the first project | n/a (prompt) | |
| 5 | Download the driver log file | partly verified (cg-08) | Academy: download "ChatGPT-generated outputs (e.g., updated spreadsheets or PDFs)". No plans, no Projects, no .md or .csv output. Help article 20001278 now loads, but names no download steps, no Projects, and only .docx, .xlsx, .pptx templates. Data analysis article 8437071 ("Updated: 2 days ago") names no downloads. The card's "No file? Copy the driver log table into a text file" is the right fallback. See F5 |
| 6 | Send the file in a new chat in the second project | verified | 8555545: "select the plus icon ("+") in the message box, then select "Add photos & files"." Documents on Free and paid plans. "Free users are limited to 3 file uploads per day." The card does not name the labels. Optional, see F1 |
| Header | Plan Go or Plus or higher | verified | 10169521: "Users can create an unlimited amount of projects." Go and Plus 25 files per project |
| Card header | "Updated: 3 days ago" when seen 2026-11-26 | stale | Page shows "Updated: 19 hours ago" on 2026-11-27. See F8 |

### Log save card (new for module 4: 2 files)

| Platform | Label | Result | Note |
| --- | --- | --- | --- |
| Claude | Delete the old file in project knowledge | not verified (no doc) | 9519177 opened today: it describes adding knowledge and deleting projects, not deleting a knowledge file. Same gap as cl-ui-09 limits. The module 3 card has the same text. See F11 |
| ChatGPT | Open the old file in the project sources list. Delete it | verified | "you can open it from the project sources list to preview, download, or delete it" |
| Copilot | **X**, **Remove**, **Upload**, **Update** | verified (by matrix) | mb-ui-12, checked 2026-11-26 |
| Gemini | **More**, **Replace file**, or whole-skill re-upload | verified (by matrix), conflict kept | gm-ui-10, undated page (module 1 D3). The card gives the re-upload fallback |

### Core cards

No new screen name in the core steps. Claude (cl-ui-09, cl-ui-10), ChatGPT (cg-ui-09), Copilot (mb-ui-12, mb-ui-13, mb-ui-14, mb-01, mb-11) and Gemini (gm-ui-10, gm-01, gm-06) rows were checked from 2026-11-20 to 2026-11-27. Today I found again: Claude **+**, **Set project instructions**, **Save instructions**, **Settings** > **Capabilities** and **Organization settings** > **Capabilities**; ChatGPT **•••** > **Project settings** > Instructions. Pass.

## Findings and fixes

Most important first. "Fail" means the builder must fix it or Dan must accept it.

| # | Severity | Where | Finding | Fix |
| --- | --- | --- | --- | --- |
| F1 | Fail | ChatGPT card stretch steps 1 and 2; card test ChatGPT stretch row 1 | The OpenAI page changed on about 2026-11-26. **New project** is now under the **+** next to **Projects** in the sidebar, then **Create project**. Step 2 names **Project settings** but not the **Instructions** field | Step 1: "In the sidebar, select **+** next to **Projects**. Name it "Alternatives Map Agent". Select **Create project**." Step 2: "In **Project settings** (**•••** menu), paste your brief, with your fixed rule 4, into **Instructions**." Optional, step 6: "In a new chat in the second project, attach the driver log file with **+**, then **Add photos & files**. Send "Run the alternatives map job"." Card test row: "**+** next to **Projects**, **Create project**, **•••**, **Project settings**, **Instructions** match the screen" |
| F2 | Fail (wording past source) | 4.2 POINT; 4.2 talk track | POINT: a competitor list "rarely shows what lost buyers really chose". Talk track: "Most teams answer from a competitor list." Neither has a source. Gate 1 recorded the buyer-choice part as a gap, and B10 keeps it off the slide, but the POINT and talk track state it as fact | POINT: "A hand-built competitor list ages fast, and it lists companies, not what lost buyers chose." Talk track: "Where does the answer come from? Often a competitor list, built by hand a while ago." Or ask it to the room: "Where does your team's answer come from?" |
| F3 | Fail (one source for "hand-built") | 4.2 on-slide line and talk track | "Age fast" has 2 independent sources (Wynter: battlecards go stale; W21: documents age quickly). "Hand-built" has W21 only, and W21 is weak. The talk track says both sources say "hand-built competitive documents go stale fast". Wynter does not say "hand-built" | Slide: "Competitor documents age fast." Talk track: "The same survey found that battlecards go stale fast. A 2026 article on a competitive analysis tool's site says documents built by hand age quickly." Option B: keep "Hand-built" on the slide only if Dan accepts W21 alone for that word |
| F4 | Minor (quote with no source) | 4.3 headline and visual intent | "We built it ourselves." is set as a quote. Dan's notes hold no direct quote from the client. Learners can take it as the client's words | Drop the quote marks and the quote styling: headline "Built it themselves". Or keep it and label it in the talk track: "In effect, they said: we will build it ourselves." The rest of the OI-05 use passes |
| F5 | Open, card test | ChatGPT stretch step 5; card test ChatGPT stretch row 2 | ChatGPT file download stays partly verified (cg-08). The new Help article 20001278 does not close it: no download labels, no Projects, no .md or .csv output. Brief rule 7 asks for Markdown or CSV | No card change. The "No file? Copy the driver log table into a text file" fallback stays. Dan's test 4 records file type and plan. Keep the stretch marked "not yet tested" |
| F6 | Minor (wording) | 4.2 talk track | "For many, competitive work is one task among many" is the MarketingProfs wording. Wynter says CI is run "on the side" or "as a side job" (52%). "By the maker of a competitive analysis tool": the page says "Originally published at seeto.ai" and does not say the author makes Seeto | "A 2026 Wynter survey of B2B SaaS product marketers found that for about half of them, competitive work is a side job." "A 2026 article first published on a competitive analysis tool's site ..." |
| F7 | Minor (card gaps) | Claude card stretch steps 2 and 5 | Step 2 does not name **Save instructions** (the doc does; the card header does). Step 5 has no "no file" fallback. The ChatGPT card and section 9 have one | Step 2: "Paste your brief, with your fixed rule 4, into **Set project instructions**. Select **Save instructions**." (Dan decides if "paste, then save" is one action, as module 5 F3.) Step 5: "Download that driver log file. No file? Copy the driver log table into a text file." |
| F8 | Minor (date text) | ChatGPT card header | "Updated: 3 days ago" when seen 2026-11-26. On 2026-11-27 the page shows "Updated: 19 hours ago" (about 2026-11-26). Module 3 F11 flagged the same line | "Updated: 19 hours ago" when seen 2026-11-27 (about 2026-11-26) |
| F9 | Minor (plan limit) | Claude card stretch | Claude Free has at most 5 projects. A Free learner with 5 projects cannot make the second project | Add to the stretch line: "Free plan: 5 projects at most." |
| F10 | Minor (unsourced line, Dan's view) | Section 1 summary, workflow row | "Teams track named competitors and miss the workarounds and "do nothing" that buyers choose" has no source. It is not on a slide | Add "(no source; recorded gap)" after the sentence |
| F11 | Open, card test | Claude log save card ("delete the old `alternatives-map` and `driver-log`") | No Claude doc describes deleting a project knowledge file (9519177 opened today). Same text in module 3, not flagged there | No card change. Add to the card test Claude log save row: "Record the label to delete a knowledge file." Add the label to cl-ui-09 after the test |
| F12 | Open, design (Dan decides) | Claude and ChatGPT stretch steps 3 and 6 | The second project gets only the job card, the map and the driver log file. The map job card input also names the CRM export, interview notes and the problem backlog. Fixed rule 4 says "read the interview" and flag CRM and buyer mismatches. Brief rule 1 says use only what the PM gives. So the second agent cannot run rule 4's interview check or output 4 (backlog link). This is a design point, not a doc failure. The pass condition (links only) can still pass | Option A (recommended): keep the file as the only hand-off (that is the teaching point). Add to the Pass line: "The second project has no interviews, CRM export or backlog. Your rule 4 interview check runs in the first project." Add a card test row: "Does the second project ask for the interviews, CRM export or backlog? Record what it does with rule 4." Option B: in step 6, also send Parts 2 and 3 of the evidence pack |
| F13 | Info | Copilot no-license box | The evidence pack is 15,350 characters. With the prompt (about 30 characters) it is about 15,380, 20 under the G2-PF-03 target. Microsoft publishes no limit (module 3 F9). The split at "## Part 3" is the right recovery | No change. Card test records it |
| F14 | Pass | Claude stretch steps 1, 3, 5, 6; ChatGPT steps 3, 6; slide 4.8; C7, C9, C10, C12, C14; OI-05 use | Match the docs, the matrix and the stretch file. "Stretch (vendor doc checked, not yet tested)" is the right label | None |

Failures: F1, F2 and F3 need a fix (F3 has a Dan option). F4, F6, F7, F8, F9 and F10 are small wording fixes. F5, F11 and F12 stay open for the card test or Dan.

Gaps (not failures):

1. No source on teams that miss "do nothing" and workarounds in their competitor tracking (mr-wf-10).
2. No second source for "hand-built" competitive documents (W21 only, weak).
3. No OpenAI doc for downloading a generated file in a project chat, or for .md or .csv output (cg-08).
4. No Claude doc for deleting a project knowledge file.
5. Hardware and internal PM for row 10: no source. The OI-05 story is an anecdote, not a source.

## Proposed platform matrix updates (for Dan's yes)

The matrix is fingerprinted. I made no change. Each row waits for Dan's yes.

| Row | Change |
| --- | --- |
| cl-pj-01 | source_date 2026-11-06 (dateModified; replace "approx 2026-11-05"). checked_on 2026-11-27. "Free users can create a maximum of five projects" found again |
| cl-ui-09 | checked_on 2026-11-27. **+ New Project** ("upper right corner"), **Set project instructions**, **Save instructions**, **+** found again. Limits unchanged: no knowledge file delete on the page |
| cl-fo-06 | source_date 2026-11-24 (dateModified; replace "approx 2026-11-05"). checked_on 2026-11-27. Add: "download directly from the conversation"; plain text files ".csv, .md, and .html"; 30 MB per file |
| cg-01 | source_date approx 2026-11-26 (page "Updated: 19 hours ago" on 2026-11-27). checked_on 2026-11-27. Add: "Users can create an unlimited amount of projects." The cg-01 and cg-03 conflict is now resolved: 8555545 says Go and Plus 25 files per project |
| cg-ui-09 | source_date approx 2026-11-26. checked_on 2026-11-27. Change the screen names: "hover over **Projects** in the sidebar and select the plus icon (+) for **New project**", then **Create project**; **•••** (upper right) > **Project settings** > **Instructions** field; project sources list to preview, download or delete; **Add to project sources** on a response |
| cg-03 | url https://help-lb.openai.com/en/articles/8555545-uploading-files-and-audio-and-video-in-chatgpt (title now "Uploading files and audio to ChatGPT"). source_date approx 2026-11-26. checked_on 2026-11-27. Add screen names: **+** in the message box, then **Add photos & files**. Documents on Free and paid plans. Free 3 uploads per day. Projects: Free 5, Go and Plus 25, Edu, Pro, Business, Enterprise 40. Remove the "Plus 20" conflict note. Note: the older slug (8555545-file-uploads-faq) returned an old cached text with "Plus 20" on 2026-11-27 |
| cg-08 | checked_on 2026-11-27. Status stays partly verified. Add: Help article 20001278 now loads ("Updated: 19 hours ago"); it names no download labels, no Projects, and only .docx, .xlsx and .pptx templates. Data analysis article 8437071 ("Updated: 2 days ago") names no downloads. Academy page found again (last updated 2026-09-04) |

Proposed ledger updates (for Dan's yes):

| Id | Change |
| --- | --- |
| N13 | checked_on 2026-11-27. Add to the note: "Wynter says battlecards go stale within 3 months (47%) and within 6 months (82%). Wynter's own wording is 'PMM owns it on the side' (52%), not 'one task among many'. No wording on manual or hand-built work." |
| W21 (`workflows.yaml`) | checked_on 2026-11-27. Add to the note: "Page says 'Originally published at seeto.ai'. No sentence says the author makes Seeto. Only source for 'hand-built'." |

No new ledger entry.

## Sources opened on 2026-11-27

- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects (curl, dateModified 2026-11-06)
- https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude (curl, dateModified 2026-11-24)
- https://support.claude.com/en/articles/9517075-what-are-projects (curl, dateModified 2026-10-30)
- https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt
- https://help-lb.openai.com/en/articles/8555545-uploading-files-and-audio-and-video-in-chatgpt
- https://help-lb.openai.com/en/articles/8555545-file-uploads-faq (old cached text, not used)
- https://help-lb.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt
- https://help-lb.openai.com/en/articles/8437071-data-analysis-with-chatgpt
- https://academy.openai.com/public/clubs/work-users-ynjqu/resources/working-with-files (cg-08)
- https://wynter.com/research/the-state-of-competitive-intelligence-in-b2b-saas (N13 primary)
- https://dev.to/yl_seeto/competitive-intelligence-in-2026-why-most-teams-still-get-it-wrong-eb8 (W21)
