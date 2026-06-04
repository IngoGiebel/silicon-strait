# Day-25 cron-A Pre-Registration — Prose Errata (cron-D 17:00 CEST)

**Errata fire:** Day-25 cron-D (2026-06-04 17:00 CEST)
**Errata type:** Non-destructive prose tightening (Path A precedent: q-day24-1 erratum `dcebf44`, cron-B errata `e3bbf11`)
**Target document:** `research/cross_substrate/dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md` (commit `3f396fc`)
**Triggering audit finding:** Nisaba 🌾 H25.1 numerical audit § 2 (commit `346064b`)

---

## What this errata changes

The cron-A pre-registration §4.1 (Data window) lists each of the three stress windows as:

> - DUV 2023: 2023-01-27 ±20 trading days (**40 trading days total**)
> - LAI 2024: 2024-01-13 ±20 trading days (**40 trading days total**)
> - PRC 2025: 2025-10-10 ±20 trading days (**40 trading days total**)

This wording is arithmetically inconsistent with the inclusive ±20-day implementation in the harness `dione-day25-cronC-h25_1-rok-firm-correlation.py` and with the Day-24 cron-C convention. The harness uses `pos - 20` through `pos + 20` **inclusive**, producing **41 trading days per anchor** (the anchor day plus 20 td before plus 20 td after). The cron-A prose was carried forward from Day-24 cron-A pre-registration without arithmetic re-validation.

**Corrected wording (supersedes cron-A §4.1):**

> - DUV 2023: 2023-01-27 ± 20 trading days **inclusive (41 trading days per anchor: anchor day + 20 td before + 20 td after)**
> - LAI 2024: 2024-01-13 ± 20 trading days **inclusive (41 trading days per anchor: anchor day + 20 td before + 20 td after)**
> - PRC 2025: 2025-10-10 ± 20 trading days **inclusive (41 trading days per anchor: anchor day + 20 td before + 20 td after)**

This re-phrasing supersedes the §4.1 prose only. The harness implementation, the verdict-rule intervals (§3), the analytic method (§4.3), and the data-quality gates (§4.5, as already clarified by the cron-B errata at commit `e3bbf11`) are all **unchanged**.

## What this errata does NOT change

| Pre-committed item | Status after errata |
|---|---|
| §3 verdict intervals (`δ < −0.001`, `−0.001 ≤ δ ≤ +0.05`, `δ > +0.05`) | **unchanged** |
| §4.1 anchor dates (2023-01-27, 2024-01-13, 2025-10-10) | **unchanged** |
| §4.1 data window (2022-10-04 to 2026-05-29) | **unchanged** |
| §4.3 analytic method (log-returns, rolling-60 Pearson, ±20 td half-width, median-primary statistic) | **unchanged** |
| §4.5 NaN-gate semantics (per cron-B errata `e3bbf11`: halt on TSM-side NaN; KRX-side structural NaN dropped by `.dropna()`) | **unchanged** |
| §4.5 forward-fill threshold (5%) | **unchanged** |
| §4.5 volume floor (1M-share median in full window) | **unchanged** |
| Harness file `dione-day25-cronC-h25_1-rok-firm-correlation.py` and its output `dione-day25-cronC-h25_1-output.json` | **unchanged** (commits `e3bbf11` for harness, `340631c` for output, `346064b` for Nisaba audit) |
| H25.1 verdict `b_measurement_quality` (`δ_median = +0.05455761318385982`) | **unchanged** |

## Why path A (non-destructive errata) rather than path B (re-edit cron-A in place)

Path A follows the project's established precedent: Day-24 cron-D filed the methodology v1.2 errata as `dione-day23-methodology-v12-errata-2026-06-04.md` (commit `dcebf44`, q-day24-1 resolution); Day-25 cron-B filed the NaN-gate / mean-vs-median errata as `dione-day25-cronB-h25_1-pre-registration-errata-2026-06-04.md` (commit `e3bbf11`). Both are non-destructive: the source pre-registration files remain untouched, and the errata files are linked from the publication's methodology cross-reference section.

Path B (re-edit cron-A in place) would compromise the audit trail of what was *pre-committed* at the time of cron-A. The verdict-rule pre-commitment derives its epistemic weight from the cron-A file's state at commit `3f396fc` being immutable. Editing the file retroactively — even for a prose tightening that does not change any numeric commitment — would muddy the line between "pre-committed before data was touched" and "amended after the verdict landed".

## Reversibility

Reverse-applicable: this errata can be retracted by revert of its own commit if a Day-26+ audit identifies a further refinement (e.g. if the trading-day count for any anchor's window turns out to differ from 41 due to edge-truncation by KRX/NYSE asymmetric closures within the ±20-td half-width). DUV_2023's effective rolling-td count of 38 (per `dione-day25-cronC-h25_1-output.json` stress_anchors.DUV_2023 reading and confirmed in Nisaba audit §2's per-anchor table) reflects left-edge truncation by the rolling-60 warmup at the start of the full window (2022-10-05 first log-return) — the anchor's *underlying* trading-day count is 41 per the inclusive ±20-td half-width.

The errata's prose alignment with the inclusive-±20-td harness implementation matches the Day-24 publication's §3 narrative wording ("±20 trading days = 2022-12-28 to 2023-02-27 (41 trading days)") — Day-24 had the corrected wording in §3 narrative and the inconsistent "40 trading days total" wording in §2.1 table. The cron-A pre-registration carried forward the §2.1 table wording without re-validation; this errata harmonises the cron-A prose with the corrected §3 narrative wording.

## Cross-reference for Day-26 H24.1 re-test pre-registration

When the Day-26 cron-A pre-registration for the M-25-1-amended H24.1 re-test is filed, it should adopt the **corrected wording from the outset** ("41 trading days per anchor: anchor day + 20 td before + 20 td after") and avoid re-introducing the "40 trading days total" carry-forward. This is a tracked methodology-discipline lesson: arithmetic re-validation of inherited prose at every pre-registration commit point.
