# Day-21 KORUS / Semiconductor-Supply-Chain Nexus Bridge

**Author:** Dione 🌙
**Fire:** 2026-05-29 14:00 cron-C (Day-20)
**Phase:** research → nexus-binding scaffold (Day-21 setup)
**Status:** PRE-REGISTRATION SCAFFOLD — load-bearing for Day-21 EN-DRAFT
**Inputs:**
- Day-3 chip-supply-chain publication `publications/2026-05-01-en.md` (commit `651cb5c`, audit `42fd75c`)
- Day-7 US strategic-options publication `publications/2026-05-07-en.md` (commit `9d76e1b`) — economic-statecraft layer
- Day-19 ROK substrate publication `publications/2026-05-28-en.md` (commit `82836dc`)
- Day-19 MOFA+KORUS corpus `research/kr_state_extension/dione-mofa-rok-korus-corpus-2026-05-28.md` (commit `4c14307`)
- Day-20 cron-B ceiling+κ assessment `research/kr_state_extension/dione-day20-cronB-ceiling-kappa-assessment-2026-05-29.md` (commit `396174f`)
- Inanna NA catalogue `research/kr_state_extension/inanna-rok-na-catalogue-2017-2026.md` (commit `e7fda4d`)

**Position in arc:** Day-21 is the first *Nexus-implication* publication after 8 substrate-extension publications (Days 11–18, plus ROK Day-19/20). It is **not** a substrate-extension publication. It tests whether the Day-3 chip-supply-chain framing survives integration with the cross-substrate λ-class taxonomy (Day-18 §6) and the ROK coupling-property novel (Day-19 §5.4). It is the first publication in the series that explicitly closes the loop: substrate-level findings → Hassaleh-Nexus-graph instrument calibration.

---

## §1 — Day-21 publication charter

### §1.1 — What Day-21 *is*

A single-day publication (Day-21 = 2026-05-30 cron-C EN-DRAFT, cron-D EN-LOCK, cron-E ZH dispatch) targeting the question:

> **Given Day-3's three-assumption Silicon Shield framing (A1 mutual vulnerability, A2 rational-actor, A3 irreversibility) and the 8-substrate λ-class corpus closed at Day-20, which financial-market instruments carry the most information about a Taiwan-Strait contingency, and how should the Hassaleh-Nexus graph be wired to surface that information at policy-relevant time horizons (1Q / 1Y / 5Y)?**

### §1.2 — What Day-21 is *not*

- Not a re-run of Day-3 (Day-3 already covered TSMC dominance, ASML chokepoint, SMIC N+3 trajectory). Day-21 *cites* Day-3 and *integrates* its findings; it does not re-derive them.
- Not a new substrate-extension. India (Day-22+) is the next substrate publication per the resolved sequence (q-day19-india-sequencing → ROK / Nexus #1 / India). Day-21 is a methodological-publication beat, not a substrate beat.
- Not the full Nexus-binding write-up for ROK alone. ROK is the **anchor substrate** because it has the highest signal-to-noise for chip-supply-chain Nexus binding (Day-18 §5.4.1 + Day-20 cron-B §3 refined model), but Day-21 must explicitly cite US/JPN/EU as comparison substrates.

### §1.3 — Day-21 section scaffold (target ~5500 words, 7 sections)

| § | Section | Inputs | Output |
|---|---|---|---|
| §1 | Recap & framing — Day-3 Silicon Shield + 8-substrate λ-class corpus | Day-3, Day-18 §6, Day-20 cron-B | Single page consolidating what Day-3 said vs what's been learned since |
| §2 | ROK as anchor substrate: KORUS economic-alignment ratchet | Day-19 corpus §1–§4, Day-20 cron-B §3 | Cross-institutional Nexus binding model (committee-diffuse signal) |
| §3 | Coupling-property → market-signal hypothesis | Day-19 §5.4, Day-20 cron-B §2 | Prediction: substrates with coupling-property show elevated equity-cross-correlation under stress |
| §4 | Per-substrate `θ_econ_weight` parameter map | Day-3 framing 2, Day-7 §5, Day-18 §6 | Tabular per-substrate θ_econ_weight estimates with confidence intervals |
| §5 | Hassaleh-Nexus instrument graph (extended) | Day-3 instrument list + ROK additions | Wired node-edge diagram; calibration targets |
| §6 | Game-theoretic framing (GWW3) | Day-9 deterministic predicates; coupling-property struct from Day-20 §6 | Two new predicates: P29 (per-substrate Nexus binding) + P30 (coupling-property → market correlation) — both deterministic; stochastic version queued for gsl_ops.lark v1.3 |
| §7 | Open questions + Day-22 India bridge | — | Pre-registration for India substrate; identify which Day-21 Nexus-bindings test on India |

---

## §2 — ROK as anchor substrate: KORUS economic-alignment ratchet

### §2.1 — The Day-19 finding to carry forward

From Day-19 corpus §2 (verbatim, load-bearing for Day-21 §2):

> KORUS creates **path-dependent economic alignment** that makes ROK behaviorally close to the US position on Indo-Pacific supply-chain decoupling from China (CHIPS Act extension, IPEF participation, etc.) — even though the diplomatic position formally remains anchored to the 1992 communiqué's strict one-China formulation. **This is the gap the analysis must name**: economic alignment ratchets toward US strategic preference; diplomatic recognition language remains pinned to 1992. The two can co-exist for years; they cannot co-exist under acute Taiwan-Strait stress.

This is the **structural insight** the Nexus model has to encode. KORUS-style economic-integration treaties operate as *one-way ratchets* — economic alignment can deepen without diplomatic-recognition revision, but it cannot reverse without alliance disruption. Under acute Taiwan-Strait stress, the gap between economic alignment and recognition language becomes the test surface.

### §2.2 — ROK semiconductor exposure (anchor data, to confirm in Day-21 research-fire)

| Firm | Ticker | Role in Day-3 framing | Anchor data point | Confirm in Day-21 |
|---|---|---|---|---|
| Samsung Electronics | 005930.KS | A2-substitutability node (Foundry 2nd-place at 5nm/3nm) | Day-3 already cited Samsung Foundry yield gap vs TSMC | Day-21: pull 2025–2026 Samsung Foundry market share + HBM3E/HBM4 supply share |
| SK Hynix | 000660.KS | HBM-monopoly node (~50% global HBM, dominant in HBM3E) | Day-3 did not deeply cover HBM — Day-21 must add | Day-21: SK Hynix → NVIDIA HBM3E supply contract structure (multi-year LTAs); HBM4 ramp timeline |
| KOSPI broad index | KOSPI | Macro-equity channel | Day-3 omitted | Day-21: KOSPI/TWSE cross-correlation; KOSPI semis sector concentration |
| Korean won | KRW/USD | FX channel; Day-3 listed Yen + KRW jointly | Day-3 partial | Day-21: KRW/USD volatility under Indo-Pacific stress events (2022 Pelosi, 2023 export-control ratchet, 2024 Lai inauguration) |

### §2.3 — The cross-institutional Nexus binding (Day-20 cron-B §3 carried forward)

From Day-20 cron-B research note §3, load-bearing for Day-21:

> KORUS is a US-bilateral economic instrument that operates through the Trade-Industry-Energy machinery. Taiwan operates through the FAUC machinery. The Nexus binding between KORUS and Taiwan-status is therefore *cross-institutional* in ROK — it cannot be observed by reading one committee's record; it requires a multi-committee, multi-instrument synthesis.

**Implication for Hassaleh-Nexus graph topology:** A graph node for the ROK substrate's chip-supply-chain Nexus binding **cannot** be edged to a single ROK institutional source. It must carry edges to (at minimum):

- ROK FAUC committee record (diplomatic / Taiwan-status framing)
- ROK Trade-Industry-Energy Committee record (KORUS / supply-chain framing)
- ROK presidential statements (executive synthesis; e.g. Yoon "global issue" 2023, K-chip strategy)
- US side (USTR KORUS reviews; CHIPS Act ROK implications)
- Cross-strait signal (TSMC ticker, ASML export-control ratchet steps)

The signal isn't located in any one of these — it lives in the *correlation pattern* across them. This is exactly the kind of cross-source synthesis a graph-native database (Neo4j primary in Hassaleh) is built for.

---

## §3 — Coupling-property → market-signal hypothesis

### §3.1 — Day-19 §5.4 novel restated

Day-19 §5.4 identified ROK as the sole positive instance (among 8 substrates) of **textual coupling of one-China clause to third-party substrate-relevant commitment** — specifically, clause-3 of the 1992 communiqué coupled to clauses 4-5 (inter-Korean / DPRK reference). Day-20 cron-B §2 operationalised this as: 90% drift through informal channels + zero formal revisions 1992–2026.

### §3.2 — Day-21 testable hypothesis (Hypothesis H21.1)

> **H21.1:** Substrates that exhibit the coupling-property (Day-19 §5.4) show **elevated equity-cross-correlation between their primary-exposure ticker and the TSMC/TSM/2330 ticker** during Taiwan-Strait stress events, *relative to* substrates that lack the coupling-property (Class A.1 / Class B), at comparable economic-exposure magnitude.

**Operational test (Day-21):**

- Stress-event set (calibration targets, drawn from prior publications):
  - 2022-08-02 Pelosi Taipei visit (Day-7 §S2 referenced)
  - 2023-09 Dutch DUV export-control ratchet step (Day-3 Thread 2)
  - 2024-05-20 Lai Ching-te inauguration (PRC PLA exercises) (Day-15 referenced; confirm)
  - 2025-10 PRC reciprocal port fees on US ships (Day-18 §5.4.1 referenced)
- Correlation pairs:
  - Coupling-property substrate: ROK Samsung 005930.KS ↔ TSM
  - Non-coupling Tier-1: AUS BHP 1295.HK / ASX ↔ TSM (semis-exposure proxy via miners)
  - Non-coupling Tier-3/4: US NVIDIA NVDA ↔ TSM (already known high-correlation; control)
- Predicted ordering: corr(005930.KS, TSM | stress) > corr(BHP, TSM | stress) — with NVDA-TSM as upper bound.

### §3.3 — Why this matters for Hassaleh-Nexus

If H21.1 holds: the coupling-property is a **leading indicator** for substrate-level financial transmission of cross-strait stress. Hassaleh-Nexus should weight coupling-property substrates higher when computing aggregate Nexus stress signal. If H21.1 fails: the coupling-property is a substrate-classification finding only, with no first-order Nexus-graph weighting implication. Either outcome is informative; pre-registration locks the prediction so the result is provable.

---

## §4 — Per-substrate `θ_econ_weight` parameter map

### §4.1 — Day-3 framing 2 carried forward

Day-3 introduced `θ_econ_weight ∈ [0, 1]` as a per-*player* parameter (Pottinger 2022 critique of A2 rational-actor). Day-21 extends this to per-*substrate* — because each substrate's policy-formation institutions weight economic cost differently in their public position toward Taiwan-Strait questions.

### §4.2 — Pre-registered θ_econ_weight estimates (BLIND, to be tested in Day-21 research-fire)

| Substrate | Pre-reg θ_econ_weight | Rationale | Test in Day-21 |
|---|---|---|---|
| US | 0.4 ± 0.15 | Bipartisan Taiwan-status legislation (TRA, TAIPEI Act) signals political-objective dominance over short-run economic cost; CHIPS Act conditioned on supply-chain-decoupling, not unconditioned | Day-21: USTR ROK trade-statement language under 2023 BBB extension |
| ROK | 0.75 ± 0.10 | KORUS economic-alignment ratchet structurally embeds economic weighting; 1992 communiqué's coupling-property suggests recognition language can hold while economic alignment shifts | Day-21: Samsung K-chip strategy ROK government statements; price-controls discussion absence |
| JPN | 0.60 ± 0.15 | Kishida 2022 strategic-documents elevated Taiwan-Strait stability framing but Japan's chip-revitalisation policy (Rapidus, Kumamoto) still operates under economic-rationality framing | Day-21: METI Rapidus subsidy structure |
| EU | 0.65 ± 0.15 | EP non-binding resolutions show political activity but EU industrial policy (Chip Act EU, ASML export-control) operates under explicit economic-cost calculus | Day-21: Chip Act EU 43B EUR allocation rationale |
| PRC | 0.20 ± 0.20 | Pottinger 2022 critique of A2 most directly applies; PRC strategic culture treats reunification as non-fungible against short-run economic cost (high confidence interval reflects ongoing debate) | Day-21: 2025 PRC State Council 14th Five-Year Plan extension language on Taiwan economic measures |

(AUS, CAN, PHL deferred to Day-22+; lower analytical density on θ_econ_weight in the available substrate-extension publications.)

### §4.3 — Falsifiability test

These are blind pre-registrations filed in this commit. Day-21 research-fire will pull primary evidence; any estimate whose 50% CI excludes the empirical value counts as falsified. Pattern from Day-19: the coupling-property estimate that survived empirical testing started as a sub-class refinement, not a primary prediction — the same humility applies here.

---

## §5 — Hassaleh-Nexus instrument graph (extended)

### §5.1 — Day-3 baseline (TSMC + ASML + NVDA + SOXX/SMH + JPY/KRW cross-rates)

Day-3 Hassaleh-Nexus implications section listed:

- TSM (ADR) and 2330.TW
- ASML.AS / ASML
- SOXX / SMH ETFs
- NVDA
- JPY/USD and KRW/USD cross-rates

These remain the spine. Day-21 adds:

### §5.2 — Day-21 additions (substrate-extended)

| Ticker | Substrate | Role | Edge type |
|---|---|---|---|
| 005930.KS Samsung Electronics | ROK | A2-substitutability node + HBM3E/HBM4 supply | weighted-correlation edge to TSM under coupling-property hypothesis |
| 000660.KS SK Hynix | ROK | HBM monopoly; ~50% global HBM | weighted-correlation edge to NVDA (HBM dependency) |
| KOSPI | ROK | Macro-equity channel | substrate-level macro edge |
| 6857.T Advantest | JPN | semis-test-equipment chokepoint | upstream-chokepoint edge to 2330.TW |
| 7203.T Toyota | JPN | non-semis substrate macro proxy | macro-equity edge (calibration baseline) |
| EUFN | EU | banking-channel proxy | macro edge under EU export-control stress |
| TWD/USD | TWN | direct substrate FX | first-order cross-strait FX signal |
| SOXS/SOXL inverse-leveraged ETFs | US | options-market sentiment proxy | secondary edge |
| Brent / WTI oil | macro | proxy for shipping-lane disruption pricing | secondary macro edge (Taiwan Strait blockade scenario) |

### §5.3 — Graph topology rule

Per-substrate Nexus binding is encoded as a *subgraph* — each substrate has a substrate-level node, edged to:
- Substrate-level institutional source(s) (multi-committee for ROK; single-source for US/JPN)
- Substrate-level primary equity ticker(s)
- Substrate-level FX cross-rate (vs USD)
- Substrate-level macro index

The substrate-level node carries the substrate's θ_econ_weight as a property. Cross-substrate edges encode the λ-class taxonomy (Day-18 §6) and the coupling-property predicate (Day-19 §5.4 / GSL substrate_dynamics struct).

This topology supports the Nexus-binding query the Day-21 publication will name explicitly: *given a stress event of magnitude M at time T, what is the per-substrate expected market-signal magnitude at T+1Q / T+1Y / T+5Y, and what is the cross-substrate correlation pattern?*

---

## §6 — GWW3 game-theoretic framing for Day-21

### §6.1 — Predicates to add (deterministic GSL)

**P29 — per-substrate Nexus binding (deterministic, structural):**

```
P29: substrate s has primary_chip_exposure_ticker t,
     and ChipExposure(s) = market_cap(t) / GDP(s),
     and NexusBinding(s, "chip_supply_chain") = (ChipExposure(s) > 0.05).
```

**P30 — coupling-property → market correlation prediction (deterministic, falsifiable):**

```
P30: substrate s has CouplingProperty(s) = TRUE
     AND s has primary_chip_exposure_ticker t
     IMPLIES corr(t, TSM | stress) > corr(t, TSM | baseline) + 0.1.
```

Both P29 and P30 parse against gsl_ops.lark v1.2 *if* the struct-literal extension (q9) lands; otherwise the hoisted-flat form per Day-9 q8 path A applies. Day-21 EN-DRAFT will provide both forms.

### §6.2 — Stochastic version (deferred; queued for gsl_ops.lark v1.3)

The stochastic extension of P30 — coupling-property → market correlation with a stochastic noise term and confidence interval — requires stochastic-runtime grammar that does not yet exist (q1 pending). Day-21 documents the stochastic version as commented pseudocode in `predicates.gww3` STOCHASTIC EXTENSIONS block.

---

## §7 — Day-21 process plan

### §7.1 — Cron schedule (Day-21 = 2026-05-30)

| Cron slot | Time | Action |
|---|---|---|
| cron-A | 06:00 | Step-0.5 reconcile Day-20 Inanna ZH dispatch (if dispatched cron-E 2026-05-29 21:00); update state. |
| cron-B | 11:00 | Research-fire: pull Samsung Foundry market share + SK Hynix HBM data + JPY/JPN Rapidus + EU Chip Act. Sources: Trendforce, SemiAnalysis (if accessible), Samsung/SK Hynix 8-K filings, METI press, EU Chip Act texts. |
| cron-C | 14:00 | EN-DRAFT §1–§4 (the analytic sections) |
| cron-D | 17:00 | EN-DRAFT §5–§7 (instrument graph + GWW3 + Day-22 bridge) + cross-check θ_econ_weight pre-registrations against pulled evidence |
| cron-E | 21:00 | EN-LOCK + Inanna ZH async dispatch + Moltbook teaser enqueue |

### §7.2 — Inanna involvement

- **Pre-EN-LOCK (cron-D):** sync source-validation check on Samsung / SK Hynix supply-chain claims (3-minute dispatch via trinity-bus, sync mode, --timeout 180; small-bore confirmation only)
- **Post-EN-LOCK (cron-E):** async ZH parallel rendition (1800s timeout)

### §7.3 — Nisaba involvement

- **Pre-EN-LOCK (cron-D):** sync numerical-audit of θ_econ_weight CI estimates + ChipExposure calculations + HBM market-share figures (300s timeout, blocking pipeline per Day-4 lesson). This is the **first publication of the Nexus-binding series with substantive numerical claims** — the Nisaba audit is non-optional.

---

## §8 — Methodology notes for Day-21

### §8.1 — Pre-registration discipline carried forward

This bridge document is itself a partial pre-registration. The θ_econ_weight estimates (§4.2) and the H21.1 hypothesis (§3.2) are filed as BLIND predictions before Day-21 research-fire reads any new evidence. The commit hash of this document will be cited in Day-21 EN-LOCK as the pre-registration anchor, mirroring Day-19's P28 pre-registration discipline (commit 2b6b81f → audit in Day-20 cron-B §1).

### §8.2 — Source-discipline for Day-21

Day-21 must include at minimum:
- 1 EN source on US side (USTR / CHIPS Act / SemiAnalysis)
- 1 ZH source on PRC side (CASS / Caixin / MIIT — q6 firecrawl accessibility status to be re-tested at cron-B)
- 1 KO source on ROK side (Samsung 8-K KO filing, SK Hynix KO disclosure, or MOTIE press)
- 1 JA source on JPN side (METI press, Nikkei semis coverage)

Multi-language quota for a Nexus-binding publication is **higher** than baseline substrate-extension publications because the financial-market evidence base is global and any single-language framing risks missing material signal.

### §8.3 — What can be deferred to Day-22+ India

- India substrate's own θ_econ_weight estimate (defer to Day-22 substrate-extension publication's pre-registration)
- India's testing of P28 boundary condition (no bilateral PRC-IND communiqué Taiwan clause) — Day-22 anchor
- Comparison of India's chip-supply-exposure (post-2022 PLI scheme) against ROK anchor — Day-23 if Day-22 single-deep

---

## §9 — Open questions for Ingo (non-blocking; default-if-no-answer noted)

### q-day21-1: Nexus-binding publication cadence

> Day-21 is the first of an envisioned ROK → Nexus #1 → India three-publication arc. Should subsequent Nexus-binding publications (Nexus #2 onwards) be interleaved 1-per-3-substrates (every 3 substrate publications get a Nexus binding write-up) or backloaded (substrate publications run to completion across all major actors first, then a concentrated Nexus-binding mini-series)?

**Default if no answer:** Interleave 1-per-3 (Nexus #2 after India + 1 more substrate = ~Day-25; Nexus #3 after two more = ~Day-29). Rationale: matches the pattern q-day19-india-sequencing approved (substrate-extension monotony broken by Nexus middle break).

### q-day21-2: Hassaleh-Nexus graph as silicon-strait artifact or hassaleh-nexus repo artifact

> The instrument-graph specification (§5) and the GSL predicates P29/P30 (§6.1) are load-bearing for Hassaleh-Nexus. Should the graph topology + predicate file live (a) in `silicon-strait/research/nexus_implications/` as analytical artifacts citing Hassaleh, (b) in `IngoGiebel/hassaleh-nexus/` as engineering artifacts citing silicon-strait analysis, or (c) symlinked / cross-referenced between both?

**Default if no answer:** (a) for the Day-21 publication (analytical artifact lives in silicon-strait); separate hassaleh-nexus engineering ticket filed for Nisaba to implement the topology in the graph database (Sprint-15 candidate work).

### q-day21-3: Pottinger-style A2 critique extension to ROK

> Day-3 framing 2 applied Pottinger's 2022 critique of A2 (rational-actor assumption) to the PRC player only. Day-21 §4 pre-registers θ_econ_weight as per-substrate. Implicit in this is the possibility that ROK's θ_econ_weight = 0.75 may be over-confident — the coupling-property finding (Day-19 §5.4) suggests ROK has reserved political capacity to override the economic-rationality default, which would push θ_econ_weight lower. Should Day-21 pre-register a wider CI (0.50–0.85) to absorb this risk, or hold the narrower (0.65–0.85) and let the empirical evidence drive any revision?

**Default if no answer:** Hold narrower (0.65–0.85). The coupling-property finding *describes* drift through informal channels but does not yet *predict* override capacity under acute stress; widening CI ex-ante without evidence-base would be unprincipled. Day-21 cron-D Nisaba audit (Pre-EN-LOCK) is the right place to test the CI width against the pulled empirical evidence.

---

## §10 — Hand-off

- Commit this document at the start of Day-20 cron-C (this fire) so Day-21 has a stable anchor.
- Update `state.publications_in_draft[Day-21]` skeleton entry at end of Day-20 cron-E (after Day-20 EN-LOCK) — this bridge feeds the Day-21 skeleton.
- Day-20 cron-D EN-DRAFT will reference this bridge in §5 (Hassaleh-Nexus implications) of the Day-20 publication; Day-20 cron-E EN-LOCK will cite this commit hash.
- Inanna pre-EN-LOCK (Day-21 cron-D) and Nisaba pre-EN-LOCK (Day-21 cron-D) dispatches use this bridge as their context-package anchor.

---

## Sources (bridge document only; Day-21 publication will carry full bibliography)

[B1] Dione (this document), 2026-05-29 14:00 cron-C. Day-21 KORUS / Semiconductor-Supply-Chain Nexus Bridge. silicon-strait/research/nexus_implications/korus-day-21-bridge-2026-05-29.md.

[B2] Dione, 2026-05-01. *Silicon Strait — Day 3: Chip supply chain — the Silicon Shield, its three assumptions, and what the GWW3 model has to either ratify or refute*. silicon-strait commit `651cb5c` (audit revision `42fd75c`). Foundational chip-supply-chain framing.

[B3] Dione, 2026-05-07 / 2026-05-11. *Silicon Strait — Day 7: US Strategic Options*. silicon-strait commit `9d76e1b`. Economic-statecraft layer (S5).

[B4] Dione, 2026-05-28. *Silicon Strait — Day 19: ROK substrate-extension (λ-class A.2 + coupling-property)*. silicon-strait commit `82836dc`. Coupling-property novel finding (§5.4).

[B5] Dione, 2026-05-28. ROK substrate — MOFA-ROK + KORUS treaty corpus. silicon-strait/research/kr_state_extension/dione-mofa-rok-korus-corpus-2026-05-28.md, commit `4c14307`. KORUS path-dependence analysis (§2).

[B6] Inanna, 2026-05-28. ROK National Assembly Taiwan-Related Catalogue (2017–2026). silicon-strait/research/kr_state_extension/inanna-rok-na-catalogue-2017-2026.md, commit `e7fda4d`. 20 instruments, Tier-1/Low-Tier-2 classification.

[B7] Dione, 2026-05-29 11:00 cron-B. Day-20 cron-B Research Note: ROK Advancement-Ceiling + κ Assessment + Pre-Registration Audit. silicon-strait/research/kr_state_extension/dione-day20-cronB-ceiling-kappa-assessment-2026-05-29.md, commit `396174f`. Refined Nexus-binding model (§3); coupling-property quantitative operationalisation (§2).
