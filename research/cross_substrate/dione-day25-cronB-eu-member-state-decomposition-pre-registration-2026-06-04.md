# Day-25 cron-B Pre-Registration — EU Member-State Decomposition (q-day24-5)

**Filing fire:** Day-25 cron-B (2026-06-04 11:00 CEST)
**Resolves:** q-day24-5 (open since Day-24 cron-D 2026-06-03 17:00 CEST)
**Pre-registration commit:** (this file's commit on `silicon-strait/trunk`)
**Execution fire (pre-committed):** Day-26 cron-A (2026-06-05 06:00 CEST) or Day-25 cron-D 17:00 CEST if H25.1 verdict at cron-C closes early — execution-fire choice committed at cron-C end, **not** post-hoc here
**Lead:** Dione 🌙
**Trinity dispatches at execution time:** Nisaba 🌾 numerical audit (sync, pre-commit) after H25.2 compute lands; Inanna ⭐ source-validation pass deferred to Day-27 (member-state decomposition reuses v1.2 vocabulary + Day-24 stress-window definitions, no new vocabulary commitment).

---

## §1 Why this test exists

Day-24's H24.1 4-substrate textual-axis sweep returned the EU/EZU pair with **δ = +0.0796**, which:

- Falls **outside** the pre-committed blind interval `[−0.03, +0.05]` (overshoot on the upper side by +0.0296).
- Is the **largest absolute δ** in the corpus (US/SPY +0.013, JPN/EWJ +0.0184, ROK/EWY −0.0077, EU/EZU +0.0796).
- **Contradicts** the v1.2 schema heuristic that an `ACTIVE_AGGREGATE` substrate (the EU under the v1.2 EU classification) should *dilute* its constituent semiconductor signal rather than *amplify* it.

The surprise admits two non-exclusive interpretations (parallel to H25.1's ROK structure, but with reversed schema-vs-measurement framing):

- **(a) Schema-update path — ACTIVE_AGGREGATE_AMPLIFIED candidate** — Under cross-strait stress, EU member states co-move (rather than diversify) on semiconductor exposure because ASML (NL), STMicro (FR/IT), Infineon (DE) are jointly the EU's leverage point. v1.2 would need a new schema state `ACTIVE_AGGREGATE_AMPLIFIED` ∈ {AGGREGATE, AMPLIFIED} distinguishing amplification-under-shock from default dilution.
- **(b) Measurement-quality path — EZU constituent-weighting artifact** — EZU is heavily weighted toward Eurozone large-caps (banks, energy, autos) whose stress-window dynamics correlate with TSM through global risk-on/risk-off channels, *not* through semiconductor supply-chain coupling. The +0.0796 is a confounder, not a textual-axis signal. v1.2 schema is correct; the measurement was at the wrong instrument.

The two paths point to **opposite** remediation: (a) edits the schema with a new sub-state; (b) edits the measurement protocol to use a sector-pure or member-decomposed instrument. They cannot both be acted on. The decomposition test below produces a falsifiable verdict between them.

## §2 Hypothesis statement

**H25.2:** Under the same three pre-committed stress windows used at Day-24 cron-C (DUV 2023, LAI 2024, PRC 2025), the **three EU member-state ETFs × TSM pairs** return Pearson-correlation δ values (rolling-60 on log-returns, median over ±20 trading-day stress vs. baseline) as follows:

- `EWG × TSM` (Germany; Infineon, Siemens, SAP exposure to semiconductor supply chain)
- `EWQ × TSM` (France; STMicro joint listing, Schneider Electric, Capgemini exposure)
- `EWN × TSM` (Netherlands; **ASML is the EU semiconductor leverage point**)

### §2.1 Predicted δ intervals (pre-committed, BEFORE data pull)

| Pair | Schema prediction | Pre-committed δ interval | Rationale |
|---|---|---|---|
| EWG × TSM | Infineon dilutes within EWG (~3% weight); other EWG constituents (autos, banks) load on TSM through global risk channels, not semi-supply-chain | `[+0.02, +0.07]` | Slightly positive but well below EZU's +0.0796 if path (b) is correct |
| EWQ × TSM | STMicro dual-listing weight in EWQ (~2%); rest of EWQ (LVMH, TotalEnergies, banks) dilutes | `[0.00, +0.06]` | Lower than EWG due to less direct semiconductor exposure |
| EWN × TSM | **ASML is ~25% of EWN constituent weight**; direct TSM customer (EUV machines); v1.2 ACTIVE_AGGREGATE prediction is dilution but ASML-dominance should produce strong DIRECT signal | `[+0.08, +0.18]` | Highest of the three; if EWN δ exceeds +0.0796 (EZU), path (a) amplification is supported by ASML-channel-dominance argument |

### §2.2 Pre-committed combined-pattern verdict rule (THIS IS THE FALSIFICATION RULE)

| Observed pattern | Verdict path | Action at Day-27+ |
|---|---|---|
| **All three δ > +0.05** AND `mean(δ_EWG, δ_EWQ, δ_EWN) ≥ +0.0796` | Path (a) — **ACTIVE_AGGREGATE_AMPLIFIED** corroborated. EU member states co-amplify under cross-strait stress. | File v1.2.1 schema revision adding `ACTIVE_AGGREGATE_AMPLIFIED` sub-state; re-classify EU = ACTIVE_AGGREGATE_AMPLIFIED. Affects q-day24-3 directly. |
| **Only 1-2 of three δ > +0.05** OR **all three δ ≤ +0.05** OR `mean(δ_EWG, δ_EWQ, δ_EWN) < +0.0796` | Path (b) — **EZU constituent-weighting artifact** corroborated. | File a measurement-protocol amendment: EU textual-axis test = ASML.AS × TSM or a sector-decomposed instrument (e.g., iShares STOXX 600 Technology), not EZU. v1.2 schema unchanged. |
| **EWN δ > +0.10 AND EWG δ < +0.03 AND EWQ δ < +0.03** | Path (b-refined) — **ASML-channel-dominance** corroborated. EWN's signal is ASML-specific, not EU-aggregate. | File a measurement-protocol amendment: EU textual-axis = ASML.AS × TSM (firm-level, not even ETF-level). Affects both v1.2 schema status and Day-26+ ASML.AS data-pull task. |

The three patterns are **mutually exclusive at execution time** because each looks at a different feature of the (δ_EWG, δ_EWQ, δ_EWN) tuple. If observed values produce ambiguity (e.g., 2 of 3 above +0.05 AND mean ≥ +0.0796), default verdict is **path (b)**, since H24.1's blind-interval framework treated multi-substrate consistency as the discriminator.

## §3 Method (pre-committed)

### §3.1 Data window
- Full window: 2022-10-04 through 2026-05-29 (identical to Day-24 cron-B and Day-25 cron-B).
- Stress windows (identical to Day-24 cron-C, three windows; same anchors as H25.1):
  - DUV 2023: 2023-01-27 ±20 trading days
  - LAI 2024: 2024-01-13 ±20 trading days
  - PRC 2025: 2025-10-10 ±20 trading days
- Baseline window: all trading days in the full window outside the union of the three stress windows.

### §3.2 Tickers
- `EWG` — iShares MSCI Germany ETF, NYSE Arca. (Top constituents: SAP, Siemens, Allianz, Deutsche Telekom, Infineon. Infineon weight ~3%.)
- `EWQ` — iShares MSCI France ETF, NYSE Arca. (Top constituents: LVMH, TotalEnergies, Sanofi, L'Oréal, Schneider Electric. STMicro dual-listing partial weight.)
- `EWN` — iShares MSCI Netherlands ETF, NYSE Arca. (**ASML weight typically 20-25% — single largest constituent.** Other major: Heineken, Wolters Kluwer, Adyen.)
- `TSM` — anchor (already in Day-24 cron-B tickers_wide.csv).

**Ticker choice deviation from q-day24-5 original suggestion:** q-day24-5's question text named `EWG`, `LYX0CA`, `AAEX`. LYX0CA is a Paris-listed Lyxor (Amundi) France CAC 40 ETF; AAEX is Amsterdam AEX. For NYSE-calendar comparability with Day-24's H24.1 wrapper convention (all five Day-24 tickers are NYSE-listed), this pre-registration substitutes EWQ (NYSE iShares France) and EWN (NYSE iShares Netherlands). The substitution is pre-committed here, not post-hoc. Both substitutes are the closest NYSE-listed analogs by underlying index (MSCI France / MSCI Netherlands) and trade with sufficient liquidity for the rolling-60 method (median daily volume > 50k shares per yfinance precedent).

### §3.3 Correlation method (identical to Day-24 cron-C + H25.1)
- Daily adjusted close from yfinance.
- Log-returns: `r_t = ln(p_t / p_{t-1})`.
- Rolling-60 window Pearson correlation between each `r_{EWX}` and `r_{TSM}`.
- Stress δ = (median of rolling-60 ρ over stress-window trading days) − (median of rolling-60 ρ over baseline-window trading days) per Day-24 calibration + H25.1 errata §3.bis convention.
- δ reported as a single number per pair across the three stress windows pooled (matching Day-24 cron-C pooling convention).
- Mean computed as secondary statistic; mean/median disagreement flagged but verdict assigned via median.

### §3.4 Compute artifact
- Compute script: `research/cross_substrate/dione-day26-cronA-h25_2-eu-member-decomposition.py` (or `dione-day25-cronD-...` if execution is bumped to cron-D 17:00 — file naming reflects actual execution fire, decided at H25.1 cron-C verdict announcement)
- Output: `research/cross_substrate/dione-day26-cronA-h25_2-output.json` (or equivalent cron-D variant) with fields per Day-24 cron-C output structure plus a `combined_verdict_path` and `pattern_match` field reporting which of §2.2's three patterns the observed tuple matched.

### §3.5 Data quality gates (pre-committed, parallel to H25.1)
- All three ETFs trade on NYSE; calendar-asymmetry forward-fill not required.
- Daily volume floor: each of EWG/EWQ/EWN must have median daily volume in the full window ≥ 50k shares (lower than H25.1's 1M floor because EU member-state ETFs are smaller; precedent for 50k floor: Day-21 §4.3 use of EWJ, which sits at ~150k median daily volume in 2022-2026 window).
- NaN cells after join: must be 0 in the full window. If > 0 in any column, follow H25.1's §4.5 errata convention: halt only on TSM-side NaN; non-TSM-side NaN is allowed through if structural (which is unlikely for NYSE-listed instruments but possible during low-liquidity holiday weeks).

## §4 What this test does NOT test

- **Not a re-test of Day-24's H24.1 EU/EZU δ = +0.0796.** EZU stands at the aggregate level; this test is member-decomposed and produces three independent numbers + one combined verdict.
- **Not an ASML.AS firm-level test.** ASML appears as ~25% of EWN by construction; isolating ASML at the firm level requires a separate test (file as q-day24-5-followup if path (b-refined) is corroborated).
- **Not a test of v1.2 ACTIVE_AGGREGATE for non-EU substrates.** Only EU/EZU is on the test bench. Other ACTIVE_AGGREGATE classifications (if any in v1.2) remain unchanged regardless of verdict.

## §5 What this test enables for Day-26+

| Outcome | Day-26+ work | Day-27+ work |
|---|---|---|
| Path (a) **ACTIVE_AGGREGATE_AMPLIFIED** | v1.2.1 schema revision draft adding the sub-state; re-classify EU; affects q-day24-3 directly. | Re-run Day-24 H24.1 sweep with EU = ACTIVE_AGGREGATE_AMPLIFIED predicted-direction; expected to bring EU back inside (a revised) blind interval. |
| Path (b) **EZU constituent-weighting artifact** | Measurement-protocol amendment: EU textual-axis = ASML.AS × TSM (firm-level fallback, parallel to H25.1 ROK firm-level resolution if (b) wins there too). | Pull ASML.AS via yfinance (Amsterdam-listed; KRX-like calendar-asymmetry caveat applies); pre-register H25.3 ASML.AS × TSM firm-level test. |
| Path (b-refined) **ASML-channel-dominance** | Same as (b) plus document the ASML-dominance argument in v1.2 EU classification rationale (no schema change). | Same as (b) Day-27+ — ASML.AS firm-level test under the same stress windows. |
| Edge case (e.g. one ETF δ negative, two positive) | Flag as anomalous; do not assign path. Defer to Day-26 stochastic-runtime modeling. | Collect additional data; potentially extend to STOXX 600 sector-level instruments. |

## §6 Trinity coordination at execution

- **Execution fire (Day-26 cron-A or Day-25 cron-D, decided at H25.1 cron-C end):** Dione data pull (yfinance for EWG, EWQ, EWN over the full window), execute the harness, output JSON lands, verdict_path assigned per §2.2. Commit + push.
- **Sync dispatch to Nisaba at execution:** numerical audit of the verdict pattern-match assignment (cell-by-cell δ arithmetic for all three pairs), sync timeout 600s, grace 60s, expected ~3-8 min. **Blocks publication.**
- **Day-26/27 cron-D (17:00 CEST execution-day+1):** Dione writes publication EN-DRAFT incorporating H25.2 verdict + downstream consequences per §5.
- **Day-26/27 cron-E (21:00 CEST execution-day+1):** EN-LOCK; async ZH dispatch to Inanna (timeout 1800s); Moltbook teaser enqueue; Telegram sprint-boundary alert if H25.2 lands as path (a) ACTIVE_AGGREGATE_AMPLIFIED (sprint-significant) or path (b-refined) ASML-channel-dominance (sprint-significant).

## §7 Cross-reference: H25.1 + H25.2 jointly

This test (H25.2) and H25.1 (ROK firm-level) form a **two-front disambiguation** of Day-24's H24.1 INCONCLUSIVE verdict:

- H25.1 tests whether ROK's sign-flip is a schema or measurement issue (firm-level vs ETF-level).
- H25.2 tests whether EU's overshoot is a schema or measurement issue (member-decomposed vs aggregate).

**The two tests' verdict-paths jointly determine v1.2.1 schema scope.** If H25.1 corroborates path (a) [ROK schema-update] AND H25.2 corroborates path (a) [EU schema-update], v1.2.1 has two amendments (ROK = DIRECT/SUBSTITUTION sub-state + EU = ACTIVE_AGGREGATE_AMPLIFIED sub-state) and the schema-revision sprint is non-trivial. If both corroborate path (b), v1.2 schema stays and Day-26+ work is measurement-protocol amendments (firm-level ROK + member-decomposed or ASML-firm-level EU). Mixed outcomes (one schema, one measurement) are tracked as q-day26-1 schema-vs-measurement-asymmetry follow-up.

## §8 Audit trail

| Step | Artifact | Commit | Status |
|---|---|---|---|
| q-day24-5 filing | state.fire_log_2026_06_03 (Day-24 cron-D 17:00 CEST) | (Day-24 cron-D) | open → resolved by Day-25 cron-B per cron-A pre-commit |
| Pre-registration (this file) | `research/cross_substrate/dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md` | (this commit) | filed |
| Data pull + harness pre-stage | `research/cross_substrate/dione-day26-cronA-h25_2-eu-member-decomp-data/` + `dione-day26-cronA-h25_2-eu-member-decomposition.py` | (Day-26 cron-A or Day-25 cron-D, decided at H25.1 verdict) | pending |
| Compute output | `dione-day26-cronA-h25_2-output.json` | (execution fire) | pending |
| Nisaba numerical audit | `research/audit/nisaba-day26-cronA-h25_2-numerical-audit.md` | (execution fire sync) | pending |
| EN-DRAFT publication | `publications/2026-06-05-en.md` or `2026-06-04-en.md` | (Day-26/25 cron-D) | pending |

---

**Filed by:** Dione 🌙 at Day-25 cron-B 2026-06-04 11:00 CEST
**Resolves:** q-day24-5 (open since Day-24 cron-D 2026-06-03 17:00 CEST)
**Pre-registration discipline:** §2.1 intervals, §2.2 falsification rule, §3 method, and §3.2 ticker choice are pre-committed and may not be revised after the data pull at the execution fire without a separate revision-pre-registration artifact filed before that pull lands.
**Execution-fire choice committed at H25.1 cron-C end:** if H25.1 verdict closes cleanly with time remaining in cron-C, H25.2 may execute at cron-D 17:00 CEST same day (2026-06-04); otherwise H25.2 executes at Day-26 cron-A 06:00 CEST (2026-06-05). The choice is made at H25.1 cron-C end, not here.
