#!/usr/bin/env python3
"""
Day-22 cron-D: H21.1a/b empirical test on India substrate.

Pre-registration anchors:
  - cron-B India primaries §4.3:  dccb673  blind prediction δ ∈ [0.05, 0.10]
  - cron-C matrix-rows-6-9 §4:    d8ce267  ticker-final-lock
  - Day-21 §3.5 H21.1a/b filed:   fe966b8  refined hypothesis pair

Refined hypothesis pair (forward-tested today):
  H21.1a (alternative): coupling-positive operational-engagement substrate shows
     elevated correlation with TSM under stress vs baseline. Quantitatively
     δ > 0.10 → textual-vs-operational distinction COLLAPSES empirically
     (operational coupling alone produces same correlation lift as textual
     coupling found Day-21 for ROK).
  H21.1b (alternative): coupling-property is empirically NULL despite operational
     engagement. Quantitatively |δ| < 0.05.
  Pre-registered blind interval (cron-B §4.3, cron-C §4.1):
     δ ∈ [0.05, 0.10] → operational coupling produces non-zero but sub-textual
     correlation lift; OPERATIONAL_POSITIVE_INDUSTRIAL classification holds.

Method (matching Day-21 cron-C exactly except for:
  - 6 stress events instead of 5 (4 standing + Galwan-2020 + Tawang-2022)
  - 3 India pairs instead of cross-substrate {ROK, AUS, NVDA}
  - within-pair temporal δ (stress-window vs baseline-window) instead of
    cross-pair ordering — the question changes from "is ROK higher than BHP"
    to "does this India pair lift during stress windows"):

  - Pearson rolling-60 correlation on adjusted-close log returns
  - ±20 trading-day window around each stress event
  - Per pair report median correlation across:
      * stress windows = union of ±20-td windows around the 6 stress events
      * baseline windows = all other rolling-60 observations (after warmup)
  - δ = median(stress) − median(baseline)
  - Per-event δ also reported (each event's ±20 vs all-other-baseline)

Three-pair ladder:
  TATAELXSI.NS ↔ TSM   firm-specific (Tata-PSMC direct downstream)
  ^CNXIT       ↔ TSM   sector-specific (NIFTY IT broader Indian IT)
  INDA         ↔ TSM   country-specific (MSCI India broad ETF control)

Ladder reading:
  δ(TATAELXSI) > δ(CNXIT) > δ(INDA)  → firm-specific signal
  δ(TATAELXSI) ≈ δ(CNXIT) > δ(INDA)  → sector-specific signal
  δ(TATAELXSI) ≈ δ(CNXIT) ≈ δ(INDA)  → country-wide signal (Tata-PSMC null)
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

TICKERS = ["TSM", "TATAELXSI.NS", "^CNXIT", "INDA"]
DOWNLOAD_START = "2020-04-01"  # backs up to cover Galwan-2020 minus rolling-60 warmup
DOWNLOAD_END = "2026-05-31"
ROLLING_WINDOW = 60
EVENT_WINDOW_TD = 20

STRESS_EVENTS = [
    {"id": "Galwan_2020", "date": "2020-06-15", "label": "Galwan Valley LAC clash"},
    {"id": "PEL_2022", "date": "2022-08-02", "label": "Pelosi Taipei visit"},
    {"id": "Tawang_2022", "date": "2022-12-09", "label": "Tawang LAC scuffle"},
    {"id": "DUV_2023", "date": "2023-09-04", "label": "Dutch DUV ratchet"},
    {"id": "LAI_2024", "date": "2024-05-20", "label": "Lai Ching-te inauguration"},
    {"id": "PRC_2025a", "date": "2025-10-10", "label": "PRC CMOT port-fee announcement"},
    {"id": "PRC_2025i", "date": "2025-10-14", "label": "PRC port-fee implementation"},
]

PAIRS = [
    {"id": "IND_TATAELXSI", "left": "TATAELXSI.NS", "right": "TSM",
     "class": "firm_specific_tata_psmc_downstream"},
    {"id": "IND_CNXIT", "left": "^CNXIT", "right": "TSM",
     "class": "sector_specific_nifty_it"},
    {"id": "IND_INDA", "left": "INDA", "right": "TSM",
     "class": "country_specific_msci_india_broad"},
]


@dataclass
class WindowResult:
    pair_id: str
    event_id: str
    event_date: str
    window_start: str
    window_end: str
    n_obs_in_window: int
    median_corr: float
    min_corr: float
    max_corr: float
    iqr_corr: float


def load_prices() -> pd.DataFrame:
    raw = yf.download(
        TICKERS,
        start=DOWNLOAD_START,
        end=DOWNLOAD_END,
        auto_adjust=True,
        progress=False,
        group_by="ticker",
        threads=True,
    )
    closes = pd.DataFrame(
        {t: raw[t]["Close"] for t in TICKERS if t in raw.columns.get_level_values(0)}
    )
    closes.index = pd.to_datetime(closes.index)
    return closes.sort_index()


def log_returns(closes: pd.DataFrame) -> pd.DataFrame:
    return np.log(closes).diff()


def rolling_pair_corr(rets: pd.DataFrame, left: str, right: str,
                      window: int) -> pd.Series:
    aligned = rets[[left, right]].dropna(how="any")
    return aligned[left].rolling(window).corr(aligned[right])


def window_around(corr: pd.Series, event_date: str, td: int) -> pd.Series:
    event_ts = pd.Timestamp(event_date)
    valid_idx = corr.dropna().index
    pos = valid_idx.searchsorted(event_ts)
    if pos >= len(valid_idx):
        return pd.Series(dtype=float)
    lo = max(0, pos - td)
    hi = min(len(valid_idx), pos + td + 1)
    window_idx = valid_idx[lo:hi]
    return corr.loc[window_idx]


def summarise_window(corr_window: pd.Series, pair: dict, ev: dict
                     ) -> WindowResult | None:
    if corr_window.empty:
        return None
    return WindowResult(
        pair_id=pair["id"],
        event_id=ev["id"],
        event_date=ev["date"],
        window_start=str(corr_window.index[0].date()),
        window_end=str(corr_window.index[-1].date()),
        n_obs_in_window=int(len(corr_window)),
        median_corr=float(corr_window.median()),
        min_corr=float(corr_window.min()),
        max_corr=float(corr_window.max()),
        iqr_corr=float(corr_window.quantile(0.75) - corr_window.quantile(0.25)),
    )


def stress_baseline_split(corr: pd.Series, events: list[dict], td: int
                          ) -> dict:
    """Partition a rolling-60 correlation series into stress vs baseline
    windows. Stress = union of ±td around each event; baseline = the rest.
    Returns medians + counts + bounds.
    """
    valid = corr.dropna()
    if valid.empty:
        return {"stress_median": None, "baseline_median": None,
                "delta": None, "n_stress": 0, "n_baseline": 0}
    valid_idx = valid.index
    stress_mask = pd.Series(False, index=valid_idx)
    for ev in events:
        event_ts = pd.Timestamp(ev["date"])
        pos = valid_idx.searchsorted(event_ts)
        if pos >= len(valid_idx):
            continue
        lo = max(0, pos - td)
        hi = min(len(valid_idx), pos + td + 1)
        stress_mask.iloc[lo:hi] = True
    stress_vals = valid[stress_mask]
    baseline_vals = valid[~stress_mask]
    if stress_vals.empty or baseline_vals.empty:
        return {"stress_median": None, "baseline_median": None,
                "delta": None,
                "n_stress": int(len(stress_vals)),
                "n_baseline": int(len(baseline_vals))}
    sm = float(stress_vals.median())
    bm = float(baseline_vals.median())
    return {
        "stress_median": sm,
        "baseline_median": bm,
        "delta": sm - bm,
        "n_stress": int(len(stress_vals)),
        "n_baseline": int(len(baseline_vals)),
        "stress_q1": float(stress_vals.quantile(0.25)),
        "stress_q3": float(stress_vals.quantile(0.75)),
        "baseline_q1": float(baseline_vals.quantile(0.25)),
        "baseline_q3": float(baseline_vals.quantile(0.75)),
    }


def classify_delta(delta: float | None) -> str:
    if delta is None:
        return "MISSING_DATA"
    if delta > 0.10:
        return "H21_1a_alternative_textual_vs_operational_distinction_collapses"
    if delta >= 0.05:
        return "blind_pre_registered_in_interval"
    if delta > -0.05:
        return "H21_1b_alternative_coupling_property_empirically_null"
    return "H21_1c_residual_anti_correlation"


def run() -> dict:
    closes = load_prices()
    rets = log_returns(closes)

    pair_corrs = {
        p["id"]: rolling_pair_corr(rets, p["left"], p["right"], ROLLING_WINDOW)
        for p in PAIRS
    }

    per_event_results = {}
    per_pair_aggregate = {}

    # Per-event ±20-td window summaries (Day-21-style)
    for ev in STRESS_EVENTS:
        per_event_results[ev["id"]] = {}
        for p in PAIRS:
            cw = window_around(pair_corrs[p["id"]], ev["date"], EVENT_WINDOW_TD)
            summary = summarise_window(cw, p, ev)
            if summary is not None:
                per_event_results[ev["id"]][p["id"]] = asdict(summary)

    # Per-pair stress-vs-baseline aggregate (Day-22 within-pair temporal δ)
    for p in PAIRS:
        aggregate = stress_baseline_split(pair_corrs[p["id"]],
                                          STRESS_EVENTS,
                                          EVENT_WINDOW_TD)
        aggregate["pair_id"] = p["id"]
        aggregate["class"] = p["class"]
        aggregate["left"] = p["left"]
        aggregate["right"] = p["right"]
        aggregate["delta_classification"] = classify_delta(aggregate.get("delta"))
        per_pair_aggregate[p["id"]] = aggregate

    # Ladder reading
    deltas = {pid: agg["delta"] for pid, agg in per_pair_aggregate.items()}
    ladder = sorted(
        [(pid, d) for pid, d in deltas.items() if d is not None],
        key=lambda x: x[1], reverse=True,
    )
    if len(ladder) == 3:
        d_tata = deltas.get("IND_TATAELXSI")
        d_cnxit = deltas.get("IND_CNXIT")
        d_inda = deltas.get("IND_INDA")
        tata_minus_cnxit = (d_tata - d_cnxit) if (d_tata is not None and d_cnxit is not None) else None
        cnxit_minus_inda = (d_cnxit - d_inda) if (d_cnxit is not None and d_inda is not None) else None
        tata_minus_inda = (d_tata - d_inda) if (d_tata is not None and d_inda is not None) else None
        if tata_minus_cnxit is not None and cnxit_minus_inda is not None:
            if tata_minus_cnxit > 0.02 and cnxit_minus_inda > 0.02:
                ladder_reading = "firm_specific_signal_tata_psmc_specific"
            elif abs(tata_minus_cnxit) <= 0.02 and cnxit_minus_inda > 0.02:
                ladder_reading = "sector_specific_signal_it_specific"
            elif abs(tata_minus_inda) <= 0.02:
                ladder_reading = "country_wide_signal_tata_psmc_null"
            else:
                ladder_reading = "mixed_signal_inconclusive_ladder"
        else:
            ladder_reading = "incomplete_ladder"
        gaps = {
            "tata_minus_cnxit": tata_minus_cnxit,
            "cnxit_minus_inda": cnxit_minus_inda,
            "tata_minus_inda": tata_minus_inda,
        }
    else:
        ladder_reading = "incomplete_ladder"
        gaps = {}

    # H21.1a/b primary verdict on the primary (TATAELXSI) pair
    primary = per_pair_aggregate.get("IND_TATAELXSI", {})
    primary_delta = primary.get("delta")
    primary_classification = primary.get("delta_classification", "MISSING_DATA")

    return {
        "method": {
            "rolling_window_days": ROLLING_WINDOW,
            "event_window_trading_days": EVENT_WINDOW_TD,
            "return_type": "log adjusted-close",
            "correlation_type": "Pearson rolling-60",
            "summary_statistic": (
                "within-pair median of correlation in stress vs baseline windows; "
                "δ = stress_median − baseline_median"
            ),
            "stress_window_definition": (
                "union of ±20-trading-day windows around each of the 6 stress events"
            ),
            "baseline_window_definition": (
                "all other rolling-60 observations after warmup"
            ),
        },
        "tickers_pulled": list(closes.columns),
        "date_range_pulled": {
            "start": str(closes.index.min().date()),
            "end": str(closes.index.max().date()),
            "n_rows": int(len(closes)),
        },
        "stress_events": STRESS_EVENTS,
        "per_event_pair_results": per_event_results,
        "per_pair_aggregate": per_pair_aggregate,
        "ladder": {
            "ordered_high_to_low": [{"pair_id": pid, "delta": d} for pid, d in ladder],
            "gaps": gaps,
            "reading": ladder_reading,
        },
        "primary_pair_verdict": {
            "pair_id": "IND_TATAELXSI",
            "delta": primary_delta,
            "classification": primary_classification,
            "blind_pre_registered_interval": [0.05, 0.10],
            "h21_1a_alternative_threshold": 0.10,
            "h21_1b_alternative_band": [-0.05, 0.05],
        },
    }


if __name__ == "__main__":
    result = run()
    out_path = Path(__file__).with_name(
        "dione-day22-cronD-h21_1ab-output.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path}")
    primary = result["primary_pair_verdict"]
    print(f"Primary (TATAELXSI.NS ↔ TSM) δ = {primary['delta']}")
    print(f"Classification: {primary['classification']}")
    print(f"Ladder reading: {result['ladder']['reading']}")
    print(f"Per-pair deltas:")
    for pid, agg in result["per_pair_aggregate"].items():
        print(f"  {pid}: δ={agg.get('delta')} stress_med={agg.get('stress_median')} "
              f"baseline_med={agg.get('baseline_median')} "
              f"n_stress={agg.get('n_stress')} n_baseline={agg.get('n_baseline')}")
    sys.exit(0)
