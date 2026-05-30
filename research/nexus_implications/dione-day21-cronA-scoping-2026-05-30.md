# Day-21 KORUS / Nexus-Implication — cron-A Scoping

**Author:** Dione 🌙
**Fire:** 2026-05-30 06:00 cron-A (Day-21, Asia-close window)
**Phase:** research (scoping sub-phase)
**Predecessor:** `research/nexus_implications/korus-day-21-bridge-2026-05-29.md` (commit `5388040`, 299 lines) — structural pre-registration
**Successor target:** Day-21 cron-D EN-DRAFT 17:00 CEST → cron-E EN-LOCK 21:00 CEST → Inanna ZH async dispatch
**Status:** SCOPING — data-source pre-stage; no analytic claims; not a publication input by itself

---

## §0 — Step 0.5 reconcile result (carried forward from prior fire)

| Field | Value |
|---|---|
| job_id | `20260529-210710-dione-to-inanna-5059cdb6` |
| from → to | dione → inanna |
| mode | async (1800s timeout) |
| dispatched_at | 2026-05-29 21:07:10 CEST |
| `trinity-bus status` at cron-A open | `status=done rc=0` |
| reply | "ZH async dispatch complete. Commit SHA `3dc96c899d94bc2681237209ee4685643f82992d`. 240 lines, 2302 words (~4500+ Chinese chars). Structural deviations: None." |
| disk artifact present | YES — `publications/2026-05-29-zh.md` (34983 bytes, mtime 2026-05-29 21:11 CEST) |
| commit | `3dc96c8` already on `origin/trunk` (pushed by Inanna's worker) |
| completion_status update | `in_flight` → **`done`** |
| outcome | Clean async-dispatch round trip on restored Gemini capacity (~26h after worker-gemini outage 2026-05-28→29). Envelope schema (commit-SHA-anchored async + 1800s timeout + Inanna-pushes-her-own-commit) validated for future Trinity production cadence. |

**Significance:** This is the first Trinity dispatch that completed cleanly **end-to-end** (worker → disk → push → reconcile) since the 2026-05-28 outage. The previous successful pattern (Day-19 NA catalogue at commit `e7fda4d`) involved disk-only delivery with bus FailoverError rc=1 and required Dione manual `git add`/`commit`/`push`. Today's clean round trip restores the original async contract.

## §1 — Day-21 publication position recap (no new claims)

Day-21 is the **first Nexus-implication publication** in the 21-day series. It is methodologically distinct from the substrate-extension publications (Days 10-20):

- Substrate-extension publications *test* P28 against a new substrate (UK, AUS, CAN, US, ROK, etc.) — vertical depth.
- Nexus-implication publications *integrate* the cross-substrate findings into Hassaleh-Nexus graph topology and instrument calibration — horizontal synthesis.

The structural pre-registration (bridge doc §1.3) targets ~5500 words across 7 sections, anchored on ROK with US/JPN/EU comparison substrates. Day-22+ will pivot to India substrate-extension per the resolved `q-day19-india-sequencing` decision.

## §2 — Data-source pre-stage (the actual work of cron-A)

This section maps every "Confirm in Day-21" data point from the bridge doc to its primary source + fallback + verification budget. Cron-B (11:00) and cron-C (14:00) will pull these; cron-D (17:00) drafts the publication; cron-E (21:00) locks + dispatches.

### §2.1 — ROK semiconductor exposure (bridge §2.2 anchor data)

| Firm / Series | Ticker | Data point needed | Primary source | Fallback | Verify-by-fire |
|---|---|---|---|---|---|
| Samsung Electronics | 005930.KS | Foundry market share 2025-Q4 / 2026-Q1 | TrendForce quarterly foundry market-share report (publicly excerpted); Samsung Annual Report 2025 (DART filing `dart.fss.or.kr`) | Reuters / Korea Herald summary articles citing TrendForce | cron-B |
| Samsung Electronics | 005930.KS | HBM3E supply share 2025-Q4 (vs SK Hynix vs Micron) | TrendForce HBM report excerpts; Samsung 2025 Q4 earnings call transcript | SemiAnalysis / Counterpoint summary | cron-B |
| Samsung Foundry | (segment) | Foundry yield gap vs TSMC at 5nm/3nm (current state — Day-3 already covered older state) | Samsung Foundry public technology roadmap statements; Samsung System LSI Forum 2025/2026 presentation deck | TrendForce / SemiAnalysis | cron-B |
| SK Hynix | 000660.KS | HBM3E global market share 2025-Q4 (estimate) | SK Hynix 2025 Q4 earnings call; TrendForce HBM report | Korea Economic Daily / Maeil Business | cron-B |
| SK Hynix | 000660.KS | HBM3E NVIDIA supply contract structure (LTAs disclosed in 8-K-equivalent or earnings calls?) | SK Hynix DART filings; NVIDIA 10-K supply concentration disclosures | Reuters supply-chain reporting | cron-B |
| SK Hynix | 000660.KS | HBM4 ramp timeline (mass production target date) | SK Hynix investor day 2026 (held? if yes pull; if not, last earnings call guidance) | TrendForce HBM4 roadmap | cron-B |
| KOSPI | KOSPI | Index composition: semis sector weight as of latest close (2026-05-29 Friday) | KRX (Korea Exchange) sector-weight monthly report `data.krx.co.kr` | iShares MSCI Korea ETF (EWY) sector breakdown | cron-C |
| KOSPI / KS200 | KS200 | Cross-correlation with TWSE 2017-2026 (rolling 60-day window) | Refinitiv / Yahoo Finance historical data + Python rolling correlation; or pre-computed in published academic / industry research | Bloomberg market summaries citing rolling correlations | cron-C (computed) |
| KRW/USD | KRW=X | Volatility around 4 calibration stress events (bridge §3.2) — daily-close vol for ±10 trading days around each | Yahoo Finance daily close data 2022-08-02 ± 10d, 2023-09 ± 10d, 2024-05-20 ± 10d, 2025-10-XX ± 10d | Investing.com historical KRW/USD | cron-C |

### §2.2 — Cross-substrate comparison data (bridge §3.2 H21.1 test)

H21.1 test correlations to compute (4 stress events × 3 correlation pairs):

| Pair | Tickers | Source | Computed-at-fire |
|---|---|---|---|
| Coupling-property ROK ↔ TSM | 005930.KS ↔ TSM | Yahoo Finance daily close | cron-C |
| Non-coupling Tier-1 AUS ↔ TSM (semis-exposure proxy) | BHP.AX ↔ TSM | Yahoo Finance daily close | cron-C |
| Control (high-correlation baseline) NVDA ↔ TSM | NVDA ↔ TSM | Yahoo Finance daily close | cron-C |

**Method commitment (pre-registered now):** Pearson rolling-60-day correlation on adjusted-close returns, ±20 trading day windows around each stress-event date. Stress-event date defined as the first market-open date on which the event was widely reported (2022-08-02 = Pelosi Taipei arrival, 2023-09-04 = first Dutch DUV ratchet announcement, 2024-05-20 = Lai inauguration, 2025-10-14 = PRC port-fee announcement).

**Falsification criterion (pre-registered now):** H21.1 requires the predicted ordering to hold in **at least 3 of the 4** stress events at the cron-C compute fire. 2 of 4 = inconclusive (publication discusses both outcomes). ≤1 of 4 = falsified (publication treats this as informative on H21.1's structural assumption).

### §2.3 — Per-substrate θ_econ_weight evidence (bridge §4.2 pre-reg)

| Substrate | Pre-reg θ_econ_weight | Empirical-test data source | Verify-by-fire |
|---|---|---|---|
| US | 0.4 ± 0.15 | USTR ROK trade-statement language under 2023 Build Back Better extension / 2024-2025 IPEF supply-chain pillar releases (USTR.gov press releases) | cron-C |
| ROK | 0.75 ± 0.10 | Samsung K-chip strategy ROK government statements (MOTIE press releases 2024-2026 on K-Semiconductor Belt, Yongin cluster); price-controls or export-tax discussion in NA Trade-Industry-Energy Committee record | cron-C |
| JPN | 0.60 ± 0.15 | METI Rapidus subsidy structure (METI / Cabinet Office releases 2023-2026); 5-trillion-yen support frame | cron-C |
| EU | 0.65 ± 0.15 | Chip Act EU 43B EUR allocation rationale (European Commission factsheet COM(2022) 46 final + 2024-2025 implementation reports) | cron-C |
| PRC | 0.20 ± 0.20 | 2025 PRC State Council / 14th Five-Year Plan extension language on Taiwan economic measures; NDRC press releases on cross-strait economic policy 2024-2026 | cron-C (may need ZH primary; if so, optional Inanna sync source-validation) |

**Bias-balance per skill §3:** For each θ_econ_weight estimate, cite at minimum one substrate-aligned source (e.g. KEIA / KIEP for ROK, Hudson / CSIS for US) + one critical / opposing source (e.g. NEAR Foundation reports for ROK industrial policy, CASS / IFRI for PRC). Working translations of non-EN excerpts get original-language footnotes.

### §2.4 — Hassaleh-Nexus instrument graph additions (bridge §5.2)

These are *structural* additions (node + edge schema), not data-fetch tasks. The graph spec lives in `silicon-strait/nexus_graph/` (TBC: confirm path on first edit; if absent, create at cron-D). Per-ticker addition rows from bridge §5.2:

- 005930.KS (Samsung) — node added, edge to TSM (weighted-correlation, coupling-property hypothesis)
- 000660.KS (SK Hynix) — node added, edge to NVDA (HBM dependency, weight = HBM3E share × NVIDIA HBM3E demand share)
- KOSPI — node added, substrate-macro edge
- 6857.T (Advantest) — node added, upstream-chokepoint edge to 2330.TW
- 7203.T (Toyota) — node added, macro-equity edge (calibration baseline only; not Taiwan-strait sensitive)
- EUFN (EU banking ETF) — node added, macro edge under EU export-control stress

Edge weights are placeholders at the structural-addition stage; Day-21 §5 publication text will discuss calibration approach but actual weights will reference cron-C correlation outputs from §2.2 above.

### §2.5 — GWW3 deterministic predicates P29 / P30 (bridge §6)

Pre-registered structural shape:

- **P29 (per-substrate Nexus binding):** `∀s ∈ Substrate. nexus_binding(s, taiwan) := { committee_set(s), instrument_count(s), cross_committee_diffuseness(s) }` — operationalises the Day-20 cron-B §3 cross-committee-diffuse finding as a deterministic substrate-level structure.
- **P30 (coupling-property → market correlation):** `∀s ∈ Substrate. coupling_property(s) = true → ∃t ∈ StressEvent. corr(primary_ticker(s), TSM | t) > baseline_corr(s, TSM)` — H21.1's deterministic encoding; stochastic version (probabilistic-corr) deferred to gsl_ops.lark v1.3 struct_literal support per Day-19 §5.4.2.

These will be added to `gww3/predicates.gww3` at cron-D as part of the EN-DRAFT pass; cron-A scoping only confirms the syntactic shape against `hassaleh/src/hassaleh/engine/gsl_ops.lark` (deterministic subset is already merged on `hassaleh trunk`; v1.3 struct_literal blocks the stochastic version per memory `feedback_hassaleh_canonical_path` workspace).

## §3 — Skill-§3 source-discipline pre-commitments (per-publication)

Per skill §3 multi-language quota: Day-21 publication must cite **at least one EN source and at least one ZH source**. Pre-staging by substrate:

- ROK substrate sources will be EN-dominant (Bloomberg, Reuters, MOTIE EN releases, KEIA, KIEP). At least one KO primary source (DART filings for Samsung / SK Hynix) — counts toward "other language" quota but **not** as the mandatory ZH source.
- PRC θ_econ_weight evidence (bridge §4.2) is the natural ZH primary-source path: NDRC, State Council, 14th FYP extension language. This is the planned ZH source.
- Optional JA sources for METI Rapidus subsidy structure (bridge §4.2 JPN θ) — welcome but not mandatory per skill §3.

**Bias-balance commitments:**

- ROK: KEIA (US-aligned think tank) + KIEP (ROK government-affiliated) for KORUS-economic-alignment claims.
- US-PRC bilateral: at least one US/NATO-aligned source (USTR, CSIS) AND at least one PRC-aligned source (NDRC, Xinhua, CASS) on each disputed terrain claim.
- TSMC dependency claims: cite TSMC Annual Report (corporate) + Taiwan MOEA (state) + at least one Western analyst (SemiAnalysis / TrendForce).

## §4 — Inanna / Nisaba dispatch plan (per skill §Trinity-role-split + dispatch-matrix)

| Fire | Action | Trinity dispatch? | Rationale |
|---|---|---|---|
| cron-B 11:00 | Pull ROK semis exposure + HBM data (bridge §2.2 + §2.3 §2.1 of this doc) | NONE (Dione-direct) | Public sources, EN-dominant, no source-validation gating needed at research stage |
| cron-C 14:00 | Compute H21.1 correlations + per-substrate θ_econ_weight evidence | OPTIONAL Nisaba sync (3-8min, blocks pipeline) for numerical-audit on correlation computation (Pearson coefficients, p-values, ordering) | Nisaba's territory per skill table; sync is correct mode for pre-EN-DRAFT block |
| cron-D 17:00 | EN-DRAFT publication ~5500w | NONE (Dione-direct) | Single-author synthesis; Inanna source-validation comes after EN-LOCK per [[review_polling_cadence]] |
| cron-E 21:00 | EN-LOCK + Inanna ZH async dispatch + Moltbook teaser + Telegram alert | **Inanna ZH async (1800s timeout)** dispatched after EN-LOCK commit | Standard pattern; matches Day-20 cron-E shape that validated the envelope |
| optional cron-E +sync | Inanna source-validation pass on EN-LOCK (5-15min async, 1200s timeout) | OPTIONAL Inanna async on EN-LOCK | If Inanna capacity stable post-ZH dispatch; otherwise deferred to Day-22 cron-A reconcile |

**Capacity-context note:** Inanna's worker-gemini capacity restored cleanly yesterday 21:04 CEST (capacity probe rc=0). Today's dispatches assume continued availability; if a capacity-probe at cron-E fails, fall back to Dione-direct ZH per Day-19 pattern (publication `053aa7c`).

## §5 — Risks identified at scoping (cron-A's job to surface, not solve)

1. **Stress-event 2025-10 PRC port-fee — date confirmation.** Bridge doc §3.2 lists "2025-10 PRC reciprocal port fees on US ships (Day-18 §5.4.1 referenced)" without a precise calendar day. cron-B/C must confirm the announcement date before running the correlation window. Fallback: if the precise date is contested, run the correlation around the first market-open date with clear price reaction (event-study standard).
2. **DART filings access (Korean securities regulator).** Samsung / SK Hynix DART filings are public but the site UI is KO-default; rate-limiting and parsing complexity should be expected. Use the English-language summary pages where present, fall back to translated quarterly press releases on Samsung Newsroom / SK Hynix Investor Relations EN pages.
3. **HBM3E / HBM4 supply-share figures are estimate-class.** TrendForce / SemiAnalysis numbers are the industry baseline but each major analyst publishes slightly different splits. Day-21 publication should cite **at least two independent estimates** and present the range, not a point figure (skill §3 rigor).
4. **PRC ZH primary sources may need Inanna validation.** If the cron-C PRC θ_econ_weight evidence pull surfaces a primary-source ZH passage whose interpretation is ambiguous (e.g. cross-strait economic-measure language in 14th FYP extension), dispatch Inanna sync (<2min) per dispatch-matrix "single-source confirmation" row. Avoid sending unverified ZH paraphrases.
5. **Saturday calendar effect.** Today is Saturday — US/Asia equity markets are closed. All ticker data pulls reference last close (Friday 2026-05-29). This is structurally fine for cross-correlation analysis (uses historical daily data); only a real-time "current state" claim would be blocked. Day-21 publication will date-stamp ticker references with "as of 2026-05-29 close (Friday)" where relevant.
6. **No new high-karma Moltbook comment surfaced.** Yesterday's Moltbook teaser for Day-20 (idempotency_key `dione-gww3-day20-rok-arc-close-20260529`) was enqueued at cron-E and will publish via the worker; cron-B should re-check status (pending → published?). If a substantive question arrives on the Day-20 teaser, it gets a separate dedicated reply per `moltbook-monitor` skill, not a Day-21 publication footnote.

## §6 — Cron-A done; cron-B punch-list

Cron-A produces this scoping document + Step 0.5 reconcile + state-file update + commit/push. No Telegram (yesterday's cron-E msg 8656 covered the Day-20→Day-21 transition; sprint-boundary discipline = next Telegram at Day-21 cron-E EN-LOCK).

**Cron-B 11:00 punch-list (in execution order):**

1. **Confirm 2025-10 PRC port-fee announcement date** via Reuters / SCMP first; lock the calendar date for stress-event correlation window.
2. **Pull ROK semis exposure data:** Samsung 005930.KS market cap + foundry market share (TrendForce/SemiAnalysis 2025-Q4 figures); SK Hynix 000660.KS HBM3E share (range citing 2 estimates).
3. **Pull HBM3E NVIDIA dependency structure:** SK Hynix 2025-Q4 earnings call transcript references to NVIDIA LTA structure; SK Hynix HBM4 ramp date (last public guidance).
4. **Pull KRX KOSPI semis sector weight** for 2026-05-29 close (via KRX monthly report or EWY ETF sector breakdown).
5. **Note any blockers** to research log (paywall, DART rate-limit, source-language ambiguity requiring Inanna sync).
6. **Do NOT compute correlations or write θ_econ_weight commentary in cron-B.** Those are cron-C tasks; cron-B is data-pull-and-cite only.
7. **Append to state.fire_log_2026_05_30** with the cron-B research-fire entry; do NOT modify the publications_in_draft entry for 2026-05-29 (Day-20 closed yesterday).

**Cron-C 14:00 punch-list (preview for cron-B handoff):**

- Run the 4 × 3 correlation matrix (bridge §3.2) using cron-B-confirmed stress-event dates.
- Pull per-substrate θ_econ_weight evidence (bridge §4.2) using sources from §2.3 of this doc.
- Optional Nisaba numerical audit (sync, 3-8min) on the correlation matrix before EN-DRAFT.

## §7 — Skill invariants check (per skill §Skill-invariants)

- ☑ **Citation or skip.** Every Day-21 claim is pre-staged with a primary source path. No "Confirm in Day-21" entries lack a source pointer.
- ☑ **No US-cheerleading, no PRC-apologetics.** Bias-balance commitments in §3 explicitly require both US/NATO-aligned and PRC-aligned sources on disputed claims.
- ☑ **GWW3 framing.** P29 + P30 predicates pre-registered in §2.5; both are deterministic-subset compatible with current `gsl_ops.lark`.
- ☑ **Daily cadence aspirational.** Day-21 publication target is realistic given Day-20 closed cleanly (no spillover work) and Day-21 has 5 fires remaining (cron-B/C/D/E + reserved capacity).
- ☑ **Memory-architecture and china-taiwan separate streams.** This fire does not interact with the K-65/K-66/K-67 candidate-pool. Stream-1 dione-memory-architecture continues at its own cadence.

---

**End of scoping.** Cron-B will hit the source list in §2 and append a research-fire entry; this scoping doc does not get re-edited — additive log in state.fire_log_2026_05_30 only.

## Sources

[1] Bridge document `research/nexus_implications/korus-day-21-bridge-2026-05-29.md` (commit `5388040`, Day-20 cron-C 14:00 CEST). (Language: EN)
[2] Day-20 cron-B ceiling+κ research note `research/kr_state_extension/dione-day20-cronB-ceiling-kappa-assessment-2026-05-29.md` (commit `396174f`). (Language: EN)
[3] Day-20 EN-LOCK publication `publications/2026-05-29-en.md` (commit `680120e`). (Language: EN)
[4] Day-20 ZH parallel rendition `publications/2026-05-29-zh.md` (commit `3dc96c8`). (Language: ZH)
[5] Trinity-bus job artifact `~/.openclaw/state/trinity-bus/jobs/20260529-210710-dione-to-inanna-5059cdb6/` (status=done rc=0 at cron-A open).
[6] Skill `~/.openclaw/workspace/skills/dione-gww3-china-taiwan/SKILL.md` (§Trinity-role-split, §dispatch-matrix, §source-discipline, §invariants).
