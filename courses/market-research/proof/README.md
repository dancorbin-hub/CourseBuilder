# Gate 2 platform proof: test cards

Course: Advanced AI for Market Research. Version 1, 2026-11-22. For Dan.

## What this proof does

The proof shows that each build pattern in the course works on each platform. It is not the Gate 3 card test of every lab. You run 3 patterns on 4 platforms, plus 5 short platform checks.

| Pattern | What it proves | Labs that use it |
| --- | --- | --- |
| P1 | Build the agent from the template, save it, reopen it and run a batch. The lab 1 planted error shows | 1, 2 |
| P2 | Add a job to the saved agent. Run 2 weeks. The second run reads the first week's result | 3 |
| P3 | One job's output feeds the next job. The agent answers a stakeholder with citations | 4, 5 |

**Time.** About 60 minutes per platform, plus about 30 minutes for the Copilot checks. You can do one platform per session.

**Order.** Do Claude first. It is the most likely to pass, so it shows what a good result looks like. Then ChatGPT, Copilot and Gemini.

## What you need

| Item | Where |
| --- | --- |
| Agent brief and job cards | This folder: `agent-brief-v1.md`, 3 job cards, `fix-rules.md` |
| Case files | The `case` folder. Use the `.txt` copies of knowledge files in Copilot |
| Results sheet | `results.md` in this folder. One column per platform |
| Accounts | Claude (code execution and file creation on), ChatGPT (Go, Plus or business plan), Copilot (agent builder access; also test without a Copilot license), Gemini (a Workspace account, if you can) |

Do not open `case/planted-errors.md` or `case/expected-results.md` during a run. They hold the answers.

## Platform setup (do this once per platform)

| Platform | Where the brief goes | Where knowledge files go | Where run files go |
| --- | --- | --- | --- |
| Claude | New Project. Paste the brief into project instructions | Project knowledge | Upload or paste in a chat in the Project |
| ChatGPT | New Project. Paste the brief into project instructions | Project files | Upload or paste in a chat in the Project |
| Copilot | Agent builder, new agent. Paste the brief into Instructions | Knowledge, as embedded files (`.txt` copies) | Upload or paste in the agent chat |
| Gemini | New skill. Paste the brief into the instructions | Skill files | Upload or paste in a chat with the skill |

Note any screen or button name that differs from this table. That goes into the step cards.

## P1: build, save, reopen and run a batch

1. Build the agent: brief `agent-brief-v1.md`, knowledge file `m1-code-book` (`.txt` in Copilot).
2. Save the agent. Close the browser tab. Open the agent again.
3. Upload `m1-interviews-batch-1.md`. Send: "Run the problem backlog job".
4. Record the result in `results.md`, P1 rows. Save the output file.
5. Add Fix 1 from `fix-rules.md` to the end of the brief. Save.
6. In a new chat, send batch 1 again with the same prompt. Record the result.

**Pass (record yes or no for each):**

| # | Check | Before the fix | After the fix |
| --- | --- | --- | --- |
| P1-a | The agent made a downloadable file, or gave the full tables in one message | yes | yes |
| P1-b | Each problem has an evidence profile with interview count, accounts and segments | yes | yes |
| P1-c | There is a proposed ranking with a reason for each rank | yes | yes |
| P1-d | **Planted error:** P05 (I-104, Multi-site visibility) is in the top 3, or first in Food service | **yes** (the error shows) | no |
| P1-e | P05 shows 1 interview, 1 account, "single source" | yes | yes |
| P1-f | P01 and P02 show 4 interviews and 4 accounts each | yes | yes |
| P1-g | The agent does not write "pattern" or "validated" | yes | yes |
| P1-h | After the fix, P05 is in the flag report and ranks last or near last | n/a | yes |
| P1-i | The structure after reopen matches the structure before | yes | n/a |

**Decision 4 rule.** If P1-d is "no" before the fix on 2 or more platforms, the error is too easy to see. Tell me, and I bring back option B with your results.

## P2: extend the agent and rerun with last week's result

Use the agent from P1, with Fix 1 in the brief.

1. Add the knowledge files `job-card-weekly-feedback.md` and `m3-tag-list` (`.txt` in Copilot).
2. Upload `m3-feedback-week-1.csv`. Send: "Run the weekly feedback job". Save the output.
3. Save the week 1 result: add the output file to the agent's knowledge files. In Gemini, upload the whole skill again with the new file. Record how long this takes.
4. In a new chat, upload `m3-feedback-week-2.csv`. Send: "Run the weekly feedback job. Compare with the week 1 result in your knowledge files."
5. Record the result. Add Fix 2 to the brief. Run step 4 again in a new chat.

**Pass:**

| # | Check | Before the fix | After the fix |
| --- | --- | --- | --- |
| P2-a | Week 2 compares with week 1 (it read the saved result) | yes | yes |
| P2-b | Counts are by account: P01 shows 7 accounts in week 2, not 11 | yes | yes |
| P2-c | **Planted error:** items F-1215 to F-1219 are tagged P02, and P02 jumps to about 7 accounts | **yes** | no |
| P2-d | After the fix, F-1215 to F-1219 are "no fit", with 4 accounts, in the flag report | n/a | yes |
| P2-e | F-1221 (a name and phone number) is in the flag report | yes | yes |
| P2-f | Copilot only: brief plus the job card stays under 8,000 characters in Instructions | yes | yes |

## P3: hand-off between jobs and a cited answer

Use the agent from P2.

1. Add the knowledge files `job-card-alternatives-map.md` and `m4-alternatives-map` (`.txt` in Copilot).
2. Upload `m4-evidence-pack.md`. Send: "Run the alternatives map job". Record the result.
3. Add Fix 3 to the brief. In a new chat, run step 2 again. Record the result.
4. Stay in this chat. Add the knowledge files `job-card-stakeholder-answers.md` and `m5-past-reports` (`.txt` in Copilot).
5. Add the age limit from `fix-rules.md` to the brief.
6. Paste Q1, Q2 and Q5 from `m5-stakeholder-questions.md`. Send: "Run the stakeholder answer job". Record the result.
7. Add Fix 4 to the brief. Ask Q2 again. Record the result.

**Pass:**

| # | Check | Before the fix | After the fix |
| --- | --- | --- | --- |
| P3-a | Each map entry links to a deal ID or interview ID | yes | yes |
| P3-b | **Planted error (lab 4):** D-3108 counts for Rimecore, and Rimecore shows "growing" (Q2 2, Q3 3) | **yes** | no |
| P3-c | After Fix 3, D-3108 is "do nothing", Rimecore shows Q3 2 "no change", and the D-3108 mismatch is in the flag report | n/a | yes |
| P3-d | Each answer cites date and segment, and has a "what we do not know" line | yes | yes |
| P3-e | **Planted error (lab 5):** the Q2 answer says buyers want a one-click inspection binder, from R-2024-07 | **yes** | no |
| P3-f | After Fix 4, the Q2 answer flags R-2024-07 (Food service, 2024) and says the question needs new research | n/a | yes |
| P3-g | Q5 does not say "many customer sites". It names Food service as the only segment with interviews | yes | yes |
| P3-h | Proposals are by segment and labeled "proposal" | yes | yes |

**Watch item.** The age limit goes in before the lab 5 run, as in the lab. If P3-e is "no" on most platforms, the error may be too easy. Tell me.

**Rebuild check.** On one platform, time how long it takes to rebuild the P3 agent from these files in a new Project or agent. The target is about 5 minutes.

## Copilot checks (G2-PF-01 to 05)

| ID | Check | How |
| --- | --- | --- |
| G2-PF-01 | Does agent builder take `.md` files as knowledge? | Try to add `m1-code-book.md`. Record yes or no. The `.txt` copy is the fallback |
| G2-PF-02 | Chat upload: 3 files in one message, and `.csv` files | Upload `m2-crm-export-q2.csv`, `m2-winloss-notes-q2.md` and `m2-check-sample.md` in one message. Test with and without a Copilot license |
| G2-PF-03 | Longest paste | Paste all of `m4-evidence-pack.md` (about 15,400 characters) into chat. Record if it is accepted |
| G2-PF-05 | No-license fallback | Without a license, paste the brief, then one job card and one knowledge file into Copilot Chat. Run P1 steps 3 and 4. Record if it works |

G2-PF-04 is the Gemini check: upload 3 files in one prompt, add 3 files to the skill, and record the most files a skill takes (the course needs 12).

## When you finish a platform

1. Fill in the column for that platform in `results.md`.
2. Paste the outputs of the "before the fix" runs in this thread, or put the files in the project files folder.
3. I check them against the expected results, and I update the step cards and the planted errors.

Log your hours with `activity=gate-2-proof`.
