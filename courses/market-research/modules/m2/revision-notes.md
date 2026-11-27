# Revision notes: module 2 (revise once)

Module builder, 2026-11-27. Inputs: `consistency-report.md`, `verifier-report.md`, Dan's yes of 2026-11-27 (commit e78ee77) and the case year shift to 2027 (`case/year-shift-map.md`). I changed only `module.md` and `card-test.md`. I did not change the spec, the case, the kit numbers, the research files or module 1.

Year shift: the kit files and slide 2.5 were already shifted to 2027 in commit 0358e45. I found no 2026 case date left in `modules/m2/`. Real dates (sources, check dates) stay 2026.

## Consistency report

| # | Severity | Finding | What I did |
| --- | --- | --- | --- |
| 1 | Major (must fix) | D1, D2, D5 and "Changes needing Dan's yes" rows 1 and 2 were decided on 2026-11-27. Case note 5 out of date | Moved D1, D2 and D5 to a new table "Decided by Dan (2026-11-27)". D2 now gives the stretch check results (cl-sc-07, cg-06, mb-06, gm-07). Removed the 2 change rows. Deleted case note 5 and renumbered the notes |
| 2 | Minor | Claude and ChatGPT stretch line out of date | Now: "No stretch step in module 2. The schedule stretch is in module 3." |
| 3 | Minor | "On the template brief" in 2.14 and section 6 | Now "On brief v2" in both places |
| 4 | Minor | 2.13: two groups of 9 can be mixed up | Talk track and the on-click line now say "7 of all 9 lost deals in the CRM" and "1 of the 6 interviewed lost deals" |
| 5 | Minor | Record sheet line leads straight to WL-2214 | Not changed. Now open decision D2 with 3 options. Recommended B: shorten the sheet line to "Then read the deal source column for every deal." |
| 6 | Minor | 2.11 talk track did not start "The goal of this activity is". 2.3 named Dan | 2.11 now starts "The goal of this activity is to know what done looks like before you start." 2.3 now says "with one change for this course" |
| 7 | Minor | 2.10 key actions miss the rerun | Added "Run again in a new chat." 6 short key actions. B2 updated |
| 8 | Minor | Fallback sum: 470 should be 484 | Now "484 characters of header (470) and separators (14) = 7,171" |
| 9 | Minor | Card test P1-m2-e misses D-2214 | Added "and, after the fix, D-2214 (no interview)" on all 4 platforms |

## Verifier report

| # | Finding | What I did |
| --- | --- | --- |
| F1 | "Both also say a manual program is slow": Clozd does not | Talk track now: "Corporate Visions also says a manual program is slow." |
| F2 | On-slide line 2 has 1 source (W2) | Open decision D1 (option A recommended: Klue as second source, line becomes "Manual win/loss is slow."). On-slide text not changed until Dan's yes. The talk track already attributes "slow" to Corporate Visions only (F1). Sources line now says line 2 rests on W2 only. Ledger addition listed for Dan's yes |
| F3 | "both wrote in 2026" | Now "both say in 2026 pages" |
| F4 | D11 text wrong: W1 also says it, from the same old Pragmatic data as W3. Spec bottleneck cites W2, which does not say it | D11 moved to "Decided" (kept off the slides, research rule) with the corrected reason. Kept-off line in section 9 corrected. Spec change listed for Dan's yes (row 1) |
| F5 | Market visit article age flag was accepted at Gate 1 | Draft D13 moved to "Decided". Slide 2.8 Sources line says so |
| F6 | New Microsoft file formats doc, licensed Copilot Chat only | Open decision D5 names it. Card wording kept ("upload, or paste the text"). New matrix row mb-ui-15 listed for Dan's yes |
| F7 | Gemini existing skill uses **Add files** | Gemini step 1, log save row and the card test row now say **Add files**. Section 9 failure row updated. Same issue in module 1 listed for Dan's yes (row 4) |
| F8 | Wrong blog title | Fixed on the Gemini card. Module 1 card has the same title: listed for Dan's yes (row 4) |
| F9 | Gemini Help page undated | No change. Module 1 D3 covers it |
| F10 | Gems line for Workspace | No change. Dan chose it at Gate 1 (PA-09) |
| F11 | Claude Team and Enterprise toggle path | Claude card note adds "Team or Enterprise: ask your owner." ("owner", the same word as module 1.) Section 9 row adds **Organization settings** |
| F12 | New chat has no control name | No card change. Card test now asks the Copilot and Gemini testers to record how a new chat starts |
| F13 | Stale decisions | Same as consistency finding 1 |
| F14 | Pass | None |
| Check dates | All docs reopened 2026-11-27 | The 4 card headers now say "Check date 2026-11-27 (all docs reopened by the module 2 verifier)". Matrix `checked_on` updates wait for Dan's yes |

## Decisions renumbered

The open decisions are now D1 to D10, one line each with a recommendation (section 1). Draft numbers map as follows: F2 is new D1. Draft D6 plus consistency finding 5 is D2. Draft D12 is D3, D7 is D4, D8 is D5, D14 is D6, D4 is D7, D3 is D8, D9 stays D9 and D10 stays D10. Draft D1, D2, D5, D11 and D13 are in "Decided by Dan".

## Checks after the revision

- 17 slides. 70 minutes (full day) and 75 (half day). 28 / 42 and 30 / 45, 40% instructor-led.
- No em or en dashes in `modules/m2/`. No banned terms.
- No step card, pass condition, notes or stretch sentence over 20 words (the standard data safety sentence is accepted, module 1 D15).
- Kit unchanged. Every `.txt` copy matches its `.md`.
