# Method library: managing a course agent

Course: market-research. Stage 1, track 2. Written 2026-11-20.

Platform facts come from `platform-matrix.yaml`. Each feature there is "not verified" until the Verifier checks it.

## What this file is

- These are design methods for an agent manager. They are not research findings.
- No study found yet shows that one method works better than another. See gaps.md, Track 2.
- Each method names where it lives on each platform, and if a core lab can use it with no connectors.

## How the four builds hold the parts

| Part | Claude | ChatGPT | Copilot agent builder | Gemini |
| --- | --- | --- | --- | --- |
| Brief (instructions) | Project instructions, or SKILL.md in a skill | Project instructions (all plans). Skill on Business, Enterprise, Edu only | Instructions field, 8,000 characters | Skill instructions (SKILL.md) |
| Knowledge (code book, log, templates) | Project knowledge, or reference files in the skill | Project files: 5 Free, 20 to 25 Plus, 40 Pro and business plans | Embedded files: 20 max. Needs a Copilot license or pay-as-you-go | Files in the skill, 100 MB total |
| File output | .xlsx, .docx, .pptx, .pdf, .csv, 30 MB (code execution on) | Not documented (gap) | Code interpreter. Formats not documented | Not documented (gap) |
| Schedule (stretch) | Cowork scheduled tasks, paid plans | Scheduled tasks. Project files are not available to the task | Scheduled workflows in agent builder, rollout to mid-December 2026 | Tasks with schedules, personal accounts only |
| Trigger (stretch) | Not found | Gmail, Slack, GitHub events, Plus and higher | Copilot Studio event triggers (outside agent builder) | Gmail and topic monitors, Pro and Ultra |
| Catch-up template | Upload a skill zip (all plans). Project sharing needs Team or Enterprise | Paste brief, upload files. Skill share on business plans | Paste brief, upload files. Sharing gives run-only or co-owner rights | Shared skill, "save a copy" (best documented) |

## Methods

### M1. The brief

- **What the learner does:** Writes the job, the inputs, the output format and the "done" criteria in one block.
- **Why:** The brief is the agent's standing order. Each later lab adds to it.
- **Where it works:** All 4 platforms. Core lab: yes.
- **Limits:** Copilot holds 8,000 characters. Keep the brief under 6,000 characters so later labs can add rules. Move long content (code book) to a knowledge file.
- **Format tip:** Use the same headings on all platforms: Job, Inputs, Steps, Output, Checks, Hand-off rules, Flag report. One template serves 4 step cards.

### M2. Quality checks

- **What the learner does:** Adds checks the agent runs on its own output before it reports. Example: "Each quote is found word for word in its source interview."
- **Why:** The agent catches the cheap errors. The learner keeps time for judgment.
- **Where it works:** All 4 platforms, as lines in the brief. Core lab: yes.
- **Limit to teach:** A check the agent runs on itself can pass and still be wrong. The planted error in the worked example (one vocal buyer counted as a pattern) passes the quote check. Only the audit (M5) finds it.

### M3. Hand-off rules

- **What the learner does:** Lists the cases where the agent stops and gives the item to the PM. Example: "A new insight contradicts the log."
- **Why:** The agent must know where its authority ends.
- **Where it works:** All 4 platforms, as lines in the brief. Core lab: yes.
- **Naming:** Call these "hand-off rules". Do not call them "exceptions" or "escalations" (CLAUDE.md rule 12).
- **Registry note:** The AI Agents course teaches boundaries and exit conditions. Refer to them. Teach only the new part: hand-off rules on a running agent.

### M4. The flag report

- **What the learner does:** Sets a fixed output section that lists each flag: item, reason, source, the decision needed.
- **Why:** The PM reads the flags, not the full output. This is the core "agent manager" habit.
- **Where it works:** All 4 platforms, as an output format in the brief. Core lab: yes.
- **File output:** Claude can write the report to a .docx or .xlsx. On ChatGPT, Copilot and Gemini, file output is not documented. Use an on-screen table in the core path until the Gate 2 proof.

### M5. The audit

- **What the learner does:** Picks 3 random items from the output. Checks each against the source by hand.
- **Why:** Finds errors that pass the agent's own checks.
- **Where it works:** All 4 platforms. It is a learner task, not an agent feature. Core lab: yes.
- **Tip:** Ask the agent to number every item. The learner picks numbers with a dice roll or a random number tool, so the agent does not choose what is audited.

### M6. Tuning the brief

- **What the learner does:** Turns each audit finding into a new rule in the brief. Runs the next batch. Checks that the error is gone.
- **Why:** The brief gets better over time. The agent improves without a new build.
- **Where it works:** All 4 platforms. Core lab: yes.
- **Platform friction:**
  - Gemini: to change files in a skill, re-upload the whole skill. Instructions can be edited in place.
  - Claude skill: re-upload the zip. A Claude Project is easier to edit in class.
  - Copilot: edit the instructions field. Watch the 8,000-character limit.
  - ChatGPT Project: edit project instructions.
- **Suggestion:** Keep a "change log" line at the end of the brief. Each tuning adds one dated line. This also gives the audit trail.

### M7. Runs over time (batch 1, batch 2)

- **What the learner does:** Gives the agent the current log plus a new batch. Checks the "what changed" summary.
- **Why:** The real workflow repeats. One-pass synthesis is already taught in PDW-AI.
- **Where it works:** All 4 platforms, by uploading the new batch in chat. Core lab: yes.
- **Limit:** Project and knowledge files are fixed until the learner replaces them. The updated log must be downloaded and re-uploaded, or pasted. Claude can output the log as a file. On the other platforms this is a gap until tested.

### M8. Schedules (stretch only)

- **What the learner does:** Sets the agent to run on a cadence, for example each Monday.
- **Where it works and the catch:**

| Platform | Feature | Plan | Catch |
| --- | --- | --- | --- |
| Claude | Cowork scheduled tasks | Paid plans | Input files must reach the task without a local folder, or the computer must be on |
| ChatGPT | Scheduled tasks | All plans; hourly on paid | A task in a project cannot read the project files. Put the brief in the task or a skill |
| Copilot | Scheduled workflows in agent builder | Copilot Premium | Rollout mid-November to mid-December 2026. Not for unpublished agents |
| Gemini | Tasks with schedules, can call a skill | Personal accounts only | Workspace accounts not supported |

- **Core lab:** No. A schedule with no new input does nothing useful. New input needs a connector or a shared folder.

### M9. Triggers (stretch only)

- **What the learner does:** Sets the agent to run when new input arrives (new email, new file).
- **Where it works:** ChatGPT (Gmail, Slack, GitHub; Plus and higher). Gemini (Gmail monitors; Pro and Ultra; personal only). Copilot Studio (new file in OneDrive or SharePoint; Copilot Credits; maker credentials). Claude: no trigger feature found.
- **Core lab:** No. All need connectors.
- **Data safety point:** Copilot Studio triggers run with the maker's credentials. Teach this as a guardrail.

### M10. Catch-up kit (for each module)

- **Problem:** No platform gives a clean "copy this template agent" for learners from many companies.
  - Claude and Copilot sharing gives either read-only use or edit rights on one shared copy.
  - Claude project sharing and ChatGPT skills need business plans.
  - Copilot sharing works only inside one tenant.
- **Method:** Give a catch-up kit per module. It holds the brief as text (with that module's additions), and the knowledge files. The learner builds a fresh agent from it in about 5 minutes.
- **Extra option:** One Agent Skills folder (SKILL.md plus files) can upload to Claude (all plans), Gemini (all accounts) and ChatGPT skills (business plans). Not tested.
- **Gemini only:** A shared skill can be saved as an editable copy. This is the cleanest path where Drive sharing is allowed.

### M11. Planted error and fading warning

- **What the instructor does:** Plants one AI error per lab in the fallback case data. Lab 1 tells learners. Middle labs hint. The last lab says nothing (CLAUDE.md rule 13).
- **Where it works:** All 4 platforms, because the error is in the data, not the tool. Core lab: yes.
- **Gate 2 check:** The same data must make the error appear on all 4 platforms. Models differ, so the card test must confirm it on each.

## Risks for the core path

1. **Copilot license.** Copilot Chat users without a license or pay-as-you-go billing cannot use embedded files as knowledge. Fallback to test: paste the code book into instructions and upload the batch in chat.
2. **Copilot 20-file limit.** Keep the course agent at 20 knowledge files or fewer across all modules.
3. **ChatGPT skills.** Only on business plans. The ChatGPT core build is a Project.
4. **ChatGPT Free.** 5 project files. A full course agent may not fit. Merge files.
5. **Gemini Workspace.** Two Google sources disagree on when work accounts get skills. Test on a Workspace business account.
6. **File output.** Only Claude documents downloadable .xlsx and .docx output.
7. **Code execution off.** Claude skills and file output need code execution. A company admin can turn it off.

## Sources

All sources, dates and check dates are in `platform-matrix.yaml`.
