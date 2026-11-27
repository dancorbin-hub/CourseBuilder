# Verifier report: module 1 and course open (Mode 3)

- Course: `market-research`. Module 1 and `course-open.md`. Kit `kit/kit-m1-template/` and `kit/kit-m2/`.
- Verifier run: 2026-11-26. All checks in this report are dated 2026-11-26.
- Scope (role Mode 3): claims and statistics not already verified in the ledger, the use of cited ledger ids, and every screen name and feature on the step cards, build check cards, log save card, fast-start cards and kit rebuild card.
- Method: Claude Help Center pages loaded with curl (page metadata `dateModified` read). Other vendor pages loaded with WebFetch (curl is blocked for those hosts). 13 web calls in total.
- Files changed: this report. `research/platform-matrix.yaml` (8 rows appended, see section 5).

## 1. Result summary

| Area | Rows | Verified | Partly verified | Not verified | Wrong | Other |
| --- | --- | --- | --- | --- | --- | --- |
| Claims and statistics (section 2) | 27 | 17 | 7 | 1 | 1 | 1 not in scope (case data) |
| Step card screen names (section 3) | 38 | 20 | 5 | 11 | 0 | 1 risk (Claude), 1 date note (ChatGPT) |

The 11 "not verified" screen names: Claude 1 (delete a knowledge file), ChatGPT 1 (new chat in a project), Copilot 1 (new chat with the agent), Gemini 8 (no dated Google doc). The Gemini content matches the undated Help page. Only the date rule fails.

## 2. Claims and statistics

Ledger ids are confirmed against their ledger entry. S-B1 was opened again at the journal page.

| Id | Where | Claim | Result | Note |
| --- | --- | --- | --- | --- |
| C01 | O.2 slide | 122 interview and consultation transcripts. Quotes 68% word for word, 20% paraphrased, 3% cut short, 9% partly or fully made up (S-B1) | verified | JAMIA 33(11), published 2026-08-06. 122 = 61 clinical consultations + 61 reflexive interviews. 9% = 6% partial + 3% full hallucination. Primary, 2026 |
| C02 | O.2 talk | The interviews were with heart failure patients | verified | Video ethnography study of patients with heart failure |
| C03 | O.2 talk | "The AI found valid themes. They matched the human team well." | partly verified | All LLM themes were judged valid. Overlap is "moderate to substantial" (Jaccard 0.44 and 0.51). LLM themes were more conceptual. "Matched well" goes past the source. See failure F3 |
| C04 | O.2 talk | "The team checked every quote the AI gave back against the transcript" | partly verified | The first author manually verified all representative quotations. Selected quotes then went to the team. See failure F3 |
| C05 | O.2 talk | Human checks of each quote stayed essential. "Analytic partners rather than autonomous coders" | verified | Quote is word for word. Source: "Human oversight remained essential for ... quotation verification" |
| C06 | O.2 talk, O.8 | The team worked in a setup approved for HIPAA health data | verified | "HIPAA-compliant environment". ChatGPT Edu through the institution |
| C07 | O.3 talk, open Q2 | "Almost 1 in 3 quotes was not what the person said" | partly verified | 32% were not word for word. But the 3% "cut short" are the person's words, shortened. See failure F4 |
| C08 | O.1 talk | "Let me start with a study from this year" | wrong | The study is from 2026. The course runs in 2027. See failure F1 |
| C09 | O.7 talk | Copilot agents use knowledge files only with a Microsoft 365 Copilot license or pay-as-you-go billing | verified | mb-03 (checked 2026-11-20). Use is within the row |
| C10 | O.7 slide | Admins can turn off code execution and file creation, and sharing | verified | Claude: owners use Organization settings > Capabilities (files page, dateModified 2026-11-24). Sharing: projects page says "where enabled by administrators" (dateModified 2026-11-06) |
| C11 | 1.2 slide | 71% of 677 product people do not spend enough time with customers or on the market (Product Focus, 2026) | verified | N5 in `research/needs.md`, status verified. Not reopened. 83% Europe, fieldwork Oct 2025 to Jan 2026, published 2026. Instructor note 6 says so. Use is within N5 |
| C12 | 1.2 talk | "That takes days per study" | partly verified | Rests on E1 and E2. Both are Perspective AI (one vendor, so 1 source). The same talk track says vendor speed figures are not used. Gate 1 approved this bottleneck text, so not a failure. Softer wording advised (F6) |
| C13 | 1.2 talk | "It codes interviews much faster than you can" | partly verified | E10: 71% say AI lets them analyze "significantly faster" (self-report, vendor survey). E12, two lines later, says the chat workflow saved no time. The talk track contradicts itself. See failure F5 |
| C14 | 1.2 talk | Condens 2026: 71% of 332 research practitioners say checking AI output still takes significant time | verified | E10. Within the entry. Sample includes designers (15%) and PMs (9%). Condens is named as a vendor in the talk track |
| C15 | 1.2 talk | 2026 peer-reviewed study: two leading models applied more codes than a human and agreed with the human far less than two humans did. Chat workflow saved no time | verified, with a condition | E12. Figures are within the entry. But the corpus is 317 news articles about nurses, not interviews. The talk track puts it after "It codes interviews", so learners hear "interviews". See failure F5 |
| C16 | 1.8 talk | "Few enterprise teams do this today" (AI-moderated interviews) | not verified | No source. It is Dan's Gate 2 view (spec line 464). A factual claim needs 2 sources. See failure F2 |
| C17 | 1.8 talk | Urgency, pervasiveness and willingness to pay come from Pragmatic's way of judging a market problem | verified | Internal Pragmatic source: PDW-AI slides 8, 35, 36, 39 (`research/alignment-log.yaml`) |
| C18 | 1.12 to 1.14, section 6 | Case facts (I-104, P05, counts, case PM order) | not in scope | Fictional case data. Checked by the case builder, not against outside sources |
| C19 | 9, failures table | ChatGPT Free has 3 uploads per day | verified | cg-03 verifier note (2026-11-20) |
| C20 | Copilot card note | Copilot does not list `.md` as a knowledge file type | verified | mb-02 file type list (2026-11-20) |
| C21 | Copilot card note | Copilot keeps an output file for the session only | verified | mb-11 (2026-11-20) |
| C22 | Gemini card note | Canvas and Deep Research do not work in skills | partly verified | gm-06, undated page. The page the card cites (`?p=pn_skills`) does not list these tools. They are on answer 18560919. See failure F9 |
| C23 | Gemini cards, open O.4 | Skill names use lowercase and hyphens | partly verified | Confirmed on the undated skills Help page only |
| C24 | Gemini card, open | "Gems are now skills" | verified | gm-02. True for personal accounts now. Workspace business Gems stop no sooner than 2027-03-01, education 2027-06. Early 2027 Workspace learners may still see Gems |
| C25 | 8 | Copilot fallback texts are 6,973 and 7,139 characters, under the 8,000 limit | verified | `wc -m` run 2026-11-26. Limit from mb-01 |
| C26 | Q11 | ChatGPT Go and Plus have 25 files per project | verified | Projects page, loaded 2026-11-26. Conflict with cg-03 (20 on Plus) is still open. No lab impact |
| C27 | Q12, demo, card notes | Claude toggle **Code execution and file creation** is called **Create and edit files** in the updated Settings layout | verified | Files page, dateModified 2026-11-24. Path is **Settings** > **Capabilities** on Free, Pro, Max and Ultra |

## 3. Step card screen names and features

Rule: 1 dated vendor doc per screen name, checked within 30 days. All checks below are 2026-11-26.

Vendor docs used:

| Doc | URL | Date |
| --- | --- | --- |
| CL-A | https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects | dateModified 2026-11-06 ("Updated over 2 weeks ago") |
| CL-B | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude | dateModified 2026-11-24 ("Updated yesterday") |
| CL-C | https://support.claude.com/en/articles/9517075-what-are-projects | dateModified 2026-10-30 |
| CG-A | https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt | "Updated: 3 days ago" (relative only, approx 2026-11-23) |
| MS-A | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents | Last updated 2026-11-16 |
| MS-B | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge | Last updated 2026-11-16 |
| MS-C | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents | Last updated 2026-11-16 |
| MS-D | https://support.microsoft.com/en-US/Microsoft-365-Copilot/add-content-to-microsoft-365-copilot-chat-prompts | ms.date 2026-11-18 (metadata only, no date in the page body) |
| GM-A | https://support.google.com/gemini?p=pn_skills ("Create and manage skills for Gemini Apps") | No date. Fails the dated doc rule |
| GM-B | https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/ | 2026-09-30 |
| GM-C | Workspace Updates, 2026-09-30 (updated 2026-11-09) and 2026-11-16 posts | Dated, but they name no skill screen labels except "@mention" |

### Claude

| Screen name or feature | Used on | Doc | Result | Note |
| --- | --- | --- | --- | --- |
| **Projects** in the sidebar | build check 1 and 6, fast start, demo 1 | CL-A | verified | "Hover over the left side ... click Projects" |
| **+ New Project** | build check 1, demo 1 | CL-A | verified | Upper right corner |
| **Set project instructions** | build check 2, card 1, card 5, fast start, demo 2, kit README | CL-A | verified | |
| **Save instructions** | card header, fast start, demo 2, kit README | CL-A | verified | |
| **+** in project knowledge | build check 3, card 1, log save, fast start, demo 3 | CL-A | verified | Knowledge base is on the right side of the project page |
| New chat in the project | build check 4 and 6, card 2 and 6, fast start, demo 4 | CL-A | partly verified | "you can initiate chats with Claude within the project". No control name. Card wording is generic, so it passes |
| Delete a file from project knowledge | log save card | CL-A, CL-C | not verified | Neither page describes it. Gap. Card test must record the real control |
| **Settings** > **Capabilities** > **Code execution and file creation** (**Create and edit files**) | card note, demo, failures table, open O.7 | CL-B | verified | Free, Pro, Max, Ultra only. On Team and Enterprise an owner sets it in **Organization settings** > **Capabilities**. See F10 |
| **Customize** > **Skills** (stretch) | card stretch | cl-cl-03 | verified | Checked 2026-11-20, within 30 days |
| New version of projects (beta) | all Claude cards (risk) | CL-C | risk | Some Pro, Max and Ultra users have had existing projects moved to a new version: "a project is one conversation", files in a "Library". The card screen names may not match for them. See F8 |

### ChatGPT

| Screen name or feature | Used on | Doc | Result | Note |
| --- | --- | --- | --- | --- |
| **New project** in the sidebar | build check 1 | CG-A | verified | "Select New project in the sidebar" |
| **•••** > **Project settings** for instructions | build check 2, card 1 and 5, fast start, kit README | CG-A | verified | "Select the more options menu (•••), then select Project settings to add instructions" |
| Add files to the project | build check 3, card 1, log save | CG-A | partly verified | Function verified ("uploading PDFs, spreadsheets, docs, images, or by pasting text"). No button name. Card wording is generic, so it passes |
| Delete the old file | log save card | CG-A | partly verified | "open it from the project sources list to preview, download, or delete it". See F7 for wording |
| New chat in the project | build check 4 and 6, card 2 and 6, fast start | CG-A | not verified | Not stated on the page. Card wording is generic. Card test confirms |
| Doc date | card header | CG-A | passes, with a note | Relative date only ("3 days ago"). Same convention as the platform matrix. help-lb.openai.com is an OpenAI host. Cite help.openai.com in learner materials |

### Microsoft Copilot agent builder

| Screen name or feature | Used on | Doc | Result | Note |
| --- | --- | --- | --- | --- |
| **New agent** > **Skip to configure** | build check 1 | MS-A, MS-B | verified | |
| **Name** field | build check 1 | MS-A | verified | 30 characters. "Market Evidence Agent" is 21 |
| **Configure** tab | card 1, fast start, log save, kit README | MS-A | verified | |
| **Instructions** | build check 2, card 1 and 5, no-license box, fast start | MS-A | verified | 8,000 characters |
| **Knowledge** > **Upload** | build check 3, card 1, fast start, kit README | MS-B | verified | "In the Knowledge section ... Upload - Upload files directly from your device". Files show under **Uploaded files** |
| **X** next to the file > **Remove** | log save card | MS-B | verified | "choose the X next to the file, and choose Remove" |
| **Create** the first time | card header, kit README | MS-C | verified | |
| **Update** after each change | card header, log save, fast start | MS-C | verified | "choose Update in the top right corner". Changes save automatically but are not visible to users until **Update** |
| **All agents** > **...** > **Edit** | card header, fast start | MS-C | verified | **Edit** is the pencil icon in the **More** (**...**) menu. Recent agents also show **...** in the left pane |
| **All agents** to reopen | build check 6 | MS-C | verified | |
| Agent chat (run the agent) | build check 4, card 2 | MS-A | partly verified | MS-A names the **Try it** tab for testing in the builder. Chat with the created agent is not described. Card wording is generic |
| New chat with the agent | card 6 | none | not verified | Not stated in MS-A, MS-B or MS-C. Card test confirms |
| Send a file in the agent chat | card note, card 2 and 6 | MS-D | partly verified | Copilot Chat: **+** in the "Message Copilot" box, then **Upload images and files**. The page does not say this works in an agent chat, and lists no file types. G2-PF-02 stays open. The paste fallback on the card covers it |

### Gemini

GM-A has no date. By the rule, every Gemini screen name that rests only on GM-A does not pass. The content of GM-A matches the card except where F9 says.

| Screen name or feature | Used on | Doc | Result | Note |
| --- | --- | --- | --- | --- |
| **Customize** > **Skills** | build check 1, card header, fast start | GM-A | not verified (no date) | Content matches. "click Customize on the sidebar (or click More first if you don't see it)" |
| **Create** > **Create manually** | build check 1 | GM-A | not verified (no date) | Content matches |
| Skill name field, lowercase and hyphens | build check 1, card header, failures table | GM-A | not verified (no date) | Content matches. Field asks for the name; "must use all lowercase with words separated by a hyphen" |
| **Instructions** field | build check 2, card 1 and 5, fast start, kit README | GM-A | not verified (no date) | The page asks for "instructions for it to follow" but does not show the exact label |
| **Add** > files | build check 3, card 1, fast start, kit README | GM-A | not verified (no date) | The page has a third click: **Add**, then **files**, then **Upload**. The cards omit **Upload**. See F9 |
| **Create** first time, **Save** after changes | card header, fast start, log save | GM-A | not verified (no date) | Content matches |
| Open a skill to edit | card header, log save | GM-A | not verified (no date) | No **Edit** button. "Click the skill you want to edit" in **Customize** > **Skills**. Card wording matches |
| **More** > **Replace file** | log save card | GM-A | not verified (no date) | Page lists **More** > **Replace file** and **More** > **Replace skill**. The same page also says "To update files in a skill, you need to upload the entire skill ... again". The page conflicts with itself. The card covers both, which is correct |
| Type **/** and pick the skill | build check 4, card 2 and 6, card note, fast start | GM-B | verified | "typing a forward slash '/' and the skill's name directly in the prompt bar" (2026-09-30). GM-A adds: "or @, if you have the updated shortcut". See F9 |

Gap: Google has no dated doc that shows the skill screen labels. Checked GM-B and both GM-C posts. A gap is not a failure of research. But under the dated doc rule the Gemini card cannot pass until Dan decides (F11).

## 4. Failures and fixes

Do not edit module files from this report. The module builder makes these changes after Dan says yes.

| # | File and place | Problem | Fix |
| --- | --- | --- | --- |
| F1 | `course-open.md`, O.1 talk track | "a study from this year" is wrong when the course runs in 2027 | Say "a study from 2026" |
| F2 | `module.md`, 1.8 talk track | "Few enterprise teams do this today" has no source (Dan's Gate 2 view only) | Remove the sentence, or say "Your team may not use them." Do not state it as a market fact |
| F3 | `course-open.md`, O.2 talk track | "They matched the human team well" and "checked every quote the AI gave back" go past S-B1 | Say "The AI's themes were all judged valid, and they overlapped with the human team's themes." Say "The lead author checked each quote the AI picked against the transcript." |
| F4 | `course-open.md`, O.3 talk track and open Q2 | "not what the person said" counts cut-short quotes (3%), which are the person's words | Say "Almost 1 in 3 quotes was not word for word." Same fix for the hook line in Q2 |
| F5 | `module.md`, 1.2 talk track | "It codes interviews much faster than you can" conflicts with "The chat-based workflow saved no time" two lines later. The E12 study coded news articles, not interviews | Say "It can code interviews faster." Then "A 2026 peer-reviewed study, coding news articles about nurses, went further." |
| F6 | `module.md`, 1.2 talk track | "That takes days per study" rests on one vendor (E1 and E2, Perspective AI). Not a failure: Gate 1 approved the bottleneck text | Optional: say "That can take days per study." |
| F7 | `module.md`, section 6 log save card, ChatGPT row | Vendor wording is "project sources list" | Say "Open the old `problem-backlog` in the project sources list. Delete it. Add the new file." |
| F8 | `module.md`, Claude card and build check card | Claude is moving some Pro, Max and Ultra projects to a new version (beta). Screen names can differ for those learners | Add a card note: "If your project opens as one conversation with a Library, tell the instructor." Add it to the readiness checklist. Recheck CL-C before each delivery |
| F9 | `module.md` Gemini card, fast start, `course-open.md` Gemini card, kit README | (a) Card omits the **Upload** click after **Add** > files. (b) Some accounts use **@**, not **/**. (c) Canvas and Deep Research limit cites the wrong page | (a) "Add the files with **Add**, then **files**, then **Upload**." (b) "Type **/** (or **@**) and pick your skill." (c) Cite https://support.google.com/gemini/answer/18560919 (gm-06) for the Canvas note |
| F10 | `module.md`, Claude card note | **Settings** > **Capabilities** is for Free, Pro, Max and Ultra. On Team and Enterprise only an owner can change it | Add: "Team or Enterprise: ask your owner. It is in **Organization settings** > **Capabilities**." |
| F11 | `module.md`, Gemini card header | The only doc for 7 Gemini screen names has no date. The rule fails | Dan decides: accept GM-A with a check date (as gm-01 and gm-06 already do), or keep the Gemini card at "card test confirms". Record the decision |
| F12 | `module.md`, Claude log save row | No vendor doc shows how to delete a project knowledge file | Card test records the real control. Until then keep the generic wording |
| F13 | `module.md`, Copilot card note and card 6; ChatGPT card 2 and 6 | Upload in the agent chat (Copilot), and new chat (Copilot, ChatGPT) have no vendor doc | Card test confirms. G2-PF-02 and G2-PF-03 stay open. The paste fallback stays |

Dates to watch: every check above expires on 2026-12-26 (30-day rule). Recheck all card docs before each delivery.

## 5. Platform matrix changes

Appended 8 rows to `research/platform-matrix.yaml` under a new "Stage 3, module 1 verifier" block. No existing row was changed.

| New id | Feature | Status |
| --- | --- | --- |
| cl-ui-09 | Claude project screen names | verified |
| cl-ui-10 | Claude file creation toggle names and path | verified |
| cl-pj-11 | Claude new version of projects (beta) | not verified (new feature, PRD decision 25). Risk note |
| cg-ui-09 | ChatGPT project screen names | verified |
| mb-ui-12 | Copilot agent builder configure and knowledge screen names | verified |
| mb-ui-13 | Copilot open, edit, create and update an agent | verified |
| mb-ui-14 | Copilot Chat file upload (**+** > **Upload images and files**) | partly verified |
| gm-ui-10 | Gemini skill screen names | partly verified (undated page; only **/** dated) |

Note for Dan: `research/platform-matrix.yaml` has a Gate 1 fingerprint in `status.yaml`. The append changes the file hash. The role file tells the Verifier to add new features to this file in Mode 3. I did not change `status.yaml`. Please confirm the append, then recompute the fingerprint.

## 6. Sources opened in this run

- Claude: CL-A, CL-B, CL-C (curl, 2026-11-26).
- OpenAI: CG-A (WebFetch, 2026-11-26).
- Microsoft: MS-A, MS-B, MS-C, MS-D (WebFetch, 2026-11-26).
- Google: GM-A, GM-B, Workspace Updates 2026-09-30 and 2026-11-16 (WebFetch, 2026-11-26).
- S-B1: Bang S.H. et al., JAMIA 33(11):2079 to 2091, https://academic.oup.com/jamia/article/33/11/2079/8753705 (WebFetch, 2026-11-26).
