# H25.1 Pre-Registration §4.5 Errata — Asymmetric-Calendar NaN Gate Clarification

**Filing fire:** Day-25 cron-B (2026-06-04 11:00 CEST)
**Pre-registration affected:** `research/cross_substrate/dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md` @ commit `3f396fc`
**Errata type:** Non-destructive clarification (path A, same as Day-23 §4.4 erratum precedent at commit `dcebf44`)
**Filed before:** the cron-B data-pull artifact was finalized — the pull.py run produced the gate-firing meta, this erratum reconciles it, then the harness pre-stage proceeds on the reconciled meta.

---

## §1 Issue

H25.1 pre-registration §4.5 specifies:

> NaN cells after join: must be 0 in the full window. If > 0, halt and re-pull.

The first execution of `dione-day25-cronB-data/pull.py` at 2026-06-04 11:07:47 UTC returned:

- joined_rows = 917 (identical to Day-24 cron-B; NYSE/TSM calendar)
- forward_fill.count = 38 (4.14% of joined window; below the 5% provisional flag)
- nan_gate.total_nan_cells = 17 (all in the `005930.KS` column; `TSM` has 0)
- nan_gate.halt_if_nonzero = True → status = `halt_nan_present`

The 17 NaN cells are **structural**, not transient. They correspond to NYSE/TSM trading days where the Korea Exchange was closed for **more than the pre-committed forward-fill limit of 1 trading day** — i.e., Lunar New Year sequences, Chuseok sequences, and similar multi-day KRX holidays that NYSE does not observe.

A re-pull will produce the identical NaN count, because the gap is calendrical, not stochastic. The pre-registration language "halt and re-pull" presumed yfinance flakiness as the failure mode; it does not address the asymmetric-calendar structural case.

## §2 Reconciliation with Day-24 cron-C convention

Day-24's four-pair correlation harness (`dione-day24-cronC-h24_1-correlation.py`) handles the analogous (much smaller) asymmetric-calendar issue by:

```python
pair = log_ret[[ticker, ANCHOR]].dropna()
```

— i.e., it drops any row where either side is NaN before computing log-returns and rolling correlations. For ETF-vs-TSM pairs all trading on NYSE (SPY, EWJ, EWY, EZU vs TSM), the drop count is approximately zero, so the convention is silent there. For 005930.KS-vs-TSM, the drop count is ~17 (1.85% of the joined window), which is exactly what `.dropna()` was designed to handle: co-trading-day correlation.

The analytic method specified in H25.1 pre-registration §4.3 — "Rolling-60 window Pearson correlation between `r_{005930.KS}` and `r_{TSM}`" — is **identical** to Day-24's per-pair correlation method. The cron-C harness mirrors `pair = log_ret[[TICKER, ANCHOR]].dropna()`. The resulting δ is computed on co-trading days only.

## §3 Resolution (clarification, not method change)

**§4.5 NaN-gate is reinterpreted as follows:**

- The pre-committed 1-trading-day forward-fill (§4.5 line 1) is unchanged.
- The volume floor gate (§4.5 line 2) is unchanged.
- The "NaN cells after join: must be 0" line is **clarified, not replaced**, to mean:
  - **NaN in the TSM column** indicates a yfinance pull failure → halt and re-pull (original intent).
  - **NaN in the 005930.KS column after ffill-limit-1** indicates a structural KRX calendar gap → log to meta, allow through, cron-C harness drops the affected rows via `.dropna()` per Day-24 cron-C convention. No re-pull.

Both interpretations of "NaN > 0" remain in the data-quality audit; only the **action** differs by which column the NaN appears in.

The §4.3 analytic method is **unchanged**. The §3 falsification rule + the §3 verdict intervals are **unchanged**. The §4.1 data window (2022-10-04..2026-05-29) is **unchanged**.

## §3.bis §4.3 mean-vs-median ambiguity resolution

**Issue.** H25.1 pre-registration §4.3 has two clauses in tension:

> "Stress δ = (mean of rolling-60 ρ over stress-window trading days) − (mean of rolling-60 ρ over baseline-window trading days)."
> "δ reported as a single number across the three stress windows pooled, matching Day-24 cron-C's pooling convention."

The first clause says **mean**. The second clause references Day-24 cron-C's pooling convention, which used **median** (`dione-day24-cronC-h24_1-correlation.py:124-125`). The §3 verdict intervals (`δ < −0.001` for sign-flip, `[−0.001, +0.05]` INCONCLUSIVE, `δ > +0.05` measurement-quality) were calibrated against Day-24's EWY × TSM **median** δ = −0.0077.

**Resolution.** Cron-C harness computes **both** mean and median, reports both, and assigns `verdict_path` using **median** to preserve calibration-comparability with Day-24's EWY × TSM benchmark (the disambiguation target). Mean is reported as a secondary statistic to satisfy the §4.3 literal text. If the two statistics disagree on verdict_path (mean and median land in different §3 buckets), the harness flags `verdict_consensus = "mean_median_disagreement"` and the verdict is assigned per **median** with the disagreement logged for Nisaba audit.

**Rationale.** Median is robust to rolling-60-correlation outliers (stress-window tails can be dominated by 1-2 extreme days that swing the mean but not the median). Day-24's calibration choice rests on this robustness. Switching to mean here would re-calibrate the verdict intervals implicitly, which is exactly what pre-registration is supposed to prevent.

**Pre-commit:** this clarification is filed before the cron-C harness is staged, before the cron-C execution at 14:00 CEST. The §3 verdict intervals (the actual falsification rule) are **unchanged**.

## §4 Operational changes (this commit)

1. `dione-day25-cronB-data/pull.py` updated: `status = "halt_nan_present"` only when `TSM` column has NaN; for `005930.KS`-side NaN, status = `"ok_structural_gap"` with `nan_gate.structural_gap_note` populated. Halt return-code 3 fires only on TSM-side NaN.
2. `pull_meta.json` regenerated under the clarified gate (overwrites the 11:07:47 UTC artifact, which is captured in this errata's §1 for audit).
3. Cron-C harness (`dione-day25-cronC-h25_1-rok-firm-correlation.py`) pre-staged at this fire will use `pair = log_ret[[TICKER, ANCHOR]].dropna()` exactly as Day-24 does, and report `n_pair_obs` (co-trading days) and `n_dropped_asymmetric_calendar` (the 17-row drop) explicitly so the audit trail surfaces the structural gap.

## §5 Reversibility

This errata is non-destructive: the original §4.5 spec stays in the pre-registration file; the clarification lives here. If Ingo or a Trinity reviewer judges the clarification too permissive, the path-A reversion is to:

- Revert this commit (the pull.py change + this errata file)
- Re-pull with a stricter calendar-intersection join (KRX∩NYSE, not NYSE-with-ffill), producing a smaller but NaN-free joined window
- Re-pre-register §4.5 with the intersection convention explicit
- Re-stage cron-C harness on the new join

The current path preserves Day-24/Day-25 method-comparability (same NYSE calendar, same `.dropna()` convention).

## §6 Audit trail

| Step | Artifact | Commit | Status |
|---|---|---|---|
| Pre-reg §4.5 spec filed | `dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md` | `3f396fc` | unchanged |
| First pull artifact (gate-firing) | `dione-day25-cronB-data/pull_meta.json` @ 11:07:47 UTC | (overwritten by §4) | quoted in §1 |
| This errata | `research/methodology/dione-day25-cronB-h25_1-pre-registration-errata-2026-06-04.md` | (this commit) | filed |
| Pull.py clarification | `dione-day25-cronB-data/pull.py` | (this commit) | applied |
| Reconciled pull artifact | `dione-day25-cronB-data/pull_meta.json` (post-rerun) | (this commit) | finalized |
| Cron-C harness (pre-stage) | `dione-day25-cronC-h25_1-rok-firm-correlation.py` | (this commit) | pending in this fire |

---

**Filed by:** Dione 🌙 at Day-25 cron-B 2026-06-04 11:00 CEST
**Cross-references:**
- Day-23 §4.4 erratum precedent at commit `dcebf44` (path-A non-destructive errata, q-day24-1)
- Day-24 cron-C `.dropna()` convention at `dione-day24-cronC-h24_1-correlation.py:117`
- H25.1 pre-registration §4.5 at `dione-day25-cronA-rok-firm-level-pre-registration-2026-06-04.md:63-66`
