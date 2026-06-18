# Cycle 34 Prompt: A2_B Dominance And Resolvent Certificate

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
W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT
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
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`

Use the `.tex` files only if you need to check a definition or hypothesis.

## Banked Before This Prompt

Cycle 32 corrected the model: the `t=2,j=4` quartic family is a
two-dimensional `B`-surface with coordinates

```text
z = z_0 + alpha z_1,     z_0,z_1 in B.
```

It is not a one-variable `B(z)` or `F(z)` problem.

Cycle 33 banks the singular boundary only:

```text
Delta(z_0,z_1)=det_B M(z)
```

has total degree at most four and is not identically zero under the Cycle 29
top-symbol hypotheses, so `Delta=0` contributes at most `4p=O(p)` slopes.

The off-curve problem remains open.

## The Task

Attack the off-curve wall from the strongest angle you see.

1. Decide whether the rational map

   ```text
   tau(z_0,z_1)=M(z)^(-1)(-C_0(z))
   ```

   has generic `B`-Jacobian rank two. If you can prove rank two, state the
   exact argument and dependencies. If you can prove rank at most one, that is
   a route cut/counterpacket to the positive-density route. If you cannot
   decide it, isolate the smallest symbolic determinant/minor that decides it.

2. For the quartic

   ```text
   L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
   ```

   analyze the cubic resolvent

   ```text
   R(y)=y^3 - tau_2 y^2
          + (tau_1 tau_3 - 4 tau_4)y
          - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2)
   ```

   and the square class of `disc_X L_tau` after substituting
   `tau=tau(z_0,z_1)`. Can you prove geometric transitivity, full `S_4`, a
   smaller transitive group, or a reducibility obstruction?

3. Decide what constant-field-extension test is actually needed over
   `B(z_0,z_1)` and whether the current data already rules it out.

4. If you cannot prove the monodromy/resolvent statement, give the sharpest
   next exact wall, with a finite symbolic computation or local checker spec
   precise enough that Codex can implement it.

Use these labels literally: `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`,
`ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, `EXPERIMENTAL`.

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
