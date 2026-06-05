# Day-26 cron-A Scheduling-Conflict Resolution — H26.1 vs H25.2 at cron-C

**Filed:** Day-26 cron-A (2026-06-05 06:00 CEST)
**Filed by:** Dione 🌙
**Resolves:** q-day25-3 (H25.2 execution-fire choice; default Day-26 cron-A had been q-day25-3's path)
**Cross-references:** H26.1 queue (`d17a3c3`, file `dione-day26-cronA-h24_1-firm-level-retest-queue-2026-06-04.md`, §5 conflict flag) · H25.2 pre-registration (`04a6c82`, file `dione-day25-cronB-eu-member-state-decomposition-pre-registration-2026-06-04.md`, §execution-fire-choice)

---

## §1 The conflict

Both H26.1 (firm-level 4-substrate re-test under M-25-1) and H25.2 (EU member-state decomposition) were pre-registered at Day-25 cron-B/cron-D. Both nominally execute via the same compute/audit slot — typically the cron-C 14:00 CEST slot, where the Nisaba sync-audit dispatch lands and the publication-day verdict crystallises.

The H26.1 queue file (§5) flagged the conflict explicitly:

> **NOTE: H25.2 and H26.1 cannot both execute at Day-26 cron-A.** Either H25.2 executes first and H26.1 moves to Day-26 cron-C, or H26.1 executes first and H25.2 moves to Day-26 cron-D / Day-27 cron-A.

This file resolves the conflict at the actual cron-A scoping fire, before any data is pulled.

## §2 Decision

**H26.1 runs first. H25.2 defers.**

| Test | Execution fire | Pre-stage fire | Audit fire |
|---|---|---|---|
| **H26.1** (firm-level 4-substrate re-test under M-25-1) | **Day-26 cron-C 14:00 CEST 2026-06-05** | Day-26 cron-B 11:00 CEST 2026-06-05 | Day-26 cron-C 14:00 CEST (Nisaba sync dispatch, identical-fire) |
| **H25.2** (EU member-state decomposition) | **Day-27 cron-C 14:00 CEST 2026-06-06** *(provisional; downgrade to Day-26 cron-D 17:00 CEST iff Day-26 cron-C closes with budget remaining)* | Day-27 cron-B 11:00 CEST 2026-06-06 *(or Day-26 cron-D if downgraded)* | Day-27 cron-C 14:00 CEST (Nisaba sync) *(or Day-26 cron-D if downgraded)* |

## §3 Rationale

H26.1 takes priority for three load-bearing reasons:

### §3.1 M-25-1 closure depends on H26.1, not on H25.2

The Day-25 cron-D publication adopted protocol amendment M-25-1 (`005930.KS` replaces `EWY` as the ROK textual-axis ticker) **prospectively**. The amendment is provisionally adopted but not yet **closed as cross-substrate-corroborated**. H26.1 is the falsification gate that closes M-25-1 at the cross-substrate level: if the M-25-1-amended ROK ticker still places ROK at the bottom of the corpus with negative δ (the Day-24 H24.1 FAIL pattern), the amendment's directional-prediction rehabilitation collapses and Sprint-15 T1 (vocabulary lock) is forced into active revision.

H25.2 addresses a separate puzzle — the Day-24 EU/EZU overshoot surprise (δ_EZU = +0.0796 above its [−0.03, +0.05] interval) — and disambiguates between active-aggregate amplification (path a) and EZU measurement artifact (path b). Neither outcome of H25.2 directly affects the M-25-1 closure. H25.2 is important but **not load-bearing for the current sprint's vocabulary-lock gate**.

### §3.2 H26.1 is the natural successor to Day-25's H25.1 verdict

Day-25 H25.1 produced `δ_005930.KS × TSM = +0.0546` (b_measurement_quality, marginal, in-interval at the bottom edge of `[+0.05, +0.10]`). The directional implication — does the firm-level signal recover the corpus-level cross-substrate ordering predicted by the original H24.1? — is the immediate next question H25.1 raises. Running H26.1 at Day-26 cron-C maintains the day-over-day continuity of the firm-level disambiguation arc (H25.1 → H26.1) and lets the publication frame the verdict as a coherent two-step closure of the M-25-1 amendment work.

Deferring H26.1 by a day would split this arc and force a more complicated framing at Day-27.

### §3.3 H25.2 has natural carry-room; H26.1 does not

H25.2's intervals were pre-committed at `04a6c82` on Day-25 cron-B 11:00 CEST 2026-06-04. The EWG/EWQ/EWN × TSM data window is identical to H25.1/H26.1 (2022-10-04..2026-05-29), the stress anchors are identical (DUV 2023-01-27, LAI 2024-01-13, PRC 2025-10-10), and the method is identical (rolling-60 Pearson, ±20 td stress vs baseline). One additional calendar day of carry on H25.2 incurs zero data-drift risk and no change to the falsifiability terms.

H26.1's framing as the M-25-1 closure gate, by contrast, has Sprint-15 vocabulary-lock semantics attached. The sprint window (`2026-06-04 → 2026-06-18`, per `IngoGiebel/hassaleh-nexus/issues/sprint-15-v12-migration.md` at commit `e648649`) treats M-25-1 closure as T1 in-scope. Earlier closure is better for sprint progress; later H25.2 closure costs nothing relative to its own constraints.

## §4 Conditional downgrade path

If Day-26 cron-C closes with sufficient time-budget remaining after H26.1 verdict + Nisaba audit lands (concretely: H26.1 verdict crystallises by 14:45 CEST, Nisaba audit returns by 15:30 CEST, **and** Inanna's source-validation dispatch for H26.1 is async-queued not in-progress), then H25.2 **may** be pulled forward to Day-26 cron-D 17:00 CEST:

- Pre-stage harness at cron-C remaining-budget tail (after audit lands).
- Execute at cron-D.
- Audit at cron-D inline (Nisaba second-dispatch of the day).
- Publication at cron-E 21:00 CEST as a same-day two-test verdict.

The downgrade is **default-no**: cron-D defaults to the Day-26 EN-DRAFT publication of H26.1 verdict, and H25.2 stays at Day-27 cron-C. Only an explicit Dione decision at cron-C tail flips the downgrade.

## §5 Pre-committed integrity

Per H26.1 queue §8 ("pre-commitment integrity") and H25.2 pre-registration §3.2 (ticker-deviation rationale), this scheduling resolution **does not modify** any numeric commitment, interval, or method specification for either test. It only assigns execution fires.

If Ingo prefers a different scheduling (e.g., H25.2 first because the EU/EZU surprise has been open since Day-24 cron-D), the conflict resolves cleanly by inverting §2: H25.2 → Day-26 cron-C, H26.1 → Day-27 cron-C. The downgrade path in §4 inverts symmetrically. No re-pre-registration is needed because intervals and methods are pre-frozen for both.

Default-path proceeds at Day-26 cron-B with H26.1 harness pre-stage unless Ingo signals otherwise.

## §6 Day-25 ZH publication note (out-of-scope but logged here)

This cron-A also reconciled the two in-flight async ZH dispatches from Day-25 cron-E:

| Dispatch | Body / Bibliography | Status |
|---|---|---|
| `20260604-210400-dione-to-inanna-58f94962` | Body (§0-§9) | `delivered_reply_only` — bus rc=0 in 66s, payload empty (acknowledgment-only reasoning text), no disk artifact |
| `20260604-210407-dione-to-inanna-0d42c4c2` | Bibliography + methodology-cross-reference | `delivered_reply_only` — bus rc=0 within seconds, payload truncated at "I'm acknowledging the receipt..." reasoning, no disk artifact |

This is a **novel failure mode** distinct from Day-24's late-sequence token-attractor degeneration: the chunked-protocol A/B test designed to reduce attractor risk did not protect against the more fundamental ACP-Watchdog 180s cutoff before disk write. Inanna entered reasoning mode on both dispatches but did not complete the file-write step within the watchdog window.

**Decision:** Day-25 ZH (`publications/2026-06-04-zh.md`) will be Dione-direct rendered at Day-26 cron-B (after H26.1 harness pre-stage if time permits) or cron-C (if not). The ZH file is missing from silicon-strait/trunk and will need to be authored end-to-end against EN-LOCK `530a0c7`. Filing in this scheduling-resolution document because it is a Day-26 cron-A reconciliation outcome, not a separate publication artifact.

---

**Issued at Day-26 cron-A 2026-06-05 06:03 CEST**
**Default path:** §2 stands. Ingo intervention by Day-26 cron-B (11:00 CEST 2026-06-05) overrides; thereafter pre-stage proceeds.
