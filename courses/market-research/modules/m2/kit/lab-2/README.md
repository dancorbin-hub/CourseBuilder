# Lab 2 files: add the win/loss job

The files you add to the Market Evidence Agent in lab 2. Your agent must be in its state after module 1. If it is lost or far behind, rebuild it from `kit-m2` first (about 5 minutes).

Not loaded into the agent. This file and `lab-2-record-sheet.md` are for you.

## Files

| File | What it is | Where it goes | Characters |
| --- | --- | --- | --- |
| `job-card-win-loss.md` | Job 2: the win/loss job | Knowledge | 1,483 |
| `driver-code-book.md` | Drivers, alternatives, deal source labels, program rules, driver log and match rate formats (Larkspan case) | Knowledge | 2,284 |
| `copilot-fallback-instructions-m2.txt` | Brief v2, win/loss job card and driver code book in one text | Copilot Instructions, no-license learners only | 7,171 |
| `lab-2-record-sheet.md` | Your flag decisions, audit findings, new rule and match rate read | Keep on your computer | not loaded |

Each knowledge file has a `.txt` copy with the same text. Use the `.txt` copies in Copilot. Use either copy on the other platforms.

Run files (case path, from the case folder): `m2-crm-export-q2.csv` and `m2-winloss-notes-q2.md`. Check file for the debrief: `m2-check-sample.md`.

On your own work: replace `driver-code-book.md` with your own drivers and alternatives. Keep the same format. Use an export of recent decided deals and any win/loss notes.

## Copilot with no license or billing

Your agent cannot read knowledge files.

1. Paste all of `copilot-fallback-instructions-m2.txt` into **Instructions**. It replaces the module 1 text. Select **Update**.
2. Paste the CRM export as text in chat. Upload the interview notes, or paste the text.
3. Keep the driver log from each run on your computer. Paste it in chat at the next run that needs it.

The text holds brief v2 with the lab 1 rule from the kit. If your own lab 1 rule differs, put yours under "My rules". The fallback agent does one job at a time. To rerun the module 1 job, use `kit-m2/copilot-fallback-instructions-m1-v2.txt`.

Data safety: Use an approved tool only. Do not put client data, health data protected by HIPAA or personal data (PII) into a tool your company has not approved. Get consent before you record an interview. Agree confidentiality for win/loss. Interview notes and CRM exports hold customer names and deal values.
