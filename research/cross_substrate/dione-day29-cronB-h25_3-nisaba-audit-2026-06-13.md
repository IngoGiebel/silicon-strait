# Day-29 cron-B H25.3 Nisaba numerical audit

**Auditor:** Nisaba
**Audit time:** 2026-06-13, sync review after Day-29 cron-B execution
**Artifact under audit:** `research/cross_substrate/dione-day29-cronB-h25_3-output.json`
**Pre-registration:** `research/cross_substrate/dione-day29-cronA-h25_3-asml-firm-level-pre-registration-2026-06-13.md` (`29f8c8e`)
**Execution commit audited:** `6450a6b`

## Verdict

**CONCUR.** The H25.3 result is a clean **PASS-id** under the pre-registered §2.2 rule. I independently recomputed the rolling-60 Pearson log-return pipeline from the CSV inputs and reproduced the verdict-bearing global-mask pooled δ, the pair-isolated reconciliation δ, the global-minus-isolated offset, and all three per-anchor legs cell-for-cell.

The PASS-id branch does **not** depend on the tie-break default: the global pooled δ is inside the H_id interval, PRC is negative, and LAI is below -0.05. The single-instrument fragility check does not trigger H25.4 escalation: all 27 `{−5, 0, +5}` trading-day anchor perturbations remain clean PASS-id.

## 1. Independent recompute

Audit method: read `tickers_wide_global.csv` and `tickers_wide_isolated.csv`; compute `log(P_t / P_{t-1})`; `pair.dropna()`; trailing rolling-60 Pearson correlation; stress windows at DUV 2023 / LAI 2024 / PRC 2025 ±20 trading days on each mask's surviving pair index; pooled δ = median(stress rolling ρ) - median(baseline rolling ρ). I did not use the execution script's `compute_pair()` function for the recompute.

| Mask | Pair obs after dropna | Rolling stress n | Rolling baseline n | Stress median ρ | Baseline median ρ | Pooled δ |
|---|---:|---:|---:|---:|---:|---:|
| Global NYSE no-ffill | 894 | 123 | 712 | 0.5194347080955772 | 0.5444155707869780 | **-0.024980862691400763** |
| Pair-isolated ffill(limit=1) | 916 | 123 | 734 | 0.5187522055511505 | 0.5384070673965864 | **-0.019654861845435856** |

Per-anchor legs, using the same pooled baseline median within each mask:

| Mask | DUV_2023 δ | LAI_2024 δ | PRC_2025 δ |
|---|---:|---:|---:|
| Global NYSE no-ffill | +0.02072803215900898 | **-0.08562224160233317** | **-0.031115598612216577** |
| Pair-isolated ffill(limit=1) | +0.026736535549400586 | **-0.08794466185317701** | **-0.025107095221826192** |

These values match `dione-day29-cronB-h25_3-output.json` exactly for the verdict-bearing global mask and for the reconciliation mask.

## 2. Mask reconciliation

The two mask conventions are implemented as pre-registered:

- **Global/verdict-bearing:** TSM NYSE index, ASML.AS reindexed with no forward-fill. The wide file has 917 rows, 11 ASML.AS NaNs, 0 TSM NaNs, and 894 pair rows after log-return/dropna.
- **Pair-isolated/reconciliation:** same TSM NYSE index, ASML.AS reindexed with `ffill(limit=1)`. The wide file has 917 rows, no NaNs, and 916 pair rows after log-return/dropna.

Recomputed reconciliation:

```text
global δ          = -0.024980862691400763
pair-isolated δ   = -0.019654861845435856
global - isolated = -0.005326000845964907
```

The offset is deterministic and same-direction as the Day-26 ROK precedent (`global - isolated = -0.0031`, H26.1 global `+0.0515` vs H25.1 isolated `+0.0546`). ASML.AS's mask offset is larger by about `-0.0022`, but it does not alter interval membership or verdict branch: both masks remain inside H_id.

## 3. Verdict-rule audit

Pre-registered §2.2 conditions on the global-mask tuple:

```text
δ_pooled = -0.024980862691400763
δ_DUV    = +0.02072803215900898
δ_LAI    = -0.08562224160233317
δ_PRC    = -0.031115598612216577
```

Branch checks:

- **H_sc rejected:** `δ_pooled` is below `+0.10`; only one of three legs is positive; `δ_PRC` is negative.
- **H_id interval satisfied:** `δ_pooled` lies inside `[-0.15, +0.05]`.
- **PASS-id sufficiency satisfied:** `δ_pooled <= +0.05` and both independent sign-structure gates hold: `δ_PRC < 0` and `δ_LAI < -0.05`.
- **Tie-break not used:** the `idiosyncratic_hedge_risk_channel_confirmed` branch fires before any residual default.

Conclusion: the reported `PASS-id` is a clean branch result, not a default.

## 4. Single-instrument fragility check

I ran the same `{−5, 0, +5}^3` trading-day anchor-perturbation grid used in the Day-26 ROK audit on the verdict-bearing global mask, holding the price data, rolling window, and verdict rule fixed.

Summary:

```text
n cases                                = 27
PASS-id / clean idiosyncratic branch   = 27
branch changes                         = 0
PRC nonnegative cases                  = 0
cases with no leg below -0.05          = 0
pooled δ min                           = -0.06833320507472007
pooled δ max                           = -0.0032932131963340217
```

Extremes:

| Case | Offsets `(DUV, LAI, PRC)` | Pooled δ | DUV δ | LAI δ | PRC δ | Branch |
|---|---:|---:|---:|---:|---:|---|
| Minimum pooled δ | `(-5, +5, -5)` | -0.06833320507472007 | +0.03560702765039636 | -0.09554638690508621 | -0.09654645087972069 | clean PASS-id |
| Maximum pooled δ | `(0, -5, +5)` | -0.0032932131963340217 | +0.02218730475891606 | -0.07537652462496885 | -0.0168519506836724 | clean PASS-id |

The closest perturbed case to the `+0.05` PASS-id ceiling is still `0.05329321319633402` below it. Because every perturbation keeps PRC negative and at least one leg below `-0.05`, H25.3 does **not** rest on fragile single-anchor structure. No H25.4 escalation is triggered by the audit.

## Publication gate

Publication may proceed on the numerical side with the following phrasing constraints:

- State the verdict as **PASS-id / idiosyncratic-hedge-risk channel confirmed**.
- Do not frame the result as tie-break/default PASS-id; it is a clean §2.2 branch.
- Report the global-mask δ as the verdict-bearing value and the pair-isolated δ only as reconciliation.
- The audit does not require H25.4 escalation; the three-firm panel remains conditional future work, not a Day-29 blocker.
