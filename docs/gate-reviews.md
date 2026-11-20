# Gate reviews in Claude Docs

Dan reviews each gate packet as a Claude Doc (PRD decision 22). This file says how a gate review works and how to test it on Dan's computer.

## How a gate review works

1. The stage skill writes the packet to the course files in the repo.
2. The skill publishes the packet as a Claude Doc and records the doc link in `courses/<course>/status.yaml`.
3. Dan reads the doc and adds comments. Dan can also edit text in place.
4. Dan tells Claude Code: "Read my comments on the Gate N doc."
5. Claude Code reads the comments and edits, applies them to the repo files (not to the doc), and replies in each comment thread.
6. Dan says "Gate N approved." Claude Code sets the gate to `approved` with the date, and records fingerprints of the approved items.

The repo is the source of truth. The doc is a view for review.

## Phase 0 test: does it work from Claude Code on Dan's computer?

The PRD lists this as a risk: Claude Docs may not be reachable from Claude Code on Dan's computer. The test proves the full loop before Phase 1 depends on it.

| # | Step | Pass if |
| --- | --- | --- |
| 1 | Claude Code makes a Claude Doc | The doc opens in the browser |
| 2 | Dan adds 2 comments and 1 edit in the doc | Saved in the doc |
| 3 | Claude Code reads the comments and the edit | It quotes all three correctly |
| 4 | Claude Code replies in one comment thread | Dan sees the reply in the doc |
| 5 | Claude Code writes the result to `logs/gate-test-result.md` | File has date, machine and pass or fail for steps 1 to 4 |

### How Dan runs it

1. Open a terminal in the CourseBuilder folder on your computer.
2. Start Claude Code: type `claude`.
3. Type `/gate-docs-test`.
4. Follow the prompts. The test takes about 10 minutes.

### Result so far

| Date | Where | Result |
| --- | --- | --- |
| 2026-11-19 | Claude Code in the cloud (claude.ai project thread) | Steps 1 and 3 pass. The worked example row doc was made and read from Claude Code |
| 2026-11-20 | Claude Code in the cloud (claude.ai project thread) | Steps 2 to 4 pass. Dan commented on the row doc. Claude Code read the comment word for word and replied in its thread. Cloud test: pass |
| | Claude Code on Dan's computer (VS Code extension) | Not run yet. Needed only if Dan works from his computer |

### If the test fails

1. Check that you signed in to Claude Code with your claude.ai account (`/login`). The Claude Docs connector comes from claude.ai.
2. Type `/mcp` in Claude Code. Look for the Claude Docs connector in the list.
3. If it is still not there, use the fallback: each gate packet is a Word file in `courses/<course>/build/gates/`. Dan adds Word comments. Claude Code reads them with the docx skill.
