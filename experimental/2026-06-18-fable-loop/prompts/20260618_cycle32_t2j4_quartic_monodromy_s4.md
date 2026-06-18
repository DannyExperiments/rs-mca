# Cycle 32 Prompt: T2J4 Quartic Monodromy Audit

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA Proximity Prize residue-line incidence loop.
Work only from the mounted source files and current-loop audit files. Do not
use the web.

Target:

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```

Goal: decide the exact algebraic invariant behind the `t=2,j=4` split locus.
Cycle 31 claims the right object is quartic monodromy rather than hidden
`O(p)` collapse, but Codex audits that as an unproved route suggestion, not a
counterpacket.

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md
current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle31_t2_j4_scaling_spotcheck_certificate.md
current_loop_20260618/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RECOVERED_CLAUDE_JSONL.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Stay in the restricted residue-line incidence setting:
  `D=F_p`, `n=p`, `t=sigma=2`, `j=4`, off `R0`, source-valid separated
  `E=X^2+cX+d`, and `c_b != 0` when using that branch.
- Do not promote anything to corrected-reserve, MCA, list-decoding, CA,
  line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize status.

Exact task:

Cycle 29 gives the rational preimage

```text
tau(z)=M(z)^(-1)(-C_0(z)) in B^4
```

away from the square determinant locus. Cycle 30 gives the split-gate
formulation for the quartic

```text
L_{tau(z)} = X^4 - tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z).
```

Cycle 31 proposes that the correct next invariant is quartic monodromy:
compute `disc_X L_{tau(z)}` and a resolvent cubic, certify the transitive
subgroup of `S_4`, and then decide whether the fully split distinct locus has
positive density or collapses.

Audit this claim source-groundedly:

1. Decide whether the family should be treated over `B(z_0,z_1)`, over
   `F(z)`, or as a two-dimensional `B`-parameter family with `z in F_{p^2}`.
   This base-field issue is not cosmetic.
2. Derive the exact discriminant/resolvent objects needed from the Cycle 29
   square-system columns, or state precisely which mounted formula is missing.
3. Prove, refute, or reduce the claim that the geometric monodromy is `S_4`
   or another transitive subgroup with positive split density.
4. If monodromy cannot be certified, give the smallest explicit checker or
   symbolic certificate that would decide it.
5. If an `O(p)` collapse is still possible, identify the exact invariant that
   forces it; do not rely on small-prime scans.

Output format:

- Start with exactly one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give field ledger, proof/counterpacket/reduction, dependency list,
  hidden assumptions, rejected overclaims, and next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

