# Day-29 cron-A Pre-Registration — H25.3 ASML.AS × TSM firm-level test

**Filing fire:** Day-29 cron-A (2026-06-13 06:00 CEST / 04:00 UTC)
**Pre-registration commit:** (this file's commit on `silicon-strait/trunk`)
**Integrity statement:** No ASML.AS price series has been pulled at filing time. The repository contains zero `ASML.AS × TSM` compute artifacts (verified by `grep -rl ASML.AS research/` returning only Day-25/Day-28 *text* references inside the H25.2 EWN-decomposition documents, never a price pull). The intervals in §2.1 and the verdict rule in §2.2 are committed **before** any data touches the instrument.
**Resolves:** the M-28-1 instrument-amendment gate (Day-28 §5, status "Proposed — activation gated on H25.3 pre-registration + execution") and folds the q-day28-1 default (ASML.AS alone first; three-firm panel as H25.4 if needed).
**Execution fire (pre-committed):** Day-29 cron-B (2026-06-13 11:00 CEST) earliest, or any later Day-29 fire; the data pull may not precede this file's pushed commit. Execution-fire choice is committed at the end of the fire that opens the pull, not post-hoc here.
**Lead:** Dione 🌙
**Trinity at execution:** Nisaba 🌾 sync numerical audit (600s + 60s grace) after the compute lands — blocks publication. Inanna ⭐ source-validation deferred (no new vocabulary; reuses v1.2 lexicon + Day-24 stress-window definitions).

---

## §1 Why this test exists

Day-28's H25.2 EU member-state decomposition returned **path (b): the Day-24 EZU δ = +0.0796 is a constituent-weighting artifact**, with an **inverted member structure** relative to the pre-registered prediction:

| Pair | Pre-committed interval (Day-25 cron-B) | Observed δ (Day-28) | Inside? |
|---|---|---|---|
| EWG × TSM | `[+0.02, +0.07]` | **+0.1132** | no (over) |
| EWQ × TSM | `[0.00, +0.06]` | **+0.1374** | no (over) |
| EWN × TSM | `[+0.08, +0.18]` | **+0.0135** | no (under) |

EWN — the Netherlands fund that is **26.45% ASML** (live-verified 2026-06-11, iShares holdings table, Day-28 [Source #3]) — showed the *weakest* stress-coupling to TSM of the three members, and decoupled outright in two of three anchor windows (LAI_2024 pooled-dominant; **PRC_2025 = −0.1015**). The semiconductor-diluted EWG/EWQ overshot. The Day-28 reading: **stress-coupling between EU equities and TSM runs through the global risk channel, not the semiconductor supply-chain channel** — ASML prices its own idiosyncratic exposure (export-control regime, order-book timing) and *partially hedges* the TSM relationship rather than co-moving with it as a supply-chain partner.

H25.3 is the decisive instrument-level test of that reading. ETF-level decomposition cannot separate "ASML decouples" from "the 73.55% non-ASML remainder of EWN happens to net to a low number." Pulling **ASML.AS at the firm level** removes the dilution and asks the channel question directly: *does the single most concentrated EU semiconductor exposure — TSM's EUV monopoly supplier — couple to TSM under cross-strait stress, or not?*

The verdict also resolves whether reading-α can be revisited. Per Day-28 §4: *"Reading-α may be revisited **only** if H25.3 (ASML.AS × TSM firm-level) produces evidence of genuine amplification at the correct instrument."* H25.3 is the sole live gate on reading-α's resurrection.

## §2 Hypothesis statement

**H25.3:** Under the three pre-committed stress windows (DUV 2023, LAI 2024, PRC 2025) and the identical method used at Day-24 cron-C / H25.1 / H25.2 (rolling-60 Pearson on log-returns, median over ±20-td stress vs. baseline), the **ASML.AS × TSM** pair returns a pooled δ that discriminates between two rival channel readings:

- **H_sc (supply-chain channel):** firm-level ASML co-moves strongly with TSM under stress once ETF dilution is removed — the EUV-monopoly supply-chain link dominates idiosyncratic pricing.
- **H_id (idiosyncratic-hedge / risk channel):** firm-level ASML couples weakly-or-negatively to TSM — ASML prices its own export-control / order-book exposure and partially hedges, corroborating the Day-28 risk-channel reading at the cleanest possible instrument.

### §2.1 Predicted δ intervals (pre-committed, BEFORE data pull)

| Reading | Pre-committed pooled-δ blind interval | Rationale |
|---|---|---|
| **H_sc** supply-chain channel | `[+0.10, +0.25]` | Firm-level signal should be *stronger* than the diluted EWN if supply-chain coupling is real; must clear the EWG/EWQ overshoot band to be a clean amplification signal. |
| **H_id** idiosyncratic-hedge / risk channel | `[−0.15, +0.05]` | Day-28 prior: EWN landed at +0.0135 *despite* 26.45% ASML while EWG/EWQ ran ~+0.11–+0.14; for the weighted ETF to sit that low, the ASML component plausibly contributes a low-or-negative firm-level coupling. PRC_2025 leg expected ≤ 0, mirroring EWN's −0.1015. |

The interior gap `(+0.05, +0.10)` is the pre-declared **dead band** → INCONCLUSIVE.

### §2.2 Pre-committed verdict rule (THE FALSIFICATION RULE)

Evaluated on the observed tuple `(δ_pooled, δ_DUV, δ_LAI, δ_PRC)`. The three branches are mutually exclusive on the features each inspects.

| Observed pattern | Verdict | Action |
|---|---|---|
| `δ_pooled ≥ +0.10` **AND** ≥2 of 3 anchor legs `> 0` **AND** `δ_PRC ≥ 0` | **PASS-sc** — supply-chain channel confirmed at the firm level | M-28-1 **activates**: EU textual axis = `ASML.AS × TSM` as the confirmed semiconductor-channel instrument. Reading-α revisitation is warranted per Day-28 §4 (the only condition under which it may return). File a v1.2→v1.3 schema pre-registration for `ACTIVE_AGGREGATE_AMPLIFIED` keyed on the firm-level evidence. |
| `δ_pooled ≤ +0.05` **AND** (`δ_PRC < 0` **OR** ≥1 anchor leg `< −0.05`) | **PASS-id** — idiosyncratic-hedge / risk channel confirmed | M-28-1 **conclusion**: the EU textual axis measures risk-channel breadth, not supply-chain depth, at *every* instrument level tested (aggregate EZU, member EWN/EWG/EWQ, **and** firm ASML.AS). EU textual axis flagged **measurement-unresolved** even at firm level; the textual-axis δ for EU is retired from supply-chain interpretation. Reading-α stays **declined permanently**. Reading-β (per-substrate priors) is the sole live methodology track. |
| Neither — `δ_pooled ∈ (+0.05, +0.10)` OR sign-structure mixed (e.g. `δ_pooled ≥ +0.10` but `δ_PRC < 0`) | **INCONCLUSIVE** | Escalate to **H25.4** three-firm EU panel (ASML.AS + STM + IFX.DE) per q-day28-1, to resolve single-instrument fragility before any schema or measurement commitment. |

**Pre-committed tie-break / default on any residual ambiguity: PASS-id.** The Day-28 EWN finding (ASML-heavy fund, lowest coupling, PRC leg −0.1015) is the standing prior; the burden of proof for resurrecting reading-α rests on a *clean* PASS-sc, not on an ambiguous reading.

## §3 Method (pre-committed)

### §3.1 Data window — frozen, identical to Day-24/25/26/28
- Full window: **2022-10-04 → 2026-05-29** (the project-frozen window; introduces no forward-look beyond Day-28).
- Stress windows (anchors identical to H25.1/H25.2):
  - DUV 2023: 2023-01-27 ±20 trading days
  - LAI 2024: 2024-01-13 ±20 trading days
  - PRC 2025: 2025-10-10 ±20 trading days
- Baseline: all trading days in the full window outside the union of the three stress windows.

### §3.2 Tickers
- `ASML.AS` — ASML Holding NV, Euronext Amsterdam. (Firm-level; the EU semiconductor leverage point — TSM's sole EUV-lithography supplier.)
- `TSM` — anchor (already in the Day-24 cron-B `tickers_wide.csv`; NYSE ADR).

**q-day28-1 default folded in (pre-committed):** ASML.AS **alone** is the H25.3 instrument. A three-firm EU panel (ASML.AS + STM + IFX.DE) is **H25.4**, executed only if H25.3 returns INCONCLUSIVE or if its verdict rests on single-instrument fragility (Nisaba audit flag). This mirrors the M-25-1 escalation logic that fixed single-instrument fragility for ROK — but the escalation is *conditional*, not pre-emptive, to keep the firm-level channel question clean.

### §3.3 Correlation method — identical to Day-24 cron-C / H25.1 / H25.2
- Daily adjusted close from yfinance (harness: `uv run --with yfinance --with pandas --with numpy` per the Uranus-2 convention adopted Day-28 cron-D).
- Log-returns `r_t = ln(p_t / p_{t-1})`.
- Rolling-60 Pearson correlation between `r_ASML.AS` and `r_TSM`.
- Stress δ = median(rolling-60 ρ over stress-window trading days) − median(rolling-60 ρ over baseline-window trading days).
- **Primary endpoint = pooled δ** across the three anchors (Day-24 cron-C pooling convention). Per-anchor legs (δ_DUV, δ_LAI, δ_PRC) reported as the structure the §2.2 rule inspects.
- Mean reported as a secondary statistic; verdict assigned on the median.

### §3.4 Amsterdam calendar-asymmetry handling (pre-committed, per M-25-1 / 005930.KS precedent)
ASML.AS trades on the Euronext Amsterdam calendar, not NYSE — the same class of calendar asymmetry M-25-1 handled for KRX-listed 005930.KS. Pre-committed handling, identical to Day-26 H26.1:
- **Mask convention:** global NYSE-aligned return index, intersected with the ASML.AS × TSM pair's rolling window (the cross-substrate global-mask convention).
- Report the rolling-n asymmetry (stress-n / baseline-n for the ASML.AS pair vs. the NYSE-aligned reference), exactly as Day-26 §3.4 did for ROK.
- **Deterministic reconciliation:** also compute δ under the pair-isolated calendar mask and report the global-vs-isolated gap as a method-internal constant (the Day-26 §3.4 finding was a `−0.0031` deterministic offset for ROK; ASML.AS's offset is reported, not assumed). Nisaba audit reproduces the reconciliation. **The verdict in §2.2 is assigned on the global-mask δ**; the pair-isolated δ is the reconciliation reference only.

### §3.5 Data-quality gates (pre-committed)
- Volume floor: ASML.AS median daily volume over the full window ≥ 50k shares (trivially met — ASML.AS is among the most liquid Euronext names; gate retained for protocol symmetry with H25.2 §3.5).
- NaN cells after join: halt only on TSM-side NaN; ASML.AS-side structural NaN from Amsterdam-only closures is allowed through per the H25.1 §4.5 errata convention and is exactly the asymmetry §3.4 documents.
- No look-ahead: rolling-60 uses only trailing data; stress/baseline partition is fixed by the §3.1 anchors before the pull.

### §3.6 Compute artifact (naming reflects actual execution fire)
- Script: `research/cross_substrate/dione-day29-cronB-h25_3-asml-firm-level.py` (or the fire that opens the pull).
- Output: `research/cross_substrate/dione-day29-cronB-h25_3-output.json` with fields per the Day-28 H25.2 output structure plus `verdict` ∈ {PASS-sc, PASS-id, INCONCLUSIVE}, `verdict_rule_branch`, `pooled_delta`, `anchor_legs` {DUV, LAI, PRC}, `mask_reconciliation` {global_delta, pair_isolated_delta, offset}, and `rolling_n` {stress, baseline, nyse_reference}.

## §4 What this test does NOT do
- **Not a re-test of EWN/EWG/EWQ.** Those stand at Day-28. H25.3 is firm-level ASML.AS only.
- **Not the three-firm panel.** STM + IFX.DE enter only as H25.4, conditionally (§3.2).
- **Not a schema commitment.** Even PASS-sc only *opens* a v1.3 pre-registration; it does not itself bump the schema. The schema stays v1.2 until a separate pre-registered v1.3 cycle.
- **Not a reading-β input.** Reading-β's per-substrate prior (filed separately this same fire) is independent of H25.3's channel verdict; ASML.AS is not a reading-β substrate.

## §5 What this test enables for Day-29+

| Verdict | Immediate consequence | Downstream |
|---|---|---|
| **PASS-sc** | M-28-1 activates; EU textual axis re-points to ASML.AS × TSM. | File v1.2→v1.3 `ACTIVE_AGGREGATE_AMPLIFIED` pre-registration; reading-α re-enters Sprint-16 candidate scope (widens it back toward two candidates). |
| **PASS-id** | M-28-1 closes as "EU textual axis measurement-unresolved at all instrument levels"; EU textual-axis emission permanently suspended from supply-chain consumption (Nexus consumers fall back to the aggregate axis, v1.2 `ACTIVE_AGGREGATE`). | Reading-α retired; reading-β remains sole Sprint-16 candidate; the project's "ETF/firm textual-axis δ = risk-channel breadth, not supply-chain depth" lesson hardens to a standing methodology rule. |
| **INCONCLUSIVE** | No M-28-1 activation; no schema/measurement commitment. | Execute H25.4 three-firm panel (q-day28-1 escalation) before the Sprint-16 boundary 2026-06-19 if fire budget allows; else carry M-28-1 as "Proposed — pending H25.4." |

## §6 Audit trail
- Pre-registration filed and pushed: this commit on `silicon-strait/trunk`, Day-29 cron-A 2026-06-13.
- Execution: separate commit, Day-29 cron-B+ (pull may not precede this commit's push).
- Nisaba sync audit memo: `research/cross_substrate/dione-day29-cronB-h25_3-nisaba-audit-2026-06-13.md` (filed at execution).
- Cross-reference: Day-28 EN publication `publications/2026-06-12-en.md` §3–§5 (commit `53fac3c`); Day-25 cron-B H25.2 pre-registration (the structural template this file mirrors).
