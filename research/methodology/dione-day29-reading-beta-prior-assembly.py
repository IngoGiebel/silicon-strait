#!/usr/bin/env python3
# Reading-β per-substrate prior-table assembly — Day-29 cron-C BEGIN
#
# Run: uv run --with numpy research/methodology/dione-day29-reading-beta-prior-assembly.py
#
# Implements the FROZEN construction protocol of the cron-A execution
# pre-registration (research/methodology/
# dione-day29-cronA-reading-beta-execution-pre-registration-2026-06-13.md, commit 29f8c8e).
# The rules below are pre-committed; this script does not tune them to outcome.
#
#   §1  Prior window = Day-1..Day-24 (substrate-extension era). H21.1c orthogonality re-test excluded (in-flight).
#   §3.2 Per substrate: pooled median δ over in-scope days, equal-weight across days.
#        PASS/FAIL thresholds = prior-90th / prior-10th percentile (numpy.percentile linear interpolation).
#   §3.3 ROK instrument-discontinuity: prior built on 005930.KS (M-25-1 instrument) only.
#        EWY-era δ EXCLUDED (not merged — the Day-26 §3.4 mask offset reconciles masks for the
#        SAME instrument, not different instruments). 005930.KS below min-n → low-power flagged.
#   §3.4 Mask = global NYSE-aligned, intersected with each pair's rolling window. min-n = 5.
#   §3.5 Verdict rule (PASS>p90 / FAIL<p10 / else INCONCLUSIVE) is for FUTURE live δ_s — NOT run here.
#        This script produces the prior table only; no live δ is tested.
#   §2  Anchor-era stratification = SECONDARY diagnostic overlay (q-day28-2 = stratify-as-secondary);
#        raises pooled_prior_masks_sign_opposite_regimes flag; no verdict effect.
#   §6  No silent truncation: every substrate considered is listed with n + disposition + reason.
#
# STATUS (Day-29 cron-C): this is the BEGIN. The δ manifest below is the preliminary
# enumeration from the cron-C archaeology sweep (Day-24 cross-substrate sweep read directly +
# Day-22 IND). Full enumeration verification, IND-comparability ruling, AUS/CAN/PHL/UK
# zero-confirmation, and the Nisaba §4 audit are cron-D/cron-E work. Commit-or-defer at the
# Sprint-16 boundary 2026-06-19.

import json

import numpy as np

MIN_N = 5  # §3.4, fixed pre-hoc (smallest n for which a 10th/90th-pctile is non-degenerate)
PRIOR_WINDOW = "Day-1..Day-24 (substrate-extension era)"

# ---------------------------------------------------------------------------
# δ MANIFEST — extracted Day-29 cron-C, full provenance. Pooled three-anchor δ
# (DUV_2023 / LAI_2024 / PRC_2025), global NYSE-aligned mask, vs TSM, unless noted.
# `era` distinguishes ROK instrument generations for the §3.3 discontinuity rule.
# `in_prior` is the pre-committed disposition reason; the code re-derives it, this
# field is the human-readable audit annotation.
# ---------------------------------------------------------------------------
MANIFEST = {
    "US": [
        {"day": 24, "date": "2026-06-03", "instrument": "SPY", "delta": 0.03419517972810138,
         "mask": "global_nyse", "era": "primary",
         "source": "research/cross_substrate/dione-day24-cronC-output.json:51",
         "anchor_legs": None},  # Day-24 sweep stores pooled δ only; no per-anchor legs persisted
    ],
    "JPN": [
        {"day": 24, "date": "2026-06-03", "instrument": "EWJ", "delta": 0.054666977480896106,
         "mask": "global_nyse", "era": "primary",
         "source": "research/cross_substrate/dione-day24-cronC-output.json:67",
         "anchor_legs": None},
    ],
    "ROK": [
        # EWY-era — EXCLUDED from the ROK prior per §3.3 (instrument discontinuity).
        {"day": 24, "date": "2026-06-03", "instrument": "EWY", "delta": -0.0076781969597641275,
         "mask": "global_nyse", "era": "ewy_pre_m25_1",
         "source": "research/cross_substrate/dione-day24-cronC-output.json:83",
         "anchor_legs": None},
        # 005930.KS-era measurements (Day-25 H25.1 +0.0546, Day-26 H26.1 +0.0515) are OUTSIDE
        # the Day-1..Day-24 prior window AND are the live-test era. They are NOT prior days and
        # are intentionally absent from this manifest. Documented here so the absence is not silent.
    ],
    "EU": [
        # EZU only. Member ETFs EWG/EWQ/EWN are H25.2 decomposition (Day-28), NOT prior days (§3.1).
        {"day": 24, "date": "2026-06-03", "instrument": "EZU", "delta": 0.07958933801768592,
         "mask": "global_nyse", "era": "primary",
         "source": "research/cross_substrate/dione-day24-cronC-output.json:99",
         "anchor_legs": None},
    ],
    "IND": [
        # CAVEAT (cron-C, pending cron-D verification + Nisaba ruling): the Day-22 IND δ pools over
        # a 7-event India-specific set (Galwan_2020, PEL_2022, Tawang_2022, DUV_2023, LAI_2024,
        # PRC_2025a, PRC_2025i) — NOT the 3-anchor cross-strait set used for US/JPN/EU. Intra-substrate
        # consistency (prior vs future live δ measured the same way) is what the per-substrate verdict
        # needs, so this is admissible in principle, but the comparability note is logged for audit.
        {"day": 22, "date": "2026-06-01", "instrument": "INDA", "delta": 0.052980496547778866,
         "mask": "global_nyse", "era": "primary",
         "source": "research/india_substrate/dione-day22-cronD-h21_1ab-output.json:363",
         "anchor_legs": None, "comparability_caveat": "7-event India set, not 3-anchor cross-strait set"},
    ],
    # Substrates in the §3.1 universe with ZERO textual-axis δ in the Day-1..Day-24 window.
    # Present in state-extension dirs as qualitative substrate_dynamics() instantiations only —
    # no computed correlation-pair δ. Listed explicitly (§6 no-silent-truncation), n=0.
    "AUS": [],
    "CAN": [],
    "PHL": [],
    "UK": [],
}

# ---------------------------------------------------------------------------
# §3.3 ROK instrument-discontinuity filter: keep 005930.KS era only; drop EWY era.
# ---------------------------------------------------------------------------
def in_prior_days(substrate, entries):
    kept = []
    for e in entries:
        if substrate == "ROK" and e["era"] == "ewy_pre_m25_1":
            continue  # EXCLUDED — not merged (§3.3)
        kept.append(e)
    return kept


def assemble():
    table = {}
    for substrate, entries in MANIFEST.items():
        prior = in_prior_days(substrate, entries)
        deltas = [e["delta"] for e in prior]
        n = len(deltas)
        low_power = n < MIN_N

        rec = {
            "instrument": sorted({e["instrument"] for e in prior}) or
                          sorted({e["instrument"] for e in entries}) or [None],
            "mask": "global_nyse",
            "prior_window": PRIOR_WINDOW,
            "in_scope_days": [{"day": e["day"], "date": e["date"], "instrument": e["instrument"],
                               "delta": e["delta"], "source": e["source"]} for e in prior],
            "delta_series": deltas,
            "n": n,
            "min_n": MIN_N,
            "low_power_flag": low_power,
            "verdict_emittable": (not low_power),
        }

        if n >= 1:
            rec["median_prior"] = float(np.median(deltas))
        else:
            rec["median_prior"] = None
        # Percentile thresholds only meaningful at/above min-n; below that they are degenerate
        # (a single point is its own p10 and p90). Report as null when low-power, with reason.
        if not low_power:
            rec["pctile_10"] = float(np.percentile(deltas, 10))
            rec["pctile_90"] = float(np.percentile(deltas, 90))
        else:
            rec["pctile_10"] = None
            rec["pctile_90"] = None
            rec["pctile_suppressed_reason"] = (
                f"n={n} < min_n={MIN_N}; 10th/90th-percentile degenerate. "
                "Verdict suppressed (reported, not emitted) per §3.3/§3.4 low-power rule.")

        # ROK-specific exclusion note (§3.3)
        if substrate == "ROK":
            excluded = [e for e in entries if e["era"] == "ewy_pre_m25_1"]
            rec["rok_instrument_discontinuity"] = {
                "prior_instrument": "005930.KS (M-25-1)",
                "excluded_ewy_era_days": [{"day": e["day"], "delta": e["delta"]} for e in excluded],
                "note": "005930.KS in-scope days within Day-1..Day-24 = 0 (005930.KS enters Day-25). "
                        "EWY-era excluded not merged. ROK prior is empty in this window.",
            }

        # IND comparability caveat surfaced (§6)
        caveats = [e["comparability_caveat"] for e in prior if e.get("comparability_caveat")]
        if caveats:
            rec["comparability_caveats"] = caveats

        # §2 SECONDARY anchor-era overlay — NOT computable from available data.
        legs_available = any(e.get("anchor_legs") for e in prior)
        rec["anchor_era_priors"] = None
        rec["pooled_prior_masks_sign_opposite_regimes"] = None
        rec["anchor_era_overlay_status"] = (
            "not_computable_from_available_data: the Day-24 cross-substrate sweep persisted pooled "
            "δ only (no per-anchor DUV/LAI/PRC legs). The secondary stratification overlay requires "
            "per-anchor legs per substrate-day; computing it needs re-running the Day-24 sweep with "
            "per-anchor output. Logged, not silently skipped (§6)."
            if not legs_available else "computable"
        )

        table[substrate] = rec
    return table


def main():
    table = assemble()
    out = {
        "artifact": "reading-β prior table (Day-29 cron-C BEGIN — preliminary)",
        "pre_registration": "research/methodology/"
                            "dione-day29-cronA-reading-beta-execution-pre-registration-2026-06-13.md",
        "pre_registration_commit": "29f8c8e",
        "prior_window": PRIOR_WINDOW,
        "min_n": MIN_N,
        "mask_convention": "global_nyse (§3.4)",
        "status": "PRELIMINARY — cron-C BEGIN. Manifest = cron-C archaeology sweep. Full verification, "
                  "IND-comparability ruling, AUS/CAN/PHL/UK zero-confirmation, and Nisaba §4 audit are "
                  "cron-D/cron-E work. Commit-or-defer call at Sprint-16 boundary 2026-06-19.",
        "substrates": table,
    }

    # Headline finding (printed; also derivable from the table)
    emittable = [s for s, r in table.items() if r["verdict_emittable"]]
    low_power = [s for s, r in table.items() if r["low_power_flag"]]
    out["headline_finding"] = {
        "substrates_with_emittable_verdict": emittable,
        "substrates_low_power_suppressed": low_power,
        "reading": (
            "NO substrate reaches min_n=5 in the Day-1..Day-24 window: the project ran one "
            "cross-substrate textual-axis sweep (Day-24) plus the Day-22 IND measurement, so every "
            "substrate's prior is n<=1. Under the frozen §3 rules the β-v1 prior emits ZERO verdicts "
            "(all low-power suppressed). ROK is empty (EWY excluded, 005930.KS outside window). "
            "This is a load-bearing input to the 2026-06-19 commit-or-defer call: β-v1 as pre-registered "
            "is not constructible on this window. Remedies (each its own pre-registration, never a "
            "retrofit per §6): (a) extend the prior window past Day-24 to admit accumulated live-era δ; "
            "(b) lower min_n; (c) defer β. Decision is NOT taken here."
        ),
    }

    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
