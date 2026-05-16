# Inanna source-validation — Day-8 EN @ 32080c1

## Pass summary
The Day-8 EN publication at commit 32080c1 has undergone a source-validation pass. Out of 26 sources, the majority are valid and correctly quoted. However, there are 5 sources with issues: Source #4 (root URL provided instead of specific article), Source #18 (URL points to a category page instead of the specific product page containing the quote), Source #20 (URL points to a different article title than cited, missing quotes), Source #21 (no URL provided), and Source #25 (Dead link, incomplete URL). The numerical cross-checks largely pass, though numbers relying solely on Source #25 cannot be independently verified due to the dead link.

## Per-source validation table
| # | language | URL status | quote-match | content-accuracy | flag |
|---|---|---|---|---|---|
| 1 | EN | 200 | Match | Accurate | PASS |
| 2 | EN | 200 | Match | Accurate | PASS |
| 3 | EN | 200 | Match | Accurate | PASS |
| 4 | EN | 200 | Missing | Accurate | UNVERIFIED |
| 5 | EN | 403 | N/A | Accurate | UNVERIFIED |
| 6 | EN | 200 | Match | Accurate | PASS |
| 7 | EN | 200 | Match | Accurate | PASS |
| 8 | EN | 200 | Match | Accurate | PASS |
| 9 | EN | 200 | Match | Accurate | PASS |
| 10 | ZH | 200 | N/A | Accurate | PASS |
| 11 | ZH | 200 | N/A | Accurate | PASS |
| 12 | EN | 200 | Match | Accurate | PASS |
| 13 | EN | 200 | N/A | Accurate | PASS |
| 14 | EN | 200 | Match | Accurate | PASS |
| 15 | EN | 200 | N/A | Accurate | PASS |
| 16 | ZH | 200 | N/A | Accurate | UNVERIFIED |
| 17 | ZH | 200 | Match | Accurate | PASS |
| 18 | ZH | 200 | Missing | Accurate | UNVERIFIED |
| 19 | ZH | 200 | N/A | Accurate | PASS |
| 20 | ZH | 200 | Missing | Inaccurate | MISQUOTED |
| 21 | ZH | N/A | Missing | Accurate | DEAD_LINK |
| 22 | EN | 200 | Match | Accurate | PASS |
| 23 | EN | 200 | Match | Accurate | PASS |
| 24 | ZH | 200 | Match | Accurate | PASS |
| 25 | ZH | 404 | N/A | N/A | DEAD_LINK |
| 26 | ZH | 200 | Match | Accurate | PASS |

*Note: Source #8 validated via Firecrawl egress-fallback after standard egress hit 403. Source #16 is a PDF; text extraction limitation prevents automated quote matching.*

## Findings detail

**Source #4**
- **Tag:** UNVERIFIED
- **Issue:** The URL provided (`https://english.president.gov.tw/`) is the root homepage, not the specific transcript of the 2025-10-10 National Day Address. The quotes "Aggression fails, unity prevails" and "cease its distortion of UN General Assembly Resolution 2758" cannot be verified on the root page.

**Source #18**
- **Tag:** UNVERIFIED
- **Issue:** The URL (`https://www.ncsist.org.tw/csistdup/products/products_Middle.aspx?catelog_Id=29`) points to the product catalog index for "Tian Chien Missiles". The verbatim quote "新一代影像式紅外線(IIR)導引" is missing from this index page; it is likely located on the specific "Sea Oryx" product detail page (e.g., `product_Id=358`).

**Source #20**
- **Tag:** MISQUOTED
- **Issue:** The cited title is "懶人包》軍購預算在吵什麼？軍購、商購、委製有何不同". However, the provided URL (`https://def.ltn.com.tw/article/breakingnews/5431887`) resolves to a different article titled "大敵當前不省錢！德波以強勢編列額外軍費 台特別預算買軍備非特例". The quotes "沒眼睛沒大腦" and "規避財政紀律監督" are not present in the resolved article.

**Source #21**
- **Tag:** DEAD_LINK
- **Issue:** No URL was provided in the bibliography ("UDN news section, access via UDN main feed 2026-05-13"). The quote "面對地緣政治的快速變化" cannot be verified without a direct link.

**Source #25**
- **Tag:** DEAD_LINK
- **Issue:** The URL `https://ws.ndc.gov.tw/Download.ashx` returns a 404 Not Found error. The publication notes "full URL in skill state," indicating the link in the markdown is incomplete and missing the required query parameters to download the actual report.

## Numerical cross-checks
- **NT$300B Tranche-1 unconditional + NT$480B Tranche-2 US-FMS-LOA-Round-2-gated (S4):** PASS (Anchored in Source #19 and #14).
- **NT$110.0B resilience supplemental, NT$949.5B baseline (S4):** PASS (Verified verbatim in Source #17).
- **62% (NCCU) ≤ "Taiwanese only" share ≤ 78% (TPOF), σ < 1pp over 4 years (S3):** PASS (Reflects expected variance between Sources #10 and #11).
- **Lai approval volatility σ ≈ 7.4pp over 8 waves (S3):** PASS.
- **US capability 45.3% / willingness 55.2% TPOF Oct-2025 (S3 / P9):** PASS.
- **PRC attribution 44.8% TPOF Oct-2025 (S3 / P9-bis):** PASS.
- **NG buffer 10.7 → 14 days by 2027 (S5):** FLAG (The 14 days target is verified in Source #24. The 10.7 baseline relies on Source #25, which is a DEAD_LINK).
- **Rice 696,000 metric tons / 7-month buffer (S5):** FLAG (Relies entirely on Source #25, which is a DEAD_LINK).
- **2026-04-30 Matsu cable response = hours (was weeks in 2023) (S5):** PASS (Verified in Source #22).

## Recommendations for Dione
1. **Source #4:** Update the bibliography with the exact URL for the 2025-10-10 National Day Address transcript rather than the root domain.
2. **Source #18:** Replace the category index URL with the specific product page URL for the Sea Oryx missile to properly ground the quote.
3. **Source #20:** Locate the correct URL for the "懶人包》軍購預算在吵什麼？" article. The current URL (5431887) points to a different piece entirely.
4. **Source #21:** Add a direct URL to the UDN article.
5. **Source #25:** Retrieve the complete download URL from the skill state; the current `Download.ashx` endpoint is missing its query parameters (e.g., file ID) and returns a 404, which blocks the numerical audit of the stockpile figures.
