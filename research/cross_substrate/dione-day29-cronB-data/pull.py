"""Day-29 cron-B data pull — H25.3 ASML.AS × TSM firm-level test.

Executed by Dione 2026-06-13 cron-B (11:00 CEST / 09:00 UTC) on Uranus-2.
Pre-registration: research/cross_substrate/dione-day29-cronA-h25_3-asml-firm-level-pre-registration-2026-06-13.md
                  (commit 29f8c8e on silicon-strait/trunk; pushed Day-29 cron-A 06:00 CEST).
INTEGRITY: this pull postdates the pre-registration commit. No ASML.AS price
series existed in the repository before this script ran (grep-verified at
Day-29 cron-A: only a text reference in research/nexus_implications/korus-day-21-bridge).

Pull spec (per pre-registration §3.1, §3.2, §3.4, §3.5):
  - ASML.AS — ASML Holding NV, Euronext Amsterdam. Fresh yfinance pull,
    native Amsterdam trading calendar.
  - TSM — anchor; NOT re-pulled. Reused from locked Day-24 cron-B
    tickers_wide.csv (NYSE calendar, 917 returns, 2022-10-03..2026-05-29).
    Re-pulling would introduce retroactive-adjustment variance and violate
    pre-commitment integrity (same rule as Day-26/Day-28 join scripts).
  - Window: 2022-10-01..2026-05-31 (yf end exclusive; captures through the
    2026-05-29 close, identical to Day-24/25/26/28 cron-B).
  - Method: adjusted close (auto_adjust), daily.

Amsterdam calendar-asymmetry handling (pre-registration §3.4, per M-25-1 /
005930.KS precedent). Two parallel join conventions are emitted from ONE raw
ASML.AS native series so Nisaba can reproduce the deterministic reconciliation:

  - tickers_wide_global.csv   — ASML.AS reindexed onto the locked TSM NYSE
    calendar, NO forward-fill. NYSE-open / Amsterdam-closed days become
    structural NaN and drop per-pair downstream. This is the global NYSE-mask
    convention (mirrors Day-26 H26.1 cross-substrate frame). THE VERDICT in
    §2.2 is assigned on this δ.

  - tickers_wide_isolated.csv — ASML.AS reindexed onto the TSM NYSE calendar
    WITH ffill(limit=1), then downstream .dropna(). This mirrors the Day-25
    H25.1 005930.KS pair-isolated treatment exactly. Used only as the
    reconciliation reference; the global-vs-isolated offset is reported as a
    method-internal constant (Day-26 §3.4 found −0.0031 for ROK; ASML.AS's
    offset is reported, not assumed).

  - tickers_asml_native.csv    — raw ASML.AS native Amsterdam-calendar close,
    so the reconciliation is fully reproducible from source.

Data-quality gates (pre-registration §3.5):
  - Volume floor: ASML.AS median daily volume over the full window ≥ 50k shares
    (retained for protocol symmetry with H25.2 §3.5; trivially met).
  - NaN gate: halt only on TSM-side NaN; ASML.AS-side structural NaN from
    Amsterdam-only closures is allowed through (H25.1 §4.5 errata convention)
    and is exactly the asymmetry §3.4 documents.
"""
from __future__ import annotations
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf

HERE = Path(__file__).resolve().parent
DAY24_DATA = HERE.parent / "dione-day24-cronB-data" / "tickers_wide.csv"

TICKER = "ASML.AS"
ANCHOR = "TSM"
START = "2022-10-01"
END = "2026-05-31"  # exclusive; captures through 2026-05-29 close
VOLUME_FLOOR = 50_000


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    staged_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not DAY24_DATA.exists():
        print(f"DAY-24 DATA MISSING: {DAY24_DATA}", file=sys.stderr)
        return 2

    day24 = pd.read_csv(DAY24_DATA, index_col="date", parse_dates=["date"]).sort_index()
    tsm = day24[ANCHOR]

    raw = yf.download(
        TICKER, start=START, end=END, auto_adjust=True,
        progress=False, group_by="column",
    )
    if raw is None or raw.empty:
        print("YFINANCE PULL EMPTY — halt.", file=sys.stderr)
        return 2

    # yfinance single-ticker frame: columns are simple (Close, Volume, ...).
    close_native = raw["Close"].copy()
    volume_native = raw["Volume"].copy()
    if isinstance(close_native, pd.DataFrame):
        close_native = close_native[TICKER]
        volume_native = volume_native[TICKER]
    close_native.index = pd.to_datetime(close_native.index).tz_localize(None)
    volume_native.index = pd.to_datetime(volume_native.index).tz_localize(None)
    close_native.name = TICKER
    close_native.index.name = "date"
    close_native.to_csv(HERE / "tickers_asml_native.csv")

    # --- Global NYSE-mask join (verdict-bearing): reindex, NO ffill ---
    asml_global = close_native.reindex(tsm.index)
    wide_global = pd.DataFrame({TICKER: asml_global, ANCHOR: tsm})
    wide_global.index.name = "date"
    wide_global.to_csv(HERE / "tickers_wide_global.csv")

    # --- Pair-isolated join (reconciliation ref): reindex, ffill(limit=1) ---
    asml_isolated = close_native.reindex(tsm.index).ffill(limit=1)
    wide_isolated = pd.DataFrame({TICKER: asml_isolated, ANCHOR: tsm})
    wide_isolated.index.name = "date"
    wide_isolated.to_csv(HERE / "tickers_wide_isolated.csv")

    # --- Calendar-asymmetry diagnostics ---
    n_nyse = int(len(tsm.index))
    n_asml_native = int(len(close_native))
    n_co_trading = int(asml_global.notna().sum())  # NYSE days with an ASML close
    n_nyse_open_asml_closed = int(asml_global.isna().sum())  # before ffill
    n_recovered_by_ffill1 = int(
        asml_isolated.notna().sum() - asml_global.notna().sum()
    )
    # Amsterdam-open / NYSE-closed days = native dates not in the NYSE index.
    n_asml_open_nyse_closed = int((~close_native.index.isin(tsm.index)).sum())

    nan_global = {c: int(wide_global[c].isna().sum()) for c in wide_global.columns}
    tsm_nan = nan_global[ANCHOR]
    halt_on_tsm_nan = tsm_nan > 0

    vol_median = float(volume_native.reindex(tsm.index).median())
    volume_gate_pass = vol_median >= VOLUME_FLOOR

    meta = {
        "status": (
            "halt_tsm_nan" if halt_on_tsm_nan
            else ("halt_volume_floor" if not volume_gate_pass else "ok")
        ),
        "staged_at": staged_at,
        "test": "H25.3",
        "purpose": "Day-29 cron-B data pull for H25.3 (ASML.AS × TSM firm-level channel test)",
        "execution_fire": "Day-29 cron-B 2026-06-13 11:00 CEST (Uranus-2); pull postdates pre-reg commit 29f8c8e",
        "pre_registration": "research/cross_substrate/dione-day29-cronA-h25_3-asml-firm-level-pre-registration-2026-06-13.md",
        "pre_registration_commit": "29f8c8e",
        "integrity": "no ASML.AS price series existed pre-pull (grep-verified Day-29 cron-A); pull postdates pushed pre-reg",
        "method": "fresh yfinance pull ASML.AS (Euronext Amsterdam, native calendar) + locked Day-24 cron-B TSM anchor (no TSM re-pull)",
        "tickers": {"firm": TICKER, "anchor": ANCHOR},
        "window": {"start": START, "end_exclusive": END},
        "anchor_source": {
            "path": str(DAY24_DATA.relative_to(HERE.parent.parent)),
            "sha256": sha256(DAY24_DATA),
            "first_date": str(day24.index.min().date()),
            "last_date": str(day24.index.max().date()),
            "n_rows": int(len(day24)),
        },
        "calendar_asymmetry": {
            "n_nyse_trading_days": n_nyse,
            "n_asml_native_trading_days": n_asml_native,
            "n_co_trading_days_global_mask": n_co_trading,
            "n_nyse_open_amsterdam_closed_nan_before_ffill": n_nyse_open_asml_closed,
            "n_recovered_by_ffill_limit1_isolated": n_recovered_by_ffill1,
            "n_amsterdam_open_nyse_closed_dropped_by_global_mask": n_asml_open_nyse_closed,
            "note": (
                "Global mask = NYSE calendar (TSM index), no ffill; structural ASML NaN "
                "from Amsterdam-only closures drop per-pair downstream. Pair-isolated mask "
                "= same reindex + ffill(limit=1), mirroring Day-25 H25.1 005930.KS treatment."
            ),
        },
        "volume_gate": {
            "floor_shares": VOLUME_FLOOR,
            "median_daily_volume_on_nyse_calendar": vol_median,
            "pass": volume_gate_pass,
            "precedent": "50k floor per pre-registration §3.5 (Day-21 §4.3 EWJ precedent)",
        },
        "nan_gate": {
            "global_join_total_nan_cells": int(wide_global.isna().sum().sum()),
            "global_join_per_column": nan_global,
            "halt_rule": "halt only on TSM-side NaN; ASML.AS-side structural NaN allowed through",
            "halt_fired": halt_on_tsm_nan,
        },
        "outputs": {
            "native": "tickers_asml_native.csv",
            "global_mask": "tickers_wide_global.csv",
            "pair_isolated": "tickers_wide_isolated.csv",
        },
        "next_step": "Execute dione-day29-cronB-h25_3-asml-firm-level.py (same fire)",
    }
    (HERE / "pull_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    print(json.dumps(meta, indent=2, ensure_ascii=False))
    if halt_on_tsm_nan:
        return 3
    if not volume_gate_pass:
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
