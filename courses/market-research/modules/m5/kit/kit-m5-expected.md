# kit-m5: what it must contain (for the module 4 builder)

**Status 2026-11-27: met.** Module 4 delivered every file in `modules/m4/kit/kit-m5/`. Rows 1 to 13: met as listed, with the counts in the last column. Row 14: met, with the map in chat (module 4 D12). Section 3 answers: (1) rule 4 lives in the brief "My rules"; (2) the text is the `case/planted-errors.md` lab 4 fix; (3) yes, the log save card saves the driver log with the Q3 rows and the map; (4) `modules/m4/kit/kit-m5/job-card-alternatives-map.md`, 1,497, now also in kit-final; (5) no "controller alarms" row in the driver code book; (6) counts in `modules/m4/module.md` section 8.

Module 5 builder, 2026-11-27. Module 4 is not built yet (OI-05 open). Module 5 starts from kit-m5, the state after module 4. This file lists exactly what kit-m5 must hold, so module 4 makes it to match. Decision for Dan: D1 in `modules/m5/module.md`.

Where kit-m5 goes: `modules/m4/kit/kit-m5/` (module 4 builder). Draft files built from the case are in `modules/m5/kit/kit-m5-draft/`. Copy them if module 4 keeps them as they are.

Status words in the table:

- **No change**: copy from `modules/m3/kit/kit-m4/` as it is.
- **From the case**: built by the module 5 builder in `kit-m5-draft/`, from case records only. Module 4 checks the format against its lab.
- **To be set by module 4**: depends on the module 4 lab rule or design. Module 4 writes it. The constraints in the last column bind it.

## 1. Files

| # | File (`.md` plus a `.txt` copy) | Loads into | Status | Source | Constraint for module 5 |
| --- | --- | --- | --- | --- | --- |
| 1 | `README.md` (no `.txt`) | Not loaded | To be set by module 4 | Pattern: `kit-m4/README.md` | Says: 10 knowledge files after module 4; lab 5 adds 2 (12 at the end) |
| 2 | `brief-v5.md` | Instructions | From the case, place to be set by module 4 | `kit-m4/brief-v4.md` plus "My rules" 4, the lab 4 fix text in `case/planted-errors.md` | 3,500 characters or fewer (draft: 3,491). If module 4 puts its rule in the job card, brief v5 is brief v4 with the new title. Then the lab 5 rule is "My rules" 4, and module 5 changes "rule 5" on the record sheet and cards |
| 3 | `job-card-problem-backlog.md` | Knowledge | No change | `kit-m4` | 1,194 |
| 4 | `code-book.md` | Knowledge | No change | `kit-m4` | 2,791 |
| 5 | `problem-backlog.md` | Knowledge | No change | `kit-m4` (same facts as Part 4 of `case/m4-evidence-pack.md`, different layout). The map job reads it. It does not write it | 15,194. Under the 15,400 paste target. Do not make it longer |
| 6 | `job-card-win-loss.md` | Knowledge | No change | `kit-m4` | 1,483 |
| 7 | `driver-code-book.md` | Knowledge | No change, unless module 4 adds controller alarms to the alternatives list (to be set by module 4) | `kit-m4` | 2,800 or fewer |
| 8 | `driver-log.md` | Knowledge | From the case. Needs D2 | `kit-m4` Q2 rows plus the 10 Q3 rows of Part 1 of `case/m4-evidence-pack.md`. Alternative chosen read from the interview: D-3102 Vantafrost (WL-3102), D-3108 do nothing (WL-3108). D-3108 quote from WL-3108: "Your trial sent alerts every lunch rush, and my managers gave up on it." (D7 in module 5). Q3 flag: D-3108 with the case PM decision | 7,616 in the draft. With the map and the past reports, 15,400 or fewer in one paste (draft: 13,675) |
| 9 | `job-card-weekly-feedback.md` | Knowledge | No change | `kit-m4` | 1,496 |
| 10 | `tag-list.md` (version 2, with P10) | Knowledge | No change | `kit-m4` | 2,038 |
| 11 | `job-card-alternatives-map.md` | Knowledge | To be set by module 4 | Start: `proof/job-card-alternatives-map.md` | 1,500 or fewer. Name where the lab 4 hand-off rule lives |
| 12 | `alternatives-map.md` | Knowledge (replaces `m4-alternatives-map`) | From the case | `case/expected-results.md` lab 4 table (after the fix), types and formats from `case/m4-alternatives-map.md` | 3,286 in the draft. Keep the types table and the 2 format tables, so a rerun of job 4 still has them |
| 13 | `lab-4-fix-rules.md` | Not loaded. Handout | To be set by module 4 | Pattern: `kit-m4/lab-3-fix-rules.md` | none |
| 14 | `copilot-fallback-instructions-m4-v5.txt` (no `.md`) | Copilot Instructions, no license | Met (module 4) | Brief v5 and map job card. Map in chat (module 4 D12: with the map it is 8,681, over 8,000) | 8,000 or fewer (mb-01). Course budget 7,800. Delivered: 5,388 |

Knowledge files after module 4: 10 (files 3 to 12). Lab 5 adds `job-card-stakeholder-answers` and `past-reports`: 12 at the end. Course budget 13.

## 2. Facts lab 5 reads from kit-m5 (acceptance test)

The lab 5 expected answers (`case/expected-results.md`, lab 5) use these records. If kit-m5 drops one, a lab 5 pass condition fails.

| Lab 5 item | Records it needs | In which kit-m5 file |
| --- | --- | --- |
| Q1 (VP Sales, pharmacy and lab price) | D-2210 (CRM only, Price). D-2211, D-3105, D-3107 (interviewed Pharmacy and lab losses, Q2 and Q3 2027). D-2206 (won) | Driver log, Q2 and Q3 rows |
| Q2 (Head of Hardware, report pack; planted) | P08 (I-107, I-108, I-113; 3 accounts). P02 in Pharmacy and lab (I-108; feedback A-14, A-29). D-2206, D-3105 | Problem backlog, driver log |
| Q3 (optional; demo question) | P06 (I-101, I-106, I-110, I-112; same account I-106 and I-112) | Problem backlog |
| Q4 (check question) | P01 in Food service (I-105, AI-moderated; feedback A-09, A-28). D-3108 (Food service, alert accuracy) | Problem backlog, driver log |
| Q5 (FDP PM, hub signal) | P03 (I-103, I-105, I-111; A-04, A-30). D-2203 (Q2, Distribution, hub, Rimecore) | Problem backlog, driver log |
| Proposals by segment | Backlog segment counts and feedback accounts. Map by segment: do nothing top in Food service | Problem backlog, alternatives map |

## 3. Choices module 4 must tell module 5

| # | Choice | Why module 5 needs it |
| --- | --- | --- |
| 1 | Where the lab 4 hand-off rule lives: "My rules" 4 in the brief, or the map job card | The lab 5 rule number on the record sheet and in brief v6 (kit-final) |
| 2 | The exact lab 4 rule text | brief v6 in kit-final copies it |
| 3 | Does the lab 4 log save card save the driver log with the Q3 rows, as well as the map? (D2) | Lab 5 Q1 and Q4 need the Q3 deals in the agent |
| 4 | Final `job-card-alternatives-map.md` | kit-final copies it |
| 5 | Does module 4 add "controller alarms" to the driver code book? | kit-final copies the driver code book |
| 6 | Character counts of the module 4 files | Module 5 section 8 and the kit-final README |

When module 4 is built, the module 5 builder (or the coordinator) checks kit-m5 against this file and updates kit-final.
