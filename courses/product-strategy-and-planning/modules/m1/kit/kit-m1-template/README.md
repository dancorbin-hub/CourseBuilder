# kit-m1-template: start of module 1

The starter template for the Strategy Evidence Agent. Use it in lab 1, or to rebuild the agent in about 5 minutes.

Not loaded into the agent. This file and `lab-1-record-sheet.md` are for you.

Fictional data for training: the Larkspan files are invented. See `case/README.md`.

## Files

| File | What it is | Where it goes | Characters |
| --- | --- | --- | --- |
| `brief-v1.md` | Core brief: role, core rule, rules you set, flag report, decision fields, "My rules" | Instructions | 2,164 |
| `job-card-portfolio-pack.md` | Job 1: the portfolio pack job, with its quality checks and hand-off rules | Knowledge | 1,365 |
| `strategy-okrs-kpis.md` | Larkspan 2028 strategy overview, OKRs and KPIs (case path) | Knowledge | 2,770 |
| `capacity-sheet.xlsx` | Course sheet with formulas. One row per team and program. It checks each program row alone | Knowledge | not counted (sheet) |
| `capacity-sheet.csv` | CSV copy of the sheet. Use it if `.xlsx` upload fails (not for Copilot knowledge) | Knowledge (Claude, ChatGPT, Gemini only) | not counted (sheet) |
| `copilot-fallback-instructions-m1.txt` | Brief, job card and strategy file in one text | Copilot Instructions, no-license learners only | 6,673 |
| `lab-1-record-sheet.md` | Data check, flag decisions, audit, new check, your calls | Keep on your computer | not loaded |

Each `.md` file that you load has a `.txt` copy with the same text. Use the `.txt` copies in Copilot. Use either copy on the other platforms.

Google Sheet option: the instructor shares a Google Sheet template of the capacity sheet. Make a copy. Work in your copy. Download it as `.xlsx` or CSV, then upload it to your agent or in chat. The agent does not write live into your Sheet.

On your own work: replace `strategy-okrs-kpis.md` with your own strategy, OKRs and KPIs. Replace the rows of the capacity sheet with your own teams and programs. Change the [EDIT] line in the brief.

## Rebuild card (about 5 minutes)

| Platform | Brief goes in | Knowledge files go in | Saves |
| --- | --- | --- | --- |
| Claude | Project: **Set project instructions** | Project knowledge: **+** | **Save instructions**. Files save when added |
| ChatGPT | Project: **•••**, then **Project settings** | Project files | As you go |
| Copilot | Agent builder, **Configure** tab: **Instructions** | **Knowledge**: **Upload** (`.txt` copies and `capacity-sheet.xlsx`) | **Create** the first time, then **Update** |
| Gemini | Skill: instructions | Skill files: **Add**, then **files**, then **Upload** | **Create** the first time, then **Save** |

Copilot with no license or billing: paste `copilot-fallback-instructions-m1.txt` into **Instructions**. Add no knowledge files. Upload `capacity-sheet.xlsx` and the run files in chat each run. If upload fails, paste the text.

Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Do not put unreleased roadmaps or release dates, forecasts, pricing, supplier terms or other non-public financial data into a tool your company has not approved. Do not put confidential names in web search queries.
