"""Day-24 cron-C — H24.1 textual-axis 4-substrate correlation test.

Pre-staged by Dione 2026-06-03 cron-B; executed at cron-C 14:00 CEST.

Method (per Day-21 §4.2 precedent, replicated for Day-24 textual axis):
  - Daily adjusted closes from Day-24 cron-B data pull (5 tickers; 2022-10-03..2026-05-29)
  - Log returns: log(P_t / P_{t-1})
  - Pearson rolling-60 correlation between each substrate ETF and TSM
  - Stress windows (±20 trading days around each anchor; union = stress; rest = baseline):
      DUV anchor: 2023-01-27 (US-JP-NL trilateral DUV export-control announcement)
      LAI anchor: 2024-01-13 (Lai Ching-te election victory)
      PRC anchor: 2025-10-10 (PRC MOFCOM port-fee announcement)
  - Delta = stress_median - baseline_median for each (substrate, TSM) pair
  - Also compute full-window Pearson(returns_substrate, returns_TSM) for comparison

H24.1 falsification rule (per cron-A scoping §3.2):
  PASSES if observed ordering matches predicted (ROK > JPN > EU > US) OR is
    1-permutation-equivalent (ROK > JPN > US > EU); ROK MUST be at top.
  FAILS if ROK is not at top.
  INCONCLUSIVE if >1 reversal from prediction OR 2+ substrates outside their blind intervals.

Blind δ intervals (per cron-A §3.1, pre-registered BEFORE this data was pulled):
  US:  [-0.05, +0.05]
  JPN: [ 0.00, +0.05]
  ROK: [+0.05, +0.10]
  EU:  [-0.03, +0.05]

Output: dione-day24-cronC-output.json (consumed by Day-24 cron-D EN-DRAFT)
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "dione-day24-cronB-data" / "tickers_wide.csv"
OUT = HERE / "dione-day24-cronC-output.json"

SUBSTRATES = {"US": "SPY", "JPN": "EWJ", "ROK": "EWY", "EU": "EZU"}
ANCHOR = "TSM"

STRESS_ANCHORS = {
    "DUV_2023": "2023-01-27",
    "LAI_2024": "2024-01-13",
    "PRC_2025": "2025-10-10",
}
STRESS_HALFWIDTH_TDAYS = 20
ROLLING_WIN = 60

BLIND_INTERVALS = {
    "US": (-0.05, 0.05),
    "JPN": (0.00, 0.05),
    "ROK": (0.05, 0.10),
    "EU": (-0.03, 0.05),
}
PREDICTED_ORDERING = ["ROK", "JPN", "EU", "US"]
PERMUTATION_EQUIVALENT = ["ROK", "JPN", "US", "EU"]


def stress_mask(idx: pd.DatetimeIndex) -> pd.Series:
    """Boolean mask: True for observations within ±20 td of any anchor."""
    mask = pd.Series(False, index=idx)
    for label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        # nearest td position to anchor; if anchor is non-td, snap to next available
        pos = idx.searchsorted(anchor)
        if pos == len(idx):
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(idx), pos + STRESS_HALFWIDTH_TDAYS + 1)
        mask.iloc[lo:hi] = True
    return mask


def main() -> int:
    computed_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not DATA.exists():
        print(f"DATA MISSING: {DATA}", file=sys.stderr)
        return 2

    wide = pd.read_csv(DATA, index_col="date", parse_dates=["date"]).sort_index()
    log_ret = np.log(wide / wide.shift(1)).dropna(how="all")

    full_window = {
        "first_date": log_ret.index.min().strftime("%Y-%m-%d"),
        "last_date": log_ret.index.max().strftime("%Y-%m-%d"),
        "n_returns": int(log_ret.shape[0]),
    }

    mask = stress_mask(log_ret.index)
    stress_idx = log_ret.index[mask]
    baseline_idx = log_ret.index[~mask]

    stress_anchor_meta = {}
    for label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        pos = log_ret.index.searchsorted(anchor)
        if pos == len(log_ret.index):
            stress_anchor_meta[label] = {"anchor": anchor_date, "in_data": False}
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(log_ret.index), pos + STRESS_HALFWIDTH_TDAYS + 1)
        stress_anchor_meta[label] = {
            "anchor": anchor_date,
            "in_data": True,
            "window_first": log_ret.index[lo].strftime("%Y-%m-%d"),
            "window_last": log_ret.index[hi - 1].strftime("%Y-%m-%d"),
            "n_td": hi - lo,
        }

    results = {}
    for substrate, ticker in SUBSTRATES.items():
        pair = log_ret[[ticker, ANCHOR]].dropna()
        full_pearson = float(pair[ticker].corr(pair[ANCHOR]))

        roll = pair[ticker].rolling(ROLLING_WIN).corr(pair[ANCHOR]).dropna()
        roll_stress = roll.loc[roll.index.intersection(stress_idx)]
        roll_baseline = roll.loc[roll.index.intersection(baseline_idx)]

        stress_median = float(roll_stress.median()) if len(roll_stress) else float("nan")
        baseline_median = float(roll_baseline.median()) if len(roll_baseline) else float("nan")
        delta = stress_median - baseline_median if not (np.isnan(stress_median) or np.isnan(baseline_median)) else float("nan")

        lo_int, hi_int = BLIND_INTERVALS[substrate]
        inside_interval = (not np.isnan(delta)) and (lo_int <= delta <= hi_int)

        results[substrate] = {
            "ticker": ticker,
            "n_pair_obs": int(pair.shape[0]),
            "full_window_pearson": full_pearson,
            "rolling_window_td": ROLLING_WIN,
            "rolling_n_stress": int(len(roll_stress)),
            "rolling_n_baseline": int(len(roll_baseline)),
            "stress_median_rolling_corr": stress_median,
            "baseline_median_rolling_corr": baseline_median,
            "delta": delta,
            "blind_interval": [lo_int, hi_int],
            "inside_blind_interval": inside_interval,
        }

    # H24.1 verdict
    ranked = sorted(SUBSTRATES.keys(), key=lambda s: results[s]["delta"], reverse=True)
    rok_top = ranked[0] == "ROK"
    matches_predicted = ranked == PREDICTED_ORDERING
    matches_permequiv = ranked == PERMUTATION_EQUIVALENT
    n_outside_interval = sum(1 for s in SUBSTRATES if not results[s]["inside_blind_interval"])

    if not rok_top:
        verdict = "FAIL"
        verdict_reason = f"ROK not at top of δ ordering (observed: {ranked[0]})."
    elif matches_predicted or matches_permequiv:
        verdict = "PASS"
        verdict_reason = (
            "Predicted ordering ROK > JPN > EU > US matched"
            if matches_predicted
            else "Permutation-equivalent ordering ROK > JPN > US > EU matched"
        )
    else:
        verdict = "INCONCLUSIVE"
        verdict_reason = f"ROK at top but ordering ({ranked}) is >1 reversal from prediction."

    if n_outside_interval >= 2:
        verdict = "INCONCLUSIVE"
        verdict_reason = f"{verdict_reason}; {n_outside_interval} substrates outside blind intervals."

    out = {
        "computed_at": computed_at,
        "input_data": str(DATA.relative_to(HERE.parent.parent)),
        "method": {
            "log_returns": "log(P_t / P_{t-1})",
            "rolling_window_td": ROLLING_WIN,
            "stress_half_width_td": STRESS_HALFWIDTH_TDAYS,
            "delta": "median(rolling_corr | stress) - median(rolling_corr | baseline)",
            "pair_anchor": ANCHOR,
        },
        "full_window": full_window,
        "stress_anchors": stress_anchor_meta,
        "n_stress_td": int(len(stress_idx)),
        "n_baseline_td": int(len(baseline_idx)),
        "per_substrate": results,
        "h24_1": {
            "predicted_ordering": PREDICTED_ORDERING,
            "permutation_equivalent": PERMUTATION_EQUIVALENT,
            "observed_ordering": ranked,
            "rok_at_top": rok_top,
            "n_outside_blind_interval": n_outside_interval,
            "verdict": verdict,
            "verdict_reason": verdict_reason,
        },
        "h21_1c_orthogonality": {
            "status": "BLOCKED",
            "blocker": "Day-23 §4.4 operational-axis δ values FAIL Nisaba audit (abbf875): 4/6 cells not reproducible from cited Day-21 source; AIR.PA conflicts with v1.2 EU=NEUTRAL classification. Pearson(δ_textual, δ_operational) cannot be computed until q-day24-1 (§4.4 repair-path) resolves.",
            "pre_committed_pass_interval": [-0.3, 0.3],
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

    OUT.write_text(json.dumps(out, indent=2, default=_np_default))
    print(json.dumps({"verdict": verdict, "ranked": ranked, "output": str(OUT.name)}, indent=2, default=_np_default))
    return 0


if __name__ == "__main__":
    sys.exit(main())
