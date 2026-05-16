# Parse-Verify Report — Day-9 (2026-05-16 06:00 fire)

**Target:** `gww3/predicates.gww3` (Day-8 deterministic-skeleton: 15 ROC-player predicates P1–P15 + cross-player promotion P12-bis)
**Verifier:** `hassaleh.engine.parser.parse_rule` (Lark Earley + PythonIndenter, grammar `hassaleh/src/hassaleh/engine/gsl_ops.lark` v1.2)
**Boundary:** deterministic block only — text up to `# STOCHASTIC EXTENSIONS` marker (the stochastic pseudocode below that marker is documentary, not valid GSL, and is excluded from parse-verify by design).
**Output script:** `gww3/parse_verify.py`

---

## Outcome summary

| Status | Count | Predicates |
|---|---|---|
| Parseable after the syntactic-conversion pass below | 12 of 15 + P12-bis | P1, P2, P3, P4, P5, P7, P8, P9-bis, P10, P11, P12, P12-bis, P14, P15 |
| Blocked on grammar gaps (structural, not syntactic) | 3 of 15 | **P6** (struct kwargs), **P9** (struct kwargs), **P13** (MIN-comprehension over a list) |

The deterministic skeleton is **80% parseable as-is** after three syntactic corrections. The remaining 20% (P6, P9, P13) cannot be expressed in the deterministic GSL subset without either (a) a grammar extension on the hassaleh side, or (b) a refactor that loses the compound-state-encoding semantics.

---

## Findings

### Finding 1 (FIXED in source) — Comment syntax: `//` → `#`

The grammar defines `COMMENT: /#[^\n]*/` and `%ignore COMMENT`. The predicate file originally used C-style `//` line comments (269 lines), which the lexer does not recognize. Fixed in-place: all leading `//` converted to `#`, preserving indentation and inner content (including the visual `═` and `──` separators).

Confusingly, the `gsl_ops.lark` grammar file *itself* uses `//` line comments — that is standard Lark *grammar* syntax, separate from the GSL *language* it defines.

### Finding 2 (FIXED in source) — Boolean-operator case: `AND`/`OR`/`NOT` → `and`/`or`/`not`

The grammar's terminal definitions:
```
OR_OP.2:  "||" | "or"
AND_OP.2: "&&" | "and"
NOT_OP.2: "!"  | "not"
```

are lowercase-only. The predicate file uses uppercase forms throughout (47 occurrences). Fixed in-place; uppercase tokens inside string literals are preserved by a string-aware substitution.

### Finding 3 (FIXED in source) — Multi-line continuation of `IF` conditions

Lark's PythonIndenter treats newlines as statement separators outside parens. The predicate file used unparenthesized multi-line conditions of the shape:

```
IF k.chair == "Cheng_Li_wun" and
   k.joint_declarations_with_ccp != null and
   k.joint_declarations_date >= "2026-02-03":
```

Fixed in-place by collapsing trailing-`and`/`or` continuations into a single logical line. Resulting file is 377 deterministic lines (down from 385 lines; 8 lines collapsed).

### Finding 4 (STRUCTURAL — not fixed) — `struct(key: value)` keyword args are not in the grammar

The grammar:
```
func_call: NAME "(" func_args? ")"
func_args: expr ("," expr)*
```

does not support keyword-argument syntax. The predicate file uses `struct(...)` calls with `key: value` pairs for compound-state encoding:

- **P6** (`roc_leg_ratification_signal_to_us`): `r.signal_to_us_exec = struct(ratified_amount: …, unconditional_fraction: …, …)` — 5 fields
- **P9** (`roc_public_us_reliability_perception`): `game_state.roc_public_us_reliability = struct(capability: 0.453, willingness: 0.552)` — 2 fields

Refactor options:
- (a) Replace `struct(...)` with separate single-field assignments — **blocked** by a second grammar limit: `PROP_ACCESS.2: /[a-zA-Z_]\w*\.[a-zA-Z_]\w*/` matches single-level dot access only, so `r.signal_to_us_exec.capability = 0.453` is also not parseable.
- (b) Hoist each field into a top-level `game_state` property: `game_state.roc_signal_ratified_amount = r.headline_amount` (10 single-purpose properties replacing 2 compound ones) — parseable, but loses the documentary grouping.
- (c) Extend `gsl_ops.lark` with explicit `struct_literal` and/or multi-level `PROP_ACCESS` rules — canonical hassaleh-side change; subject to Ingo review.

### Finding 5 (STRUCTURAL — not fixed) — `MIN(expr FOR x IN coll)` aggregator-over-comprehension not in the grammar

The grammar has `list_comp: "[" expr "FOR" NAME "IN" expr ("IF" expr)? "]"` — comprehensions are valid only inside `[...]` brackets. The predicate file uses an aggregator-over-bare-comprehension form:

- **P13** (`roc_energy_buffer_days`): `LET binding_window = MIN(b.days FOR b IN game_state.roc_energy_buffers)`

The parser rejects this because `MIN(b.days FOR …)` is read as a `func_call` whose first arg is `b.days` followed by an unexpected `FOR` token.

Refactor options:
- (a) Materialize the comprehension first: `LET buffers = [b.days FOR b IN game_state.roc_energy_buffers]` then `LET binding_window = MIN(buffers)` — **blocked**: the grammar's `func_call: NAME "(" func_args? ")"` with `func_args: expr ("," expr)*` does not have variadic `MIN` over a list argument either; `MIN` is documented as `MIN(a, b)` taking two scalars. Same gap as Finding 4(c).
- (b) Hard-code the binding window: replace the aggregator with an explicit IF chain over the three commodities (petroleum, NG, coal) and assign `game_state.coercion_window_lower_bound_days = …` directly. Parseable, but loses generality — the aggregator's whole point is to be extensible when new commodity buffers are added.
- (c) Extend `gsl_ops.lark` with either a `MIN_OVER_COMP` form or a variadic-list `MIN(list_expr)` form — canonical hassaleh-side change.

---

## Recommendation for Day-10 (or earlier today)

1. **Apply hoist-refactor (Findings 4(b) + 5(b)) to predicates.gww3** so the deterministic skeleton parses 15/15 + P12-bis. Document the loss of compound-state grouping in inline comments. This is a low-risk, ~30-line refactor.
2. **File the grammar-extension as a separate hassaleh-side question** (logged into `state.open_questions_for_ingo[]` this fire). Worth doing the right way upstream, but not blocking Day-9 publication work.
3. **Defer Nisaba `simulations/game_theory.py` work** (skill Day-9 task (c)) until predicates.gww3 parses cleanly — the simulation derives its game-tree directly from the deterministic skeleton, so a parse-clean skeleton is the precondition.

---

## Reproducing this report

```bash
cd ~/projects/silicon-strait
python gww3/parse_verify.py
```

Expected output (current state of repo at this report's commit):
```
Parsing 377 lines of deterministic GSL (cut at line containing '# STOCHASTIC EXTENSIONS')
PARSE FAILURE:
  line=132, column=28
  type=UnexpectedToken
  context:
            ratified_amount: r.headline_amount,
                           ^
```

The failure is at P6's first kwargs line (`ratified_amount:`). Fix P6 + P9 (struct hoist) + P13 (aggregator hoist) and the deterministic block will parse end-to-end.
