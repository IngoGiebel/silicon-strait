# Day-19 Arc-Pivot Scoping Plan

**Date:** 2026-05-28
**Fire:** 11:00 cron-B (Europe morning)
**Author:** Dione 🌙
**Phase output:** plan document (no publication this fire — per skill §Step-2 `scoping` row)
**Predecessor:** Day-18 P28 cross-substrate consolidation (commits 589369d → 0f23f9b, 2026-05-27)

---

## §1 — Why this scoping fire exists

Day-18 closed the 8-day P28 substrate-extension arc (Days 10–17 substrate pulls → Day-18 consolidation across PHL, EU, JP, KR-pending, AUS, CAN, US — seven substrates, three λ-classes). It is the first natural arc-boundary since Day-9 methodology day. The 06:00 cron-A fire today reconciled the Day-18 ZH dispatch (first clean async delivery in six dispatches: `0f23f9b` written + committed + pushed autonomously by Inanna's worker) and enqueued the Day-18 Moltbook teaser (terminal `posted` at 04:15Z).

**The 11:00 fire's job** per the 06:00 next_fire_intent line: *"Day-19 scoping (begin new arc post-consolidation; await Ingo input on next research thread direction)."* This document is that scoping output.

Day-18 §6.5 (`publications/2026-05-27-en.md`) already named three forward-direction candidates and recommended one. The purpose of this fire is to (a) restate the candidates with concrete first-day plans, (b) flag the cross-cutting decisions Ingo needs to make once, not per-fire, and (c) propose a default trajectory that is executable starting at the next research fire (14:00 cron-C today) if no Ingo input arrives.

## §2 — Three candidate next-arc directions

The Day-18 §6.5 candidates (a/b/c), now expanded into concrete one-day plans.

### Candidate (a) — Substrate extension: South Korea first, India second

**One-day arc starting Day-19 (today's 14:00 cron-C):**

- **Primary research target:** 1992 PRC-ROK normalization communiqué — verbatim ZH text + EN/KO translations, λ-class verb determination (`acknowledge` / `承認` / `承认` / `留意` / `respect` register expected to fall in Class A or B by structural symmetry with JP-1972 and CAN-1970, but ZH text required to confirm).
- **Institutional architecture survey:** ROK National Assembly digitized proceedings (assembly.go.kr), MOFA-ROK Taiwan-related statements, KORUS alliance treaty corpus, Inter-Korean dimension as confound variable (does the PRC use the DPRK lever to constrain ROK Taiwan-statements? — empirical question).
- **P28 predicate evaluation:** Pre-registered before research pull (per skill §Step-3 bias-balance): λ-class prediction = Class B by structural prior (Westminster-derived → A; Japan-Asian-derived under post-1972 normalization frame → B); advancement-ceiling tier prediction = Tier-1 (executive-discretionary, no Tier-2 legislative codification at this time, no Tier-3 enacted-law equivalent).
- **Trinity dispatches expected:** Inanna ⭐ async on 1992 communiqué ZH-text + ROK National Assembly digitized-Hansard catalogue Taiwan-related (≈30 min, target 14:00 cron-C dispatch, reconcile 17:00 cron-D); Nisaba 🌾 sync on PRC-ROK trade-volume + semiconductor-export-share table (Samsung, SK Hynix into PRC-mainland market vs into TW-foundry-chain) (≈5 min, late same fire if §3 numbers emerge).
- **Publication target:** Day-19 EN-LOCK 2026-05-28 21:00 cron-E if substrate is small enough; otherwise Day-19+20 two-day arc EN-LOCK 2026-05-29 21:00 with ZH 2026-05-30 06:00 reconcile.
- **Sources accessibility:** Medium-high. ROK MOFA + National Assembly are accessible; ZH-text of 1992 communiqué archived at MOFA-PRC `fmprc.gov.cn` (verified accessible in Day-15 AUS-1972 pull on the same domain); KO-primary sourcing requires translation discipline but Inanna handles JP-KO pivot acceptably (Day-14 JP-1972 pass was clean).
- **λ-test value:** **High.** This is the single highest-information experiment available in the current sample — a Class-A-or-B prediction with a clean ZH-verb empirical answer, in a substrate that doubles as a major semiconductor actor (binding to Nexus implication §5.4.2 from Day-18).

**India follows (Day-20 or Day-21):**

- **Primary research target:** Absence of bilateral PRC-IND communiqué Taiwan clause as architectural variation. Lok Sabha + Rajya Sabha proceedings on Taiwan; MOFA-IND statements; Modi government's Taiwan-investment policy (Foxconn, semiconductor incentives) as substantive without diplomatic-verb constraint.
- **λ-test value:** **Very high but structurally different** — tests whether P28 explains absence-of-communiqué cases or whether a separate predicate (P29?) is required for "no diplomatic-verb constraint" substrates.

**Risk for (a):** ROK National Assembly digitized-Hansard interface is partially KO-only and the Taiwan-related catalogue may have lower hit-rate than UK/CAN. Mitigation: Inanna dispatch lifts catalogue construction off the cron's wall-time; fallback to MOFA-ROK English statements as secondary floor.

### Candidate (b) — Stochastic-model development

**Methods-day publication (Day-19) + simulation publications (Day-20+):**

- **Methods-day target:** Document the stochastic-extension design — `STOCHASTIC BLOCK` syntax targets for `gsl_ops.lark` v1.3 (already filed as `q9` in state.open_questions_for_ingo[], 2026-05-16), `SAMPLE` primitive (Bernoulli, Categorical, Normal, etc.), `TRANSITION` primitive for state-transition kernels, conditioning syntax (`GIVEN`/`UNDER`).
- **Stochastic targets to be encoded:** S1 — ceiling-movement probability (per-substrate, λ-class-conditioned); S2 — PRC counter-strategy selection (response distribution over substrates); S3 — cross-substrate contagion (intra-cluster transition kernels).
- **Implementation dependency:** **Blocked on Hassaleh engine — `gsl_ops.lark` v1.3.** The deterministic GSL grammar today (q8(A) hoist) cannot express stochastic primitives. The methods-day publication is *design output* not *implementation output* — its value is to crystallize the grammar specification so that the next Hassaleh engine sprint can implement it cleanly.
- **Publication target:** Day-19 methods publication EN+ZH same-day if Inanna can render the design philosophy parallel (lower-information ZH pass than substrate publications, ~15-20 min async).
- **Risk for (b):** **High dependency risk.** Publishing a methods-day on a grammar that does not yet exist creates a documentation-implementation drift hazard. Recommended only if Ingo has bandwidth to schedule the Hassaleh engine sprint that implements v1.3 in the near term (this week / next week). Otherwise the methods-day publication becomes a future-tense design document that may not match the actual grammar when it ships.
- **λ-test value:** **None directly** (this candidate moves the *modeling* axis, not the *empirical* axis).

### Candidate (c) — Hassaleh-Nexus deep-dive

**Three Nexus implication publications (Day-19 + 20 + 21):**

The Day-18 §5.4 consolidation named three Nexus implications:

1. **Semiconductor-supply-chain durability signal** — TSMC capacity, ASML photolithography restrictions, Samsung+SK Hynix (KR substrate dependency), RAPIDUS Japan, ESMC Dresden as tracked instruments. λ-class-conditioned: stronger advancement ceilings → higher cross-strait economic interdependence → higher chip-supply-chain volatility under shock.
2. **Defence-corridor predictor** — arms-sales (US Foreign Military Sales actuals to TW + TW Indigenous Defence Submarine programme + AUS-AUKUS Pillar-2 quantum-and-undersea adjacent procurement). Forward indicator from substrate-level legislative pre-positioning (Tier-2 Hansard motions or floor speeches signaling appropriations).
3. **κ-as-crisis-early-warning signal** — Canadian-style commission-of-inquiry instances as a predictive feature for substrate-level crisis publications. N=1 today (Hogue Commission Foreign Interference 2023-2024) but the structural claim is testable: would similar institutions emerging in other substrates predict crisis events?

- **Day-19 first publication target:** Semiconductor-supply-chain durability signal (Nexus implication #1). Most directly useful for Hassaleh Nexus signal generation — already covered partially in Day-7 economic-statecraft work + Day-17 US-substrate's CHIPS-Act discussion.
- **Trinity dispatches expected:** Nisaba 🌾 sync on instrument-set table construction (≈5-10 min sync); Inanna ⭐ async on EU-side semiconductor-policy primaries (ESMC Dresden, Chips Act EU) parallel rendition (≈15-20 min async).
- **λ-test value:** **None directly** (this candidate moves the *Nexus-binding* axis, not the *empirical* axis).
- **Risk for (c):** Risk of mission-creep into Hassaleh-Nexus codebase territory. Nexus-binding publications must commit to the "publication" output type (markdown report) and not drift into "signal-generation-implementation" output type (Hassaleh-Nexus Python/Kotlin). The boundary is *report on what signals would move, with the methodological argument why*, not *write the signal extractor*.

## §3 — Cross-cutting decisions Ingo needs to make once

These decisions persist beyond Day-19 and currently sit in `state.open_questions_for_ingo[]`:

1. **`q1` — GWW3 stochastic-runtime documentation pointer.** Still unresolved. If candidate (b) is chosen, this becomes blocking before Day-19 starts.
2. **`q9` — Hassaleh `gsl_ops.lark` v1.3 grammar extension.** Filed 2026-05-16; status null. Day-19 candidate (b) is hard-blocked on this. Even under candidate (a) or (c), some publications eventually need v1.3 grammar to advance the GWW3 framing beyond the current local-hoist workaround.
3. **`q-day15-moltbook-teaser-backlog` — submolt tag confirmation.** Still null. Day-15 + Day-16 teasers are queued-pending. Day-18 teaser went out under `geopolitics` (skill-default fallback). Backlog is 2-deep right now. If `geopolitics` is the accepted final answer, the carrying-cost is zero; if Ingo wants `gww3` (project-specific submolt) then the backlog needs a one-fire backfill to switch tag.
4. **`q10` — errata policy for posted publications.** Filed 2026-05-16; status null. Day-8 EN/ZH had one misquoted citation flagged by Inanna validation; commit `6a5a1be` audit committed but no retroactive patch on publications. Default (A) — audit-as-canonical-correction — still standing. Question whether this default propagates to future audits or whether Day-19+ adopts a different errata policy.

## §4 — Recommended default trajectory (if no Ingo input by 14:00 cron-C)

**Direction (a) — South Korea substrate extension, Day-19 single-deep or Day-19/20 two-day arc.**

Justification:
- Highest-information-per-fire empirical experiment available in the current sample.
- No dependency blockers (sources accessible, language-pivot well-understood, λ-class prediction pre-registerable).
- Directly answers Day-18 §6.5 (a) recommendation without requiring grammar work.
- Strengthens semiconductor-supply-chain Nexus implication (#1 in candidate (c)) as a side effect — KR substrate is both a state-extension test case and a semiconductor-actor case.
- Single-fire dispatchable starting 14:00 cron-C if no Ingo input arrives by then.

14:00 cron-C plan under default trajectory:
1. Pre-register P28 prediction for ROK in `research/kr_state_extension/p28-pre-registration-2026-05-28.md` (Class B, Tier-1 ceiling, no κ).
2. Dispatch Inanna async on 1992 communiqué ZH-text + ROK National Assembly Taiwan-related catalogue (≈30 min, reconcile 17:00 cron-D).
3. Dione-direct pull of MOFA-ROK English statements + KORUS treaty corpus + secondary-source survey while Inanna runs.
4. By 17:00 cron-D: §1 institutional architecture EN-DRAFT + §2 1992 communiqué λ-class determination + Inanna catalogue integrated.
5. 21:00 cron-E: §3-§5 + §6 + §7 + EN-LOCK if scope compressible to single day; otherwise EN-LOCK Day-20 21:00.

## §5 — Open questions specifically generated by this scoping

To be appended to `state.open_questions_for_ingo[]` after this fire:

**`q-day19-arc-direction-20260528T1100`** — Day-19 arc-direction confirmation: candidate (a) South Korea substrate extension (default; high empirical value, no blockers), or override to (b) stochastic methods-day (blocked on q1+q9 resolution), or (c) Nexus deep-dive starting with semiconductor-supply-chain signal (zero new substrate data, leverages existing Day-7+17 work)? *Default if no answer by 14:00 cron-C: (a) South Korea.*

**`q-day19-kr-depth-20260528T1100`** — If (a) chosen: single-deep Day-19 (21:00 EN-LOCK target, compressed scope: 1992 communiqué + institutional-architecture survey + P28 evaluation, defer KORUS deep-pass) or two-day arc Day-19/20 (KORUS treaty corpus + Inter-Korean DPRK lever as confound variable get full Day-20 treatment)? *Default: two-day arc — ROK substrate has higher institutional density than PHL/CAN single-day arcs and a compressed Day-19 would risk repeating the Day-10 ASEAN/PHL conflation pattern.*

**`q-day19-india-sequencing-20260528T1100`** — India as Day-20 or Day-21 follow-on: structurally different test (no communiqué Taiwan clause → tests P28 boundary condition) but lower urgency than ROK. Sequence ROK → India directly, or interleave a Day-20 Nexus implication publication (candidate (c) #1 semiconductor-supply-chain) between ROK and India to break the substrate-extension monotony? *Default: ROK (Day-19/20) → semiconductor-supply-chain Nexus implication #1 (Day-21) → India (Day-22+), three-publication arc.*

## §6 — What this scoping does NOT decide

Out of scope for this fire (deferred to future fires once §5 questions resolve):

- The actual content of any Day-19 publication — no source pulls, no predicate evaluations, no GSL drafting in this fire.
- The `gsl_ops.lark` v1.3 grammar specification — that work belongs in candidate (b) if and when chosen.
- The Hassaleh-Nexus signal-extractor implementation — explicitly out of scope per §2 (c) risk note.
- The Moltbook teaser submolt-tag final answer — q-day15 carry-forward remains the canonical entry for that decision.
