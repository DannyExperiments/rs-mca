# Cycle 47 Domain-Uniform Bessel Moment Audit

Status: PROOF_CANDIDATE / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Raw outputs:

- `raw/cycle47_domain_uniform_bessel_5p5/01_OFFICIAL_DOMAIN_ADMISSIBILITY_AUDITOR.txt`
- `raw/cycle47_domain_uniform_bessel_5p5/02_BESSEL_MOMENT_PROOF_BUILDER.txt`
- `raw/cycle47_domain_uniform_bessel_5p5/03_SMOOTH_DOMAIN_MCA_TRANSFER_BUILDER.txt`
- `raw/cycle47_domain_uniform_bessel_5p5/04_OBSTRUCTION_COUNTERPACKET_HUNTER.txt`
- `raw/cycle47_domain_uniform_bessel_5p5/05_INTERLEAVED_LIST_BRIDGE_AUDITOR.txt`
- `raw/cycle47_domain_uniform_bessel_5p5/06_REFEREE_THEOREM_FORMALIZER.txt`

## Verdict

The six fresh 5.5-style external answers strongly converge: the target

```text
W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT
```

is closed at the algebraic/source-local lower-branch level. Five answers call
it `PROOF`; the admissibility-auditor answer calls it `AUDIT -- algebraic
PROOF; literal-official promotion admissible under one extra source check`.

This is the strongest Cycle 45-47 result so far for the scalar MCA side. It
promotes the Cycle 45 restricted additive random-anchor theorem to a
domain-uniform smooth-domain theorem candidate. It is not yet a full prize
solve, because it proves the failure/lower branch, not the matching safe-side
upper threshold, and the survey's literal MCA Definition 4.3 should still be
matched line-by-line against the support-wise MCA source definition.

## Bankable Lemma: Domain-Free Pair Rank

Let `F=F_Q`, let `D subset F` be any set of `n` distinct points, let
`1 <= t <= n-k`, set `a=k+t` and `j=n-a`, and let `E in F[X]` have degree `t`
with no roots on `D`. For an `a`-set `S`, let

```text
R_S(w) = [interp_S(w)]_E in A=F[X]/(E).
```

For two `a`-sets `S,S'`, put `d=|S\S'|=|S'\S|` and `C=S cap S'`. Then

```text
Im(R_S,R_S') = {(u,v) in A^2 : u-v in [L_C F[X]_<d]_E}
```

and, since `[L_C]_E` is a unit,

```text
rank_F(w -> (R_S(w),R_S'(w))) = t + min(t,d).
```

The proof uses only interpolation on distinct points. It does not use
`D=F_p`, additivity, `X^p-X`, Frobenius, symmetric functions, or a quadratic
extension.

## Bankable Lemma: Bessel Shell Moment Bound

For a fixed slope `z`, define

```text
nu_w(z) = #{T in binom(D,j) : R_{D\T}(w) = z[1]_E},
N = binom(n,j) = binom(n,k+t),
lambda = N / Q^t.
```

For exchange distance `d`, the number of ordered neighbors is
`K_d=binom(j,d)binom(a,d)`. The pair-rank lemma gives the exact second moment

```text
E nu_w(z)^2 = lambda^2 + lambda V
```

where

```text
V = sum_{0 <= d < t} K_d (Q^{-d}-Q^{-t})
```

and hence

```text
Var nu_w(z) <= lambda J,
J = sum_{0 <= d < t} binom(j,d)binom(a,d)Q^{-d}.
```

The shell is bounded by

```text
J <= sum_{d>=0} (aj/Q)^d/(d!)^2
  = I_0(2 sqrt(aj/Q))
  <= exp(2 sqrt(aj/Q))
  <= exp(n/sqrt(Q)).
```

Therefore

```text
E_w sum_z (nu_w(z)-lambda)^2 <= Q lambda J.
```

If `M(w)` is the number of missed slopes, every missed slope contributes
`lambda^2` to the defect. Thus some anchor satisfies

```text
M(w) <= QJ/lambda.
```

Consequently the fraction of bad slopes is at least

```text
1 - J/lambda,
```

and every slope is bad if

```text
lambda > QJ,
```

equivalently

```text
binom(n,k+t) > Q^{t+1} J.
```

## Smooth-Domain MCA Transfer

For an official smooth multiplicative domain `L subset F^*`, take

```text
E=X^t,  B_num=1,  f=w/E,  g=-1/E.
```

For any occupied slope `z`, choose `S=L\T` with

```text
[I_S(w)]_E = z.
```

Then

```text
P_z = (I_S(w)-z)/E
```

has degree `< k`, and on `S`,

```text
P_z = f + z g.
```

Noncontainment is automatic: if `G in F[X]_<k` agreed with `g=-1/E` on
`a=k+t` points, then `EG+1` would have `a` roots while having degree `<a`,
forcing `EG+1=0`, impossible.

Thus the source-local support-wise conclusion is

```text
epsilon_mca(RS[F,L,k], j/n) >= (1 - J/lambda)_+
```

with equality `epsilon_mca=1` under `lambda>QJ`.

## Entropy Consequence

If `k/n -> rho`, `t=(c+o(1)) n/log_2 Q`, and `log_2 Q=o(n)`, then

```text
log_2 lambda = (H_2(rho)-c+o(1))n
```

while `log_2 J=o(n)`. Hence the theorem gives all slopes, and therefore
source-local `epsilon_mca=1`, throughout the strict range

```text
c < H_2(rho).
```

For the four challenge rates, the coefficients are:

```text
rho=1/2   : H_2(rho)=1
rho=1/4   : H_2(rho)=0.811278...
rho=1/8   : H_2(rho)=0.543564...
rho=1/16  : H_2(rho)=0.337290...
```

This removes the Cycle 45 additive half-threshold `H_2(rho)/2`; that was an
artifact of the restricted ledger `n=p`, `Q=p^2`.

## Relation to PRZ Origin Files

The result targets the exact live object identified in
`experimental/paper_b_counterexample_comparison.md`: the balanced arbitrary
anchor residue-cloud regime. It does not contradict Paper B. It supplies a
lower/failure construction below entropy; it does not prove the safe-side
upper theorem above entropy.

The extension-coordinate transfer file does not disqualify the scalar
same-field theorem. In an extension presentation, the same line can be viewed
as a structured multiplication-slice phenomenon in an interleaved base code,
but in the same-field smooth-domain specialization it is scalar over `F`.

The Frobenius-compressed construction is no longer the preferred scalar-MCA
route. It remains useful as an alternate/additive mechanism, but it has a
common-factor/nonminimal-denominator caveat absent from the clean Bessel route
`E=X^t`, `B_num=1`.

## List-Decoding Implications

The Bessel route threatens the grand MCA challenge, not the grand list-decoding
challenge by itself.

Many bad slopes give many received words `f+zg`; they do not automatically give
many codewords around one fixed received word. The `m`-anchor zero-residue
construction is a genuine interleaved/list lower-bound mechanism, but its
exponent is the ordinary volume exponent

```text
H_2(rho) - m c,
```

so it reaches only `c < H_2(rho)/m` for `m` interleaving. It does not inherit
the MCA coefficient `H_2(rho)` for `m>=2`.

## Exact New Wall

The next full-MCA wall is the opposite-quantifier theorem:

```text
W-MCA-AA-RES-ENTROPY-BOUNDARY-MATCHING-UPPER
```

Equivalent labels used by the external answers:

```text
W-M1-AA-BALANCED-RESIDUE-CLOUD-UNIFORM-UPPER
W-M1-AA-RES-ABOVE-ENTROPY-QUOTIENT-SEPARATED-UNIFORM-UPPER-PACKING
```

The needed lemma is a uniform high-cloud inverse theorem:

> Above the entropy boundary, for every reduced/aperiodic residue-line datum
> `(E,B_num,w)` in the balanced range `t=sigma`, if the residue cloud contains
> more than `n^{1+o(1)}` noncontained slopes, then the datum must come from an
> explicit quotient-pullback, tangent/contained, or other already-separated
> template.

Together with the repaired residual-list reduction for `t<sigma`, this would
give the two-sided entropy transition for scalar smooth-domain MCA.

For the list side, the next exact wall is:

```text
W-L2-CORRELATED-COMMON-SUPPORT-RANK-COMPRESSION-VS-DIAGONALIZATION
```

One must either construct a non-diagonal `m`-row ensemble with effective
residue rank below `mt`, or prove every such rank compression diagonalizes to a
lower-arity/list-volume construction.
