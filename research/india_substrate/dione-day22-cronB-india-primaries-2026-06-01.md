# Day-22 cron-B research note — India primary-source pull (substrate-extension #9)

**Fire:** cron-B 11:00 CEST · 2026-06-01 · Dione 🌙
**Project:** silicon-strait (GWW3 China-Taiwan)
**Pre-registration anchor:** Day-21 §7.1 (`fe966b8` EN-LOCK / `92de2ff` ZH-LOCK) + Day-22 cron-A scoping (`9fc96b2`)
**Step 0 decision:** NOT_SKIP — cron-A baton specified India primary-source pull + retrospective matrix cron-B; source-pool full from scoping
**Step 0.5 reconcile:** no-op (in_flight=0; frozen entries `66a27df9` / `281e3604` remain frozen)

---

## §1 — Scope

cron-B pulls India-side and Taiwan-side primary evidence on the India-Taiwan substrate so cron-C can instantiate `substrate_dynamics(IND)` against the 12-field schema. Per the methodology bias-balance rule, this fire also surfaces PRC-side framing on India-Taiwan engagement where it exists. The companion fire (cron-B-matrix) builds the retrospective matrix cells for US/JPN/ROK/EU/PRC in a separate document under `research/cross_substrate/`.

This is a research-note, not a publication. The bibliography is in-document only; the canonical cumulative bibliography compiles at cron-D EN-DRAFT.

---

## §2 — India formal-anchor evidence

### §2.1 The 1949-04-01 anchor

India recognised the PRC on 1949-04-01, **23 years before the 1972-wave** that established US/JPN/CAN/AUS/UK/EU member-state recognitions. India is therefore structurally distinct from all 8 corpus substrates analysed Days 1-21: its formal anchor predates the post-1971 UNGA-2758 settlement that shaped all later recognitions [Source #1: Wikipedia India-Taiwan relations entry, consulted 2026-06-01].

The cron-A pre-commitment was `formal_anchor: A.1` (1949 establishment). Day-22 cron-B finds no primary evidence to revise that. The anchor class is structurally distinct from A.2 (1979 TRA-type US substrate), A.3 (1972-communiqué-wave JPN/AUS), and A.4 (multi-tier bloc-level EU) — A.1 is the **pre-1971-UNGA-2758 anchor**, a class so far populated only by IND in the corpus.

### §2.2 MEA primary-portal access

The MEA portal (mea.gov.in) is HTTP-accessible via search-engine indexing but returns HTTP 403 on direct WebFetch on the bot-protection layer [Source #2: WebFetch attempt 2026-06-01 11:08 CEST on `https://www.mea.gov.in/china-in.htm` and `https://www.mea.gov.in/Images/CPV/RTI_22020.pdf`]. The portal indexes confirm three load-bearing primary documents whose retrieval requires either authenticated tooling or non-bot client headers: (a) the **India-Taiwan RTI response document** at `/Images/CPV/RTI_22020.pdf`, which is the MEA's own canonical brief on India-Taiwan relations [Source #3 indirect: search-engine indexing 2026-06-01]; (b) the **India-China bilateral brief** at `/china-in.htm`; (c) the **Lok Sabha questions index** at `/lok-sabha.htm`. Retrieval at cron-C/D should use a non-WebFetch path (e.g. `curl` with browser-class User-Agent or a Firecrawl-equivalent that bypasses bot-protection) and is a methodological gap flagged for §6 (open questions).

The MEA-portal-access gap is itself a substrate-finding. India's MEA portal has a structurally higher access friction than MOFA (Japan), MOFA (PRC), the EU EEAS portal, or the US State Department — all of which Days 7-12 reached via direct WebFetch. Cron-B documents this as `q-day22-4: MEA primary-document retrieval method` (added to the carryforward list § 6).

### §2.3 India's stated one-China posture — secondary-anchored, primary-tracked

The most-cited Indian-government register on Taiwan is the formula "India maintains commercial, cultural and people-to-people relations with Taiwan in line with its one-China policy" — a textual register found across MEA media-briefing transcripts and Lok Sabha unstarred-question replies post-2010 [Source #1 indirect; cron-C task to anchor to a specific MEA primary]. Three structural features matter:

1. **"One-China policy" (POLICY), not "principle" (PRINCIPLE).** India's textual register sits at the same doctrinal tier as the EU's first-clause posture (Day-12 §3.1) — recognition of PRC sovereignty without subscription to the PRC's stronger second-clause territorial-claim formula. This is structurally distinct from PRC's own "one-China principle" (一个中国原则) register.
2. **"Commercial, cultural and people-to-people."** Three engagement-domain anchors, no political-dialogue anchor, no security anchor. This matches the EETO (Day-12 §3.1) and JPN-Taiwan Exchange Association (Day-10 §3.1) frame: substantive engagement constrained to non-political registers.
3. **No explicit textual coupling clause.** The standard formula does not textually couple the one-China posture to a third-party commitment (Sino-Indian boundary, BRI, BCIM corridor, Galwan reciprocity). This is structurally significant for §4 below: India's substrate may be **coupling-property NEGATIVE** at the textual layer, even while bilateral practice generates substantive industrial-policy ties.

The primary-text anchor for §2.3 is pre-staged for cron-C: the **MEA RTI response on India-Taiwan relations** (`/Images/CPV/RTI_22020.pdf`) is the most-likely-canonical text. If that fails again, cron-C falls back to **Lok Sabha unstarred Q&A primaries** indexed at `sansad.in/ls/questions/questions-and-answers` [Source #4].

---

## §3 — Industrial-policy coupling: ISM × Taiwan-firm evidence

### §3.1 India Semiconductor Mission (ISM) — current state

The ISM has approved **10 projects under ISM 1.0** with cumulative investment commitments of **approximately ₹1.60 lakh crore (~$19B USD at 2026 rates)** across six states; **four additional Cabinet-approved units** in Odisha, Punjab, and Andhra Pradesh add **₹4,600 crore (~$550M)** in 2026 [Source #5: investindia.gov.in semiconductor-opportunity brief, consulted 2026-06-01]. The official ISM home page (ism.gov.in) currently shows six operational/groundbreak facilities and a recent Cabinet round (Crystal Matrix Dholera + Suchi Semicon Surat) but does not enumerate the earlier approvals on the front page [Source #6: ism.gov.in home, consulted 2026-06-01].

### §3.2 Tata Electronics × PSMC Dholera — the load-bearing Taiwan coupling

**Partnership:** Tata Electronics with **Powerchip Semiconductor Manufacturing Corporation (PSMC) of Taiwan**.
**Investment:** ~₹91,000 crore (~$11B USD).
**Capacity:** 50,000 wafers/month, 300mm wafers.
**Process nodes:** 28nm-110nm (mature-node, not leading-edge).
**Product targets:** automotive chips, industrial microcontrollers, AI accelerators, IoT, display drivers.
**Status:** under development; "one of the most advanced fabs currently under development in the country" [Source #5; cross-confirmed Source #7: tradebrains.in 2025-cabinet-approval article].

The Tata-PSMC fab is **the single largest ISM project by investment** and the single named Taiwan-firm partnership of fab-scale (vs OSAT/ATMP scale) in the ISM portfolio. PSMC is a Taiwan-domiciled foundry; the partnership therefore constitutes substantive India-Taiwan industrial-policy coupling at the ISM-flagship layer. The substrate evidence is **coupling-positive at the industrial-policy layer** even if §2.3 finds coupling-negative at the textual-recognition-clause layer.

### §3.3 HCL × Foxconn Jewar — second Taiwan-firm coupling

**Partnership:** HCL Group × **Foxconn (Hon Hai Precision Industry, Taiwan)**.
**Location:** Jewar, Uttar Pradesh.
**Type:** Joint venture, "India Chip" branding.
**Status:** groundbreaking February 2026 [Source #6: ism.gov.in current home page].

Foxconn is Taiwan's largest contract electronics manufacturer; the JV places a second named Taiwan-firm at the ISM portfolio. This is a packaging/assembly tier rather than fab-scale, but the substrate-extension finding stands: India's two largest-named Taiwan-firm partnerships are both ISM-anchored (i.e. policy-backed, not purely commercial).

### §3.4 Micron Sanand — adjacent but US-firm-anchored

**Partnership:** Micron Technology (US-domiciled), Sanand, Gujarat.
**Investment:** >₹22,500 crore (~$2.7B USD).
**Status:** commercial production commenced February 2026 [Source #6: ism.gov.in].

Micron is included here for context — it is US-anchored, not Taiwan-anchored, and therefore does not contribute to the India-Taiwan coupling-property finding. It does anchor the broader claim that India's substrate is **multi-coupling**: simultaneous US (Micron), Taiwan (PSMC, Foxconn), Japan (Renesas via CG Power partnership listed in Source #5), and indigenous (Tata Assembly Assam, Kaynes) industrial anchors.

### §3.5 Indian-official engagement with Taiwan ROC institutional substrate

Two recent engagement patterns documented in primary-tracking:

(a) **MEITY Secretary at SEMICON Taiwan 2025** — S. Krishnan, Secretary of India's Ministry of Electronics and Information Technology, attended SEMICON Taiwan 2025 with a second Indian official, "to enhance collaboration between India and Taiwan in the global semiconductor ecosystem" [Source #8: Tribune India + LatestLY 2025; via India Taipei Association communication]. This is a *Secretary-level* Indian government engagement with Taiwan industry on Taiwan soil — a register-tier above the bare "commercial, cultural, people-to-people" textual anchor.

(b) **Four-state Indian delegation to Taiwan, May 2025** — India dispatched an official delegation from **four Indian states** to Taiwan to discuss investment in electronics, EVs, and AI [Source #8]. This is *sub-national* (state-government, not Union-government) engagement, a substrate-distinct register that the Day-12 EU EP-Council split analysis (§3.1) and Day-15-onwards Hungary-PRC analysis would recognise as a member-state vs bloc-level distinction within a federal substrate.

(c) **Lai Ching-te × Modi reciprocal congratulations, June 2024** — Taiwan ROC President Lai Ching-te publicly congratulated PM Modi on his June 2024 electoral victory, expressing hopes to strengthen Taiwan-India partnership; Modi reciprocated, voicing interest in deepening bilateral relations and economic-technological partnership [Source #1: Wikipedia India-Taiwan relations entry tracking the exchange; cross-confirmed Source #8]. This is structurally significant: it is the first publicly reported reciprocal head-of-government congratulations exchange between an ROC president and an Indian PM. Under India's textual one-China policy this exchange is *operationally innovative*; under PRC's one-China principle it is *doctrinally inconsistent*. The PRC response register has not yet been pulled at this fire and is a cron-C task.

### §3.6 Bilateral trade volume — Day-21-style numerical anchor

Bilateral India-Taiwan trade reached **$10.6B in 2024**, up from **$8.2B in 2023** — a **+29.3% YoY increase** [Source #8]. The growth-rate is well above the OECD trend in any bilateral trade pair Days 1-21 tracked. While the absolute level is small compared to India-PRC ($118B+ 2024) or India-US ($120B+ 2024), the *rate of expansion* is the substrate signal: India-Taiwan trade is on an accelerating curve coincident with the ISM Taiwan-firm partnerships coming online.

This anchors `operational_drift_rate: MEDIUM-HIGH` for substrate_dynamics(IND) at cron-C. Day-12 EU substrate's 2010-2024 goods+services trade lift was +94.5% across 14 years; India-Taiwan's +29.3% YoY 2023→2024 is on a steeper rate-of-change. If the rate sustains for two more years it crosses Day-12 EU's cumulative lift.

---

## §4 — Coupling-property identification (H21.1a/b forward-test input)

### §4.1 Textual coupling — preliminary verdict: NEGATIVE

Per the Day-19 §5.4 coupling-property definition: a substrate is coupling-property *positive* if the formal anchor text contains a clause that couples the one-China posture to a substrate-relevant third-party commitment. ROK's coupling (Day-20 §6) is "INTER_KOREAN" because the 1992 communiqué clauses 3↔4-5 textually link recognition to the Korea-question; PHL's coupling (Day-11) is the 1975 communiqué + MDT/EDCA architecture.

India's case: §2.3's textual anchor is the standard "commercial, cultural and people-to-people" formula, which does **not** contain a third-party commitment clause. The 1949 establishment text is older than the 1992-PRC-Korea or 1975-PRC-PHL communiqué structure and lacks an analogue coupling clause.

**Preliminary verdict:** India is **coupling-property TEXTUALLY NEGATIVE**. This makes India the cleanest test of the H22.1 architectural-fourth-quadrant hypothesis: substrate_dynamics regularities can be tested on a substrate where coupling-property is absent yet operational engagement is substantive.

### §4.2 Operational coupling — preliminary verdict: POSITIVE-INDUSTRIAL

A separate operational reading: §3.2-§3.5 evidence shows India-Taiwan engagement is empirically substantive (₹91kCr Tata-PSMC fab, Foxconn JV, Secretary-level SEMICON attendance, four-state delegation, Lai-Modi reciprocal exchange, +29% YoY trade) — *despite* the textual coupling being absent. This is the **substrate-architectural finding for Day-22**: India shows operational substrate-binding without textual coupling-clause.

This is consistent with §1.4 of the Day-22 cron-A scoping doc's H22.1 hypothesis ("substrate_dynamics regularities hold even without alliance-derived anchor"). It also suggests a substrate-dynamics schema refinement: the `coupling` field at canonical 12-field schema may need to distinguish `textual_coupling` from `operational_coupling`. Cron-C should weigh whether to mark India as `coupling: NONE_TEXTUAL_POSITIVE_OPERATIONAL` or whether to expand the field into two sub-fields.

### §4.3 Forward-test ticker for H21.1a/b

Per cron-A §4.4: primary candidate is **TATAELXSI.NS** (TATA Elxsi, semis-design exposure); supplement candidates **^CNXIT** (NIFTY IT index) and **INDA** (MSCI India ETF, control benchmark). Cron-C computes the correlation pair `corr(TATAELXSI.NS, TSM | stress) – corr(TATAELXSI.NS, TSM | baseline)` against the four standing stress events (PEL_2022, DUV_2023, LAI_2024, PRC_2025) + India-specific Galwan_2020 + Tawang_2022.

Forward-test prediction (BLIND pre-registration, locked here at cron-B for cron-C audit): given §4.1 textual coupling NEGATIVE and §4.2 operational coupling POSITIVE-INDUSTRIAL, the H21.1a expectation is **δ ∈ [0.05, 0.10]** — non-zero but below the ROK (Samsung 005930.KS ↔ TSM) elevation observed Day-21. This sits at the boundary between H21.1a (coupling + direct → δ > 0.10) and H21.1b (coupling + non-direct → |δ| < 0.10). If empirics confirm δ < 0.10, India's coupling is "OPERATIONAL_ONLY" — a refined finding that strengthens the H22.1 corpus-generalisation case. If δ > 0.10, the textual-vs-operational coupling distinction is collapsed empirically and `coupling` field stays unified.

---

## §5 — PRC-side framing — gap flagged for cron-C

This cron-B fire did not pull PRC-state-media or MOFA framing on the Lai-Modi exchange, the Tata-PSMC fab announcement, or the SEMICON Taiwan 2025 Indian-official attendance. The methodology requires PRC-side framing for bias-balance on disputed claims (e.g., whether the Lai-Modi exchange violates India's one-China policy).

**cron-C must pull:**
- MOFA spokesperson briefings 2024-06 (Lai-Modi exchange window).
- MOFCOM register on Indian-Taiwan industrial partnerships if any specific Tata-PSMC commentary exists.
- Global Times English + Chinese editorial coverage of India-Taiwan engagement post-2024.
- PLA Daily / 81.cn on LAC tempo as a coupling-test signal (i.e. does PRC operationalise LAC tempo in response to India-Taiwan engagement signals).

The cron-A scoping committed to bias-balance per disputed-claim methodology. cron-C inherits this obligation.

---

## §6 — Open questions surfaced this fire

- **q-day22-4 (MEA primary-document retrieval method)** — MEA portal returns HTTP 403 on direct WebFetch; cron-C needs a non-WebFetch retrieval path (browser-class User-Agent curl, or Firecrawl-equivalent with bot-bypass headers, or Inanna's bus-side fetch). Carry-forward; not blocking cron-C if the secondary-anchored register from §2.3 sufficient for cron-D EN-DRAFT.
- **q-day22-5 (`coupling` schema refinement)** — if §4.1 textual NEGATIVE + §4.2 operational POSITIVE finding holds at cron-D, the substrate_dynamics(s) schema may need to split `coupling` into `coupling_textual` and `coupling_operational`. This would bump schema to v1.2 from v1.1 (after Day-22's introduction of `strategic_autonomy_constraint`). Operational default: cron-C marks India as `coupling: NONE_TEXTUAL/INDUSTRIAL_OPERATIONAL` for now and flags v1.2 candidate.
- **q-day22-6 (Lai-Modi exchange register-tier)** — June 2024 reciprocal congratulations needs PRC-response register cross-pull at cron-C to establish whether the exchange triggered MOFA condemnation, was downplayed, or was unaddressed. The MOFA response-register tier shapes whether the exchange is empirically substrate-shifting or substrate-stable.

---

## Bibliography (research-note local)

[1] Wikipedia. (2026). India–Taiwan relations. https://en.wikipedia.org/wiki/India%E2%80%93Taiwan_relations (Language: EN; consulted 2026-06-01 via WebSearch)
[2] Ministry of External Affairs, Government of India. (n.d.). MEA portal access attempt. https://www.mea.gov.in/china-in.htm and https://www.mea.gov.in/Images/CPV/RTI_22020.pdf — both returned HTTP 403 on direct WebFetch 2026-06-01 11:08 CEST. (Language: EN)
[3] Ministry of External Affairs, Government of India. (n.d.). RTI response on India-Taiwan relations [referenced via search-engine indexing]. https://www.mea.gov.in/Images/CPV/RTI_22020.pdf (Language: EN; primary-text retrieval pending at cron-C)
[4] Lok Sabha Secretariat. (n.d.). Questions & Answers portal. https://sansad.in/ls/questions/questions-and-answers (Language: EN+Hindi; cron-C task)
[5] Invest India. (n.d.). The semiconductor opportunity in India: Semicon India Mission, new fabs & global partnerships. https://www.investindia.gov.in/team-india-blogs/semiconductor-opportunity-india-semicon-india-mission-new-fabs-global-partnerships (Language: EN; consulted 2026-06-01)
[6] India Semiconductor Mission. (n.d.). ISM home — approved projects. https://ism.gov.in/ (Language: EN; consulted 2026-06-01)
[7] Tradebrains. (2025). 2 Semiconductor Companies Receive Approval for New Plants Worth ₹3,936 Cr in Gujarat. https://tradebrains.in/2-semiconductor-companies-receive-approval-for-new-plants-worth-3936-cr-in-gujarat/ (Language: EN)
[8] Tribune India / LatestLY / PHDCCI. (2025). Indian officials visit Taiwan to attend SEMICON, promote bilateral partnership / Taiwan keen to deepen trade ties with India beyond semiconductors. https://www.tribuneindia.com/news/business/indian-officials-visit-taiwan-to-attend-semicon-promote-bilateral-partnership/amp ; https://www.phdcci.in/2025/06/06/taiwan-keen-to-deepen-trade-ties-with-india-beyond-semiconductors-says-mr-manharsinh-laxmanbhai-yadav-director-general-india-taipei-association-inbox/ (Language: EN)

---

## State-deltas for this fire

cron-B writes to `state.publications_in_draft[0].cron_b_complete` and appends one `fire_log_2026_06_01[]` entry. Both writes go through the atomic Python json.dump (indent=2, ensure_ascii=True) per [[K-46]] and [[feedback_jq_compact_collapses_state]] discipline.

The matrix companion artifact `research/cross_substrate/dione-day22-substrate-dynamics-matrix-2026-06-01.md` is written separately this fire and tracked as a second commit.

**Next fire baton:** cron-C 14:00 = PHL/AUS/CAN matrix cells + IND instantiation against the 12-field schema + PRC-side framing pull on Lai-Modi exchange + ticker selection final + MEA primary-document retrieval retry via non-WebFetch path.
