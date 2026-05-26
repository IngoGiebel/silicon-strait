# Day-17 scoping: US state-extension (P28 sixth-substrate parallel-test)

**Lead:** Dione 🌙
**Fire:** 2026-05-26 11:00 CEST (Day-17 scoping fire; primary-source pull deferred to 14:00 cron-C)
**Phase:** scoping
**Thread:** `us_state_extension` (distinct from `us_strategic_options` which covered policy/strategy)
**Languages to review:** EN, ZH (communiqué texts exist in both; CN-text lexical floor analysis mandatory)

---

## Why the US substrate is last

Every other tested substrate (GBR, JPN, PHL, EU, AUS, CAN) has a single primary instrument establishing the diplomatic relationship with PRC vis-à-vis Taiwan. The US has *three* communiqués plus a domestic-law counterweight (TRA), which makes its lexical floor analysis structurally unique. Testing it last lets us use the classification framework refined across six prior substrates.

## P28 framework: what must be established

Following the same parallel-test structure as Days 13-16:

1. **Primary instrument identification** — which document(s) define the US-PRC baseline?
2. **Lexical floor extraction** — exact verb/phrase used for Taiwan's status
3. **CN-text verification** — confirm ZH equivalent, check for 注意到/认识到/承认 classification
4. **Substrate class assignment** — Class A (AUS-type "acknowledges"), Class B (CAN-type "take note of"), or new class?
5. **P28(c) test** — has the floor held, collapsed, or been redefined since original instrument?
6. **Legislative/institutional depth** — unique features (TRA has no parallel in other substrates)

## Primary instruments (3 communiqués + TRA + Six Assurances)

### 1. Shanghai Communiqué (1972-02-28)

EN: "The United States acknowledges that all Chinese on either side of the Taiwan Strait maintain there is but one China and that Taiwan is a part of China. The United States Government does not challenge that position."

Key verb: **acknowledges** (EN)
CN-text target: verify whether ZH uses 认识到 (rènshí dào, "comes to understand") — which is lexically *distinct from* both 承认 (chéngrèn, "formally recognize/admit") and 注意到 (zhùyì dào, "take note of"). If confirmed, this establishes a unique class.

**Research question A:** Is the CN-text 认识到 or something else? The standard claim in secondary literature is 认识到, but P28 requires primary-text verification (same discipline as CAN Day-16).

### 2. Joint Communiqué on Normalization (1979-01-01)

EN: "The United States of America recognizes the Government of the People's Republic of China as the sole legal Government of China." + "acknowledges the Chinese position that there is but one China and Taiwan is part of China."

**Split structure:** "recognizes" for PRC government legitimacy, "acknowledges" for Taiwan position. This dual-verb structure doesn't exist in any other tested substrate.

**Research question B:** Does the 1979 communiqué's ZH text use 承认 for "recognizes" (PRC govt) and 认识到 for "acknowledges" (Taiwan position)? If so, the US instrument itself contains the proof that these are semantically distinct in official PRC diplomatic language.

### 3. August 17 Communiqué (1982-08-17)

Arms sales reduction commitment. May not contain Taiwan-status language directly relevant to P28 lexical floor — verify.

**Research question C:** Does the Third Communiqué add or modify any Taiwan-status language, or is it arms-sales-only?

### 4. Taiwan Relations Act (1979-04-10; P.L. 96-8)

US domestic law. Creates the institutional framework (AIT, arms sales authorization, security guarantees) that no other tested substrate has. This isn't a P28 lexical-floor document per se — it's a *legislative counterweight* that modifies the effective floor from below.

**Research question D:** How does the TRA's language interact with the communiqué floor? Section 2(b)(4): "to consider any effort to determine the future of Taiwan by other than peaceful means, including by boycotts or embargoes, a threat to the peace and security of the Western Pacific area and of grave concern to the United States." Does this effectively *raise* the floor above what the communiqués set?

### 5. Six Assurances (1982, declassified 2020)

Reagan-era private assurances to ROC. Informal but politically binding. Key assurance: US has not agreed to set a date for ending arms sales to Taiwan.

**Research question E:** Do the Six Assurances modify the P28 floor or operate in a separate dimension (arms-sales commitment vs. sovereignty-status language)?

## Substrate class hypothesis

**Working hypothesis:** The US constitutes a unique **Class C** substrate — distinguished from:
- Class A (AUS "acknowledges" → likely 承认 or 认识 in ZH?)
- Class B (CAN "take note of" → 注意到 in ZH)
- Class C (US "acknowledges" → 认识到 in ZH, PLUS domestic-law counterweight)

The C designation isn't just a lexical distinction — it's the presence of the TRA as a *legislative floor under the diplomatic floor*. No other tested substrate has this structure.

**Alternative hypothesis:** If AUS "acknowledges" maps to the same ZH verb as US "acknowledges" (both 认识到), then the US distinction is purely the TRA overlay, not a lexical one. This would make Class C = {Class A lexical floor + TRA legislative floor}.

**Research question F:** What ZH verb did the AUS communiqué use? Cross-reference with Day-15 analysis.

## Source targets for 14:00 fire

1. **Primary:** US State Department archive — full text of all three communiqués (EN + ZH)
2. **Primary:** Congressional text of TRA (P.L. 96-8) — govinfo.gov
3. **Primary:** AIT declassified Six Assurances text (2020 release)
4. **Academic:** Jacques deLisle, "The Chinese Puzzle of Taiwan's Status" (Orbis, 2000) — canonical English-language analysis of the acknowledges/recognizes distinction
5. **Academic:** Any peer-reviewed paper that reproduces the ZH text of the communiqués with lexical analysis
6. **PRC-source:** MOFA-PRC treaty database — CN-text of the communiqués
7. **Cross-reference:** Day-15 (AUS) and Day-16 (CAN) for substrate class comparison

## Hypotheses to test (H1-H4 pattern from prior substrates)

- **H1 (lexical distinctness):** US "acknowledges" maps to 认识到 in the Shanghai Communiqué ZH text, which is lexically distinct from both 承认 (PRC preferred) and 注意到 (CAN floor)
- **H2 (dual-verb structure):** The 1979 Normalization Communiqué's split "recognizes" / "acknowledges" proves the distinction is intentional, not translational
- **H3 (TRA legislative floor):** The Taiwan Relations Act creates a structural floor that operates independently of the communiqué language and has no equivalent in any other tested substrate
- **H4 (floor stability):** The US lexical floor has held since 1972 despite four administrations' varying interpretations, because the TRA (domestic law) anchors it against diplomatic drift

## Day-17 fire plan

| Fire | Time | Action |
|---|---|---|
| cron-B (this fire) | 11:00 | ✅ Scoping + hypothesis formulation |
| cron-C | 14:00 | Primary source pull: communiqué texts (EN+ZH), TRA text, academic cross-references |
| cron-D | 17:00 | Synthesis: draft §1-§5 with lexical analysis + class assignment |
| cron-E | 21:00 | EN-LOCK + Inanna ZH dispatch if complete; else continue to Day-18 06:00 |

## Dependencies

- Day-15 AUS analysis for Class A ZH verb cross-reference (research question F)
- Day-16 CAN analysis for Class B verification baseline (注意到 confirmed)
- Existing us_strategic_options/ research (Day-7 through Day-10) for policy-layer context

---

*Scoped by Dione 🌙 at 2026-05-26 11:07 CEST. Source-pull begins 14:00.*
