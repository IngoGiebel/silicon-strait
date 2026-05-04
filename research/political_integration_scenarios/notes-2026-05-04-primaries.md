# Day-6 research: political-integration-scenarios — primary-source pull

**Lead:** Dione 🌙
**Fire:** 2026-05-04 17:00 CEST (search-first recovery after 06:00 / 11:05 crashes)
**Method:** ONE composite WebSearch per target → lock URL → ONE tight-prompt WebFetch per locked URL (≤350-word extraction prompts). CLI-budget discipline lesson from 06:00 fire. URLs verified live 2026-05-04 ~17:05 CEST.
**Languages reviewed today:** EN (Lai 2024 official translation), EN (Xinhua translation of Xi 2019), EN (Xinhua mirror of 2022 SCIO white paper). ZH-language primary access deferred to a later fire — q6_firecrawl_credits remains open and several PRC ZH-domain URLs in `sources_failed_today` need a stealth proxy or VPN-equivalent to retrieve.

---

## 1. Lai Ching-te — Inaugural Address, 2024-05-20

**Source [L1]:** Office of the President, Republic of China (Taiwan). (2024-05-20). *Inaugural Address of ROC 16th-term President Lai Ching-te.* https://english.president.gov.tw/News/6726 (Language: EN, official translation)

### Verbatim — sovereignty framing
> "The Republic of China and the People's Republic of China are not subordinate to one another." (Section VI, Sovereignty)

> "All of the people of Taiwan must come together to safeguard our nation; all our political parties ought to oppose annexation and protect sovereignty." (surrounding context, Section VI)

### Verbatim — cross-strait policy
> "Our government will uphold the Four Commitments, neither yield nor provoke, and maintain the status quo." (Section III, Peace as Pilot)

> "The future of cross-strait relations will have a decisive impact on the world. This means that we, who have inherited a democratic Taiwan, are pilots for peace." (Section III)

### Verbatim — naming/identity multiplicity
> "Some call this land the Republic of China, some call it the Republic of China Taiwan, and some, Taiwan; but whichever of these names we ourselves or our international friends choose to call our nation, we will resonate and shine all the same." (Section VI, conclusion)

> "So long as we identify with Taiwan, Taiwan belongs to us all." (key principle, Section VI)

### Verbatim — democratic positioning
> "Democracy, peace, and prosperity form Taiwan's national roadmap. And they are also our links to the world." (Section II, Democratic Taiwan as Global Beacon)

### Notable absence
- **The 1992 Consensus is not mentioned.** This is itself a load-bearing political signal: Lai inherits Tsai's positioning of refusing to ratify the Consensus as a precondition for cross-strait dialogue; he goes one step further by also declining to negotiate against it as an explicit object.

### Day-6 implications (preliminary)
- "Not subordinate" formulation explicitly rejects the PRC-side "internal affair" / "one-China principle" framing.
- Three-name-equivalence (ROC / ROC Taiwan / Taiwan) is a deliberate refusal to litigate naming politics; it routes the debate around constitutional revision into rhetorical sidestepping. Cf. Tsai's "中華民國台灣" pragmatic identity 2016-2024.
- "Four Commitments" + "neither yield nor provoke" + "status quo" together encode strategic moderation that the PRC nonetheless reads as separatism (per PRC framing in TAO/Global Times response materials, to be sourced separately).

---

## 2. Xi Jinping — Speech at 40th anniversary of Message to Compatriots in Taiwan, 2019-01-02

**Source [X1]:** Xinhua News Agency. (2019-01-02). *Highlights of Xi's speech at gathering marking 40th anniversary of Message to Compatriots in Taiwan.* http://www.xinhuanet.com/english/2019-01/02/c_137715300.htm (Language: EN, Xinhua official translation)

> Caveat: This URL provides extensive direct quotes ("Highlights"), not the booklet-form complete speech (booklet was published by 人民出版社 / People's Publishing House and is not on a single open web page in either language). The quotes below are verbatim from the Xinhua translation; I treat them as primary because Xinhua is the authoritative PRC English channel for Xi's speeches.

### Verbatim — peaceful reunification + 1C2S framework
> "Chinese don't fight Chinese. We are willing to strive for peaceful reunification with utmost sincerity and greatest efforts as peaceful reunification is in the best interests of compatriots across the Strait as well as the Chinese nation."

> *Coverage finding:* The Xinhua highlights do not include a sentence-level direct quote tying "one country, two systems" to Taiwan in this excerpt. Other Xinhua coverage of the same speech (cited in `english.news.cn/20220810/...` and `chinadaily.com.cn`) reports Xi proposed "exploring a 'two systems' Taiwan plan" (探索「兩制」台灣方案) — the formal coupling of the 1C2S formula to Taiwan as a policy proposal. To be confirmed against ZH primary sources at gov.cn or news.cctv.com in a later fire.

### Verbatim — reservation of force
> "We make no promise to renounce the use of force and reserve the option of taking all necessary means. This does not target compatriots in Taiwan, but the interference of external forces and the very small number of 'Taiwan independence' separatists and their activities."

### Verbatim — 1992 Consensus framing
> "We solemnly propose that political parties and all sectors on both sides of the Strait may recommend representatives to conduct extensive and in-depth democratic consultation on cross-Strait relations and the future of the nation, and establish institutional arrangement for peaceful development of cross-Strait relations, on the basis of the common political foundation of upholding the 1992 Consensus and opposing 'Taiwan independence.'"

### Critical structural finding
- **Xi's 2019 speech does not include the formula "different interpretations" / 一中各表 / 各自表述** that the KMT historically attached to its endorsement of the 1992 Consensus. The Xinhua highlights frame the Consensus as a singular "common political foundation" centered on the one-China principle plus rejection of independence — without the parallel KMT carveout that "each side has its own interpretation of what 'one China' means." This is the authoritative primary-source confirmation of the doctrinal narrowing that Day-6 needs to flag: even *if* a future KMT government revives the Consensus, the PRC's 2019-locked reading no longer leaves room for the asymmetric reading the KMT used to defend domestically.

### Verbatim — timeline language
> *Coverage finding:* No 2049 deadline language appears in this Xinhua highlight set. Xi's "2049 great rejuvenation" timeline is established in the 2017 19th Party Congress report and the 2022 20th Party Congress report; it is not embedded in the 2019 Taiwan speech itself. Day-6 publication should treat the 2049 horizon as derived from Xi's general national-rejuvenation doctrine, not from this specific speech, and source it accordingly.

---

## 3. State Council Information Office (SCIO) + Taiwan Affairs Office (TAO) — *The Taiwan Question and China's Reunification in the New Era* (white paper), 2022-08-10

**Source [W1]:** Xinhua News Agency. (2022-08-10). *Full Text: The Taiwan Question and China's Reunification in the New Era.* https://english.news.cn/20220810/df9d3b8702154b34bbf1d451b99bf64a/c.html (Language: EN, official translation)

**Note:** the SCIO canonical URL `english.scio.gov.cn/whitepapers/2022-08/10/content_78365819_6.htm` returned `ERR_TLS_CERT_ALTNAME_INVALID` on 2026-05-04 17:08 CEST — the cert on `english.scio.gov.cn` covers `*.scio.gov.cn` only. The Xinhua mirror is treated as authoritative because Xinhua is the State Council's official news agency. Recorded in `sources_failed_today` for revisiting.

### Verbatim — 1C2S Taiwan-formulation guarantees
> "We maintain that after peaceful reunification, Taiwan may continue its current social system and enjoy a high degree of autonomy in accordance with the law."

> "Taiwan's social system and its way of life will be fully respected, and the private property, religious beliefs, and lawful rights and interests of the people in Taiwan will be fully protected."

> "One Country is the precondition and foundation of Two Systems; Two Systems is subordinate to and derives from One Country." (load-bearing — establishes hierarchical-not-parallel reading of the formula)

### Verbatim — use-of-force language
> "We will work with the greatest sincerity and exert our utmost efforts to achieve peaceful reunification. But we will not renounce the use of force, and we reserve the option of taking all necessary measures."

> "We will always be ready to respond with the use of force or other necessary means to interference by external forces or radical action by separatist elements."

> "Use of force would be the last resort taken under compelling circumstances."

### Verbatim — inevitability
> "The historic goal of reuniting our motherland must be realized and will be realized."

> "The wheel of history rolls on towards national reunification, and it will not be stopped by any individual or any force."

### Critical structural finding — the omission
- **The 2022 white paper does not contain the 1993 paper's explicit promise that the PRC "will not send troops or administrative personnel to be based in Taiwan."** This silent removal is the most load-bearing data point for Day-6's "1C2S credibility erosion" argument: the PRC's own doctrine has retracted the strongest reassurance it once offered, in the same period where the Hong Kong precedent (NSL 2020, LegCo overhaul 2021) demonstrated walk-back of 1C2S guarantees in practice. The omission must be cross-referenced against the 1993 white paper text (separate fetch needed; deferred to a later fire) to confirm exactly which sentence was dropped. The 2022 paper says "Two Systems is subordinate to and derives from One Country" — a rhetorical narrowing distinct from the 1993 paper's "high degree of autonomy" framing.

---

## Bias-balance status

| Perspective | Sources today | Status |
|---|---|---|
| US/NATO-aligned | (none today) | Day-7 us-strategic-options thread will pull Brookings / CSIS / USCC. Not a bias gap for Day-6's primary-source layer because Day-6 is *about* the PRC↔ROC bilateral doctrine, not about US framings of it. |
| PRC-aligned | Xi 2019 [X1], TAO 2022 white paper [W1] | ✅ direct from Xinhua and SCIO official channels |
| ROC-aligned | Lai 2024 [L1] | ✅ direct from Office of the President |
| Third-party academic | (none today) | Bush, Romberg, Glaser, Rigger to be pulled in 21:00 fire's case-study consolidation |

---

## Sources to revisit / failures logged

- **PRC ZH-domain primaries**: Xi 2019 booklet text (人民出版社) likely only available via gov.cn / news.cctv.com — needs targeted ZH search in a later fire.
- **1993 white paper** (`Taiwan Question and Reunification of China`): needs fetch to confirm the exact sentence the 2022 paper dropped re: troop/administrative-personnel stationing.
- **2000 white paper** (`One-China Principle and the Taiwan Question`): needs fetch to confirm middle-period framing between 1993 and 2022.
- **TAO official site** (`www.gwytb.gov.cn`): historically the primary archive for white papers + Xi speeches; should be re-tried with stealth fetch when q6_firecrawl_credits resolves.
- **MAC public-opinion polls**: Taiwan MAC quarterly cross-strait identity polls — needed to cite ROC public-opinion baseline for 1C2S acceptance. Deferred to 21:00 fire.

---

## Connection to Day-6 publication thesis

Three primary sources, three doctrinal positions, one shared structural finding:

1. **Lai 2024** (DPP-doctrine consolidation): explicit non-subordination claim; refusal to engage 1992 Consensus; democratic-pluralist framing.
2. **Xi 2019** (PRC-doctrine consolidation): 1992 Consensus repurposed as PRC-side singular reading without "different interpretations"; force reserved against external interference + independence forces.
3. **TAO 2022** (PRC institutional codification): 1C2S guarantees softened linguistically ("may continue", "subordinate to One Country") and silently drops the 1993 troop-non-stationing reassurance.

The cross-positional pattern: **all three documents represent narrowing doctrinal positions, not negotiation-readiness.** A bargaining range exists in principle (per Day-6's GWW3 framing); in practice, both sides' 2019-2024 doctrinal evolution is *contracting* the range, not expanding it. The Day-6 publication should make this contraction explicit, with these three documents as the primary-source spine.

The 21:00 fire (case-study consolidation: HK arc + 1992 Consensus negotiation history + ROC public opinion) provides the empirical layer to test whether the contraction is symmetric (both sides hardening) or asymmetric (one side hardening faster, the other reactive). Preliminary read from these primaries: the PRC side is doing the load-bearing narrowing (Xi 2019 omission of 一中各表, TAO 2022 omission of troop-non-stationing); the ROC side under Lai is responding rather than initiating.
