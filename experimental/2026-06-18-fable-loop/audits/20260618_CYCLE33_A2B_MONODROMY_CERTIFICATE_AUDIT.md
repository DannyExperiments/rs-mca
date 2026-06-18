# Cycle 33 A2_B Monodromy Certificate Audit

Status: BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is audited conservatively.

Source artifacts:

- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RAW.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RUN_RESULT.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Branch: off `R0`, source-valid separated quadratic `E=X^2+cX+d`
  nonzero on `F_p`, with `c_b != 0` on the branch using the Cycle 28/29
  top-symbol nonvanishing.

This is only a residue-line / bad-slope incidence calculation. It is not a
corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Restricted Lemma

Cycle 33 banks a narrow singular-bound lemma:

```text
L-T2J4-A2B-SINGULAR-OP.
In the restricted t=2, j=4 A^2_B model, under the Cycle 29 top-symbol
nonzero hypotheses, the determinant locus Delta(z_0,z_1)=0 contributes
at most 4p split slopes.
```

Proof skeleton:

1. In the Cycle 32 `A^2_B` model, write `z=z_0+alpha z_1` with
   `z_0,z_1 in B`.
2. Multiplication by `z` on `A=F[X]/E` is `B`-linear:

   ```text
   m_z = z_0 I_4 + z_1 A_alpha.
   ```

3. Each Cycle 29 column `C_i(z)=P_i-m_z(R_i)` is affine-linear in
   `(z_0,z_1)`. Therefore every entry of the square matrix `M(z)` has total
   degree at most one, and

   ```text
   Delta(z_0,z_1)=det_B M(z)
   ```

   has total degree at most four.
4. Cycle 29's top-symbol calculation gives

   ```text
   TopSym(Delta) = -N(kappa) * N(z)^2 * Q_4.
   ```

   On the source-valid branch, `N(kappa) != 0` and `Q_4 != 0`; since the norm
   form `N(z)` is nonzero as a polynomial, `Delta` is not the zero polynomial.
5. A nonzero two-variable polynomial over `F_p` of total degree at most four
   has at most `4p` zeros in `F_p^2` by the elementary Schwartz-Zippel /
   line-count bound.
6. Any split slope arising from the singular determinant locus is represented
   by a point of `Delta=0`; hence the singular contribution is at most `4p`.

This is a conditional local proof, not a global theorem: it depends on the
source-valid branch hypotheses and on the previously banked Cycle 29/28
top-symbol nonvanishing.

## Audit Judgment

Bank:

1. The singular determinant curve cannot by itself create a
   `Theta(q_line)=Theta(p^2)` split-slope family in the restricted `t=2,j=4`
   branch.
2. Boundary mismatches in the Cycle 32 checker are consistent with an `O(p)`
   singular locus and should not be read as off-curve monodromy evidence.
3. The off-curve positive-density question is now isolated from the singular
   curve.

Do not bank:

- No proof that `C2=Theta(q_line)`.
- No source-valid counterpacket.
- No proof of `G_geom=S_4`.
- No proof that arithmetic monodromy equals geometric monodromy.
- No proof that the off-curve split locus has positive density.
- No proof of the opposite `O(p)` collapse.

## Exact Monodromy Reduction

For

```text
L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4,
```

with cubic resolvent

```text
R(y)=y^3 - tau_2 y^2
       + (tau_1 tau_3 - 4 tau_4)y
       - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2),
```

Cycle 33 says the useful certificate is not necessarily full `S_4`. A smaller
transitive subgroup of `S_4` would still give positive split density provided
the arithmetic and geometric groups match and the identity Frobenius class is
realized.

Thus the off-curve wall splits into:

1. generic `B`-Jacobian rank of the rational map
   `tau:A^2_B -> A^4_B`;
2. factorization of the resolvent cubic and the square class of
   `disc_X L_tau` over `B(z_0,z_1)` and over `\bar B(z_0,z_1)`;
3. constant-field-extension test `G_arith=G_geom`.

## Next Exact Wall

```text
W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT
```

Prove or refute a symbolic certificate for the off-curve family:

1. `tau(z_0,z_1)=M(z)^(-1)(-C_0(z))` has generic `B`-Jacobian rank two.
   Rank two keeps the image surface-sized; rank at most one would give an
   `O(p)` collapse route.
2. The quartic family is geometrically irreducible/transitive, or the exact
   smaller transitive subgroup is identified.
3. The arithmetic and geometric monodromy groups agree, or a constant-field
   obstruction is exhibited.

## Rejected Overclaims

- Do not cite Cycle 33 as a proof of a `Theta(q_line)` counterpacket.
- Do not cite Cycle 33 as a proof of `S_4` or positive split density.
- Do not merge `q_gen=p` and `q_line=p^2`.
- Do not promote this local `t=2,j=4` audit into corrected-reserve, MCA, CA,
  list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.
