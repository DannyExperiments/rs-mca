I have enough to give a rigorous verdict. Let me confirm the one numerical sanity check that backs my main lemma against the recorded `singular_z` counts before writing.

The recorded singular counts (`singular_z`: p=7→11, 11→11, 13→13, 17→20, 19→26, 23→18, 29→33) are all far below `4p` (28, 44, 52, 68, 76, 92, 116), which is exactly what my degree bound predicts. That is the one empirical fact my proof needs to be consistent with, and it is. No code run is required; the deliverable is a proof plus a reduction.

---

BANKABLE_LEMMA

I can bank one unconditional restricted lemma (the singular-curve `O(p)` bound), give an exact reduction of the positive-density question, and pin the obstruction sharply. I cannot bank positive density, `S_4`, or `Theta(q_line)`: the histogram is not upgradable to a certificate.

## Field ledger

- `q_gen = p`. `B = F_p`. `F = F_{p^2} = B(alpha)`. `q_line = |F| = p^2`. `q_chal` unused.
- `D = F_p`, `n = p`; restricted regime `t = sigma = 2`, `j = n-a = r-t = 4`; off `R0`; source-valid separated `E = X^2 + cX + d` nonzero on `F_p`, `c_b != 0` on that branch.
- `z = z_0 + alpha z_1`, `(z_0,z_1) in A^2_B`. The parameter space is the affine `B`-surface `A^2_B`, counted at its `F_p`-points; this is **not** a one-variable `B(z)` or `F(z)` Chebotarev count.
- Scope: residue-line / bad-slope incidence only. Not corrected-reserve, MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, SNARK, or Proximity Prize.

## Task 1 verdict: not upgradable to a certificate

The Cycle 32 checker is a numeric histogram at finitely many small primes. A finite histogram can certify **neither** a monodromy group **nor** the absence of a constant-field extension, and both are needed for any density statement. So the checker stays EXPERIMENTAL. What the Cycle 29/30 equations *do* support rigorously is (i) Lemma A below and (ii) the reduction. The checker is also validated as an implementation: off `Delta=0` it reproduces the direct support enumeration (`match=True` whenever `singular_split_C2=0`), so the residual `singular_split_C2 in {1,2}` rows are boundary artifacts, not checker errors.

## Task 2: PROOF that `Delta = 0` contributes only `O(p)` split slopes

This is the one fully provable item.

1. By the Cycle 32 base model, the columns `C_i(z) = P_i - m_z(R_i)` are affine-linear in `(z_0,z_1)` because `m_z = z_0 I_4 + z_1 A_alpha` is `B`-linear. Hence each entry of `M(z)` has total degree `<= 1` in `(z_0,z_1)`, and
   `Delta(z_0,z_1) = det_B M(z)` has total degree `<= 4`.
2. `Delta` is **not** the zero polynomial: Cycle 29's top-symbol computation gives
   `TopSym(Delta) = -N(kappa) * N(z)^2 * Q_4`,
   with `N(kappa) != 0` and `Q_4 != 0` source-valid. Since `N(z)^2` is the square of the (anisotropic) norm form of `F/B`, the degree-4 part of `Delta` is a nonzero binary quartic; thus `deg Delta = 4` exactly and `Delta !≡ 0`.
3. Schwartz–Zippel over `F_p`: a nonzero polynomial of total degree `d` in two variables has at most `d·p` zeros in `F_p^2`. Therefore
   `#{(z_0,z_1) in F_p^2 : Delta = 0} <= 4p`.
4. Every split slope arising from the singular locus is in particular a point of `{Delta = 0}`. Hence the singular curve contributes at most `4p = O(p)` split slopes — **independent of the monodromy group and unconditional given source validity.**

Consistency: recorded `singular_z` is between `~p` and `~1.4p`, and `singular_split_C2 in {0,1,2}`, both comfortably under `4p`. (The leading form `N(z)^2` vanishes over `F_p` only at the origin, which is why the curve carries `~p`, not `~4p`, points.)

This bound is bankable as the restricted lemma:
`L-T2J4-A2B-SINGULAR-OP`: the `Delta=0` locus contributes `<= 4p` split slopes.

## Task 3: the exact monodromy theorem needed

It is **not** any single one of the offered options; it is a conjunction, split into a geometric part (controls which group) and an arithmetic part (controls whether the density constant is realized).

For `L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` with cubic resolvent
`R(y) = y^3 - tau_2 y^2 + (tau_1 tau_3 - 4 tau_4) y - (tau_1^2 tau_4 - 4 tau_2 tau_4 + tau_3^2)`:

- Geometric `G_geom = S_4` over `\bar B(z_0,z_1)` ⟺ **both** `disc_X L_tau` is a nonsquare in `\bar F_p(z_0,z_1)` **and** `R(y)` is irreducible over `\bar F_p(z_0,z_1)`. (Resolvent irreducible ⟹ `3 | |G|` ⟹ `G in {A_4, S_4}`; disc nonsquare ⟹ `G ⊄ A_4`; together ⟹ `S_4`.)
- The density constant is governed by the **arithmetic** group `G_arith` over `B(z_0,z_1) = F_p(z_0,z_1)`, with `G_geom ⊴ G_arith`. The extra hypothesis needed is `G_arith = G_geom`, i.e. **no constant-field extension**: the field of constants of the `S_4`-splitting field is exactly `F_p`. Equivalently, the discriminant double cover and the resolvent cubic cover are each geometrically irreducible.

Only with both parts does function-field Chebotarev / Lang–Weil on the surface give
`#{split (z_0,z_1) in A^2(F_p)} = p^2/|G| + O(p^{3/2})`,
which for `S_4` is `p^2/24 + O(p^{3/2})`.

## Task 4: a smaller transitive group suffices (and is preferable for a seed)

For a `Theta(q_line) = Theta(p^2)` counterpacket **seed** one needs only positive density of completely-split fibers, i.e. density `1/|G_geom| > 0`, which holds for **any** transitive `G ⊆ S_4` provided `G_arith = G_geom`. So `S_4` is not required. The minimal transitive subgroups are `V_4` and `C_4` (both order 4), giving the **largest** split density `1/4`; `D_4 → 1/8`, `A_4 → 1/12`, `S_4 → 1/24`. Hence the counterpacket only needs: (a) `L_tau` geometrically irreducible over `\bar F_p(z_0,z_1)` (transitivity), and (b) no constant-field extension. This is strictly weaker than the `S_4` target carried since Cycle 31, and it is the right thing to chase next.

## Task 5: the sharpest obstruction

Not a checker error (the checker matches direct enumeration off `Delta=0`), and not primarily a constant-field extension (that only rescales the constant, it does not by itself kill positivity). The sharpest live obstruction is **failure of generic dominance / dimension collapse of `z -> tau(z)`**:

`tau(z) = M(z)^{-1}(-C_0(z))` is a rational map `A^2_B --> A^4`. If its image is genuinely 2-dimensional (generic `B`-Jacobian rank 2) with transitive monodromy, the split count is `Theta(p^2)`. If instead the image collapses to a curve (rank `<= 1`), the split count is governed by a 1-dimensional Lang–Weil count and is `O(p)` — exactly the "hidden collapse" the Cycle 30 random-`T` scan flirted with. The Cycle 32 full-`z` enumeration argues **against** collapse: `hist_C2/p^2` sits at `0.018–0.039`, stable/rising toward `1/24`, rather than decaying to `0`. But "stable ratio at seven small primes" is evidence, not a proof of rank 2.

So the obstruction is concretely: the generic Jacobian rank of `z -> tau` and the geometric Galois data of `R(y)` and `disc_X L_tau` over `F_p(z_0,z_1)` are **uncomputed**. These are finite *symbolic* computations valid for all large `p` — which is what a certificate would require, and which a small-prime histogram structurally cannot supply.

## Dependency list

- Cycle 32 base-field model: `A^2_B`, `m_z = z_0 I_4 + z_1 A_alpha`, affine-linear columns, `deg Delta <= 4`.
- Cycle 29 top symbol: `TopSym(Delta) = -N(kappa) N(z)^2 Q_4`, source-valid nonzero ⟹ `Delta !≡ 0`.
- Cycle 30: explicit `Phi(tau)` two-quadric reduction and the split-gate definition.
- Cycle 24/28: locator-norm nonvanishing and `Q_4` source validity.
- Cycle 11 utilities underlying the Cycle 32 checker (validated off `Delta=0`).
- Standard: Schwartz–Zippel over `F_p`; quartic resolvent-cubic Galois criterion; function-field Chebotarev / Lang–Weil with `O(q^{dim-1/2})` error.

## Hidden assumptions

- Source validity (`kappa != 0`, `c_b != 0`, `E` separated and nonzero on `F_p`, off `R0`) holds, so `TopSym(Delta) != 0` and `deg Delta = 4`.
- `p` large enough that the Cycle 29 quotient recursion is unaffected by the `-X` tail of `X^p - X`.
- The `O(p)` lemma counts *points of the curve*; it bounds split slopes from the singular locus regardless of whether `tau` is defined there, so it needs no monodromy input.
- Lang–Weil/Chebotarev would additionally require the bad locus (singular curve + branch/discriminant locus) to be `O(p)`, which Lemma A supplies for the `Delta=0` part.

## Rejected overclaims

- No proof of `G_geom = S_4`, of `G_arith = G_geom`, or of any Chebotarev density constant.
- No proof of `C2 = Theta(q_line)`; no source-valid counterpacket.
- No proof of the opposite `O(p)` collapse either — the full-`z` data leans against it but does not settle it.
- The `O(p)` singular bound is **only** for the `Delta=0` locus; it says nothing about the off-curve count.
- No `q_gen`/`q_line` merge; no promotion to corrected-reserve, MCA, CA, list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.

## Next exact wall

```
W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT
```

A symbolic (all-large-`p`), not numeric, certificate of three items over `F_p(z_0,z_1)`:
1. Generic `B`-Jacobian rank of `z -> tau(z)` (rank 2 ⟹ 2-dimensional image, ruling out the `O(p)` collapse; rank `<= 1` ⟹ collapse and `C2 = O(p)`).
2. Factorization of the resolvent cubic `R(y)` and the square class of `disc_X L_tau` over both `F_p(z_0,z_1)` and `\bar F_p(z_0,z_1)` — giving `G_arith`, `G_geom`, and the transitivity needed for a seed.
3. The constant-field-extension test `G_arith = G_geom`.

Route to a full solve: yes, conditionally. Item 1 alone is decisive — rank 2 plus transitivity (item 2, weaker than `S_4`) plus no-constant-extension (item 3) yields a `Theta(p^2)` counterpacket seed via Lang–Weil, with Lemma A already disposing of the singular boundary. The next lemma to attempt is exactly the generic-rank-2 / dominance computation for `z -> tau`.
