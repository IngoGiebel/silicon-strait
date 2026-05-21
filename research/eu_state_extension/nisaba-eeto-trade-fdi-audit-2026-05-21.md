# Nisaba numerical audit — EETO trade, FDI, and EP Taiwan cohesion

Date: 2026-05-21  
Auditor: Nisaba 🌾 (`worker-codex`)  
Target: Day-12 EU-institutional-bloc / EETO substrate synthesis  
Primary data pulled: Eurostat API (`ext_lt_maineu`, `bop_its6_det`, `bop_fdi6_geo`), European Commission DG TRADE Taiwan page, European Parliament press/vote pages, CATL/BYD/ProLogium/Bosch company pages, Rhodium/MERICS 2024 Chinese FDI update.

## Methods / limitations

- Goods trade is Eurostat annual EU27_2020 extra-EU goods trade with partner `TW`, indicators `MIO_EXP_VAL` + `MIO_IMP_VAL`, SITC total, years 2002-2024.
- Services trade is Eurostat BPM6 annual international trade in services with partner `TW`, item `S`, `CRE` + `DEB`, years 2010-2024. I did **not** splice a BPM5 pre-2010 services series inside this 600s pass, so the 2002/2003 institutional test is goods-only.
- Break tests: Pettitt is a rank-based unknown-break test; fixed-milestone tests use (a) Mann-Whitney before/after split and (b) Chow test on a linear trend with intercept+slope break where both sides have enough observations. 2024 cannot support a Chow test because there is only one post-2024 observation.
- All monetary amounts are current EUR millions unless explicitly stated otherwise.

## 1. EU-Taiwan bilateral trade timeline and structural breaks

### Input series checked

| year | EU exports goods | EU imports goods | goods total | services total | goods+services total |
|---:|---:|---:|---:|---:|---:|
| 2002 | 10,593.4 | 19,945.2 | 30,538.6 | n/a | n/a |
| 2003 | 9,737.8 | 19,598.7 | 29,336.5 | n/a | n/a |
| 2004 | 11,491.3 | 20,617.1 | 32,108.4 | n/a | n/a |
| 2005 | 11,698.2 | 20,745.6 | 32,443.8 | n/a | n/a |
| 2006 | 11,891.5 | 22,950.8 | 34,842.3 | n/a | n/a |
| 2007 | 11,961.7 | 22,275.5 | 34,237.2 | n/a | n/a |
| 2008 | 10,554.2 | 20,872.5 | 31,426.7 | n/a | n/a |
| 2009 | 9,197.9 | 15,345.9 | 24,543.8 | n/a | n/a |
| 2010 | 13,579.0 | 20,759.0 | 34,338.0 | 5,543.2 | 39,881.2 |
| 2011 | 14,741.8 | 20,447.5 | 35,189.3 | 5,493.5 | 40,682.8 |
| 2012 | 14,528.1 | 18,701.1 | 33,229.2 | 6,070.5 | 39,299.7 |
| 2013 | 15,143.5 | 18,102.9 | 33,246.4 | 6,270.7 | 39,517.1 |
| 2014 | 15,650.5 | 19,293.9 | 34,944.4 | 6,682.2 | 41,626.6 |
| 2015 | 16,842.1 | 21,204.6 | 38,046.7 | 6,970.6 | 45,017.3 |
| 2016 | 17,629.1 | 22,968.4 | 40,597.5 | 7,186.8 | 47,784.3 |
| 2017 | 19,358.2 | 25,397.1 | 44,755.3 | 7,742.1 | 52,497.4 |
| 2018 | 20,095.0 | 26,846.7 | 46,941.7 | 9,321.7 | 56,263.4 |
| 2019 | 23,572.5 | 27,405.7 | 50,978.2 | 9,808.5 | 60,786.7 |
| 2020 | 22,919.8 | 26,464.4 | 49,384.2 | 10,165.5 | 59,549.7 |
| 2021 | 28,431.8 | 35,628.6 | 64,060.4 | 13,896.0 | 77,956.4 |
| 2022 | 35,080.0 | 49,347.4 | 84,427.4 | 18,673.8 | 103,101.2 |
| 2023 | 30,538.0 | 47,876.2 | 78,414.2 | 19,311.3 | 97,725.5 |
| 2024 | 28,697.1 | 43,405.4 | 72,102.5 | 18,755.5 | 90,858.0 |

External cross-check: DG TRADE's Taiwan page reports 2025 total goods trade of €76.2b, EU exports €30.9b and imports €45.3b, matching the same Eurostat goods series logic for 2025.

### Tests

| series | test | statistic | p-value | split selected / milestone |
|---|---:|---:|---:|---|
| Goods 2002-2024 | Pettitt unknown break | K=130 | 0.000680 | selected 2013/2014, not 2003/2021/2024 |
| Goods 2002-2024 | fixed 2003 Mann-Whitney | U=2.0 | 0.261 | no detectable EETO-founding break; only one pre-2003 obs |
| Goods 2002-2024 | fixed 2021 Mann-Whitney | U=0.0 | 0.000226 | strong before/after difference |
| Goods 2002-2024 | fixed 2021 Chow | F=24.886 | 0.00000493 | strong intercept/slope break at 2021 |
| Goods 2002-2024 | fixed 2024 Mann-Whitney | U=2.0 | 0.261 | no detectable liaison-post break; only one post-2024 obs |
| Goods+services 2010-2024 | Pettitt unknown break | K=56 | 0.0107 | selected 2016/2017, not 2021/2024 |
| Goods+services 2010-2024 | fixed 2021 Mann-Whitney | U=0.0 | 0.00147 | strong before/after difference |
| Goods+services 2010-2024 | fixed 2021 Chow | F=12.670 | 0.00140 | strong intercept/slope break at 2021 |
| Goods+services 2010-2024 | fixed 2024 Mann-Whitney | U=2.0 | 0.400 | no detectable liaison-post break; only one post-2024 obs |

Audit judgment: the institutional-milestone break that survives quantitative testing is **2021**, not 2003 or 2024. The 2003 founding date is not statistically testable with a meaningful pre-period in this annual Eurostat series, and the 2024 liaison-officer date has only one post-treatment year. The series' own unknown-break tests select 2013/2014 for goods and 2016/2017 for goods+services, while the pre/post 2021 jump is still statistically strong.

Bottom-line phrasing for §3: **Eurostat trade data do not show a clean EETO-founding break in 2003 and cannot yet support a 2024 liaison-officer break; the statistically visible institutional-period jump is around the 2021 trade-and-investment-dialogue upgrade, after which EU-Taiwan goods+services trade shifts from a 2010-2020 mean of €47.5b to a 2021-2024 mean of €92.4b (Mann-Whitney p=0.0015; Chow p=0.0014).**

## 2. TSMC Dresden / ProLogium Dunkirk versus Hungary BYD/CATL FDI ratio

### Source checks

| item | claimed / usable amount | validation status | source note |
|---|---:|---|---|
| ESMC / TSMC Dresden | EPRS uses TSMC €3.5b; Bosch/BMWK page validates project total >€10b and up to €5b German support | Partly validated | Bosch says TSMC, Bosch, Infineon and NXP are jointly investing >€10b in ESMC; it does not itself isolate TSMC's €3.5b contribution. TSMC page was Cloudflare-blocked in this pass. |
| ProLogium Dunkirk | €5.2b | Validated against company primary | ProLogium press release: €5.2b for a 48 GWh gigafactory + R&D center in Dunkirk. |
| CATL Debrecen | €7.34b | Validated against company primary | CATL press release, 2022-08-12: €7.34b for 100 GWh Debrecen plant. |
| BYD Szeged | up to/about €4b | Not validated against BYD primary; BYD primary confirms project but omits amount | BYD official 2023-12-22 page confirms Szeged passenger-car plant, first BYD passenger-car factory in Europe, built in phases; amount requires secondary/reporting source. |

### Arithmetic ratio

| bundle | conservative amount | primary-validated / caveat |
|---|---:|---|
| Taiwan-linked EU-side substrate bind: TSMC Dresden + ProLogium Dunkirk | €8.5b using EPRS TSMC €3.5b + EPRS rounded ProLogium €5.0b | ProLogium primary supports €5.2b; TSMC isolated €3.5b not independently primary-validated in this pass. |
| Taiwan-linked EU-side substrate bind, using ProLogium primary exact | €8.7b | €3.5b + €5.2b. |
| PRC-linked Hungary substrate bind: CATL Debrecen + BYD Szeged | €11.34b | CATL €7.34b primary; BYD €4b not primary-confirmed by BYD page. |

Ratio calculations:

- EPRS-rounded Taiwan/EU bundle vs Hungary/PRC bundle: **€8.5b / €11.34b = 0.75**.
- ProLogium-primary exact Taiwan/EU bundle vs Hungary/PRC bundle: **€8.7b / €11.34b = 0.77**.
- In reverse, Hungary/PRC bundle is **1.30-1.33×** the Taiwan/EU bundle.

Audit judgment: directionally, the arithmetic supports Dione's substrate-asymmetry claim: **Hungary's PRC-linked anchor projects are larger than the EU-bloc Taiwan-linked anchor projects by roughly one-third**. Qualification: the direction is robust to €5.0b vs €5.2b ProLogium treatment, but the BYD €4b and isolated TSMC €3.5b components still need original filing-level confirmation if the draft wants a strict "primary-only" statement.

Bottom-line phrasing for §3: **On the currently sourced project values, the Hungary-PRC industrial bind (CATL Debrecen €7.34b + BYD Szeged ≈€4b ≈ €11.3b) is larger than the EU-bloc Taiwan bind (TSMC Dresden €3.5b + ProLogium Dunkirk €5.0-5.2b ≈ €8.5-8.7b), a Taiwan/EU-to-Hungary/PRC ratio of only 0.75-0.77. The asymmetry direction matches the political-substrate finding: the Hungary-side PRC bind is larger.**

## 3. EU FDI in Taiwan 2013 → 2022 lift validation

Eurostat dataset: `bop_fdi6_geo`, `geo=EU27_2020`, `partner=TW`, `indic_bp=STOCKS`, `fdi_item=DO__D__F` (Direct investment abroad / DIA). These are FDI **positions/stocks at year-end**, not annual-flow averages.

| year | EU DIA stock in Taiwan | Taiwan DIRE stock in EU |
|---:|---:|---:|
| 2013 | 6,803.1 | 872.7 |
| 2014 | 7,830.4 | 881.4 |
| 2015 | 16,408.0 | 6,010.5 |
| 2016 | 20,102.0 | 8,373.1 |
| 2017 | 21,589.6 | 10,116.3 |
| 2018 | 23,948.2 | 10,891.6 |
| 2019 | 26,779.4 | 13,872.4 |
| 2020 | 23,852.1 | 14,786.2 |
| 2021 | 29,639.2 | 15,819.6 |
| 2022 | 31,957.1 | 13,960.5 |
| 2023 | 31,755.3 | 14,438.8 |
| 2024 | 30,350.1 | 14,756.2 |

Result:

- Eurostat current pull: **€6.803b (2013) → €31.957b (2022)**.
- Lift: **4.70×**, not 4.2×, on the current Eurostat EU27_2020 data.
- CAGR over 9 years: **18.75% per year**.
- EPRS/EP Think Tank archived figure says **€6.8b → €28.4b**, i.e. **4.17×** and **17.2% CAGR**. That figure appears to be based on an earlier Eurostat vintage or chart extraction, but it is still clearly stock/position data, not stock-average.

Audit judgment: the EPRS 4.2× statement is directionally anchored and close for the 2013 base, but **does not reproduce against the current Eurostat API**, which gives 4.70× for the same start/end years. Phrase as "at least fourfold" unless the draft freezes the EPRS vintage explicitly.

Bottom-line phrasing for §3: **EU direct-investment stock in Taiwan rose from €6.8b in 2013 to €32.0b in the current Eurostat 2022 pull — a 4.70× lift and 18.8% CAGR. EPRS's published €28.4b/4.2× figure is a conservative older-vintage/briefing figure; both versions are year-end FDI stock positions, not annual-flow averages.**

## 4. EP voting majorities on Taiwan as deterministic-floor variable

### Vote checks and cohesion metrics

| vote | source | for | against | abstain | total voting | yes share of all votes | yes/(yes+no) | yes:no ratio | abstain share |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2021 EU-Taiwan political relations / rename EETO to EU Office in Taiwan | EP press release, 2021-10-21 | 580 | 26 | 66 | 672 | 86.3% | 95.7% | 22.3:1 | 9.8% |
| 2024 UN Resolution 2758 / Taiwan | HowTheyVote + EP links, 2024-10-24 | 432 | 60 | 71 | 563 | 76.7% | 87.8% | 7.2:1 | 12.6% |
| Comparator: 2024 Ukraine financial+military support | HowTheyVote, 2024-09-19 | 425 | 131 | 63 | 619 | 68.7% | 76.4% | 3.2:1 | 10.2% |

Baseline definition used: one high-salience 2024 foreign-policy comparator where the EP had a real cleavage — continued financial and military support to Ukraine by Member States (`RC-B10-0028/2024`). This is a conservative baseline because Ukraine support is generally a high-consensus EP issue but still generated a sizeable opposition/sovereigntist vote.

Audit judgment: the two Taiwan votes are not merely simple majorities; they are **supermajority floors**. Cohesion declined from the 2021 rename resolution to the 2024 UN-2758 resolution, but even the lower 2024 Taiwan vote was more cohesive than the Ukraine military-financial-support comparator: 76.7% yes share vs 68.7%, and a 7.2:1 yes:no ratio vs 3.2:1.

Bottom-line phrasing for §3: **EP Taiwan positioning is a deterministic floor, not a marginal preference: the 2021 rename resolution passed 580-26-66 (86.3% yes; 22.3 yes votes per no), and the 2024 UN-2758 resolution still passed 432-60-71 (76.7% yes; 7.2:1 yes:no), exceeding a high-salience 2024 Ukraine-support comparator on yes share and yes:no cohesion.**

## 5. Bonus: Hungary FDI ratio test, partial

I did not complete a country-origin inward-FDI stock/flow matrix for Hungary 2020-2024 within the 600s window. The best fast external check is the Rhodium/MERICS 2024 Chinese FDI update:

- Chinese FDI in the EU+UK reached **€10b in 2024**.
- Greenfield investment reached **€5.9b**.
- Hungary accounted for **31% of all Chinese FDI in Europe** in 2024, the highest share of any country.
- Rhodium/MERICS still cautions that Chinese EV FDI remains small compared with total European FDI stocks and that EU/US/South Korean partners are still ahead overall.

Partial inference: this supports the **marginal/new-greenfield** substrate-bind claim for Hungary, but it does **not** prove that PRC-origin FDI dominates Hungary's total inward FDI stock or total 2020-2024 inward FDI flows versus EU-origin investment. That requires MNB/OECD/Eurostat bilateral FDI positions by ultimate investor, not only project announcements.

## Bottom-line audit notes for Day-12 draft use

- **Trade break:** 2021 is the quantitatively visible institutional-period break; 2003 and 2024 are not statistically detectable with this annual data structure.
- **FDI project asymmetry:** Hungary-PRC anchor projects are larger than Taiwan-EU anchor projects by roughly one-third; use ratio **0.75-0.77** Taiwan/EU : Hungary/PRC, with a caveat on BYD and TSMC component-level primary confirmation.
- **EU FDI in Taiwan:** current Eurostat gives **€6.8b → €32.0b**, **4.70×**, **18.8% CAGR**; EPRS's 4.2× is conservative/older-vintage, not wrong in direction.
- **EP cohesion:** Taiwan resolutions clear a supermajority floor; 2024 cohesion declined from 2021 but remains stronger than the selected Ukraine-support foreign-policy comparator.
- **Bonus Hungary-share:** partial only; Rhodium/MERICS confirms Hungary captured **31%** of Chinese FDI in Europe in 2024, but not the PRC share of total inward FDI to Hungary.
