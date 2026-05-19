# Nisaba numerical audit — AMTI Scarborough monthly patrol-days series

Date: 2026-05-19  
Auditor: Nisaba 🌾 (`worker-codex`)  
Target: Day-11 GWW3 China-Taiwan ASEAN/PHL state-extension  
Primary source: CSIS AMTI, “Holding the Line: China’s Expanding Patrols around Scarborough Shoal,” published 2025-06-16, https://amti.csis.org/holding-the-line-chinas-expanding-patrols-around-scarborough-shoal/

## Input series checked

AMTI states that AIS-derived values are minimum estimates. The audit below uses the 10-row monthly series supplied for this pass:

| month | CCG ship-days | PCG/BFAR ship-days | interaction days |
|---|---:|---:|---:|
| 2024-08 | 35 | 18 | 5 |
| 2024-09 | 44 | 15 | 14 |
| 2024-10 | 42 | 22 | 16 |
| 2024-11 | 50 | 0 | 0 |
| 2024-12 | 69 | 22 | 4 |
| 2025-01 | 120 | 32 | 29 |
| 2025-02 | 76 | 11 | 6 |
| 2025-03 | 80 | 44 | 15 |
| 2025-04 | 91 | 37 | 28 |
| 2025-05 | 106 | 27 | 4 |

Methods: Welch two-sample t-tests are two-sided and compare Jan-May 2025 minus Aug-Dec 2024. Confidence intervals are 95% CIs for the mean difference in ship-days. Mann-Kendall p-values use the standard normal approximation with continuity correction and tie correction where needed. Correlation p-values are two-sided.

## 1. CCG 5-vs-5 binned Welch test

| bin | n | mean | SD |
|---|---:|---:|---:|
| Aug-Dec 2024 | 5 | 48.0 | 12.90 |
| Jan-May 2025 | 5 | 94.6 | 18.35 |

Result:

- Mean difference: **+46.6 ship-days**.
- Lift: **+97.1%** (`94.6 / 48.0 - 1`). This reproduces the reported **+97%** lift.
- Welch t-test: **t = 4.645**, **df = 7.18**, **p = 0.00221**.
- 95% CI for mean difference: **[+22.99, +70.21] ship-days**.

Audit judgment: the CCG +97% lift is arithmetically correct for the supplied series and statistically strong despite the small sample. The CI is wholly positive.

## 2. PCG/BFAR binned Welch test, including and excluding November 2024

AMTI attributes the November 2024 zero to capacity reallocation rather than a generic collection failure: Indonesia port visit, domestic disaster relief, Second Thomas Shoal resupply, and combat drills. Substantively, I would treat it as a **genuine operational zero** for the main test because it captures Philippine capacity limits in the same theater. Because it is also an extreme leverage point, the missing-data sensitivity is reported directly below.

### 2a. Main specification: November 2024 as genuine zero

| bin | n | mean | SD |
|---|---:|---:|---:|
| Aug-Dec 2024 | 5 | 15.4 | 9.10 |
| Jan-May 2025 | 5 | 30.2 | 12.44 |

Result:

- Mean difference: **+14.8 ship-days**.
- Lift from supplied rows: **+96.1%** (`30.2 / 15.4 - 1`).
- Welch t-test: **t = 2.147**, **df = 7.33**, **p = 0.0671**.
- 95% CI for mean difference: **[-1.35, +30.95] ship-days**.

### 2b. Sensitivity: November 2024 excluded as missing/non-comparable

| bin | n | mean | SD |
|---|---:|---:|---:|
| Aug, Sep, Oct, Dec 2024 | 4 | 19.25 | 3.40 |
| Jan-May 2025 | 5 | 30.2 | 12.44 |

Result:

- Mean difference: **+10.95 ship-days**.
- Lift from supplied nonzero late-2024 rows: **+56.9%** (`30.2 / 19.25 - 1`).
- Welch t-test: **t = 1.882**, **df = 4.73**, **p = 0.122**.
- 95% CI for mean difference: **[-4.26, +26.16] ship-days**.

Audit judgment: the supplied PCG/BFAR rows do **not** reproduce a +47% lift. They imply +96.1% if November is treated as a true zero, or +56.9% if November is excluded. A +47.3% lift would follow from `30.2 / 20.5 - 1`, but the supplied Aug-Dec values sum to 77 with November included (mean 15.4) and to 77 across the four nonzero months (mean 19.25), not 82 across four months (mean 20.5). Directionally, Philippine patrol-days rose, but the 5-vs-5 statistical evidence is weaker than the CCG result and the CI crosses zero in both specifications.

## 3. Mann-Kendall monotonic-trend tests

| series | n | S | tau | p |
|---|---:|---:|---:|---:|
| CCG ship-days | 10 | 35 | 0.778 | 0.00236 |
| PCG/BFAR ship-days, Nov as zero | 10 | 18 | 0.400 | 0.12685 |
| PCG/BFAR ship-days, Nov excluded/compressed | 9 | 15 | 0.417 | 0.14221 |

Audit judgment: CCG has a statistically clear upward monotonic trend across the 10-month window. PCG/BFAR has a positive but statistically non-significant monotonic trend under both November treatments.

## 4. Correlations

| relationship | Pearson r | Pearson p | Pearson 95% CI | Spearman rho | Spearman p |
|---|---:|---:|---:|---:|---:|
| CCG vs PCG/BFAR ship-days | 0.569 | 0.0858 | [-0.094, 0.883] | 0.608 | 0.0623 |
| Total ship-days (CCG + PCG/BFAR) vs interaction days | 0.580 | 0.0785 | [-0.078, 0.886] | 0.486 | 0.1541 |

Audit judgment: both correlations are positive but not conventionally significant at n=10. They are compatible with the qualitative claim that denser law-enforcement presence increases encounters, but the monthly sample is too short and uneven to treat these as stable effect estimates.

## 5. Optional regime-change test on CCG series

Pettitt test on the 10-month CCG series:

- Maximal change statistic: **K = 25**.
- Estimated split: **after 2024-12 / before 2025-01**, matching the hypothesized January 2025 regime shift.
- Approximate p-value: **p = 0.0661**.

Audit judgment: Pettitt identifies the expected January 2025 break, but at n=10 the evidence is suggestive rather than conventionally significant. This is consistent with the Welch result: the before/after difference is large, but the series is short.

## Bonus register-elevation marker: September 2025 USNI incident

Do **not** append this as a continuation row to the monthly AMTI series; it is event-level evidence, not a month-aggregate patrol-days observation.

Source checked: USNI News, Aaron-Matthew Lariosa, “VIDEO: Philippine Sailor Injured in Chinese Water Cannon Attack Near Scarborough Shoal,” published 2025-09-16, https://news.usni.org/2025/09/16/video-philippine-sailor-injured-in-chinese-water-cannon-attack-near-scarborough-shoal

Event markers suitable for narrative/register elevation:

- Incident date: **2025-09-16**.
- Location: **14 nautical miles east of Scarborough Shoal**.
- Philippine vessel: **BRP Datu Gumbay Piang / Datu Gumby Piang (MMOV 3014)**; USNI article uses both spellings in text/captions.
- Chinese vessels: **CCG 5201** and **Type 301-class coastal patrol boat 21562**.
- Action: port/starboard water-cannon attacks; one blast damaged the bridge and injured a Philippine sailor with flying glass.
- Register elevation: PLAN Type 054 frigate **Ma’anshan** broadcast a warning of a “prompt live fire exercise” at coordinate points directly east of Scarborough, causing fear/panic among Filipino fishermen according to the PCG release as reported by USNI.

Use as a September 2025 escalation/register marker, not as part of the Aug 2024-May 2025 monthly statistical series.

## Bottom-line audit notes for Day-11 draft use

- **CCG claim passes**: +97.1% lift, Welch p=0.00221, CI fully positive, MK trend p=0.00236.
- **PCG/BFAR claim needs correction/qualification**: the supplied rows do not reproduce the stated +47% baseline. The operational-zero specification gives +96.1% but only marginal Welch evidence (p=0.0671); the missing-zero sensitivity gives +56.9% and weaker evidence (p=0.122). Phrase as “directionally higher but statistically weaker and sensitive to the November capacity-reallocation zero,” unless a corrected AMTI chart extraction reconciles the 20.5 late-2024 mean.
- **Interactions linkage is plausible, not proven**: correlations are positive but n=10 and not conventionally significant.
- **January 2025 break is plausible**: Pettitt selects Jan 2025 as the split, p≈0.066.
