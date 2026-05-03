# Nisaba numerical audit — Silicon Strait Day 5 EN (2026-05-03)

**Scope:** `publications/2026-05-03-en.md` pre-commit quantitative audit against local source notes:

- `research/economic_pressure_pathways/notes-2026-05-02-primaries-en.md`
- `research/economic_pressure_pathways/notes-2026-05-02-case-studies.md`
- `research/economic_pressure_pathways/notes-2026-05-02-primaries-zh.md`

External spot checks were attempted for the Priority-1/3 anchors. Firecrawl search was credit-blocked; direct fetches worked for WTO DS602 and Federal Register EO pages, but DFAT/LT/USGS pages were not fully retrievable within the deadline. I therefore distinguish **LOCK**, **KEEP UNVERIFIED**, and **REWRITE** below.

## Executive audit finding

The headline thesis can stand, but the draft should **not** untag all quantitative anchors yet. The strongest numerical foundation is the case-attrition curve if column 15 is rewritten as computed ratios rather than kept as hand-estimated bands.

Material fixes:

1. **Lithuania `~€300M / ~0.7% exports`: KEEP UNVERIFIED or rewrite.** `~€300M` is plausible for Lithuania-to-China exports, but `0.7%` depends on denominator choice. Against goods exports it is closer to ~0.9–1.1%; against broader exports/goods+services it can approach ~0.7%. Do not lock without a Eurostat/LT primary citation and denominator note.
2. **Australia `~30% exports`: LOCK as conservative range only.** DFAT-style 2019 decomposition is usually ~30–36% depending on goods-only vs goods+services denominator. Phrase as “roughly one-third / about 30–35%”, not a precise 30.0%.
3. **Australia investment `61% drop in 2020`: LOCK with methodology footnote.** This is the KPMG/University of Sydney/ANU-style value basis (Chinese investment value, not FIRB approval count). Keep if footnoted as investment-flow value.
4. **Australia beef `35%`: REWRITE.** The 35% figure refers to the four suspended processors' share of **Australian beef exports to China**, not all Australian beef exports. Current wording “35% of beef exports” is too broad.
5. **Wine tariffs: LOCK with precision.** Interim anti-dumping range `107.1%–212.1%`; final combined anti-dumping/countervailing duties are commonly stated as **up to 218.4%**. Draft `218%` is acceptable if rounded, better as `218.4%`.
6. **Gallium `$110–130/kg → $687/kg`: KEEP UNVERIFIED.** I could not verify the baseline/final pair from the cited notes or a primary price series within deadline. USGS MCS is not enough for the May-2025 spot price. Keep tag unless an Argus/Asian Metal/Bloomberg series is cited.
7. **EOs 13902 and 13846: LOCK.** Federal Register confirms EO 13902 is “Imposing Sanctions With Respect to Additional Sectors of Iran” and EO 13846 is “Reimposing Certain Sanctions With Respect to Iran.” MOFCOM Notice #21's Iran-secondary-sanctions frame is source-consistent.

## Priority 1 — load-bearing quantitative claims

| Claim in draft | Audit verdict | Notes / required edit |
|---|---|---|
| Lithuania pre-coercion trade `~€300M annually / ~0.7% of LT exports` | **KEEP UNVERIFIED / denominator-sensitive** | `~€300M` likely refers to LT exports to China, not total bilateral trade (`~$1.4B` in case table). `0.7%` is not safe without specifying goods vs goods+services denominator. Rewrite: “roughly €300M in direct exports; below ~1% of Lithuania's broad export base, denominator-dependent.” |
| Australia pre-coercion trade `~30% of AU exports` | **LOCK AS RANGE** | Use “about one-third” or `~30–35%`. A precise 30% is too low if using goods exports; closer if using broader exports / selected year. |
| Australia Chinese investment dropped `61% in 2020` | **LOCK WITH FOOTNOTE** | Treat as Chinese direct-investment value basis from KPMG/University of Sydney/ANU CIS reporting, not FIRB approval-count basis. If using FIRB, numbers may differ; do not mix methods. |
| Australia beef `35% of beef exports concentrated in 4 plants` | **REWRITE** | Should read: “four suspended processors accounted for about **35% of Australia's beef exports to China**,” not 35% of all AU beef exports. |
| Australia wine `107.1%–212.1%`, then `218% final` | **LOCK / PRECISION EDIT** | WTO DS602 confirms the wine AD/CVD dispute. Public tariff figures support interim AD `107.1–212.1%`; final combined rate is better written `up to 218.4%` (or “about 218%”). |
| Gallium `$110–130/kg pre-2023-07 → $687/kg by 2025-05` | **KEEP UNVERIFIED** | Local notes cite the figure but no primary series. USGS MCS does not by itself lock a May-2025 spot price. Needs Argus/Asian Metal/USGS monthly methodology. |

## Priority 2 — case-attrition curve, column 15

Column 15 should be explicitly computed as:

`peak trade-impact USD / target nominal GDP same-year USD`

The existing table values are directionally right for Norway/S. Korea/Australia, but Lithuania's `<0.3%` is too low if using the table's own `$300M` impact value.

| Case | Table impact | GDP denominator used for audit | Computed impact/GDP | Existing table | Verdict |
|---|---:|---:|---:|---:|---|
| Norway 2010 salmon | `$1.1B` | Norway 2010 nominal GDP ≈ `$429B` | `0.26%` | `<0.3%` | **OK** |
| S. Korea THAAD 2017 | `$15B` | Korea 2017 nominal GDP ≈ `$1.62T` | `0.92%` | `~1.0%` | **OK** |
| Australia 2020/2019 | `$20B` | Australia nominal GDP ≈ `$1.39T` 2019 or `$1.33T` 2020 | `1.44–1.50%` | `~1.4%` | **OK**, write `~1.4–1.5%` |
| Lithuania 2021/direct | `$300M` | Lithuania nominal GDP ≈ `$57B` 2020 or `$66–67B` 2021 | `0.45–0.53%` | `<0.3%` | **DRIFT >5%; REVISE** |
| Japan rare earths 2010 | n/a regime-level | n/a | n/a | n/a | **OK as n/a** |

Recommended replacement column-15 values:

- Norway: `~0.26%`
- S. Korea: `~0.9–1.0%`
- Australia: `~1.4–1.5%`
- Lithuania: `~0.45–0.55% direct-impact/GDP` (or keep `<0.3%` only if a narrower verified direct-import-loss value below ~$180M is sourced)
- Japan rare earths: `n/a — regime/commodity-market shock, not target-GDP case`

**Effect on thesis:** The ordering still supports the thesis qualitatively: Lithuania remains below Australia and S. Korea, and bloc-backstop remains explanatory. But the clean threshold claim “ratio <1% sustains hold; ratio >5% degrades hold” is not supported by this five-case table because Australia is ~1.5%, not >5%. Rewrite to: **“lower direct GDP exposure plus bloc-backstop sustains hold; higher exposure without trade-bloc backstop degrades hold.”** Do not state a `>5%` threshold from this dataset.

## Priority 3 — Executive Orders 13902 and 13846

- **EO 13902:** **VERIFIED.** Federal Register title: “Imposing Sanctions With Respect to Additional Sectors of Iran” (2020-01-14 publication of 2020-01-10 EO). This is Iran-sector sanctions.
- **EO 13846:** **VERIFIED.** Federal Register title: “Reimposing Certain Sanctions With Respect to Iran” (2018-08-07). This is Iran sanctions after JCPOA withdrawal.
- **MOFCOM Notice #21 reference:** **SOURCE-CONSISTENT.** The Chinese notice's clause naming `第13902号行政令、第13846号行政令` is correctly described as U.S. Iran-sanctions / secondary-sanctions substrate.

## Additional arithmetic / wording checks in EN draft

| Draft claim | Check | Verdict |
|---|---|---|
| Lithuania duration “~4.5y” | 2021-08/11 to 2026-02/05 = ~4.25–4.75y depending endpoint | OK as loose; table `4 yr 3 mo and counting` is better |
| Australia duration “~3y break” | 2020-04/05 to 2024-03 = ~3 yr 11 mo | Draft “~3y” understates; use “nearly 4 years” for wine final resolution, or distinguish 2023 political reset |
| China-Russia not relevant here | — | No Day-4 carryover issue |
| Gallium `5.3x` | `687/130 = 5.28`; `687/110 = 6.25` | If baseline retained, range is `5.3–6.2x`; current “5.3x” uses high baseline only |

## Publication-safe edits before EN commit

1. Change Lithuania quantitative sentence to denominator-safe wording:  
   **“Lithuania-PRC direct export exposure was small — roughly hundreds of millions of euros annually, below ~1% of Lithuania's broad export base depending on denominator [Nisaba: primary citation still needed].”**

2. Change Australia exposure sentence to:  
   **“AU-PRC trade absorbed roughly one-third of Australian exports at peak (~30–35%, denominator-dependent).”**

3. Change beef sentence to:  
   **“4 AU processors, accounting for about 35% of Australia's beef exports to China.”**

4. Change wine sentence to:  
   **“wine tariffs at 107.1%–212.1% interim, later up to about 218.4% combined final duties.”**

5. Keep `[UNVERIFIED]` tags on: Lithuania `0.7%` exact denominator; gallium `$110–130 → $687`; any exact “pre-coercion trade $/€” if not primary-cited.

6. Rewrite the GWW3 threshold sentence. Current draft says ratio `<1%` hold and `>5%` break; this table does **not** show a >5% Australia ratio. Use lower/higher relative exposure, not a hard >5 threshold.

## Bottom line

**Ship only after these edits.** The Day-5 systemic-coercion thesis survives the audit, but the quantitative foundation should be described as **relative exposure + bloc-backstop**, not a precise threshold model. The only hard numerical error is the Lithuania column-15 `<0.3%` if `$300M` is the impact numerator; it should be about `0.45–0.55%`.
