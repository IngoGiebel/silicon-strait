# Nisaba Numerical Audit — Day-25 cron-C H25.1 ROK Firm-Level Disambiguation

**Audit fire:** Day-25 cron-C, 2026-06-04 14:xx CEST  
**Auditor:** Nisaba 🌾  
**Target commit:** `340631c0011e9cfe2bc309670f0e7f0c78b41b01`  
**Target output:** `research/cross_substrate/dione-day25-cronC-h25_1-output.json`  
**Verdict:** **PASS-WITH-NOTES**

The published H25.1 output is reproducible cell-for-cell, excluding the intentionally time-varying `computed_at` field. The pre-registered median-based verdict assignment is implemented correctly and lands at `b_measurement_quality`. The only substantive caution is brittleness: the median δ exceeds the `+0.05` threshold by only `+0.0045576`, and a defensible rolling-window sensitivity (`rolling-30`, also `rolling-90`) flips the verdict to `inconclusive`.

## 1. Reproducibility

Fresh detached worktree at `340631c0011e9cfe2bc309670f0e7f0c78b41b01`; command run:

```bash
python3 research/cross_substrate/dione-day25-cronC-h25_1-rok-firm-correlation.py
```

Comparison against committed JSON, excluding only `computed_at`:

| Field | Committed | Recomputed | Status |
|---|---:|---:|---|
| `verdict_path` | `b_measurement_quality` | `b_measurement_quality` | PASS |
| `verdict_consensus` | `agree` | `agree` | PASS |
| `n_pair_obs_after_dropna` | 891 | 891 | PASS |
| `n_dropped_asymmetric_calendar` | 25 | 25 | PASS |
| `full_window_pearson` | 0.1353960545 | 0.1353960545 | PASS |
| `stress_median_rolling_corr` | 0.1858138766 | 0.1858138766 | PASS |
| `baseline_median_rolling_corr` | 0.1312562635 | 0.1312562635 | PASS |
| `delta_median` | 0.0545576132 | 0.0545576132 | PASS |
| `stress_mean_rolling_corr` | 0.1927030241 | 0.1927030241 | PASS |
| `baseline_mean_rolling_corr` | 0.1403736695 | 0.1403736695 | PASS |
| `delta_mean` | 0.0523293546 | 0.0523293546 | PASS |

Result: **0 mismatches** excluding `computed_at`; all numeric cells match well beyond 4 d.p.

## 2. Method-spec adherence

Checked harness: `research/cross_substrate/dione-day25-cronC-h25_1-rok-firm-correlation.py`.

- **Log returns:** PASS. The harness computes `log_ret = np.log(wide / wide.shift(1))`, i.e. `log(P_t / P_{t-1})` on price levels, not on first differences.
- **Joined pair + dropna before rolling Pearson:** PASS. The harness computes `pair = log_ret[[TICKER, ANCHOR]].dropna()` and then `pair[TICKER].rolling(60).corr(pair[ANCHOR]).dropna()`, matching the Day-24 cron-C convention.
- **Stress windows:** PASS with wording note. The code uses `pos - 20` through `pos + 20` inclusive, yielding 41 return observations per anchor before rolling-window truncation. This matches the requested `±20 td` half-width and Day-24 convention, though the cron-A pre-registration prose also says “40 trading days total,” which is arithmetically inconsistent with an inclusive ±20-day window.
- **Delta statistic:** PASS. Primary verdict statistic is `median(rolling_corr | stress) - median(rolling_corr | baseline)`, as clarified by cron-B errata §3.bis; mean is computed and reported as secondary.

Per-anchor rolling-60 stress contribution:

| Anchor | Window | Return td | Rolling td | Median rolling ρ | Mean rolling ρ |
|---|---:|---:|---:|---:|---:|
| DUV_2023 | 2022-12-23..2023-02-27 | 41 | 38 | 0.1945360137 | 0.1903721331 |
| LAI_2024 | 2023-12-14..2024-02-15 | 41 | 41 | 0.1179963295 | 0.1151231560 |
| PRC_2025 | 2025-09-08..2025-11-10 | 41 | 41 | 0.2650054864 | 0.2724432302 |

## 3. Verdict-rule adherence

`assign_verdict()` implements exactly:

- `delta < -0.001` → `a_schema_update`
- `delta > 0.05` → `b_measurement_quality`
- otherwise → `inconclusive`, which includes `-0.001 <= delta <= +0.05`

With `delta_median = 0.0545576132`, verdict assignment is therefore **correct**: `b_measurement_quality`.

Minor code note: `VERDICT_BUCKETS` is defined but unused and represents `inconclusive` as `(-0.001, 0.05)` without explicit inclusivity. This does not affect output because `assign_verdict()` is the actual rule used and is correct.

## 4. Asymmetric-calendar drop count

Raw joined rows: `917`  
Paired returns after log-return shift + `.dropna()`: `891`  
Harness drop formula: `917 - 891 - 1 = 25`

This is internally consistent. The 25 dropped return rows are:

```text
2022-10-04,
2023-01-24, 2023-01-25,
2023-09-29, 2023-10-02, 2023-10-03, 2023-10-04,
2024-02-12, 2024-02-13,
2024-09-17, 2024-09-18, 2024-09-19,
2025-01-28, 2025-01-29, 2025-01-30, 2025-01-31,
2025-05-06, 2025-05-07,
2025-10-06, 2025-10-07, 2025-10-08, 2025-10-09, 2025-10-10,
2026-02-18, 2026-02-19
```

The reconciled pull meta reports 17 structural KRX-side price NaNs and zero TSM-side NaNs, with forward-fill count `38 / 917 = 4.1439%`, below the 5% provisional threshold. The larger 25 return-row drop is expected because a structural price NaN also invalidates the first return after the gap (`P_t / P_{t-1}` needs both endpoints). The listed dates align with KRX-only multi-day closures such as Lunar New Year, Chuseok, Children’s Day substitute closure, and National Foundation/Hangeul-linked October closures while NYSE/TSM traded.

## 5. Marginality / sensitivity check

The primary result is numerically valid but threshold-close:

`0.0545576132 - 0.0500000000 = +0.0045576132`

Sensitivity variants on the same paired-return series:

| Variant | δ median | δ mean | δ trimmed mean 5% | Verdict by median | Verdict by mean | Verdict by trimmed mean |
|---|---:|---:|---:|---|---|---|
| Rolling-30 | 0.0337823846 | 0.0450834252 | 0.0458642307 | inconclusive | inconclusive | inconclusive |
| Rolling-45 | 0.0572930406 | 0.0521166544 | 0.0508795105 | b_measurement_quality | b_measurement_quality | b_measurement_quality |
| Rolling-60 | 0.0545576132 | 0.0523293546 | 0.0529819660 | b_measurement_quality | b_measurement_quality | b_measurement_quality |
| Rolling-90 | 0.0199485673 | 0.0476228080 | 0.0486233742 | inconclusive | inconclusive | inconclusive |

Conclusion: the pre-registered rolling-60 / median verdict is a PASS, but the result is **brittle to defensible rolling-window choices**. Cron-D EN-DRAFT should footnote that the `b_measurement_quality` call is threshold-close and not robust to rolling-30 or rolling-90 alternatives.

## 6. Cross-check vs Day-24 EWY result

Day-24 ROK/EWY × TSM median δ was `-0.0076781970`; H25.1 Samsung × TSM median δ is `+0.0545576132`, so:

`delta_vs_day24_ewy_median = 0.0545576132 - (-0.0077) = +0.0622576132`

This magnitude is plausible as a broad-ETF dilution effect. Current iShares EWY holdings data show Samsung Electronics at about `24.04%` of EWY and SK Hynix at `23.24%` as of 2026-06-02, with `78` holdings and Information Technology at `52.88%`; that concentration is high, but still leaves nearly half of the ETF outside IT and about three quarters outside Samsung Electronics alone. A firm-level Samsung-vs-TSM coupling materially stronger than EWY-vs-TSM is therefore plausible for a supply-chain stress mechanism, though not by itself causal proof.

## Final audit verdict

**PASS-WITH-NOTES.** The committed H25.1 JSON is reproducible and the pre-registered median verdict assignment is correct. The result should be reported with a marginality/brittleness footnote because the threshold overshoot is only `+0.0045576` and rolling-window sensitivity can flip the verdict to `inconclusive`.
