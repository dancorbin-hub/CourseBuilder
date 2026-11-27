# Revision notes: module 1 (revise once)

Module builder, 2026-11-27. Inputs: `consistency-report.md` and `verifier-report.md` (both 2026-11-27). No spec, case, research or fingerprinted file was edited. After the revision: slide minutes 70 (full day) and 80 (half day), split 28/42 and 32/48 (40/60). Course open 25. No em or en dashes (grep on U+2014 and U+2013 in `modules/m1/`).

## Must fix

| Finding | What I changed |
| --- | --- |
| Consistency M1: Copilot step 1 uploads "the other `.txt` files", which includes the fallback text (a second brief) | Copilot step 1 now names the files: "replace the starter instruction with `brief-v1.txt`. Upload `job-card-portfolio-pack.txt` and `strategy-okrs-kpis.txt` in **Knowledge**." |
| Consistency M2: the Google Sheet template does not exist | Placeholder "[Google Sheet link: added before the card test]" on each card and in the `kit-m1-template` README. The Gemini sums check falls back to `capacity-sheet.xlsx` or `.csv` in any spreadsheet tool until the link exists. Listed for Dan (question 2). The template itself is not made: it is a Google asset outside the repo |
| Verifier M1: O.7 says a Copilot license is needed to create an agent | O.7 slide: "Agent or skill creation allowed? Copilot knowledge files: license or billing?" Talk track: "On Copilot, the agent reads knowledge files only with a Microsoft 365 Copilot license or pay-as-you-go billing." |
| Verifier M2: O.8 says a one-off prompt forgets your data | Sentence removed. New line: "An agent keeps files in its knowledge and uses them on every run." |
| Verifier M3: Gemini label is **images or files**, not **files** | Fixed in all 4 places: Gemini card step 1, fast-start row, build check step 3, kit README rebuild card |

## Should fix

| Finding | What I changed, or why not |
| --- | --- |
| Consistency S1: pass condition on the card against spec `planted_error_fade.rule`; no second sample on 1.10 | Kept on the card (PRD rule 7, Market Research D7). 1.10 on-slide text and talk track now name the second sample and say the pass condition is on the card. Spec line not edited: question 3 |
| Consistency S2: `kit-m2/job-card-requests.md` missing | Not built: the module 2 builder owns it. The kit-m2 README already says so. Information line for Dan |
| Consistency S3: Google Sheet line as a shared block; Copilot `.xlsx` only; "not verified" wording | The shared block now points to the per-card lines. Each card has its own Google Sheet line. Copilot says "`.xlsx` only". All cards and the kit README say "A live write by the agent into your Sheet is not verified" |
| Consistency S4: O.7 talk track says "Two minutes" | Now "Three minutes" |
| Consistency S5: card step 1 does not say replace | All 4 cards: "Replace the starter instruction with `brief-v1`" |
| Consistency S6: Copilot step 2 in the agent chat | Now "In a new chat" |
| Verifier F1: Copilot toggle conflict | "If you see **Create documents, charts, and code**, check that it is on." |
| Verifier F2, F3: Trendslop wording past the sources | O.2 slide and talk: "many scenarios", "whatever the context". The "being different or cost" trade-off is removed. "The advice sounded tailored. It was not." became "The researchers warn that an answer can sound tailored to your situation and still not fit it" (Fortune quote of the authors) |
| Verifier F4: 1.8 "tell you what to fund" | Now "A model will happily pick a strategy for you. Its answer will sound tailored." |
| Verifier F5: ChatGPT memory labels and delay | Cards and build check use **Default memory** and **Project-only memory**. Build check cue and a section 9 row say to fix memory at the build check, because a change "may take a few hours" |
| Verifier F6: Gemini "No Customize? Select More first" | Added to the Gemini lab card notes and the build check pass line |
| Verifier F7: card doc dates | Check dates now 2026-11-27 (verifier). Claude skills page dateModified 2026-10-30. ChatGPT projects page approx 2026-11-27. Gemini card adds the dated Workspace Updates post (2026-10-21) for **Customize** and **Skills** |
| Verifier F8: question 9 (Gemini `.xlsx`) | Closed: `.xlsx` is supported (gm-14). Moved to information. Card test row kept |
| Verifier F9: no recovery for Claude new projects beta | Section 9 row added: send each run as a new message and say "Use only the Q4 files", or pair the learner. Claude card header cites "What are projects?" (cl-pj-11) |
| Verifier F10: paste fallback does not work for `.xlsx` | Copilot card notes and kit README: "For the sheet, paste the text of `capacity-sheet.csv`." |
| Verifier F11: N21 has no ledger row | Not edited (research file). Listed in question 6 for research to add |

## Consider items

| Finding | Action |
| --- | --- |
| C1: headlines 1.12, 1.13, 1.15, 1.16, O.4 match Market Research word for word | Renamed: "What did your team totals show?", "Test the tuned brief on a new quarter", "Monday: total your shared teams", "Decide what the capacity log keeps", "Build, save, reopen" |
| C2: model names in O.2 | Kept. Verifier C04 verified them (Fortune) |
| C3: 1.14 crowded | Not changed. The story slot is optional and first to cut (section 9 timing flex). Card test records the time |
| C4: O.6 "read only the flags" | Now "You read the flags and audit a sample" |
| C5: "pack log" against the capacity sheet | Information line for the planner |
| C6: cl-pj-11 missing from the verifier list | Added to the screen name table |
| C7: no `.txt` copies of `.md` run files for Copilot chat | Not changed. Card test row covers it. If upload fails, the case builder adds `.txt` copies |
| C8: `Team_capacity_pct` 100 fixed in the template | Kit README now labels it the Larkspan PM's choice, to set on your own work |

## Questions for Dan

Cut from 14 to 8. Dropped or moved to information: lab brief short version (Dan's own rule), kit-m2 contents, data safety sentence length, check sample quarter, half-day minutes, Gemini `.xlsx` (answered by the verifier). Final list: `module.md`, section 1.
