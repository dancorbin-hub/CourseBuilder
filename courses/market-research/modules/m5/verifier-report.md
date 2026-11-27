# Verifier report: module 5 and the course close (module mode)

Course: `market-research`. Module 5, the stakeholder answer job, and section 10, the course close. Checked 2026-11-27 by the research verifier (Stage 3, step 2b).

Files checked: `modules/m5/module.md` (sections 1 to 10), `modules/m5/kit/` (`lab-5/`, `kit-final/`, `kit-m5-draft/`, `kit-m5-expected.md`), `modules/m5/card-test.md`.

## How I checked

1. I checked only claims and features that are new since Gate 1, or that the module 2 and 3 verifiers did not check on 2026-11-27. Focus from the task: the share stretch steps on all 4 cards, what a shared agent exposes, and the slide and talk track claims.
2. Core card screen names (Claude, ChatGPT, Copilot, Gemini) are the same as the module 2 and 3 cards. The module 2 verifier reopened those docs on 2026-11-27. I did not check them again, except the Gemini **Add files** label and the Claude projects page, which I reopened for the share steps.
3. I opened the Claude pages by curl and read the page metadata. I opened the OpenAI, Microsoft, Google and source pages by WebFetch (the proxy blocks curl to them).
4. A check date older than 30 days fails. Every doc a module 5 card uses was checked on 2026-11-26 or 2026-11-27. No date fails.
5. I did not edit `platform-matrix.yaml` or `evidence-ledger.yaml`. Both are fingerprinted. Proposed updates are in the last section.

## Results: claims (slides, talk track, kit)

| Id | Claim (where) | Result | Note |
| --- | --- | --- | --- |
| C1 | "Past research is hard to find and reuse" (5.2 on-slide line; W13, W20) | verified | W13 (NN/g, Maria Rosala, 2024-07-26): "it's not only hard for stakeholders to find old research"; "aren't looking there for past research". W20 (UserTesting, 2026-07-08): "it had forgotten where the answer lived". 2 independent sources. W13 age flag kept by Dan |
| C2 | "Nielsen Norman Group ... says research repositories fail. Adding to them is too much work, and people cannot find past insights" (5.2 talk track) | verified | W13 title "Why Research Repositories Fail"; heading "It's too much work to contribute". "That article is from 2024, so we use it as a claim only" is correct |
| C3 | "UserTesting ... wrote in 2026 that people do not remember study names" (5.2 talk track; also section 1 row 1, B14) | partly verified | W20: "Product managers don't remember the names of studies." The source names product managers, not people in general or stakeholders. See F6 |
| C4 | "Teams commission new studies on questions already answered" (5.2 talk track) | verified (1 source, attributed) | W20: "Two weeks later, the team commissions another study." It is an anecdote. The talk track says "That is a vendor's experience, not a study", which is correct. W20 cites conversations with research leaders, no data |
| C5 | "Or someone answers from memory, and the answer goes further than the evidence" (5.2 talk track) | not verified | Not in W13 or W20. It reads as a finding. See F7 |
| C6 | Case claims on 5.6, 5.13, 5.15, 5.16 and in section 6 (record ids, counts, dates) | pass (case data) | From `case/`, not external. Not a verifier check. "About 26 months old" (2025-09-12 to November 2027) is correct |
| C7 | C.1 recap table: the check that passed and what found it, labs 1 to 5 | pass | Matches the summary table in `case/planted-errors.md` |
| C8 | C.1 title "Five audits, five rules" and talk track "Your brief now has six of them" | pass, note | Both are true (rule 5 is a hand-off rule, not an audit rule), but a learner can read them as a conflict. See F11 |
| C9 | Kit character counts (section 8, READMEs) | verified | `wc -m` today: job card 1,398, past reports 2,773, fallback m5 5,293, brief v6 4,008, fallback v6 5,813, fix rules 1,155, Monday plan 2,046, record sheet 2,239. Every `.txt` copy in `lab-5/` and `kit-final/` matches its `.md` (`cmp`) |
| C10 | `lab-5/README.md`, no-license step 5: "send messages 2 and 3 again" | wrong (kit text) | Card and section 8 say messages 1 and 2 (backlog, then logs and past reports). Message 3 is the questions file. See F5 |

## Results: share stretch screen names and features

### Claude (cl-pj-02)

Doc: Claude Help Center, "How can I create and manage projects?" (9519177). Page metadata dateModified 2026-11-06T18:06:37Z. Page shows "Updated over 3 weeks ago". Opened 2026-11-27.

| Card step | Screen name or feature | Result | Note |
| --- | --- | --- | --- |
| Header | Team or Enterprise plan only | verified | "If you're on a Team or Enterprise plan, you can share projects with other users in your organization" |
| Header | Share section "Updated over 2 weeks ago" | wrong | Page shows "Updated over 3 weeks ago". See F9 |
| 2 | A **Can view** member sees the instructions and all knowledge files | verified | "Can view: Members can see project contents, knowledge, and instructions, and chat within the project, but cannot edit it." |
| 3 | Open the project. **Share project** | verified | "Open the project you want to share. Click the "Share project" button to the right of the project name." |
| 4 | Name or email, **Can view**, **Share** | verified | "Add individual members using their name or email address ... Click "Share" to send invitations." Step has 3 actions. See F3 |
| 6 | Sharing menu, their role, **Remove access** | verified | "The project creator can click on the member's current role and select "Remove access."" The doc does not say how to open "the sharing menu". Card test row covers it |
| After 6 | Admin can turn sharing off | verified | "unless your admin has turned off project sharing" |
| Not on card | Project memory in a shared project | gap | "Each project has its own memory" (9519177; and 11817273, dateModified 2026-11-24). No doc says if a Can view member's chats use project memory made from the owner's chats. See F2 |
| Not on card | Can a Can view member see the owner's chats? | gap | "project contents" is not defined. Card test row already asks it |

### ChatGPT (cg-02)

Doc: OpenAI Help Center, "Projects in ChatGPT" (10169521). Page shows "Updated: 3 days ago" (relative date only). Opened 2026-11-27.

| Card step | Screen name or feature | Result | Note |
| --- | --- | --- | --- |
| Header | Plan | verified | "Project sharing is available on ChatGPT Free, Go, Plus, Pro, Business, Enterprise, and Edu". The card's Go or Plus minimum (from the core lab) covers it |
| 2 | Members see all chats and files, and can download the files | verified, one item missing | "Project members can view the project's chats, files, and member list." "All members of a project can view and download files added to the project." "Chat access lets members see and interact with the project's chats, files, and instructions". The card does not say instructions. See F4 |
| 3 | Open the project. **Share** | verified | "Select Share to open the sharing pane." |
| 4 | Invite one colleague, chat access | verified, one choice missing | "Enter a name, email address, or group, then choose chat or edit access." The pane also has "Only those invited" or "Anyone with a link". The card does not name it. No send button is named on the page. 2 actions in one step. See F3 and F4 |
| After 5 | Only the owner can remove a member | partly verified | "Project owners can remove members individually." "Editors can add members, but not remove them." Also: "Workspace owners may also remove collaborators from a project at any time." Fine for a learner. No change needed |
| After 5 | Workspace settings can limit sharing | verified | "Workspace owners can control project sharing"; "sharing can be turned off entirely from workspace settings" (Enterprise); invitations "may be limited to members of your workspace" |

### Copilot agent builder (mb-05)

Doc: Microsoft Learn, "Share and manage agents" (agent-builder-share-manage-agents). "Last updated on 2026-11-16". Opened 2026-11-27.

| Card step | Screen name or feature | Result | Note |
| --- | --- | --- | --- |
| Header | Microsoft 365 Copilot license only | verified, conservative | The page gives a recipient rule only: "Users can only add agents that are shared with them when they have the type of Microsoft 365 Copilot license required for accessing the capabilities configured in that agent." The card line is safe. Pay-as-you-go billing is not named. No change needed |
| 2 | Anyone who can use the agent gets answers from all its files | verified | "Files uploaded from a device become embedded knowledge. Anyone who can access the agent can receive responses grounded in that content ... Review uploaded content before sharing the agent." |
| 3 | **Share** | verified | "Open the agent you want to share and select Share." Position on screen not stated |
| 4 | **Add a name, group, or email**, **Can chat**, **Add** | verified, one field missing | Exact labels found. "Can chat ... can only interact with the agent." The **Add people** panel also has a **Send notification** checkbox, on by default. The card does not name it. 3 actions in one step. See F3 |
| After 5 | License that the agent's features require | verified | Same quote as the header row |
| After 5 | Never choose **Can edit** for a stakeholder | verified | "Can edit ... Owner ... full rights to edit, share, and manage the agent." |
| Not on card | Stop sharing | verified, missing on card | "Select the role dropdown next to the user. Choose a new option: ... Remove - revoke the user's access. Changes take effect immediately." The Claude card has a stop step. Copilot has none. See F8 |
| Not on card | Can chat users see the instructions or files? | gap | The page does not say. It says only that they get answers grounded in the files. See F1 |

### Gemini (gm-04)

Docs: Google Workspace Updates post, "Share skills and add files from Google Drive, Gemini Notebook and Google Photos to your skills in the Gemini app" (2026-11-16). Gemini Apps Help, skills page (pn_skills, no date on the page; module 1 D3 accepts it with a check date). Both opened 2026-11-27.

| Card line | Feature | Result | Note |
| --- | --- | --- | --- |
| "Google's post names no screen labels for it" | Share labels | true for the post, but the Help page has them | Post: share "from the "Skills" page ... with View or Edit permissions", web only. Help page: **Customize**, **Skills**, hover the skill, **More**, **Share skill** ("This creates a copy of the skill in Google Drive"), enter email, **Viewer** or **Editor**, **Send**. Remove: the access level, **Remove access**, **Save**. See F10 |
| "A shared skill needs its Drive files shared too" | Files | verified | Post: "If a skill includes Drive files, you'll also need to share access to those files." Help: "If your skill includes files, you'll also need to share access to those files." |
| Not on card | What a Viewer sees | verified (undated page) | Help: Viewers "View the skill's description, instructions, and uploaded files." |
| Not on card | Limits | verified | Post: "on by default ... can be disabled in the Admin console"; follows Drive sharing settings; web only; rollout started 2026-11-12, up to 15 days. Help: "skills with a notebook attached can't be shared"; only the owner and Editors can share; recipients get the skill as inactive and select **Add skill** |
| Core step 1 | **Add files** on an existing skill | verified (undated page) | "To add a file, click Add files." Same as module 2 F7 |

## Findings and fixes

Most important first. "Fail" means the builder must fix it or Dan must accept it.

| # | Severity | Where | Finding | Fix |
| --- | --- | --- | --- | --- |
| F1 | Fail (wording past source) | Record sheet section 7 ("A shared agent shows its files"); D6 ("A shared agent shows all its files") | True for Claude (Can view), ChatGPT (chat access) and Gemini (Viewer). Not stated for Copilot: Microsoft says only that Can chat users get answers grounded in the files. The Copilot card step 2 has the correct words | Record sheet: "Which files may they see? (A shared agent can show its files, or answer from all of them)". D6: "A shared agent shows all its files (Copilot: answers from all its files; ChatGPT also shows all project chats)" |
| F2 | Open, card test | Claude card stretch step 2; card test Claude share table | Each Claude project has its own memory. No doc says if a Can view member's chats use project memory built from the owner's chats. That memory can hold own-work details. The step 2 "stop here" check names only instructions and knowledge files | Add to step 2: "Project memory may also carry what you said in this project." Add a card test row: "Does a Can view member's chat use project memory from the owner's chats? (doc does not say)". Until the test answers it, keep the stretch after class only |
| F3 | Fail (house rule 8) | Claude stretch step 4 (3 actions) and step 6 (2 actions); ChatGPT stretch step 4 (2 actions); Copilot stretch step 4 (3 actions) | One action per step. Each stretch step 1 repeats the "Share plan" bullet above it ("Fill in section 7"), so a slot is free on each card | Delete stretch step 1 on each card (the share plan bullet covers it). Claude: "4. Add one colleague by name or email. 5. Choose **Can view**, then select **Share**." Copilot: "3. Enter your colleague in **Add a name, group, or email**. 4. Choose **Can chat**, then select **Add**." ChatGPT: "3. Enter your colleague's name or email. 4. Choose chat access." Dan decides if "choose, then select" counts as one action |
| F4 | Minor (missing fact and choice) | ChatGPT stretch steps 2 and 4 | Chat access members also see the instructions. The sharing pane offers "Anyone with a link". A learner who picks it shares the agent with anyone who has the link | Step 2: "Members see all chats, files and instructions in the project, and can download the files." Step 4 (or a note): "Keep **Only those invited**." Add a card test row for the label |
| F5 | Fail (kit text wrong) | `lab-5/README.md`, "Copilot with no license or billing", step 5 | "send messages 2 and 3 again" conflicts with the card ("send the same 2 messages first") and section 8 (messages 1 and 2). A learner who follows the README skips the backlog | Change to: "Debrief: in a new chat, send the backlog, then the second message again. Then send the questions file with the Q4 prompt." |
| F6 | Minor (wording past source) | 5.2 talk track; section 1 row 1; B14 | W20 says "Product managers don't remember the names of studies." The module says "people" and "stakeholders" | Talk track: "UserTesting ... wrote in 2026 that product managers do not remember study names." Section 1 and B14: "product managers do not remember study names" |
| F7 | Minor (unsourced line) | 5.2 talk track | "Or someone answers from memory, and the answer goes further than the evidence." Not in W13 or W20 | Say it as the risk this job removes: "The risk: someone answers from memory, and the answer goes further than the evidence." |
| F8 | Minor (step missing) | Copilot stretch | No stop-sharing step. The Claude card has one. The doc gives the labels | Add after the steps: "To stop sharing, open **Share**. Select the role next to their name, then **Remove**." Card test row for the labels |
| F9 | Minor (date text) | Claude card header; D6 | Header says the share section showed "Updated over 2 weeks ago" on 2026-11-27. The page shows "Updated over 3 weeks ago". dateModified is 2026-11-06 | Change to: "page metadata 2026-11-06, "Updated over 3 weeks ago" when seen 2026-11-27" |
| F10 | Dan decides | Gemini card stretch; D6; change 5 | D6 puts Gemini on "plan only" because the dated post names no labels. The undated Help page names all labels (**More**, **Share skill**, **Viewer**, **Send**, **Remove access**). Module 1 D3 already accepts this undated page for the core Gemini steps | Option A (recommended): keep plan only, but fix the card line to "The dated Google post names no screen labels. The share step is not on this card." Option B: Dan extends the D3 exception. Add Gemini share steps from the Help page (web only; Workspace admin can turn sharing off; files must be shared too; a Viewer sees instructions and files; skills with a notebook attached cannot be shared). B needs the same card test rows as the other platforms |
| F11 | Minor (clarity) | C.1 title and talk track | "Five audits, five rules" on the slide, then "Your brief now has six of them" in the talk track | Talk track: "Your brief now has six rules. Five came from your audits." |
| F12 | Pass | Share steps on Claude, ChatGPT and Copilot | All screen names on the 3 share cards match a vendor doc checked 2026-11-27 (except F3, F4 and F8 gaps). "Not yet tested" and "after class" are the right labels. Data safety line "Share answers only inside approved tools" fits | None |
| F13 | Pass | Slide and talk track claims C1, C2, C4, C7, C9 | Verified. No statistic on any slide. No figure from W13 or W20 | None |

Failures: F1, F3 and F5 need a fix. F10 needs Dan's choice. F4, F6, F7, F8, F9 and F11 are small wording fixes. F2 stays open for the card test.

Gaps (not failures):

1. No doc says if Claude project memory is shared with Can view members (F2).
2. No doc says if a Claude Can view member sees the owner's chats. The card test row covers it.
3. No doc says if a Copilot Can chat user can see the instructions or the uploaded files.
4. No dated Google doc names the Gemini share labels. Only the undated Help page does.
5. ChatGPT project page shows a relative date only ("Updated: 3 days ago" on 2026-11-26 and 2026-11-27).

## Proposed platform matrix updates (for Dan's yes)

The matrix is fingerprinted. I made no change. Each row waits for Dan's yes.

| Row | Change |
| --- | --- |
| cl-pj-02 | status: verified (doc) for the share steps. source_date 2026-11-06 (dateModified; page "Updated over 3 weeks ago"). checked_on 2026-11-27. Screen names: **Share project** (to the right of the project name), name or email, **Can view**, **Can edit**, **Share**, sharing menu, member role, **Remove access** (project creator only). Limits: Team and Enterprise; admin can turn sharing off; Can view sees "project contents, knowledge, and instructions" and can chat. Each project has its own memory; doc does not say if members share it (11817273, dateModified 2026-11-24). Keep the catch-up note |
| cg-02 | status: verified (doc) for the share steps. source_date approx 2026-11-24 (page "Updated: 3 days ago" on 2026-11-27). checked_on 2026-11-27. Screen names: **Share** (sharing pane), name, email or group, chat or edit access, "Only those invited" or "Anyone with a link". Limits: chat access sees chats, files and instructions; all members can view and download files; members see the member list; owners remove members, editors cannot; workspace owners can remove collaborators and limit or turn off sharing. Collaborators: Free 5, Go and Plus 10, Pro 100, workspace project 100 |
| mb-05 | status: verified (doc) for the share steps. checked_on 2026-11-27. Screen names: **Share**, **Add a name, group, or email**, **Add people** panel, **Can chat**, **Can edit**, **Send notification**, **Add**, role dropdown then **Remove**, **Copy chat link**, **Org-wide sharing for chat access**. Limits: recipients need the license for the agent's capabilities; groups get Can chat only; anyone who can use the agent gets answers grounded in uploaded files; doc does not say if Can chat users see instructions or files |
| gm-04 | status: partly verified. checked_on 2026-11-27. Dated post (2026-11-16): share from the Skills page, View or Edit, web only, on by default, admin can turn off, follows Drive sharing, Drive files must be shared. Undated Help page (pn_skills): **Customize** > **Skills** > **More** > **Share skill**, email, **Viewer** or **Editor**, **Send**; remove with the access level, **Remove access**, **Save**; Viewers see description, instructions and uploaded files; skills with a notebook cannot be shared; recipient selects **Add skill**. Labels only on the undated page |
| gm-ui-10 | checked_on 2026-11-27. **Add files** on an existing skill found again |

Proposed ledger updates (for Dan's yes): W13 and W20 in `workflows.yaml`, checked_on 2026-11-27. Quotes found again. Add to the W20 note: "The source says product managers, not stakeholders, do not remember study names." No new ledger entry.

## Sources opened on 2026-11-27

- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects (curl, dateModified 2026-11-06)
- https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context (curl, dateModified 2026-11-24)
- https://help-lb.openai.com/en/articles/10169521-projects-in-chatgpt
- https://learn.microsoft.com/en-us/microsoft-365-copilot/extensibility/agent-builder-share-manage-agents
- https://workspaceupdates.googleblog.com/2026/11/share-skills-add-files-from-Drive-Notebook-Photos-to-skills-Gemini-app.html
- https://support.google.com/gemini?p=pn_skills
- https://www.nngroup.com/articles/why-repositories-fail/ (W13)
- https://www.usertesting.com/blog/your-research-repository-probably-graveyard-heres-how-change-ai (W20)
