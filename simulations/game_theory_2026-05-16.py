#!/usr/bin/env python3
"""Day-9 deterministic 5-player pruning evaluation for Silicon Strait.

Scope: first-cut deterministic branch-elimination only. This file deliberately
ignores the documentary stochastic block in gww3/predicates.gww3 because q1
(GWW3 stochastic runtime documentation) is still open. No randomness, no Nash
solver, no belief dynamics.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
PREDICATES_PATH = ROOT / "gww3" / "predicates.gww3"
RESULT_PATH = ROOT / "simulations" / "results" / "day9-five-player-pruning-eval-2026-05-16.json"
PARSER_VERSION = "gsl_ops.lark v1.2"
AUDIT_BASIS_COMMIT = "ea531e5"  # Day-8 Nisaba numerical audit header: audited commit.


@dataclass(frozen=True)
class USExecState:
    """US_Exec: Trump-2 executive node plus FMS-LOA action promotion."""

    name: str = "US_Exec"
    transactional_rhetoric_active: bool = True  # Day-7 S7 / Day-8 S6.a qualitative state.
    can_unilaterally_repeal_statutory_substrate: bool = False  # Day-7 S8 substrate gate; sources #19/#20/#21/#6/#7/#8.
    taiwan_nuclear_umbrella_doctrinally_explicit: bool = False  # Day-7 S6/S8; NPR-2022 source #23.
    fms_loa_round_2_issued: bool = False  # Day-8 S4/S6 P12/P12-bis current pre-Round-2 state; sources #14/#15/#19/#20.
    action_nodes: tuple[str, str] = ("extend_security_umbrella", "fms_loa_cadence")


@dataclass(frozen=True)
class USLegState:
    """US_Leg: Taiwan Caucus + statute-encoded commitment substrate."""

    name: str = "US_Leg"
    taiwan_caucus_member_count_range_119th: tuple[int, int] = (114, 139)  # Day-7 S7 source #28.
    statutory_substrate_repeal_path: str = "supermajority"  # Day-7 S8 substrate-protection gate.
    chips_clawback_years: int = 10  # CHIPS Act §103/§107; Day-7 source #19.
    tera_fmf_authorization_usd_b: float = 10.0  # TERA authorization; Day-7 source #6.
    ndaa_taiwan_cycles: int = 4  # FY2023-FY2026 density from Day-7 S1/S8; sources #6/#7/#8 plus S8 text.


@dataclass(frozen=True)
class PRCState:
    """PRC composite: CCP/MOFA/MOD/TAO with Xi as principal."""

    name: str = "PRC"
    taipei_track_lever: str = "transactional_executive"  # Day-7 S7/S8 TAO pattern; sources #29/#30.
    washington_track_lever: str = "core_interest"  # Day-7 S7/S8 MOFA pattern; sources #29/#30.
    pitched_energy_reunification_inducement: bool = True  # Day-8 S5/S6 D8.1; source #23.
    attempts_statutory_substrate_negotiation: bool = False  # Day-7 S8 briefing-pattern verdict.
    warhead_trajectory: tuple[int, int, int] = (600, 1000, 1500)  # Day-7 S6 source #26; stochastic residual only.


@dataclass(frozen=True)
class ROCExecState:
    """ROC_Exec: Lai administration doctrinal stack and energy substrate."""

    name: str = "ROC_Exec"
    sovereignty_position: str = "non_subordinate_to_PRC"  # P1; Day-8 source #1, reaffirmed #2/#4.
    threat_perception_state: str = "escalating"  # P3 shell; Day-8 source #2.
    doctrinal_layer_count: int = 4  # P15; nuclear-restart energy layer, Day-8 source #23.
    nuclear_restart_pivot_active_since: str = "2026-03"  # P15; source #23.
    kmt_cross_strait_energy_framing_preempted: bool = True  # P15/D8.1; source #23.
    can_unilaterally_release_tranche2: bool = False  # P12; source #15/#19.


@dataclass(frozen=True)
class ROCLegState:
    """ROC_Leg: DPP/KMT/TPP legislature with KMT caucus gate."""

    name: str = "ROC_Leg"
    dpp_seat_share_below_half: bool = True  # P2; Day-8 sources #2/#3.
    kmt_chair: str = "Cheng_Li_wun"  # P4; Day-8 sources #6/#7/#8.
    kmt_joint_declarations_date: str = "2026-02-03"  # P4; sources #6/#7.
    kmt_doctrinal_alignment_active: bool = True  # P4.
    kmt_repudiation_path: str = "new_chair_election_or_joint_decl_withdrawal"  # P4.
    defense_special_total_ntd_b: float = 780.0  # P5/P10/P12; source #15/#19, audit CLEAN.
    tranche1_unconditional_ntd_b: float = 300.0  # P10/P12; source #15/#19, audit CLEAN.
    tranche2_loa_gated_ntd_b: float = 480.0  # P10/P12; source #15/#19, audit CLEAN.


@dataclass(frozen=True)
class DeterministicState:
    """Full deterministic 5-player snapshot consumed by pruning evaluators."""

    us_exec: USExecState = field(default_factory=USExecState)
    us_leg: USLegState = field(default_factory=USLegState)
    prc: PRCState = field(default_factory=PRCState)
    roc_exec: ROCExecState = field(default_factory=ROCExecState)
    roc_leg: ROCLegState = field(default_factory=ROCLegState)

    # P7 identity band; Day-8 audit: CLEAN.
    identity_band: tuple[float, float] = (0.62, 0.78)  # Sources #10/#11/#12; audit CLEAN.
    # P8 volatility envelope; stochastic shell only. Day-8 audit: CLEAN.
    lai_approval_sigma_pp: float = 7.4  # Source #11; audit CLEAN (population 7.29/sample 7.80 pp).
    # P9 reliability split. Day-8 audit: CLEAN willingness complement = 1 - 0.448.
    us_capability_pct: float = 0.453  # Source #11; audit CLEAN.
    us_willingness_pct: float = 0.552  # Source #11; audit CLEAN (1 - unwilling 0.448).
    # P9-bis PRC blame; provisional single-wave, audit CLEAN.
    prc_blame_pct: float = 0.448  # Source #11; audit CLEAN.
    # P10 three-layer defense spend; audit CLEAN after NT$110.0B unit correction.
    fy2026_baseline_ntd_b: float = 949.5  # Source #17; audit CLEAN.
    resilience_supplemental_ntd_b: float = 110.0  # Source #17; audit CLEAN (not NT$1.1T).
    special_unconditional_ntd_b: float = 300.0  # Source #19; audit CLEAN.
    special_loa_gated_ntd_b: float = 480.0  # Source #19; audit CLEAN.
    # P13 energy buffers; audit CLEAN.
    petroleum_buffer_days: float = 148.0  # Source #25; audit CLEAN.
    natural_gas_buffer_days_current: float = 10.7  # Source #25; audit CLEAN.
    natural_gas_buffer_days_2027: float = 14.0  # Source #24; audit CLEAN.
    coal_buffer_days: float = 45.7  # Source #25; audit CLEAN.
    # P14 cable resilience; audit CLEAN on Matsu 2.64km source fact.
    matsu_cut_km_off_dongyin: float = 2.64  # Source #22; audit CLEAN.


@dataclass(frozen=True)
class PruningResult:
    branch_id: str
    branch_description: str
    predicates_invoked: list[str]
    parameters_used: dict[str, Any]
    survives: bool
    justification_text: str


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_commit() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()


def prune_d7_1_chips_repeal(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.us_exec.can_unilaterally_repeal_statutory_substrate and state.us_leg.chips_clawback_years == 0
    return survives, {
        "predicate": "Day-7 S8 substrate-protection gate",
        "sources": ["publications/2026-05-07-en.md S8", "source-#19 CHIPS Act §103/§107"],
        "chips_clawback_years": state.us_leg.chips_clawback_years,
        "repeal_path": state.us_leg.statutory_substrate_repeal_path,
        "us_exec_unilateral_repeal_power": state.us_exec.can_unilaterally_repeal_statutory_substrate,
        "verdict": "blocked: 10-year statutory clawback requires substrate-level repeal, not executive discretion",
    }


def prune_d7_2_tera_repeal(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.us_exec.can_unilaterally_repeal_statutory_substrate and state.us_leg.tera_fmf_authorization_usd_b == 0
    return survives, {
        "predicate": "Day-7 S8 substrate-protection gate",
        "sources": ["publications/2026-05-07-en.md S8", "source-#6 Taiwan Enhanced Resilience Act"],
        "tera_fmf_authorization_usd_b": state.us_leg.tera_fmf_authorization_usd_b,
        "repeal_path": state.us_leg.statutory_substrate_repeal_path,
        "us_exec_unilateral_repeal_power": state.us_exec.can_unilaterally_repeal_statutory_substrate,
        "verdict": "blocked: TERA FMF authorization is legislative substrate, not a day-of-crisis executive switch",
    }


def prune_d7_3_ndaa_repeal(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.us_exec.can_unilaterally_repeal_statutory_substrate and state.us_leg.ndaa_taiwan_cycles == 0
    return survives, {
        "predicate": "Day-7 S8 substrate-protection gate",
        "sources": ["publications/2026-05-07-en.md S8", "sources-#6/#7/#8 FY2023-FY2025 NDAA density"],
        "ndaa_taiwan_cycles": state.us_leg.ndaa_taiwan_cycles,
        "repeal_path": state.us_leg.statutory_substrate_repeal_path,
        "us_exec_unilateral_repeal_power": state.us_exec.can_unilaterally_repeal_statutory_substrate,
        "verdict": "blocked: four-cycle NDAA substrate cannot be erased as one executive action",
    }


def prune_d7_4_nuclear_umbrella_addition(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.us_exec.taiwan_nuclear_umbrella_doctrinally_explicit
    return survives, {
        "predicates": ["Day-7 S8 nuclear non-commitment", "NPR-2022 negative-space predicate"],
        "sources": ["publications/2026-05-07-en.md S6/S8", "source-#23 NPR-2022"],
        "taiwan_nuclear_umbrella_doctrinally_explicit": state.us_exec.taiwan_nuclear_umbrella_doctrinally_explicit,
        "second_order_alliance_coverage": "geographic residual via Japan/ROK, not doctrinal Taiwan umbrella",
        "verdict": "blocked: no explicit Taiwan nuclear-umbrella commitment exists to add by deterministic executive fiat",
    }


def prune_d7_5_prc_substrate_negotiation_redirect(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.prc.attempts_statutory_substrate_negotiation
    return survives, {
        "predicate": "Day-7 S8 PRC counter-framing pressure pattern",
        "sources": ["publications/2026-05-07-en.md S7/S8", "sources-#29/#30 PRC TAO/MOFA briefings"],
        "taipei_track_lever": state.prc.taipei_track_lever,
        "washington_track_lever": state.prc.washington_track_lever,
        "attempts_statutory_substrate_negotiation": state.prc.attempts_statutory_substrate_negotiation,
        "verdict": "blocked: PRC messaging targets recognition/electorate pressure, not substrate-touching statutory bargaining",
    }


def prune_d8_1_energy_framing_redirect(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.prc.pitched_energy_reunification_inducement and not state.roc_exec.kmt_cross_strait_energy_framing_preempted
    return survives, {
        "predicates": ["P15 roc_executive_energy_doctrine_layer_active"],
        "sources": ["publications/2026-05-12-en.md S5/S6", "source-#23 Lai nuclear pivot + MOEA rejection"],
        "roc_doctrinal_layer_count": state.roc_exec.doctrinal_layer_count,
        "nuclear_restart_pivot_active_since": state.roc_exec.nuclear_restart_pivot_active_since,
        "energy_framing_preempted": state.roc_exec.kmt_cross_strait_energy_framing_preempted,
        "verdict": "blocked: Lai's energy-security substrate closes the PRC/KMT-friendly issue-space",
    }


def prune_d8_2_roc_exec_tranche2_unilateral_release(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = state.roc_exec.can_unilaterally_release_tranche2 or state.us_exec.fms_loa_round_2_issued
    return survives, {
        "predicates": ["P10 roc_defense_spend_structure", "P12 roc_special_budget_release_rate", "P12-bis us_exec_fms_loa_cadence"],
        "sources": ["publications/2026-05-12-en.md S4/S6", "sources-#15/#19", "Day-8 numerical audit §1/§4"],
        "special_total_ntd_b": state.roc_leg.defense_special_total_ntd_b,
        "tranche1_unconditional_ntd_b": state.roc_leg.tranche1_unconditional_ntd_b,
        "tranche2_loa_gated_ntd_b": state.roc_leg.tranche2_loa_gated_ntd_b,
        "us_fms_loa_round_2_issued": state.us_exec.fms_loa_round_2_issued,
        "verdict": "blocked at current snapshot: NT$480B Tranche 2 is gated by US-FMS-LOA-Round-2, not ROC_Exec discretion",
    }


def prune_d8_3_kmt_92_consensus_repudiation(state: DeterministicState) -> tuple[bool, dict[str, Any]]:
    survives = not state.roc_leg.kmt_doctrinal_alignment_active
    return survives, {
        "predicates": ["P4 kmt_doctrinal_alignment_with_ccp_92_consensus"],
        "sources": ["publications/2026-05-12-en.md S2/S6", "sources-#6/#7/#8"],
        "kmt_chair": state.roc_leg.kmt_chair,
        "joint_declarations_date": state.roc_leg.kmt_joint_declarations_date,
        "repudiation_path": state.roc_leg.kmt_repudiation_path,
        "doctrinal_alignment_active": state.roc_leg.kmt_doctrinal_alignment_active,
        "verdict": "blocked under current chair: repudiation requires new chair election or formal Joint-Declarations withdrawal",
    }


PRUNINGS: list[tuple[str, str, list[str], Callable[[DeterministicState], tuple[bool, dict[str, Any]]]]] = [
    ("D7.1", "US_Exec unilateral repeal of CHIPS §103/§107 10-year clawback", ["Day-7 substrate-protection gate"], prune_d7_1_chips_repeal),
    ("D7.2", "US_Exec unilateral repeal of TERA $10B FMF authorization", ["Day-7 substrate-protection gate"], prune_d7_2_tera_repeal),
    ("D7.3", "US_Exec unilateral repeal of NDAA Taiwan provisions across four cycles", ["Day-7 substrate-protection gate"], prune_d7_3_ndaa_repeal),
    ("D7.4", "US_Exec doctrinal addition of Taiwan nuclear umbrella under Trump-2", ["Day-7 nuclear non-commitment predicate"], prune_d7_4_nuclear_umbrella_addition),
    ("D7.5", "PRC redirect of Xi-Trump summit toward statutory-substrate negotiation", ["Day-7 PRC counter-framing pattern"], prune_d7_5_prc_substrate_negotiation_redirect),
    ("D8.1", "PRC cross-strait energy-framing redirect via peaceful-reunification inducement", ["P15"], prune_d8_1_energy_framing_redirect),
    ("D8.2", "ROC_Exec unilateral release of NT$480B Tranche 2 ahead of US-FMS-LOA-Round-2", ["P10", "P12", "P12-bis"], prune_d8_2_roc_exec_tranche2_unilateral_release),
    ("D8.3", "KMT-internal repudiation of 92-consensus alignment under current chair", ["P4"], prune_d8_3_kmt_92_consensus_repudiation),
]


def evaluate(state: DeterministicState) -> list[PruningResult]:
    results: list[PruningResult] = []
    for branch_id, description, predicates, evaluator in PRUNINGS:
        survives, details = evaluator(state)
        verdict = "survives" if survives else "pruned"
        results.append(
            PruningResult(
                branch_id=branch_id,
                branch_description=description,
                predicates_invoked=predicates,
                parameters_used=details,
                survives=survives,
                justification_text=f"{branch_id} {verdict}: {details['verdict']}",
            )
        )
    return results


def build_payload() -> dict[str, Any]:
    state = DeterministicState()
    results = evaluate(state)
    return {
        "metadata": {
            "run_label": "Day-9 first-cut deterministic 8-pruning evaluation on 5-player frame",
            "commit_at_run": git_commit(),
            "predicates_file": str(PREDICATES_PATH.relative_to(ROOT)),
            "predicates_file_sha256": sha256(PREDICATES_PATH),
            "parser_version": PARSER_VERSION,
            "audit_basis": {
                "file": "research/audit/numerical-audit-2026-05-14-nisaba.md",
                "audited_commit": AUDIT_BASIS_COMMIT,
            },
            "scope": "deterministic pruning only; stochastic extensions, Nash equilibrium, belief asymmetry, and repeated-game dynamics are out of scope",
            "player_frame": [state.us_exec.name, state.us_leg.name, state.prc.name, state.roc_exec.name, state.roc_leg.name],
        },
        "state": asdict(state),
        "prunings": [asdict(result) for result in results],
        "summary": {
            "total": len(results),
            "survives": sum(1 for result in results if result.survives),
            "pruned": sum(1 for result in results if not result.survives),
            "surviving_branch_ids": [result.branch_id for result in results if result.survives],
            "pruned_branch_ids": [result.branch_id for result in results if not result.survives],
        },
    }


def main() -> None:
    payload = build_payload()
    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(payload["summary"], indent=2, ensure_ascii=False))
    print(f"wrote {RESULT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
