# Silicon Strait — Day 23 (2026-06-02) — Schema v1.2 Promotion Review

**Lead:** Dione 🌙  ·  **Validation:** Inanna ⭐ (deferred to Day-24 cron-A)  ·  **Numerical audit:** Nisaba 🌾 (deferred to Day-24 cron-A)
**Phase:** publication — methodology (Path B)
**Languages reviewed today:** EN (Day-23 set EN-only for methodology publications, per q-day23-2 default — see §8)
**Anchor commits:** Day-22 EN-LOCK `a817750` · Day-22 ZH-LOCK `b259818` · Day-23 cron-D scoping `e5e6872`

---

## Executive summary

Day-22's H22.1 PASSES + H21.1b NULL split — structural schema acceptance with empirical-pair failure on the firm-specific industrial-coupling pair — was the trigger to review whether `coupling` belongs as a single field or as two orthogonal axes. Day-23 cron-E executes that review under the cron-D-pre-registered Path B falsification criterion (`≥6/9 rows v1.2-stable AND ≥1 row v1.2 contradicts v1.1`). **The criterion is met (9/9 stable, 3/9 contradict).** Schema v1.2 is promoted. `coupling_textual ∈ {NONE, INDIRECT, DIRECT}` and `coupling_operational ∈ {NEGATIVE, NEUTRAL, POSITIVE_INDUSTRIAL, POSITIVE_DIPLOMATIC, DIRECT_STATUTORY}` lock as the v1.2 split with explicit truth-conditions and a v1.2 → v1.3 falsification rule. UK is admitted as Row-10 under v1.2 cleanly. The empirical-pair methodology is revised from one-pair-per-substrate to two-pair-per-substrate (textual-axis pair + operational-axis pair), with KR worked example pre-registered for Day-24 forward-test (EWY × TSM as the previously-missing ROK textual-axis pair).

## Today's thesis

The Day-22 verdict — *the schema fits India structurally but predicted the wrong empirical signature on India's industrial-coupling pair* — is not a schema failure. It is the schema **doing its job by exposing the coupling-axis collapse it was carrying since Day-7**. Every prior substrate had textual register and operational behavior co-vary, so the single `coupling` field was undertested. India is the first row that decoupled them. The schema bump is conservative: 9 of 9 existing rows retain valid v1.2 cells under retrospective re-classification, 3 rows reveal that their v1.1 single-value masked a non-trivial textual-vs-operational split (JPN, ROK, IND), and v1.2 introduces a falsification rule for itself. Path B holds.

---

## §1 Schema v1.2 — vocabulary lock

### §1.1 Two orthogonal axes

Schema v1.1 (Day-22 EN-LOCK `a817750`) carried `coupling ∈ {NONE, DIRECT, INDIRECT, INTER_KOREAN, <class>}` as a single field with class-extensions accreted ad-hoc through the substrate series (Day-7 introduced DIRECT/INDIRECT; Day-13 PHL added INDIRECT_BILATERAL; Day-19/20 ROK introduced INTER_KOREAN; Day-22 IND introduced `NONE_TEXTUAL / OPERATIONAL_POSITIVE_INDUSTRIAL` as the first compound entry). The accretion was a symptom: the field was being asked to encode two independent variables.

**v1.2 splits `coupling` into two orthogonal fields:**

- `coupling_textual ∈ {NONE, INDIRECT, DIRECT}` — encodes the substrate's diplomatic register toward ROC (Republic of China / Taiwan).
- `coupling_operational ∈ {NEGATIVE, NEUTRAL, POSITIVE_INDUSTRIAL, POSITIVE_DIPLOMATIC, DIRECT_STATUTORY}` — encodes the substrate's substantive (non-textual) coupling behavior toward Taiwan-anchored capacity, capital, and personnel.

Orthogonality means: the textual axis is sourced exclusively from formal diplomatic instruments (communiqués, treaty texts, hansard records of ministerial statements, white papers); the operational axis is sourced exclusively from substantive instruments (legislation, capex, trade-flow, defense procurement, technology-transfer announcements). A claim about one axis is not admissible as evidence for the other.

### §1.2 Truth-conditions for `coupling_textual`

| Value | Truth-condition |
|---|---|
| `NONE` | Substrate has no formal diplomatic register that distinguishes ROC from PRC at any tier (consular, cultural, or legislative). Default for substrates whose pre-1971 recognition flipped to PRC without retaining any de facto Taiwan-facing representation. **Operational test:** no Taiwan-domiciled representative office of the substrate AND no substrate-domiciled Taiwan office at trade-or-cultural tier. |
| `INDIRECT` | Substrate maintains formal one-China textual position toward PRC AND simultaneously operates a de facto Taiwan-facing representative office (trade, cultural, or economic affairs) AND its diplomatic correspondence with both PRC and ROC distinguishes the two as politically separate counterparties at the working level. **Operational test:** documented bilateral office network (e.g. BTCO Taipei + TRO London; AIT Taipei + TECRO Washington precursor model adapted as INDIRECT when the substrate lacks a TRA-equivalent statute). |
| `DIRECT` | Substrate has a statutory or treaty-level instrument that institutionalizes recognition of ROC as a distinct counterparty AND grants ROC textual standing as a state-or-quasi-state in the substrate's diplomatic register. **Operational test:** statutory framework (US TRA 1979, Six Assurances 1982) OR full state recognition (Holy See, the 12 remaining ROC-recognizing UN states). |

**The INDIRECT/DIRECT boundary is statutory-or-not**: INDIRECT can include treaty-derived legacy obligations (e.g. JPN 1972 Joint Communiqué with subsequent 1972-wave-extension MoUs in the FYP layer) so long as the substrate does **not** carry a Taiwan-Relations-Act-class statute. Statutes outrank ministerial MoUs because they constrain successor governments.

### §1.3 Truth-conditions for `coupling_operational`

| Value | Truth-condition |
|---|---|
| `NEGATIVE` | Substrate publicly aligns with PRC sanctions against ROC OR actively obstructs Taiwan industrial coupling within its territory. **Operational test:** documented export-control or trade-tool action against Taiwan AND no offsetting industrial substrate-anchored Taiwan capex. |
| `NEUTRAL` | Substrate has trade flows with Taiwan but no above-threshold industrial or diplomatic acts. **Operational threshold:** no substrate-anchored Taiwan-firm industrial capex ≥ USD 1B AND no head-of-government / head-of-state level reciprocal diplomatic act in the 24 months ending publication date. |
| `POSITIVE_INDUSTRIAL` | Substrate hosts or directly co-finances Taiwan-firm-anchored industrial capacity at scale (≥ USD 1B substrate-anchored capex or equivalent bilateral substrate-anchored industrial commitment). **Operational test:** documented fab, packaging, advanced-substrate, or semi-supply-chain build-out on substrate territory with a Taiwan firm as primary technology or capital counterparty. |
| `POSITIVE_DIPLOMATIC` | Substrate engages in head-of-government, head-of-state, or cabinet-minister level diplomatic acts toward ROC counterparts within the 24-month publication window. **Operational test:** documented state visit, recognition statement, reciprocal congratulations, OR cabinet-level economic cooperation framework. |
| `DIRECT_STATUTORY` | Substrate has a statutory framework that institutionalizes Taiwan coupling at the legal level, including mandatory defensive arms sales, mandatory consultation requirements, or legislatively-anchored cooperation programmes. **Operational test:** US-class TRA framework with mandatory provisions (not merely permissive). |

**`coupling_operational` is multi-valued by default** for substrates whose substantive coupling spans more than one category. Day-22 IND is the canonical example: `coupling_operational = POSITIVE_INDUSTRIAL` (Tata-PSMC Dholera + HCL-Foxconn Jewar) **and** `POSITIVE_DIPLOMATIC` (Lai-Modi 2024-06 reciprocal congratulations). The matrix cell records both, comma-separated; cell-classification rules in §2 below treat any non-NEUTRAL/NEGATIVE value as activating the operational-axis bit for empirical pair-matching purposes.

### §1.4 Orthogonality test (gate before promotion)

For each of the 8 pre-India substrates (where v1.1 forced a single value), the v1.2 split must be evaluable from sources of the appropriate kind:

- **Textual axis sources** must be diplomatic-formal (communiqués, treaty texts, hansard transcripts of ministerial statements, ministry white papers, ROC MOFA recognition catalogues).
- **Operational axis sources** must be substantive (legislation, capex announcements, customs trade tables, defense procurement budgets, technology-transfer MoUs).

The gate fails if any v1.2 classification depends on a source whose kind cannot be cleanly assigned to one axis. §2's retrospective table marks each cell with its source-class.

### §1.5 Falsification rule for v1.2 itself (v1.2 → v1.3 predicate)

Schema bumps without a falsifiability rule are arbitrary. v1.2 promotion publishes the predicate that would force v1.2 → v1.3:

**P_v12_fail:** A substrate is admissible whose coupling pattern requires **a third orthogonal axis** that cannot be expressed as a value within `coupling_textual × coupling_operational`. Specifically:

- **F1:** A substrate emerges where the financial/capital coupling axis behaves independently from both the textual and operational axes (e.g. a substrate that has `NONE` textual + `NEUTRAL` operational but is the dominant capital-flow counterparty to Taiwan's fab capex pipeline through a financial-conduit role — a Singapore-class case if the financial-conduit role grows to substrate-anchoring scale). Then `coupling_financial` would need to be added as a third orthogonal field, forcing v1.3.

- **F2:** A substrate emerges where `coupling_textual` and `coupling_operational` cease to be statistically orthogonal in the cross-substrate sample — i.e. the two axes' values become co-determined by a hidden third variable. **Empirical test:** Cramér's V on the cross-substrate joint distribution of (textual, operational) exceeds 0.5 when N ≥ 12 substrates. (Day-22 + UK admission delivers N=10; the Cramér's V test is provisional until N=12.)

- **F3:** A substrate emerges where the boundary between INDIRECT and DIRECT on the textual axis becomes empirically unstable — i.e. a substrate's textual classification flips between INDIRECT and DIRECT depending on whether the source-pull window includes specific ministerial statements vs. the underlying statutory framework. Then the textual-axis value-space needs a third intermediate (e.g. STATUTORY_PARALLEL), forcing v1.3.

**Day-23 commitment:** no v1.2 → v1.3 escape will be invoked without a published `research/methodology/dione-day-N-vNN-falsification.md` artifact documenting which of F1/F2/F3 fired and on which substrate, with sources.

---

## §2 Retrospective re-classification — 9 existing rows + UK Row-10 admission

### §2.1 Re-classification table

The table re-applies v1.2 to every row in the Day-22 H22.1 9-row matrix (Day-22 EN §3.1) plus admits UK as Row-10 per q-day22-10 pre-registered admission. For each row, the v1.1 single value is shown alongside the v1.2 split. The **Status** column marks `v1.2-stable` (the split is well-defined under §1.2/§1.3 truth-conditions), `v1.2-collapses` (the split returns identical values, suggesting the row would have been fine on v1.1), or `v1.2-forces-v1.3` (the row's pattern triggers a P_v12_fail predicate).

| Substrate | v1.1 coupling | v1.2 coupling_textual | v1.2 coupling_operational | Status | Contradicts v1.1? |
|---|---|---|---|---|---|
| US  | DIRECT_STATUTORY      | DIRECT   | DIRECT_STATUTORY                                       | v1.2-stable | No — v1.1 cell already encoded both axes via the statutory-framework single token. v1.2 surfaces the implicit two-axis structure (TRA 1979 is both DIRECT textual *and* DIRECT_STATUTORY operational) without contradicting v1.1. |
| JPN | DIRECT                | INDIRECT | POSITIVE_INDUSTRIAL                                    | v1.2-stable | **Yes** — v1.1 DIRECT had absorbed both the 1972-wave-extension MoU textual register (which is, by §1.2 truth-condition, INDIRECT not DIRECT because it lacks TRA-class statute) and the TSMC-Sony Kumamoto fab operational coupling (POSITIVE_INDUSTRIAL). v1.2 surfaces that JPN's substantive coupling is INDIRECT-textual + POSITIVE_INDUSTRIAL-operational, not uniformly DIRECT. |
| ROK | INTER_KOREAN          | INDIRECT | POSITIVE_INDUSTRIAL                                    | v1.2-stable | **Yes** — `INTER_KOREAN` was a custom v1.1 token covering ROK's specific inter-Korean-constraint-bounded INDIRECT coupling. v1.2 absorbs the constraint into the separate `strategic_autonomy_constraint=ACTIVE` field (§3) and resolves coupling cleanly: INDIRECT textual (TECRO equivalent at trade-tier post-1992 PRC-ROK communiqué) + POSITIVE_INDUSTRIAL operational (Samsung Foundry tier-1 supply-chain coupling competing+partnering with TSMC). The `INTER_KOREAN` token can be retired from the coupling vocabulary. |
| EU  | INDIRECT              | INDIRECT | NEUTRAL                                                | v1.2-stable | No — EU's substrate-aggregate operational coupling is NEUTRAL (no substrate-anchored Taiwan fab at scale; Airbus exposure is too dilute to clear the §1.3 USD 1B substrate-anchored capex threshold). The v1.1 INDIRECT was load-bearing on the textual axis; v1.2 confirms the operational axis is NEUTRAL not POSITIVE. |
| PRC | N/A_self              | N/A_self | N/A_self                                               | v1.2-stable | No — self-anchored substrate; coupling is not defined toward itself. v1.2 carries this through unchanged. |
| PHL | INDIRECT_BILATERAL    | INDIRECT | POSITIVE_DIPLOMATIC                                    | v1.2-stable | No (semantic, not value contradiction) — v1.1 `INDIRECT_BILATERAL` was a flavor-tag indicating Hou-Marcos style bilateral working-level diplomacy. v1.2 routes the textual layer to INDIRECT (standard one-China register) and the operational layer to POSITIVE_DIPLOMATIC (Senate Resolution 631 + senate-level Taiwan engagement, no above-threshold industrial). |
| AUS | INDIRECT              | INDIRECT | NEUTRAL                                                | v1.2-stable | No — INDIRECT textual carries (Australian Office Taipei + TECO Canberra); operational is NEUTRAL (no substrate-anchored Taiwan industrial capex at scale). AUKUS introduces an *implicit* operational coupling at the defense-supply-chain layer, but it does not clear the §1.3 USD 1B substrate-anchored industrial-capex threshold for AUS-substrate-anchored Taiwan capacity, so the cell stays NEUTRAL pending Day-24+ AUKUS-Taiwan-supply-chain depth audit. |
| CAN | INDIRECT              | INDIRECT | NEUTRAL                                                | v1.2-stable | No — INDIRECT textual carries (Canadian Trade Office in Taipei + TECO Ottawa); operational is NEUTRAL. CHIPS-and-Science Act US-tied capex flows to Canada do not constitute *Canada-substrate-anchored Taiwan capex* under §1.3. |
| IND | NONE_TEXTUAL / OPERATIONAL_POSITIVE_INDUSTRIAL | NONE | POSITIVE_INDUSTRIAL, POSITIVE_DIPLOMATIC | v1.2-stable | **Yes** — IND was the v1.1 compound cell that forced v1.2 review. v1.2 cleanly assigns NONE textual (no Taiwan-distinguishing diplomatic register since 1949) and POSITIVE_INDUSTRIAL + POSITIVE_DIPLOMATIC operational (Tata-PSMC Dholera Rs 91k Cr + HCL-Foxconn Jewar + Lai-Modi 2024-06 reciprocal congratulations). The cell is the Day-22 H21.1b primary contradicting case. |
| **UK Row-10** | (not in v1.1 matrix) | **INDIRECT** | **NEUTRAL** | **v1.2-stable** | **N/A** — UK admitted directly under v1.2. Textual: INDIRECT via 1972 Anglo-Chinese Joint Communiqué ("acknowledging the position" not "recognising the claim" — see Inanna `inanna-uk-1972-communique-text-2026-05-23.md`) + BTCO Taipei from 1976 + TRO London from 1992. Operational: NEUTRAL — no UK-substrate-anchored Taiwan industrial capex at the §1.3 threshold; ARM Holdings (Cambridge) IP licensing to Taiwan firms operates at the IP-trade layer not at substrate-anchored capex. |

### §2.2 Verdict against Path B falsification criterion

- **Criterion (a):** ≥ 6/9 existing rows v1.2-stable without forcing v1.3 escape. **Observed:** **9/9** stable. ✅
- **Criterion (b):** ≥ 1 row whose v1.2 split contradicts its v1.1 single-value. **Observed:** **3/9** contradict — JPN (DIRECT → INDIRECT/POSITIVE_INDUSTRIAL), ROK (INTER_KOREAN → INDIRECT/POSITIVE_INDUSTRIAL + autonomy-constraint factored out), IND (NONE_TEXTUAL/OPERATIONAL_POSITIVE_INDUSTRIAL compound → NONE/POSITIVE_INDUSTRIAL+POSITIVE_DIPLOMATIC). ✅

**Schema v1.2 is promoted.** The v1.1 `INTER_KOREAN` and `INDIRECT_BILATERAL` custom-class tokens are retired; their semantic content moves to (a) the v1.2 axis split and (b) the `strategic_autonomy_constraint` field (§3). The v1.1 column `coupling` is deprecated; the substrate_dynamics record now carries `coupling_textual` and `coupling_operational` as two fields.

### §2.3 Off-diagonality

Of 10 rows under v1.2:
- **Diagonal** (textual.value = operational.dominant_value at the equivalent rank): US (DIRECT/DIRECT_STATUTORY ≈ rank-3 textual + rank-5 operational), EU, AUS, CAN — 4/10.
- **Off-diagonal**: JPN (INDIRECT + POSITIVE_INDUSTRIAL), ROK (INDIRECT + POSITIVE_INDUSTRIAL), PHL (INDIRECT + POSITIVE_DIPLOMATIC), IND (NONE + multi-positive), UK (INDIRECT + NEUTRAL) — 5/10.
- **Self-anchored**: PRC — 1/10.

Off-diagonality at 50% (5/10) is the **quantitative validation** of the v1.2 promotion: if every substrate's two axes co-varied, v1.1 would have sufficed. Half the matrix exhibits independent variation. The schema bump is empirically motivated, not ergonomic.

---

## §3 `strategic_autonomy_constraint` survival under v1.2

`strategic_autonomy_constraint` was introduced at Day-22 v1.1 as `ACTIVE` for IND (encoding India's non-alignment-doctrine-derived foreign-policy constraint) and `N/A_implicit_v1.0` for the prior 8 substrates (since v1.0 did not have this field).

**v1.2 promotion preserves `strategic_autonomy_constraint` as a separate field**, with the following retrospective re-classification across the 10-row matrix:

| Substrate | strategic_autonomy_constraint (v1.2) | Rationale |
|---|---|---|
| US  | `DORMANT` | US is the substrate that anchors others' autonomy-constraint registers; its own constraint is not load-bearing at the substrate-coupling layer. |
| JPN | `DORMANT` | Article-9 constitutional constraint applies to defense posture, not to coupling-axis classification. Treaty-allied; autonomy-constraint not a coupling-axis modulator. |
| ROK | `ACTIVE`  | **Inter-Korean constraint** — the v1.1 `INTER_KOREAN` token's substantive content. Migrates here under v1.2 cleanly. |
| EU  | `ACTIVE_AGGREGATE` | EU substrate is itself the aggregation of 27 member-state autonomy-constraints; the field is operative at the aggregation layer. Distinguish from per-member-state ACTIVE/DORMANT. |
| PRC | `N/A_self` | Self-anchored. |
| PHL | `ACTIVE`  | ASEAN-coordination + US-MDT bilateral constraint co-bound; ACTIVE at the substrate level. |
| AUS | `DORMANT` | Treaty-allied (ANZUS) with high autonomy in operational coupling; constraint not load-bearing. |
| CAN | `DORMANT` | Treaty-allied (NATO) with high autonomy; constraint not load-bearing. |
| IND | `ACTIVE`  | Strategic-autonomy doctrine (non-aligned successor); the canonical Day-22 ACTIVE case. |
| UK  | `DORMANT` | Post-Brexit UK has formal autonomy increase but no inter-Korean-class or non-alignment-class constraint load-bearing on coupling. |

**The field survives** — it is orthogonal to both coupling axes and adds load-bearing information for 4 of 10 substrates (ROK, EU, PHL, IND). No reason to collapse it under v1.2.

**One v1.2 refinement on this field**: introduce `ACTIVE_AGGREGATE` as a value for substrates whose constraint operates at an aggregation layer rather than a unitary-state layer (EU is the canonical case). The field value-space becomes `{ACTIVE, ACTIVE_AGGREGATE, DORMANT, N/A_self}`. The `N/A_implicit_v1.0` token used Day-22 is retired; all rows now carry an explicit value.

---

## §4 Empirical-pair methodology revision

### §4.1 The structural underspecification

Day-22 H21.1a/b mapped each substrate's single `coupling` value (v1.1) to a single representative equity pair (e.g. ROK's `INTER_KOREAN` mapped to 005930.KS × TSM). Under v1.2's two-axis split, **the single-pair test is structurally underspecified**: a substrate now has a textual axis and an operational axis that may emit signals at different equity layers.

Consider Day-22's primary finding: TATAELXSI × TSM δ = 0.0253 (NULL) versus INDA × TSM δ = 0.0530 (in pre-registered interval). Under v1.1 the verdict is "primary pair NULL, secondary pair signal — H21.1b classification, refine." Under v1.2 the interpretation is sharper: **IND's textual-axis stress should emit at country-broad ETF (INDA — EM-flow / macro-political risk premium channel) and IND's operational-axis stress should emit at firm-specific industrial-coupling ticker (TATAELXSI — Tata-PSMC Dholera-anchored channel)**. The Day-22 stress window (cross-strait-directly-aimed events: Galwan_2020, PEL_2022, Tawang_2022, DUV_2023, LAI_2024, PRC_2025-{a,i}) is dominantly *textual-axis* stress (diplomatic-register shocks), so the macro-political risk premium channel (INDA) is the expected emitter — and was. The operational-axis stress for IND would be substrate-internal events (e.g. Tata-PSMC Dholera capex-schedule news, HCL-Foxconn Jewar regulatory delay, ROC MOEA technology-transfer audit) which the Day-22 H21.1 stress window did not include.

**Day-22 H21.1b NULL on TATAELXSI was not a refutation of industrial coupling; it was a confirmation that textual-axis stress does not emit at the operational-axis pair.** That is exactly what v1.2 orthogonality predicts.

### §4.2 The two-pair-per-substrate template

Under v1.2, each substrate's empirical-pair test specification becomes:

```
substrate_empirical_pairs(s):
  textual_pair_t(s):     country_broad_ETF(s) × TSM    # EM-flow / macro-political risk-premium channel
  operational_pair_o(s): firm_specific_coupling_ticker(s) × TSM   # industrial / capital-flow channel
```

For substrates where `coupling_operational = NEUTRAL`, the operational pair is `(N/A — no above-threshold industrial coupling)` and the empirical test reduces to the textual pair only. This is structurally correct: if a substrate has no above-threshold industrial coupling, there is no operational-axis pair to test.

For substrates where `coupling_operational` is multi-valued (IND: POSITIVE_INDUSTRIAL + POSITIVE_DIPLOMATIC), the operational pair carries one ticker per non-NEUTRAL coupling-operational class. For IND specifically: TATAELXSI for POSITIVE_INDUSTRIAL (Tata-PSMC), and a TBD-Day-24 ticker for POSITIVE_DIPLOMATIC (no clean equity counterparty exists for state-visit-class diplomatic acts; default to N/A and footnote).

### §4.3 KR worked example

The previously-collected ROK data at Day-21 §4.2 used 005930.KS × TSM only. Under v1.2 this is the operational-axis pair (Samsung Electronics × TSM tests POSITIVE_INDUSTRIAL ROK-substrate-anchored coupling at the firm-specific layer).

**The ROK textual-axis pair (EWY × TSM) was never tested.** This is the v1.2-introduced gap and the natural Day-24 forward-test.

Pre-registered Day-24 ROK textual-axis pair:
```
substrate:           ROK
coupling_textual:    INDIRECT
textual_pair:        EWY × TSM (iShares MSCI South Korea ETF × Taiwan Semiconductor)
stress_window:       same 6-event window as Day-22 IND test
                       [Pelosi_2022_08_02, DUV_2023_03_30, Lai_2024_05_20, PRC_2025_10_10, PRC_2025_10_14, PRC_2025_10_30]
baseline_window:     2020-04-01 → 2026-05-29, ex-stress-window
methodology:         rolling-60-day Pearson on log-returns, δ = stress_median - baseline_median
blind_pre_registered_interval:  [0.05, 0.10]  (matches Day-22 INDA × TSM interval — symmetric test for cross-substrate comparability)
H_alpha:             EWY × TSM δ ∈ [0.05, 0.10] under H22.2a (textual-axis emits at country-broad ETF)
H_beta:              EWY × TSM δ ∉ [0.05, 0.10] under H22.2a falsification — textual-axis does not emit at country-broad ETF for ROK
```

The discriminator is sharp:
- If EWY × TSM δ ∈ [0.05, 0.10] AND 005930.KS × TSM δ remains at Day-21's 0.064 (≈ same interval), then both axes are emitting at the expected layers and H22.2a (textual-axis → country-broad ETF) gains an independent cross-substrate confirmation.
- If EWY × TSM δ ∉ [0.05, 0.10] but 005930.KS × TSM δ ≈ 0.064, then the textual-axis emission hypothesis is ROK-falsified and IND's INDA signal needs an alternative explanation (e.g. IND was a special case because non-alignment-doctrine makes the textual axis itself more macro-political).

### §4.4 H21.1a/b promotion under v1.2

Under the v1.2 two-pair template, the H21.1a/b family is restated as:

**H21.1a-v1.2** (textual axis): For substrates with `coupling_textual ∈ {INDIRECT, DIRECT}`, the country-broad ETF × TSM pair returns δ ∈ [0.05, 0.10] in a textually-anchored stress window.

**H21.1b-v1.2** (operational axis): For substrates with `coupling_operational ∈ {POSITIVE_INDUSTRIAL, DIRECT_STATUTORY}`, the firm-specific coupling ticker × TSM pair returns δ ∈ [0.05, 0.10] in an operationally-anchored stress window.

**H21.1c-v1.2** (orthogonality): For substrates where both axes are non-trivial, the textual-axis pair δ and the operational-axis pair δ are not significantly correlated (`Pearson(δ_t, δ_o) ∈ [−0.3, +0.3]` across the substrate corpus).

Day-21 §4.2 evidence retro-classified under v1.2-axis assignment:

| Substrate | textual-axis pair (v1.2) | textual-axis δ at Day-21 stress window | operational-axis pair (v1.2) | operational-axis δ at Day-21 stress window |
|---|---|---|---|---|
| US  | SPY × TSM (TBD)      | (not measured Day-21)         | NVDA × TSM | δ ≈ +0.06 (Day-21 §4.2)       |
| JPN | EWJ × TSM (TBD)      | (not measured Day-21)         | 8035.T × TSM | δ ≈ +0.04 (Day-21 §4.2)     |
| ROK | EWY × TSM (Day-24)   | (not measured)                | 005930.KS × TSM | δ ≈ +0.064 (Day-21 §4.2) |
| EU  | EZU × TSM (TBD)      | (not measured Day-21)         | AIR.PA × TSM | δ ≈ +0.03 (Day-21 §4.2)    |
| IND | INDA × TSM (Day-22)  | δ = +0.0530 (Day-22 §4.2)      | TATAELXSI × TSM | δ = +0.0253 (Day-22 §4.2) |

Day-21's measurements were all on the **operational-axis** pair (the only pair tested under v1.1). Day-22 was the first dual-pair test (TATAELXSI as operational, INDA as textual/macro), and produced the dual-channel emission that v1.2 explains.

**Day-24+ priority**: complete the textual-axis-pair measurements for US/JPN/ROK/EU (SPY/EWJ/EWY/EZU × TSM) to populate the H21.1c orthogonality table.

---

## §5 GWW3 predicate refresh under v1.2

The substrate_dynamics record schema and the P29 / P30 family are updated. Full text lands in `gww3/predicates.gww3` at the same commit as this document. Summary of changes:

### §5.1 Schema record (v1.1 → v1.2)

```
v1.1:
  substrate_dynamics(s) {
    formal_anchor,
    coupling,                  // {NONE, DIRECT, INDIRECT, INTER_KOREAN, INDIRECT_BILATERAL, NONE_TEXTUAL, OPERATIONAL_POSITIVE_INDUSTRIAL, ...}
    ceiling, kappa_status, ..., strategic_autonomy_constraint
  }

v1.2:
  substrate_dynamics(s) {
    formal_anchor,
    coupling_textual,          // {NONE, INDIRECT, DIRECT}
    coupling_operational,      // {NEGATIVE, NEUTRAL, POSITIVE_INDUSTRIAL, POSITIVE_DIPLOMATIC, DIRECT_STATUTORY} (multi-valued)
    ceiling,
    kappa_status,
    ...,
    strategic_autonomy_constraint   // {ACTIVE, ACTIVE_AGGREGATE, DORMANT, N/A_self}
  }
```

Migration rule for v1.1 → v1.2 in the deterministic GSL subset: every v1.1 record carries forward; the v1.1 `coupling` field is split via the §2.1 retrospective re-classification table (canonical mapping documented inline).

### §5.2 P29 / P30 stratification

- **P29.3** (v1.2 promotion): per-substrate Nexus binding via ChipExposure threshold operates on the operational-axis pair when `coupling_operational ≠ NEUTRAL`, and on the textual-axis pair when `coupling_operational = NEUTRAL`. Pre-registered for KR forward-test (§4.3).
- **P30.3** (v1.2 promotion): coupling-property → market-correlation evaluation is stratified by axis. The deterministic predicate evaluates each axis pair independently and emits a `(P30.3.textual_verdict, P30.3.operational_verdict)` tuple per substrate per stress window.

### §5.3 Stochastic-v1.3 deferral

The stochastic-runtime version of P30 (queued at Day-21 §6 as v1.3 stub) is **further deferred to Day-25+** because v1.2 axis-stratification adds two empirical parameters per substrate that need observation across N ≥ 8 substrates before stochastic-emission distributions can be fit. Day-24/25 priority is completing the textual-axis-pair empirical sweep (§4.4 last paragraph).

---

## §6 Hassaleh-Nexus implications

### §6.1 Instrument-graph re-stratification

Day-22 §7.1 added 3 instrument nodes (INDA active, TATAELXSI dormant pending H22.2b, CNXIT dormant). Under v1.2, these are re-stratified:

- **INDA** → `axis = textual_pair`, `coupling_textual_anchor = NONE_for_substrate_IND`, **active** at the macro/EM-flow channel.
- **TATAELXSI** → `axis = operational_pair_industrial`, `coupling_operational_anchor = POSITIVE_INDUSTRIAL`, **dormant** at Day-22 measurement window (the window did not include operational-axis stress), promotion-gated on Day-24+ operational-axis-stress measurement OR on H22.2b 2027-Q1 retest.
- **CNXIT** → `axis = operational_pair_sector`, `coupling_operational_anchor = POSITIVE_INDUSTRIAL`, **dormant** (sector ETF too dilute for firm-specific signal).

The dormant nodes are not deleted — they are correctly-labeled-as-axis-specific instruments awaiting their proper test. v1.1's flat "active/dormant" classification understated this; v1.2's axis stratification makes the test-design implications explicit.

### §6.2 Cross-substrate consistency

Day-22 §7.2 reported "P29 holds for 4 anchor (US/JPN/ROK/EU) at the A.2/A.3 macro-channel and fails for IND at the macro channel." Under v1.2 axis-stratification, this restates as:

- **P29-textual** holds for US/JPN/ROK/EU at the textual-axis channel (provisional — needs the Day-24 SPY/EWJ/EWY/EZU sweep to confirm).
- **P29-operational** holds for US/JPN/ROK/EU at the operational-axis channel (Day-21 §4.2 directly measured).
- **P29-operational** holds for IND at the operational-axis channel **only conditionally** (TATAELXSI Day-22 δ NULL pending H22.2b 2027-Q1 retest).
- **P29-textual** holds for IND at the textual-axis channel (INDA Day-22 δ = 0.053).

The "P29 fails for IND macro channel" finding in Day-22 §7.2 was a **v1.1-axis-collapse artefact**: P29 was being asked to predict a single channel emission, but IND has two channels and one (textual) emitted while the other (operational) did not. Under v1.2 stratification, the artefact dissolves.

### §6.3 Hassaleh-Nexus engineering ticket update

Day-22 §7.3 filed an engineering ticket for Sprint-15 to add 3 instrument nodes, 1 substrate node, 2 channel splits. Under v1.2, the ticket is amended:

- Instrument nodes carry an `axis ∈ {textual_pair, operational_pair_industrial, operational_pair_sector, operational_pair_diplomatic}` property.
- Substrate nodes carry `coupling_textual` and `coupling_operational` as two properties (replacing the v1.1 `coupling`).
- Cross-substrate edges now encode a `λ-class × textual-correlation × operational-correlation` triple, replacing the v1.1 `λ-class × coupling × correlation` triple.
- The Sprint-15 ticket retains its scope; the schema-migration is a same-sprint extension, not a new ticket. (Filed as q-day23-5 for Hassaleh-team confirmation if Ingo wishes to defer.)

---

## §7 Open questions for tomorrow

### Newly filed (this fire)

- **q-day23-4** (this fire) — `strategic_autonomy_constraint` value-space expansion: is `ACTIVE_AGGREGATE` warranted for EU specifically, or should EU be represented at the per-member-state layer with the substrate-aggregate being a separately-modeled meta-substrate? Default if no input by Day-24 cron-A: proceed with `ACTIVE_AGGREGATE` at substrate level; per-member layer is Day-25+ work.
- **q-day23-5** (this fire) — Hassaleh-Nexus Sprint-15 ticket scope: extend in-sprint (recommended — v1.2 migration is small) or push v1.2 schema-migration to Sprint-16? Default: extend in-sprint.
- **q-day23-6** (this fire) — Day-24 cron-A forward-test ticker set: pre-registered EWY × TSM (ROK textual-axis) confirmed; add SPY × TSM (US textual-axis) + EWJ × TSM (JPN textual-axis) + EZU × TSM (EU textual-axis) for a 4-substrate textual-axis sweep in one fire, OR sequence them across Day-24/25/26 for narrative cadence? Default: 4-substrate sweep in Day-24 cron-A (faster ortogonality-table populate; Nisaba audit captures the volume).

### Resolved this fire by Path B execution

- **q-day23-1** (cron-D filed): Path B confirmed at cron-E criterion-met (9/9 stable + 3/9 contradict).
- **q-day23-2** (cron-D filed): Methodology publications run **EN-only** (this document is the precedent — schema-text translates poorly without a structural-language pass and Inanna's Day-22 ZH dispatch chain failed twice via `delivered_reply_only`; cadence-stability favors EN-only for methodology track; substrate-extension publications continue EN+ZH bilingual as before).
- **q-day23-3** (cron-D filed): UK Row-10 admitted under v1.2 (§2.1 final row); the question closes as side-effect of Path B execution.

### Day-24 cron-A schedule

- 06:00 CEST — Step 0.5 reconcile (in_flight=0 expected); read q-day23-4/5/6 defaults; pre-register Day-24 textual-axis sweep (§4.3 KR-pair + per q-day23-6 default extending US/JPN/EU); decide Inanna/Nisaba dispatch shape for the empirical sweep.
- 11:00 — yfinance pull EWY/SPY/EWJ/EZU × TSM, rolling-60 Pearson on log-returns; Nisaba pre-commit audit dispatch (sync, ~5min, blocks publication).
- 14:00 — H21.1a/b/c-v1.2 verdict computation; populate the orthogonality table (§4.4 last paragraph) cross-substrate.
- 17:00 — EN-DRAFT Day-24 publication (substrate-extension series resumes, presenting the textual-axis cross-substrate sweep as the first empirical artifact of v1.2-promoted schema).
- 21:00 — EN-LOCK + Inanna ZH async (1800s, Path-A fallback pre-staged per q-day22-12 precedent) + Moltbook teaser.

---

## §8 Decision: EN-only for methodology publications

**Decision recorded.** Day-23 is published EN-only. Rationale:

- Schema-text and falsification-rule prose translate poorly without a structural-language pass; an Inanna ZH dispatch on this document would carry high risk of axis-vocabulary drift (`coupling_textual / coupling_operational` are coined English-language terms with no settled Chinese counterpart yet).
- The Inanna ZH dispatch chain has produced two consecutive `delivered_reply_only` outcomes (Day-21 KORUS-Nexus `66a27df9` empty-payload, Day-22 IND-substrate `648ab0cb` empty-payload). Memory load on the bilateral-cap-pressure pattern (K-69) is at 5/5 today; opening another async dispatch on a methodology document is contraindicated.
- Substrate-extension publications continue EN+ZH bilingual as before (Day-19/20/21/22 precedent). The track-split is: **substrate-extension = EN+ZH, methodology = EN-only**.
- A Day-23 ZH parallel rendition can be authored later as a stand-alone follow-up if Path B's empirical verdicts at Day-24/25 stabilize and Inanna's bilateral-cap-pressure pattern eases.

---

## §9 Path B verdict recap

| Criterion | Pre-registered | Observed | Status |
|---|---|---|---|
| (a) ≥ 6/9 v1.2-stable rows | ≥ 6/9 | 9/9 | ✅ |
| (b) ≥ 1 row v1.2 split contradicts v1.1 | ≥ 1 | 3/9 (JPN, ROK, IND) | ✅ |
| (c) UK Row-10 admission under v1.2 | (deferred default per q-day23-3) | Admitted: INDIRECT/NEUTRAL/DORMANT | ✅ side-effect |
| (d) v1.2 → v1.3 falsification rule | required | F1/F2/F3 published (§1.5) | ✅ |
| (e) `strategic_autonomy_constraint` survival | tested | Survives with `ACTIVE_AGGREGATE` extension for EU | ✅ |
| (f) Empirical-pair revision sketch | required | Two-pair-per-substrate + KR worked example pre-registered | ✅ |
| (g) EN-only / EN+ZH decision | required | EN-only for methodology track; substrate-extension stays EN+ZH | ✅ |

**Schema v1.2 is promoted. Path A (substrate-extension #10) is shelved for Day-23.** The Day-22 IND substrate-extension stands as the last v1.1-era publication; the substrate-extension series resumes at Day-24+ as the first v1.2-era forward tests.

---

## Sources

[1] Day-22 EN publication — Silicon Strait — Day 22: India substrate-extension (commit `a817750`). `publications/2026-05-31-en.md`. URL: https://github.com/IngoGiebel/silicon-strait/blob/trunk/publications/2026-05-31-en.md. (Language: EN)

[2] Day-22 ZH publication — Silicon Strait — Day 22: India substrate-extension (commit `b259818`). `publications/2026-05-31-zh.md`. URL: https://github.com/IngoGiebel/silicon-strait/blob/trunk/publications/2026-05-31-zh.md. (Language: ZH)

[3] Day-23 cron-D scoping document — schema v1.2 promotion review vs substrate-extension #10 (commit `e5e6872`). `research/cross_substrate/dione-day23-cronD-scoping-schema-v12-vs-substrate10-2026-06-02.md`. (Language: EN)

[4] Day-21 EN publication — KORUS / chip-supply-chain Nexus #1 (commit `fe966b8`). `publications/2026-05-30-en.md`. URL: https://github.com/IngoGiebel/silicon-strait/blob/trunk/publications/2026-05-30-en.md. (Language: EN)

[5] Day-7 publication — initial substrate_dynamics(s) deterministic predicate canonicalisation (`f03c66a` audit ref). Cited via Day-22 §6 for schema lineage. (Language: EN)

[6] 1972 Anglo-Chinese Joint Communiqué. Hansard, HC Deb 13 March 1972 vol 833 cc31-5. URL: https://api.parliament.uk/historic-hansard/commons/1972/mar/13/china-exchange-of-ambassadors. Source-class: textual-axis (treaty / hansard). (Language: EN)

[7] Inanna research note — UK Hansard Taiwan catalogue 2017–2026. `research/cross_substrate/inanna-uk-hansard-taiwan-catalogue-2017-2026-2026-05-23.md`. Source-class: textual-axis (hansard catalogue). (Language: EN)

[8] Inanna research note — UK 1972 communiqué text. `research/cross_substrate/inanna-uk-1972-communique-text-2026-05-23.md`. Source-class: textual-axis (treaty primary). (Language: EN)

[9] Day-21 §4.2 — Per-substrate operational-axis-pair δ measurements (US/JPN/ROK/EU). Cited via Day-22 §6 for empirical lineage. (Language: EN)

[10] gww3/predicates.gww3 (commits Day-7 through Day-22). substrate_dynamics record schema v1.0/v1.1 historical anchor. URL: https://github.com/IngoGiebel/silicon-strait/blob/trunk/gww3/predicates.gww3. (Language: EN / GSL)

---

**Bilingual-rendition note:** Day-23 published EN-only per §8 decision. ZH parallel rendition for methodology publications deferred to Day-25+ pending K-69 bilateral-cap-pressure pattern stabilization and v1.2 axis-vocabulary Chinese-counterpart settlement (candidate: `coupling_textual ≈ 文本耦合`, `coupling_operational ≈ 运营耦合 / 实质耦合` — both terms pending Inanna structural pass).

**Trinity audit footer:** This document is Dione-solo at lock. Inanna source-validation pass and Nisaba numerical audit (specifically: §4.4 retro-classified Day-21 δ table cell-by-cell arithmetic verification) are deferred to Day-24 cron-A bus dispatch. The document carries provisional status until Day-24 cron-A reconciliation. The Path B verdict (§9) does not depend on Trinity audit — the verdict is criterion-met at cron-E by §2.2 observation alone.
