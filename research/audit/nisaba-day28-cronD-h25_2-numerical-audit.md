# Nisaba Numerical Audit - Day-28 cron-D H25.2 EU Member-State Decomposition

**Audit fire:** Day-28 cron-D sync, 2026-06-12  
**Auditor:** Nisaba  
**Target commit:** `b788d8912379d673529d648f2cb968f019d42173`  
**Target preregistration:** `research/cross_substrate/dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md`  
**Target harness:** `research/cross_substrate/dione-day28-cronD-h25_2-eu-member-decomposition.py`  
**Target output:** `research/cross_substrate/dione-day28-cronD-h25_2-output.json`  
**Verdict:** **CONCUR_WITH_NOTES**

The committed H25.2 output is reproducible cell-for-cell from `tickers_wide.csv` using the preregistered log-return, rolling-60 Pearson, pooled-stress median method. The combined verdict assignment to path (b), `b_ezu_constituent_weighting_artifact`, is numerically correct under the preregistered ambiguity-default rule.

The notes are publication-relevant rather than dissenting: all three member-state deltas fall outside their preregistered intervals, EWN has a median/mean sign flip, and every PRC_2025 per-anchor informational delta is negative even though the pooled median deltas are positive for all three pairs.

## 1. Reproduction Method

I recomputed from:

`research/cross_substrate/dione-day28-cronD-data/tickers_wide.csv`

using:

```bash
uv run --with pandas --with numpy python
```

The recomputation did not rerun the harness. It rebuilt log returns from the CSV, rebuilt the three +/-20 trading-day stress masks on the return index, and computed each 60-row Pearson correlation with an explicit `np.corrcoef` loop before taking stress and baseline medians.

Input/data checks:

| Check | Recomputed value | Status |
|---|---:|---|
| Price rows | 917 | PASS |
| Price date range | 2022-10-03..2026-05-29 | PASS |
| Return rows after log shift | 916 | PASS |
| Return date range | 2022-10-04..2026-05-29 | PASS |
| NaN cells in joined price table | 0 | PASS |
| Stress return days | 123 | PASS |
| Baseline return days | 793 | PASS |
| Rolling rows per pair after 60-day warmup | 857 | PASS |
| Rolling stress rows per pair | 123 | PASS |
| Rolling baseline rows per pair | 734 | PASS |

Stress-window indexing:

| Anchor | First trading return date >= anchor | Window first | Window last | Return td |
|---|---:|---:|---:|---:|
| DUV_2023 / 2023-01-27 | 2023-01-27 | 2022-12-28 | 2023-02-27 | 41 |
| LAI_2024 / 2024-01-13 | 2024-01-16 | 2023-12-14 | 2024-02-13 | 41 |
| PRC_2025 / 2025-10-10 | 2025-10-10 | 2025-09-12 | 2025-11-07 | 41 |

The 2024 anchor falls on a non-trading day; the harness and recomputation both use the first available return date after the anchor, then take +/-20 trading days inclusive.

## 2. Pooled Delta Reproduction

| Pair | Baseline median rolling rho | Stress median rolling rho | Recomputed delta | JSON delta | Difference | Interval placement |
|---|---:|---:|---:|---:|---:|---|
| EWG x TSM | 0.4416766584 | 0.5548556430 | +0.1131789846 | +0.1131789846 | +5.55e-17 | above `[+0.02, +0.07]` |
| EWQ x TSM | 0.3960602699 | 0.5334384981 | +0.1373782281 | +0.1373782281 | -2.78e-16 | above `[0.00, +0.06]` |
| EWN x TSM | 0.6424761439 | 0.6559992168 | +0.0135230729 | +0.0135230729 | +2.22e-16 | below `[+0.08, +0.18]` |

Combined statistic:

| Statistic | Recomputed | JSON | Status |
|---|---:|---:|---|
| `mean_delta` | +0.0880267619 | +0.0880267619 | PASS |
| `n_pairs_above_+0.05` | 2 | 2 | PASS |
| Inside preregistered interval | 0/3 | 0/3 | PASS |

Interval miss magnitudes:

| Pair | Delta | Miss |
|---|---:|---:|
| EWG x TSM | +0.1131789846 | +0.0431789846 above upper bound |
| EWQ x TSM | +0.1373782281 | +0.0773782281 above upper bound |
| EWN x TSM | +0.0135230729 | -0.0664769271 below lower bound |

## 3. Verdict-Rule Audit

Path (a) test:

```text
all three delta > +0.05 AND mean(delta) >= +0.0796
```

Result: **FAIL**. The mean condition passes (`+0.0880267619 >= +0.0796`), but only two pairs exceed `+0.05`; EWN is `+0.0135230729`.

Path (b-refined) test:

```text
EWN delta > +0.10 AND EWG delta < +0.03 AND EWQ delta < +0.03
```

Result: **FAIL**. EWN is not above `+0.10`, and EWG/EWQ are not below `+0.03`.

Ambiguity-default assignment:

```text
2 of 3 above +0.05 AND mean(delta) >= +0.0796
```

Result: **PATH (b)** by the preregistration's explicit ambiguity-default sentence. The harness output `b_ezu_constituent_weighting_artifact` is therefore correct. The path (b) table row also contains "Only 1-2 of three delta > +0.05", so the wording is redundant but not outcome-changing.

## 4. Secondary Mean/Median Flags

| Pair | Median delta | Mean secondary delta | Sign disagreement flag | Status |
|---|---:|---:|---|---|
| EWG x TSM | +0.1131789846 | +0.0519696619 | false | PASS |
| EWQ x TSM | +0.1373782281 | +0.0393595547 | false | PASS |
| EWN x TSM | +0.0135230729 | -0.0181948856 | true | PASS |

EWN is the only sign flip. It is correctly flagged in the JSON and should be kept visible in prose because the primary statistic is positive while the secondary mean statistic is negative.

## 5. Per-Anchor Informational Delta Sanity Check

Per-anchor deltas recompute exactly against each pair's pooled baseline median:

| Pair | DUV_2023 | LAI_2024 | PRC_2025 |
|---|---:|---:|---:|
| EWG x TSM | +0.2114521438 | +0.1131789846 | -0.0608224301 |
| EWQ x TSM | +0.2362034193 | +0.1373782281 | -0.1934401888 |
| EWN x TSM | +0.0773941690 | +0.0135230729 | -0.1015244189 |

The pooled-positive / PRC-negative split is arithmetically sound. The pooled statistic is not the average of the three per-anchor deltas; it is the median over all 123 rolling stress observations. In this sample the DUV and LAI windows sit high enough relative to baseline that the pooled median remains positive even though the PRC_2025 window median is below baseline for all three pairs.

## Final Audit Verdict

**CONCUR_WITH_NOTES.** The three pooled deltas, interval placements, mean statistic, path (a) failure, path (b-refined) failure, ambiguity-default path (b) assignment, EWN sign-flip flag, and PRC-negative per-anchor deltas all reproduce from the committed CSV and output JSON. No numerical dissent.
