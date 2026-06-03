# Day-24 Textual-Axis Sweep — cron-A Scoping

**Author:** Dione 🌙
**Fire:** 2026-06-03 06:00 cron-A (Day-24, Asia-close window)
**Phase:** scoping (Day-23 archive → Day-24 scoping)
**Track:** substrate-extension (bilingual EN+ZH; methodology track closed at Day-23 cron-E commit `10381e9`)
**Predecessor:** `research/methodology/dione-day23-cronE-v12-vocabulary-lock-2026-06-02.md` (schema v1.2 promoted) — pre-registers KR EWY × TSM textual-axis pair forward-test
**Successor target:** Day-24 cron-D EN-DRAFT 17:00 CEST → cron-E EN-LOCK 21:00 CEST → Inanna ZH async dispatch
**Status:** SCOPING — design pre-registration; no analytic claims; not a publication input by itself.

---

## §0 — Step 0.5 reconcile result

| Field | Value |
|---|---|
| `in_flight` dispatches at fire-open | **0** |
| reconciliation action | none required |
| rationale | Day-23 cron-E closed methodology track EN-only; no async ZH dispatch outstanding. Last Inanna dispatch `648ab0cb` already reconciled at Day-23 cron-A as `delivered_reply_only` with Path-A Dione-direct 3-fire fallback executed Day-22 cron-A/B/C. Last Nisaba dispatch was Day-21 cron-D `f03c66a` reproduction audit (commit landed). |

## §1 — Default resolutions: q-day23-4 / q-day23-5 / q-day23-6

All three open questions filed at Day-23 cron-E carry default trigger time **Day-24 cron-A 2026-06-03 06:00 CEST** = NOW. No Ingo override received overnight; defaults trigger per pre-registration discipline.

| ID | Question | Default | Resolution at this fire |
|---|---|---|---|
| q-day23-4 | `strategic_autonomy_constraint` ACTIVE_AGGREGATE for EU (substrate-aggregate) vs per-member-state layer with separately-modeled EU meta-substrate | ACTIVE_AGGREGATE at substrate level | **RESOLVED** — proceed with ACTIVE_AGGREGATE for EU Row in v1.2 schema; per-member-state layer deferred to Day-25+ if Day-24 EZU × TSM δ shows aggregation-dilution evidence |
| q-day23-5 | Hassaleh-Nexus Sprint-15 ticket scope: extend in-sprint with v1.2 schema-migration vs push to Sprint-16 | extend in-sprint | **RESOLVED** — file engineering ticket at Day-24 cron-D scope: (a) instrument-node `axis ∈ {textual, operational}` property, (b) substrate-node `coupling_textual` + `coupling_operational` properties, (c) cross-substrate triple-edge encoding. Ticket text drafted at cron-D, filed at cron-E. |
| q-day23-6 | Day-24 cron-A forward-test ticker set: ROK EWY × TSM only vs 4-substrate textual-axis sweep (SPY + EWJ + EWY + EZU × TSM) single fire vs sequenced Day-24/25/26 | 4-substrate textual-axis sweep in single fire | **RESOLVED** — 4-substrate sweep; populates H21.1c orthogonality table from §4.4 of Day-23 methodology doc in single empirical fire (Day-24 cron-C analytic), enables clean cross-substrate ordering test at cron-D EN-DRAFT |

## §2 — Day-24 publication architecture

**Title (provisional):** Silicon Strait — Day 24: textual-axis sweep — H24.1 4-substrate ordering test on schema v1.2

**Track:** substrate-extension (bilingual EN+ZH per Day-19/20/21/22 precedent)

**Sections (pre-registered):**

1. §1 — v1.2 textual-axis-pair methodology recap (~600w; cite Day-23 methodology doc, no re-derivation)
2. §2 — Pre-registered hypotheses (H24.1 ordering, blind intervals per substrate, falsification rules) (~800w)
3. §3 — Data pull (4 textual-axis pairs × stress windows); citation tables (~1200w)
4. §4 — H24.1 analytic test (Python correlation matrix, ordering verdict, per-substrate δ vs blind interval) (~1500w)
5. §5 — H21.1c orthogonality test (Pearson(δ_textual, δ_operational) across substrate corpus) (~800w)
6. §6 — GWW3 predicate impact (P29.3 / P30.3 falsifiability assessment under Day-24 empirical readings) (~600w)
7. §7 — Hassaleh-Nexus instrument-graph update (axis property + ETF nodes) — feeds Sprint-15 ticket (~700w)
8. §8 — Sources (~25-30 entries)

**Target length:** ~6200 words EN; line-parity ~1.005:1 expected for ZH per Day-22 precedent.

## §3 — Pre-registered blind intervals and H24.1 ordering hypothesis

### §3.1 — Substrate × ticker matrix

| Substrate | Schema v1.2 classification | textual-axis pair | Pre-registered blind δ interval | Pre-reg fire (commit) |
|---|---|---|---|---|
| US | A.1 canonical / `coupling_textual=INDIRECT` / `autonomy=DORMANT` | SPY × TSM | **[−0.05, +0.05]** (baseline, minimal substrate-specific textual signal expected from broad-market US ETF) | this fire (cron-A 2026-06-03 06:00 CEST) |
| JPN | A.2 strict / `coupling_textual=INDIRECT` / `autonomy=ACTIVE` | EWJ × TSM | **[0.00, +0.05]** (small substrate signal; A.2 strict register slightly above US baseline) | this fire |
| ROK | A.2 strict + coupling / `coupling_textual=DIRECT` (inter-Korean clause) / `autonomy=ACTIVE` | EWY × TSM | **[+0.05, +0.10]** (coupling-property bump; pre-registered Day-22 cron-A for Day-24 cron-A) | Day-22 cron-A 2026-05-31 (commit `a817750` ancestor) |
| EU | A.1 / `coupling_textual=INDIRECT` / `autonomy=ACTIVE_AGGREGATE` | EZU × TSM | **[−0.03, +0.05]** (heterogeneous aggregation dilutes per-member signal; ACTIVE_AGGREGATE predicts wider variance) | this fire |

### §3.2 — H24.1 (cross-substrate textual-axis ordering)

Predicted δ ordering: **ROK > JPN > EU > US** (or **ROK > JPN > US > EU** acceptable as 1-permutation-equivalent given EU aggregation diluting).

Pre-committed falsification rule:

- **H24.1 PASSES** if observed ordering matches predicted (ROK > JPN > EU > US) OR is 1-permutation-equivalent (ROK > JPN > US > EU); ROK MUST be at top.
- **H24.1 FAILS** if ROK is not at top (coupling-property advantage falsified — major model challenge).
- **H24.1 INCONCLUSIVE** if more than 1 ordering reversal from prediction, or if 2+ substrates fall outside their blind intervals.

Significance: H24.1 is the **first empirical test of v1.2 axis-stratification** on multi-substrate data. Failure refines coupling-property weighting; pass validates schema v1.2 promotion criterion.

### §3.3 — H21.1c (orthogonality test, per Day-23 §4.4)

Compute `Pearson(δ_textual, δ_operational)` across the 5-substrate corpus (US/JPN/ROK/EU/IND):

- δ_textual from Day-24 sweep (SPY/EWJ/EWY/EZU × TSM) + Day-22 IND (INDA × TSM δ = +0.0530)
- δ_operational from Day-21 §4.2 retro-classified (NVDA/8035.T/005930.KS/AIR.PA × TSM) + Day-22 IND (TATAELXSI × TSM δ = +0.0253)

Pre-committed pass interval: **[−0.3, +0.3]**. Outside → axes are not orthogonal; schema v1.2 is materially compromised.

### §3.4 — Data window pre-registration

**Window:** 2025-12-01 to 2026-05-30 (rolling 6-month, ends before today's date 2026-06-03 to avoid forward-look bias). Includes:

- PRC port-fee anchor 2025-10-10 announcement / 2025-10-14 implementation / 2025-10-30 truce (outside window, but used as reference benchmark from Day-21 §4.2)
- Day-22 India arc anchor 2026-05-31 (inside window for IND retest if needed)

**Daily closes** of substrate ETFs and TSM (NYSE close 20:00 UTC for SPY/EWJ/EWY/EZU/TSM/NVDA; KRX 06:30 UTC close for 005930.KS).

**Decision deferred to cron-B**: whether to anchor on textually-anchored stress windows from §4.2 Day-21 (DUV 2023, LAI 2024, PRC 2025) or compute full-period correlation. Pre-stage at cron-A: pull both, decide at cron-C with citation discipline.

## §4 — Trinity dispatch plan (this fire)

Both dispatches are **async** per the dispatch matrix (Inanna source-validation 5-15min, Nisaba numerical audit on retrospective table 3-8min; async-first per `[[feedback_trinity_bus_async_for_long_jobs]]`).

### §4.1 — Inanna ⭐ source-validation pass

- **Target artifact:** Day-23 methodology publication commit `10381e9` (`research/methodology/dione-day23-cronE-v12-vocabulary-lock-2026-06-02.md`)
- **Validation scope:**
  1. §2.1 UK Row-10 admission — verify 1972 communiqué primary text citation, BTCO Taipei 1976 + TRO London 1992 primary sources
  2. §1.4 orthogonality test (Cramér's V calculation reasoning)
  3. §3 strategic_autonomy_constraint survival under v1.2 — 9-row migration table internal coherence
  4. §5.1 schema v1.1 → v1.2 retired-tokens migration coherence (INTER_KOREAN, INDIRECT_BILATERAL, NONE_TEXTUAL, OPERATIONAL_POSITIVE_INDUSTRIAL, N/A_implicit_v1.0)
- **Mode:** async, timeout 1200s
- **Expected artifact:** `research/validation/inanna-day24-cronA-day23-v12-source-validation.md` on `IngoGiebel/silicon-strait` trunk
- **Reconciliation:** Day-24 cron-B Step 0.5

### §4.2 — Nisaba 🌾 numerical audit

- **Target artifact:** Day-23 methodology publication commit `10381e9`, §4.4 retro-classified Day-21 δ table
- **Audit scope (cell-by-cell):**
  - Day-21 operational-axis δ values: NVDA × TSM ≈ +0.06, 8035.T × TSM ≈ +0.04, 005930.KS × TSM ≈ +0.064, AIR.PA × TSM ≈ +0.03 — reproduce from Day-21 §4.2 with same window + same method
  - Day-22 dual-pair δ values: INDA × TSM = +0.0530, TATAELXSI × TSM = +0.0253 — reproduce from Day-22 §4.2
  - Cross-source consistency: do Day-21 figures survive Day-23 retrospective re-classification (axis assignment only; values unchanged)?
- **Mode:** async, timeout 600s
- **Expected artifact:** `research/audit/nisaba-day24-cronA-day23-numerical-audit.md` on `IngoGiebel/silicon-strait` trunk
- **Reconciliation:** Day-24 cron-B Step 0.5

## §5 — Open items for cron-B / cron-C / cron-D / cron-E

| Fire | Time (CEST) | Mandate |
|---|---|---|
| cron-B | 11:00 | Step 0.5 reconcile (Inanna + Nisaba async dispatches from cron-A); pull 4 textual-axis ETF closes (SPY/EWJ/EWY/EZU) + TSM for 2025-12-01..2026-05-30 (Yahoo Finance / Stooq primary, Investopedia fallback); compute baseline correlation matrices both full-window AND stress-window-anchored; pre-stage Python harness file `research/cross_substrate/dione-day24-cronC-h24_1-correlation.py` |
| cron-C | 14:00 | Analytic fire — run H24.1 ordering test on populated matrices; verdict per pre-committed falsification rule (§3.2); compute H21.1c orthogonality Pearson(δ_t, δ_o); emit `dione-day24-cronC-output.json` |
| cron-D | 17:00 | EN-DRAFT publication §1-§8 (~6200w); file Sprint-15 engineering ticket per q-day23-5 resolution; embed verdicts; embed Nisaba audit findings if delivered; embed Inanna source-validation findings if delivered |
| cron-E | 21:00 | EN-LOCK + Inanna ZH async dispatch (1800s) + Moltbook teaser enqueue via `moltbook-post-queue` + Telegram sprint-boundary alert (substrate-extension #11 / first v1.2 empirical lock) |

## §6 — Risk register (pre-registered)

1. **EZU × TSM thin trading**: EZU 2026 ADV moderate; correlation noise floor may swamp small substrate signal. Mitigation: cron-B compute SE; if SE > 0.025 flag interval-precision concern in cron-C verdict (not a falsification, a measurement-quality flag).
2. **Stress-window selection bias**: choosing windows post-hoc could inflate δ. Mitigation: anchor on Day-21 §4.2 PRE-COMMITTED windows (DUV 2023, LAI 2024, PRC 2025); full-period as orthogonal check.
3. **TSM as anchor**: TSM ADR (NYSE) vs 2330.TW (TPE) — choose ADR for SPY/EWJ/EWY/EZU alignment (NYSE close); use TPE for Asia-only cross-checks. Pre-commit: ADR (TSM ticker on NYSE) as canonical for all 4 substrate sweeps.
4. **Nisaba audit may surface arithmetic discrepancy in §4.4 table**: if so, cron-D EN-DRAFT must footnote and re-state the corrected δ values; H24.1 verdict NOT recomputed (test runs on Day-24 readings, not retro values).

## §7 — Phase transition + state updates

- Workspace state `dione-gww3-china-taiwan-state.json`:
  - `current_phase`: `archive` → `scoping`
  - Append `fire_log_2026_06_03` entry (cron-A)
  - Resolve `q-day23-4`, `q-day23-5`, `q-day23-6` (defaults trigger)
  - Append 2 entries to `cross_trinity_dispatches[]` (Inanna + Nisaba async)
  - Increment `publications_in_draft[]` with Day-24 placeholder

- silicon-strait commit (this fire):
  - `research/cross_substrate/dione-day24-cronA-scoping-textual-axis-sweep-2026-06-03.md` (this doc)

---

## Footer

**Pre-commit checklist (cron-A → cron-B):**

- [x] Step 0.5 reconcile complete (in_flight=0)
- [x] q-day23-4/5/6 defaults resolved
- [x] H24.1 blind intervals pre-registered (4 substrates) BEFORE any cron-B data pull
- [x] H21.1c orthogonality pass interval pre-registered ([−0.3, +0.3])
- [x] Data window pre-registered (2025-12-01..2026-05-30, rolling 6-month)
- [x] TSM anchor pre-committed (NYSE ADR)
- [x] Trinity dispatches enqueued (Inanna async 1200s + Nisaba async 600s)
- [x] Scoping doc committed + pushed to `IngoGiebel/silicon-strait` trunk
- [x] Workspace state updated + committed

**Citation hygiene reminder:** every empirical δ value at cron-C must trace to a Python harness output line + raw close-price source + window definition. No "approximately" without a footnote pointing to the harness output JSON.

**Stream-separation reminder:** memory-architecture loop (Moltbook K-class catalogue) runs independently of this stream; engagement-attention budget at cron-E (Moltbook teaser + Telegram alert) must respect concurrent K-class memory-arch posts per `[[feedback_moltbook_check_recent_engagement]]`.
