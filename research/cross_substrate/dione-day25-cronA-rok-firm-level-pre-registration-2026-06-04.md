# Day-25 cron-A Pre-Registration — 005930.KS × TSM ROK Firm-Level Disambiguation Test

**Filing fire:** Day-25 cron-A (2026-06-04 06:00 CEST)
**Resolves:** q-day24-4 default path (yes — file as Day-25 cron-A first analytic claim)
**Pre-registration commit:** (this file's commit on `silicon-strait/trunk`)
**Execution fire (pre-committed):** Day-25 cron-C (2026-06-04 14:00 CEST)
**Lead:** Dione 🌙
**Trinity dispatches at execution time:** Nisaba 🌾 numerical audit (sync, pre-commit) after cron-C compute lands; Inanna ⭐ source-validation pass deferred to Day-26 (firm-level test reuses Day-24's already-validated v1.2 vocabulary, no new vocabulary commitment).

---

## §1 Why this test exists

Day-24's H24.1 4-substrate textual-axis sweep returned INCONCLUSIVE with the substantive finding that **ROK / EWY × TSM δ sign-flipped** from the pre-registered interval `[+0.05, +0.10]` (predicted by `coupling_textual = DIRECT` under v1.2) to the observed value `δ = −0.0077`. The sign-flip is the most severe single-substrate prediction failure in the corpus and admits two non-exclusive interpretations:

- **(a) Schema-update path** — `coupling_textual = DIRECT` under inter-Korean security pressure translates to **partial substitution**, not co-movement. When PRC fab capacity is squeezed, Samsung Foundry's order book firms up *independently* of (or even inversely to) TSM. v1.2 would need a schema revision distinguishing co-movement-DIRECT from substitution-DIRECT for ROK.
- **(b) Measurement-quality path** — EWY (the broad iShares MSCI South Korea ETF) is too dilute. The ~89 constituents include sectors uncoupled from semiconductor supply-chain dynamics (banking, autos, consumer goods) that wash out the firm-level coupling signal that would surface if we tested Samsung Foundry directly. v1.2 schema is correct; the textual-axis measurement at the ETF level is too noisy for ROK.

The two paths point to **opposite** remediation: (a) edits the schema, (b) edits the measurement. They cannot both be acted on. The disambiguation test below produces a falsifiable verdict between them.

## §2 Hypothesis statement

**H25.1:** Under the same three pre-committed stress windows used at Day-24 cron-C (DUV 2023, LAI 2024, PRC 2025), the firm-level pair **005930.KS × TSM** returns Pearson-correlation δ (rolling-60 on log-returns, ±20 trading-day stress vs. baseline) in the interval `[−0.05, +0.10]`.

The wider-than-EWY interval (5pt wider on the lower side: −0.05 instead of −0.05; identical upper bound +0.10) allows for either interpretation to land in-interval; the **sign and magnitude** of the observed δ resolve the disambiguation, not in-interval / out-of-interval status alone.

## §3 Pre-committed falsification + interpretation rule

| Observed δ on 005930.KS × TSM | Interpretation | Action at Day-26+ |
|---|---|---|
| **δ < −0.001 (sign-flip)** | Path (a) — schema-update — corroborated. ROK exhibits inter-Korean-pressure-driven substitution dynamics at the firm level, consistent with the textual axis at the ETF level. | File v1.2.1 schema revision proposing `coupling_textual_dynamics ∈ {COMOVEMENT, SUBSTITUTION}` as a sub-state of DIRECT; ROK = DIRECT/SUBSTITUTION; JPN/EU/US likely DIRECT/COMOVEMENT pending re-test. |
| **−0.001 ≤ δ ≤ +0.05** | INCONCLUSIVE — both paths remain alive. Sign matches EWY direction but magnitude is below the schema-predicted floor. | Day-26+ stochastic-runtime modeling of ROK substrate under both readings; do not edit schema or remeasurement protocol until additional evidence. |
| **δ > +0.05 (positive, schema-consistent)** | Path (b) — measurement-quality — corroborated. EWY is too dilute for textual-axis testing on ROK; the firm-level signal exists and is in the predicted direction. | File a measurement-protocol amendment: ROK textual-axis = 005930.KS × TSM (firm-level), not EWY × TSM (ETF-level). v1.2 schema unchanged. |

The three intervals are **pre-committed**. No post-hoc re-interpretation.

## §4 Method (pre-committed)

### §4.1 Data window
- Full window: 2022-10-04 through 2026-05-29 (identical to Day-24 cron-B; ends before today to avoid forward-look bias).
- Stress windows (identical to Day-24 cron-C, three windows):
  - DUV 2023: 2023-01-27 ±20 trading days (40 trading days total)
  - LAI 2024: 2024-01-13 ±20 trading days (40 trading days total)
  - PRC 2025: 2025-10-10 ±20 trading days (40 trading days total)
- Baseline window: all trading days in the full window outside the union of the three stress windows.

### §4.2 Tickers
- `005930.KS` — Samsung Electronics, Korea Exchange (KRX). Yahoo Finance ticker.
- `TSM` — Taiwan Semiconductor Manufacturing Company ADR, NYSE. Anchor for cross-substrate textual-axis comparability with Day-24.

### §4.3 Correlation method
- Daily adjusted close from yfinance.
- Log-returns: `r_t = ln(p_t / p_{t-1})`.
- Rolling-60 window Pearson correlation between `r_{005930.KS}` and `r_{TSM}`.
- Stress δ = (mean of rolling-60 ρ over stress-window trading days) − (mean of rolling-60 ρ over baseline-window trading days).
- δ reported as a single number across the three stress windows pooled, matching Day-24 cron-C's pooling convention.

### §4.4 Compute artifact
- Compute script: `research/cross_substrate/dione-day25-cronC-h25_1-rok-firm-correlation.py` (to be written at Day-25 cron-B 11:00 CEST data pull + harness pre-stage; mirrors `dione-day24-cronC-h24_1-correlation.py` structure with single-pair instead of four-pair logic).
- Output: `research/cross_substrate/dione-day25-cronC-h25_1-output.json` with fields `{ticker_pair, n_stress_td, n_baseline_td, stress_window_dates, baseline_window_dates, rolling_60_pearson_stress_mean, rolling_60_pearson_baseline_mean, delta, verdict_path}` where `verdict_path ∈ {a_schema_update, b_measurement_quality, inconclusive}`.
- Reproducibility: pre-stage at Day-25 cron-B; execute at Day-25 cron-C with the data pull and harness frozen.

### §4.5 Data quality gates (pre-committed)
- KRX trading calendar differs from NYSE; merge-on-date inner join is required (drops weekends and asymmetric holidays). Day-24 cron-C convention: align on TSM ADR (NYSE) calendar, forward-fill 005930.KS by ≤ 1 trading day at the asymmetric edges. **Pre-committed gate:** if forward-fill count ≥ 5% of the joined window, log a measurement-quality flag and present δ as `provisional`.
- Daily volume floor: 005930.KS median daily volume in the full window must be ≥ 1M shares (it is; precedent confirmed in Day-21 §4.2 use). If the median drops below 1M in the stress windows, log a liquidity-anomaly flag.
- NaN cells after join: must be 0 in the full window. If > 0, halt and re-pull.

## §5 What this test does NOT test

- **Not a re-test of Day-24's H24.1 ETF-level claim.** EWY × TSM δ = −0.0077 stands at the ETF level; this test is firm-level and produces an independent number.
- **Not a re-test of Day-21 §4.2's 005930.KS × TSM event-window median correlation.** Day-21 used event-window medians, not stress-vs-baseline δ. This test uses Day-24/25's pooled-stress-window δ method.
- **Not a test of inter-Korean security dynamics directly.** The disambiguation is between *measurement dilution at the ETF level* (path b) and *schema-level substitution dynamics under inter-Korean pressure* (path a). The inter-Korean security claim itself is not on the test bench; only its *coupling implication for the textual axis* is.
- **Not a test of the EU/EZU surprise** (`δ = +0.0796`, q-day24-3). EU surprise is disambiguated by Day-25 cron-B EU member-state decomposition (q-day24-5), separate fire and separate pre-registration.

## §6 What this test enables for Day-26+

| Outcome | Day-26+ work | Day-27+ work |
|---|---|---|
| **(a) Schema-update** | v1.2.1 schema revision draft (`coupling_textual_dynamics` sub-state); re-classify ROK = DIRECT/SUBSTITUTION; re-derive H25.1-like hypotheses for JPN, EU, US under DIRECT/COMOVEMENT default. | Re-run Day-24 H24.1 sweep with schema-aware predicted directions per substrate; expected to move H24.1 from INCONCLUSIVE to PASS or FAIL. |
| **(b) Measurement-quality** | Measurement-protocol amendment: ROK textual-axis = 005930.KS × TSM; document ETF-vs-firm-level decision rule for future substrate-extensions. | Apply firm-level fallback to JPN (8035.T × TSM as textual-axis, not just operational-axis), EU (mixed firm-level basket), US (NVDA × TSM textual replicate). |
| **INCONCLUSIVE** | Day-26+ stochastic-runtime modeling of ROK substrate under both readings; no schema or protocol edit. | Day-27+ collect additional ROK-firm-level data (000660.KS SK Hynix × TSM as second-firm test) for power increase. |

## §7 Trinity coordination at execution

- **Day-25 cron-B (11:00 CEST):** Dione data pull (yfinance for 005930.KS over the full window, joined to existing TSM series from Day-24 cron-B), harness pre-stage (`dione-day25-cronC-h25_1-rok-firm-correlation.py`). Commit + push.
- **Day-25 cron-C (14:00 CEST):** Dione executes the harness; output JSON lands; verdict_path is assigned per §3; pre-registered intervals are checked.
- **Day-25 cron-C sync dispatch to Nisaba:** numerical audit of the verdict_path assignment (cell-by-cell δ arithmetic), sync timeout 600s, grace 60s, expected ~3–8 min. **Blocks publication.**
- **Day-25 cron-D (17:00 CEST):** Dione writes Day-25 publication EN-DRAFT incorporating H25.1 verdict + downstream consequences per §6.
- **Day-25 cron-E (21:00 CEST):** EN-LOCK; async ZH dispatch to Inanna (timeout 1800s); Moltbook teaser enqueue; Telegram sprint-boundary alert if H25.1 lands as sign-flip (sprint-significant) or in-interval-positive (sprint-significant).

## §8 Audit trail

| Step | Artifact | Commit | Status |
|---|---|---|---|
| q-day24-4 filing | state.open_questions_for_ingo[q-day24-4] | (Day-24 cron-D 17:00 CEST) | open → resolved by default at this fire |
| Pre-registration (this file) | `research/cross_substrate/dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md` | (this commit) | filed |
| Data pull + harness pre-stage | `research/cross_substrate/dione-day25-cronB-data/` + `dione-day25-cronC-h25_1-rok-firm-correlation.py` | (Day-25 cron-B) | pending |
| Compute output | `research/cross_substrate/dione-day25-cronC-h25_1-output.json` | (Day-25 cron-C) | pending |
| Nisaba numerical audit | `research/audit/nisaba-day25-cronC-day25-numerical-audit.md` | (Day-25 cron-C sync) | pending |
| EN-DRAFT publication | `publications/2026-06-04-en.md` | (Day-25 cron-D) | pending |
| EN-LOCK publication | `publications/2026-06-04-en.md` | (Day-25 cron-E) | pending |
| ZH parallel rendition | `publications/2026-06-04-zh.md` | (Day-25 cron-E async, reconcile at Day-26 cron-A Step 0.5) | pending |

---

**Filed by:** Dione 🌙 at Day-25 cron-A 2026-06-04 06:00 CEST
**Resolves:** q-day24-4 (open since Day-24 cron-D 17:00 CEST 2026-06-03)
**Pre-registration discipline:** intervals, falsification rule, and method are pre-committed and may not be revised after the data pull at cron-B without a separate revision-pre-registration artifact filed before that pull lands.
