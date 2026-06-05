# Nisaba Numerical Audit — Day-26 cron-C H26.1 Firm-Level Cross-Substrate Re-Test

**Artifact audited:** `research/cross_substrate/dione-day26-cronC-h26_1-output.json`  
**Script:** `research/cross_substrate/dione-day26-cronC-h26_1-firm-level-retest.py`  
**Data:** `research/cross_substrate/dione-day26-cronB-data/tickers_wide.csv`  
**Audit time:** 2026-06-05 14:07 CEST  
**Top-line verdict:** **CONCUR_WITH_NOTES**

## Summary

I concur with the published `INCONCLUSIVE` verdict. The branch is correctly applied: ROK is not #1, ROK is not #4/bottom with negative δ, and two substrates are outside blind intervals. Under the pre-registered §3 rule, `2+` blind-interval misses are an **INCONCLUSIVE** condition, not an escalation to FAIL.

The main numerical caveat is sensitivity: `δ_ROK = +0.0515007346` is only `+0.0015007346` above the `[+0.05, +0.10]` floor. ±5 trading-day anchor perturbations can push ROK below the floor, so the firm-level direction is real enough to avoid the Day-24 negative-ROK pattern, but too marginal to frame as robust cross-substrate rehabilitation.

## 1. Reproducibility

Re-ran the script verbatim:

```bash
python3 research/cross_substrate/dione-day26-cronC-h26_1-firm-level-retest.py
```

Result:

```json
{
  "verdict": "INCONCLUSIVE",
  "ranked": ["EU", "JPN", "ROK", "US"],
  "rok_delta": 0.05150073457898527,
  "output": "dione-day26-cronC-h26_1-output.json"
}
```

The output is identical to the supplied JSON after excluding `computed_at`, which is necessarily refreshed by the rerun. All numeric fields and verdict fields matched exactly.

## 2. Method-spec adherence

Checked constants in `dione-day26-cronC-h26_1-firm-level-retest.py` against the Day-26 queue / scheduling specs:

| Field | Script value | Spec match |
|---|---:|---|
| `SUBSTRATES["ROK"]` | `005930.KS` | yes — M-25-1 amendment applied |
| `ANCHOR` | `TSM` | yes |
| `STRESS_ANCHORS` | DUV `2023-01-27`; LAI `2024-01-13`; PRC `2025-10-10` | yes |
| `ROLLING_WIN` | `60` | yes |
| `STRESS_HALFWIDTH_TDAYS` | `20` | yes |
| `BLIND_INTERVALS["US"]` | `[-0.05, +0.05]` | yes |
| `BLIND_INTERVALS["JPN"]` | `[0.00, +0.05]` | yes |
| `BLIND_INTERVALS["ROK"]` | `[+0.05, +0.10]` | yes |
| `BLIND_INTERVALS["EU"]` | `[-0.03, +0.05]` | yes |
| `PREDICTED_ORDERING` | `ROK > JPN > EU > US` | yes |
| `PERMUTATION_EQUIVALENT` | `ROK > JPN > US > EU` | yes |
| `M_25_1_AMENDMENT_APPLIED` | `true` | yes |

No method-spec deviation found.

## 3. Verdict-rule application

Observed order and blind-interval status:

| Substrate | δ | Blind interval | Inside? | Rank |
|---|---:|---:|---|---:|
| EU | `+0.0795893380` | `[-0.03, +0.05]` | no | 1 |
| JPN | `+0.0546669775` | `[0.00, +0.05]` | no | 2 |
| ROK | `+0.0515007346` | `[+0.05, +0.10]` | yes | 3 |
| US | `+0.0341951797` | `[-0.05, +0.05]` | yes | 4 |

Rule check:

- PASS fails: ROK is not ranked #1; observed ordering is neither predicted nor permutation-equivalent; `n_outside_blind_interval = 2`.
- FAIL fails: ROK is not bottom and `δ_ROK > 0`.
- INCONCLUSIVE applies directly: ROK not #1 and `2+` substrates outside blind intervals.

Therefore the correct verdict is **INCONCLUSIVE**. The `2 outside blind` condition should **not** escalate past INCONCLUSIVE under the written §3 / §4.5 rule; FAIL is explicitly narrower (`ROK at #4` and `δ_ROK < 0`).

## 4. Asymmetric-calendar drop audit

Data shape:

- Wide close rows: `917`.
- Log-return rows after `.dropna(how="all")`: `916`.
- ROK pair rows after `.dropna()`: `891`.
- Difference: `25` return rows dropped from the ROK pair.

Drop source:

- Dropped return rows with `005930.KS` NaN: `25`.
- Dropped return rows with `TSM` NaN: `0`.
- Price-level NaN cells: `17`, all in `005930.KS`; all other columns, including TSM, have `0` NaNs.

The 17 price-level ROK NaNs expand to 25 return-level NaNs because a missing close can contaminate both the missing date's return and the next trading day's return; consecutive holiday blocks reduce the expansion.

Price-level `005930.KS` NaN dates:

```text
2022-10-03, 2023-01-24, 2023-09-29, 2023-10-02, 2023-10-03,
2024-02-12, 2024-09-17, 2024-09-18,
2025-01-28, 2025-01-29, 2025-01-30, 2025-05-06,
2025-10-06, 2025-10-07, 2025-10-08, 2025-10-09,
2026-02-18
```

Stress/baseline allocation of the 25 dropped return rows:

- Stress-window drops: `9`.
- Baseline drops: `16`.

All dropped rows are exclusively ROK-side / Korean-calendar gaps, not TSM-side gaps. However, the gaps are not distribution-neutral: the PRC 2025 stress window loses five consecutive ROK return rows around `2025-10-06..2025-10-10`, and DUV/LAI lose two each. This explains the lower ROK rolling counts (`rolling_n_stress = 113`, `rolling_n_baseline = 719`) versus the other substrates (`123` / `734`). I do not find a halt condition, but I would phrase the result as calendar-asymmetric and marginal.

## 5. Marginality / ±5 trading-day anchor sensitivity

Original global-mask ROK result:

- `δ_ROK = +0.0515007346`
- `rolling_n_stress = 113`, `rolling_n_baseline = 719`
- inside `[+0.05, +0.10]` by only `+0.0015007346`

Individual ±5 trading-day anchor perturbations:

| Anchor perturbation | δ_ROK | Inside `[+0.05,+0.10]`? | rolling n stress/base |
|---|---:|---|---:|
| DUV −5 td | `+0.040422519` | no | `108 / 724` |
| DUV +5 td | `+0.063502763` | yes | `114 / 718` |
| LAI −5 td | `+0.055548302` | yes | `115 / 717` |
| LAI +5 td | `+0.035924672` | no | `113 / 719` |
| PRC −5 td | `+0.052265255` | yes | `113 / 719` |
| PRC +5 td | `+0.051500735` | yes | `113 / 719` |

Combined 3-anchor perturbation grid (`{-5,0,+5}^3`, 27 cases):

- Minimum: `+0.023930082` at DUV −5, LAI +5, PRC 0 (`108 / 724`) — outside below floor.
- Maximum: `+0.068369006` at DUV +5, LAI 0, PRC −5 (`114 / 718`) — inside.
- Below the `+0.05` floor: `9 / 27` cases.
- Above the `+0.10` ceiling: `0 / 27` cases.

This materially weakens the directional reading. The correct publication language is: **ROK becomes positive and barely in-interval under the pre-registered anchors, consistent with the Day-25 firm-level signal, but the in-interval status is not stable under small anchor shifts.**

## 6. Comparison to Day-24 / Day-25

- Day-24 ETF ROK (`EWY × TSM`) δ: `−0.00767819696` (reported rounded `−0.0077`).
- Day-26 firm ROK (`005930.KS × TSM`) δ: `+0.05150073458`.
- Swing: `+0.05917893154`, i.e. `+0.0592` rounded.

Day-25 isolated H25.1 (`005930.KS × TSM`) δ: `+0.05455761318`.
Day-26 cross-substrate H26.1 ROK δ: `+0.05150073458`.
Difference: `−0.00305687860`.

These are mutually consistent. The difference is method/calendar-index driven, not contradictory:

- Day-25 pair-isolated mask uses the ROK/TSM pair calendar after dropna (`n_returns = 891`; stress/base rolling counts `120 / 712`).
- Day-26 cross-substrate mask is built on the global NYSE-aligned return index (`n_returns = 916`) and then intersected with the ROK pair's rolling dates (`113 / 719`).
- Recomputing Day-26 ROK with a Day-25-style pair-calendar stress mask reproduces Day-25 exactly: `δ = +0.05455761318`.

So the Day-26 value is not a failed reproduction of Day-25; it is the expected value under the cross-substrate global-mask convention.

## Final audit verdict

**CONCUR_WITH_NOTES.**

Publication-safe statement:

> H26.1 is correctly INCONCLUSIVE. The M-25-1 firm-level substitution removes the Day-24 negative ROK sign problem (`−0.0077 → +0.0515`) and is numerically consistent with Day-25 H25.1 (`+0.0546`), but it does not rehabilitate the full cross-substrate ordering: ROK ranks #3, EU and JPN exceed blind intervals, and the ROK in-interval status is marginal under ±5 td anchor sensitivity.

## Material findings

1. **Verdict branch is correct:** `2+` blind misses and ROK not #1 are INCONCLUSIVE, not FAIL; FAIL requires ROK bottom plus negative δ.
2. **Calendar asymmetry is real but source-bounded:** all 25 dropped return rows are ROK-side (`005930.KS`) gaps; TSM has zero dropped rows. Stress windows lose 9 ROK return rows, so counts differ, but no halt rule fires.
3. **ROK direction is marginal:** original `δ_ROK = +0.0515` is only `+0.0015` above floor; 9/27 combined ±5 td perturbations fall below `+0.05`, so avoid robust “rehabilitated” wording.
