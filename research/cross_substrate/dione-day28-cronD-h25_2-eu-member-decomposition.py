"""Day-28 cron-D — H25.2 EU member-state decomposition (q-day24-5 path test).

Executed by Dione 2026-06-12 cron-D (first post-migration fire on Uranus-2).
Pre-registered at Day-25 cron-B:
research/cross_substrate/dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md

Execution-fire deferral: pre-registered for Day-28 cron-A (2026-06-07 06:00
CEST per Day-27 §3.1); the Uranus-1→Uranus-2 migration freeze pushed execution
to Day-28 cron-D 2026-06-12 17:00 CEST. The data window ends 2026-05-29 as
pre-registered — no new data enters; §2.1 intervals, §2.2 verdict rule, and
§3 method are applied unmodified.

Method (per pre-registration §3.3, identical to Day-24 cron-C + H25.1 + H26.1):
  - Daily adjusted closes from dione-day28-cronD-data/tickers_wide.csv
    (EWG, EWQ, EWN fresh-pulled; TSM = locked Day-24 cron-B anchor).
  - Log returns: log(P_t / P_{t-1}).
  - Pearson rolling-60 correlation between each member ETF and TSM.
  - Stress windows (±20 td around each anchor; union = stress; rest = baseline):
      DUV anchor: 2023-01-27
      LAI anchor: 2024-01-13
      PRC anchor: 2025-10-10
  - Stress δ = median(rolling-60 ρ | stress) − median(rolling-60 ρ | baseline)
    per pair, pooled across the three windows (Day-24 cron-C convention).
  - Mean as secondary statistic; verdict assigned via median.

Pre-committed δ intervals (§2.1):
  EWG × TSM: [+0.02, +0.07]
  EWQ × TSM: [ 0.00, +0.06]
  EWN × TSM: [+0.08, +0.18]

Combined-pattern verdict rule (§2.2, THE falsification rule):
  path_a   ACTIVE_AGGREGATE_AMPLIFIED corroborated:
           all three δ > +0.05 AND mean(δ) ≥ +0.0796
  path_b_refined  ASML-channel-dominance corroborated:
           EWN δ > +0.10 AND EWG δ < +0.03 AND EWQ δ < +0.03
  path_b   EZU constituent-weighting artifact corroborated:
           only 1-2 of three δ > +0.05 OR all three ≤ +0.05 OR mean < +0.0796
  Ambiguity default: path_b.

Output: dione-day28-cronD-h25_2-output.json
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE / "dione-day28-cronD-data" / "tickers_wide.csv"
OUT = HERE / "dione-day28-cronD-h25_2-output.json"

PAIRS = {"EWG": "Germany", "EWQ": "France", "EWN": "Netherlands"}
ANCHOR = "TSM"
EZU_REFERENCE_DELTA = 0.0796  # Day-24 cron-C H24.1 EU/EZU pooled δ

STRESS_ANCHORS = {
    "DUV_2023": "2023-01-27",
    "LAI_2024": "2024-01-13",
    "PRC_2025": "2025-10-10",
}
STRESS_HALFWIDTH_TDAYS = 20
ROLLING_WIN = 60

PRECOMMITTED_INTERVALS = {
    "EWG": (0.02, 0.07),
    "EWQ": (0.00, 0.06),
    "EWN": (0.08, 0.18),
}


def stress_mask(idx: pd.DatetimeIndex) -> pd.Series:
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
            "n_td": int(hi - lo),
        }

    results = {}
    for ticker, member in PAIRS.items():
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
        stress_mean = float(roll_stress.mean()) if len(roll_stress) else float("nan")
        baseline_mean = float(roll_baseline.mean()) if len(roll_baseline) else float("nan")
        delta_mean_stat = (
            stress_mean - baseline_mean
            if not (np.isnan(stress_mean) or np.isnan(baseline_mean))
            else float("nan")
        )

        # Per-anchor informational breakdown (secondary; not verdict-bearing)
        per_anchor = {}
        for label in STRESS_ANCHORS:
            am = stress_anchor_meta[label]
            if not am.get("in_data"):
                per_anchor[label] = None
                continue
            w = roll.loc[am["window_first"]: am["window_last"]]
            per_anchor[label] = (
                float(w.median() - baseline_median) if len(w) else None
            )

        lo_int, hi_int = PRECOMMITTED_INTERVALS[ticker]
        results[ticker] = {
            "member_state": member,
            "n_pair_obs": int(pair.shape[0]),
            "full_window_pearson": full_pearson,
            "rolling_window_td": ROLLING_WIN,
            "rolling_n_stress": int(len(roll_stress)),
            "rolling_n_baseline": int(len(roll_baseline)),
            "stress_median_rolling_corr": stress_median,
            "baseline_median_rolling_corr": baseline_median,
            "delta": delta,
            "delta_mean_secondary": delta_mean_stat,
            "median_mean_disagreement_flag": (
                bool(np.sign(delta) != np.sign(delta_mean_stat))
                if not (np.isnan(delta) or np.isnan(delta_mean_stat)) else None
            ),
            "per_anchor_delta_informational": per_anchor,
            "pre_committed_interval": [lo_int, hi_int],
            "inside_pre_committed_interval": (
                (not np.isnan(delta)) and (lo_int <= delta <= hi_int)
            ),
        }

    deltas = {t: results[t]["delta"] for t in PAIRS}
    mean_delta = float(np.mean(list(deltas.values())))
    n_above_005 = sum(1 for d in deltas.values() if d > 0.05)

    # §2.2 combined-pattern verdict rule, evaluated most-specific-first.
    pattern_a = (n_above_005 == 3) and (mean_delta >= EZU_REFERENCE_DELTA)
    pattern_b_refined = (
        deltas["EWN"] > 0.10 and deltas["EWG"] < 0.03 and deltas["EWQ"] < 0.03
    )
    anomalous_edge = any(d < 0 for d in deltas.values()) and any(d > 0 for d in deltas.values())

    if pattern_b_refined:
        verdict_path = "b_refined_asml_channel_dominance"
        pattern_match = "EWN δ > +0.10 AND EWG δ < +0.03 AND EWQ δ < +0.03"
        action = (
            "Measurement-protocol amendment: EU textual-axis = ASML.AS × TSM (firm-level). "
            "Document ASML-dominance argument in v1.2 EU classification rationale; no schema change. "
            "Pre-register H25.3 ASML.AS × TSM firm-level test (Amsterdam calendar caveat)."
        )
    elif pattern_a:
        verdict_path = "a_active_aggregate_amplified"
        pattern_match = "all three δ > +0.05 AND mean(δ) ≥ +0.0796"
        action = (
            "File v1.2.1 schema revision adding ACTIVE_AGGREGATE_AMPLIFIED sub-state; "
            "re-classify EU. Affects q-day24-3 directly; reading-α corroborated."
        )
    else:
        verdict_path = "b_ezu_constituent_weighting_artifact"
        pattern_match = (
            f"{n_above_005} of three δ > +0.05 (need 3) "
            f"{'AND' if mean_delta < EZU_REFERENCE_DELTA else 'BUT'} "
            f"mean(δ)={mean_delta:+.4f} {'<' if mean_delta < EZU_REFERENCE_DELTA else '≥'} +0.0796"
        )
        action = (
            "Measurement-protocol amendment: EU textual-axis = ASML.AS × TSM or sector-decomposed "
            "instrument, not EZU. v1.2 schema unchanged; reading-α EU basis undermined."
        )

    out = {
        "test": "H25.2",
        "computed_at": computed_at,
        "execution_fire": "Day-28 cron-D 2026-06-12 17:00 CEST (Uranus-2; deferred from pre-registered Day-28 cron-A 2026-06-07 by migration freeze; window/method/intervals unmodified)",
        "pre_registration": "research/cross_substrate/dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md",
        "data": str(DATA.relative_to(HERE)),
        "full_window": {
            "first_date": log_ret.index.min().strftime("%Y-%m-%d"),
            "last_date": log_ret.index.max().strftime("%Y-%m-%d"),
            "n_returns": int(log_ret.shape[0]),
        },
        "stress_anchors": stress_anchor_meta,
        "n_stress_td": int(mask.sum()),
        "n_baseline_td": int((~mask).sum()),
        "pairs": results,
        "combined": {
            "deltas": deltas,
            "mean_delta": mean_delta,
            "ezu_reference_delta_h24_1": EZU_REFERENCE_DELTA,
            "n_pairs_above_+0.05": n_above_005,
            "anomalous_mixed_sign_edge_case": anomalous_edge,
        },
        "combined_verdict_path": verdict_path,
        "pattern_match": pattern_match,
        "pre_registered_action": action,
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
