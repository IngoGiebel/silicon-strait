"""Day-9 parse-verify: hand the deterministic block of predicates.gww3 to
hassaleh.engine.parser and report tree summary or first parse error.

Cuts the file at line containing "STOCHASTIC EXTENSIONS" (the stochastic
pseudocode below that marker is documentary, not valid GSL).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "hassaleh" / "src"))

from hassaleh.engine.parser import parse_rule
from lark.exceptions import UnexpectedInput


def main() -> int:
    src_path = Path(__file__).parent / "predicates.gww3"
    full = src_path.read_text()

    marker = "# STOCHASTIC EXTENSIONS"
    idx = full.find(marker)
    if idx < 0:
        print("ERROR: STOCHASTIC EXTENSIONS marker not found; deterministic boundary undefined")
        return 2

    deterministic = full[:idx]
    line_count = deterministic.count("\n") + 1
    print(f"Parsing {line_count} lines of deterministic GSL (cut at line containing {marker!r})")

    try:
        tree = parse_rule(deterministic)
    except UnexpectedInput as e:
        print("PARSE FAILURE:")
        print(f"  line={e.line}, column={e.column}")
        print(f"  type={type(e).__name__}")
        print(f"  context:\n{e.get_context(deterministic, 200)}")
        return 1

    statement_count = sum(1 for _ in tree.children if getattr(_, "data", None))
    matches = [c for c in tree.children if getattr(c, "data", None) == "match_block"]
    every = [c for c in tree.children if getattr(c, "data", None) == "every_block"]
    comments = [c for c in tree.children if getattr(c, "data", None) == "comment_line"]

    print(f"PARSE OK")
    print(f"  top-level statements: {statement_count}")
    print(f"  MATCH blocks: {len(matches)}")
    print(f"  EVERY blocks: {len(every)}")
    print(f"  comment lines: {len(comments)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
