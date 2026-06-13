"""Day-29 cron-B — H25.3 ASML.AS × TSM firm-level channel test.

Executed by Dione 2026-06-13 cron-B (11:00 CEST / 09:00 UTC) on Uranus-2.
Pre-registration: research/cross_substrate/dione-day29-cronA-h25_3-asml-firm-level-pre-registration-2026-06-13.md
                  (commit 29f8c8e on silicon-strait/trunk).

Resolves the M-28-1 instrument-amendment gate (Day-28 §5) and folds the
q-day28-1 default (ASML.AS alone first; three-firm panel = H25.4 only on
INCONCLUSIVE or single-instrument fragility).

Method (pre-registration §3.3, identical to Day-24 cron-C / H25.1 / H25.2):
  - Daily adjusted closes from the Day-29 cron-B pull.
  - Log returns: log(P_t / P_{t-1}).
  - Pearson rolling-60 correlation between r_ASML.AS and r_TSM.
  - Stress windows (±20 td around each anchor; union = stress; rest = baseline):
      DUV anchor: 2023-01-27
      LAI anchor: 2024-01-13
      PRC anchor: 2025-10-10
  - Stress δ = median(rolling-60 ρ | stress) − median(rolling-60 ρ | baseline).
  - PRIMARY endpoint = pooled δ across the three anchors (median convention).
    Per-anchor legs (δ_DUV, δ_LAI, δ_PRC) reported as the structure §2.2 inspects.
  - Mean reported as a secondary statistic; verdict assigned on the median.

Amsterdam calendar-asymmetry handling (pre-registration §3.4):
  - VERDICT assigned on the GLOBAL NYSE-mask δ (tickers_wide_global.csv,
    no ffill — mirrors Day-26 H26.1 cross-substrate frame).
  - The pair-isolated δ (tickers_wide_isolated.csv, ffill limit=1 — mirrors
    Day-25 H25.1) is the reconciliation reference only. The global-vs-isolated
    offset is reported as a method-internal constant (Day-26 §3.4: −0.0031 for ROK).

Pre-committed blind intervals (§2.1):
  H_sc supply-chain channel : pooled δ ∈ [+0.10, +0.25]
  H_id idiosyncratic/risk   : pooled δ ∈ [−0.15, +0.05]
  dead band (INCONCLUSIVE)  : pooled δ ∈ (+0.05, +0.10)

Pre-committed verdict rule (§2.2, THE falsification rule), on the global-mask
tuple (δ_pooled, δ_DUV, δ_LAI, δ_PRC):
  PASS-sc  if δ_pooled ≥ +0.10 AND ≥2/3 anchor legs > 0 AND δ_PRC ≥ 0
  PASS-id  if δ_pooled ≤ +0.05 AND (δ_PRC < 0 OR ≥1 anchor leg < −0.05)
  INCONCLUSIVE if δ_pooled ∈ (+0.05, +0.10) (dead band) OR sign-structure mixed
               (δ_pooled ≥ +0.10 but δ_PRC < 0)
  Tie-break / default on any residual ambiguity = PASS-id (Day-28 EWN prior).

Output: dione-day29-cronB-h25_3-output.json
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA_DIR = HERE / "dione-day29-cronB-data"
DATA_GLOBAL = DATA_DIR / "tickers_wide_global.csv"
DATA_ISOLATED = DATA_DIR / "tickers_wide_isolated.csv"
OUT = HERE / "dione-day29-cronB-h25_3-output.json"

TICKER = "ASML.AS"
ANCHOR = "TSM"

STRESS_ANCHORS = {
    "DUV_2023": "2023-01-27",
    "LAI_2024": "2024-01-13",
    "PRC_2025": "2025-10-10",
}
STRESS_HALFWIDTH_TDAYS = 20
ROLLING_WIN = 60

# §2.1 pre-committed blind intervals (pooled δ).
INTERVAL_SC = (0.10, 0.25)
INTERVAL_ID = (-0.15, 0.05)
DEAD_BAND = (0.05, 0.10)  # exclusive interior → INCONCLUSIVE


def stress_mask(idx: pd.DatetimeIndex) -> pd.Series:
    mask = pd.Series(False, index=idx)
    for _label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        pos = idx.searchsorted(anchor)
        if pos == len(idx):
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(idx), pos + STRESS_HALFWIDTH_TDAYS + 1)
        mask.iloc[lo:hi] = True
    return mask


def compute_pair(wide: pd.DataFrame) -> dict:
    """Run the full rolling-60 δ pipeline on one join convention.

    Returns pooled δ (median + mean), per-anchor legs, and the n-counts.
    Identical pipeline to Day-24 cron-C / H25.1 / H25.2: log-returns on the
    full grid, pair.dropna(), rolling-60, median(stress)−median(baseline).
    """
    n_before_drop = int(len(wide))
    log_ret = np.log(wide / wide.shift(1))
    pair = log_ret[[TICKER, ANCHOR]].dropna()
    n_pair_obs = int(len(pair))
    n_dropped = n_before_drop - n_pair_obs - 1  # -1 for leading shift(1) NaN row

    full_pearson = float(pair[TICKER].corr(pair[ANCHOR]))

    mask = stress_mask(pair.index)
    stress_idx = pair.index[mask]
    baseline_idx = pair.index[~mask]

    anchor_meta = {}
    for label, anchor_date in STRESS_ANCHORS.items():
        anchor = pd.Timestamp(anchor_date)
        pos = pair.index.searchsorted(anchor)
        if pos == len(pair.index):
            anchor_meta[label] = {"anchor": anchor_date, "in_data": False}
            continue
        lo = max(0, pos - STRESS_HALFWIDTH_TDAYS)
        hi = min(len(pair.index), pos + STRESS_HALFWIDTH_TDAYS + 1)
        anchor_meta[label] = {
            "anchor": anchor_date,
            "in_data": True,
            "window_first": pair.index[lo].strftime("%Y-%m-%d"),
            "window_last": pair.index[hi - 1].strftime("%Y-%m-%d"),
            "n_td": int(hi - lo),
        }

    roll = pair[TICKER].rolling(ROLLING_WIN).corr(pair[ANCHOR]).dropna()
    roll_stress = roll.loc[roll.index.intersection(stress_idx)]
    roll_baseline = roll.loc[roll.index.intersection(baseline_idx)]

    stress_median = float(roll_stress.median()) if len(roll_stress) else float("nan")
    baseline_median = float(roll_baseline.median()) if len(roll_baseline) else float("nan")
    pooled_delta = (
        stress_median - baseline_median
        if not (np.isnan(stress_median) or np.isnan(baseline_median))
        else float("nan")
    )
    stress_mean = float(roll_stress.mean()) if len(roll_stress) else float("nan")
    baseline_mean = float(roll_baseline.mean()) if len(roll_baseline) else float("nan")
    pooled_delta_mean = (
        stress_mean - baseline_mean
        if not (np.isnan(stress_mean) or np.isnan(baseline_mean))
        else float("nan")
    )

    # Per-anchor legs vs the SAME pooled baseline median (Day-24/H25.2 convention).
    per_anchor = {}
    for label in STRESS_ANCHORS:
        am = anchor_meta[label]
        if not am.get("in_data"):
            per_anchor[label] = None
            continue
        w = roll.loc[am["window_first"]: am["window_last"]]
        per_anchor[label] = (
            float(w.median() - baseline_median) if len(w) else None
        )

    return {
        "n_pair_obs_after_dropna": n_pair_obs,
        "n_dropped_asymmetric_calendar": n_dropped,
        "full_window_first": pair.index.min().strftime("%Y-%m-%d"),
        "full_window_last": pair.index.max().strftime("%Y-%m-%d"),
        "full_window_pearson": full_pearson,
        "stress_anchors": anchor_meta,
        "n_stress_td": int(len(stress_idx)),
        "n_baseline_td": int(len(baseline_idx)),
        "rolling_n_stress": int(len(roll_stress)),
        "rolling_n_baseline": int(len(roll_baseline)),
        "stress_median_rolling_corr": stress_median,
        "baseline_median_rolling_corr": baseline_median,
        "pooled_delta": pooled_delta,
        "pooled_delta_mean_secondary": pooled_delta_mean,
        "per_anchor_delta": per_anchor,
    }


def classify_interval(delta: float) -> str:
    if np.isnan(delta):
        return "nan_undefined"
    if INTERVAL_SC[0] <= delta <= INTERVAL_SC[1]:
        return "H_sc_interval"
    if INTERVAL_ID[0] <= delta <= INTERVAL_ID[1]:
        return "H_id_interval"
    if DEAD_BAND[0] < delta < DEAD_BAND[1]:
        return "dead_band"
    return "outside_all_blind_intervals"


def assign_verdict(g: dict) -> dict:
    """Apply the §2.2 pre-committed verdict rule to the GLOBAL-mask tuple."""
    d_pooled = g["pooled_delta"]
    legs = g["per_anchor_delta"]
    d_prc = legs.get("PRC_2025")
    leg_vals = [v for v in legs.values() if v is not None]
    n_pos = sum(1 for v in leg_vals if v > 0)
    n_below_neg005 = sum(1 for v in leg_vals if v < -0.05)

    if np.isnan(d_pooled) or d_prc is None:
        return {
            "verdict": "INDETERMINATE",
            "verdict_rule_branch": "nan_or_missing_prc_leg",
            "reason": "pooled δ NaN or PRC anchor leg absent; cannot evaluate §2.2 rule",
        }

    pass_sc = (d_pooled >= 0.10) and (n_pos >= 2) and (d_prc >= 0)
    pass_id = (d_pooled <= 0.05) and ((d_prc < 0) or (n_below_neg005 >= 1))

    if pass_sc:
        return {
            "verdict": "PASS-sc",
            "verdict_rule_branch": "supply_chain_channel_confirmed",
            "reason": (
                f"δ_pooled={d_pooled:+.4f} ≥ +0.10 AND {n_pos}/3 anchor legs > 0 (≥2) "
                f"AND δ_PRC={d_prc:+.4f} ≥ 0."
            ),
            "consequence": (
                "M-28-1 ACTIVATES: EU textual axis = ASML.AS × TSM. Reading-α revisitation "
                "warranted (Day-28 §4 sole gate met); file v1.2→v1.3 ACTIVE_AGGREGATE_AMPLIFIED "
                "pre-registration. Schema stays v1.2 until that separate cycle."
            ),
        }
    if pass_id:
        return {
            "verdict": "PASS-id",
            "verdict_rule_branch": "idiosyncratic_hedge_risk_channel_confirmed",
            "reason": (
                f"δ_pooled={d_pooled:+.4f} ≤ +0.05 AND "
                f"(δ_PRC={d_prc:+.4f} < 0: {d_prc < 0}) OR "
                f"({n_below_neg005} anchor leg(s) < −0.05: {n_below_neg005 >= 1})."
            ),
            "consequence": (
                "M-28-1 CONCLUDES: EU textual axis measures risk-channel breadth, not "
                "supply-chain depth, at every instrument level (EZU, EWN/EWG/EWQ, ASML.AS). "
                "EU textual-axis δ retired from supply-chain interpretation; reading-α stays "
                "declined permanently; reading-β sole live methodology track."
            ),
        }

    # Neither clean branch fired — resolve per §2.2 row 3 + pre-committed default.
    in_dead_band = DEAD_BAND[0] < d_pooled < DEAD_BAND[1]
    mixed_sign = (d_pooled >= 0.10) and (d_prc < 0)
    if in_dead_band:
        return {
            "verdict": "INCONCLUSIVE",
            "verdict_rule_branch": "dead_band",
            "reason": f"δ_pooled={d_pooled:+.4f} ∈ (+0.05, +0.10) dead band.",
            "consequence": "Escalate to H25.4 three-firm EU panel (ASML.AS + STM + IFX.DE) per q-day28-1.",
        }
    if mixed_sign:
        return {
            "verdict": "INCONCLUSIVE",
            "verdict_rule_branch": "mixed_sign_structure",
            "reason": f"δ_pooled={d_pooled:+.4f} ≥ +0.10 but δ_PRC={d_prc:+.4f} < 0 (sign-structure mixed).",
            "consequence": "Escalate to H25.4 three-firm EU panel per q-day28-1.",
        }
    # Residual ambiguity (e.g. δ_pooled ≤ +0.05 but δ_PRC ≥ 0 and no leg < −0.05).
    return {
        "verdict": "PASS-id",
        "verdict_rule_branch": "tie_break_default_pass_id",
        "reason": (
            f"δ_pooled={d_pooled:+.4f}; neither PASS-sc nor the PASS-id sufficiency clause "
            f"fired and not in dead band / mixed-sign — pre-committed tie-break default "
            f"(§2.2: burden of proof for reading-α resurrection rests on a CLEAN PASS-sc)."
        ),
        "consequence": (
            "Treated as PASS-id by the pre-committed default: EU textual axis not rehabilitated "
            "as a supply-chain instrument; reading-α stays declined; reading-β sole live track."
        ),
    }


def main() -> int:
    computed_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    for p in (DATA_GLOBAL, DATA_ISOLATED):
        if not p.exists():
            print(f"DATA MISSING: {p}", file=sys.stderr)
            return 2

    wide_global = pd.read_csv(DATA_GLOBAL, index_col="date", parse_dates=["date"]).sort_index()
    wide_isolated = pd.read_csv(DATA_ISOLATED, index_col="date", parse_dates=["date"]).sort_index()

    g = compute_pair(wide_global)      # verdict-bearing
    iso = compute_pair(wide_isolated)  # reconciliation reference

    global_delta = g["pooled_delta"]
    isolated_delta = iso["pooled_delta"]
    offset = (
        global_delta - isolated_delta
        if not (np.isnan(global_delta) or np.isnan(isolated_delta))
        else float("nan")
    )

    verdict_block = assign_verdict(g)

    out = {
        "test": "H25.3",
        "computed_at": computed_at,
        "execution_fire": "Day-29 cron-B 2026-06-13 11:00 CEST (Uranus-2)",
        "pre_registration": "research/cross_substrate/dione-day29-cronA-h25_3-asml-firm-level-pre-registration-2026-06-13.md",
        "pre_registration_commit": "29f8c8e",
        "instrument": f"{TICKER} × {ANCHOR} (firm-level; q-day28-1 default — ASML.AS alone)",
        "method": {
            "log_returns": "log(P_t / P_{t-1})",
            "rolling_window_td": ROLLING_WIN,
            "stress_half_width_td": STRESS_HALFWIDTH_TDAYS,
            "delta_primary": "median(rolling_corr | stress) - median(rolling_corr | baseline), pooled across 3 anchors",
            "delta_secondary": "mean(rolling_corr | stress) - mean(rolling_corr | baseline)",
            "verdict_uses": "median (Day-24 calibration convention)",
            "verdict_assigned_on": "global NYSE-mask δ (§3.4)",
        },
        "blind_intervals": {
            "H_sc_supply_chain": list(INTERVAL_SC),
            "H_id_idiosyncratic_hedge": list(INTERVAL_ID),
            "dead_band_inconclusive_exclusive": list(DEAD_BAND),
        },
        "global_mask": g,
        "pair_isolated_mask": iso,
        "mask_reconciliation": {
            "global_delta": global_delta,
            "pair_isolated_delta": isolated_delta,
            "offset_global_minus_isolated": offset,
            "rok_precedent_offset_day26": -0.0031,
            "note": (
                "Global mask (no ffill, NYSE calendar) is verdict-bearing; pair-isolated "
                "(ffill limit=1) reproduces the H25.1-style treatment. Offset reported, not "
                "assumed (Day-26 §3.4 method). Nisaba audit reproduces this reconciliation."
            ),
        },
        "pooled_delta_interval_classification": {
            "global": classify_interval(global_delta),
            "pair_isolated": classify_interval(isolated_delta),
        },
        "verdict_block": verdict_block,
        "verdict": verdict_block["verdict"],
        "verdict_rule_branch": verdict_block["verdict_rule_branch"],
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
        "verdict": out["verdict"],
        "verdict_rule_branch": out["verdict_rule_branch"],
        "global_pooled_delta": global_delta,
        "pair_isolated_pooled_delta": isolated_delta,
        "offset": offset,
        "per_anchor_global": g["per_anchor_delta"],
        "output": str(OUT.name),
    }, indent=2, default=_np_default, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
