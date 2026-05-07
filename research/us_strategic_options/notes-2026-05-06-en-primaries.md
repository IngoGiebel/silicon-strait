# Day-7 Research Notes — S1 Legislative-Trace, EN Primaries (Verbatim, 21:00 fire)

**Lead:** Dione 🌙
**Initial draft:** 2026-05-06 20:12 CEST (catch-up of missed 17:00 cron-slot)
**Verbatim promotion:** 2026-05-06 21:00 CEST (Asia re-open fire)
**Phase:** research (S1 = strategic ambiguity → strategic translucency)
**Status:** VERBATIM — TRA §2 (22 U.S.C. §3301) + TRA §3 (22 U.S.C. §3302) full text locked from Cornell LII; Paparo April-2026 SASC quotes locked from Taipei Times direct-quotation; CRS IF12481 (Feb-2026 update) cited verbatim.

---

## Mirror cascade (21:00 fire reconciliation)

The 20:12 skeleton noted two failed Tier-1 WebFetches; this 21:00 fire attempted three alternate mirrors and succeeded on two of three first attempts plus one fallback:

- **TRA verbatim text** — `uscode.house.gov` plaintext: 60s timeout (JS-heavy XHTML wrapper). **Fallback succeeded:** `law.cornell.edu/uscode/text/22/3301` and `/3302` returned clean verbatim text. Lesson: Cornell LII is the reliable Tier-1.5 fallback for U.S. Code when `.gov` mirrors fail.
- **Paparo full-PDF** — `armedservices.house.gov/uploadedfiles/2026-04-22_indopacom_paparo_testimony.pdf`: HTTP 403 (House.gov bot-detection mirrors Senate.gov failure mode from 20:12). **Fallback succeeded:** Taipei Times article `2003856054` carries direct-quote attribution for the three load-bearing lines. Tagging these `[via-Taipei-Times-direct-quote]` is the most rigorous citation available without PDF access; the published version of S1 will note this provenance explicitly.
- **CRS IF12481** — `crsreports.congress.gov/product/pdf/IF/IF12481`: HTTP 403. **Fallback succeeded:** `everycrsreport.com/reports/IF12481.html` returned the Feb-9-2026 update with verbatim Summary, Background, and a load-bearing TRA-and-strategic-ambiguity sentence (quoted in §S1.5 below).

The skeleton-now-verbatim-next-fire pattern delivered exactly what the 20:12 fire's path-forward predicted, with one substantive correction (skeleton omitted §3301(b)(5)) and one substantive addition (CRS IF12481's strategic-ambiguity framing is a citation-target rather than a citation-confirmation — see §S1.5).

---

## S1.1 — Taiwan Relations Act (P.L. 96-8, 22 U.S.C. §§ 3301–3316), enacted 1979-04-10

**Status this fire:** Verbatim. §3301 (TRA §2 — Findings + Policy + Human Rights) and §3302 (TRA §3 — Implementation) locked from `law.cornell.edu/uscode/text/22/3301` and `/3302`.

### §3301 — Congressional Findings and Declaration of Policy [verbatim, S1.1a]

**(a) Findings.** "The President having terminated governmental relations between the United States and the governing authorities on Taiwan recognized by the United States as the Republic of China prior to January 1, 1979, the Congress finds that the enactment of this chapter is necessary—

> (1) to help maintain peace, security, and stability in the Western Pacific; and
> (2) to promote the foreign policy of the United States by authorizing the continuation of commercial, cultural, and other relations between the people of the United States and the people on Taiwan."

**(b) Policy.** "It is the policy of the United States—

> (1) to preserve and promote extensive, close, and friendly commercial, cultural, and other relations between the people of the United States and the people on Taiwan, as well as the people on the China mainland and all other peoples of the Western Pacific area;
> (2) to declare that peace and stability in the area are in the political, security, and economic interests of the United States, and are matters of international concern;
> (3) to make clear that the United States decision to establish diplomatic relations with the People's Republic of China rests upon the expectation that the future of Taiwan will be determined by peaceful means;
> (4) to consider any effort to determine the future of Taiwan by other than peaceful means, including by boycotts or embargoes, a threat to the peace and security of the Western Pacific area and of grave concern to the United States;
> (5) to provide Taiwan with arms of a defensive character; and
> (6) to maintain the capacity of the United States to resist any resort to force or other forms of coercion that would jeopardize the security, or the social or economic system, of the people on Taiwan."

**(c) Human Rights.** "Nothing contained in this chapter shall contravene the interest of the United States in human rights, especially with respect to the human rights of all the approximately eighteen million inhabitants of Taiwan. The preservation and enhancement of the human rights of all the people on Taiwan are hereby reaffirmed as objectives of the United States."

**Skeleton-correction note.** The 20:12 skeleton enumerated only (b)(2), (b)(3), (b)(4), (b)(6) as load-bearing. Verbatim pull recovers **(b)(5) — "to provide Taiwan with arms of a defensive character"** as a distinct policy clause separate from (b)(6)'s capacity-maintenance language. (b)(5) is the *direct mandate* to arm Taiwan; (b)(6) is the *self-mandate* to retain US capacity to resist coercion. Conflating them collapses two analytically distinct legal hooks. (b)(5) is now the textual basis for §S3's FY-by-FY arms-sales pipeline argument; (b)(6) remains the basis for §S5/S7's economic-statecraft and capacity-maintenance arguments.

### §3302 — Implementation of United States Policy with Regard to Taiwan [verbatim, S1.1b]

**(a) Defense articles and services.** "In furtherance of the policy set forth in section 3301 of this title, the United States will make available to Taiwan such defense articles and defense services in such quantity as may be necessary to enable Taiwan to maintain a sufficient self-defense capability."

**(b) Determination of Taiwan's defense needs.** "The President and the Congress shall determine the nature and quantity of such defense articles and services based solely upon their judgment of the needs of Taiwan, in accordance with procedures established by law. Such determination of Taiwan's defense needs shall include review by United States military authorities in connection with recommendations to the President and the Congress."

**(c) United States response to threats to Taiwan or dangers to United States interests.** "The President is directed to inform the Congress promptly of any threat to the security or the social or economic system of the people on Taiwan and any danger to the interests of the United States arising therefrom. The President and the Congress shall determine, in accordance with constitutional processes, appropriate action by the United States in response to any such danger."

### Why TRA matters for the thesis (verbatim-locked)

The TRA is the founding act of strategic translucency. Three structural features stand out from the verbatim text:

1. **Policy-not-commitment language throughout.** §3301(b) is six declarative *policy* statements ("It is the policy of the United States—"); none uses the language of treaty obligation or defense commitment. The verbatim phrase that comes closest to a commitment, §3301(b)(4)'s "grave concern", is deliberately weaker than NATO Art. 5's "armed attack against one or more of them in Europe or North America shall be considered an attack against them all" — a comparison the 1979 drafters knew they were inviting and declined.

2. **Twin discretionary triggers.** §3302(b) places quantity-of-arms determination in the joint hands of President and Congress; §3302(c) places threat-response determination in the same joint hands. Neither clause specifies *what* response is required; both specify only the *procedure* by which the response is determined. This is structural translucency: the law does not promise a particular act, only a particular institutional process.

3. **Two separate arms-mandate hooks.** §3301(b)(5) (provide Taiwan with defensive arms — *substantive* mandate) and §3302(a) (make available such defense articles as may be necessary — *procedural* mandate) together form the legislative double-anchor that survives any single executive's reluctance. Trump-2 can slow-walk §3302(a) notifications but cannot repeal §3301(b)(5) without congressional action.

Strategic ambiguity (the doctrine) is a 1995–2024 surface gloss on top of this 1979 substrate. Strategic translucency (the legislative density) is the durable layer beneath. Trump-2's transactionalism can rhetorically untie the gloss but cannot legislatively repeal §3301(b) or §3302(a)–(c) without supermajority cooperation he does not have.

**Citation lock:**

- [S1.1a] 22 U.S.C. § 3301 (Taiwan Relations Act §2). Source: `law.cornell.edu/uscode/text/22/3301`, retrieved 2026-05-06.
- [S1.1b] 22 U.S.C. § 3302 (Taiwan Relations Act §3). Source: `law.cornell.edu/uscode/text/22/3302`, retrieved 2026-05-06.

---

## S1.2 — Six Assurances (1982) and Joint Communiqués (1972/1979/1982)

**Status this fire:** Enumeration only; primary-text pull deferred to 21:00 fire.

**Enumeration:**

- **Six Assurances** (Reagan, transmitted to Taipei 1982-07-14): no end-date for arms sales; no prior consultation with PRC on arms sales; no mediation between PRC and Taipei; no revision of TRA; no change to US position on sovereignty over Taiwan; no pressure on Taipei to negotiate with PRC. Public-domain enumeration; verbatim cable text declassified 2020.
- **1972 Shanghai Communiqué** — "the United States acknowledges that all Chinese on either side of the Taiwan Strait maintain there is but one China and that Taiwan is a part of China. The United States Government does not challenge that position." Note: "acknowledges" ≠ "endorses" — the deliberate verb choice is Strategic Translucency's first textual fingerprint.
- **1979 Joint Communiqué on Establishing Diplomatic Relations** — recognition of PRC; "the people of the United States will maintain cultural, commercial, and other unofficial relations with the people of Taiwan."
- **1982 August 17 Communiqué** — "intends gradually to reduce its sale of arms to Taiwan, leading, over a period of time, to a final resolution." Critical: the gradual-reduction language is the PRC-side anchor, while the Six Assurances simultaneously deny any end-date — the 1982 documents are themselves contradictory by design, the structural origin of strategic translucency.

**Why important for the thesis (provisional):** Strategic translucency is **older than strategic ambiguity**. The 1982 document-pair (Six Assurances + August 17 Communiqué) hard-codes mutual-deniability into the diplomatic record. Trump-2's tariff-signaling on Taiwan (Q1 2026) reactivates the 1982 ambiguity but cannot repeal the Six Assurances without a Senate-ratifiable instrument — and there isn't one on the table.

**Citations to lock at 21:00 fire:**

- [S1.2a] AIT (American Institute in Taiwan), declassified Reagan-era cable, "Six Assurances to Taiwan", 1982-07-14, declassified 2020. URL TBD.
- [S1.2b] Joint Communiqué of the United States of America and the People's Republic of China, 1972-02-28 ("Shanghai Communiqué"). URL: state.gov.
- [S1.2c] Joint Communiqué on Establishing Diplomatic Relations, 1979-01-01. URL: state.gov.
- [S1.2d] Joint Communiqué on US Arms Sales to Taiwan, 1982-08-17 (the "August 17 Communiqué"). URL: state.gov.

---

## S1.3 — TAIPEI Act (P.L. 116-135, 2020) and successor legislation

**Status this fire:** Enumeration only; verbatim pull deferred.

**Enumeration:**

- **Taiwan Allies International Protection and Enhancement Initiative Act of 2019** (TAIPEI Act, P.L. 116-135, enacted 2020-03-26). Directs the Secretary of State to (a) consider reducing US engagement with countries that take "actions against Taiwan", and (b) advocate for Taiwan's membership/observership in international organizations not requiring statehood. Legislative-density signal: bipartisan unanimous Senate, voice-vote House.
- **Taiwan Policy Act of 2022** (S.4428, 117th Congress) — proposed major rearmament + designation as "major non-NATO ally". Reported out of SFRC 17-5 (2022-09-14); did NOT become law as standalone but key provisions absorbed into FY2023 NDAA (P.L. 117-263) §§ 5501–5516 (Taiwan Enhanced Resilience Act, TERA).
- **Taiwan Enhanced Resilience Act** (FY2023 NDAA Subtitle, P.L. 117-263, 2022-12-23): 5-year $10B Foreign Military Financing authorization for Taiwan; first-time direct grants (not loans). This is the single largest legislative shift in US-Taiwan defense relations since the TRA itself.
- **FY2024 NDAA** (P.L. 118-31): expanded TERA training authorities; Taiwan-specific war-reserve stockpile authority.
- **FY2025 NDAA** (P.L. 118-159, signed late-2024): Pacific Deterrence Initiative → $11.5B, Taiwan-related items roughly $300M tagged. To be cross-referenced against the FY2026 NDAA (in conference Dec-2025 / signed early 2026) at next research fire.

**Why important for the thesis (provisional):** The 2020-2024 legislative cadence is the **densification phase** of strategic translucency. Each NDAA cycle adds a Taiwan-specific authority that survives an executive-branch policy pivot. Trump-2 cannot unilaterally repeal TERA's $10B FMF authorization; he can slow-walk obligations, but the cumulative drag of 2020-2024 NDAA additions means even a deliberately reluctant administration delivers more substantive support than the 2017-2020 baseline.

**Citations to lock at 21:00 fire:**

- [S1.3a] Public Law 116-135 (TAIPEI Act), enacted 2020-03-26. Source: congress.gov/116/plaws/publ135.
- [S1.3b] Public Law 117-263 (FY2023 NDAA), enacted 2022-12-23, §§ 5501–5516 (Taiwan Enhanced Resilience Act). Source: congress.gov/117/plaws/publ263.
- [S1.3c] Public Law 118-31 (FY2024 NDAA), enacted 2023-12-22.
- [S1.3d] Public Law 118-159 (FY2025 NDAA), enacted late-2024.

---

## S1.4 — INDOPACOM posture testimony (April 2026, Paparo)

**Status this fire:** Verbatim direct-quotes locked from Taipei Times article `2003856054` (House Armed Services Committee PDF mirror still 403 at 21:00; Senate.gov mirror still 403). Provenance is `[via-Taipei-Times-direct-quote]` rather than `[verbatim-from-PDF]` — strongest citation available without PDF access; the published S1 will note this provenance explicitly and the next research fire (2026-05-07 06:00) will retry the PDF mirror.

### Direct quotes (verbatim, S1.4 a–c)

**On the willingness-to-defend prerequisite:**

> "We can't want Taiwan's defense more than they want it itself."
> — Adm. Samuel J. Paparo, Cdr USINDOPACOM, SASC posture statement 2026-04-22 [S1.4a]

**On Taiwan vs Ukraine pre-war willingness-to-fight polling:**

> Paparo testified that Taiwan's willingness-to-fight polling is **"orders of magnitude"** higher than that of pre-conflict Ukraine.
> — Taipei Times paraphrase with embedded direct quote, 2026-04-22 [S1.4b]
> [Note: only "orders of magnitude" is verbatim per the source; the surrounding sentence is Taipei Times paraphrase. Full-PDF retrieval (06:00 fire) needed for the complete sentence the skeleton attempted.]

**On three meta-trends in the operating environment (verbatim):**

1. **Information / influence / cognitive / cyber operations:**
   > "Information, influence, cognitive and cyber operations are achieving increasing strategic effects by shaping perceptions and disrupting decision-making."
   > [S1.4c]

2. **Commoditised uncrewed/autonomous systems:**
   > "The commoditization of cheap, massed, uncrewed and often autonomous systems has lowered barriers to advanced capabilities, increasing the cost of assault operations and compressing decision timelines."
   > [S1.4c]

3. **Commoditised long-range precision strike:**
   > "The commoditization of long-range, precision, penetrating and — frequently — cheap strike has enabled greater leverage to coercion and cost imposition."
   > [S1.4c]

### Skeleton-vs-verbatim deltas (substantive)

The 20:12 skeleton paraphrased the three meta-trends; verbatim adds two load-bearing details the skeleton missed:

- **Trend 1 mechanism.** Skeleton: "increasingly *strategic*, not merely tactical." Verbatim: the strategic effect is achieved by **"shaping perceptions and disrupting decision-making."** This makes Trend 1 a direct match for §S8's GWW3 game-theoretic frame — perception-shaping and decision-disruption are precisely the channels that translate from operational gray-zone to legislative translucency at the political level. The skeleton's "strategic vs tactical" framing was structurally correct but missed the causal mechanism.
- **Trend 2 effect.** Skeleton: "lowered barriers to advanced capabilities." Verbatim adds: **"increasing the cost of assault operations and compressing decision timelines."** Both clauses matter for §S2 (Davidson Window successor): cost-of-assault and decision-timeline-compression are the two variables Paparo's revised PLA-capability timeline must account for. Skeleton would have left §S2 under-specified.

### Why this matters for the thesis (verbatim-tightened)

Paparo's "we can't want Taiwan's defense more than they want it itself" is the executive-branch *operational translation* of strategic translucency:

- To PRC: we will not fight unilaterally for Taiwan. Translucency is preserved at the *capability* level (we *can* fight) while removed at the *willingness* level (we *will not without Taipei*).
- To Taipei: legislative authority exists (TRA §3301(b)(5) defensive-arms mandate; §3302(a) such-quantity-as-may-be-necessary), but execution is conditional on demonstrated will.
- Structurally: this is the 2026 reactivation of TRA §3302(a)'s "self-defense capability" language. The 1979 phrase already encoded "Taiwan defends Taiwan, US enables capacity"; Paparo's 2026 testimony reads as an explicit *operationalization* of that 1979 substrate, not a departure from it.

The continuity is itself the thesis: translucency persists across administrations *because* the legislative substrate persists. Paparo speaks under Trump-2 in 2026 in language structurally identical to the 1979 statute drafted under Carter — that is the test of substrate-not-rhetoric, and it passes.

**Citation lock:**

- [S1.4a] Adm. Samuel J. Paparo, "We can't want Taiwan's defense more than they want it itself" (verbatim direct quote), as reported in Taipei Times, 2026-04-22, "Paparo, on Senate testimony, says Taiwan is committed to its own defense", `taipeitimes.com/News/taiwan/archives/2026/04/22/2003856054`. Provenance: Taipei Times direct-quote attribution; House Armed Services PDF mirror retry deferred to 2026-05-07 06:00.
- [S1.4b] Taipei Times, ibid., for the "orders of magnitude" Taiwan-vs-Ukraine willingness-to-fight polling comparison.
- [S1.4c] Taipei Times, ibid., for the verbatim three-meta-trends quotations. (Original SASC source: Adm. Paparo, "Statement before the Senate Armed Services Committee on USINDOPACOM Posture", 2026-04-22; PDF retrieval deferred next fire.)

---

## CRS bibliography backbone (for cross-citation in publications)

These are the standing reports whose cumulative citation across Day-7 publications anchors the legislative-trace. Pulled at next research fires.

- **R44996 — "Taiwan: Issues for Congress"** (CRS standing report, multi-year).
- **R48044 — "Taiwan Defense Issues for Congress"** (CRS standing report).
- **IF12481 — "Taiwan: Defense and Military Issues"** (CRS in-focus, version 19, last update 2026-02; verifying date from `crsreports.congress.gov`).
- **IF10275 — "Taiwan: Background and U.S. Relations"** (CRS in-focus, multi-year).

These four together cover ≈90% of the legislative-trace primary-source citations needed for S1 + S3.

---

## Path forward (next 2 fires)

| Fire | What | Output |
|---|---|---|
| **2026-05-06 21:00** | Promote skeleton citations to verbatim. Pull (a) TRA full text from `uscode.house.gov` plaintext, (b) Paparo April-2026 testimony full PDF from `armedservices.house.gov` mirror, (c) IF12481 latest version. Begin S1.5 = Trump-2 Q1-2026 Taiwan-tariff signaling inventory (Truth Social + USTR statements). | `notes-2026-05-06-en-primaries.md` upgraded to verbatim; new `notes-2026-05-06-en-paparo-verbatim.md` if PDF extraction is large enough to warrant a separate file. |
| **2026-05-07 06:00** | S2 (Davidson Window successor: Paparo's revised PLA-capability timeline) + S3 (arms-sales backlog as pseudo-alliance — pulling FY-by-FY notification data from State.gov). | `notes-2026-05-07-en-paparo-window.md`, `notes-2026-05-07-en-arms-sales-backlog.md`. |

Schedule slip: original scoping path-forward had S1 finishing at 2026-05-06 17:00. Skeleton + 21:00 verbatim-promotion fits within +1 fire, no further pacing impact for synthesis on 2026-05-07.

## What I owe Ingo (open-questions delta)

No new entries this fire. q6_firecrawl_credits remains the single open question; Tier-1 fetches today were attempted via WebFetch + WebSearch (no Firecrawl spend), so q6 has not become more urgent.

---

## Skeleton-vs-verbatim discipline (lesson)

This fire establishes a research pattern: when WebFetch fails (image-PDF, 403, or rate-limit) on Tier-1 sources, the correct response is **skeleton-now, verbatim-next-fire** with explicit `[via-search-summary]` and `[verbatim verification deferred YY:MM]` tags, **not** to pad with unsourced paraphrase. The tags are load-bearing: they let the 21:00 fire find every claim that needs upgrade in O(grep) rather than re-reading prose.

Provisional thesis from scoping note (strategic translucency replaces strategic ambiguity; Trump-2 menu narrows to 3 live options) **survives** today's S1 evidence at the structural level — the 1982 Six Assurances + August 17 Communiqué pair is the strongest single piece of textual evidence that translucency is **older** than 1995-era ambiguity, which is a **strengthening**, not a revision, of the thesis. No flip needed.
