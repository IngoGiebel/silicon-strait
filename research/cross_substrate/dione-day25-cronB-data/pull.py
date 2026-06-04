"""Day-25 cron-B data pull — H25.1 ROK firm-level disambiguation.

Pre-staged by Dione 2026-06-04 cron-B per H25.1 pre-registration §4.4.
Inputs to cron-C's single-pair correlation harness.

Pull spec (per Day-25 cron-A pre-registration §4.1, §4.2, §4.5):
  - Ticker: 005930.KS (Samsung Electronics, KRX)
  - Anchor: TSM (already pulled in Day-24 cron-B at ../dione-day24-cronB-data/tickers_wide.csv)
  - Window: 2022-10-01..2026-05-31 (yf end exclusive; captures through 2026-05-29 close,
    identical to Day-24 cron-B; ends before today to avoid forward-look bias).
  - Source: Yahoo Finance via yfinance (primary).
  - Method: adjusted close, daily.
  - Calendar gate (§4.5): KRX differs from NYSE; align on NYSE (TSM) calendar, forward-fill
    005930.KS by ≤ 1 td at asymmetric edges. If fill ≥ 5% of joined window, flag provisional.
  - Volume gate (§4.5): median daily volume in joined window must be ≥ 1M shares.
  - NaN gate (§4.5, clarified by 2026-06-04 errata at
    research/methodology/dione-day25-cronB-h25_1-pre-registration-errata-2026-06-04.md):
      * NaN in TSM column → yfinance failure → halt + re-pull (original intent).
      * NaN in 005930.KS column after ffill-limit-1 → structural KRX calendar
        gap (Lunar New Year, Chuseok, etc.) → log to meta, allow through,
        cron-C harness drops affected rows via .dropna() per Day-24 convention.
  - Output:
      tickers_005930ks.csv          (raw KRX-calendar series)
      tickers_wide.csv              (joined to TSM on NYSE calendar w/ forward-fill ≤ 1 td)
      pull_meta.json                (gate outcomes, fill_count, volume_median, NaN_count)
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf

HERE = Path(__file__).resolve().parent
DAY24_DATA = HERE.parent / "dione-day24-cronB-data" / "tickers_wide.csv"
TICKER = "005930.KS"
ANCHOR = "TSM"
START = "2022-10-01"
END = "2026-05-31"

FORWARD_FILL_MAX_TDAYS = 1
FORWARD_FILL_FLAG_RATIO = 0.05
VOLUME_FLOOR_SHARES = 1_000_000


def main() -> int:
    pulled_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    failures: list[dict] = []

    try:
        raw = yf.download(
            TICKER,
            start=START,
            end=END,
            auto_adjust=False,
            progress=False,
            threads=False,
        )
    except Exception as exc:  # noqa: BLE001
        failures.append({"ticker": TICKER, "reason": str(exc)[:200]})
        raw = pd.DataFrame()

    if raw.empty:
        meta = {
            "status": "failed",
            "pulled_at": pulled_at,
            "ticker_requested": TICKER,
            "failures": failures,
        }
        (HERE / "pull_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
        print(json.dumps(meta, indent=2, ensure_ascii=False))
        return 2

    if isinstance(raw.columns, pd.MultiIndex):
        raw.columns = raw.columns.get_level_values(0)
    close_col = "Adj Close" if "Adj Close" in raw.columns else "Close"
    vol_col = "Volume"

    krx_close = raw[close_col].rename(TICKER)
    krx_volume = raw[vol_col].rename(f"{TICKER}_volume") if vol_col in raw.columns else None

    krx_close.index = pd.to_datetime(krx_close.index).tz_localize(None)
    krx_close.index.name = "date"
    krx_close.to_frame().to_csv(HERE / "tickers_005930ks.csv")

    # Load Day-24 TSM series (NYSE calendar)
    day24 = pd.read_csv(DAY24_DATA, index_col="date", parse_dates=["date"]).sort_index()
    tsm = day24[[ANCHOR]].copy()
    tsm.index = pd.to_datetime(tsm.index).tz_localize(None)
    tsm.index.name = "date"

    # Reindex KRX to NYSE calendar with forward-fill limit ≤ 1 td
    krx_on_nyse = krx_close.reindex(tsm.index).ffill(limit=FORWARD_FILL_MAX_TDAYS)
    fill_mask = krx_on_nyse.notna() & krx_close.reindex(tsm.index).isna()
    fill_count = int(fill_mask.sum())
    join_n = int(len(tsm.index))
    fill_ratio = fill_count / join_n if join_n else 0.0
    fill_flag = fill_ratio >= FORWARD_FILL_FLAG_RATIO

    joined = pd.concat([krx_on_nyse, tsm[ANCHOR]], axis=1)
    joined.columns = [TICKER, ANCHOR]
    joined.to_csv(HERE / "tickers_wide.csv")

    nan_count = int(joined.isna().sum().sum())
    nan_per_col = {c: int(joined[c].isna().sum()) for c in joined.columns}
    nan_tsm = nan_per_col.get(ANCHOR, 0)
    nan_krx = nan_per_col.get(TICKER, 0)
    halt_on_tsm_side_nan = nan_tsm > 0

    # Volume gate
    volume_median: float | None = None
    volume_floor_ok: bool | None = None
    if krx_volume is not None:
        krx_volume.index = pd.to_datetime(krx_volume.index).tz_localize(None)
        krx_vol_on_nyse = krx_volume.reindex(tsm.index).ffill(limit=FORWARD_FILL_MAX_TDAYS)
        krx_vol_clean = krx_vol_on_nyse.dropna()
        if len(krx_vol_clean):
            volume_median = float(krx_vol_clean.median())
            volume_floor_ok = volume_median >= VOLUME_FLOOR_SHARES

    if halt_on_tsm_side_nan:
        status_str = "halt_nan_present"
    elif nan_krx > 0:
        status_str = "ok_structural_gap"
    else:
        status_str = "ok"

    meta = {
        "status": status_str,
        "pulled_at": pulled_at,
        "ticker_requested": TICKER,
        "anchor": ANCHOR,
        "window": {"start": START, "end": END, "end_exclusive": True},
        "join_calendar": "NYSE (Day-24 cron-B TSM index)",
        "joined_rows": join_n,
        "first_date": str(joined.index.min().date()),
        "last_date": str(joined.index.max().date()),
        "forward_fill": {
            "max_tdays": FORWARD_FILL_MAX_TDAYS,
            "count": fill_count,
            "ratio": fill_ratio,
            "flag_threshold": FORWARD_FILL_FLAG_RATIO,
            "flag_provisional": fill_flag,
        },
        "volume_gate": {
            "median_shares": volume_median,
            "floor_shares": VOLUME_FLOOR_SHARES,
            "floor_met": volume_floor_ok,
        },
        "nan_gate": {
            "total_nan_cells": nan_count,
            "per_column": nan_per_col,
            "halt_rule_clarified_2026_06_04": "halt only on TSM-side NaN; KRX-side NaN is structural (dropped by cron-C .dropna() per Day-24 convention)",
            "halt_fired": halt_on_tsm_side_nan,
            "structural_gap_note": (
                f"{nan_krx} KRX-side rows are >1-td-gap structural closures "
                "(Lunar New Year, Chuseok, etc.); cron-C harness drops them via .dropna()"
                if nan_krx > 0 else None
            ),
        },
        "outputs": [
            "tickers_005930ks.csv",
            "tickers_wide.csv",
        ],
    }
    (HERE / "pull_meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    print(json.dumps(meta, indent=2, ensure_ascii=False))
    return 3 if halt_on_tsm_side_nan else 0


if __name__ == "__main__":
    sys.exit(main())
