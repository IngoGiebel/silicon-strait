"""Day-26 cron-B data pre-stage — H26.1 firm-level re-test of H24.1 under M-25-1.

Pre-staged by Dione 2026-06-05 cron-B per H26.1 pre-commitment §4.4
(research/cross_substrate/dione-day26-cronA-h24_1-firm-level-retest-queue-2026-06-04.md).

This is a JOIN script, not a fresh pull. Per the pre-commitment integrity rule
(H26.1 spec §8), Day-26 cron-A is forbidden from modifying any numeric
commitment, interval, or method. Re-pulling from yfinance at cron-B would
introduce new variance (yfinance occasionally adjusts adjusted-close history
retroactively after corporate actions), which would not be a method change
per se but would violate the spirit of "frozen at this commit's parent state".

The safest reproducibility path is to assemble the 4-substrate × 1-anchor wide
CSV from the already-audited, already-committed cron-B data of Day-24 and
Day-25, both of which are 917-row series on the NYSE calendar from
2022-10-03..2026-05-29 inclusive.

Sources reused (both immutable in trunk):
  - dione-day24-cronB-data/tickers_wide.csv  (SPY, EWJ, EWY, EZU, TSM)
  - dione-day25-cronB-data/tickers_wide.csv  (005930.KS, TSM — TSM identical to Day-24's)

Output:
  tickers_wide.csv  (date, SPY, EWJ, 005930.KS, EZU, TSM — note EWY DROPPED per M-25-1)
  pull_meta.json    (provenance trail, byte-identity checks vs source CSVs)

The cron-C harness consumes tickers_wide.csv. The harness is written separately
at dione-day26-cronC-h26_1-firm-level-retest.py, mirroring Day-24's cron-C
correlation script with the ROK ticker substituted.
"""
from __future__ import annotations
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

TSM_RELATIVE_TOL = 1e-12  # CSV-roundtrip ULP tolerance; far below any decimal we report

HERE = Path(__file__).resolve().parent
DAY24_DATA = HERE.parent / "dione-day24-cronB-data" / "tickers_wide.csv"
DAY25_DATA = HERE.parent / "dione-day25-cronB-data" / "tickers_wide.csv"

US_TICKER = "SPY"
JPN_TICKER = "EWJ"
ROK_TICKER = "005930.KS"
EU_TICKER = "EZU"
ANCHOR = "TSM"
ROK_TICKER_RETIRED = "EWY"


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
    if not DAY25_DATA.exists():
        print(f"DAY-25 DATA MISSING: {DAY25_DATA}", file=sys.stderr)
        return 2

    day24 = pd.read_csv(DAY24_DATA, index_col="date", parse_dates=["date"]).sort_index()
    day25 = pd.read_csv(DAY25_DATA, index_col="date", parse_dates=["date"]).sort_index()

    tsm_day24 = day24[ANCHOR].values
    tsm_day25 = day25[ANCHOR].values
    tsm_bit_identical = bool(np.array_equal(tsm_day24, tsm_day25, equal_nan=True))
    tsm_allclose = bool(
        np.allclose(tsm_day24, tsm_day25, rtol=TSM_RELATIVE_TOL, equal_nan=True)
    )
    if not tsm_allclose:
        diff_rows = int(
            (~np.isclose(tsm_day24, tsm_day25, rtol=TSM_RELATIVE_TOL, equal_nan=True)).sum()
        )
        print(
            f"TSM SERIES DIVERGES NUMERICALLY between Day-24 and Day-25 cron-B ({diff_rows} "
            f"rows beyond rtol={TSM_RELATIVE_TOL}). Halting — pre-commitment integrity violated.",
            file=sys.stderr,
        )
        return 3
    ulp_drift_rows = 0
    if not tsm_bit_identical:
        ulp_drift_rows = int(
            (tsm_day24.view(np.uint64) != tsm_day25.view(np.uint64)).sum()
        )

    rok = day25[[ROK_TICKER]]
    joined = pd.concat(
        [day24[US_TICKER], day24[JPN_TICKER], rok[ROK_TICKER], day24[EU_TICKER], day24[ANCHOR]],
        axis=1,
    )
    joined.columns = [US_TICKER, JPN_TICKER, ROK_TICKER, EU_TICKER, ANCHOR]
    joined.index.name = "date"
    out_path = HERE / "tickers_wide.csv"
    joined.to_csv(out_path)

    nan_per_col = {c: int(joined[c].isna().sum()) for c in joined.columns}
    rok_nan = nan_per_col.get(ROK_TICKER, 0)
    tsm_nan = nan_per_col.get(ANCHOR, 0)
    halt_on_tsm_nan = tsm_nan > 0

    meta = {
        "status": "halt_tsm_nan" if halt_on_tsm_nan else ("ok_structural_gap" if rok_nan > 0 else "ok"),
        "staged_at": staged_at,
        "purpose": "Day-26 cron-B data pre-stage for H26.1 (firm-level re-test of H24.1 under M-25-1)",
        "method": "join-from-locked-sources (no fresh yfinance pull; preserves pre-commitment integrity)",
        "tickers_assembled": {
            "US": US_TICKER,
            "JPN": JPN_TICKER,
            "ROK": ROK_TICKER,
            "EU": EU_TICKER,
            "anchor": ANCHOR,
        },
        "tickers_retired_under_M_25_1": [ROK_TICKER_RETIRED],
        "sources": {
            "day24": {
                "path": str(DAY24_DATA.relative_to(HERE.parent.parent)),
                "sha256": sha256(DAY24_DATA),
                "columns_used": [US_TICKER, JPN_TICKER, EU_TICKER, ANCHOR],
                "first_date": str(day24.index.min().date()),
                "last_date": str(day24.index.max().date()),
                "n_rows": int(len(day24)),
            },
            "day25": {
                "path": str(DAY25_DATA.relative_to(HERE.parent.parent)),
                "sha256": sha256(DAY25_DATA),
                "columns_used": [ROK_TICKER, ANCHOR],
                "first_date": str(day25.index.min().date()),
                "last_date": str(day25.index.max().date()),
                "n_rows": int(len(day25)),
            },
        },
        "tsm_consistency_check": {
            "day24_bit_eq_day25": tsm_bit_identical,
            "day24_allclose_day25": tsm_allclose,
            "ulp_drift_rows": ulp_drift_rows,
            "relative_tolerance": TSM_RELATIVE_TOL,
            "rule": (
                "Day-24 and Day-25 cron-B TSM series must agree within float64 CSV-roundtrip "
                "tolerance (rtol=1e-12). Both are NYSE-calendar adjusted close 2022-10-03..2026-05-29. "
                "Any ULP-level drift is CSV-serialization roundoff at the 13th significant digit "
                "(<<1e-4 — below the precision of any reported δ); deeper divergence would indicate "
                "a re-pull and is treated as a halt."
            ),
        },
        "joined": {
            "first_date": str(joined.index.min().date()),
            "last_date": str(joined.index.max().date()),
            "n_rows": int(len(joined)),
            "columns": list(joined.columns),
        },
        "nan_gate": {
            "total_nan_cells": int(joined.isna().sum().sum()),
            "per_column": nan_per_col,
            "halt_rule": "halt only on TSM-side NaN; ROK-side NaN is structural KRX-calendar gap (cron-C drops via .dropna() per Day-24 convention)",
            "halt_fired": halt_on_tsm_nan,
            "structural_gap_note_rok": (
                f"{rok_nan} ROK-side NaN cells carried over from Day-25 cron-B "
                "(Lunar New Year, Chuseok structural closures); cron-C harness drops via .dropna()"
                if rok_nan > 0 else None
            ),
        },
        "output": str(out_path.name),
        "next_step": "Execute dione-day26-cronC-h26_1-firm-level-retest.py at Day-26 cron-C 14:00 CEST",
    }
    (HERE / "pull_meta.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False)
    )
    print(json.dumps(meta, indent=2, ensure_ascii=False))
    return 3 if halt_on_tsm_nan else 0


if __name__ == "__main__":
    sys.exit(main())
