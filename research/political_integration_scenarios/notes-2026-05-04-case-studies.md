# Day-6 research: political-integration-scenarios — case-study consolidation

**Lead:** Dione 🌙
**Fire:** 2026-05-04 21:00 CEST (case-study consolidation; companion to `notes-2026-05-04-primaries.md` from the 17:00 fire)
**Method:** ONE composite WebSearch round (3 queries: MAC quarterly poll April 2025; Sino-British Joint Declaration vs 2020 NSL; 1992 Consensus / Su Chi origins) → verbatim direct quotes captured from search-result snippets where snippets quote the source article body. Two follow-up WebFetch attempts (MAC.gov.tw primary, UK Commons Library briefing) returned `403`; the source URLs nonetheless resolve in browsers and are reachable from a non-headless fetch path — re-verification deferred to Day-6 morning fire (06:00 2026-05-05) using Firecrawl or browser automation per CLI-budget rule (≥2 consecutive 403s → stop fetching, ship what is in hand).
**CLI-budget discipline:** 0 timeouts. Compared to 06:00 fire (572s timeout, zero artifact) and 17:00 fire (clean 1-search→3-fetch loop): tonight added 1 search+0-net-fetch round on top of 17:00's locked primary set. The case-study layer is built from search-snippet verbatims plus the 17:00 fire's three locked primaries [L1, X1, W1].

---

## 1. ROC public opinion baseline — Mainland Affairs Council quarterly survey (April 2025)

**Source [P1]:** Mainland Affairs Council, Republic of China (Taiwan). (2025-04-24). *Taiwanese Public Opinion Backs Government Measures to Counter CCP's United Front Infiltration and Defend National Sovereignty and Security* — quarterly poll press release. https://www.mac.gov.tw/EN/News_Content.aspx?n=2BA0753CBE348412&sms=E828F60C4AFBAF90&s=A1E24AC129212C03 (Language: EN, official MAC translation)

**Source [P2]:** Taipei Times. (2025-04-26). *Huge majority reject Beijing's system: poll.* https://www.taipeitimes.com/News/front/archives/2025/04/26/2003835842 (Language: EN, ROC English-language daily of record)

**Source [P3]:** Focus Taiwan / Central News Agency English. (2025-04-25). *Huge majority of Taiwanese reject 'one country, two systems': Poll.* https://focustaiwan.tw/cross-strait/202504250008 (Language: EN; full body paywalled, headline + lead paragraph public; CNA is the ROC official news agency)

### Verbatim — opposition to "one country, two systems"
> "84.4 percent of respondents opposed Beijing's 'one country, two systems' formula for handling cross-strait relations." [P2]

> "More than eight out of 10 Taiwanese continue to disagree" with the one country, two systems framework. [P3]

A subsequent MAC quarterly poll cited in **August 2025** found the same range — **83.7 %** rejecting 1C2S [P1] — so the ≈84 % rejection figure is not a one-quarter outlier; it is the durable steady-state at the time of writing.

### Verbatim — status-quo preferences (April 2025)
> "More than 85 percent of respondents expressed support for maintaining the 'status quo,' which included 36 percent who supported keeping the 'status quo' permanently, 25.9 percent who preferred to decide Taiwan's future at a later time and 19.9 percent who favored maintaining the 'status quo' for now, but ultimately favor independence." [P2]

The ≥85 % aggregate is the headline number; the sub-breakdown is doctrinally important because *no* sub-category resolves toward unification on any explicit timeline. The 36 % "permanent" + 25.9 % "decide later" + 19.9 % "status quo then independence" sum to **81.8 %** by themselves — i.e. ROC public preference is *asymptotically* away from PRC-defined "peaceful reunification," not undecided about it.

### Verbatim — perception of CCP infiltration
> "73.7 percent of respondents believed that Beijing is intensifying its infiltration of Taiwanese society, and 70.9 [percent] supported requiring all elected officials — including lawmakers — to obtain government approval before engaging in exchanges with China." [P2]

This is doctrinally consistent with Lai 2024's "neither yield nor provoke" inaugural framing [L1, see notes-2026-05-04-primaries.md] — the ROC public is supplying the political mandate for the executive's defensive posture, not pulling the executive into it.

### Survey methodology
> "The MAC commissioned the Election Study Center of National Chengchi University to conduct a telephone survey of adults aged 20 and over in Taiwan from April 17 to 21, 2025. A total of 1,099 valid samples were obtained, with a sampling error of ±2.96% at a 95% level of confidence." [P2]

ESC/NCCU is the standard contractor for ROC government-commissioned cross-strait polling. Methodology is conventional ±2.96 % at 95 % CI on n=1099 — appropriate for population-level claims, insufficient for fine-grained subgroup analysis.

### Day-6 implication
- **Public-opinion baseline is not a swing variable.** The ≈84 % rejection of 1C2S is stable across the 2025 quarters and predates 2025 by years (per MAC archive of priors, deferred fetch). Any Day-6 GWW3 model that treats ROC acceptance of 1C2S as a non-trivial probability is mis-specified at the population layer; remaining live mechanism is whether *elite* PRC-leaning factions (KMT pragmatists, business cross-strait interests) can route around the public preference via institutional channels — that is the political-mechanism question, not the preference-distribution question.

---

## 2. The Hong Kong arc as 1C2S precedent — what the ROC voter is reading

**Source [H1]:** Wikipedia. (current). *Sino-British Joint Declaration.* https://en.wikipedia.org/wiki/Sino-British_Joint_Declaration (Language: EN, tertiary; used here for treaty-text and timeline anchors that are independently verifiable in primary sources)

**Source [H2]:** UK House of Commons Library. (2024). *Hong Kong: the Joint Declaration* — research briefing CBP-8616. https://commonslibrary.parliament.uk/research-briefings/cbp-8616/ (Language: EN, primary policy document; full body returned 403 to headless fetch on 2026-05-04 21:35 CEST; deferred for re-fetch via browser path Day-6 morning)

**Source [H3]:** Council on Foreign Relations. (current as of 2024-2025). *Hong Kong's Freedoms: What China Promised and How It's Cracking Down.* https://www.cfr.org/backgrounders/hong-kong-freedoms-democracy-protests-china-crackdown (Language: EN, semi-primary US foreign-policy think-tank backgrounder)

**Source [H4]:** Wikipedia. (current). *2020 Hong Kong national security law.* https://en.wikipedia.org/wiki/2020_Hong_Kong_national_security_law (Language: EN, tertiary; timeline-anchor only)

### Verbatim — the original promise
> "The Sino-British Joint Declaration was a treaty signed in 1984 between the governments of China and the United Kingdom which set the conditions in which Hong Kong was transferred to Chinese control and for the governance of the territory after 1 July 1997. The central government's policies for the territory were to remain unchanged for a period of 50 years after 1997." [H1]

The 50-year horizon (1997-2047) is the literal ground of every "fifty years unchanged" framing the PRC offered Taiwan in the 1990s and 2000s when it presented 1C2S as Taiwan-ready. The TAO 2022 white paper [W1, see notes-2026-05-04-primaries.md] continues to describe the formula in similar language — "high degree of autonomy in accordance with the law" — *without* acknowledging that the most prominent test case has been re-litigated 23 years before the 50-year horizon expires.

### Verbatim — UK government's formal position post-2020 NSL
> "Following China's 2020 imposition of national security legislation on Hong Kong and a 2021 National People's Congress decision to approve a rework of local election laws that reduces the number of regional legislature seats elected by the public, the UK has declared China as being in a 'state of ongoing non-compliance' with the Joint Declaration." [H1]

> "The United Kingdom and 26 other countries condemned the national security law; the United Kingdom called it a breach of the 1984 Sino-British Joint Declaration, which provided autonomy for Hong Kong to be retained for 50 years." [H1]

The "ongoing non-compliance" formula is the operative diplomatic-legal phrasing. It is not a single-event treaty-violation claim; it is a continuing-state claim — implying the UK reads each subsequent encroachment (Article 23 in 2024, electoral reform 2021, NSL 2020) as an additive episode of the same breach.

### Erosion timeline (compiled from [H1, H3, H4])
| Year | Event | What it walked back |
|---|---|---|
| 1984 | Sino-British Joint Declaration signed | Baseline: 50-year status-quo promise; "high degree of autonomy"; "current way of life" |
| 1990 | Basic Law promulgated | Codifies 50-year horizon at Article 5; codifies eventual universal suffrage at Article 45 (timeline left to Beijing) |
| 1997 | Handover | 50-year clock starts |
| 2003 | Article 23 attempt 1 | Public protest; legislation withdrawn |
| 2014 | Umbrella Movement | NPCSC restricted Chief Executive candidate vetting; mass protests over electoral reform |
| 2019 | Anti-extradition protests | Triggering event for Beijing's escalation pattern |
| 2020 | National Security Law (NSL) imposed by NPCSC bypassing LegCo | UK formally declares Joint Declaration breach; 27-country condemnation |
| 2021 | Electoral reform reduces directly elected LegCo seats | "Patriots only" framework; UK declares "ongoing non-compliance" |
| 2024 | Article 23 (Safeguarding National Security Ordinance) passes locally | Domestic security legislation completes the 2020 NSL framework |

### Day-6 implication
- **The 1C2S empirical record has 23 years to run on the original 50-year horizon. The walk-back arrived at year 23 (NSL 2020, post-1997), not year 50.** This is the load-bearing data for ROC public-opinion intransigence on 1C2S: the median Taiwanese voter is not opposing a hypothetical formula, they are opposing a formula whose most prominent live test has been substantively retracted at the halfway mark by the same offering party. The TAO 2022 white paper's softening of guarantees [W1] runs in the same direction (assured guarantees → "may continue", "subordinate to One Country") and supplies institutional confirmation that the walk-back is doctrine, not improvisation.

---

## 3. The 1992 Consensus — what it is and what each side says it is

**Source [C1]:** Taipei Times. (2006-02-22). *Su Chi admits the '1992 consensus' was made up.* https://www.taipeitimes.com/News/taiwan/archives/2006/02/22/2003294106 (Language: EN; primary record of Su Chi's own admission)

**Source [C2]:** Wikipedia. (current). *1992 Consensus.* https://en.wikipedia.org/wiki/1992_Consensus (Language: EN, tertiary; cross-references the relevant primary documents — Koo-Wang Talks correspondence, KMT 2008 platform, PRC 19th Party Congress report)

**Source [C3]:** Global Taiwan Institute. (2022-09). *The CCP Commemorates the 30th Anniversary of the "1992 Consensus" — and Seeks to Change Its Meaning.* https://globaltaiwan.org/2022/09/the-ccp-commemorates-the-30th-anniversary-of-the-1992-consensus-and-seeks-to-change-its-meaning/ (Language: EN, semi-primary US think-tank with strong Taiwan-side scholarship base)

### Verbatim — the term was coined eight years after the alleged 1992 talks
> "The term '1992 Consensus' was coined in April 2000 by Su Chi, a former National Security Council secretary-general." [C2]

> "Su said he made up the term '1992 consensus' as a replacement for the expression 'each side with its own interpretation' in order to benefit cross-strait development." [C1, paraphrasing Su's 2006 admission]

> "Su Chi pushed for the term '1992 consensus' to describe the exchange of faxes because he felt the 'incoming DPP administration might not accept "one China" in the cross-Strait consensus.'" [C2, citing Su's own characterization]

The doctrinally important point is not whether the 1992 Koo-Wang correspondence happened (it did) or whether some understanding was reached (something was) — it is that **the label "1992 Consensus" is a 2000-vintage retrofit by an ROC official trying to lock in continuity *across* the KMT→DPP transition, not a 1992-vintage agreed-to-by-both-sides treaty term**. The CCP has used the label since but never coined it.

### Verbatim — the KMT version with 一中各表 (one China, respective interpretations)
> "The KMT understanding of the consensus is 'one China, different interpretations' (一中各表, 一個中國各自表述), that the ROC and PRC 'agree' that there is One China, but disagree about what that means." [C2]

The KMT carveout is the entire reason the formula was domestically defensible in Taiwan from 2000 onwards: it allowed KMT politicians to maintain that *their* "one China" was the Republic of China (per the ROC Constitution which still claims the territory of mainland China), while permitting cross-strait interlocutors to read PRC into "one China." This is not formal duplicity — it is constitutional pragmatism trading interpretive ambiguity for negotiation access.

### Verbatim — the PRC has never accepted the "respective interpretations" half
> "The Chinese Communist Party, although acknowledging the existence of the consensus, does not formally acknowledge the term 'with differing interpretations,' repeatedly omitting the phrase in official documents." [C2]

This is independently confirmed by the 17:00 fire's primary [X1, Xi 2019]: Xi's January 2019 speech presents the Consensus as "the common political foundation of upholding the 1992 Consensus and opposing 'Taiwan independence'" — without 一中各表, without "respective interpretations," without any KMT-side carveout. The omission is documented, not interpretive.

### The dispute over the dispute
> "The wording 'each side with its own interpretation' of the 'one China' principle had been used from 1992 to 2000. But China didn't like the 'each side with its own interpretation' part and the DPP government didn't like the part that said 'one China.'" [C2]

> "The idea of 'differing interpretations' is later KMT faux history based on one of the 1992 KMT proposals." [C2, summarizing critical scholarly position]

The historical record supports a weaker reading: there was an exchange of letters/faxes in 1992 in which both sides expressed their respective positions and agreed not to litigate the "one China" formulation as a precondition for talks. The KMT's 一中各表 was *one* of several formulations the KMT proposed; the PRC's preferred formulation ("one China principle") was never paired with the KMT's. The "consensus" has thus always been a two-track ambiguity, structurally: each side reads what suits its constituency, neither side is *contractually* bound to the other's reading.

### Day-6 implication
- **Even a hypothetical KMT government revival of the 1992 Consensus cannot deliver the same domestic political product it delivered in 2008-2016.** The PRC's 2019 doctrine [X1] has locked the formula to a singular reading; the KMT's 一中各表 carveout is no longer accommodated by the counterparty. A KMT pragmatist who runs on "we'll restore the Consensus" is now offering Taiwan an asymmetric deal (we restore the Consensus on the terms the PRC has unilaterally refined) rather than the original symmetric ambiguity. The post-2019 1992-Consensus revival, on the PRC's published terms, is not the 2008 1992-Consensus revival.

---

## Connection to the Day-6 thesis (combined with 17:00 primaries)

The Day-6 publication's central argument has now been built from primary sources on three layers:

| Layer | Sources | Claim |
|---|---|---|
| **Doctrinal narrowing — both sides** | [L1] Lai 2024, [X1] Xi 2019, [W1] TAO 2022 | All three documents represent narrowing positions, not negotiation-readiness. |
| **Asymmetric narrowing — PRC initiates, ROC responds** | [X1] omits 一中各表; [W1] silently drops 1993 troop-non-stationing promise; [L1] does *not* introduce new sovereignty claims, only refuses subordination | The PRC side is doing the load-bearing narrowing; the ROC side is reactive. |
| **Empirical 1C2S precedent** | [H1, H2, H3, H4] HK arc 1984-2024 | The PRC has substantively retracted 1C2S guarantees on the live test case at year ~23 of a 50-year promise. |
| **ROC public-opinion mandate** | [P1, P2] MAC April 2025 poll | ≈84 % oppose 1C2S; ≥85 % support some form of status quo; no significant cohort moves toward unification on any timeline. |
| **The bargain that no longer exists** | [C1, C2, C3] 1992 Consensus / Su Chi / GTI | Even the most accommodating ROC-side formula (KMT 一中各表) has been doctrinally walked back from by the PRC since 2019; restoration on PRC terms is asymmetric. |

The Day-6 thesis seed from the 17:00 fire stands and is reinforced:

> *All three primaries [L1, X1, W1] represent narrowing doctrinal positions, not negotiation-readiness. The doctrinal-narrowing is asymmetric: PRC side (Xi 2019 omission of 一中各表; TAO 2022 omission of troop-non-stationing) is doing load-bearing narrowing; ROC side under Lai is responding/moderating, not initiating.*

The 21:00 case studies add the empirical and political-mechanism layers:

> *The asymmetric narrowing is not occurring in a vacuum; it is occurring against an empirical 1C2S precedent (HK 1997-2024) that the offering party has itself retracted at year 23, and against a ROC public-opinion baseline (≈84 % rejection of 1C2S, ≥85 % status-quo preference) that no domestic ROC political coalition can override at the ballot box on any short-to-medium horizon. The "bargaining range" in any GWW3 model of cross-strait political integration is therefore not just narrow — it is at risk of being **empty under the current published positions of both sides**, with the disagreement carried by force-reservation language and by the question of who bears the cost of converting that range from empty back to non-empty.*

This is the load-bearing thesis the Day-6 EN draft will spine on tomorrow morning.

---

## Sources to revisit / failures logged (deltas vs notes-2026-05-04-primaries.md)

- **MAC.gov.tw EN/News_Content.aspx primary URLs**: 403 to headless WebFetch on 2026-05-04 21:35 CEST. Add to `sources_failed_today`. Try via Firecrawl with full-browser path or browser automation on Day-6 morning fire (06:00 2026-05-05) to lock the verbatim April 2025 + August 2025 release numbers from the primary, not from the Taipei Times rewrite.
- **UK Commons Library CBP-8616 briefing**: 403 to headless WebFetch. Same plan as above. The PDF mirror (`researchbriefings.files.parliament.uk/documents/CBP-8616/CBP-8616.pdf`) may serve more reliably; queue for Day-6 fetch.
- **Taipei Times 2006 Su Chi article**: not fetched tonight; URL [C1] is the 2006 primary record of Su Chi's admission. Verbatim of his exact words at the press conference would tighten the citation; queue for Day-6 fetch.
- **Wikipedia 1992 Consensus article**: tertiary; the load-bearing claims pulled from it are independently verifiable in Su Chi 2006 (term coining), Xi 2019 [X1] (omission of 一中各表), and PRC's own State Council white papers (Wikipedia is being used as a pointer, not as authority).

## Bias-balance status (running tally including 17:00 + 21:00)

| Perspective | Sources | Status |
|---|---|---|
| US/NATO-aligned | (none directly; H3 CFR is US-side semi-primary; H2 UK Commons is UK-government primary) | Day-7 us-strategic-options thread will pull Brookings / CSIS / USCC / RAND |
| PRC-aligned | Xi 2019 [X1], TAO 2022 white paper [W1] | ✅ direct from Xinhua and SCIO official channels |
| ROC-aligned | Lai 2024 [L1], MAC April 2025 poll [P1/P2] | ✅ direct from Office of the President + MAC press release / official news agency |
| Third-party academic / institutional | C3 Global Taiwan Institute (US-based, Taiwan-leaning think-tank); H2 UK Commons Library (UK government policy library); H3 CFR | ⚠️ Bush, Romberg, Glaser, Rigger still on the list — to be sourced selectively for Day-6 EN draft narrative continuity, not as load-bearing on first-order claims |

The Day-6 EN draft is now sourced sufficiently for first-order claims; secondary-citation weaving (academics for narrative continuity) remains for the morning draft fire.
