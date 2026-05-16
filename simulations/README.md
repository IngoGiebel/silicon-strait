# Simulations — Silicon Strait

Python game-theoretic models of cross-strait dynamics. Nisaba 🌾's territory.

## Roadmap

- **Day-9:** First cut delivered — deterministic 8-pruning evaluation on the promoted 5-player frame; see `game_theory_2026-05-16.py` and `results/day9-five-player-pruning-eval-2026-05-16.json`. This is **not** the Day-14 Nash equilibrium milestone.

- **Day ~14:** First formal game tree. Players: PRC, ROC, USA, JPN, ASEAN, EU. Action sets calibrated from the qualitative analysis days 1–13. Static (one-shot) Nash equilibrium analysis.

- **Day ~30:** Iterated game with Belief-Subgraph. Each player acts on a *belief* about the others' types and likely moves, not on ground truth. Belief asymmetries seeded from real-world signals (PRC white papers, U.S. National Defense Strategy, Taiwanese MND assessments).

- **Day ~60:** Sensitivity analysis on the chip-supply-chain payoff coefficient. How does the equilibrium shift as the global compute-economy's dependence on Taiwan changes (e.g. as TSMC's Arizona / Japan / Germany fabs come online)?

- **Day ~90:** Preprint-grade write-up. Target: Zenodo or arXiv (cs.GT or econ.TH).

## Engineering principles

- **Reproducibility.** Every simulation result reported in a publication is reproducible from a single `python sim_<name>.py` invocation, with inputs documented and outputs deterministic for a given random seed.
- **No hidden parameters.** Every numerical input traces to a cited source in `sources/bibliography.md` or to a clearly labeled "exploratory assumption" with a sensitivity range.
- **Audit-first commits.** Nisaba reviews every simulation before commit. No untested model files in the publication path.

## License

MIT. The publications under `publications/` are CC BY 4.0; the simulations are MIT so they can be re-used in other formal-modeling work without copyleft entanglement.
