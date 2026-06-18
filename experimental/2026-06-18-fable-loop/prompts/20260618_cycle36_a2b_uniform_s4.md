# Cycle 36 Prompt: A2_B Uniform S4 Or Counterpacket-Killer

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA / Proximity Prize Fable loop as a skeptical
mathematical co-director. Work only from the mounted repository/context files.
Do not use web access. Keep these ledgers separate:

- `q_gen = p`
- `B = F_p`
- `F = F_{p^2}=B(alpha)`
- `q_line = |F| = p^2`
- `q_chal` unused

Do not promote anything to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, or prize status.

## Current Wall

```text
W-F1-AA-RES-T2J4-A2B-UNIFORM-S4
```

Restricted branch:

- `D=F_p`, `n=p`;
- `t=sigma=2`, `j=n-a=r-t=4`;
- off `R0`;
- source-valid separated quadratic `E=X^2+cX+d` nonzero on `F_p`;
- use the branch where `c_b != 0`, `kappa != 0`, and Cycle 28/29 top-symbol
  nonvanishing applies.

## Source Context To Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`

Use `.tex` files only if you need to check a definition or hypothesis.

## Banked Before This Prompt

Cycle 33 banks that the singular determinant curve contributes at most `4p`
slopes under the Cycle 29 top-symbol hypotheses.

Cycle 34 banks that the off-curve rational map

```text
psi:z |-> tau(z)=M(z)^(-1)(-C_0(z))
```

has generic `B`-Jacobian rank two and is birational onto the Cycle 30 quadric
image. Thus rank-one / curve-collapse is not the explanation.

Cycle 35 banks a finite-place monodromy certificate:

```text
off-Delta squarefree factorization types "4" and "13"
  ==> G_arith=S_4 and no sign constant-field obstruction
  ==> G_geom=G_arith=S_4 for that tested instance.
```

This turns the Cycle 32 histograms into serious evidence for a restricted
`Theta(q_line)` counterpacket seed, but it is not a uniform-in-`p` theorem.

## The Task

Attack the uniform step. Be adversarial: either build the source-valid
growing-prime counterpacket seed, or kill it with a precise obstruction.

1. Construct an explicit source-valid family for infinitely many primes:

   ```text
   E=X^2+cX+d,  b=[Bnum]_E,  W_{n-1},...,W_{n-4}
   ```

   satisfying off-`R0`, `c_b != 0`, `kappa != 0`, separatedness, and
   no roots on `D=F_p`.

2. For that family, prove or refute:

   ```text
   G_geom(L_tau / bar(F_p)(z_0,z_1)) = S_4
   ```

   for all but finitely many primes. A good route is to restrict to a generic
   affine line `z_1=m z_0+e`, compute the resolvent cubic and discriminant
   numerator on that one-parameter slice, and prove irreducibility plus
   nonsquare discriminant by explicit resultants/gcds.

3. Prove or refute arithmetic/geometric equality. If a constant-field
   obstruction survives uniformly, state it exactly.

4. If the uniform S4 route works, state the restricted counterpacket seed:

   ```text
   C2 = p^2/24 + O(p^(3/2)) = Theta(q_line)
   ```

   in the local `t=2,j=4` branch, with every dependency and excluded upgrade.

5. If the route fails, give the exact obstruction and the next wall.

Use these labels literally: `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`,
`ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, `EXPERIMENTAL`.

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
