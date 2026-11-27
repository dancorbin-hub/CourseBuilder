# Stretch verification: schedule and second agent (Gate 2 decision 10)

- Course: market-research
- Spec key: `spec.yaml` > `stretch_verification` and `stretch_scope`
- Check date: 2026-11-27 (all rows)
- Role: Verifier. This is a doc check. It is not a test. The spec rule needs a dated vendor doc and a test.
- Files not changed: `spec.yaml`, `research/platform-matrix.yaml` and all other fingerprinted files.

## 1. Questions

1. Schedule: can the learner make the saved course agent run on a recurring schedule (for example a weekly feedback run), with no extra paid tool?
2. Second agent: can the learner run a second agent that takes the output of the first agent as input, in the same product?

Two kinds of second-agent hand-off are in the table:

- Automatic: one agent calls or receives work from the other agent.
- Manual: the learner downloads the output file of agent 1 and uploads it to agent 2. This uses only core path features (project or agent, file output, file upload).

## 2. Results

| Platform | Capability | Verdict | UI path | Limits | Source URL | Doc date | Check date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude | Schedule (Cowork scheduled task) | verified (doc) | Claude Desktop or web > Cowork > Scheduled (left sidebar) > New task (upper right) > Set up manually > enter task name, prompt, approval mode, frequency, model (optional), folder (optional) > Save. In a Cowork project: Projects > open the project > Scheduled tasks. Create a Cowork project from a chat project with Projects > + > Import from project | Pro, Max, Ultra, Team, Enterprise. Not Free. Frequency: hourly, daily, weekly, weekdays, manual. Each run is a new Cowork session. Tasks can use skills, plugins and connectors. A picked folder turns on "Require this computer": the computer must be awake and Claude Desktop open. Team and Enterprise: admin toggle for Cowork. New experience on Team and Enterprise needs "Chat and Cowork unified" | https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork | 2026-11-18 (page metadata dateModified). Projects page: https://support.claude.com/en/articles/14116274-organize-your-tasks-in-claude-cowork, 2026-11-12 | 2026-11-27 |
| Claude | Second agent, automatic (plugin agents in Cowork) | not verified | Customize > Plugins > Add > Create with Claude (or Create a plugin). Cowork "runs the plugin's agents" | Agents work in Cowork and Claude Code, not in chat. The doc says agents are "specialists Claude can delegate part of a task to". Claude decides when to delegate. The doc does not show that agent 2 reads the output file of agent 1. Plugin agents and hooks can run commands on the computer (data safety review needed) | https://claude.com/docs/plugins/overview | 2026-11-12 (page metadata dateModified) | 2026-11-27 |
| Claude | Second agent, manual file hand-off | verified (doc, by existing rows) | Build a second project (Projects > + New Project). Download the output file of agent 1. Upload it to agent 2 in the chat or project knowledge | Uses verified rows cl-pj-01, cl-fo-06 and cl-ui-09. No new feature. Rollout risk: new version of projects (cl-pj-11, not verified) can change screen names | platform-matrix.yaml rows cl-pj-01, cl-fo-06, cl-ui-09 | see matrix | 2026-11-27 |
| ChatGPT | Schedule (scheduled tasks) | verified (doc), poor fit | Scheduled (sidebar) > "Schedule a task" input. Or ask ChatGPT in a chat, for example "every Monday at 9, ..." | Free, Go, Plus, Pro, Business, Enterprise, Edu. Active tasks: 3 (Free, Go), 5 (Plus), 10 (Business, Edu), 15 (Pro, Enterprise). Free: at most once a day. A task made in a project "cannot access uploaded files or files stored in that project". GPTs are not supported. The page does not mention skills or workspace agents. So a scheduled run cannot read the tag list, the brief in project files or a new feedback file without a connector | https://help-lb.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt | undated in metadata. Page shows "Updated: 18 days ago" (approx 2026-11-09) | 2026-11-27 |
| ChatGPT | Schedule (workspace agent "Add schedule") | verified (doc), fails "no extra paid tool" | Agents > Create (or Browse templates) > Build this agent > Create. Then on the ChatGPT channel page: Add schedule > channel, schedule type, "run every" > Add schedule | Business and Enterprise only (Enterprise: off by default, admin turns it on). Credit-based pricing since 2026-05-06. A typical run uses 5 to 25 credits from the shared pool. More use needs purchased credits | https://help-lb.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business ; pricing: https://openai.com/index/introducing-workspace-agents-in-chatgpt/ ; credits: https://help-lb.openai.com/en/articles/11481834-chatgpt-rate-card-business-enterprise-edu-credit-based-pricing | Help: undated ("Updated: 4 days ago", approx 2026-11-23). Blog: 2026-04-22. Rate card: undated ("Updated: 34 minutes ago") | 2026-11-27 |
| ChatGPT | Second agent, automatic | not verified | none found | Workspace agents help page, Academy page and launch post do not say that one agent can call another agent or use its output. Skills page says ChatGPT can use "one or more skills", but skills are Business, Enterprise, Healthcare and Edu only, and a skill is not a second agent | https://help-lb.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business ; https://openai.com/academy/workspace-agents | approx 2026-11-23 ; 2026-04-22 | 2026-11-27 |
| ChatGPT | Second agent, manual file hand-off | verified (doc, by existing rows), file output only partly verified | Build a second project (New project). Download the output file of agent 1. Upload it to agent 2 | Uses cg-01 and cg-ui-09 (verified) and cg-08 (partly verified: file types and plans not fully named) | platform-matrix.yaml rows cg-01, cg-ui-09, cg-08 | see matrix | 2026-11-27 |
| Copilot | Schedule (agent builder workflow) | not verified | Message Center text: agent builder menu > "Create a workflow for this agent" or "Manage workflows" > "Create a workflow to prompt your agent" > Prompt and schedule | Microsoft 365 Copilot (Premium) license. Hourly, daily, weekly, monthly, yearly. Runs only for the creator. Not shared with the agent. Does not run for draft or unpublished agents. Rollout mid-November to mid-December 2026, so it is still rolling out. Only sources are a third-party Message Center mirror and a Microsoft Korea GitHub page. No Microsoft Learn or support page found. The Learn page and the support page for scheduled tasks do not say that a schedule can call an agent builder agent | https://mc.merill.net/message/MC1302906 (mirror, not a vendor doc) ; https://microsoft.github.io/mwkorea/copilot/CopilotAgentBuilderScheduledPrompts/ ; https://learn.microsoft.com/copilot/microsoft-365/scheduled-prompts ; https://support.microsoft.com/en-us/topic/schedule-your-most-used-copilot-prompts-29dfd5fb-211a-4515-88a6-730b8074e489 | MC1302906 v3 2026-10-30. Korea page 2026-10-14. Learn 2026-11-11. Support 2026-11-18 (ms.date 2026-11-04) | 2026-11-27 |
| Copilot | Second agent (automatic or in agent builder) | not available | none in agent builder | No doc says an agent builder agent can call another agent. Routing rules send a prompt from Copilot Chat to one agent. They are admin-set and in private preview. Workflows Agent needs the Frontier program and links to Power Platform (out of scope). Manual file hand-off is possible with mb-11 (verified) and mb-ui-14 (partly verified), but stretch_scope keeps Copilot on the core path | https://learn.microsoft.com/en-us/microsoft-365/copilot/agent-essentials/copilot-agent-orchestration ; https://support.microsoft.com/en-us/topic/8c6aba25-db31-443d-8319-bc79747b280a | Routing: 2026-10-31 (updated_at). Workflows: 2026-08-14 (metadata) | 2026-11-27 |
| Gemini | Schedule (Gemini Spark tasks, can call a skill) | not available (Workspace) | gemini.google.com > Scheduled (sidebar) > Create a scheduled task > name, Plan, when to run > Create. Type "/" to pick a skill | Personal accounts only. The page says it "isn't available if you sign in with a work or school Google Account". 18+. Active schedules 50 (Pro, Ultra) or 10 (Plus, no subscription). Free and Plus: once a day in a window. A personal account with work data breaks the lab data safety note | https://support.google.com/gemini/answer/17094710?hl=en | undated | 2026-11-27 |
| Gemini | Schedule (scheduled actions in chat) | not verified for the course agent | gemini.google.com > enter the prompt with when and how often > Submit | Personal accounts and qualifying Workspace editions. 10 active schedules. History must be on. The page does not say that a scheduled action can use a skill or uploaded files | https://support.google.com/gemini/answer/16316416?hl=en | undated | 2026-11-27 |
| Gemini | Second agent | not available | none found | No doc says a skill can call another skill or take its output. Skills Workspace rollout post (2026-10-13, update 2026-11-09) names no chaining. Manual file hand-off is possible with gm-09 (verified in the Gemini app, not verified for skills), but stretch_scope keeps Gemini on the core path | https://workspaceupdates.googleblog.com/2026/10/an-update-on-launch-of-skills-in-gemini-app-and-workspace.html | 2026-10-13 (update 2026-11-09) | 2026-11-27 |

Age flag: no source is older than 12 months. The oldest dated vendor source is the OpenAI launch post (2026-04-22). Four sources are undated or show only a relative date (Gemini 17094710 and 16316416, the OpenAI help pages). Dan decides if undated pages are acceptable (same issue as module 1 verifier report F11).

## 3. Differences from the spec expectation

| Spec expectation | Finding | Why it matters |
| --- | --- | --- |
| Schedule: likely yes for Claude | Yes by doc | Matches. Needs a test |
| Schedule: likely yes for ChatGPT | The feature exists, but a scheduled task in a project cannot read project files | The weekly run cannot read the tag list or the saved backlog. New feedback cannot reach the task without a connector. Workspace agents can schedule, but only on Business or Enterprise with credits |
| Second agent: likely yes for Claude and ChatGPT | Automatic hand-off: not verified on either. Manual file hand-off: yes on both, with core features | "Second agent" on the module 4 card must mean a second project that reads an uploaded output file, unless Dan's test proves Claude plugin agents |
| Copilot: core path only | Confirmed. Agent builder schedule is still rolling out and has no Microsoft-hosted public doc | Matches |
| Gemini: core path only | Confirmed for Workspace accounts | Matches |

## 4. Recommendation

### Module 3 (schedule stretch step)

| Card | Schedule stretch step | Condition |
| --- | --- | --- |
| Claude | Yes, if Dan's test passes | Cowork project imported from the course project, with a local folder for the weekly feedback files and the log. The card says: paid plan, Claude Desktop open, computer awake |
| ChatGPT | No, at this time | Put it back only if Dan's test finds an input path with no connector that the scheduled task can read. Otherwise the card uses the standard "not available" line |
| Copilot | No | Card says: "The schedule and second-agent stretch steps are not available on this platform in this course." Recheck mb-06 after mid-December 2026 |
| Gemini | No | Same card line. Spark works only on personal accounts |

### Module 4 (second-agent stretch step)

| Card | Second-agent stretch step | Condition |
| --- | --- | --- |
| Claude | Yes, manual hand-off: build the map job as a second project and upload the win/loss output file | Uses verified rows. Plugin agents stay out until Dan tests them and a data safety review passes |
| ChatGPT | Yes, manual hand-off, same as Claude | Uses cg-01 and cg-08. cg-08 is partly verified, so Dan's test must confirm the file download |
| Copilot | No (stretch_scope) | Manual hand-off is technically possible. Changing this needs Dan's yes, because spec.yaml is approved |
| Gemini | No (stretch_scope) | Same as Copilot |

### Module 5

The module 5 stretch is "share the agent with a stakeholder", not a second agent. No second-agent step is in the spec for module 5. Do not add one.

## 5. Hands-on tests Dan still needs (a doc check is not a test)

1. Claude schedule: import the course project into a Cowork project. Add a weekly task that reads the week 2 feedback file from the folder. Confirm the run reads the tag list and the week 1 backlog and writes the new backlog file.
2. Claude schedule: confirm the task runs on a Pro plan, and record what happens when the computer sleeps.
3. Claude manual hand-off: run the win/loss job, download the output, upload it to a second project, run the map job. Confirm each map entry links to a deal id or interview id.
4. ChatGPT manual hand-off: same as test 3. Confirm the output downloads as a file (cg-08).
5. ChatGPT schedule (optional): find if any no-connector input path works for a scheduled task. If none, keep ChatGPT off the module 3 schedule step.
6. Claude plugin agents (optional): build one plugin agent for the map job. Confirm it reads the win/loss output and record which commands it runs on the computer.
7. Copilot: after mid-December 2026, check if "Create a workflow for this agent" shows in agent builder. Find a Microsoft Learn or support page for it. Until then, keep the core path.

## 6. Gaps

- No Microsoft-hosted public doc for agent builder scheduled workflows (MC1302906). Message Center needs a tenant admin login.
- No vendor doc for automatic agent-to-agent hand-off in Claude chat, ChatGPT, Copilot agent builder or Gemini skills.
- Gemini schedule pages have no date.
