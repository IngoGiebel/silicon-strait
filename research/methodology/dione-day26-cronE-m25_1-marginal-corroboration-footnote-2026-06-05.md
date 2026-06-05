# M-25-1 Marginal-Corroboration Footnote (Day-26 cron-E)

**Footnote fire:** Day-26 cron-E (2026-06-05 21:00 CEST)
**Footnote type:** Non-destructive corroboration qualification (does not retract M-25-1, does not re-open path-(a), does not modify the verdict-rule intervals or the harness method)
**Target amendment:** **M-25-1** (filed at Day-25 cron-D in `publications/2026-06-04-en.md` §6, commit `530a0c7`)
**Triggering evidence:** Day-26 H26.1 firm-level cross-substrate re-test verdict (commit `6712a00`) + Nisaba 🌾 H26.1 numerical audit (same commit, `CONCUR_WITH_NOTES`)
**Resolves:** open-question `q-day26-2` (filed at Day-26 cron-D, `publications/2026-06-05-en.md` §2 Open Questions, commit `24d29ae`) — default-path triggered: "qualify M-25-1 with a 'marginal-corroboration, cross-substrate replication ROK rank-3' footnote in the methodology file at Day-26 cron-E."

---

## Canonical footnote text

The footnote is added to the M-25-1 amendment record (Day-25 publication §6) by reference; the canonical wording, reproduced verbatim from `publications/2026-06-05-en.md` §6 (EN-LOCK at Day-26 cron-E), is:

> **M-25-1 footnote (Day-26 cron-E):** Cross-substrate replication at Day-26 H26.1 (commit `6712a00`) corroborates the M-25-1 substitution at the substrate-isolated level (`δ_ROK = +0.0515` in-interval; sign recovered from Day-24's `−0.0077`) but does not rehabilitate the H24.1 cross-substrate predicted ordering (ROK ranks #3 vs predicted #1). The in-interval status is marginal: `+0.0015` above floor, with 9/27 ±5 td anchor perturbations falling below `+0.05`. Downstream Nexus consumers of ROK's textual-axis δ should treat the M-25-1 ticker as the correct firm-level proxy under v1.2 but expect the rank-position to depend on the cross-substrate ordering invariant adopted (per q-day26-1's reading-α vs reading-β disambiguation, pending Day-28 cron-A).

## What this footnote qualifies

The M-25-1 amendment (Day-25 cron-D) asserts that the ROK textual-axis ticker for cross-substrate δ tests under v1.2 is `005930.KS` (Samsung Electronics direct, KRX-listed), retiring `EWY` from ROK textual-axis duty. The amendment is a measurement-protocol substitution; it does not assert any cross-substrate ranking position for ROK.

H26.1 (Day-26 cron-C) executed the H24.1 4-substrate textual-axis sweep with `005930.KS` substituted into the ROK slot under M-25-1, holding all other Day-24 method parameters constant. The verdict is INCONCLUSIVE: ROK at rank #3 (predicted #1); two substrates outside their blind intervals (EU and JPN, both over).

**The footnote qualifies M-25-1 along two axes:**

1. **Substrate-isolated corroboration is positive but marginal.** M-25-1's load-bearing assertion — that ROK's firm-level δ under `005930.KS` lands in the predicted direction and inside the `[+0.05, +0.10]` blind interval — is corroborated at `δ_ROK = +0.0515`. The in-interval status is `+0.0015` above the lower bound; Nisaba audit §5's `{−5, 0, +5}³ = 27`-case ±5 td anchor-perturbation grid puts 9 / 27 (33%) cases below `+0.05`. The corroboration is real but not robust to small calendar-anchor shifts.

2. **Cross-substrate ranking is not rehabilitated.** Even with `005930.KS` substituted, the observed substrate ordering by stress-vs-baseline δ_median is EU > JPN > ROK > US, not the H24.1-predicted ROK > JPN > EU > US. EU (EZU, `+0.0796`) leads the corpus at both Day-24 (ETF-level, ROK sign-flipped) and Day-26 (firm-level under M-25-1). The ranking-level falsifier is the H24.1 directional prediction, not M-25-1.

## What this footnote does NOT do

| Item | Status after footnote |
|---|---|
| Retract M-25-1 | **No.** The amendment stands. `005930.KS` remains the canonical ROK textual-axis ticker under v1.2. |
| Re-open path-(a) of Day-25 H25.1's two-path disambiguation | **No.** Path-(a) (signal-failure) was retired at Day-25 by H25.1's `+0.0546` isolated δ corroboration; H26.1 reinforces that retirement. |
| Modify the verdict-rule intervals or the harness method | **No.** The Day-24 cron-A `bd31a40` §3 intervals and rule structure are unchanged. The harness's rolling-60 Pearson on log-returns and the global NYSE-aligned mask convention are unchanged. |
| Block downstream Nexus consumers from using `005930.KS` for ROK textual-axis δ | **No.** Consumers should continue to consume the M-25-1 ticker. The footnote only asks consumers to read the in-interval status as marginal and route through the `marginal_in_interval` watcher branch when reading. |
| Pre-commit to reading-α (schema iteration) or reading-β (methodology iteration) | **No.** q-day26-1's disambiguation is deferred to Day-28 cron-A. |

## Downstream impact

### Hassaleh-Nexus Sprint-15 T4 acceptance criterion

Sprint-15 v1.2-migration's T4 (watcher consistency tests) is updated by this footnote to require a **tri-state status flag** on ROK textual-axis δ emission:

| Watcher state | Definition |
|---|---|
| `robust_in_interval` | δ in interval AND `margin_above_floor ≥ +0.01` AND `perturbation_below_floor_share ≤ 0.25` |
| `marginal_in_interval` | δ in interval AND (`margin_above_floor < +0.01` OR `perturbation_below_floor_share > 0.25`) |
| `out_of_interval` | δ outside interval |

The H26.1 ROK observation (`+0.0515`, margin `+0.0015`, perturbation-below-floor `9/27 = 0.333`) emits `marginal_in_interval` under this scheme.

### Predicate-emission ROK tuple under P29.3

P29.3's pooled-level ROK textual-axis tuple is `POSITIVE` with an explicit `marginal` flag carrying `(margin_above_floor=+0.0015, perturbation_below_floor_share=9/27)`, per the corresponding clarification in `publications/2026-06-05-en.md` §7.1. Downstream consumers branch on the `marginal` flag rather than treat `POSITIVE` as unconditionally robust.

### EU corpus-top finding (q-day24-3 candidate)

Independent of M-25-1, the H26.1 sweep cross-validates EU's corpus-top position across two independent measurement protocols (Day-24 ETF-level, Day-26 firm-level-amended). The Day-24 q-day24-3 candidate `ACTIVE_AGGREGATE_AMPLIFIED` enters the Day-27+ schema-iteration queue with stronger evidence than at filing. This is recorded here for traceability; it is not part of the M-25-1 amendment and is not modified by this footnote.

## When this footnote is superseded or retracted

- If a Day-27+ schema iteration (reading-α path) promotes `ACTIVE_AGGREGATE_AMPLIFIED` to a v1.2 schema state and the new predicate emission resolves EU's corpus-top position structurally, the cross-substrate ranking falsifier in §2 above may be re-read as schema-level rather than ROK-marginality-level. The footnote stands as a record of the H26.1 evidence in either case.
- If a Day-27+ methodology iteration (reading-β path) adopts per-substrate priors instead of cross-substrate rankings, the H24.1 verdict-rule itself is retired and this footnote's `marginal_in_interval` watcher logic becomes the canonical downstream consumption pattern (rather than a Sprint-15 acceptance criterion).
- If subsequent firm-level retests under different anchor windows show ROK δ stably above `+0.05` (e.g. with the perturbation-below-floor share dropping to ≤ 0.10), the `marginal` qualification weakens and the footnote may be revised to "stable corroboration" wording at a future cron fire.

## Provenance

| Field | Value |
|---|---|
| Footnote filed at | Day-26 cron-E, 2026-06-05 21:00 CEST |
| Filing fire commit | (this commit) |
| H26.1 source commit | `6712a00` |
| Day-26 publication EN-LOCK commit | (this commit, joint with the publication) |
| M-25-1 original amendment commit | `530a0c7` (Day-25 cron-D EN-LOCK) |
| Day-25 H25.1 isolated-pair commit | `340631c` (Day-25 cron-C verdict) + `346064b` (cron-C Nisaba audit) |
| Day-24 cron-A pre-committed verdict-rule | `bd31a40` |
| Default-path triggered | q-day26-2 default ("file at cron-E"), no Ingo override by EN-LOCK fire |
| Cross-reference | `publications/2026-06-05-en.md` §6 (canonical footnote text reproduced verbatim) |
