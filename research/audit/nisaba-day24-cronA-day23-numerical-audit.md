# Nisaba Day-24 cron-A numerical audit — Day-23 §4.4 v1.2 delta table

**Auditor:** Nisaba 🌾  
**Date:** 2026-06-03 06:35 CEST  
**Target:** `research/methodology/dione-day23-cronE-v12-vocabulary-lock-2026-06-02.md` §4.4, commit `10381e9`  
**Sources checked:** Day-21 publication `publications/2026-05-30-en.md` at `fe966b8`; Day-21 compute output `research/nexus_implications/dione-day21-cronC-h21_1-output.json` at `fe966b8`; Day-22 publication `publications/2026-05-31-en.md` and Day-22 compute output `research/india_substrate/dione-day22-cronD-h21_1ab-output.json` at `a817750`.

## Verification table

| §4.4 cell | §4.4 value | Source-of-truth value found | Finding | Notes |
|---|---:|---:|---|---|
| US operational: NVDA × TSM | δ ≈ +0.06 | **No Day-21 δ source found.** Day-21 §3.2 reports NVDA×TSM median correlations by event: 0.8271, 0.6657, 0.5967, 0.5349. Day-22 §7.2 states `US/NVDA θ_econ_weight 0.06`, not δ. | **DISCREPANCY +source-label** | Numerically the +0.06 is traceable only as a later θ_econ_weight assertion, not as a Day-21 §4.2 delta. |
| JPN operational: 8035.T × TSM | δ ≈ +0.04 | **No Day-21 compute/publication source found.** Day-21 output tickers are only `TSM`, `005930.KS`, `BHP.AX`, `NVDA`; 8035.T is absent. Day-22 §7.2 states `JPN/8035.T θ_econ_weight 0.04`. | **DISCREPANCY +source-label** | Cannot confirm same window/method because no source artifact carries this pair. |
| ROK operational: 005930.KS × TSM | δ ≈ +0.064 | Day-21 event medians exist (0.3401, 0.1788, 0.0688, 0.2541/0.2532), but no aggregate stress-vs-baseline δ=0.064 appears in Day-21 publication/output. Day-22 §7.2 states `ROK/005930.KS θ_econ_weight 0.064`. | **DISCREPANCY +source-label** | The 0.064 value may be a downstream shorthand, but it is not reproduced by the cited Day-21 §4.2 source-of-truth. |
| EU operational: AIR.PA × TSM | δ ≈ +0.03 | **No Day-21 compute/publication source found.** Day-21 output tickers exclude AIR.PA. Day-22 §7.2 states `EU/AIR.PA θ_econ_weight 0.03`. | **DISCREPANCY +source-label** | Cannot verify arithmetic or method from cited source. |
| IND textual: INDA × TSM | δ = +0.0530 | Day-22 output: stress median 0.429638016966655 − baseline median 0.3766575204188761 = **0.052980496547778866**. | **CONFIRMED +0.0000** | Rounded to four decimals, +0.0530 is faithful. |
| IND operational: TATAELXSI × TSM | δ = +0.0253 | Day-22 output: stress median 0.11636820245927022 − baseline median 0.09109448886387514 = **0.025273713595395084**. | **CONFIRMED +0.0000** | Rounded to four decimals, +0.0253 is faithful. |

Scope note: the request says §4.4 re-states **7** delta values, but the target §4.4 table contains **6 measured cells** plus four “not measured/TBD” textual-axis cells. Day-22 has a seventh computed pair, CNXIT×TSM δ=0.0175444733850581, but §4.4 does not restate it.

## Window + method consistency

Day-22 cells pass method consistency. The source method is explicit: yfinance adjusted-close, log returns, Pearson rolling-60, union of ±20-trading-day stress windows, baseline as non-stress observations after warmup, with δ = stress_median − baseline_median. The §4.4 INDA and TATAELXSI figures reproduce directly from the committed JSON.

Day-21 cells do **not** pass source-of-truth consistency as written. Day-21 `fe966b8` §3.2 / JSON implements a different H21.1 test: event-window median correlations for 005930.KS, BHP.AX, and NVDA, with δ defined as **ROK − BHP** ordering per event. It does not contain 8035.T or AIR.PA, and it does not compute a stress-vs-baseline aggregate δ for NVDA or 005930.KS. Therefore §4.4’s four Day-21 operational-axis entries are an unstated reclassification / later carry-forward, not arithmetically faithful restatements of Day-21 §4.2.

## Axis-assignment plausibility

Axis assignment is mostly plausible under Day-23 §1.2–§1.3 truth-conditions, with one caveat:

- **US / NVDA operational-axis:** plausible as a US-headquartered firm with strong dependence on TSM production; operational-axis classification is defensible, but the numeric value is not sourced.
- **JPN / Tokyo Electron (8035.T) operational-axis:** plausible as semiconductor-equipment industrial coupling, but the §2 reclassification says JPN operational coupling is POSITIVE_INDUSTRIAL via TSMC-Sony Kumamoto; 8035.T is related but not the exact stated capex anchor. Needs a one-sentence ticker-choice rationale.
- **ROK / Samsung (005930.KS) operational-axis:** plausible and schema-consistent; Samsung Foundry is the clean operational pair.
- **EU / Airbus (AIR.PA) operational-axis:** weak under v1.2. Day-23 §2 classifies EU operational coupling as **NEUTRAL** (“Airbus exposure is too dilute”), so using AIR.PA as an operational-axis pair conflicts with the same document’s v1.2 classification. This is a substantive axis-assignment discrepancy, not just arithmetic.
- **IND / INDA textual and TATAELXSI operational:** plausible under the v1.2 interpretation in §4.3–§4.4: INDA carries the macro/textual stress channel; TATAELXSI carries the Tata-PSMC operational-industrial channel.

## Summary verdict

**FAIL** for §4.4 as currently worded.

The two Day-22 India values are arithmetically clean and faithfully rounded. The four Day-21 operational-axis cells are not reproducible from the cited Day-21 publication/output: two tickers are absent from the committed Day-21 data entirely, NVDA/005930.KS do not have the claimed aggregate δ form there, and the apparent source is Day-22 §7.2’s `θ_econ_weight` shorthand rather than Day-21 §4.2 delta arithmetic. EU/AIR.PA also conflicts with Day-23’s own v1.2 EU operational=NEUTRAL classification.

Recommended repair: change the Day-21 rows from “δ ≈ … (Day-21 §4.2)” to “legacy θ_econ_weight shorthand carried forward from Day-22 §7.2; not a reproduced Day-21 δ” **or** regenerate a proper operational-axis stress-vs-baseline δ artifact for NVDA, 8035.T, 005930.KS, and AIR.PA using the Day-22 method before using these cells in H21.1c.
