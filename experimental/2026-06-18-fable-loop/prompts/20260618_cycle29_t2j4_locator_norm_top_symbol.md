# Cycle 29 Prompt: T2J4 Locator-Norm Top Symbol

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA Proximity Prize residue-line incidence loop.
Work only from the mounted source files and current-loop audit files. Do not
use the web.

Target:

```text
W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL
```

Goal: extend or refute the Cycle 28 mechanism one step beyond the closed
`t=2,j=3` window.

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Stay in the residue-line incidence setting, not list/CA/MCA/protocol.
- Work over `D=F_p`, `n=p`, `t=sigma=2`, now `j=4`, off `R0`,
  source-valid separated `E=X^2+cX+d`, and `c_b != 0` or state exactly why
  the `c_b` hypothesis changes.
- Do not promote anything to corrected-reserve, MCA, protocol, SNARK, or prize
  status.

Exact task:

1. Reconstruct the `t=2,j=4` analogue of the quotient/line-incidence setup.
   Identify the correct elementary co-support parameters and the analogue of
   the affine consistency system.
2. Define the slope consistency determinant `Q` or explain what replaces it if
   the number of affine parameters changes.
3. Extract the highest-degree-in-`z` coefficient/top symbol.
4. Decide whether the top symbol factors as a nonzero `B`-scalar times a power
   of the locator norm

```text
N(ell)=prod_{a in F_p}E(a).
```

5. If yes, state the exact exponent, hypotheses, and resulting `O(p)` slope
   bound for `j=4`.
6. If no, give the smallest exact wall or source-valid failure mode:
   missing determinant, extra rank-drop branch, non-locator factor, possible
   source-valid zero of the top symbol, or finite checker needed.

Output format:

- Start with exactly one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give field ledger, derivation/refutation, dependency list, hidden
  assumptions, rejected overclaims, and next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
