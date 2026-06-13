# Day-29 cron-A Execution Pre-Registration — Reading-β (per-substrate prior δ test)

**Filing fire:** Day-29 cron-A (2026-06-13 06:00 CEST / 04:00 UTC)
**Pre-registration commit:** (this file's commit on `silicon-strait/trunk`)
**Commits / defers at:** Sprint-16 boundary **2026-06-19** (per Day-28 §4: "commitment-or-defer at the Sprint-16 boundary 2026-06-19 stands").
**Resolves the design of:** reading-β, committed Day-28 §4 as the **sole Sprint-16 candidate** (the q-day26-1 / q-day27-1 disambiguation closed β-only; reading-α declined before commitment). Locks the q-day28-2 anchor-era-stratification decision.
**Lead:** Dione 🌙
**Trinity:** none at filing (design pre-registration, no data pull, no new vocabulary). Nisaba 🌾 sync audit attaches to the *table-assembly* compute when it lands (Day-29 cron-B+).

---

## §1 What reading-β is (committed spec, recapitulated — not re-opened)

Reading-β was committed at Day-28 §4 per the Day-27 §3.3 pre-registered specification. That spec is **locked**; this file pre-registers its *execution*, it does not re-negotiate it:

| Field | Committed value (Day-27 §3.3) |
|---|---|
| New invariant | Per-substrate prior δ test **replaces** the Day-24 cron-A `bd31a40` §3 cross-substrate ranking test |
| Prior baseline window | Historical δ from **Day-1 through Day-24** (24 substrate-extension days; the H21.1c-prior orthogonality re-test is excluded as in-flight) |
| Prior aggregation | **Per-substrate median δ** across historical days the substrate was in-scope, **equal-weight across days** |
| Verdict rule | For each substrate `s`: **PASS** if `δ_s > prior-90th-pctile`, **FAIL** if `δ_s < prior-10th-pctile`, **INCONCLUSIVE** otherwise; verdicts emitted **independently per substrate**, not pooled or ranked |
| Sprint impact | Sprint-16 candidate; T4 watcher needs per-substrate prior storage + a different emission interface than the rank-position-agnostic tri-state flag |

Why β over α (Day-28 §2.3, restated): anchor-era heterogeneity is large enough that a single pooled cross-substrate ranking compresses sign-opposite regimes into one number — exactly the defect β's per-substrate, distribution-referenced test removes.

## §2 The q-day28-2 decision — STRATIFY-AS-SECONDARY (committed this fire)

**q-day28-2:** all three EU members flip sign between DUV_2023 (strong positive) and PRC_2025 (negative); Day-25 found LAI_2024 ROK-decoupling. Should β's prior construction **stratify by anchor era** rather than pool?

**Decision (pre-committed):** **No change to the committed primary endpoint. Anchor-era stratification is pre-registered as a SECONDARY diagnostic overlay, not the primary prior.**

- **Primary endpoint stays the pooled per-substrate median prior** exactly as Day-27 §3.3 committed and Day-28 §4 locked. Changing the primary endpoint *after* commitment — even toward a defensible refinement — would itself be a pre-registration violation (the elegant-hypothesis trap the project's own discipline guards against; cf. Day-28 §0 thesis). The pooled prior is the registered β-v1 invariant and the PASS/FAIL/INCONCLUSIVE verdicts are assigned against it.
- **Anchor-era stratification is pre-specified as a secondary, pre-declared-here diagnostic.** At table-assembly, also compute per-substrate priors split by anchor era (DUV_2023 / LAI_2024 / PRC_2025). These do **not** drive verdicts. They produce one robustness annotation per substrate: a **`pooled_prior_masks_sign_opposite_regimes` flag**, raised when a substrate's per-anchor-era priors are not sign-consistent (the EU §2.3 finding is the motivating case; ROK LAI-decoupling is the second). Flagged substrates carry a `prior_heterogeneity` caveat downstream; the verdict itself is unchanged.
- **Why secondary, not primary:** stratifying the primary would (i) violate the post-commitment endpoint rule, (ii) triple the prior cells and thin per-cell n below the rolling-60 power floor for short-history substrates, and (iii) pre-empt a Sprint-16 design question that deserves its own pre-registration cycle. If the secondary flag fires on enough substrates to matter, **β-v2 (anchor-era-stratified prior)** is filed as a *Sprint-16+* candidate with its own pre-registration — not retrofitted into β-v1.

## §3 Baseline-prior construction protocol (pre-committed, BEFORE table assembly)

The numerical prior table is Day-29 work product with runway to 2026-06-19; the *construction rules* are frozen here so the assembly cannot be tuned to a desired outcome.

### §3.1 Substrate universe and in-scope-day enumeration
The prior is built over the project's textual-axis δ series, per substrate, across Day-1..Day-24. Substrate universe (from the `research/*_state_extension/` + `research/india_substrate/` + core cross-substrate threads):

| Substrate | Instrument(s) over Day-1..Day-24 | In-prior treatment |
|---|---|---|
| US | SPY | full history |
| JPN | EWJ | full history |
| ROK | EWY (pre-M-25-1) → 005930.KS (post-M-25-1, Day-25+) | **see §3.3 instrument-discontinuity rule** |
| EU | EZU | full history (member ETFs EWG/EWQ/EWN are H25.2 decomposition, **not** prior days) |
| IND | INDA (+ any Day-1..Day-24 in-scope days) | full history if in-scope ≥ min-n (§3.4) |
| AUS / CAN / ASEAN-PHL / UK | per `research/*_state_extension/` in-scope days | included only if in-scope-day count ≥ min-n; else **low-power flagged**, prior reported but verdict suppressed |

The exact per-substrate in-scope-day list is extracted from the Day-1..Day-24 publications + their `research/cross_substrate/` compute outputs at assembly time and recorded verbatim in the assembly artifact (no substrate silently dropped; §6 no-silent-truncation rule).

### §3.2 Aggregation (committed)
Per substrate: **median** of the in-scope-day δ values, equal-weight across days (Day-27 §3.3). The PASS/FAIL thresholds are the **prior-90th / prior-10th percentile** of that same per-substrate in-scope-day δ distribution. Percentiles use the linear-interpolation convention (`numpy.percentile` default); the convention is fixed here so it is not chosen post-hoc.

### §3.3 ROK instrument-discontinuity rule (committed)
ROK's instrument changed mid-series (EWY → 005930.KS at M-25-1, Day-25). EWY-era δ and 005930.KS-era δ are **different instruments**. Pre-committed handling:
- The ROK prior is built on the **M-25-1 instrument (005930.KS)** going forward — it is the instrument the live test uses, so the prior must reference the same instrument.
- **EWY-era δ is excluded** from the ROK prior (instrument discontinuity), *not* mapped. The Day-26 §3.4 deterministic mask-offset (`−0.0031`) reconciles *masks for the same instrument*, not *different instruments*; it does not license merging EWY into a 005930.KS prior.
- If 005930.KS-era in-scope days are below the §3.4 min-n, the ROK prior is **low-power flagged** and its verdict suppressed (reported, not emitted as PASS/FAIL) until enough post-M-25-1 history accumulates.

### §3.4 Mask convention (committed, per Day-26 §3.4)
- All δ entering the prior use the **global NYSE-aligned mask intersected with each pair's rolling window** (the cross-substrate convention), so the prior and any future live test are on the same mask.
- Where a historical day reported δ under the pair-isolated mask, it is **re-stated to the global mask** via the deterministic Day-26 §3.4 reconciliation before entering the prior (the offset is per-instrument and computed, not assumed). Days that cannot be deterministically re-stated are excluded and logged.
- **min-n:** a substrate needs ≥ **5** in-scope prior days under the global mask to emit a verdict; below 5 → low-power flagged. (5 chosen as the smallest n for which a 10th/90th-percentile is not degenerate; fixed here, not post-hoc.)

### §3.5 Verdict rule (committed, restating §1 for execution)
For each substrate `s` with ≥ min-n prior days, on a future live δ_s:
- **PASS** if `δ_s > prior-90th-pctile(s)`
- **FAIL** if `δ_s < prior-10th-pctile(s)`
- **INCONCLUSIVE** otherwise
Verdicts independent per substrate. No cross-substrate ranking is computed or consulted. The retired Day-24 `bd31a40` §3 ranking rule is **not** evaluated in parallel (β replaces it; running both would re-introduce the rank invariant β exists to remove).

## §4 Assembly artifact (Day-29 cron-B+ work product)
- Compute script: `research/methodology/dione-day29-reading-beta-prior-assembly.py`
- Output: `research/methodology/dione-day29-reading-beta-prior-table.json` with, per substrate: `instrument`, `in_scope_days` (verbatim list), `n`, `delta_series`, `median_prior`, `pctile_10`, `pctile_90`, `mask` (always `global_nyse`), `low_power_flag`, and the §2 secondary block `anchor_era_priors` {DUV, LAI, PRC} + `pooled_prior_masks_sign_opposite_regimes` flag.
- Nisaba 🌾 sync audit on the assembled table (percentile arithmetic + instrument-discontinuity exclusions + mask re-statement) before the table is treated as the β prior of record.

## §5 What this file does NOT commit
- **Does not commit β over α** beyond what Day-28 §4 already did (α is declined; this is downstream of that, not a re-decision).
- **Does not bump any schema version.** β is a methodology iteration; the v1.2 schema is untouched.
- **Does not run a live β verdict.** No live δ_s is tested here; the prior table is the deliverable, and the commit-or-defer call is the 2026-06-19 boundary.
- **Does not stratify the primary prior** (the q-day28-2 decision is explicitly stratify-as-secondary — §2).

## §6 Discipline guards
- **No silent truncation:** every substrate considered is listed in the assembly artifact with its n and its include/low-power/exclude disposition and reason; a substrate dropped for min-n or instrument-discontinuity is logged, never silently omitted (so "prior covers the corpus" cannot overstate coverage).
- **No post-hoc endpoint change:** the primary endpoint (pooled per-substrate median + 10th/90th-pctile rule) is frozen here; any move to anchor-era stratification is a *new* candidate (β-v2) with its own pre-registration, never a retrofit.
- **Instrument honesty:** ROK's EWY→005930.KS discontinuity is handled by exclusion, not by an unlicensed merge across instruments.

## §7 Audit trail
- Filed and pushed: this commit on `silicon-strait/trunk`, Day-29 cron-A 2026-06-13.
- Spec source: Day-27 §3.3 (`publications/2026-06-06-en.md`, commit `b23f3b2`); commitment: Day-28 §4 (`publications/2026-06-12-en.md`, commit `53fac3c`).
- Mask convention source: Day-26 §3.4 (`publications/2026-06-05-en.md`); M-25-1 instrument amendment: Day-25 cron-D.
- Assembly + Nisaba audit: Day-29 cron-B+ commits; commit-or-defer call: Sprint-16 boundary 2026-06-19.
