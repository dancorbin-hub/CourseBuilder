# Bond story candidates: Advanced AI for Product Strategy and Planning

- Course id: `product-strategy-and-planning`. Written 2026-11-22 for Dan.
- Purpose: propose a bond story to open the class (PRD decision 39). Dan picks one at Gate 1.
- Method: 6 candidates. 14 of 15 page fetches used. Other facts come from search result titles and summaries. The status line of each candidate says what was opened.
- The workflow rows are written in parallel. So the core messages below come from the scope in `stage-1-inputs.md`, not from the rows.

## Core messages the story must set up

| # | Core message | Workbook skill |
| --- | --- | --- |
| M1 | Strategy is a forced choice that stays human. AI makes plausible plans, scores and business cases fast. The PM's job moves to checking evidence and assumptions | 2.1 Strategy Alignment, 2.2 Opportunity Prioritization |
| M2 | A fast, confident number or plan is not a validated one (false precision, circular sources, anchoring on a score) | 2.2, 2.3 Business Case Development |
| M3 | The roadmap is direction, not a promise. AI must not turn uncertain direction into commitments | 2.4 Product Vision and Roadmap |

## Checks done

- Pragmatic deck text checked for story names: Focus 28.01, Build 28.01, PRC, MKT 2026, BPW-AI, CAW-AI, PDW-AI, PRW-AI and Dan's AI Agents deck.
  - Focus opens with WeWork. It does not use Kodak, Blockbuster, Nokia or Intel's memory exit.
  - PRC uses Netflix and Blockbuster, Ron Johnson at JCPenney, the first iPhone price cut and AMC popcorn. None is a candidate.
  - No candidate name below appears as a story in any deck.
- Not reused: Juicero, WeWork, the Jitterbug phone, the "employees maxed out" finding, and all 6 Market Research candidates (JAMIA quotes, Pew synthetic polls, Deloitte Australia, Febreze, Amazon Fire Phone, Humane AI Pin).
- No story is told as the instructor's own experience (decision 43). Each hook line is about the company or the study.

## 1. Summary

| # | Candidate | Type | Year | Hook line (short) | Sets up | Main risk | Recommend |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | "Trendslop": LLMs give every company the same strategy (HBR) | 2026 finding | 2026 | "7 models, 15,000 runs, and almost always the same trendy answer." | M1, M2. Strategy context in the agent brief, checks against your own strategy | No percentages in the sources I could open. The full HBR article is paywalled | Yes, first choice |
| 2 | Apple's personal Siri: shown, advertised, delayed, 250 million dollar settlement | AI-era story, hardware | 2024 to 2026 | "They put a feature that did not exist yet into the ads. It cost 250 million dollars." | M3. Direction against commitment, hand-off rules before a roadmap leaves the team | Overused in tech talks. Legal: settlement with no admission of wrongdoing | Yes |
| 3 | Commonwealth Bank: the AI business case that was wrong in 4 weeks | AI-era story, FinTech, internal operations | 2025 | "The bank said the bot cut call volumes. The calls went up." | M2, M1. Assumptions in a business case, check the claim against data | Job cuts and a union: sensitive. 15 months old | Yes |
| 4 | Intel leaves memory chips: "What would the new guy do?" | Classic story, hardware | 1984 to 1985 | "If the board fired us, what would the new CEO do?" | M1. A forced choice against the data you love, sunk cost | Old (40 years). Known to strategy readers | Yes, classic option |
| 5 | Executives' AI forecast: 0.2% so far, 0.6% expected (NBER Firm Data on AI) | 2026 finding | 2026 | "Three years gave 0.2%. The next three are expected to give three times that." | M2. Forecasts in business cases, AI unit economics | Close in theme to the "employees maxed out" finding. Paper revised in October 2026 | No, backup |
| 6 | Sonos app rebuild breaks a hardware company | AI-era timeframe, hardware (not an AI story) | 2024 to 2025 | "A 20 to 30 million dollar fix, two launches held back, and a CEO gone." | M3. Shipping on a date the product was not ready for | Not about AI. The "deadline drove it" angle is not verified | No, backup |

## 2. Recommendation

1. **First choice: candidate 1 (Trendslop).** It is 2026, from strategy researchers, and it is exactly M1. It gives the course its reason to exist: the agent is only as good as the strategy context the PM gives it and the checks the PM sets.
2. **Candidate 2 (Apple Siri)** if Dan wants a company name. It is the clearest M3 story in the AI era. It is hardware. It is recent (settlement terms live in May 2026).
3. **Candidate 3 (Commonwealth Bank)** if Dan wants a business case story. It is internal operations in FinTech, a priority gap area. Keep it to the business case, not to the job cuts.
4. **Candidate 4 (Intel)** if Dan wants a classic story. It is the best "forced choice" story I found, and it is hardware.
5. Do not pick candidate 1 if the module 1 lab already uses the trendslop finding as a slide. House rule 9 forbids a repeated slide. Use it once.
6. Candidates 1 and 4 combine well in a talk track: Intel shows the human forced choice, and trendslop shows why AI will not make it for you. Dan decides if the opening has room for two.

## 3. Detail per candidate

### Candidate 1. "Trendslop": LLMs give every company the same strategy (2026)

- **Story:**
  1. In 2026 researchers from Esade, the University of Sydney and NYU Stern asked seven leading LLMs, including GPT-5, Claude, Gemini and Grok, for strategic advice across about 15,000 simulations and scenarios.
  2. They tested hard trade-offs, for example long-term against short-term growth, and automating against augmenting workers' jobs.
  3. The models almost always picked the same trendy option, whatever the context, and the authors named this "trendslop": advice that sounds tailored but steers every company to the same small set of management trends.
- **Hook line:** "Researchers asked seven AI models for strategy advice 15,000 times. The models almost always gave the same trendy answer, whatever the company. If your competitors ask the same model, whose strategy is it?"
- **Sets up:**
  - M1: strategy is a forced choice that stays human. The authors say leaders should use LLMs to expand options, not to make the choice.
  - M2: an answer that sounds tailored is not the same as an answer that fits.
  - Course design: the agent brief holds the company's own strategy and evidence. Checks test each output against the Strategy Matrix, not against what sounds modern. A possible planted error: a generic "trend" recommendation that ignores the case company's stated strategy.
- **Why PMs relate:** PMs now get strategy drafts from AI and from executives who used AI. Many have seen the same buzzwords in three plans in one quarter.
- **Risks:**
  - The open sources give no percentages. "Almost uniformly" is the authors' words. Do not invent a number. If Dan wants a number, someone with HBR access must read the full article.
  - The models tested include Claude, the course core platform. Say so openly. It makes the point stronger.
  - Published 2026-03-16. Not overused yet. Media coverage grew in April 2026, so some learners may know the word.
  - No political or legal risk.
- **Sources:** S-T1 (primary, HBR), S-T2 (NYU Stern summary, author's school), S-T3 (Fortune via Yahoo Finance, independent report with the 7 models and 15,000 simulations).
- **Status:** verified for the finding, the authors, the date, the model count and the simulation count. Not verified: per-trade-off percentages (paywall).

### Candidate 2. Apple's personal Siri: shown, advertised, delayed, settled (2024 to 2026)

- **Story:**
  1. At WWDC in June 2024 Apple showed a more personal, AI-powered Siri, and from September 2024 it used those features in iPhone 16 ads and videos.
  2. In March 2025 Apple delayed the features and pulled the ads, and a class action said Apple sold phones "with features that did not exist or were materially misrepresented".
  3. In 2026 Apple agreed to pay 250 million dollars to settle (25 to 95 dollars per eligible iPhone), with no finding of wrongdoing, and as of May 2026 the features had still not shipped.
- **Hook line:** "Apple showed a feature on stage, then put it in the ads. Nine months later it was still not ready. The settlement was 250 million dollars. Somewhere a roadmap slide said 'coming soon'."
- **Sets up:**
  - M3: the roadmap is direction, the release plan is the promise. AI timelines are uncertain, so the gap between "we plan to" and "available now" is where trust breaks.
  - Hand-off rules: what the agent may say to an external audience, and what needs the PM's sign-off.
  - Ties to Focus without reteaching it. Focus says "the roadmap is the vision, the release plan is the promise". This course adds the agent that drafts the roadmap narrative and the check that catches a commitment.
- **Why PMs relate:** every PM has seen sales or marketing turn a roadmap item into a date in front of a customer. AI features make this worse because the PM cannot be sure when the model will be good enough.
- **Risks:**
  - Overused: the Siri delay is common in tech talks. The settlement angle is newer.
  - Legal: Apple did not admit wrongdoing. Say "settled", never "was found to have misled". The settlement had preliminary approval in May 2026. Final approval was not checked.
  - Current status: I did not check if the features shipped after May 2026 (reports said iOS 27). Check this before class.
  - Age: the delay is from March 2025 (20 months). The settlement is from May 2026 (6 months). Flag for Dan.
  - Learners who love Apple may defend it. Keep to the facts.
- **Sources:** S-S1 (MacRumors), S-S2 (AppleInsider). Independent reports of the settlement and timeline. Search results also show Bloomberg, TechCrunch and Axios reports of the March 2025 delay (not opened).
- **Status:** verified for the timeline, settlement amount, class period, and the no-wrongdoing statement.

### Candidate 3. Commonwealth Bank: the AI business case that was wrong (2025)

- **Story:**
  1. In July 2025 Commonwealth Bank of Australia, the country's biggest bank, told 45 customer service staff their roles were redundant because a new AI voice bot had reduced call volumes.
  2. The Finance Sector Union said call volumes were in fact rising: the bank offered overtime and had team leaders answer phones.
  3. In August 2025 the bank reversed the decision and said its assessment "did not adequately consider all relevant business considerations and this error meant the roles were not redundant".
- **Hook line:** "The business case said the bot had cut the calls. The people still on the phones knew the calls had gone up. The bank had to say, in public, that its assessment was an error."
- **Sets up:**
  - M2: a confident claim in a business case ("the bot reduced call volume") is not validated until someone checks it against the operating data.
  - M1: the decision to act on the case stays human. The check was skipped, not the AI.
  - Business case skills: list the assumptions, find the data that would prove each one wrong, red-team the case before it goes to leadership.
  - Internal product example: the "product" is the bank's own service operation.
- **Why PMs relate:** PMs write AI business cases now. The savings line is the first number leadership reads and the last one anyone checks.
- **Risks:**
  - Sensitive: job cuts and a union campaign. Keep the focus on the assessment error, not on who was right about AI and jobs.
  - The bank's call volume number is not in the sources I opened. Do not quote a number.
  - Age: August 2025 (15 months). Flag for Dan.
  - Media also report other 2026 "AI layoff reversals" (IBM, Ford). I did not verify them. Do not add them without sources.
- **Sources:** S-C1 (The Register), S-C2 (Information Age, ACS). Independent reports. Search results also show Bloomberg (2025-08-21) and the union's own release (not opened).
- **Status:** verified for the 45 roles, the reversal, the bank's quote and the union's account.

### Candidate 4. Intel leaves memory chips (1984 to 1985)

- **Story:**
  1. Intel was the first successful maker of DRAM memory chips, but by the mid-1980s Japanese makers made memory chips cheaper and better.
  2. Andy Grove asked Gordon Moore what a new CEO would do if the board threw them out, and Moore said: "Get out of the memory business."
  3. They made that choice themselves, and microprocessors, which had already become Intel's core business, carried the company for the next decades.
- **Hook line:** "Andy Grove asked: if the board fired us and brought in someone new, what would that person do? Gordon Moore said: get out of memory. So they did it themselves."
- **Sets up:**
  - M1: strategy is a forced choice. The data showed the answer for years. The hard part was the choice, and that stays human.
  - Opportunity prioritization: the business the company loves against the business the evidence supports.
  - An agent question for the course: an AI asked "how do we win in memory?" will write a good plan to win in memory. The PM must ask the "new CEO" question.
- **Why PMs relate:** every PM has a product line that leadership loves and the numbers do not support. Hardware PMs know the price war with a cheaper competitor.
- **Risks:**
  - Old: 1984 to 1985. Flag for Dan. It is classic on purpose.
  - Known to strategy readers (Grove's book "Only the Paranoid Survive", Burgelman's Stanford case).
  - Wording: the NPR transcript gives Grove's question as "what would happen if somebody took us over, got rid of us? What would the new guy do?" Many retellings use other words. Use the NPR words.
  - Focus teaches explicit and implicit strategy. The Burgelman case says middle managers moved capacity to microprocessors before the top decision. Do not teach that point again here; use only the forced choice.
  - Intel's recent troubles may draw comments. That can help: no choice stays right forever.
- **Sources:** S-I1 (NPR, Laura Sydell, 2012, Grove and Moore in their own voices), S-I2 (Stanford GSB case, Burgelman, 2005). Independent.
- **Status:** verified for the decision, the year and the exchange.

### Candidate 5. Executives' AI forecast: 0.2% so far, 0.6% expected (NBER, 2026)

- **Story:**
  1. In 2026 economists surveyed nearly 9,000 CEOs, CFOs and senior executives in 7 countries, including the US, UK and Germany.
  2. 78% of firms use AI, but executives said AI had raised annual labor productivity growth by only 0.2% over the last 3 years, with essentially no net effect on employment.
  3. The same executives predict a 0.6% per year boost over the next 3 years: three times what they have seen so far.
- **Hook line:** "Nine thousand executives say AI gave them 0.2% in the last three years. They expect three times that in the next three. Which number is in your AI business case?"
- **Sets up:**
  - M2: a forecast is not evidence. Business cases often use the expected number, not the measured one.
  - Business case skills: AI unit economics, sensitivity tests, the assumption list.
- **Why PMs relate:** PMs are asked to justify AI features and AI tools with productivity gains they cannot yet measure.
- **Risks:**
  - Close in theme to the "employees maxed out, leaders expect more productivity" finding used in AI for Product Managers. A learner who took that course may feel it is a repeat.
  - The paper was first issued in February 2026 and revised in October 2026. The abstract now describes a Summer 2026 survey. Check the numbers again before class.
  - Numbers are small and abstract. A weaker room hook than a company story.
- **Sources:** S-N1 (primary, NBER Working Paper 34836). Search results show The Register (2026-02-18) and Fortune coverage (not opened).
- **Status:** verified from the NBER abstract.

### Candidate 6. Sonos app rebuild breaks a hardware company (2024 to 2025)

- **Story:**
  1. In May 2024 Sonos, a speaker maker, released a rebuilt app that was buggy, hard for vision-impaired users, and missing features like alarms, timers and "play next".
  2. In August 2024 the CEO said the fix would cost 20 to 30 million dollars, and Sonos held back two new products until the app was fixed.
  3. In January 2025 the CEO stepped down; revenue had dropped, and the company promised stricter pre-launch testing and a "quality ombudsperson".
- **Hook line:** "A 20 to 30 million dollar fix, two product launches held back, and a CEO gone. All for an app the company was 'confident' was 'easier, faster and better'."
- **Sets up:**
  - M3: a launch date is a promise. If the release plan is not ready, the promise breaks.
  - Confidence is not validation (M2).
- **Why PMs relate:** hardware PMs know that the app is now part of the product. Every PM has shipped on a date that was set before the work was ready.
- **Risks:**
  - It is not an AI story. The link to the course is indirect.
  - Many retellings say the app was rushed to meet the Ace headphones launch and that staff warned before launch. I did not find this in the sources I opened. Do not tell that part without a source.
  - Age: May 2024 to January 2025 (22 months). Flag for Dan.
  - Names a CEO who left. Keep to the reported facts.
- **Sources:** S-O1 (The Register), S-O2 (Fast Company), S-O3 (Engadget).
- **Status:** verified for the facts above. Not verified: the "deadline drove it" angle.

## 4. Rejected ideas (not researched in depth)

| Idea | Reason |
| --- | --- |
| Kodak, Blockbuster, Nokia | Very overused. PRC already uses Netflix and Blockbuster |
| HBR "Executives who used gen AI made worse predictions" (Nvidia forecasts) | Strong fit for M2, but published 2025. Statistics must be 2026 or later |
| MIT NANDA "95% of gen AI pilots fail" | 2025. The number itself was widely questioned |
| Klarna AI customer service reversal | Overused. Mostly a support staffing story |
| Builder.ai collapse (inflated revenue) | Legal risk (fraud inquiries). About investors, not PMs |
| Zillow Offers (pricing algorithm, 2021) | Good M2 story, but old and well known. Possible backup if Dan wants another classic |
| Deloitte reports with AI-made citations | Used as a Market Research candidate. Same lesson |
| Sycophancy studies (AI agrees with the user, 2026) | General AI caution, not strategy specific. Better as a module point |
| "55% of companies regret AI layoffs" (2026 reports) | Vendor survey, primary source not opened. HR topic, sensitive |

## 5. Sources

All sources opened on 2026-11-22 unless the row says "not opened". checked_on: 2026-11-22.

| Id | Source | Date | Type | Used for | Age flag |
| --- | --- | --- | --- | --- | --- |
| S-T1 | Romasanta A., Thomas L.D.W., Levina N., "Researchers Asked LLMs for Strategic Advice. They Got 'Trendslop' in Return", Harvard Business Review. https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return | 2026-03-16 | Primary (summary and introduction readable; body paywalled) | Candidate 1: authors, finding, recommendations | No |
| S-T2 | NYU Stern Research Highlights, same title. https://www.stern.nyu.edu/experience-stern/faculty-research/research-highlights/researchers-asked-llms-strategic-advice-they-got-trendslop-return | 2026-03-16 | Secondary, author's school | Candidate 1: "almost uniformly select the same trendy strategies" | No |
| S-T3 | Rogelberg S., "Meet 'trendslop', the new, AI-fueled scourge of workplace consultants everywhere", Fortune (via Yahoo Finance). https://finance.yahoo.com/economy/policy/articles/meet-trendslop-ai-fueled-scourge-214741487.html | 2026-04-10 | News, independent | Candidate 1: 7 LLMs, 15,000 simulations, trade-offs tested, quotes | No |
| S-S1 | Clover J., "Apple to Pay $250 Million to Settle Class Action Over Delayed Siri Features", MacRumors. https://www.macrumors.com/2026/05/05/apple-class-action-siri-lawsuit-settlement/ | 2026-05-05 | News | Candidate 2: timeline, amount, class, no wrongdoing | No |
| S-S2 | AppleInsider, "Lawsuit over delayed Siri features reaches massive $250M settlement". https://appleinsider.com/articles/26/05/05/lawsuit-over-delayed-siri-features-reaches-massive-250m-settlement | 2026-05-05 | News, independent | Candidate 2: allegation quote, feature status in May 2026 | No |
| S-S3 | TechCrunch, "AI-powered, more personalized Siri is delayed". https://techcrunch.com/2025/03/07/ai-powered-more-personalized-siri-is-delayed/ | 2025-03-07 | News (not opened, search result) | Candidate 2: March 2025 delay | Yes (20 months) |
| S-C1 | The Register, "Bank reverses decision to replace 45 customer service staff with AI chatbot". https://www.theregister.com/2025/08/22/commonwealth_ban_chatbot_fail_rehiring/ | 2025-08-22 | News | Candidate 3: 45 roles, union account, reversal | Yes (15 months) |
| S-C2 | Information Age (ACS), "CBA reverses AI-driven job cuts, admits 'error'". https://ia.acs.org.au/article/2025/cba-reverses-ai-driven-job-cuts--admits--error-.html | 2025-08-21 | News, independent | Candidate 3: bank's admission quote, union quotes | Yes (15 months) |
| S-C3 | Bloomberg, "Australia's Biggest Bank Reverses Plan to Replace Jobs With AI". https://www.bloomberg.com/news/articles/2025-08-21/commonwealth-bank-reverses-job-cuts-decision-over-ai-chatbots | 2025-08-21 | News (not opened, paywall) | Candidate 3: context | Yes (15 months) |
| S-I1 | Sydell L., "Intel Legends Moore And Grove: Making It Last", NPR transcript. https://www.npr.org/transcripts/150057676 | 2012-04-06 | News interview | Candidate 4: Grove and Moore exchange, 1985, Japanese competition | Yes (old story) |
| S-I2 | Burgelman R., "Intel Corporation (A): The DRAM Decision", Stanford GSB case BP256A. https://www.gsb.stanford.edu/faculty-research/case-studies/intel-corporation-dram-decision | 2005 | Teaching case | Candidate 4: end of 1984 decision, first mover in DRAM, microprocessors as core business | Yes (old story) |
| S-N1 | Yotzov I., Barrero J.M., Bloom N., Davis S.J. et al., "Firm Data on AI", NBER Working Paper 34836. https://nber.org/papers/w34836 | 2026-02 (revised 2026-10) | Primary study, non-vendor | Candidate 5: all figures | No |
| S-N2 | The Register, "6,000 execs struggle to find the AI productivity boom". https://www.theregister.com/2026/02/18/ai_productivity_survey/ | 2026-02-18 | News (not opened, search result) | Candidate 5: shows the earlier version had about 6,000 executives | No |
| S-O1 | The Register, "Sonos CEO steps down". https://theregister.com/2025/01/14/sonos_ceo_steps_down | 2025-01-14 | News | Candidate 6: CEO change, revenue, quality promises | Yes (22 months) |
| S-O2 | Fast Company, "Sonos CEO steps down following a disastrous app redesign". https://www.fastcompany.com/91259432/sonos-ceo-steps-down-following-a-disastrous-app-redesign | 2025-01-13 | News, independent | Candidate 6: missing features, ombudsperson | Yes (22 months) |
| S-O3 | Engadget, "Sonos is delaying two product launches until it fixes its buggy app". https://www.engadget.com/audio/speakers/sonos-is-delaying-two-product-launches-until-it-fixes-its-buggy-app-213743460.html | 2024-08-07 | News | Candidate 6: 20 to 30 million dollar fix, two products delayed | Yes (27 months) |

Fetch log: 14 page fetches used of 15. One fetch (NBER w34984) opened the wrong paper; it is not used.

## 6. Open items for Dan

1. Pick one bond story at Gate 1.
2. If you pick candidate 2, 3, 4 or 6, confirm the old source can stay (research rule 5).
3. If you pick candidate 1, decide if someone with HBR access reads the full article for per-trade-off numbers. Without it, tell the story with no percentages.
4. If you pick candidate 2, check the current Siri feature status before class.
5. Decide if candidate 1 is the bond story or a module 1 slide. Not both (house rule 9).
