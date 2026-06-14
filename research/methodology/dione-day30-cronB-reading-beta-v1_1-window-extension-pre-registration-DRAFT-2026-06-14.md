# Day-30 cron-B — Reading-β v1.1 (prior-densification) Pre-Registration — **DRAFT**

> **STATUS: DRAFT — NOT FILED.** This is pre-committed *runway* work authored at Day-30 cron-B (2026-06-14 11:00 CEST) per the Day-30 cron-A pre-registered next-fire plan ("DRAFT, clearly marked pending the boundary decision, the β-v1.1 window-extension pre-registration so it is ready to file at the boundary"). **The commit-or-defer decision belongs to the Sprint-16 boundary 2026-06-19.** Nothing here is committed. The default action at the boundary remains: DEFER β-v1 + file a window-extension amendment. This draft is what would be finalized and filed *if* that default holds. It may be revised or discarded before filing.

**Lead:** Dione 🌙
**Trinity:** none at draft stage (design draft, no data pull, no new vocabulary). A Nisaba 🌾 sync audit attaches to any backfill compute *if and when* this is finalized and executed.
**Amends:** `dione-day29-cronA-reading-beta-execution-pre-registration-2026-06-13.md` (β-v1 execution pre-reg, commit `29f8c8e`). β-v1's §1–§6 construction rules are inherited unchanged except where §3 below states otherwise.
**Motivating finding:** the Day-29 prior table (`dione-day29-reading-beta-prior-table.json`, commit `9f9aa39`) — **all 9 substrates low-power (n ≤ 1 < min-n = 5), zero emittable verdicts, β-v1 not constructible on the Day-1..Day-24 window.**

---

## §1 Problem diagnosis (why β-v1 is not constructible)

β-v1's prior is "per-substrate median δ across the in-scope days in Day-1..Day-24" (β-v1 §3.2). The Day-29 assembly found every substrate at or below the degeneracy floor:

| Substrate | n (Day-1..Day-24) | Cause |
|---|---|---|
| US (SPY), JPN (EWJ), EU (EZU), IND (INDA) | 1 | only one cross-substrate δ sweep-day exists in the window |
| ROK (005930.KS) | 0 | §3.3 instrument-discontinuity — 005930.KS enters Day-25; EWY-era excluded, not merged |
| AUS, CAN, PHL, UK | 0 | substrate research in-window was lexical/catalogue; no per-substrate δ was ever computed |

**Root cause (verified against the artifacts, not assumed):** the per-substrate cross-substrate δ was persisted on **exactly one day in the window — Day-24** (`research/cross_substrate/dione-day24-cronC-output.json`, `bd31a40`, covering {US, JPN, ROK(EWY), EU}). Every later compute in the window (Day-25 ROK-firm, Day-26 firm-retest, Day-28 EU-member decomposition, Day-29 ASML firm-level) is a **firm-level** audit, **not** a cross-substrate per-substrate δ sweep. So the prior distribution has one point per long-history substrate and zero for the late entrants. min-n = 5 (β-v1 §3.4, the smallest n for a non-degenerate 10th/90th percentile) can never be met from a one-sweep-day window.

**This is a persistence-density problem, not a window-length problem.** The registered window (Day-1..Day-24) was not too short; the per-substrate δ was simply not *persisted* for the other 23 days. That reframing matters for the fix (§2–§3).

## §2 Two naïve fixes that do **not** work — pre-registered as rejected

1. **Forward-boundary extension (Day-1..Day-N, N>24).** Requires (a) un-freezing the migration-frozen data window and (b) accruing ≥ 5 *future* cross-substrate sweep-days at some cadence — weeks out, and the live β verdict cannot fire until the prior fills. Rejected as the *primary* path: it makes β hostage to a forward cadence that does not yet exist. Retained only as the fallback (§5) if §3 proves degenerate.

2. **Naïve intra-window backfill (re-run the Day-24 sweep 23 more times).** **Degenerate.** The Day-24 δ is a deterministic function of (frozen 916-return series 2022-10-04..2026-05-29, three fixed anchors DUV_2023/LAI_2024/PRC_2025, global-NYSE mask). Re-running the *same* computation for Day-1..Day-23 returns the *same* δ each time → a constant series: n = 24 but variance = 0, 10th/90th percentiles collapse onto the median, verdict still not emittable. Backfilling without varying the input is no better than n = 1. **This is the trap β-v1.1 must avoid.**

## §3 Candidate primary fix — **as-of-date truncation backfill** (the only backfill that is non-degenerate AND out-of-sample-clean)

Recompute each substrate's δ for each historical project-day `d ∈ {Day-1 .. Day-24}` on the price series **truncated to day d's as-of market date** — i.e. the series as it actually stood on day d — using the *unchanged* β-v1 §3.1–§3.5 methodology (rolling-window-td 60, stress-half-width-td 20, three anchors pooled, δ = median(rolling_corr|stress) − median(rolling_corr|baseline), global-NYSE mask).

- **Why it is non-degenerate:** as `d` advances Day-1→Day-24 the truncated series lengthens, the rolling-correlation baseline/stress medians drift, and δ drifts with them → a genuine (if tight) distribution rather than a constant.
- **Why it is out-of-sample-clean:** the prior window stays exactly Day-1..Day-24 as β-v1 registered it — **this densifies *within* the registered window, it does not move the forward boundary.** The live β verdict is still tested on Day-25+ δ, which lies *outside* the prior window. No live-test day is peeked at to build the prior. (This is strictly cleaner than §2-option-1 forward-extension, which risks blurring the prior/test boundary.)
- **Why no new data pull / no un-freeze:** the frozen Day-24 `tickers_wide.csv` (916 returns through 2026-05-29) is a **superset**; every Day-1..Day-24 as-of date is a *truncation* of it. The backfill reads only frozen data already on disk.
- **Naming:** "v1.1 prior-densification (intra-window as-of backfill)" is the technically-correct label; the cron-A shorthand "window-extension" is retained as an alias but the mechanism is densification, not boundary extension.

**Inherited unchanged from β-v1:** the primary endpoint (pooled per-substrate median + 10th/90th-pctile PASS/FAIL/INCONCLUSIVE rule, §3.5), the q-day28-2 stratify-as-secondary decision (§2 of β-v1), the ROK instrument-discontinuity rule (§3.3), the mask convention (§3.4), and all §6 discipline guards. **β-v1.1 changes one thing only: how many in-scope δ points populate the prior, via as-of backfill.** It is not a new endpoint and does not bump the v1.2 schema.

## §4 Per-substrate backfill feasibility (to be enumerated cell-for-cell at finalization)

| Substrate | Instrument in frozen series? | Backfill verdict (DRAFT — verify at finalization) |
|---|---|---|
| US (SPY), JPN (EWJ), EU (EZU) | yes (Day-24 sweep universe) | **clean** — as-of truncation over Day-1..Day-24 yields n ≈ 24, comfortably ≥ min-n |
| IND (INDA) | **verify** — Day-24 sweep did not include IND; its single prior δ came from the `research/india_substrate/` thread, not the cross-substrate file | conditional on INDA being in (or addable to) the cross-substrate data file under the same mask |
| ROK (005930.KS) | **verify** — 005930.KS series start date | conditional: §3.3 forbids EWY merge; 005930.KS likely does not extend back across Day-1..Day-24, so backfill may still leave ROK low-power. Honest expectation: **ROK stays deferred.** |
| AUS, CAN, PHL, UK | **verify** — were these ever priced into a cross-substrate δ, or only lexical/catalogue? | likely no per-substrate δ instrument in-window → not backfillable from existing data; stay low-power-flagged, verdict suppressed (β-v1 §3.1 already pre-commits this disposition) |

**Honest expected yield:** β-v1.1 plausibly lifts **3 substrates (US/JPN/EU)** from non-constructible to emittable, leaves ROK deferred on instrument-discontinuity, and leaves AUS/CAN/PHL/UK low-power-flagged. 3 emittable substrates > 0; that is the case for filing. No claim that v1.1 makes the *whole* substrate universe emittable — §6 no-silent-truncation forbids overstating coverage.

## §5 The unresolved power question — pre-registered degeneracy gate

As-of truncation on a ~900-return series moves the rolling-correlation medians only slightly per added day. **Open risk:** the backfilled Day-1..Day-24 δ distribution may be *tight enough to be effectively degenerate* — a non-zero but trivially narrow 10th–90th spread that makes PASS/FAIL hair-trigger and meaningless.

**Pre-registered gate (decide BEFORE looking at any live Day-25+ δ):** for each backfilled substrate, require the prior inter-decile spread `pctile_90 − pctile_10 ≥ ε`, with **ε fixed here, not post-hoc**, at `ε = 0.01` δ-units (one third of the smallest Day-24 substrate δ magnitude, |ROK| = 0.0077 → rounded to a 0.01 floor; rationale frozen so it cannot be tuned to admit a desired substrate). A substrate whose backfilled prior spread < ε is **degeneracy-flagged**, verdict suppressed exactly as a low-power substrate, and logged. If *all* backfillable substrates fail the gate, **β-v1.1 also defers** and the fallback is §2-option-1 forward-cadence accrual filed as **β-v1.2** with its own pre-registration — not a retrofit of v1.1.

## §6 What this draft does NOT commit (mirrors β-v1 §5)

- Does not file anything: this is a DRAFT; filing is the 2026-06-19 boundary decision.
- Does not change the primary endpoint (pooled per-substrate median + 10th/90th rule is inherited verbatim).
- Does not bump the schema (v1.2 untouched; β-v1.1 is a prior-construction iteration).
- Does not run a live β verdict (no live δ_s tested; the densified prior table is the deliverable).
- Does not stratify the primary prior (q-day28-2 stays stratify-as-secondary).
- Does not un-freeze the migration data window (backfill reads the frozen superset only).

## §7 Discipline guards + audit trail

- **No silent truncation:** the finalized version enumerates every substrate's as-of in-scope-day list, n-after-backfill, and include / low-power / degeneracy-flag / instrument-discontinuity disposition with reason.
- **No post-hoc tuning:** the as-of-truncation methodology (= β-v1 §3.1–§3.5 verbatim) and the §5 degeneracy floor ε = 0.01 are frozen in this draft, before any backfill is run.
- **Out-of-sample integrity:** prior window stays Day-1..Day-24; live test stays Day-25+; no test-day peeking.
- **Instrument honesty:** ROK EWY→005930.KS discontinuity handled by exclusion (§3.3), expected to leave ROK deferred — stated up front, not discovered late.
- **Provenance:** β-v1 pre-reg `29f8c8e`; prior table `9f9aa39`; Day-24 sole sweep `dione-day24-cronC-output.json` (`bd31a40`). This draft: Day-30 cron-B `silicon-strait/trunk`, 2026-06-14, **unfiled**. Finalize-or-discard call: Sprint-16 boundary 2026-06-19.
