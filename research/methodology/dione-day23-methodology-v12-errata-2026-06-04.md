# Day-23 Methodology Publication — §4.4 Erratum (Non-Destructive)

**Filing fire:** Day-25 cron-A (2026-06-04 06:00 CEST)
**Resolves:** q-day24-1 default path (A)
**Source publication:** `research/methodology/dione-day23-cronE-v12-vocabulary-lock-2026-06-02.md` at commit `10381e9` (2026-06-02 21:00 CEST EN-LOCK)
**Audit trigger:** Nisaba numerical audit `research/audit/nisaba-day24-cronA-day23-numerical-audit.md` at commit `abbf875` (2026-06-03 06:35 CEST) — §4.4 FAIL on 4/6 cells
**Resolution path chosen:** (A) non-destructive errata, per q-day24-1 default-if-no-answer; not (B) destructive operational-axis re-pull

---

## §1 What this erratum says

The Day-23 §4.4 "Day-21 §4.2 evidence retro-classified under v1.2-axis assignment" table contains six cells in the **operational-axis δ at Day-21 stress window** column. Of these six cells, **only two are faithful reproductions of Day-21 §4.2 arithmetic**:

| Substrate | Cell as published in Day-23 §4.4 | Faithful to Day-21 §4.2? | Provenance |
|---|---|---|---|
| US  | NVDA × TSM δ ≈ +0.06 | **NO**  | Day-22 §7.2 `θ_econ_weight` shorthand carried forward |
| JPN | 8035.T × TSM δ ≈ +0.04 | **NO**  | Day-22 §7.2 `θ_econ_weight` shorthand carried forward |
| ROK | 005930.KS × TSM δ ≈ +0.064 | **NO**  | Day-22 §7.2 `θ_econ_weight` shorthand carried forward |
| EU  | AIR.PA × TSM δ ≈ +0.03 | **NO**  | Day-22 §7.2 `θ_econ_weight` shorthand carried forward |
| IND | INDA × TSM δ = +0.0530 (textual, not operational) | n/a — wrong axis column | Day-22 §4.2 (textual axis), miscategorized in published table |
| IND | TATAELXSI × TSM δ = +0.0253 | **YES** | Day-22 §4.2 operational axis |

Nisaba's audit (`abbf875`) reproduced only 2/6 cells faithfully (the two IND rows traceable to Day-22 §4.2; INDA is textual-axis not operational, but the underlying number is correct against its true source). The four non-IND cells trace to Day-22 §7.2 — where they appear as **`θ_econ_weight` shorthand** parameters used in v1.1's pre-axis-stratification economic-weight computation, not as Pearson-correlation δ values around stress windows. Day-21 §4.2 itself measured **event-window median correlations** under H21.1 (PRC port-fee shock event-study) for `NVDA/005930.KS/BHP.AX × TSM` only, and did **not** publish 8035.T or AIR.PA at all.

The Day-23 §4.4 table is therefore a **layered representational error**: it presents Day-22 §7.2 `θ_econ_weight` values as if they were Day-21 §4.2 deltas. The numerical magnitudes (`+0.06`, `+0.04`, `+0.064`, `+0.03`) are real numbers from Day-22, but they are not what Day-23 §4.4 claims they are.

## §2 What this erratum does NOT do (per non-destructive path A)

- **Day-23 §4.4 is not edited.** The publication at commit `10381e9` remains as-is on `trunk`. This erratum is filed as a sibling document and linked from the §4.4 entry-point in the Day-25+ methodology track.
- **No new computations are run.** Path (B) — re-running Day-22's method (rolling-60 Pearson on log-returns, ±20 trading-day stress windows around DUV 2023, LAI 2024, PRC 2025) for NVDA/8035.T/005930.KS/AIR.PA × TSM — is **not** executed at this fire. Path (B) is the larger-scope remediation and remains available if Ingo overrides path (A).
- **H21.1c orthogonality test is not run.** The Day-23 §4.4 table feeds the H21.1c orthogonality cross-substrate corpus. Under path (A), the corpus is reduced to the 2/6 faithful cells (both IND), which is insufficient for a meaningful Pearson on substrate-corpus orthogonality. H21.1c remains **BLOCKED** until Day-25 cron-C (2-cell IND-only recompute, exploratory) or until Ingo overrides to path (B) for the full 6/6 recompute.

## §3 Re-labeling rule (for Day-25+ references to §4.4)

When Day-25+ methodology or publications cite the Day-23 §4.4 table, the four non-IND `operational-axis δ at Day-21 stress window` cells **must be re-labeled** as:

> "legacy `θ_econ_weight` shorthand carried forward from Day-22 §7.2; not a reproduced Day-21 §4.2 δ"

The INDA × TSM cell **must be re-labeled** as textual-axis, not operational-axis, with the unchanged value δ = +0.0530.

The TATAELXSI × TSM cell **may be cited as-is** (δ = +0.0253, operational-axis, Day-22 §4.2 faithful).

## §4 Downstream consequences of path (A)

### §4.1 H21.1c orthogonality test

BLOCKED at Day-23 §4.4 corpus level. Day-25 cron-C may run an exploratory 2-cell IND-only orthogonality check, but the result is not load-bearing for the v1.2 axis-orthogonality claim. v1.2 axis-orthogonality remains a **provisional commitment** until either:
- (a) path (B) recomputes the 6/6 operational-axis corpus at Day-25/26 and H21.1c runs at full power, OR
- (b) Day-24's textual-axis sweep (H24.1, already executed at INCONCLUSIVE) plus Day-25 ROK firm-level test (`q-day24-4` first analytic claim) plus Day-25 cron-B EU member-state decomposition (`q-day24-5`) cumulatively provide an axis-orthogonality signal that does not depend on the Day-21-derived operational-axis corpus.

### §4.2 v1.2 schema commitment status

Unchanged. The v1.2 vocabulary lock (`coupling_textual` ∈ {NONE, INDIRECT, DIRECT}, `coupling_operational` ∈ multi-valued, retired-token list) is **independent** of the §4.4 table arithmetic. Inanna's source-validation pass (`d926630`) confirmed 4/4 scope items for §1-§5; §4.4 is a §4-internal table, not a vocabulary-level commitment.

### §4.3 P29.3 / P30.3 predicate updates

Unchanged. The GWW3 predicate refresh (§5 of Day-23) is vocabulary-level and does not depend on the §4.4 retro-classification arithmetic.

### §4.4 Day-24 publication interpretive risk

The Day-24 H24.1 textual-axis sweep is **independent** of the Day-23 §4.4 operational-axis cells. Day-24's INCONCLUSIVE verdict (ROK sign-flip + EU/EZU overshoot + 3 cells outside blind intervals) does not depend on the operational-axis corpus integrity. Day-24's substantive findings stand.

The Day-24 publication's §5 (H21.1c orthogonality test) was **already marked BLOCKED** pending q-day24-1 resolution; path (A) does not change that status, only sharpens the reason (2/6 cells faithful instead of 6/6).

## §5 What changes at Day-25+

1. **Day-25 cron-A** (this fire): Files this erratum; resolves q-day24-1 by path (A); closes the question.
2. **Day-25 cron-C** (14:00 CEST): If exploratory 2-cell IND-only orthogonality check is run, it must footnote that the corpus is `n=2, IND-only` and not represent it as a substrate-corpus orthogonality result.
3. **Day-26+** (open): If Ingo overrides to path (B), a separate fire commits a new artifact `research/india_substrate/dione-day26-operational-axis-repull-day21-method.json` with rolling-60 Pearson on log-returns for NVDA/8035.T/005930.KS/AIR.PA × TSM around DUV 2023, LAI 2024, PRC 2025. H21.1c then runs at full 6/6 power.

## §6 Audit trail

| Step | Artifact | Commit |
|---|---|---|
| Day-23 EN-LOCK | `research/methodology/dione-day23-cronE-v12-vocabulary-lock-2026-06-02.md` | `10381e9` |
| Nisaba audit | `research/audit/nisaba-day24-cronA-day23-numerical-audit.md` | `abbf875` |
| Inanna validation | `research/validation/inanna-day24-cronA-day23-v12-source-validation.md` | `d926630` |
| Day-24 EN-LOCK | `publications/2026-06-03-en.md` (§5 marks BLOCKED per q-day24-1) | `eb424f6` |
| **This erratum (path A)** | `research/methodology/dione-day23-methodology-v12-errata-2026-06-04.md` | (this commit) |

## §7 Closing note

Path (A) is the **non-destructive** remediation: it acknowledges the layered representational error without re-running computations and without amending the locked publication. The cost is that H21.1c orthogonality remains provisional. Path (B) would have re-run Day-22's method against the four non-IND substrates and fully unblocked H21.1c, but at the cost of an additional ~30min compute fire and a second representational layer (Day-22-method applied to four substrates that Day-22 did not originally include) to audit.

The choice of path (A) reflects q-day24-1's `default_if_no_answer` and is reversible: at any future fire, an override to path (B) can be filed as a separate erratum and the operational-axis corpus regenerated. Until then, the 2/6 IND-faithful corpus is the load-bearing operational-axis evidence and H21.1c remains BLOCKED.

---

**Filed by:** Dione 🌙 at Day-25 cron-A 2026-06-04 06:00 CEST
**Resolves:** q-day24-1 (open since Day-24 cron-B 2026-06-03 11:08 CEST)
**Resolution status:** path (A) default applied; reversible to path (B) on Ingo override
