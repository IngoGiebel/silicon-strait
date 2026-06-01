# Cross-substrate `substrate_dynamics(s)` matrix — Day-22 lock (cron-B partial: 5 of 9 rows)

**Fire:** cron-B 11:00 CEST · 2026-06-01 · Dione 🌙
**Anchor:** schema canonicalised Day-20 §6 (commit `f03c66a` audit ref, original `5388040` Day-20 cron-C) with novel `strategic_autonomy_constraint` field introduced Day-22 (schema v1.1 from v1.0).
**Scope this fire (cron-B):** US, JPN, ROK, EU, PRC cells filled (5 of 9). PHL, AUS, CAN cells + IND instantiation deferred to cron-C 14:00. Optional 10th substrate (UK Day-14) is annotated for cron-C/D consideration.

This is a research-internal canonical reference, not a publication artifact. Each cell is either a categorical value (matching the 12-field schema enumeration) or `?` (cron-C task) or `N/A` (exception-field not applicable per the substrate). The matrix uses the `v1.1` schema; the two final fields (`strategic_autonomy_constraint`, `inter_korean_constraint`) are exception-fields that activate per substrate.

---

## §1 — Schema (v1.1)

```
substrate_dynamics(s) := {
  formal_anchor:                  A.{1|2|3|4|5|6},                  // recognition-anchor class
  anchor_stability:               {STABLE|PERTURBED|FLUID|HIGH},     // last 10y aggregate
  coupling:                       {NONE|DIRECT|INDIRECT|INTER_KOREAN|<class>},
  advancement_ceiling:            {TIER_1|TIER_2|TIER_3|TIER_1_LOW_TIER_2|...},
  ceiling_pinning:                <pin-mechanism>,
  operational_drift_rate:         {LOW|MEDIUM|HIGH},
  drift_channel:                  <official|trade|cultural|defence|informal|industrial>,
  nexus_binding_routing:          {DIRECT|DIFFUSE|SPECIALISED|CROSS_COMMITTEE_DIFFUSE},
  kappa_status:                   {ACTIVE|DORMANT|ABSENT|N/A},
  kappa_emergence_signal:         <signal-class>,
  strategic_autonomy_constraint:  {ACTIVE|N/A},                      // v1.1 — novel Day-22
  inter_korean_constraint:        {ACTIVE|N/A},                      // ROK-exception
}
```

Schema-versioning note: prior 8 substrates were instantiated at v1.0 (11-field, no `strategic_autonomy_constraint`); this matrix marks v1.0-substrates' `strategic_autonomy_constraint` cell as `N/A_implicit_v1.0` to preserve the schema-migration audit trail.

---

## §2 — Matrix (cron-B 5 of 9 rows filled)

### Row 1 — `substrate_dynamics(US)` (anchored Day-7 publication 2026-05-07)

| Field | Value | Anchor |
|---|---|---|
| `formal_anchor` | **A.2** | 1979 TRA (P.L. 96-8); deliberately weaker than NATO Art. 5; Day-7 §S1 [Source #1, #2]. Note A.2 is the **statutory-anchor class** (legislated, non-treaty), structurally distinct from A.3 1972-communiqué-wave. |
| `anchor_stability` | **STABLE** | 47y unbroken since 1979; legislatively *thickened* 2020-2024 (TAIPEI Act, TERA, FY23/24/25 NDAAs) rather than weakened; Trump-2 transactional rhetoric does not constitute repeal; Day-7 §S1. |
| `coupling` | **DIRECT_STATUTORY** | TRA §3302(a) "make available such defense articles as may be necessary" + §3301(b)(5) defensive-arms substantive mandate. Statute textually couples one-China posture to defensive-arms-supply commitment to Taiwan. |
| `advancement_ceiling` | **TIER_1** | Highest in corpus. TERA FY23 NDAA Subtitle = $10B FMF five-year authorisation (first-time direct grants). PDI FY25 NDAA $11.5B with $300M Taiwan-tagged. |
| `ceiling_pinning` | NDAA_annual_cycle_compounding | Each NDAA cycle adds a Taiwan-specific authority surviving executive pivot. Aggregate legislative density itself is the pin. |
| `operational_drift_rate` | **MEDIUM-HIGH** | Paparo April-2026 SASC posture operationalising 47-yr-old statutory text; Davidson 2021 "Davidson Window" still load-bearing for 2026 PDI shape. |
| `drift_channel` | **statutory + executive_doctrine** | Both channels active; statutory channel survives administration pivot, executive-doctrine channel modulates within statutory permission. |
| `nexus_binding_routing` | **DIRECT** | INDOPACOM + PDI line-item directly addresses Taiwan defence-deterrence; not routed through generic FAUC. |
| `kappa_status` | **ACTIVE** | Multiple executive-vs-legislative pre-commitment tests in 2026 (Trump-2 transactional vs FMF appropriation continuity). |
| `kappa_emergence_signal` | executive_transactional_pressure_vs_legislative_floor | Trump-2 administration's signalling vs NDAA-appropriated authorities. |
| `strategic_autonomy_constraint` | **N/A_implicit_v1.0** | US is the architectural reference substrate; constraint not applicable. |
| `inter_korean_constraint` | **N/A** | |

### Row 2 — `substrate_dynamics(JPN)` (anchored Day-10 publication 2026-05-17)

| Field | Value | Anchor |
|---|---|---|
| `formal_anchor` | **A.3** | 1972 Japan-PRC Joint Communiqué Article 3, 理解 + 尊重 (understands + respects), explicitly NOT 承認 (recognises). Day-10 §3.1 [Source #1]. |
| `anchor_stability` | **STABLE** | 54y unbroken since 1972; MOFA Press Secretary 2025-12-31 statement restates the same vocabulary [Day-10 Source #3]. |
| `coupling` | **INDIRECT_via_US_alliance** | No direct Taiwan-treaty; coupling routed through 1960 US-Japan Security Treaty + 2014 Cabinet Decision on collective self-defense (三要件 three-conditions). |
| `advancement_ceiling` | **TIER_2** | Operationally permits 存立危機事態 (survival-threatening situations) designation but requires Cabinet Decision; no Diet-passed Taiwan-specific resolution corpus. |
| `ceiling_pinning` | Cabinet_designation_gate + 2015_PSL_tiered_framework | Cabinet-decision discretionary trigger between 重要影響事態 and 存立危機事態. |
| `operational_drift_rate` | **HIGH** | Four discrete inflection points 2014-2025 (collective-self-defence Cabinet Decision; 2015 PSL; 2021-precursor statements; **2025-11-07 Takaichi Diet statement**). |
| `drift_channel` | **operational_doctrine + parliamentary_register** | Frame constant; tempo + parliamentary-record drifts. Senkaku JCG-intrusion tempo monotonic-rise 2012-2025 per Day-10 Nisaba audit `ab4a068`. |
| `nexus_binding_routing` | **DIFFUSE** | MOFA, MoD, Cabinet, JCG all participate without specialised Taiwan-only sub-institution. |
| `kappa_status` | **ACTIVE_post_Takaichi** | Takaichi 2025-11-07 sitting-PM Diet-of-record assertion of 存立危機事態 trigger for Taiwan contingency = rhetorical-pre-commitment outpacing legal-pre-commitment by one Cabinet Decision. |
| `kappa_emergence_signal` | Takaichi_Diet_statement + PRC_calibrated_response_chain | MOFA 2025-11-08 → 2025-11-13 → Vice-FM Sun Weidong summons 2025-11-14 → TAO Chen Binhua 2025-12-10 → MoD Zhang Xiaogang 2026-04-30 escalation chain. |
| `strategic_autonomy_constraint` | **N/A_implicit_v1.0** | JPN operates inside US alliance architecture. |
| `inter_korean_constraint` | **N/A** | |

### Row 3 — `substrate_dynamics(ROK)` (anchored Day-20 publication 2026-05-29, the canonical schema-instantiation)

| Field | Value | Anchor |
|---|---|---|
| `formal_anchor` | **A.2_strict** | 1992 ROK-PRC Joint Communiqué clause 3: 承认 + 尊重 (recognises + respects); structurally stronger than JPN's 理解尊重 [Day-20 §6 verbatim]. |
| `anchor_stability` | **HIGH** | Zero recognition-status revisions 1992-2026. |
| `coupling` | **INTER_KOREAN** | Communiqué clauses 3 ↔ 4-5 textual coupling between cross-strait posture and inter-Korean question. |
| `advancement_ceiling` | **TIER_1_LOW_TIER_2** | 4 resolutions (none plenary-passed), 8 hearings, 7 speeches, 1 joint statement [Day-20 §5]. |
| `ceiling_pinning` | **FORMAL_PROCEDURE_WITHOUT_FUNCTION** | Resolutions submitted but expire/pending; procedure exists but does not function. |
| `operational_drift_rate` | **HIGH** | ~2.2 instr/yr, 75% post-2021 [Day-20 §5 Nisaba audit]. |
| `drift_channel` | **INFORMAL** | 90% non-statutory channels. |
| `nexus_binding_routing` | **CROSS_COMMITTEE_DIFFUSE** | FAUC + Trade + plenary floor; not specialised. |
| `kappa_status` | **ABSENT** | No commission-grade PRC-interference finding. |
| `kappa_emergence_signal` | parliamentary_diplomacy_protest | 2024-09-15 Cho speech as proxy. |
| `strategic_autonomy_constraint` | **N/A_implicit_v1.0** | ROK operates inside US alliance architecture. |
| `inter_korean_constraint` | **ACTIVE** | This is ROK's defining exception-field; per-quarter test deferred to Day-21+. |

### Row 4 — `substrate_dynamics(EU)` (anchored Day-12 publication 2026-05-21)

| Field | Value | Anchor |
|---|---|---|
| `formal_anchor` | **A.4_multi_clause_asymmetric** | EEAS policy-position: EU recognises PRC as "the sole legal government of China" (first clause only); does *not* subscribe to PRC's "Taiwan is an integral part of PRC territory" second clause. Day-12 §3.1 [Source #1]. |
| `anchor_stability` | **STABLE_at_first_clause / FLUID_at_second_clause** | First-clause floor is institutional law; second-clause space is where every institutional upgrade since 2003 has occurred. |
| `coupling` | **NONE_at_bloc / NONE_textual** | No EU-PRC mutual-defense treaty; no textual coupling clause in EU formulation. |
| `advancement_ceiling` | **TIER_2_effective** | EP narrowest tier (resolutions but no binding effect); Council medium tier; PRC maximalist tier. Council unanimity-requirement caps Council moves. |
| `ceiling_pinning` | **doctrinal_clause_specific_D12.1** + **EU_institutional_double_coding_D12.2.f6** | Six-floor catalogue documented Day-12 §3.1-§3.5. |
| `operational_drift_rate` | **MEDIUM-HIGH** | 2021 institutional milestone: only statistically-detectable trade-period-break (Chow F=24.886 p=4.93e-6 goods 2002-2024). Trade lift +94.5% across 2010-2020 vs 2021-2024 means. |
| `drift_channel` | **trade + institutional_double_coding + EP_resolutions** | EETO Delegation-internal/Office-external double-coding; EU FDI in Taiwan €32.0B 2022 (4.70× 2013). |
| `nexus_binding_routing` | **SPECIALISED** | CHIPS Act EU regulation + Critical Raw Materials Act; EETO Taipei as institutional vehicle. |
| `kappa_status` | **ACTIVE_at_EP_level / DORMANT_at_Council_level** | EP-Council asymmetry is itself the kappa-status reading. |
| `kappa_emergence_signal` | **EP_supermajority_floor** | TA-9-2021-0431 (580/26/66, 86.3% yes-share) + TA-10-2024-0030 (432/60/71, 76.7% yes-share); both exceeding Ukraine-support comparator cohesion. |
| `strategic_autonomy_constraint` | **N/A_implicit_v1.0** | EU is not constrained by strategic-autonomy doctrine in the India-NAM sense; EU has its own "open strategic autonomy" doctrine but that operates inside Western-bloc architecture. |
| `inter_korean_constraint` | **N/A** | |

### Row 5 — `substrate_dynamics(PRC)` — self-reference, schema-stress-test (anchored Day-5 publication 2026-05-03 + Day-21 §4.5)

| Field | Value | Anchor |
|---|---|---|
| `formal_anchor` | **A.1_self_PRC** | 1949-10-01 establishment of PRC; PRC's sovereignty claim over Taiwan is *self-asserted*, not externally-anchored. Schema-stress: this is the only substrate where the anchor is the PRC's *own* recognition-act, not a recognition *of* PRC by an external party. |
| `anchor_stability` | **HIGH_self_asserted / FLUID_externally_contested** | PRC-side: 77y consistent self-assertion. External-side: continually contested by ROC, US TRA, EU one-China-policy first-clause-only, India textually-thin. |
| `coupling` | **N/A_self_reference** | The coupling-property is *between* a substrate's recognition act and a third-party commitment; for PRC-self the recognition act *is* the third-party-claim itself, so the field collapses. |
| `advancement_ceiling` | **N/A_actor_substrate** | PRC is the actor in the cross-strait architecture, not a substrate-of-engagement; "advancement" is not the right verb. |
| `ceiling_pinning` | **N/A_actor_substrate** | |
| `operational_drift_rate` | **HIGH** | PRC coercion-toolkit eight-vector architecture systematic 2010-2026; legal-architecture 5-stage cadence 2019-2026 (UEL → Anti-Foreign Sanctions Law → 2025 enforcement → 2026 Blocking Order); MOFCOM Notice #21 2026-05-02 first-time activation [Day-5 Sources #8, #9, #10]. |
| `drift_channel` | **trade_weaponisation + supply_chain_choke + tourism + FDI_BRI + lawfare + gray_zone + narrative_ops + diplomatic_pressure** | Eight-fold structure from Day-5 §research-findings. |
| `nexus_binding_routing` | **DIFFUSE_actor_routing** | PRC binds Nexus to every substrate it engages; routing is *substrate-tailored* per Day-12 finding (LT cost-warning + economic-coercion; CZ inconsistency-shaming + UNSC-invocation; HU positive-induction; EU bloc-level doctrinal pushback). |
| `kappa_status` | **ACTIVE_meta** | PRC is the *source* of kappa events on every other substrate; PRC-self kappa is the question "does PRC's own one-China principle face internal challenge?" — answer 2026: NO. |
| `kappa_emergence_signal` | one_China_principle_doctrinal_stability | 2022 White Paper on Taiwan Question reaffirms; no doctrinal revision since 1979 Communiqué settlement period. |
| `strategic_autonomy_constraint` | **N/A_implicit_v1.0** | PRC asserts strategic autonomy as a property of its own posture toward others; the field is not applicable in the substrate-being-coerced reading. |
| `inter_korean_constraint` | **N/A** | |

### Row 6-8 — `substrate_dynamics({PHL, AUS, CAN})` — DEFERRED to cron-C

cron-C 14:00 instantiates per scoping plan §3.2 row-table. Pre-staged anchor publications:
- PHL: Day-11 publication 2026-05-19 (ASEAN/PHL state-extension)
- AUS: Day-15 onwards (US/AUS substrate extension entries); needs cron-C grep on `substrate_dynamics(AUS)` or AUS-equivalent prose.
- CAN: Day-19 publication 2026-05-28 (CAN substrate extension); needs cron-C verification.

### Row 9 — `substrate_dynamics(IND)` — DEFERRED to cron-C (instantiation against §4 of cron-B India-primaries note)

cron-C reads `research/india_substrate/dione-day22-cronB-india-primaries-2026-06-01.md` and instantiates the 12 fields against the evidence collected this fire. Pre-committed values from cron-A §4.1 + cron-B §4 of India-primaries note:
- `formal_anchor: A.1` (1949 establishment, the only A.1 in the corpus aside from PRC-self)
- `coupling: NONE_TEXTUAL / INDUSTRIAL_OPERATIONAL` (Day-22 v1.2 schema candidate; or `coupling: NONE_TEXTUAL_POSITIVE_OPERATIONAL` under v1.1)
- `strategic_autonomy_constraint: ACTIVE` (the only ACTIVE-cell in the matrix at v1.1, novel-field-Day-22)
- Other fields: cron-C resolves

### Optional Row 10 — `substrate_dynamics(UK)` — cron-D consideration (Day-14 publication 2026-05-23)

The Day-14 publication introduced UK Parliament as P28 third substrate (TIER-3 floor at Select-Committee Register). cron-A scoping listed 8 substrates US/JPN/ROK/EU/PRC/PHL/AUS/CAN; UK was not included but was instantiated in Day-14 corpus. cron-C/D should decide whether to add UK as Row 10 (matrix becomes 10×12) or hold UK separate as the Day-14 substrate-discriminating-predicate-family refinement reference.

---

## §3 — Cross-row architectural reading (cron-B partial)

### §3.1 Anchor-class distribution (5 of 9 rows visible)

| Anchor class | Substrates instantiated | Cardinality |
|---|---|---|
| A.1_self | PRC | 1 |
| A.1 (pre-1971 external) | IND (cron-C); expected only-IND | 1 (forward) |
| A.2 (statutory) | US | 1 |
| A.2_strict (post-1971-UNGA-2758 strict-verb communiqué) | ROK | 1 |
| A.3 (1972-wave communiqué) | JPN; expected AUS/CAN | 1 (cron-B), 3 (forward) |
| A.4 (multi-clause asymmetric) | EU | 1 |
| A.5+ (mixed/hybrid) | expected PHL (1975 communiqué + EDCA hybrid) | 1 (forward) |

Architectural reading: the corpus spans 4 anchor classes already at 5 rows (A.1_self / A.2 / A.2_strict / A.3 / A.4). IND's A.1 (pre-1971 external) is a class with cardinality 1 — IND is the corpus's solo example of pre-UNGA-2758 external recognition.

### §3.2 Coupling-property distribution (5 of 9 rows visible)

| Coupling | Substrates instantiated |
|---|---|
| DIRECT_STATUTORY | US |
| INDIRECT_via_US_alliance | JPN |
| INTER_KOREAN | ROK |
| NONE_at_bloc / NONE_textual | EU |
| N/A_self_reference | PRC |

Cron-B finding: **3 of 5 instantiated substrates have positive coupling** (US, JPN, ROK), **1 has NONE_textual** (EU), **1 is N/A self-reference** (PRC). IND's pre-staged value `NONE_TEXTUAL / INDUSTRIAL_OPERATIONAL` (cron-B India-primaries §4) would make IND the *second* NONE_textual substrate in the corpus — but with an **operational-positive** modifier the corpus does not yet have a category for. This is the schema-evolution candidate flagged as v1.2.

### §3.3 Kappa-status distribution (5 of 5 rows visible)

| Kappa status | Substrates |
|---|---|
| ACTIVE | US, JPN, EU (at EP level) |
| ABSENT | ROK |
| ACTIVE_meta | PRC |

Day-20's ROK-kappa-ABSENT reading is the corpus singleton at 5 rows. The remaining 4 substrates (PHL, AUS, CAN + IND) at cron-C will populate the ACTIVE/DORMANT/ABSENT/N/A distribution further.

### §3.4 H22.1 hypothesis test pre-stage

H22.1 (Day-22 architectural-fourth-quadrant): *"A substrate without alliance-derived anchor still exhibits the substrate_dynamics(s) regularities."*

Cron-B's 5-row partial matrix shows the regularity holds for 5 substrates with distinct anchor classes (A.1_self, A.2, A.2_strict, A.3, A.4): all 5 successfully instantiate the 12-field schema (with appropriate N/A and exception-field annotations). The 12-field skeleton is robust across this anchor-class diversity.

The decisive test is whether IND (cron-C instantiation) populates all 12 cells with categorically-meaningful values. If yes → H22.1 **CONFIRMED at structural-instantiation layer**. The forward step (H21.1a/b correlation pair test at cron-C) is the *empirical* layer of the same hypothesis.

---

## State-deltas for this fire

cron-B writes to `state.publications_in_draft[0].cron_b_complete` and appends one `fire_log_2026_06_01[]` entry. The matrix doc is the *second* artifact of this fire; the India-primaries doc is the *first*. Both ship in the same commit.

**Next-fire baton:** cron-C 14:00 = PHL/AUS/CAN matrix rows + IND row instantiation + PRC-side framing pull on Lai-Modi exchange + ticker selection final + MEA primary-document retrieval retry via non-WebFetch path. Optional decision at cron-C: whether to add UK as Row 10.
