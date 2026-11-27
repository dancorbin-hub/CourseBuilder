# Revision notes: module 3 (revise once)

Module builder, 2026-11-27. Inputs: `consistency-report.md`, `verifier-report.md` and the coordinator's notes of 2026-11-27. I changed `module.md`, `card-test.md`, `kit/lab-3/README.md`, `kit/kit-m4/README.md` and `kit/kit-m4/problem-backlog.md` (and its `.txt` copy). I did not change the spec, the case, the research files, module 1 or module 2.

## Consistency report

| # | Severity | Finding | What I did |
| --- | --- | --- | --- |
| 1 | Major | Learner end state has no P10; kit-m4 has it | Chose option A, because it keeps the learner path the same. The kit-m4 README and the 3.17 talk track now say kit-m4 holds the case PM's decision (P10 added) and tell learners to add their own new tag the same way. B11 updated. New decision D2: option B (the log save card also loads the kit-m4 tag list) changes the learner path, so it waits for Dan |
| 2 | Major | Module 2 ChatGPT stretch line | Not touched. The coordinator fixed it in module 2 (commit 1360b2d) |
| 3 | Major | Run times disagree | Slide 3.5 now says to send week 1 by minute 1 of the slide and talk over the run. New cut-over cue: "If week 2 is not done at minute 6, open the rehearsal output and move on." The demo script asks you to time the rehearsal runs, and its step 4 recovery has the same cue. Card test: a demo rehearsal row (each run, slide 3.5 total, slide 3.14 length) and a "week 1 run, then week 2 run" minutes row on every platform. The rerun rule stays (D3 option B if over 3 minutes on 2 platforms) |
| 4 | Minor | Section 6 lists 3 pass items, the card 5 | Section 6 now lists the same 5 items, with the source of items 4 and 5 |
| 5 | Minor | 3 spec wordings not listed | Added as "Changes needing Dan's yes" rows 2 (rerun both weeks, if D3), 3 (after class, if D14) and 4 (ship before the test, if D1) |
| 6 | Minor | D1 option B incomplete | D1 now names the 5 places option B changes |
| 7 | Minor | No-license rerun does not resend the backlog | Same fix as verifier F10 |
| 8 | Minor | P04 willingness to pay clue differs from Part 4 | Now "1 account asks about a battery swap service (A-11, feedback)". Backlog is now 15,194 characters. Section 8, case note 8 and the kit-m4 README updated |
| 9 | Minor | "The Head of Product asks" | Now "one of the current market questions is" |
| 10 | Minor | Audit hint on 3.7 | Cut "It is short, and it is where new things show up." B5 notes it |
| 11 | Minor | Stretch step 4 has 4 actions | Replaced by the verifier F1 rewrite (6 steps) |
| Consider | Survey wave on Copilot and Gemini | No change. `stretch_scope` limits only the schedule and second-agent steps, as the module 1 screening stretch |
| Consider | 3.14 length | Card test demo rehearsal row now times the 3.14 talk track |
| Consider | 3.8 "top movers" claim | Reworded (verifier F6) |
| Consider | kit-m4 backlog size for module 4 | Case note 8 for the module 4 builder |
| Consider | Core message names the "no fit" rule before the lab | No change. It is spec text |

## Verifier report

| # | Finding | What I did |
| --- | --- | --- |
| F1 | Claude stretch steps skip labels and have several actions per step | Used the verifier's 6-step rewrite. I split the actions so each step has 1 action and 20 words or fewer: 1 **+** next to **Projects**, then **Import from project**. 2 pick the project, a folder, **Create**. 3 save the export in that folder. 4 **Scheduled tasks**, **New task**, **Set up manually**. 5 fill in name, prompt, **Weekly**, folder. 6 keep the default approval mode, **Save**. Card test rows name **Import from project**, **Create** and the approval mode. Steps 2 and 5 are one form each, the same way module 1 step 1 counts "add the kit" as one action |
| F2 | **New task** not documented inside a project | Added the card note: "No **New task** in the project? Select **Scheduled** in the left sidebar, then **New task**. Pick the project folder." New section 9 row. Card test row records which path shows the labels |
| F3 | "People stop reading" not in W4 or W5 | POINT cut to "Feedback arrives every day, and tagging it by hand is slow and inconsistent." The line is now a question to the room. Added to "Kept off the slides" |
| F4 | 3.4 states a 1-source claim as fact | Now "The risk is that the team that writes the most gets served first." The [IF ASKED] line stays |
| F5 | Hardware line has no verified source | Now "In hardware, install notes and technician notes can hold product feedback too", followed by the case design line |
| F6 | "Top movers" claim has no source | Now "A 'top movers' view lets a number decide what you see. This job does not." |
| F7 | 3 doc risks (new Claude experience, move to the cloud, Computer access) | Card note: "With a folder, the task runs only while..."; "Your company must allow Cowork and Computer access"; "Your screens look different (new Claude experience)? Stop the stretch and tell the instructor." Section 9 row adds the new Claude experience as a cause. 3 card test rows added (new experience, Pro folder option, cloud move after **Save**). D1 stays option A |
| F8 | Pass, note | No change |
| F9 | No vendor message limit for Copilot Chat | D5 (was D13) names the Support page. The section 9 row cites it. Matrix row mb-ui-16 is in "Changes needing Dan's yes" row 6 |
| F10 | No-license debrief rerun has no backlog, and the message is too long | The no-license box and the lab-3 README now send the backlog alone first at step 2 and again at the debrief rerun, then the exports in a second message. Largest message is 10,004 characters, under the 15,400 target. Card test rows for step 2, the rerun (18,877 in total) and the longest paste |
| F11 | ChatGPT card date | Now "seen 2026-11-27" |
| F12 | kit-m4 backlog size for module 4 | Case note 8 for the module 4 builder. No module 3 change |
| F13 | Pass | No change |
| Matrix and ledger proposals | cl-sc-07, cl-ui-11, mb-ui-16; W4, W5, W18 checked_on | Listed in "Changes needing Dan's yes" rows 6 and 7. Old row 3 (cl-sc-07 screen names) is now inside row 6 |

## Decisions renumbered

Open decisions are now D1 to D14, most important first. Map from the draft: D1 stays D1. New D2 (P10 end state). Draft D2 is D3, D3 is D4, D13 is D5, D4 is D6, D5 is D7, D6 is D8, D7 is D9, D8 is D10, D9 is D11, D10 is D12, D11 is D13, D12 is D14.

## Checks after the revision

- 17 slides, 60 minutes, 24 / 36 (40%). Slide minutes not changed.
- No em or en dashes. No banned terms.
- No step card or stretch sentence over 20 words. The standard data safety sentence is the one allowed exception (module 1 D15).
- Kit: every `.txt` copy matches its `.md` file. The only kit text change is the P04 cell in the kit-m4 backlog (15,176 to 15,194 characters) and the 2 READMEs. The fallback texts did not change (6,856 and 7,194).
