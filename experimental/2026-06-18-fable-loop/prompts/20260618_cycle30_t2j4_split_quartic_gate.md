# Cycle 30 Prompt: T2J4 Split-Quartic Gate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA Proximity Prize residue-line incidence loop.
Work only from the mounted source files and current-loop audit files. Do not
use the web.

Target:

```text
W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE
```

Goal: settle, refute, or sharply reduce the split-quartic gate left by Cycle
29. The top-symbol/invertibility calculation is not enough: at `t=2,j=4` the
affine system is square, so generic slopes have a unique affine preimage
`tau(z)`. The source-correct question is how often that preimage is the
elementary-symmetric tuple of a distinct 4-subset of `F_p`.

Read first:

```text
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md
current_loop_20260618/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RECOVERED_CLAUDE_JSONL.md
```

Ledger constraints:

- Keep `q_gen=p`, `q_line=p^2`, `q_chal`, `B=F_p`, and `F=F_{p^2}` separate.
- Stay in the restricted residue-line incidence setting:
  `D=F_p`, `n=p`, `t=sigma=2`, `j=4`, off `R0`, source-valid separated
  `E=X^2+cX+d`, and `c_b != 0`.
- Do not promote anything to corrected-reserve, MCA, list-decoding, CA,
  line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize status.

Exact task:

1. Starting from Cycle 29's square system

```text
M(z) tau = -C_0(z),     tau(z)=M(z)^(-1)(-C_0(z))
```

   isolate the exact algebraic condition that the monic quartic

```text
P_z(X)=X^4 - tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z)
```

   splits into four distinct roots in `F_p`.

2. Try to prove the slope count

```text
#{ z in F : P_z splits into four distinct roots in F_p } = O(p).
```

3. If the `O(p)` bound is false or implausible, construct the strongest
   source-valid growing-prime counterpacket you can: specify the family of
   `E,u,b,W` or the missing degrees of freedom, and whether it can realize
   `Theta(p^2)=Theta(q_line)` slopes.

4. If neither direction closes, give the smallest exact next wall. Good
   acceptable outputs include:
   - a low-degree curve versus totally-split locus theorem;
   - a reduction to a norm/discriminant/Frobenius condition;
   - an explicit finite checker spec for `p=5,7,11,13`;
   - a source-valid obstruction showing the split locus can have density;
   - a proof that only a lower-dimensional subfamily of split quartics is hit.

5. Keep the noninvertibility curve `det_B M(z)=0` separate. It has only
   `O(p)` possible slopes and cannot by itself prove or refute the generic
   split-quartic gate.

Output format:

- Start with exactly one of:
  `PROOF`, `BANKABLE_LEMMA`, `ROUTE_CUT`, `EXACT_NEW_WALL`,
  `COUNTERPACKET`, or `AUDIT`.
- Then give field ledger, proof/counterpacket/reduction, dependency list,
  hidden assumptions, rejected overclaims, and next exact wall.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
