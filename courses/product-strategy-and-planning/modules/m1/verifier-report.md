# Verifier report: module 1 and course open (Mode 3)

- Course: `product-strategy-and-planning`. Files checked: `modules/m1/module.md`, `modules/m1/course-open.md`, `modules/m1/kit/` (READMEs and character counts).
- Verifier run: 2026-11-27. All checks in this report are dated 2026-11-27.
- Scope (role Mode 3): claims and statistics not already verified at Gate 1, and every screen name and feature on the step cards, build check cards, fast-start cards, log save card and kit rebuild card.
- Method: Claude Help Center pages loaded with curl (page metadata `dateModified` read). Other pages loaded with WebFetch (curl is blocked for those hosts). 12 WebFetch calls, 4 curl page loads, 2 web searches.
- Files changed: this report. `research/platform-matrix.yaml`: 12 rows added (7 copied from Market Research and rechecked, 1 carried row now verified, 4 new), and a `recheck_2026_11_27` field on cl-cl-03, cg-14, mb-04 and mb-11. No module file changed.

## 1. Result summary

| Area | Rows | Verified | Partly verified | Not verified | Wrong | Not in scope |
| --- | --- | --- | --- | --- | --- | --- |
| Claims and statistics (section 2) | 29 | 19 | 6 | 1 | 1 | 2 |
| Screen names and features (section 3) | 45 | 28 | 14 | 2 | 1 | 0 |

Card check dates: every card says 2026-11-26. That is 1 day old. Pass (30-day rule).

Must-fix: 3 items (section 4). Should-fix: 11. Dan decides: 2.

## 2. Claims and statistics

| Id | Where | Claim | Result | Note |
| --- | --- | --- | --- | --- |
| C01 | 1.2 talk | N21: "72.2% of nearly 250 product professionals said they spend 25% or less of their time on product strategy". Fieldwork Q4 2025. A tool vendor sponsored it | verified | Primary PDF reopened. p. 39: question "What percentage of your time is spent determining product strategy?", "72.2% spending 25% or less on this activity". p. 6: "In Q4 2025, we surveyed nearly 250 product professionals". p. 6 also calls it "ProductPlan's eleventh annual" report, so "a tool vendor sponsored" is fair. Dan accepted N21 with "fieldwork Q4 2025" (Gate 1 decision i). N21 is only in `research/rerun-track-3.md`, not in `evidence-ledger.yaml` (F11) |
| C02 | O.2 slide, talk | Romasanta, Thomas and Levina, Harvard Business Review, March 2026 | verified | hbr.org page, 2026-03-16 |
| C03 | O.2 talk | Researchers at Esade, the University of Sydney and NYU Stern | verified | HBR author bios: Esade Business School; University of Sydney Business School; NYU Stern |
| C04 | O.2 talk | Models included ChatGPT, Gemini and Claude | verified | Fortune (2026-04-10): 7 models, including GPT-5, Claude, Gemini, Grok. E3 lists ChatGPT and GPT-5 API |
| C05 | O.2 talk | Trade-offs: long term or short term; automate or augment; differentiation or cost | partly verified | Fortune confirms the first 2. "Compete on being different, or on cost" is only in the third-party HBR snapshot (E3, zby.github.io). HBR body is paywalled (F3) |
| C06 | O.2 slide line 1, talk | "Across many company scenarios" | partly verified | NYU Stern: "regardless of context", "thousands of simulations". Fortune: about 15,000 simulations "built around workplace tensions". No source says the scenarios were company types (F2) |
| C07 | O.2 slide line 2, talk | Models almost always picked the same trendy option, whatever the context | verified | NYU Stern: "almost uniformly select the same trendy strategies, regardless of context". HBR summary: "consistently recommend strategies that align with modern managerial buzzwords and trends". "Whatever the company" goes slightly past (F2) |
| C08 | O.2 talk | "The advice sounded tailored. It was not." | partly verified | Fortune quotes the researchers: "An LLM can sound highly tailored to your situation". One report of the authors' words. Not on the readable HBR or NYU pages |
| C09 | O.2 slide line 3 | The authors' name for it: trendslop | verified | HBR summary and NYU Stern |
| C10 | O.2 talk | Advice: use AI to widen options, not to make the choice | verified | HBR summary: "use it to expand options, not make choices". Fortune: keep the decision human |
| C11 | O.2, open summary | No HBR number on a slide or in the talk track | verified | O.2 slide and talk track hold no percentage or run count. The "DO NOT QUOTE" cue is present. Matches OI-10 and module question 2 |
| C12 | O.1 talk | "It starts with a study from 2026" | verified | HBR 2026-03-16. Wording is safe for a 2027 class |
| C13 | 1.8 talk | "A model will happily tell you what to fund. Its answer will sound tailored." | partly verified | The study tested strategy trade-offs, not funding choices. "Sound tailored" is from Fortune. The funding part goes past the source (F4) |
| C14 | O.7 slide, talk | "Can you create an agent or a skill? On Copilot that needs a Microsoft 365 Copilot license or pay-as-you-go billing" | wrong | mb-03 (verified 2026-11-20): instructions, code interpreter and web search work in all 3 license states. Embedded knowledge files need a license or billing. The module's own no-license path builds an agent with no license. See M1 |
| C15 | O.8 talk | "A one-off prompt forgets your data when you close the chat." | not verified | No source. ChatGPT default memory lets a project use other chats (cg-14, cg-ui-15). Claude projects have memory ("Use account memory", projects page 2026-11-06). Chats also stay in history. The line understates data retention in a data safety slide. See M2 |
| C16 | 1.2 talk | Vendors describe the stale pack, "human integration layer". Leaders say strategy is clear, few show the link | verified | W22 and W1 (verified at Gate 1, two independent vendors). Words only, no W1 or W3 figure. Use is within the rows |
| C17 | 1.4 talk | Hardware shares firmware teams, test labs, suppliers; stage gates of months against weeks | verified | W19, W22 (Gate 1). Within the rows |
| C18 | Copilot card, section 9 | Copilot does not take `.md` or CSV as knowledge | verified | Add knowledge page (2026-11-16): table lists .doc, .docx, .pdf, .ppt, .pptx, .txt, .xls, .xlsx. No .md, no .csv |
| C19 | Copilot card, section 9 | Copilot keeps output files for the session only | verified | Code interpreter page (2026-11-16): "available for download during the active session only" |
| C20 | Gemini card | Canvas and Deep Research do not work in skills | partly verified | gm-06, undated page, not reopened (budget). Same as Market Research |
| C21 | Gemini cards | "Gems are now skills" | verified | gm-02. Workspace business Gems stop no sooner than 2027-03-01, so some 2027 learners may still see Gems |
| C22 | ChatGPT cards | ChatGPT Work does not run in a project with project-only memory | verified | Projects page today: "ChatGPT Work is not available in the project" |
| C23 | Claude card note | Claude is moving some projects to a new version with a Library | verified | "What are projects?" (dateModified 2026-10-30): beta, one conversation, Library, moving existing projects for some Pro, Max and Ultra users. Row cl-pj-11 now verified |
| C24 | Claude stretch | Custom skills on all plans, code execution on | verified | Skills page dateModified 2026-10-30. Card says "approx 2026-10-28" (F7) |
| C25 | Section 8 | Character counts and the 8,000 limit | verified | Python `len` run 2026-11-27: 2,164; 1,365; 2,770; 6,673; 2,469; 6,997; 1,705 all match. 8,000 on Build agents page (2026-11-16) |
| C26 | B3 | Reading knowledge files with code interpreter is not documented | verified | Still not on the code interpreter page (2026-11-16) |
| C27 | Q9 | gm-01 does not name `.xlsx` | partly verified | Out of date. The skills page lists ".csv, .ods, .xlsx" under "Spreadsheets & data tables". Not supported: ".doc, .xls, .ppt". Page undated (gm-14). See F8 |
| C28 | 1.3 talk | Capability Standards wording | not in scope | Pragmatic internal source, from the approved spec |
| C29 | 1.6, 1.12 to 1.14, section 6 | Case figures | not in scope | Fictional case data |

## 3. Screen names and features

Rule: 1 dated vendor doc per screen name, checked within 30 days.

Vendor docs used:

| Doc | URL | Date |
| --- | --- | --- |
| CL-A | https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects | dateModified 2026-11-06 |
| CL-B | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude | dateModified 2026-11-24 |
| CL-C | https://support.claude.com/en/articles/12512198-how-to-create-custom-skills | dateModified 2026-10-30 |
| CL-D | https://support.claude.com/en/articles/9517075-what-are-projects | dateModified 2026-10-30 |
| CG-A | https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt | approx 2026-11-27 ("Updated: 35 minutes ago") |
| MB-A | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents | 2026-11-16 |
| MB-B | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge | 2026-11-16 |
| MB-C | https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents | 2026-11-16 |
| MB-D | https://learn.microsoft.com/microsoft-365-copilot/extensibility/code-interpreter | 2026-11-16 |
| MB-E | https://support.microsoft.com/en-au/topic/add-content-and-agents-to-copilot-chat-438173cf-2a2b-47e0-a1e0-82d830922fe5 | ms.date 2026-11-18 |
| GM-A | https://support.google.com/gemini?p=pn_skills | no date on page |
| GM-B | https://workspaceupdates.googleblog.com/2026/10/an-easier-way-to-customize-how-gemini-works-for-you.html | 2026-10-21 |
| GM-C | blog.google, "Let skills in Gemini tackle your most repetitive tasks" (carried, checked 2026-11-26) | 2026-09-30 |

| Id | Platform | Name or feature on the card | Result | Doc | Matrix row | Note |
| --- | --- | --- | --- | --- | --- | --- |
| S01 | Claude | **Projects** | verified | CL-A | cl-ui-09 | "click 'Projects'" |
| S02 | Claude | **+ New Project** | verified | CL-A | cl-ui-09 | Quoted |
| S03 | Claude | **Set project instructions** | verified | CL-A | cl-ui-09 | Quoted |
| S04 | Claude | **Save instructions** | verified | CL-A | cl-ui-09 | Quoted |
| S05 | Claude | **+** in project knowledge | verified | CL-A | cl-ui-09 | "Click on the '+' button to add content to the project" |
| S06 | Claude | New chat in the project | partly verified | CL-A | cl-ui-09 | Described, no control name. Plain words on the card. OK |
| S07 | Claude | **Settings**, **Capabilities**, **Code execution and file creation** (**Create and edit files**) | verified | CL-B | cl-ui-10 | Both names and path quoted |
| S08 | Claude | **Organization settings**, **Capabilities** | verified | CL-B | cl-ui-10 | Quoted for Team and Enterprise owners |
| S09 | Claude | **Customize**, **Skills** (stretch) | verified | CL-C | cl-cl-03 | "Go to Customize > Skills" |
| S10 | Claude | Delete a file from project knowledge (log save) | not verified | none | cl-ui-09 | Not on CL-A. Plain words on the card (D2) |
| S11 | ChatGPT | **New project** in the sidebar | verified | CG-A | cg-ui-09 | "select the plus icon (+) for New project", then "Create project" |
| S12 | ChatGPT | **•••**, then **Project settings** (instructions) | verified | CG-A | cg-ui-09 | Quoted. The field is "Instructions" |
| S13 | ChatGPT | Add files to the project's files | verified | CG-A | cg-ui-09 | Upload or paste. No button name. Plain words. OK |
| S14 | ChatGPT | Project sources list, delete (log save) | verified | CG-A | cg-ui-09 | "open it from the project sources list to preview, download, or delete it" |
| S15 | ChatGPT | Project memory "default, not project-only" | verified | CG-A | cg-ui-15 | Labels are "Default memory" and "Project-only memory". Can change later in Project settings, but "Changes may take a few hours" (F5) |
| S16 | ChatGPT | New chat in a project | not verified | none | cg-ui-09 | No control named. Plain words (D2) |
| S17 | ChatGPT | ChatGPT Work for a sheet file | partly verified | CG-A, cg-09, cg-10 | cg-14 | Plan and memory rules verified. How Work starts in a project chat is not documented. Card test |
| S18 | ChatGPT | New chat outside the project, paste brief, attach 3 files (pass condition) | partly verified | CG-A | cg-01 | Generic chat actions. No label used. OK |
| S19 | Copilot | **New agent** | verified | MB-A | mb-ui-12 | Quoted |
| S20 | Copilot | **Skip to configure** | verified | MB-A | mb-ui-12 | Quoted |
| S21 | Copilot | **Configure** tab | verified | MB-A, MB-B | mb-ui-12 | Quoted |
| S22 | Copilot | **Name** | verified | MB-A | mb-ui-12 | Fields table |
| S23 | Copilot | **Instructions** | verified | MB-A | mb-ui-12 | Fields table, 8,000 characters |
| S24 | Copilot | **Knowledge** | verified | MB-A, MB-B | mb-ui-12 | Quoted |
| S25 | Copilot | **Upload** | verified | MB-B | mb-ui-12 | "Upload - Upload files directly from your device" |
| S26 | Copilot | **X**, then **Remove** (log save) | verified | MB-B | mb-ui-12 | "choose the X next to the file, and choose Remove" |
| S27 | Copilot | **All agents**, **...**, **Edit** | verified | MB-C | mb-ui-13 | Quoted. Edit is the pencil icon |
| S28 | Copilot | **Create** (first time) | verified | MB-C | mb-ui-13 | Quoted. Position not stated |
| S29 | Copilot | **Update** (after each change) | verified | MB-C | mb-ui-13 | "choose Update in the top right corner" |
| S30 | Copilot | **Create documents, charts, and code** is on | partly verified | MB-A, MB-D | mb-ui-15 | Label verified on MB-A (Capabilities, "select the toggle"). MB-D, same date: "always enabled in Agent Builder". MB-A also says capabilities come "automatically". Conflict not resolved (F1) |
| S31 | Copilot | Upload the run files and `capacity-sheet.xlsx` in the agent chat (steps 2, 6, pass condition, no-license path) | partly verified | MB-D, MB-E | mb-ui-14 | MB-E covers Copilot Chat only. MB-D says "Users can also upload data files" (Excel and CSV named) with no control name and no agent chat steps. Core step depends on it. Card test (G2-PF-02). Paste fallback does not work for `.xlsx` (F10) |
| S32 | Copilot | New chat with the agent (step 6) | partly verified | MB-A | mb-ui-12 | MB-A names **New chat** only in the Try it tab. Plain words on the card. OK |
| S33 | Copilot | `.txt` and `.xlsx` as knowledge, not `.md` or CSV | verified | MB-B | mb-ui-12 | File type table |
| S34 | Gemini | **Customize** | verified | GM-B | gm-ui-11 | First dated Google doc for this label. GM-A adds: "If you don't see Customize, click More first" (F6) |
| S35 | Gemini | **Skills** | verified | GM-B | gm-ui-11 | Section of the Customize hub |
| S36 | Gemini | **Create**, then **Create manually** | partly verified | GM-A | gm-ui-10 | Matches. Undated page (D1) |
| S37 | Gemini | **Add** | partly verified | GM-A | gm-ui-10 | Matches. Undated (D1) |
| S38 | Gemini | **files** | wrong | GM-A | gm-ui-10 | The page says "click images or files". See M3 |
| S39 | Gemini | **Upload** | partly verified | GM-A | gm-ui-10 | Matches. Undated (D1) |
| S40 | Gemini | **Create** the first time, **Save** after each change | partly verified | GM-A | gm-ui-10 | Matches. Undated (D1) |
| S41 | Gemini | **/** in chat | verified | GM-A, GM-C | gm-ui-10 | Dated by GM-C (2026-09-30). GM-A also names **@** for "the updated shortcut" |
| S42 | Gemini | **More**, then **Replace file** (log save) | partly verified | GM-A | gm-ui-10 | Matches. Same page also says to re-upload the whole skill to update files. Card keeps both paths. Undated (D1) |
| S43 | Gemini | The skill instructions field | partly verified | GM-A | gm-ui-10 | Page refers to the "Instructions" field. Undated. Plain words on the card. OK |
| S44 | Gemini | `capacity-sheet.xlsx` in a skill | partly verified | GM-A | gm-14 | `.xlsx` listed as supported. Undated. CSV backup on the card is also supported |
| S45 | Gemini | Skill name in lowercase with hyphens | partly verified | GM-A | gm-ui-10 | Quoted. Undated |

## 4. Must-fix list

| # | Where | Problem | Fix |
| --- | --- | --- | --- |
| M1 | `course-open.md` O.7 slide ("Agent or skill creation allowed (Copilot: license or billing)?") and O.7 talk track | Wrong (C14). A Copilot license or billing is needed for knowledge files, not to create an agent (mb-03). The open's own no-license path builds an agent | Slide: "Agent or skill creation allowed? Copilot knowledge files: license or billing?" Talk: "On Copilot, the agent reads knowledge files only with a Microsoft 365 Copilot license or pay-as-you-go billing." |
| M2 | `course-open.md` O.8 talk track | Not verified (C15). "A one-off prompt forgets your data when you close the chat" is not true with memory and chat history. It understates retention on the data safety slide | Replace with: "An agent keeps files in its knowledge and uses them on every run." Delete the sentence about the one-off prompt |
| M3 | `module.md` Gemini card step 1 and fast-start row; `course-open.md` Gemini build check step 3; `kit/kit-m1-template/README.md` line 34 | Wrong label (S38). The Gemini page says **images or files**, not **files** | Change "**Add**, **files**, **Upload**" to "**Add**, **images or files**, **Upload**" in all 4 places |

## 5. Should-fix list

| # | Where | Item |
| --- | --- | --- |
| F1 | Copilot card notes, section 1 table | Two Microsoft pages of the same date disagree on the toggle (mb-ui-15). Write: "If you see **Create documents, charts, and code**, check that it is on." The card test records what the screen shows (G2-PF-03) |
| F2 | O.2 slide line 1 and talk track | "Many company scenarios" and "Whatever the company" go past the sources. Use "many scenarios" and "whatever the context" |
| F3 | O.2 talk track | "Compete on being different, or on cost" rests only on a third-party copy of the HBR text. Keep the 2 trade-offs Fortune confirms, or Dan accepts E3 as is |
| F4 | 1.8 talk track | The study tested strategy trade-offs, not funding. Suggest: "A model will happily pick a strategy for you. Its answer will sound tailored." |
| F5 | ChatGPT cards, build check, section 9 | Use the vendor label **Default memory**. Add an instructor note: a memory change "may take a few hours", so fix it at the build check, not in the lab |
| F6 | Gemini cards | Add: "No **Customize**? Select **More** first." (GM-A) |
| F7 | Claude and ChatGPT card headers | Skills page date is dateModified 2026-10-30, not approx 2026-10-28. ChatGPT projects page now says "Updated: 35 minutes ago" (approx 2026-11-27). Labels did not change |
| F8 | Module question 9 | The skills page now lists `.xlsx` as supported (gm-14, undated). The question can close to "A, confirm in the card test" |
| F9 | Section 9 failures table | No recovery row for a Claude learner whose project is the new version (cl-pj-11). "New chat in the project" does not fit one conversation. Add a row (for example, run each quarter as a new message in the project and say "Use only the Q4 files") or pair the learner |
| F10 | Copilot card notes, kit README | "If a chat upload fails, paste the text" does not work for `capacity-sheet.xlsx`. Add: "Paste the text of `capacity-sheet.csv`." |
| F11 | `research/evidence-ledger.yaml` | N21 is verified in `rerun-track-3.md` but has no ledger row. Add it at the next ledger update so Mode 2 trace finds it |

## 6. Dan decides

| # | Item | Recommendation |
| --- | --- | --- |
| D1 | Gemini labels from an undated page: **Create**, **Create manually**, **Add**, **images or files**, **Upload**, **Save**, **More**, **Replace file**, name rule, `.xlsx` support. **Customize**, **Skills** and **/** now have dated docs | Accept with the 2026-11-27 check date, as in Market Research D3. The card test confirms |
| D2 | Plain-word steps with no vendor doc: Claude delete a knowledge file; ChatGPT new chat in a project | Keep as plain words. The card test confirms |

## 7. Card test items from this check

1. Copilot: `.xlsx` upload in the agent chat works, and code interpreter totals it (S31, G2-PF-02).
2. Copilot: the toggle shows, or code interpreter is always on (S30, G2-PF-03).
3. ChatGPT: ChatGPT Work makes the sheet file in a default-memory project chat (S17).
4. Gemini: **More**, **Replace file** works, or a whole-skill upload is needed (S42).
5. Gemini: `capacity-sheet.xlsx` adds to the skill (S44).

## 8. Gaps

- No dated Google doc names the Gemini create, add, upload, save or replace labels. Searched Workspace Updates (2026-09-30, 2026-10-21, 2026-11-16) and blog.google. Gap, not a failure.
- No Microsoft doc gives steps to upload a file in a chat with an Agent Builder agent.

## 9. Sources opened

- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects
- https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://support.claude.com/en/articles/9517075-what-are-projects
- https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-build-agents
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-add-knowledge
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents
- https://learn.microsoft.com/microsoft-365-copilot/extensibility/code-interpreter
- https://support.microsoft.com/en-au/topic/add-content-and-agents-to-copilot-chat-438173cf-2a2b-47e0-a1e0-82d830922fe5
- https://support.google.com/gemini?p=pn_skills
- https://workspaceupdates.googleblog.com/2026/10/an-easier-way-to-customize-how-gemini-works-for-you.html
- https://3434168.fs1.hubspotusercontent-na1.net/hubfs/3434168/SPM26/State%20of%20Product%20Management%202026_Final.pdf
- https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return
- https://www.stern.nyu.edu/experience-stern/faculty-research/research-highlights/researchers-asked-llms-strategic-advice-they-got-trendslop-return
- https://finance.yahoo.com/economy/policy/articles/meet-trendslop-ai-fueled-scourge-214741487.html
