"""Day-28 cron-D data pull — H25.2 EU member-state decomposition (q-day24-5 path test).

Executed by Dione 2026-06-12 cron-D (first post-migration fire on Uranus-2).
Pre-registered at Day-25 cron-B:
research/cross_substrate/dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md

Execution-fire note: pre-registration §3.4 names the artifact after the actual
execution fire. Pre-registered execution was Day-28 cron-A (2026-06-07 06:00
CEST, per Day-27 §3.1); the Uranus-1→Uranus-2 migration freeze (2026-06-06
12:00 → 2026-06-12) deferred execution to Day-28 cron-D 2026-06-12 17:00 CEST.
No numeric commitment, interval, ticker, or method changed — the data window
ends 2026-05-29 exactly as pre-registered, so the deferral introduces no new
data and no forward-look.

Pull spec (per pre-registration §3.1, §3.2, §3.5):
  - Tickers: EWG (iShares MSCI Germany), EWQ (iShares MSCI France),
    EWN (iShares MSCI Netherlands) — all NYSE Arca; fresh yfinance pull.
  - Anchor: TSM — NOT re-pulled. Reused from locked Day-24 cron-B
    tickers_wide.csv (same provenance rule as Day-26 cron-B join script:
    re-pulling would introduce retroactive-adjustment variance and violate
    pre-commitment integrity).
  - Window: 2022-10-01..2026-05-31 (yf end exclusive; captures through
    2026-05-29 close, identical to Day-24/25 cron-B).
  - Method: adjusted close (auto_adjust), daily.
  - Calendar gate (§3.5): all three ETFs trade NYSE; no forward-fill expected.
    Join on the locked TSM (NYSE) calendar.
  - Volume gate (§3.5): median daily volume over the full window must be
    ≥ 50k shares for each of EWG/EWQ/EWN.
  - NaN gate (§3.5): halt only on TSM-side NaN; non-TSM NaN allowed through
    if structural (harness drops via .dropna() per Day-24 convention).
  - Output:
      tickers_eu_members.csv   (raw pulled series, NYSE calendar)
      tickers_wide.csv         (date, EWG, EWQ, EWN, TSM)
      pull_meta.json           (gate outcomes, provenance, sha256 of TSM source)
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

MEMBER_TICKERS = ["EWG", "EWQ", "EWN"]
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
        MEMBER_TICKERS, start=START, end=END, auto_adjust=True,
        progress=False, group_by="column",
    )
    if raw is None or raw.empty:
        print("YFINANCE PULL EMPTY — halt.", file=sys.stderr)
        return 2

    close = raw["Close"][MEMBER_TICKERS].copy()
    volume = raw["Volume"][MEMBER_TICKERS].copy()
    close.index = pd.to_datetime(close.index).tz_localize(None)
    volume.index = pd.to_datetime(volume.index).tz_localize(None)
    close.index.name = "date"
    close.to_csv(HERE / "tickers_eu_members.csv")

    # Join on locked TSM (NYSE) calendar — left-join, no fill expected (all NYSE).
    joined = close.reindex(tsm.index)
    joined[ANCHOR] = tsm
    joined.index.name = "date"
    out_path = HERE / "tickers_wide.csv"
    joined.to_csv(out_path)

    nan_per_col = {c: int(joined[c].isna().sum()) for c in joined.columns}
    tsm_nan = nan_per_col[ANCHOR]
    halt_on_tsm_nan = tsm_nan > 0

    vol_median = {
        t: float(volume[t].reindex(tsm.index).median()) for t in MEMBER_TICKERS
    }
    volume_gate_pass = all(v >= VOLUME_FLOOR for v in vol_median.values())

    meta = {
        "status": (
            "halt_tsm_nan" if halt_on_tsm_nan
            else ("halt_volume_floor" if not volume_gate_pass else "ok")
        ),
        "staged_at": staged_at,
        "purpose": "Day-28 cron-D data pull for H25.2 (EU member-state decomposition, q-day24-5)",
        "execution_fire": "Day-28 cron-D 2026-06-12 17:00 CEST (deferred from pre-registered Day-28 cron-A 2026-06-07 by Uranus-1→Uranus-2 migration freeze; window unchanged, no forward-look introduced)",
        "method": "fresh yfinance pull EWG/EWQ/EWN (NYSE Arca) + locked Day-24 cron-B TSM anchor (no TSM re-pull)",
        "tickers": {"members": MEMBER_TICKERS, "anchor": ANCHOR},
        "window": {"start": START, "end_exclusive": END},
        "anchor_source": {
            "path": str(DAY24_DATA.relative_to(HERE.parent.parent)),
            "sha256": sha256(DAY24_DATA),
            "first_date": str(day24.index.min().date()),
            "last_date": str(day24.index.max().date()),
            "n_rows": int(len(day24)),
        },
        "joined": {
            "first_date": str(joined.index.min().date()),
            "last_date": str(joined.index.max().date()),
            "n_rows": int(len(joined)),
            "columns": list(joined.columns),
        },
        "volume_gate": {
            "floor_shares": VOLUME_FLOOR,
            "median_daily_volume": vol_median,
            "pass": volume_gate_pass,
            "precedent": "50k floor per pre-registration §3.5 (Day-21 §4.3 EWJ precedent)",
        },
        "nan_gate": {
            "total_nan_cells": int(joined.isna().sum().sum()),
            "per_column": nan_per_col,
            "halt_rule": "halt only on TSM-side NaN; non-TSM NaN allowed through if structural (harness drops via .dropna())",
            "halt_fired": halt_on_tsm_nan,
        },
        "output": str(out_path.name),
        "next_step": "Execute dione-day28-cronD-h25_2-eu-member-decomposition.py (same fire)",
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
