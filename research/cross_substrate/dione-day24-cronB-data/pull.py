"""Day-24 cron-B data pull — H24.1 textual-axis sweep + stress-window anchors.

Pre-staged by Dione 2026-06-03 cron-B. Inputs to cron-C's correlation harness.

Pull spec (per Day-24 cron-A scoping §3.1, §3.4, §6 risk #2):
  - Tickers: SPY, EWJ, EWY, EZU, TSM (5 NYSE-aligned daily closes)
  - Window: 2022-10-01..2026-05-30 (wide enough for DUV-2023 60-day warmup + full-period baseline)
  - Source: Yahoo Finance via yfinance (primary)
  - Method: adjusted close, daily, business days only
  - Output: tickers.csv (tidy), tickers_wide.csv (wide), pull_meta.json
"""
from __future__ import annotations
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf

HERE = Path(__file__).resolve().parent
TICKERS = ["SPY", "EWJ", "EWY", "EZU", "TSM"]
START = "2022-10-01"
END = "2026-05-31"  # yf end is exclusive — captures through 2026-05-30 close


def main() -> int:
    pulled_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    frames = {}
    failed = []
    for t in TICKERS:
        try:
            df = yf.download(
                t,
                start=START,
                end=END,
                auto_adjust=False,
                progress=False,
                threads=False,
            )
            if df.empty:
                failed.append({"ticker": t, "reason": "empty_frame"})
                continue
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            close_col = "Adj Close" if "Adj Close" in df.columns else "Close"
            ser = df[close_col].rename(t)
            frames[t] = ser
        except Exception as exc:  # noqa: BLE001
            failed.append({"ticker": t, "reason": str(exc)[:200]})

    if not frames:
        meta = {
            "status": "failed",
            "pulled_at": pulled_at,
            "tickers_requested": TICKERS,
            "tickers_pulled": [],
            "failures": failed,
        }
        (HERE / "pull_meta.json").write_text(json.dumps(meta, indent=2))
        print("ALL FAILED", file=sys.stderr)
        return 1

    wide = pd.concat(frames.values(), axis=1, keys=frames.keys())
    if isinstance(wide.columns, pd.MultiIndex):
        wide.columns = wide.columns.get_level_values(0)
    wide.index.name = "date"
    wide.to_csv(HERE / "tickers_wide.csv")

    tidy = wide.stack().reset_index()
    tidy.columns = ["date", "ticker", "adj_close"]
    tidy.to_csv(HERE / "tickers_tidy.csv", index=False)

    per_ticker = {}
    for t in frames:
        ser = wide[t].dropna()
        per_ticker[t] = {
            "first_date": ser.index.min().strftime("%Y-%m-%d"),
            "last_date": ser.index.max().strftime("%Y-%m-%d"),
            "n_obs": int(ser.shape[0]),
            "first_close": float(ser.iloc[0]),
            "last_close": float(ser.iloc[-1]),
            "nan_in_window": int(wide[t].isna().sum()),
        }

    meta = {
        "status": "ok",
        "pulled_at": pulled_at,
        "source": "yfinance",
        "method": "auto_adjust=False, then prefer Adj Close",
        "window_requested": {"start": START, "end_exclusive": END},
        "tickers_requested": TICKERS,
        "tickers_pulled": list(frames.keys()),
        "failures": failed,
        "per_ticker": per_ticker,
        "files": {
            "wide_csv": "tickers_wide.csv",
            "tidy_csv": "tickers_tidy.csv",
        },
        "purpose": "Day-24 cron-C H24.1 correlation matrix inputs (textual axis: SPY/EWJ/EWY/EZU x TSM); wide history enables both full-window AND Day-21 stress-window-anchored analyses per cron-A scoping risk #2.",
    }
    (HERE / "pull_meta.json").write_text(json.dumps(meta, indent=2))
    print(json.dumps(meta, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
