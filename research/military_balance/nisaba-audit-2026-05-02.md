# Nisaba numerical audit — Silicon Strait Day 4 EN (2026-05-02)

**Scope:** `publications/2026-05-02-en.md` quantitative claims cross-checked only against the cited local source notes: `notes-2026-05-01*.md`.

## Executive audit finding

The draft is mostly source-consistent, but it has three material numerical/source issues:

1. **Budget ratio error:** the executive claim that PLA outspends Taiwan by **at least 16:1 on official figures** is not consistent with the CSIS official 2025 figure used in the draft. `244.8 / 20.1 = 12.18`, not 16. The 16–17x ratio comes only from the older Wikipedia scaffold figure `336 / 20.1 = 16.72`, which the draft does not use as its main official budget figure.
2. **Several Taiwan modernization quantities are not verified from the cited source notes:** the draft's **66 upgraded F-16s**, **400 Harpoons**, and **DF-17 ~300-second TSMC flight-time estimate** are not supported in the cited notes. Tag **UNVERIFIED** unless another source is added.
3. **Prompt/transcription caveat:** if the audit-scope shorthand means `36B / 14B / 31B / 44.8B / 76.7B / 1.5B / 71B / 26B`, those are decimal/hundreds-truncated. The actual source notes/draft use **336B/314B**, **231B/244.8B/276.7B**, **21.5B**, **471B**, and **226B**.

## Arithmetic checks

| Claim | Check | Result |
|---|---:|---|
| PLA active vs ROC active, `2,035,000 / 160,000` | `12.71875` | OK: “nearly 13:1” |
| PLA official 2025 vs ROC 2026, `244.8 / 20.1` | `12.18` | **ERROR** if described as 16:1 |
| PLA Wikipedia scaffold vs ROC, `336 / 20.1` | `16.72` | Explains where 16:1 came from, but conflicts with draft's CSIS official budget framing |
| SIPRI premium, `(313.7 - 231) / 231` | `35.8%` | OK: +36% |
| IISS premium, `(325 - 231) / 231` | `40.7%` | OK: +41% |
| PPP premium, `(471 - 231) / 231` | `103.9%` | OK: +104% |
| DoD premium, official × `1.32–1.63` | `+32–63%` | OK |
| Budget-opacity spread, `471 / 244.8` | `1.924` | OK: 1.92x, but mixes 2025 official with 2024 PPP study |
| “as-if deterrence”, `471 - 244.8` | `226.2B` | OK: ~$226B, same year-mix caveat |
| Carrier days outside FIC, `(58 - 32) / 32` | `81.25%` | OK: +81% |
| Carrier sorties, `(1680 - 1240) / 1240` | `35.48%` | OK: +35.5% |
| ADIZ May-Dec YoY, `(2479 - 2613) / 2613` | `-5.13%` | Draft says -5.4%; source note says -5.4%. Arithmetic from rounded figures is closer to **-5.1%**. Minor rounding/source-exactness issue. |
| China-Russia exercises, `(6 - 14) / 14` | `-57.14%` | OK: -57% |
| Literal shorthand `71 / 44.8` if read without hundreds digits | `1.585` | **Not** 1.92x. Correct intended arithmetic is `471 / 244.8`. |

## Claim-by-claim source check

### 1. PLA force structure / budget overview

- `2,035,000` active and `510,000` reserve: **VERIFIED** in `notes-2026-05-01.md` PLA overview.
- `US$336B 2025`, `US$314B 2024`, `1.7% GDP`, `~12% global share`: **VERIFIED** in `notes-2026-05-01.md` scaffold, but **not used as the final budget anchor** in the publication.
- Draft final: `1.78T RMB / $244.8B 2025 / +7% YoY`, `1.91T RMB / $276.7B 2026`, official spending at/below 2% GDP: **VERIFIED** in `notes-2026-05-01-csis-extension.md`.
- **ERROR:** “outspends Taiwan by at least 16:1 on official figures” should be revised to either **~12:1 using CSIS official 2025 vs Taiwan 2026** or explicitly explain the alternative Wikipedia/SIPRI-like 16–17x basis.

### 2. CSIS spending table

- Official `2024 ~$231B`, `2025 $244.8B`, `2026 $276.7B`: **VERIFIED** in `notes-2026-05-01-csis-extension.md`.
- SIPRI `2024 $313.7B`: **VERIFIED**.
- IISS `2024 $325B`: **VERIFIED**.
- PPP-adjusted `~$471B`: **VERIFIED**.
- DoD `official × 1.32–1.63`: **VERIFIED**.
- Premium arithmetic: **OK**.
- Caveat: comparing `$244.8B` official 2025 to `~$471B` PPP 2024 is analytically acceptable only if labelled as a cross-year estimate spread; otherwise use 2024 official `$231B` for same-year premium and spread.

### 3. Off-budget / composition

- PAP `$21.5B in 2024`: **VERIFIED** in `notes-2026-05-01-csis-extension.md`. If any version says `$1.5B`, that is **ERROR**.
- Equipment `~41%` of total spend, 2017 white paper: **VERIFIED**.
- UN-reported `36.6%` in 2022: **VERIFIED** in notes, but not present in the EN publication body.

### 4. PLARF arsenal and named missile systems

- Arsenal: `900 SRBM`, `~1,300 conventional MRBM`, `~500 IRBM`, `~400 cruise missiles`, `~400 ICBM`: **VERIFIED** in `notes-2026-05-01.md`; publication cites Source 2 via DoD secondary in PLARF article.
- DF-21D `1,500 km`: **VERIFIED**.
- DF-17 `1,600 km`, `Mach 10`: **VERIFIED**.
- DF-26 `5,000 km`, `~250 launchers`, Bases `61/62/64/66`: **VERIFIED**.
- DF-41 `12,000–15,000 km`, `~44 launchers`: **VERIFIED in notes**, but not included in the EN publication body.
- CJ-100 `2,000 km`: **VERIFIED in notes**, but not included in the EN publication body.

### 5. PLAN

- `3 carriers`: **VERIFIED**.
- `62 destroyers`, `8 × Type 055`: **VERIFIED**.
- `4 amphibious assault ships`, `8 amphibious transport docks`, `33 tank landing craft`: **VERIFIED in notes**, but not included in the EN publication body.
- `68 submarines`, `12 nuclear-powered`, `6 Type 094 SSBN`, `72 warheads`: **VERIFIED**.
- Carrier operational data `58 days outside FIC vs 32`, `1,680 vs 1,240 sorties`, `+81%`, `+35.5%`: **VERIFIED** in CSIS extension notes; arithmetic OK.

### 6. ROC / Taiwan

- `~160,000` active: **VERIFIED**.
- Reserve `1.66–2.5M`: **VERIFIED**.
- Defense budget `2026 $20.1B`: **VERIFIED**.
- `>3% GDP`, first since 2009: **VERIFIED**.
- Lai 8-year plan `$39.89B`: **VERIFIED**.
- `384 F-16s (2015 baseline)` / `4 destroyers` / `22 frigates` / `4 diesel submarines`: **VERIFIED in notes**.
- Draft claim `full fleet of 66 upgraded aircraft from legacy F-16A/B`: **UNVERIFIED** from cited notes and conflicts with the local scaffold's `384 total` phrasing. Needs a direct source or rewrite.
- Draft claim `400 Harpoon Block II+ coastal defense missiles`: **UNVERIFIED** from cited notes. DSCA was explicitly blocked in the notes; do not present this as sourced unless another citation is added.

### 7. ADIZ / operational tempo

- `3,764 ADIZ incursions in 2025`, `+22.4% YoY`: **VERIFIED**.
- `~319/month since May 2024` vs `~156/month Jan 2022-Apr 2024`: **VERIFIED**.
- Naval vessels `221/month`, `+42%`, baseline `156/month`, `190+/month since May 2024`: **VERIFIED in notes**; the EN body only uses part of this.
- May-Dec `2,479 vs 2,613`: **VERIFIED**. Draft/source-note `-5.4%` differs from simple arithmetic on rounded figures (`-5.1%`); acceptable if CSIS exact underlying data yields -5.4, otherwise revise to “about -5%”.
- Carrier `58 days outside FIC vs 32`, sorties `1,680 vs 1,240`: **VERIFIED**, arithmetic OK.

### 8. Exercises

- Strait Thunder-2025A: `135 sorties`, `38 vessels`: **VERIFIED**.
- Justice Mission-2025: `8 exercise zones`, `27 rockets`: **VERIFIED**.
- Joint Sword-2024B: `153 sorties`: **VERIFIED**.

### 9. South China Sea / Japan axis

- SCS `163 PLA operations in 2025`: **VERIFIED**.
- `55 live-fire` vs `47 in 2024`: **VERIFIED**.
- Senkaku `1,380 CCG/state vessels` in contiguous zone: **VERIFIED**.
- Territorial-sea entries `89` vs `115`, `-23%`: **VERIFIED**; arithmetic `(89-115)/115=-22.6%` OK.
- PLAN voyages near Japan `111` vs `108`: **VERIFIED**; “flat” characterization OK.
- CCG Scarborough presence “more than doubled”: **VERIFIED qualitatively** in notes; no exact count available locally.

### 10. China-Russia exercises

- `6 in 2025` vs `14 in 2024`: **VERIFIED**.
- `-57%`: **VERIFIED**, arithmetic OK (`-57.14%`).

### 11. 1.92x spread / “as-if deterrence”

- In the EN publication, the actual calculation is `$471B / $244.8B = 1.92x`; arithmetic **OK**.
- `$471B - $244.8B = $226.2B`; “~$226B” **OK**.
- Caveat: source note labels PPP as a `2024 study`; `$244.8B` is official 2025. If strict year alignment matters, use `$471B / $231B = 2.04x` and `$240B` spread for 2024, or label the current version as an estimate-range comparison rather than a same-year spread.
- If the shorthand claim is literally `71B / 44.8B` and `~26B`, it is **ERROR** caused by dropped hundreds digits.

## Additional quantitative claims in EN publication that need tags

- `Fujian operational-ready date 2026–2027`: **UNVERIFIED** from the cited notes; notes explicitly say this remains contested/open.
- `66 upgraded F-16V aircraft`: **UNVERIFIED** from the cited notes.
- `400 Harpoon Block II+ missiles`: **UNVERIFIED** from the cited notes.
- `TSMC fabs within ~300 seconds from eastern China launch positions (DF-17 flight-time estimate)`: **UNVERIFIED** from the cited military-balance notes; the preliminary notes list TSMC/missile geography as an open research item, not a sourced result.
- `TSMC 70%/90% foundry concentration`: outside Day-4 military-balance notes; not audited here unless Day-3 source files are added to scope. Tag **UNVERIFIED in this source set**.

## Recommended fixes before publication locks

1. Replace “outspends it by at least 16:1 on official figures alone” with: **“outspends it by roughly 12:1 using the CSIS official 2025 PLA budget against Taiwan's 2026 budget; alternative headline estimates produce larger ratios.”**
2. Add a source or tag/remove: **66 F-16V**, **400 Harpoons**, **DF-17 ~300 seconds to TSMC**, **Fujian 2026–2027 OSD**.
3. Clarify the budget-opacity comparison: either keep **1.92x / ~$226B** as a cross-year estimate-range heuristic, or switch to same-year 2024 official **2.04x / ~$240B**.
4. Consider changing May-Dec ADIZ decline from **-5.4%** to **about -5%** unless CSIS exact underlying values justify -5.4.
