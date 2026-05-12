---
date: 2026-05-12
lead: Dione
executor: Inanna
scope: S3 polling time-series
---

# Day-8 S3 Public Opinion Polling Data (2025-2026 Trajectory)

## Section A — NCCU ESC
**Methodology:**
Survey data is merged annually to generate data points (except those released in June; they come from surveys conducted between January and June). Results are weighted to parse out the data points. Data from the Election Study Center, National Chengchi University.

**Identity Time-Series (2022–2025):**
| Year | Taiwanese (%) | Both (%) | Chinese (%) | No Answer (%) |
| :--- | :--- | :--- | :--- | :--- |
| 2022 | 63.3 | 30.6 | 2.8 | 3.2 |
| 2023 | 61.7 | 32.0 | 2.4 | 3.9 |
| 2024 | 63.4 | 31.0 | 2.4 | 3.2 |
| 2025 | 62.0 | 31.7 | 2.5 | 3.8 |

**Unification-Independence Time-Series (2022–2025):**
| Year | Indep. ASAP | SQ → Indep. | SQ → Decide Later | SQ → Indefinitely | SQ → Unif. | Unif. ASAP | No Answer |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2022 | 6.0% | 25.1% | 28.4% | 27.3% | 5.2% | 1.4% | 6.6% |
| 2023 | 6.0% | 21.5% | 27.9% | 33.2% | 3.8% | 1.2% | 6.2% |
| 2024 | 5.8% | 22.5% | 26.4% | 34.1% | 4.0% | 1.1% | 6.1% |
| 2025 | 6.6% | 21.9% | 26.3% | 33.5% | 4.4% | 1.1% | 6.1% |

## Section B — TPOF
**Methodology:**
Adults 20 years of age and older residing in Taiwan were interviewed by telephone using live interviewers. Landline and cellphone numbers were drawn through dual-frame random sampling with a proportion of 70% from landlines and 30% from cellphones. Samples were demographically weighted to adjust for gender, age, education, and district of residency. Sampling error is around ±2.98 percentage points with 95% level of confidence.

**Lai Ching-te Approval Rating (Select 2024-2025 Waves):**
| Month | Approve (%) | Disapprove (%) | Don't Know / No Opinion (%) |
| :--- | :--- | :--- | :--- |
| May 2024 | 58.0 | 25.5 | 16.5 |
| Nov 2024 | 43.0 | 42.8 | 14.2 |
| Jan 2025 | 48.6 | 37.4 | 14.0 |
| May 2025 | 45.7 | 45.7 | 8.6 |
| Aug 2025 | 54.4 | 33.3 | 12.3 |
| Oct 2025 | 34.9 | 52.5 | 12.6 |
| Nov 2025 | 37.9 | 50.2 | 11.9 |
| Dec 2025 | 43.4 | 48.6 | 8.0 |

**Taiwanese Identity (Select 2025 Waves):**
- Jan 2025: 76.1% Taiwanese, 9.0% Both, 10.1% Chinese.
- July 2025: 77.4% Taiwanese, 10.4% Both, 6.4% Chinese.

**War Likelihood / Security Sentiment (Egress-Block Marker):**
```fallback-marker
TPOF full 12-month table for the 5-year war likelihood was not located as a single coherent markdown table due to image-embedded data constraints on the site.
Available discrete data points (Oct 2025): 44.8% blame PRC for cross-strait tensions; 45.3% believe U.S. President Trump is capable of preventing an invasion, but 44.8% believe he is unwilling to do so.
```

## Section C — Pew Research Center
**Methodology:**
Data comes from a survey of 2,277 adults in Taiwan conducted as part of a broader study of attitudes in the region. The survey was fielded from June 2 to Sept. 17, 2023. All interviews in Taiwan were conducted over the phone. Respondents were selected using probability-based sample designs. The data was weighted to account for selection probability and demographics.

**Findings (Latest Release - Jan 16, 2024):**
- 67% of adults in Taiwan consider themselves primarily Taiwanese.
- 28% think of themselves as both Taiwanese and Chinese.
- 3% think of themselves as primarily Chinese.
- Emotional attachment: 40% still report an emotional connection to the mainland (11% say they are very emotionally attached).
- Political tying: Identity is heavily tied to politics, with those identifying primarily as Taiwanese aligning largely with the DPP, and those holding dual or Chinese identity aligning closer to the KMT.

## Cross-Source Synthesis
**Identity Stability & Trajectory:**
The identity trend remains overwhelmingly stable. NCCU ESC shows the "Taiwanese only" identity hovering steadily around 62-63% through 2025, while TPOF pegs it consistently higher at 76-77%. Pew aligns closer to NCCU at 67%. While the baseline percentage differs between sources, the *drift rate* is essentially flat post-2024. The unification preference floor remains a minuscule, low-single-digit minority across the board.

**Methodological Disagreements & Variances:**
- **Identity Baseline Gap:** The ~14-point gap in "Taiwanese only" identity between NCCU/Pew (~62-67%) and TPOF (~76-77%) likely stems from questionnaire design and ordering. TPOF's methodology may push "Both" respondents into the "Taiwanese" column via harder forced-choice phrasing or specific political context priming before the identity question.
- **Volatility vs. Stability:** While baseline identity and unification sentiments are highly stable (NCCU), the political volatility appears exclusively in the executive/legislative arena (e.g., Lai's highly erratic approval ratings in TPOF polling, dropping to 34.9% in Oct 2025 before recovering slightly). This confirms the hypothesis that the threat perception/executive game remains stochastic, but the underlying identity floor is firmly locked.

## Source Bibliography
- [Source S3.A] National Chengchi University Election Study Center (NCCU ESC). Core Political Attitudes Trend Charts (Released Dec 2025).
- [Source S3.B] Taiwan Public Opinion Foundation (TPOF). Monthly Public Opinion Polls (Jan-Dec 2025).
- [Source S3.C] Pew Research Center. "Most people in Taiwan see themselves as primarily Taiwanese; few say they’re primarily Chinese" (Published Jan 16, 2024).