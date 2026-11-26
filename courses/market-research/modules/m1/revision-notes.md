# Revision notes: module 1 (revise once)

Module builder, 2026-11-26. Inputs: `consistency-report.md` and `verifier-report.md`. I changed only module files and the kit. I did not change the spec, the case or research files.

## Consistency report: must fix

| # | Finding | What I did |
| --- | --- | --- |
| 1 | Card step 6 (both batches in a new chat) differs from spec `card_steps` 6 | Kept my version, as the coordinator asked. It is now decision D1 in `module.md`. D1 gives the reason and spells out the revert option (step 6, slide 1.10 and brief text) |
| 2 | Slide 1.11 time guide disagrees with its notes and section 9. Half-day cues missing | Fixed. Send both batches at minute 28 (half day 32). Learners who are behind skip step 6 at minute 30 (half day 35). On-slide guide, notes and section 9 now agree. The half-day guide and cues are added |
| 3 | Slide 1.16 transition "[BREAK, OR MODULE 2 IN THE HALF DAY]" | Changed to "[BREAK]". Both agendas have a break after module 1 |
| 4 | Pass condition item 4: 21 words, and the "if the learner added the lab 1 rule" condition was dropped | Split into 2 sentences. Restored the condition: "If you added a single-source rule, it also lists P07 (all 3 quotes from I-201)." |
| 5 | "AI-moderated only" inconsistent in the kit | No case or spec edit. The kit now matches the code book: brief v1, brief v2 and the `kit-m2` backlog have all 3 labels (P07 has the label; P08 shows the label clearing). Slides and cards still show 2 labels (decision C2). The slide 1.8 talk track says the third label may appear. Decision D2 lists the 4 places and the options |

## Consistency report: consider

| # | Finding | What I did |
| --- | --- | --- |
| 1 | Pass condition on the card vs spec `success_checks` (PRD wins) | Kept on the card. Decision D7 asks Dan to update the spec line |
| 2 | Audit hint points at the error | Kept for lab 1 only. B4 now says labs 2 to 4 do not carry it. Decision D11 |
| 3 | Minute 12 cue "read the flag report while you wait" cannot be done | Changed to "open batch 1 and read one interview while you wait" |
| 4 | Registry: slide 1.3 teaches one-pass synthesis and the quote check; slide 1.8 re-defines the three tests | Slide 1.3: the known items are one small line, not a column, with a one-line reminder in the talk track. Slide 1.8: the three tests are named as known with one reminder line. The slide and talk track now teach how the agent reports each test and how the PM checks it |
| 5 | Data safety box not on the lab brief slide 1.10 | Added the standard box to slide 1.10 and one talk track line |
| 6 | Copilot fallback text says "find that job card in your knowledge files" | Both fallback headers now say: "Where the brief says 'find that job card in your knowledge files', use the job card below." Recounted |
| 7 | Spec wording ("persona P05"; 22-word data safety sentence) | Decision D15. No spec edit |
| 8 | kit-m2 has no module 2 fallback | Decision D13 (module 2 builder adds it, about 2,600 characters left) |
| 9 | The half-day minutes line names more slides than spec `half_day.note` | Reworded: the slide minutes follow spec `arc_minutes`. The line names the extra minute on 1.4, 1.5 and 1.9. Decision D16 |
| 10 | Gemini Replace file vs whole-skill upload | Decision D4. The card keeps both |
| 11 | kit-m2 README: "Each file has a `.txt` copy" | Reworded: each loaded file and the fix rules handout have a `.txt` copy. The READMEs and the fallback texts have none |

## Verifier report

| # | Finding | What I did |
| --- | --- | --- |
| F1 | O.1 "a study from this year" | Changed to "a study from 2026" |
| F2 | 1.8 "Few enterprise teams do this today" has no source | Removed. Now "Your team may not use them." |
| F3 | O.2 "matched the human team well" and "checked every quote" go past S-B1 | Changed to "The AI's themes were all judged valid, and they overlapped with the human team's themes." and "the lead author checked each quote the AI picked against the transcript" |
| F4 | "not what the person said" counts cut-short quotes | Changed to "Almost 1 in 3 quotes was not word for word" (O.3 talk track and the O.2 POINT). The old course-open question about the hook line is closed |
| F5 | 1.2 "codes interviews much faster" conflicts with E12; E12 coded news articles | Changed to "It can code interviews faster." E12 line now says "coding news articles about nurses" |
| F6 | 1.2 "That takes days per study" rests on one vendor | Changed to "That can take days per study." |
| F7 | ChatGPT log save wording | Changed to "Open the old `problem-backlog` in the project sources list. Delete it. Add the new file" |
| F8 | Claude projects new version (beta) | Claude card note added: "Your project opens as one conversation with a Library? Tell the instructor." Decision D10 for the readiness checklist |
| F9 | Gemini: missing **Upload** click; **@** shortcut; Canvas note cited the wrong page | Gemini lab card step 1, fast-start row and build check step 3 now say **Add**, **files**, **Upload**. **/** (or **@**) everywhere. Canvas note cites answer 18560919 (gm-06). Gemini card header adds the dated Google blog (2026-09-30) for **/** |
| F10 | Claude Team and Enterprise toggle is set by the owner | Claude card note adds: "Team or Enterprise: ask your owner. It is in **Organization settings**, then **Capabilities**." Decision D14 |
| F11 | Gemini screen names have no dated doc | Decision D3 |
| F12 | Claude delete-a-file control has no doc | Kept the generic wording. Decision D8 (card test records it) |
| F13 | Copilot agent chat upload and new chat; ChatGPT new chat have no doc | Kept the generic wording and the paste backup. Decisions D8 and D9 |
| Section 5 | Platform matrix append changes a fingerprinted file | Decision D19. I did not edit `status.yaml` |

## Other changes

- "Questions for Dan" in `module.md` is now "Decisions for Dan": 19 decisions, D1 to D19, most important first, each with a recommended answer. `course-open.md` points to that list (D17 and D18 cover the open).
- Character counts after the revision (`wc -m`): brief v1 2,772; job card 1,194; code book 2,791; fallback m1 7,111 (budget 7,800); brief v2 2,920; fallback m1-v2 7,277; kit-m2 backlog 10,004. Every `.txt` copy matches its `.md` file (`cmp`).
- Script checks rerun: slide minutes 70 and 80 (16 slides), course open 25. No em or en dashes. No step or pass-condition sentence over 20 words. None of the banned terms appear.
