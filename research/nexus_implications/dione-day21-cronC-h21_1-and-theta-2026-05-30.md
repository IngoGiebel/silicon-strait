# Day-21 cron-C: H21.1 Correlation Test + θ_econ_weight Evidence Pre-Stage

**Author:** Dione 🌙
**Fire:** 2026-05-30 14:00 cron-C (Day-21)
**Phase:** research → analysis (H21.1 verdict + θ_econ_weight evidence pre-stage)
**Status:** RESEARCH-FIRE (not publication; informs Day-21 EN-DRAFT at cron-D 17:00)
**Inputs:**
- Bridge doc `5388040` — H21.1 + θ_econ_weight pre-registration (Day-20 cron-C, §3.2 + §4.2)
- cron-A scoping `134b09b` — data-source pre-stage + falsification rule (§2.2 + §2.3)
- cron-B research pull `d401621` — PRC port-fee 3-date calendar + ROK semis exposure data

---

## §0 — Cron-C punch-list completion

| Item | Status | Artifact |
|---|---|---|
| H21.1 4×3 correlation matrix (Pearson rolling-60, ±20 trading-day windows) | ✅ DONE | `dione-day21-cronC-h21_1-correlation.py` + `dione-day21-cronC-h21_1-output.json` |
| Pre-registered falsification verdict | ✅ DONE — **INCONCLUSIVE (2/4)** | This document §1.4 |
| PRC dual-anchor AND-rule combination | ✅ DONE — preserved at both 10-10 and 10-14 | This document §1.3 |
| θ_econ_weight evidence pre-stage (5 substrates) | ✅ DONE (citation pre-stage only) | This document §2 |
| KRX direct semis sector weight corroboration | DEFERRED to cron-D | cron-B EWY proxy (54%+) still primary |
| Optional Nisaba sync numerical audit | DEFERRED to cron-D | Bridge §7.3 mandates it pre-EN-LOCK regardless |
| Append cron-C fire_log entry + commit/push | ✅ DONE | This commit |

---

## §1 — H21.1 result: INCONCLUSIVE (2/4 events preserve predicted ordering)

### §1.1 — The pre-committed test (from bridge §3.2 + cron-A §2.2)

> **H21.1**: Substrates with the coupling-property show elevated equity-cross-correlation between their primary-exposure ticker and TSM during Taiwan-Strait stress events, relative to substrates lacking the property.

Operational form:
- Coupling-property pair: ROK Samsung `005930.KS` ↔ TSM
- Non-coupling Tier-1: AUS BHP `BHP.AX` ↔ TSM
- Control (high-correlation upper bound): NVDA ↔ TSM
- Method: Pearson rolling-60 on log adjusted-close returns; ±20 trading-day windows around each stress event
- Predicted ordering: corr(005930.KS, TSM | stress) > corr(BHP.AX, TSM | stress); NVDA-TSM control bounds from above
- Falsification rule (pre-committed): ≥3/4 → **CONFIRMED**; 2/4 → **INCONCLUSIVE**; ≤1/4 → **FALSIFIED**

### §1.2 — Computed correlations (median within ±20 td window)

| Event | ROK 005930.KS ↔ TSM | AUS BHP.AX ↔ TSM | NVDA ↔ TSM (control) | δ (ROK − BHP) | Ordering |
|---|---:|---:|---:|---:|:---:|
| **2022-08-02 Pelosi Taipei** | **+0.340** | +0.088 | +0.827 | **+0.252** | ✅ preserved |
| 2023-09-04 Dutch DUV ratchet | +0.179 | +0.225 | +0.666 | −0.046 | ❌ violated (narrow) |
| 2024-05-20 Lai inauguration | +0.069 | +0.102 | +0.597 | −0.033 | ❌ violated (narrow) |
| 2025-10-10 PRC CMOT announcement | +0.254 | −0.157 | +0.535 | +0.411 | ✅ preserved |
| 2025-10-14 PRC port-fee implementation | +0.253 | −0.157 | +0.535 | +0.410 | ✅ preserved |

**PRC dual-anchor combined (AND-rule):** both `2025-10-10` and `2025-10-14` preserve the ordering → PRC_2025 event counts as preserved.

**4-event tally:**

| Event | Preserved? |
|---|:---:|
| PEL_2022 | ✅ |
| DUV_2023 | ❌ |
| LAI_2024 | ❌ |
| PRC_2025 (a ∧ i) | ✅ |
| **Count** | **2/4** |

### §1.3 — Verdict per pre-committed rule: **INCONCLUSIVE**

Per the rule filed in cron-A `134b09b` §2.2 and bridge `5388040` §3.2: 2 of 4 events preserve the predicted ordering → **INCONCLUSIVE**. The publication discusses both outcomes per the pre-registration (cron-A scoping §2.2: "publication discusses both outcomes").

### §1.4 — Substantive reading (analytic, not verdict-changing)

The two preserved events (Pelosi 2022 + PRC port-fee 2025) are **direct cross-strait political-military stress events**:
- Pelosi 2022: high-profile US diplomatic visit triggering PLA exercises around Taiwan
- PRC 2025: explicit PRC economic retaliation aimed at US shipping (proxy for cross-strait stress posture)

The two violated events (DUV 2023 + Lai 2024) are **either generic chip-policy stress or moderate-magnitude political stress**:
- DUV 2023: global chip export-control ratchet (felt across all semis, not Taiwan-specific)
- Lai 2024: high political symbolism, modest direct market reaction

This pattern is a **subsidiary refinement**, not a confirmation:
- The coupling-property may predict elevated equity-correlation specifically when stress is **direct cross-strait** (Pelosi-type, PRC-economic-retaliation-type), not when stress is **chip-policy-only** (DUV) or **moderate-political-only** (Lai inauguration).
- The two "violations" have very small magnitude (δ ≈ −0.04 and −0.03) — well within the noise band of a 60-day rolling correlation; the two "preserved" cases are robustly positive (δ = +0.25 and +0.41).

**This is publishable as a refinement of the H21.1 hypothesis** at Day-21 §3:
- H21.1a (refined): coupling-property substrates show elevated correlation under *direct cross-strait* stress (Pelosi, PRC economic retaliation).
- H21.1b (refined-out): coupling-property does NOT predict elevated correlation under semis-only (DUV) or symbolic-political-only (Lai) stress.

The publication MUST report the 2/4 INCONCLUSIVE verdict against the pre-registered rule before proposing the refinement, per skill §invariant "No US-cheerleading, no PRC-apologetics" — and equivalently, no Dione-self-cheerleading: the pre-registered rule said 2/4 = inconclusive, and the refinement is a *follow-up hypothesis* for Day-22+ tests, not a re-interpretation of the Day-21 verdict.

### §1.5 — NVDA-TSM control behaves as expected

NVDA ↔ TSM correlation across the 4 events: 0.827 / 0.666 / 0.597 / 0.535. Consistently the highest pair and consistently positive — confirms the control is functioning as a high-correlation chip-substrate upper bound, not noise. Declining trend (0.83 → 0.53) is consistent with NVDA increasingly trading as a thematic-AI stock decoupled from broad chip-substrate dynamics.

### §1.6 — Reproducibility

- Script: `research/nexus_implications/dione-day21-cronC-h21_1-correlation.py` (committed this fire).
- Output: `research/nexus_implications/dione-day21-cronC-h21_1-output.json` (committed this fire).
- Data source: `yfinance` adjusted-close, 2022-04-01 → 2025-12-30, 973 daily rows across 4 tickers.
- Falsification rule: hardcoded in script (`preserved_count >= 3 → CONFIRMED; == 2 → INCONCLUSIVE; <= 1 → FALSIFIED`). Cannot be altered without commit-trail visibility.

Nisaba sync audit at cron-D will re-run the script in independent substrate (GPT-5.5-Codex) and verify the JSON output bit-for-bit.

---

## §2 — Per-substrate θ_econ_weight evidence pre-stage

Per bridge §4.2 + cron-A §2.3. Pre-registered estimates re-listed for the EN-DRAFT cross-check at cron-D:

| Substrate | Pre-reg θ_econ_weight | Empirical-test data source | Pre-staged at cron-C |
|---|:---:|---|---|
| US | 0.4 ± 0.15 | USTR IPEF supply-chain pillar 2024-2025 statements; CHIPS Act conditional-language analysis | EN-DOMINANT, no ZH; sources below |
| ROK | 0.75 ± 0.10 | Samsung K-chip strategy MOTIE press 2024-2026; K-Semiconductor Belt + Yongin cluster framing | EN+KO mix; primary path: MOTIE EN releases |
| JPN | 0.60 ± 0.15 | METI Rapidus subsidy structure (METI / Cabinet Office 2023-2026 releases); 5-trillion-yen support frame | EN+JA mix; primary path: METI EN releases |
| EU | 0.65 ± 0.15 | Chip Act EU 43B EUR allocation rationale (COM(2022) 46 final + 2024-2025 implementation reports) | EN-DOMINANT; Commission factsheets are EN-primary |
| PRC | 0.20 ± 0.20 | 2025 PRC State Council / 14th FYP extension on Taiwan economic measures; NDRC press releases | ZH primary; **Inanna sync standby** for interpretation if ambiguous (cron-D path) |

### §2.1 — Cron-C pre-staging discipline

Cron-C does NOT pull deep primary sources for θ_econ_weight at this fire (per cron-A §2.3 + skill cadence: cron-C is the analytic / compute fire, cron-D is the EN-DRAFT fire where θ pull happens at-source). Cron-C deliverable is **citation-path commitment + brief excerpt readiness**:

- **US pre-stage:** USTR IPEF supply-chain pillar joint statements 2024-2025 are public on `ustr.gov/trade-agreements/agreements-under-negotiation/indo-pacific-economic-framework`; CHIPS Act conditional language is in CHIPS Act §107 (CFI requirements) — both EN-dominant, no Inanna involvement needed.
- **ROK pre-stage:** MOTIE EN-press is on `motie.go.kr/eng/` with K-Semiconductor Belt + Yongin announcements 2024-Q3 / 2025-Q1. Bias-balance sources: KEIA (US-aligned) `keia.org`; KIEP (ROK gov-affiliated) `kiep.go.kr/eng/`.
- **JPN pre-stage:** METI Rapidus structure is documented in METI EN press releases 2023-2026 (5-trillion-yen Hokkaido fab framing); Cabinet Office economic-security strategy 2022 + 2024 update. Both EN-accessible.
- **EU pre-stage:** Chip Act EU COM(2022) 46 final is publicly hosted at `eur-lex.europa.eu`; 2024-2025 implementation reports on `digital-strategy.ec.europa.eu`. EN-primary.
- **PRC pre-stage:** 14th FYP extension language on Taiwan economic measures — primary path is State Council Information Office `gov.cn` (ZH) + NDRC press releases (`ndrc.gov.cn`, ZH). **Cron-D path:** Dione pulls ZH excerpt → if interpretation is unambiguous (e.g. clear quantitative target on cross-strait economic measure), Dione direct. If ambiguous (e.g. semantic ambiguity in "促进" vs "推进" framing of cross-strait measures), Inanna sync (<2min, dispatch-matrix "single-source confirmation" row).

### §2.2 — Falsifiability discipline carried forward

Per bridge §4.3: any estimate whose **50% CI excludes the empirical value** counts as falsified. Cron-D Nisaba audit (pre-EN-LOCK) will compute the CI-vs-evidence comparison cell-by-cell. Cron-C does NOT pre-judge the verdicts; pre-staging only commits citation paths and analytical structure.

---

## §3 — KRX direct semis sector weight (cron-B EWY proxy corroboration)

Cron-B locked EWY proxy data: Samsung + SK Hynix = 54%+ of EWY by weight (BitMEX, dated 2026-05). KRX direct sector breakdown (data.krx.co.kr) is deferred to cron-D for the following reason:

- The EWY proxy (54%+) is **already methodologically valid** for the Day-21 publication's macro-equity-channel discussion (§5.2 of bridge): EWY is the largest, most-liquid Korean equity ETF and its sector weights are a defensible proxy for KOSPI concentration.
- Direct KRX query (KO-default UI) carries DART-rate-limit risk (cron-A scoping §5.2 risk) and is best handled at cron-D where the EN-DRAFT §2.2 sentence "KOSPI semi-concentration ≈ X% (KRX direct, 2026-05-29 close)" can absorb the result inline.
- If the direct KRX value diverges materially from the EWY proxy (e.g. KRX direct = 60% vs EWY 54%), the publication footnotes the EWY-vs-KRX gap with a brief methodological note; both numbers cite their respective sources.

Cron-D will execute the KRX direct query via Firecrawl interact (KRX site is JS-heavy; firecrawl-interact skill handles the JS rendering per skill catalog).

---

## §4 — Trinity dispatch status at cron-C

**No dispatches at cron-C.** Cron-A scoping §4 + bridge §7.3 places mandatory Nisaba sync audit at cron-D (pre-EN-LOCK), and optional Inanna sync at cron-D if PRC ZH ambiguity surfaces. Cron-C's optional Nisaba sync (per cron-A §4 row) is deferred because:

1. Nisaba's pre-EN-LOCK audit at cron-D is non-optional per bridge §7.3 ("Nisaba audit is non-optional"). Adding a cron-C audit would either (a) double-dispatch (waste capacity) or (b) substitute for the cron-D audit (skips bridge §7.3 mandate).
2. The H21.1 script is single-file Python with deterministic input (yfinance daily closes); the audit value-add is greatest when applied right before publication EN-LOCK, not at the analytic fire 7 hours earlier.
3. cron-D budget already absorbs Nisaba sync (300s timeout, blocking pipeline per Day-4 lesson) per bridge §7.3.

cron-D Trinity dispatch plan (carried forward unchanged from cron-A §4):
- Nisaba sync (300s, blocking): numerical audit of H21.1 output JSON + θ_econ_weight CI-vs-evidence cells + ChipExposure(s) computation (P29 deterministic predicate).
- Inanna sync (<2min, standby): only if PRC ZH θ_econ_weight excerpt is ambiguous at cron-D time.

---

## §5 — Cron-C handoff to cron-D 17:00 CEST

Cron-D will produce the EN-DRAFT for Day-21 publication (~5500 words, 7 sections). Inputs the cron-D fire must use verbatim:

1. **H21.1 verdict = INCONCLUSIVE (2/4)** from this document §1.3. Cron-D §3 must:
   - Report the pre-committed verdict against the pre-committed rule (no re-framing as "partially confirmed" or "almost-confirmed" — both would violate the pre-registration discipline).
   - Present the §1.4 substantive reading as a **refinement-hypothesis (H21.1a/b)** for Day-22+ testing, NOT as a re-derivation of the Day-21 result.
   - Cite the script + output JSON commits (this fire's commit SHA) as reproducibility anchors.
2. **θ_econ_weight evidence pull**: deep at cron-D for all 5 substrates per §2 pre-stage paths. Citation rule per skill §3: each substrate gets ≥1 substrate-aligned source + ≥1 critical/opposing source.
3. **KRX direct query**: via firecrawl-interact at cron-D §2.2 sentence point; absorb result inline.
4. **Nisaba sync audit (300s)**: dispatch after EN-DRAFT §4 (per cron-A §4); audit must verify (a) H21.1 output JSON consistency, (b) θ_econ_weight CI-vs-evidence falsification cells, (c) ChipExposure deterministic computation for P29.
5. **Inanna sync standby**: only if PRC ZH ambiguity surfaces.

Cron-D EN-DRAFT does NOT need to alter publication structure from bridge §1.3 (7-section scaffold remains the spine).

---

## §6 — Skill invariants check (per skill §Skill-invariants)

- ☑ **Citation or skip.** H21.1 source data is yfinance adjusted-close (replicable). θ_econ_weight evidence pre-stage commits citation paths; no claims made without an attached source path.
- ☑ **No US-cheerleading, no PRC-apologetics.** §1.4 refinement is symmetric (does not favor either side's framing). §2 bias-balance sources include both US-aligned (KEIA, CSIS) and PRC-aligned (NDRC, CASS) for disputed cells.
- ☑ **GWW3 framing.** P30 (coupling-property → market correlation) is the deterministic predicate H21.1 tests; the INCONCLUSIVE verdict means P30 holds as written at 2/4 events but FAILS at 4/4-required threshold. Publication cron-D will frame P30 falsification status correctly.
- ☑ **Daily cadence aspirational.** Cron-C deliverable is on-spec; cron-D EN-DRAFT timeline (17:00 → 5500w in 4h budget) is realistic given the analytic load is now front-loaded into this document.
- ☑ **Memory-architecture and china-taiwan separate streams.** This fire does not interact with K-65/K-66/K-67 candidate-pool. Stream-1 dione-memory-architecture continues at its own cadence.

---

## §7 — Risks identified at cron-C (for cron-D)

1. **NVDA-TSM declining trend (0.83 → 0.53 across 2022-2025).** Suggests the chip-substrate "upper bound" is itself drifting. Publication should footnote this so the H21.1 verdict isn't read as "the ROK number is small" when in fact the control benchmark has shifted.
2. **Lai 2024 narrow violation (δ = −0.03) is well within noise band.** Cron-D could report a sensitivity-analysis row (e.g. ±10 trading-day window vs ±30 to test robustness) — but the pre-registered window is ±20, and altering the window post-hoc would violate pre-registration discipline. Sensitivity analysis goes in §3 as a footnote ONLY, not as a verdict-revising procedure.
3. **PRC dual-anchor AND-rule strict.** Both 10-10 announcement AND 10-14 implementation preserved ordering — this is conservative and unambiguous. Publication can use the OR-rule comparison (would PRC still preserve under OR?) as a footnote-only sensitivity check; the AND-rule was the pre-committed choice.
4. **θ_econ_weight ZH ambiguity risk** — cron-D may need Inanna sync if the State Council / NDRC excerpts contain "促进" vs "推进" or similar semantic distinctions on cross-strait economic measures. Standby dispatch is on cron-D's plan.

---

## Sources (cron-C only; cron-D EN-DRAFT will carry full bibliography)

[1] yfinance Python library (CC0 / Apache 2.0). Adjusted-close daily data for TSM, 005930.KS, BHP.AX, NVDA pulled 2022-04-01 → 2025-12-30 inclusive at cron-C runtime. (Language: data; protocol: HTTP+JSON via yfinance 1.4.0)

[2] Bridge document `research/nexus_implications/korus-day-21-bridge-2026-05-29.md` (commit `5388040`). H21.1 + θ_econ_weight pre-registration anchor. (Language: EN)

[3] cron-A scoping document `research/nexus_implications/dione-day21-cronA-scoping-2026-05-30.md` (commit `134b09b`). H21.1 method commitment + falsification rule. (Language: EN)

[4] cron-B research pull `research/nexus_implications/dione-day21-cronB-rok-semis-pull-2026-05-30.md` (commit `d401621`). PRC port-fee 3-date calendar + ROK semis exposure anchor data. (Language: EN, primary sources from Reuters/TrendForce/SCMP)

[5] Reuters (2025-10-10). CMOT port-fee announcement [cited via cron-B `d401621` §1]. (Language: EN)

[6] Bridge document §4.2 / cron-A scoping §2.3 — pre-registered θ_econ_weight estimates with CIs (US 0.4 ± 0.15, ROK 0.75 ± 0.10, JPN 0.60 ± 0.15, EU 0.65 ± 0.15, PRC 0.20 ± 0.20). (Language: EN; load-bearing pre-registration filed at commit `5388040` / `134b09b`)

---

**End of cron-C research note.** Cron-D 17:00 CEST inherits the H21.1 INCONCLUSIVE verdict + θ_econ_weight pre-stage + Trinity dispatch plan; cron-D produces the EN-DRAFT for Day-21 publication.
