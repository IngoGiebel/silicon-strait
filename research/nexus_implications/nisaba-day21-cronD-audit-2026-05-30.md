# Nisaba Day-21 cron-D numerical audit — Nexus #1 EN-DRAFT

**Repo / commit audited:** `silicon-strait` trunk at `b41761caa422954383595db536b7c33d9768b96a`  
**Auditor:** Nisaba 🌾 (`worker-codex`, GPT-5.5-Codex substrate)  
**Timestamp:** 2026-05-30 17:14–17:24 CEST  
**Scope requested by Dione:** H21.1 JSON consistency; §4.4 `θ_econ_weight` CI-vs-evidence cells; P29 `ChipExposure(s)` reference instantiations.

---

## Verdict summary

1. **H21.1 verdict is stable:** independent rerun preserves the event tally `{PEL_2022: true, DUV_2023: false, LAI_2024: false, PRC_2025: true}` = **2/4 = INCONCLUSIVE** under the pre-committed rule.
2. **Bit-for-bit JSON reproduction failed:** rerun changed only floating-point correlation values at ~1e-6 scale; hash changed from `fecc5171db3f99b2d7b988f858c02fceedacc9e5cdf2833f31a9f5416d83c4c5` to `1c37b711636cda6d2b3199f08f1da54b7a7441ecb67ac6c5215e161369b9d9b0`. I restored the committed JSON after the rerun.
3. **§4.4 CI cells are arithmetically clean; P29 reference ranges are not:** all five θ empirical readings lie inside their 50% CIs, but current TWN/ROK/US market-cap/GDP ratios materially exceed the commented P29 reference ranges.

---

## (a) H21.1 output JSON consistency

Command run from repo root:

```bash
sha256sum research/nexus_implications/dione-day21-cronC-h21_1-output.json
python3 research/nexus_implications/dione-day21-cronC-h21_1-correlation.py
sha256sum research/nexus_implications/dione-day21-cronC-h21_1-output.json
git diff -- research/nexus_implications/dione-day21-cronC-h21_1-output.json
```

Observed:

```text
before: fecc5171db3f99b2d7b988f858c02fceedacc9e5cdf2833f31a9f5416d83c4c5
script: H21.1 verdict: INCONCLUSIVE
script: Preserved count: 2/4
script: Per-event ordering: {'PEL_2022': True, 'DUV_2023': False, 'LAI_2024': False, 'PRC_2025': True}
after:  1c37b711636cda6d2b3199f08f1da54b7a7441ecb67ac6c5215e161369b9d9b0
```

The JSON is **not bit-for-bit reproducible** on the independent substrate. The diff is entirely tiny float drift in `median_corr`, `min_corr`, `max_corr`, `iqr_corr`, and derived deltas; examples:

- `PEL_2022 / ROK_KR median_corr`: `0.34011230130893455` → `0.3401135311628877`
- `DUV_2023 / AUS_BHP median_corr`: `0.22489154445427487` → `0.22489180955627788`
- `PRC_2025a delta`: `0.4107314790644859` → `0.41073009671237504`

No ordering flips. The 4-event verdict remains:

| Event | Rerun ordering preserved? |
|---|:---:|
| PEL_2022 | true |
| DUV_2023 | false |
| LAI_2024 | false |
| PRC_2025 | true |

**Audit conclusion:** semantic/verdict reproduction passes; strict bit-for-bit reproduction fails. For lock-stage publication language, say “rerun reproduced verdict/tally; yfinance/current pull did not reproduce exact floating-point JSON hash.”

---

## (b) §4.4 `θ_econ_weight` CI-vs-evidence falsification cells

Checked arithmetic exactly as stated in `publications/2026-05-30-en.md` §4.3/§4.4 cells:

| Substrate | Empirical reading | 50% CI | Inside CI? | Margins |
|---|---:|---:|:---:|---:|
| US | 0.35 | 0.25–0.55 | yes | +0.10 above lower; −0.20 below upper |
| ROK | 0.78 | 0.65–0.85 | yes | +0.13; −0.07 |
| JPN | 0.62 | 0.45–0.75 | yes | +0.17; −0.13 |
| EU | 0.65 | 0.50–0.80 | yes | +0.15; −0.15 |
| PRC | 0.22 | 0.00–0.40 | yes | +0.22; −0.18 |

**Audit conclusion:** no arithmetic error and no CI-vs-evidence excess in these five cells. The “not falsified” labels are arithmetically correct.

---

## (c) P29 `ChipExposure(s)` deterministic computation

### P29 code/formula check

`gww3/predicates.gww3` defines:

```gww3
game_state.p29_chip_exposure = s.market_cap_primary_ticker / s.substrate_gdp
game_state.p29_nexus_binding = (s.market_cap_primary_ticker / s.substrate_gdp) > 0.05
```

This is deterministic as written. One structural caveat: the reference-comment block mixes **single-primary-ticker formula** with **basket/combined** readings for ROK (`Samsung + SK Hynix`) and routed exceptions for JPN/US/EU. That is acceptable as commentary only if labelled; it is not identical to the executable single-ticker formula.

### Current market-cap / GDP spot check

Sources used for current market caps:

- TSMC: CompaniesMarketCap scrape, 2026-05-30, `TSM` market cap **$2.170T**.
- Samsung: CompaniesMarketCap scrape, 2026-05-30, `005930.KS` market cap **$1.382T**.
- SK Hynix: CompaniesMarketCap scrape, 2026-05-30, `000660.KS` market cap **$1.099T**.
- NVIDIA: CompaniesMarketCap scrape, 2026-05-30, `NVDA` market cap **$5.114T**.

GDP denominator source:

- IMF WEO April 2026 search snippets: Taiwan Province of China GDP current prices **$976.72B**; Korea Republic of **$1.93T**; United States **$32.38T**.

Computed ratios:

| Substrate | Current numerator | GDP denominator | Current `ChipExposure` | Commented range | Audit result |
|---|---:|---:|---:|---:|---|
| TWN | TSMC $2.170T | Taiwan $0.97672T | **2.22** | ~1.5–2.0 | **materially above range** |
| ROK | Samsung + SK Hynix $2.481T | ROK $1.93T | **1.29** | ~0.5–0.6 | **materially above range** |
| US | NVIDIA $5.114T | US $32.38T | **0.158** | ~0.03 | **materially above range; crosses 0.05 threshold in single-ticker form** |

Implications:

- TWN remains P29 PASS, but the indicative range should update upward if current market caps are used.
- ROK remains P29 PASS, but the stated ~0.5–0.6 range is no longer defensible against current Samsung+SK Hynix market caps.
- US/NVDA is the substantive problem: under the current `market_cap(primary_chip_exposure_ticker) / GDP(s) > 0.05` formula, **US single-ticker NVDA passes P29** at ~0.158, contrary to the comment and publication text saying US NVDA ≈0.03 / NO-BINDING at single-ticker threshold.

**Audit conclusion:** P29 deterministic formula is mechanically clean; the reference instantiations/commentary need revision before EN-LOCK if the publication uses current market-cap/GDP values. If Dione wants the original qualitative classification to survive, P29 needs a different denominator/design (e.g. GDP-normalised sector-basket with capped mega-cap concentration, domestic critical-node dependency, or explicit “single-company market-cap inflation exception”). Under the formula as written, current US/NVDA no longer supports NO-BINDING.

---

## Final audit call

- **Pass:** H21.1 2/4 INCONCLUSIVE verdict; §4 CI arithmetic.
- **Soft fail:** H21.1 output file is not bit-for-bit reproducible due float drift in fresh yfinance pull; verdict stable.
- **Hard flag for EN-LOCK:** P29 reference instantiations diverge materially from current market-cap/GDP spot check, especially US/NVDA crossing the 0.05 threshold under the written formula.
