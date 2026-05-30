#!/usr/bin/env python3
"""
Day-21 cron-C: H21.1 correlation-matrix computation.

Pre-registration anchors:
  - Bridge doc commit:  5388040  (research/nexus_implications/korus-day-21-bridge-2026-05-29.md §3.2)
  - cron-A scoping:     134b09b  (research/nexus_implications/dione-day21-cronA-scoping-2026-05-30.md §2.2)
  - cron-B research:    d401621  (research/nexus_implications/dione-day21-cronB-rok-semis-pull-2026-05-30.md §1, PRC dates)

H21.1: Substrates with the coupling-property (Day-19 §5.4) show elevated equity-
       cross-correlation between their primary-exposure ticker and TSM during
       Taiwan-Strait stress events, relative to substrates lacking the property,
       at comparable economic-exposure magnitude.

Method (pre-committed; do NOT alter after seeing the data):
  - Pearson rolling-60 correlation on adjusted-close log returns
  - ±20 trading-day window around the stress-event date
  - Per pair per event report median + min + max correlation within the window
  - Predicted ordering: corr(005930.KS, TSM) > corr(BHP.AX, TSM); NVDA-TSM is
    a high-correlation control (chip-substrate upper bound).
  - Falsification rule: ≥3/4 events preserve the predicted ordering → confirmed.
    2/4 = inconclusive (both outcomes discussed in publication).
    ≤1/4 = falsified.

PRC stress-event has dual anchor: 2025-10-10 announcement AND 2025-10-14
implementation. Both are computed and reported; the PRC event contributes a
single vote to the 4-event tally, computed as the AND of the two anchors
(ordering must hold at BOTH anchors to count as preserved at PRC event).
"""
from __future__ import annotations

import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

TICKERS = ["TSM", "005930.KS", "BHP.AX", "NVDA"]
DOWNLOAD_START = "2022-04-01"
DOWNLOAD_END = "2025-12-31"
ROLLING_WINDOW = 60
EVENT_WINDOW_TD = 20  # ±20 trading days

STRESS_EVENTS = [
    {"id": "PEL_2022", "date": "2022-08-02", "label": "Pelosi Taipei visit"},
    {"id": "DUV_2023", "date": "2023-09-04", "label": "Dutch DUV ratchet"},
    {"id": "LAI_2024", "date": "2024-05-20", "label": "Lai Ching-te inauguration"},
    {"id": "PRC_2025a", "date": "2025-10-10", "label": "PRC CMOT port-fee announcement"},
    {"id": "PRC_2025i", "date": "2025-10-14", "label": "PRC port-fee implementation"},
]

PAIRS = [
    {"id": "ROK_KR", "left": "005930.KS", "right": "TSM",
     "class": "coupling_property"},
    {"id": "AUS_BHP", "left": "BHP.AX", "right": "TSM",
     "class": "non_coupling_tier_1"},
    {"id": "NVDA_US", "left": "NVDA", "right": "TSM",
     "class": "non_coupling_control_upper_bound"},
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


def evaluate_ordering(per_pair: dict[str, WindowResult]) -> dict:
    rok = per_pair.get("ROK_KR")
    bhp = per_pair.get("AUS_BHP")
    nvda = per_pair.get("NVDA_US")
    if rok is None or bhp is None:
        return {"verdict": "missing_data", "rok_median": None,
                "bhp_median": None, "delta": None, "ordering_preserved": None}
    delta = rok.median_corr - bhp.median_corr
    preserved = bool(rok.median_corr > bhp.median_corr)
    return {
        "verdict": "preserved" if preserved else "violated",
        "rok_median": rok.median_corr,
        "bhp_median": bhp.median_corr,
        "nvda_median": nvda.median_corr if nvda else None,
        "delta": delta,
        "ordering_preserved": preserved,
    }


def run() -> dict:
    closes = load_prices()
    rets = log_returns(closes)

    pair_corrs = {
        p["id"]: rolling_pair_corr(rets, p["left"], p["right"], ROLLING_WINDOW)
        for p in PAIRS
    }

    per_event_results = {}
    ordering_verdicts = {}

    for ev in STRESS_EVENTS:
        per_pair = {}
        for p in PAIRS:
            cw = window_around(pair_corrs[p["id"]], ev["date"], EVENT_WINDOW_TD)
            summary = summarise_window(cw, p, ev)
            if summary is not None:
                per_pair[p["id"]] = summary
        per_event_results[ev["id"]] = {
            pair_id: asdict(result) for pair_id, result in per_pair.items()
        }
        ordering_verdicts[ev["id"]] = evaluate_ordering(per_pair)

    # PRC event: AND-rule across {a, i} anchors
    prc_a = ordering_verdicts.get("PRC_2025a", {})
    prc_i = ordering_verdicts.get("PRC_2025i", {})
    prc_combined_preserved = bool(prc_a.get("ordering_preserved")
                                  and prc_i.get("ordering_preserved"))
    prc_combined = {
        "verdict": "preserved" if prc_combined_preserved else "violated",
        "anchor_a_preserved": prc_a.get("ordering_preserved"),
        "anchor_i_preserved": prc_i.get("ordering_preserved"),
        "ordering_preserved": prc_combined_preserved,
        "rule": "AND of {a=2025-10-10, i=2025-10-14} anchors",
    }

    # 4-event tally
    event_tally = {
        "PEL_2022": ordering_verdicts["PEL_2022"]["ordering_preserved"],
        "DUV_2023": ordering_verdicts["DUV_2023"]["ordering_preserved"],
        "LAI_2024": ordering_verdicts["LAI_2024"]["ordering_preserved"],
        "PRC_2025": prc_combined["ordering_preserved"],
    }
    preserved_count = sum(1 for v in event_tally.values() if v is True)

    if preserved_count >= 3:
        h21_1_verdict = "CONFIRMED"
    elif preserved_count == 2:
        h21_1_verdict = "INCONCLUSIVE"
    else:
        h21_1_verdict = "FALSIFIED"

    return {
        "method": {
            "rolling_window_days": ROLLING_WINDOW,
            "event_window_trading_days": EVENT_WINDOW_TD,
            "return_type": "log adjusted-close",
            "correlation_type": "Pearson rolling-60",
            "summary_statistic": "median of correlation within ±20-td window",
        },
        "tickers_pulled": list(closes.columns),
        "date_range_pulled": {
            "start": str(closes.index.min().date()),
            "end": str(closes.index.max().date()),
            "n_rows": int(len(closes)),
        },
        "per_event_pair_results": per_event_results,
        "ordering_verdicts": ordering_verdicts,
        "prc_combined": prc_combined,
        "event_tally": event_tally,
        "preserved_count": preserved_count,
        "h21_1_verdict": h21_1_verdict,
        "falsification_rule": "≥3/4 → CONFIRMED · 2/4 → INCONCLUSIVE · ≤1/4 → FALSIFIED",
    }


if __name__ == "__main__":
    result = run()
    out_path = Path(__file__).with_name(
        "dione-day21-cronC-h21_1-output.json")
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path}")
    print(f"H21.1 verdict: {result['h21_1_verdict']}")
    print(f"Preserved count: {result['preserved_count']}/4")
    print(f"Per-event ordering: {result['event_tally']}")
    sys.exit(0)
