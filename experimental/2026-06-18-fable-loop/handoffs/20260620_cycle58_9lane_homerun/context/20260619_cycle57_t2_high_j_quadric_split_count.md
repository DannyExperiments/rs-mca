# Cycle 57 Prompt: t=2 High-j Determinantal Quadric Split Count

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the recent Cycle 54, Cycle 55, and Cycle 56 local audits first. Preserve
the labels `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and
`EXACT_NEW_WALL` literally.

## Why This Prompt Exists

Cycle55 showed that the `t=2,j=2` conic subcase has a corrected Weil-scale
count

```text
R=binomial(n,2)/Q+O(sqrt(Q))
```

and cuts the literal toy target `+O(1)`. Cycle56 local audit then cut the route
that tries to promote this to an official counterpacket: balanced `t=2,j=2`
forces

```text
k=n-4,
rho -> 1,
```

so it is not one of the official constant rates

```text
rho in {1/2,1/4,1/8,1/16}.
```

The constant-rate branch has

```text
j=n-k-sigma=(1-rho)n-sigma,
```

so `j` is linear in `n`, not fixed.

## Banked t=2 Normal Form

Cycle54 banked that for `t=2` the transverse landing count is

```text
R=#{T split : D(T)=0, b(T)!=0},
```

where

```text
D(T)=a_0(T)b_1(T)-a_1(T)b_0(T)
```

is a canonical quadratic form in the locator coefficients

```text
ell_T=(ell_0(T),...,ell_j(T)).
```

Equivalently,

```text
D(T)=sum_{l,l'=0}^{j} kappa_{l,l'} ell_l(T) ell_{l'}(T),
kappa_{l,l'}=u_l v_{l'+1}-u_{l+1}v_l.
```

For `j=1`, Cycle54 proved `R<=2=O(j)`.

For `j=2`, Cycle55 reduced the count to split pairs on a conic and corrected
the toy target to `+O(sqrt(Q))`.

## Active Wall

```text
W-MCA-T2-HIGH-J-DETERMINANTAL-QUADRIC-SPLIT-COUNT
```

Let `L` be a smooth multiplicative evaluation domain, `|L|=n`, and let

```text
t=2,
k=floor(rho n),
j=n-k-t,
rho in {1/2,1/4,1/8,1/16}.
```

After removing tangent/core, same-witness, contained, quotient-action-rank,
and imprimitive/coset packets, prove or refute a constant-rate upper bound for

```text
R=#{T in binom(L,j) : D(T)=0, b(T)!=0}.
```

The target scale is not `+O(1)`. The relevant safe-side numerator target is
roughly `n^{1+o(1)}` after quotient terms are separated.

## Required Questions

1. Does the t=2 determinant equation define a high-dimensional quadric section
   of the split-locator variety whose nonquotient split points are bounded by
   `n^{1+o(1)}`?

2. Can the count be reduced to a known or provable subgroup-variety incidence
   theorem for elementary symmetric coordinates of `j`-subsets of `L`?

3. If the answer is no, produce a source-valid constant-rate `COUNTERPACKET`
   with more than `n^{1+o(1)}` slopes after quotient/tangent packets are
   removed.

4. Does the Cycle55 `O(sqrt(Q))` phenomenon generalize to an error term that
   is harmless at constant rate, or can it compound across high-dimensional
   split-locator families?

5. Is the better next formulation actually the global syndrome wall

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

rather than a t=2 quadric sublane? If so, give the exact reduction.

## Required Output Options

Return one of:

1. `PROOF`: a constant-rate t=2 high-`j` upper bound at the intended
   `n^{1+o(1)}` scale after named templates are removed.
2. `COUNTERPACKET`: a source-valid constant-rate high-`j` construction with
   too many nonquotient slopes.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction to a smaller exact
   theorem, preferably a named subgroup/split-locator incidence statement.
4. `ROUTE_CUT`: a precise reason the t=2 quadric sublane is not the right
   route and the work must return to the syndrome transverse-secant inverse.

Do not promote a fixed-`j` toy phenomenon to the official branch.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```
