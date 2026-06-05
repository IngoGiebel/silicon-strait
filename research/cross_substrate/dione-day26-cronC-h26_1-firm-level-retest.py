"""Day-26 cron-C — H26.1 firm-level re-test of H24.1 under protocol amendment M-25-1.

Pre-staged by Dione 2026-06-05 cron-B; executed at cron-C 14:00 CEST.

Mirrors Day-24 cron-C dione-day24-cronC-h24_1-correlation.py with one change:
the ROK textual-axis ticker is 005930.KS (Samsung Electronics, KRX) per the
Day-25 cron-D protocol amendment M-25-1 (retires EWY for the textual axis).

Method (per H26.1 spec §4 in research/cross_substrate/dione-day26-cronA-h24_1-firm-level-retest-queue-2026-06-04.md;
identical to Day-24 cron-C except the ROK substitution):
  - Daily adjusted closes from Day-26 cron-B data assembly (dione-day26-cronB-data/tickers_wide.csv).
    Columns: SPY, EWJ, 005930.KS, EZU, TSM. 917 rows. NYSE calendar.
    Source provenance: locked Day-24 cron-B SPY/EWJ/EZU/TSM + locked Day-25 cron-B 005930.KS.
  - Log returns: log(P_t / P_{t-1}).
  - Pearson rolling-60 correlation between each substrate ticker and TSM.
  - Stress windows (±20 td around each anchor; union = stress; rest = baseline):
      DUV anchor: 2023-01-27
      LAI anchor: 2024-01-13
      PRC anchor: 2025-10-10
  - Stress δ = median(rolling-60 ρ | stress) − median(rolling-60 ρ | baseline) per substrate.

H26.1 falsification rule (per spec §3, identical to H24.1 §3.2):
  PASS         if observed ordering matches predicted (ROK > JPN > EU > US) OR is
               1-permutation-equivalent (ROK > JPN > US > EU); ROK MUST be at top;
               and ≤1 substrate falls outside its blind interval.
  INCONCLUSIVE if ROK not at top, OR >1 reversal from prediction, OR 2+ substrates
               outside blind intervals.
  FAIL         if ROK at #4 (bottom) AND δ_ROK < 0 — falsifies path (b)
               measurement-quality at the cross-substrate level even after M-25-1.

Blind δ intervals (per spec §4.5, pre-registered at Day-25 cron-D and CARRIED OVER unchanged to Day-26):
  US:  [-0.05, +0.05]
  JPN: [ 0.00, +0.05]
  ROK: [+0.05, +0.10]  (carries over from H24.1; Day-25 H25.1 δ=+0.0546 inside bottom edge)
  EU:  [-0.03, +0.05]

Output: dione-day26-cronC-h26_1-output.json
  Schema matches Day-24 cron-C output with m_25_1_amendment_applied=true and the
  h24_1 verdict block renamed to h26_1.
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "dione-day26-cronB-data" / "tickers_wide.csv"
OUT = HERE / "dione-day26-cronC-h26_1-output.json"

SUBSTRATES = {"US": "SPY", "JPN": "EWJ", "ROK": "005930.KS", "EU": "EZU"}
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

M_25_1_AMENDMENT_APPLIED = True
ROK_TICKER_RETIRED_UNDER_M_25_1 = "EWY"


def stress_mask(idx: pd.DatetimeIndex) -> pd.Series:
    """Boolean mask: True for observations within ±20 td of any anchor."""
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
        delta = (
            stress_median - baseline_median
            if not (np.isnan(stress_median) or np.isnan(baseline_median))
            else float("nan")
        )

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

    # H26.1 verdict
    ranked = sorted(SUBSTRATES.keys(), key=lambda s: results[s]["delta"], reverse=True)
    rok_top = ranked[0] == "ROK"
    rok_bottom = ranked[-1] == "ROK"
    rok_delta = results["ROK"]["delta"]
    matches_predicted = ranked == PREDICTED_ORDERING
    matches_permequiv = ranked == PERMUTATION_EQUIVALENT
    n_outside_interval = sum(1 for s in SUBSTRATES if not results[s]["inside_blind_interval"])

    # Per spec §3:
    # FAIL: ROK at #4 AND δ_ROK < 0
    # PASS: rok_top AND (matches_predicted OR matches_permequiv) AND n_outside_interval <= 1
    # INCONCLUSIVE: everything else
    if rok_bottom and (not np.isnan(rok_delta)) and rok_delta < 0:
        verdict = "FAIL"
        verdict_reason = (
            f"ROK at bottom of δ ordering (observed: {ranked[-1]}) AND δ_ROK={rok_delta:+.4f} < 0; "
            "path (b) measurement-quality falsified at cross-substrate level under M-25-1."
        )
    elif rok_top and (matches_predicted or matches_permequiv) and n_outside_interval <= 1:
        verdict = "PASS"
        verdict_reason = (
            "Predicted ordering ROK > JPN > EU > US matched"
            if matches_predicted
            else "Permutation-equivalent ordering ROK > JPN > US > EU matched"
        )
        verdict_reason += f"; {n_outside_interval} substrate(s) outside blind intervals (≤1 allowed)."
    else:
        verdict = "INCONCLUSIVE"
        rok_pos = ranked.index("ROK") + 1
        reasons = []
        if not rok_top:
            reasons.append(f"ROK at rank #{rok_pos} (not #1)")
        elif not (matches_predicted or matches_permequiv):
            reasons.append(f"ordering {ranked} differs from predicted by >1 reversal")
        if n_outside_interval >= 2:
            reasons.append(f"{n_outside_interval} substrates outside blind intervals (>1)")
        verdict_reason = "; ".join(reasons) if reasons else "no specific INCONCLUSIVE condition matched but PASS gate failed"

    out = {
        "computed_at": computed_at,
        "input_data": str(DATA.relative_to(HERE.parent.parent)),
        "m_25_1_amendment_applied": M_25_1_AMENDMENT_APPLIED,
        "amendment_note": (
            f"Day-25 cron-D protocol amendment M-25-1 retires {ROK_TICKER_RETIRED_UNDER_M_25_1} as ROK "
            f"textual-axis ticker; H26.1 substitutes {SUBSTRATES['ROK']} into the ROK slot for the "
            "Day-24 H24.1 4-substrate sweep, mirroring all other Day-24 method parameters exactly."
        ),
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
        "h26_1": {
            "predicted_ordering": PREDICTED_ORDERING,
            "permutation_equivalent": PERMUTATION_EQUIVALENT,
            "observed_ordering": ranked,
            "rok_at_top": rok_top,
            "rok_at_bottom": rok_bottom,
            "rok_delta": rok_delta,
            "n_outside_blind_interval": n_outside_interval,
            "verdict": verdict,
            "verdict_reason": verdict_reason,
        },
        "comparison_to_day_24": {
            "day_24_etf_level_verdict": "INCONCLUSIVE",
            "day_24_etf_level_observed_ordering": ["EU", "JPN", "US", "ROK"],
            "day_24_etf_level_rok_delta": -0.0077,
            "day_25_firm_level_h25_1_rok_delta_005930ks_x_tsm": 0.0546,
            "note": (
                "H26.1 verdict is the firm-level cross-substrate sweep under M-25-1; "
                "compare against Day-24 ETF-level result to assess whether the M-25-1 "
                "amendment rehabilitates the directional H24.1 prediction."
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

    OUT.write_text(json.dumps(out, indent=2, default=_np_default))
    print(
        json.dumps(
            {"verdict": verdict, "ranked": ranked, "rok_delta": rok_delta, "output": str(OUT.name)},
            indent=2,
            default=_np_default,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
