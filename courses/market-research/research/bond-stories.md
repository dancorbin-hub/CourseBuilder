# Bond story candidates: Advanced AI for Market Research

- Course id: `market-research`. Written 2026-11-21 for Dan.
- Purpose: propose a bond story to open the class. PRD decision 39 asks for 3 to 4 candidates. Dan picks one at Gate 1.
- Method: 6 candidates. Each source was opened on 2026-11-21. The 4 recommended candidates are marked "Yes".
- Checks done:
  - Pragmatic deck text (BPW-AI, CAW-AI, PDW-AI, PRC, PRW-AI, MKT 2026) has no match for any candidate name. PRC uses Netflix and Blockbuster (pricing). It is not a candidate.
  - No candidate is mainly about competitive analysis, personas or pricing.
  - Existing series stories (Juicero, WeWork, Jitterbug, maxed-out employees) are not reused.

## 1. Summary

| # | Candidate | Type | Year | Hook line (short) | Sets up | Main risk | Recommend |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AI quotes in health interviews (JAMIA study) | 2026 finding | 2026 | "Almost 1 in 3 quotes the AI gave back was not what the person said." | Insight log, quote checks, flag report, audit | Health care setting. Learners may say "that is not my data" | Yes, first choice |
| 2 | Synthetic poll flattens opinion (Pew) | 2026 finding | 2026 | "Nearly half the questions had an answer that no AI respondent chose." | Synthetic respondents, market visits, one loud voice | Political survey topics. The model tested is Claude | Yes |
| 3 | Deloitte Australia report with a made-up court quote | AI-era story | 2025 | "One reader checked the footnotes. The firm paid money back." | Unchecked AI output, invented quotes, audit before hand-off | Older than 12 months. Real firm: keep to reported facts | Yes |
| 4 | Febreze: the woman with nine cats | Classic story | 1996 to 1998 | "She lived with nine cats and said, 'They hardly smell at all!'" | Market visits, watch what buyers do, research the lab missed | Old. Well known. Facts rest on one reporter | Yes |
| 5 | Amazon Fire Phone: built for the boss | Classic hardware story | 2014 | "Engineers said they designed for him instead of actual customers." | Building without the market, opinion against evidence | Second phone story in the series (Jitterbug). Key quote has one root source | No, backup |
| 6 | Humane AI Pin | AI-era hardware story | 2024 to 2025 | "230 million dollars raised. Devices turned off after less than a year." | Building without the market, AI hype | Same pattern as Juicero. No source shows a research gap | No |

## 2. Recommendation

1. Use candidate 1 or 2 if Dan wants a finding. Both are 2026 primary sources. Both hit the core message: AI makes research faster, and the work moves to checking.
2. Use candidate 3 if Dan wants a story with a company name. It is the strongest "nobody checked" story. It is 13 months old, so it needs Dan's yes (research rule 5).
3. Use candidate 4 if Dan wants a classic story. It is the best "go and see the buyer" story. It sets up market visits, not AI checks.
4. My pick: candidate 1. It is the closest match to the lab 1 work (insight log from interviews). It names the exact errors the course teaches learners to catch.
5. Do not combine candidate 2 with the synthetic respondent slide in a module. Pick one place for the Pew finding (E16 is already in the evidence ledger). House rule 9 forbids a repeated slide.

## 3. Detail per candidate

### Candidate 1. AI quotes in health interviews (JAMIA, 2026)

- **Story:**
  1. In 2026 a research team gave 122 interview and consultation transcripts from heart failure patients to an LLM-assisted workflow.
  2. The AI found valid themes that matched the human team well, but only 68% of its quotes were word for word: 20% were paraphrased, 3% cut short and 9% partly or fully made up.
  3. The authors said human checks of each quote stayed essential, and that LLMs are "analytic partners rather than autonomous coders".
- **Hook line:** "The themes were good. But almost 1 in 3 quotes the AI gave back was not what the person said. Would your stakeholders know?"
- **Sets up:** interview synthesis into the insight log (mr-wf-01), quote checks in the brief, the flag report, the audit. Core message: the work moves to checking.
- **Why PMs relate:** PMs paste quotes into decks and PRDs every week. A reworded quote that sounds right is the error nobody sees.
- **Risks:**
  - Health care data. Use it to make the data safety point: the team worked in a HIPAA-compliant setup.
  - Some PMs may say "my interviews are not clinical". Answer: the error comes from the model, not the topic.
  - Not overused. Published 2026-08-06.
- **Sources:** S-B1 (primary, statistic). S-B2 (secondary, vendor, for context only).
- **Status:** verified. Abstract and figures read on the journal page.

### Candidate 2. Synthetic poll flattens opinion (Pew Research Center, 2026)

- **Story:**
  1. Pew asked an AI model (Claude Opus 4.6, the best of the models tested) to answer three real 2026 surveys as "digital twins" of real panel members.
  2. In 47% of the synthetic questions, at least one answer option got no AI respondent at all; in the human surveys, this happened on no question.
  3. On one question, the AI said 98% of Americans think China gains more from US trade: 56 points above the real share, which erased everyone who was unsure or disagreed.
- **Hook line:** "Nearly half the questions had an answer that no AI respondent chose. Real people chose all of them. The minority view is where your next insight hides."
- **Sets up:** synthetic respondents flatten opinion; AI never replaces talking to real buyers (market visits); one loud voice against the real spread of opinion.
- **Why PMs relate:** vendors now sell synthetic personas and AI-moderated panels. PMs are asked "why not just ask the AI?"
- **Risks:**
  - Survey topics are political. Use the 47% figure and the trade example. Do not use the questions about named politicians.
  - The model tested is Claude, the course core platform. Say so openly. It makes the point stronger: the best model still flattens opinion.
  - Already in the evidence ledger (E16). Use it once: as the bond story or as a module slide, not both.
  - Published 2026-09-30. Not overused yet.
- **Sources:** S-P1 (primary, statistic).
- **Status:** verified.

### Candidate 3. Deloitte Australia report with a made-up court quote (2025)

- **Story:**
  1. The Australian government paid Deloitte AU$440,000 for an independent review of a welfare compliance system.
  2. A University of Sydney academic found references to reports that do not exist and a made-up quote from a federal court judgment.
  3. Deloitte disclosed that it had used a GPT-4o tool chain, removed more than a dozen bad references and agreed to repay the last payment of the contract.
- **Hook line:** "A Big Four firm delivered a report with a court quote that a judge never said. One reader checked the footnotes. Who checks yours?"
- **Sets up:** invented quotes and sources, unchecked AI output, the PM audit, hand-off rules (what leaves the agent only after a check).
- **Why PMs relate:** PMs send research summaries to executives. One wrong quote can discredit the whole recommendation.
- **Risks:**
  - Age: October 2025, 13 months old. Flag for Dan (research rule 5).
  - Real firm. Keep to reported facts. Say that the department kept the recommendations unchanged.
  - Fairly well known in AI talks. Moderate overuse risk.
  - Welfare policy topic. Do not discuss the policy itself.
- **Sources:** S-D1 (AP), S-D2 (The Register). Independent reports.
- **Status:** verified.

### Candidate 4. Febreze: the woman with nine cats (1996 to 1998)

- **Story:**
  1. In the mid-1990s P&G had a spray that removed bad smells, and it marketed Febreze to people with smelly homes, but sales started small and got smaller.
  2. Researchers went into homes and met a woman near Phoenix with nine cats who said, "They hardly smell at all!" People stop noticing smells they live with.
  3. Hours of video of people cleaning showed the real use: a final spray after cleaning, so P&G relaunched it that way in 1998 and sales doubled in two months.
- **Hook line:** "The lab said it worked. The ads said who needed it. Only a home visit showed that the people who needed it could not smell the problem."
- **Sets up:** AI never replaces talking to real buyers (market visits); what buyers say against what they do; the course rule that the agent works only on conversations a person held.
- **Why PMs relate:** every PM has a launch that made sense on paper. Hardware and consumer goods PMs know the gap between lab and home use.
- **Risks:**
  - Age: 1996 to 1998, reported 2012. Flag for Dan.
  - Well known through Duhigg's "The Power of Habit". Some learners will know it.
  - All accounts trace back to one reporter (Duhigg). Under research rule 2, this counts as one source. I found no P&G account with the home visit details (the WARC item confirms a weak launch and a rethink only).
  - It is also a habit and positioning story. Keep the focus on the home visit.
- **Sources:** S-F1 (NYT, Duhigg), S-F2 (NPR interview with Duhigg, same root), S-F3 (Business Insider India, repeats Duhigg), S-F4 (WARC, P&G executive, weak launch only).
- **Status:** partly verified (one root source for the home visit details).

### Candidate 5. Amazon Fire Phone: built for the boss (2014)

- **Story:**
  1. In 2014 Amazon launched the Fire Phone at the iPhone price, with a 3D screen effect that tracked the user's head.
  2. Engineers told Fast Company that Jeff Bezos acted as the phone's product manager and that they were "constantly designing for him instead of actual customers".
  3. Within months the price fell to 99 cents, and Amazon took a 170 million dollar write-down, with about 83 million dollars of unsold phones.
- **Hook line:** "Engineers said they were designing for him instead of actual customers. Today the 'him' could be an AI that sounds just as sure."
- **Sets up:** building without the market; an opinion that sounds certain replaces buyer evidence. Hardware example.
- **Why PMs relate:** every PM has built a HiPPO feature (the highest paid person's opinion).
- **Risks:**
  - Age: 2014. Flag.
  - A second phone story in the series (Build uses Jitterbug).
  - The "designing for him" quote rests on one report (Fast Company, Austin Carr, January 2015). Business Insider repeats it.
  - Names a living executive. Keep to the reported quote.
  - The link to AI is weak. It is mainly a product strategy story.
- **Sources:** S-A1 (Fortune and TIME, financial facts and "solving problems that nobody had"), S-A2 (Business Insider India, repeats Fast Company), S-A3 (Fast Company original; body text not fully readable).
- **Status:** partly verified. Financial facts verified. The key quote has one root source.

### Candidate 6. Humane AI Pin (2024 to 2025)

- **Story:**
  1. Humane raised more than 230 million dollars and sold the AI Pin for 699 dollars as a smartphone replacement.
  2. Reviewers called it slow and unreliable with no advantage over a phone, and returns reportedly passed sales in summer 2024.
  3. In February 2025 HP bought the assets for 116 million dollars, and the devices stopped working on 28 February.
- **Hook line:** "230 million dollars of AI, and the buyer's question was still: what can it do that my phone cannot?"
- **Sets up:** building without the market in the AI era.
- **Why PMs relate:** many PMs are under pressure to "add AI" without a buyer problem.
- **Risks:**
  - Same pattern as Juicero (hyped, funded hardware that failed). Too close to the Foundations story.
  - No source I opened shows how Humane did or did not research its market. The "no market" claim is an inference.
  - Age: February 2025. Flag.
  - It does not teach the course core: checking AI research output.
- **Sources:** S-H1 (TechCrunch), S-H2 (Fortune).
- **Status:** verified for facts. Not verified for the "no market research" angle.

## 4. Rejected ideas (not researched in depth)

| Idea | Reason |
| --- | --- |
| New Coke | Very overused. It is also about brand and taste tests more than research method |
| Netflix price change | Used in Pragmatic PRC deck. Pricing course |
| METR developer study (AI made developers slower) | Published 2025. Statistics must be 2026 or later. METR is named in PRC and MKT deck text |
| Chicago Sun-Times AI reading list with fake books (2025) | Weaker than Deloitte for a B2B room. Same lesson |
| US government report with fake citations (2025) | Politically charged |
| Klarna AI customer service reversal | About support staffing, not market research |

## 5. Sources

All sources opened on 2026-11-21. "Vendor" = the publisher sells a product in this area.

| Id | Source | Date | Type | Used for | Age flag |
| --- | --- | --- | --- | --- | --- |
| S-B1 | Bang S.H. et al., "Developing and evaluating human-led and large language model-assisted hybrid deductive-inductive workflows for qualitative analysis", JAMIA 33(11):2079 to 2091, doi 10.1093/jamia/ocag123. https://academic.oup.com/jamia/article/33/11/2079/8753705 | 2026-08-06 | Primary study, non-vendor | Candidate 1 figures | No |
| S-B2 | Qualitati blog, "How Often Do LLMs Fabricate Interview Quotes? 2026 Study". https://qualitati.com/blog/llm-hallucinated-quotes-qualitative-analysis-2026 | 2026-08-21 | Secondary, vendor | How the study was found. Do not cite in class | No |
| S-P1 | Chapekis A. et al., "How well synthetic polls capture the diversity of public opinion", Pew Research Center Data Labs. https://www.pewresearch.org/data-labs/2026/09/30/how-well-synthetic-polls-capture-the-diversity-of-public-opinion/ | 2026-09-30 | Primary study, non-vendor | Candidate 2 figures | No |
| S-D1 | Associated Press, "Deloitte to partially refund Australian government for report with apparent AI-generated errors" (via CTV News). https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | News | Candidate 3 | Yes (13 months) |
| S-D2 | The Register, "Deloitte refunds Aussie gov after AI fabrications slip into $440K welfare report". https://www.theregister.com/2025/10/06/deloitte_ai_report_australia/ | 2025-10-06 | News | Candidate 3: academic who found errors, GPT-4o disclosure, recommendations unchanged | Yes (13 months) |
| S-F1 | Duhigg C., "How Companies Learn Your Secrets", New York Times Magazine (PDF copy). https://moglen.law.columbia.edu/twiki/pub/CompPrivConst/HowCompaniesLearnOurConsumingSecrets/How_Companies_Learn_Your_Secrets_-_NYTimes.com.pdf | 2012-02-16 | News feature | Candidate 4: nine cats, video, 1998 relaunch, sales doubled | Yes (old story) |
| S-F2 | NPR interview with Charles Duhigg, transcript. https://www.npr.org/transcripts/147296743 | 2012 | Interview, same root as S-F1 | Candidate 4: flop, people stop noticing smells | Yes |
| S-F3 | Damani A., "How the world's best marketer got it wrong, but eventually got it right", Business Insider India. https://www.businessinsider.in/How-the-worlds-best-marketer-got-it-wrong-but-eventually-got-it-right/articleshow/55725321.cms | Not shown (about 2016) | Opinion, repeats Duhigg | Candidate 4: 1996 launch | Yes |
| S-F4 | WARC, "Former P&G exec reveals Febreze rethink". https://www.warc.com/newsandopinion/news/former_pg_exec_reveals_febreze_rethink/38210 | 2017-02-16 | Trade news | Candidate 4: weak launch and rethink only | Yes |
| S-A1 | Fortune (TIME), "4 reasons Amazon's Fire Phone was a flop". https://fortune.com/2014/10/24/4-reasons-amazons-fire-phone-was-a-flop/ | 2014-10-24 | News | Candidate 5: write-down, inventory, price | Yes |
| S-A2 | Business Insider India, "The Amazon Fire Phone shows what happens when the CEO gets too involved in product design". https://www.businessinsider.in/The-Amazon-Fire-Phone-Shows-What-Happens-When-The-CEO-Gets-Too-Involved-In-Product-Design/articleshow/45783982.cms | About 2015-01 | News, repeats S-A3 | Candidate 5: "designing for him" quote | Yes |
| S-A3 | Carr A., "The Inside Story Of Jeff Bezos's Fire Phone Debacle", Fast Company. https://www.fastcompany.com/3039887/amazon | 2015-01-06 | News | Candidate 5: write-down, 99 cent price. Full text not readable by the fetch tool | Yes |
| S-H1 | TechCrunch, "Humane's AI Pin is dead, as HP buys startup's assets for $116M". https://techcrunch.com/2025/02/18/humanes-ai-pin-is-dead-as-hp-buys-startups-assets-for-116m | 2025-02-18 | News | Candidate 6 | Yes (21 months) |
| S-H2 | Fortune, "HP Humane deal: AI Pin shutting down". https://fortune.com/2025/02/19/hp-humane-deal-ai-pin-shutting-down/ | 2025-02-19 | News | Candidate 6 | Yes (21 months) |

## 6. Open items for Dan

1. Pick one bond story at Gate 1.
2. If you pick candidate 3, 4, 5 or 6, confirm the old source can stay (research rule 5).
3. If you pick candidate 4, accept one root source (Duhigg) or ask for a P&G source.
4. If you pick candidate 2, decide where the synthetic respondent caution goes in module 1, so the Pew finding is not shown twice.
