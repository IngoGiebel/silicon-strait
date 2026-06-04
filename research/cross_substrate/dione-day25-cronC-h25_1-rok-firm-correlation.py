"""Day-25 cron-C — H25.1 ROK firm-level disambiguation correlation test.

Pre-staged by Dione 2026-06-04 cron-B; executed at cron-C 14:00 CEST.

Pre-registration: research/cross_substrate/dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md
                  (commit 3f396fc; not revised post data-pull)
Errata (clarifications, no method change): research/methodology/dione-day25-cronB-h25_1-pre-registration-errata-2026-06-04.md
                  (this fire; clarifies §4.5 NaN gate + §4.3 mean-vs-median ambiguity)

Method (single-pair adaptation of Day-24 cron-C four-pair template):
  - Daily adjusted closes from Day-25 cron-B data pull (005930.KS reindexed to NYSE/TSM calendar
    w/ ffill-limit-1, joined to TSM from Day-24 cron-B)
  - Log returns: log(P_t / P_{t-1})
  - Pearson rolling-60 correlation between r_{005930.KS} and r_{TSM}, on co-trading days only
    (i.e. after `.dropna()` to handle the 17 KRX-side structural NaN per Day-24 cron-C convention)
  - Stress windows (±20 trading days around each anchor; union = stress; rest = baseline),
    IDENTICAL to Day-24 cron-C:
      DUV anchor: 2023-01-27 (US-JP-NL trilateral DUV export-control announcement)
      LAI anchor: 2024-01-13 (Lai Ching-te election victory)
      PRC anchor: 2025-10-10 (PRC MOFCOM port-fee announcement)
  - Stress δ (verdict-assignment statistic): MEDIAN of rolling-60 ρ over stress trading days
    minus MEDIAN over baseline trading days. Median chosen per Day-24 cron-C calibration
    convention (errata §3.bis); mean computed and reported as secondary statistic.

H25.1 verdict assignment (pre-registration §3, UNCHANGED):
  δ < −0.001 → verdict_path = "a_schema_update"     (sign-flip; ROK = DIRECT/SUBSTITUTION dynamics)
  −0.001 ≤ δ ≤ +0.05 → verdict_path = "inconclusive" (both paths alive)
  δ > +0.05 → verdict_path = "b_measurement_quality" (EWY too dilute; firm-level signal correct)

Output: dione-day25-cronC-h25_1-output.json
        (consumed by Day-25 cron-D EN-DRAFT publication)
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "dione-day25-cronB-data" / "tickers_wide.csv"
OUT = HERE / "dione-day25-cronC-h25_1-output.json"

TICKER = "005930.KS"
ANCHOR = "TSM"

STRESS_ANCHORS = {
    "DUV_2023": "2023-01-27",
    "LAI_2024": "2024-01-13",
    "PRC_2025": "2025-10-10",
}
STRESS_HALFWIDTH_TDAYS = 20
ROLLING_WIN = 60

VERDICT_BUCKETS = {
    "a_schema_update": (-np.inf, -0.001),       # δ < -0.001
    "inconclusive": (-0.001, 0.05),             # -0.001 ≤ δ ≤ 0.05
    "b_measurement_quality": (0.05, np.inf),    # δ > 0.05
}


def stress_mask(idx: pd.DatetimeIndex) -> pd.Series:
    """Boolean mask: True for observations within ±20 td of any anchor.

    Identical to Day-24 cron-C convention.
    """
    mask = pd.Series(False, index=idx)
    for label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        pos = idx.searchsorted(anchor)
        if pos == len(idx):
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(idx), pos + STRESS_HALFWIDTH_TDAYS + 1)
        mask.iloc[lo:hi] = True
    return mask


def assign_verdict(delta: float) -> str:
    if np.isnan(delta):
        return "nan_undefined"
    if delta < -0.001:
        return "a_schema_update"
    if delta > 0.05:
        return "b_measurement_quality"
    return "inconclusive"


def main() -> int:
    computed_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not DATA.exists():
        print(f"DATA MISSING: {DATA}", file=sys.stderr)
        return 2

    wide = pd.read_csv(DATA, index_col="date", parse_dates=["date"]).sort_index()
    n_before_drop = int(len(wide))

    # Compute log-returns on full grid first, then dropna (Day-24 convention)
    log_ret = np.log(wide / wide.shift(1))
    pair = log_ret[[TICKER, ANCHOR]].dropna()
    n_pair_obs = int(len(pair))
    n_dropped = n_before_drop - n_pair_obs - 1  # -1 for the leading shift(1) NaN row

    full_window = {
        "first_date": pair.index.min().strftime("%Y-%m-%d"),
        "last_date": pair.index.max().strftime("%Y-%m-%d"),
        "n_returns": n_pair_obs,
    }

    full_pearson = float(pair[TICKER].corr(pair[ANCHOR]))

    mask = stress_mask(pair.index)
    stress_idx = pair.index[mask]
    baseline_idx = pair.index[~mask]

    stress_anchor_meta = {}
    for label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        pos = pair.index.searchsorted(anchor)
        if pos == len(pair.index):
            stress_anchor_meta[label] = {"anchor": anchor_date, "in_data": False}
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(pair.index), pos + STRESS_HALFWIDTH_TDAYS + 1)
        stress_anchor_meta[label] = {
            "anchor": anchor_date,
            "in_data": True,
            "window_first": pair.index[lo].strftime("%Y-%m-%d"),
            "window_last": pair.index[hi - 1].strftime("%Y-%m-%d"),
            "n_td": hi - lo,
        }

    roll = pair[TICKER].rolling(ROLLING_WIN).corr(pair[ANCHOR]).dropna()
    roll_stress = roll.loc[roll.index.intersection(stress_idx)]
    roll_baseline = roll.loc[roll.index.intersection(baseline_idx)]

    stress_median = float(roll_stress.median()) if len(roll_stress) else float("nan")
    baseline_median = float(roll_baseline.median()) if len(roll_baseline) else float("nan")
    delta_median = (
        stress_median - baseline_median
        if not (np.isnan(stress_median) or np.isnan(baseline_median))
        else float("nan")
    )

    stress_mean = float(roll_stress.mean()) if len(roll_stress) else float("nan")
    baseline_mean = float(roll_baseline.mean()) if len(roll_baseline) else float("nan")
    delta_mean = (
        stress_mean - baseline_mean
        if not (np.isnan(stress_mean) or np.isnan(baseline_mean))
        else float("nan")
    )

    verdict_path = assign_verdict(delta_median)
    verdict_path_via_mean = assign_verdict(delta_mean)
    verdict_consensus = (
        "agree" if verdict_path == verdict_path_via_mean else "mean_median_disagreement"
    )

    out = {
        "computed_at": computed_at,
        "pre_registration": "research/cross_substrate/dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md (commit 3f396fc)",
        "errata": "research/methodology/dione-day25-cronB-h25_1-pre-registration-errata-2026-06-04.md (this Day-25 cron-B fire)",
        "input_data": str(DATA.relative_to(HERE.parent.parent)),
        "method": {
            "log_returns": "log(P_t / P_{t-1})",
            "rolling_window_td": ROLLING_WIN,
            "stress_half_width_td": STRESS_HALFWIDTH_TDAYS,
            "delta_primary": "median(rolling_corr | stress) - median(rolling_corr | baseline)",
            "delta_secondary": "mean(rolling_corr | stress) - mean(rolling_corr | baseline)",
            "verdict_uses": "median (per Day-24 calibration convention)",
            "pair": f"{TICKER} x {ANCHOR}",
            "join_calendar": "NYSE (Day-24 cron-B TSM index); KRX ffill-limit-1; then .dropna()",
        },
        "full_window": full_window,
        "stress_anchors": stress_anchor_meta,
        "n_stress_td": int(len(stress_idx)),
        "n_baseline_td": int(len(baseline_idx)),
        "rolling_n_stress": int(len(roll_stress)),
        "rolling_n_baseline": int(len(roll_baseline)),
        "n_pair_obs_after_dropna": n_pair_obs,
        "n_dropped_asymmetric_calendar": n_dropped,
        "full_window_pearson": full_pearson,
        "stress_median_rolling_corr": stress_median,
        "baseline_median_rolling_corr": baseline_median,
        "stress_mean_rolling_corr": stress_mean,
        "baseline_mean_rolling_corr": baseline_mean,
        "delta_median": delta_median,
        "delta_mean": delta_mean,
        "h25_1": {
            "verdict_path": verdict_path,
            "verdict_path_via_mean": verdict_path_via_mean,
            "verdict_consensus": verdict_consensus,
            "verdict_intervals": {
                "a_schema_update": "delta < -0.001",
                "inconclusive": "-0.001 <= delta <= 0.05",
                "b_measurement_quality": "delta > 0.05",
            },
            "day24_ewy_benchmark_delta": -0.0077,
            "delta_vs_day24_ewy_median": (
                None if np.isnan(delta_median) else float(delta_median - (-0.0077))
            ),
        },
    }

    def _np_default(o):
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        raise TypeError(f"Object of type {type(o).__name__} is not JSON serializable")

    OUT.write_text(json.dumps(out, indent=2, default=_np_default, ensure_ascii=False))
    print(json.dumps({
        "verdict_path": verdict_path,
        "verdict_consensus": verdict_consensus,
        "delta_median": delta_median,
        "delta_mean": delta_mean,
        "output": str(OUT.name),
    }, indent=2, default=_np_default, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
