# Cycle 42 External Homerun Packet Manifest

Purpose: give a different model a focused, source-grounded packet for a
homerun attempt after Cycle 41.

## Main Prompt

- `PROMPT.md` - copy-ready prompt for the external model.

## Route State

- `ACTIVE_WALLS.md` - current live walls and ordering.
- `BANKED_LEMMAS.md` - banked lemmas and what they do not prove.
- `CUTS_AND_FALSE_ROUTES.md` - known route cuts and false upgrades.
- `ROUTE_BOARD_CURRENT.md` - route-board narrative.
- `README_FOR_FABLE.md` - project orientation.

## Source / Reviewer Instructions

- `agents.md` - repository instructions for keeping material under
  `experimental/`, tagging claim status, and preserving raw outputs as
  provenance.
- `readme.md` - upstream repository orientation.
- `tex/*.tex` - source papers/notes for exact definitions and hypotheses.

## Key Audits

- `audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md` - determinant
  degree and `Delta=0` singular bound context.
- `audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md` - repaired finite-place
  S4 checker setup.
- `audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md` - locator-collapse proof:
  `ell=alpha` or `ell=-2X`.
- `audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md` - finite-place geometric
  S4 certificates for both subcases.
- `audits/20260618_CYCLE41_CHAR0DELTA_GOODRED_AUDIT.md` - current A/B
  asymmetry and good-reduction wall.

## Raw / Provenance

- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RECOVERED_FINAL_ASSISTANT.md` -
  recovered coherent Cycle 41 answer.
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RESPONSE_STREAM_MALFORMED.md` -
  malformed stream capture preserved as provenance only.
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RUN_RESULT.json` - run metadata.

## Local Checkers

- `local_checks/20260618_cycle39_locator_collapse_verify_result.json` -
  locator-collapse sanity check.
- `local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py` -
  Cycle 40 finite-place checker.
- `local_checks/20260618_cycle40_subcase_goodred_checker_result.json` -
  `all_pass=true` finite-place S4 result.
- `local_checks/20260618_cycle41_char0delta_checker_from_response.py` -
  original Cycle 41 checker, preserved unmodified.
- `local_checks/20260618_cycle41_char0delta_checker_result.json` - original
  Cycle 41 checker failure.
- `local_checks/20260618_cycle41_char0delta_checker_patched.py` - minimal
  Codex-patched checker.
- `local_checks/20260618_cycle41_char0delta_checker_patched_result.json` -
  patched result: B passes, A fails at first target prime.
- `local_checks/20260618_cycle41_char0delta_goodprime_scan_result.json` -
  good-prime scan: A fails at `7,23,43,47,67,83`; B passes at `19,31,59`.

## Expected External-Model Focus

The central question is not whether finite-place S4 exists; Cycle 40 says it
does for both subcases. The central question is whether the A-side
good-reduction failure in Cycle 41 is real, line-dependent, or a checker/model
artifact.

The packet is intentionally focused: it does not include every raw answer from
Cycles 1-40. Use the included audits and checkers first; only consult source
`.tex` files for definitions/hypotheses.
