# Cycle 56 Prompt: t=2, j=2 Conic Sqrt Counterpacket Check

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project source and recent loop material first, especially the Cycle 54
and Cycle 55 audits. Preserve the labels `PROOF`, `COUNTERPACKET`,
`BANKABLE_LEMMA`, `ROUTE_CUT`, and `EXACT_NEW_WALL` literally.

## Banked State

Cycle 54 proved that in the balanced `t=2` stratum the slope variable can be
eliminated. With

```text
a(T)=H(u)ell_T,
b(T)=H(v)ell_T,
D(T)=a_0(T)b_1(T)-a_1(T)b_0(T),
```

the transverse landing count is exactly

```text
R=#{T split : D(T)=0, b(T)!=0}.
```

Cycle 54 also proved the `j=1` case:

```text
R<=2=O(j).
```

Cycle 55 analyzed the first open case `t=2,j=2`. For `T={s,s'}`,

```text
e_1=s+s',
e_2=ss',
ell_T=(e_2,-e_1,1),
```

and the determinant becomes the explicit conic

```text
D(e_1,e_2)=0.
```

Writing the skew Plucker coefficients as

```text
M_ab = u_a v_b - u_b v_a,
```

the conic is

```text
D(e_1,e_2)
= M12 e_1^2 - M02 e_1 e_2 + M01 e_2^2
  - M13 e_1 + (M03-M12)e_2 + M23.
```

The split-pair curve is

```text
F(s,s')=D(s+s',ss')=0.
```

Cycle 55 banked the corrected statement:

```text
R = binomial(n,2)/Q + O(sqrt(Q))
```

after removing tangent/core and quotient/coset components. It cut the literal
`+O(1)` target in the large-domain genus-one regime unless extra hypotheses
force genus zero or a small-subgroup incidence theorem.

## Active Wall

```text
W-MCA-T2J2-CONIC-SQRT-COUNTERPACKET-CHECK
```

The Cycle 55 response suggests a possible `Theta(sqrt(Q))` excess coming from
Frobenius trace fluctuations of a genus-one split-pair curve. This is not yet
banked as `COUNTERPACKET`.

Your job is to verify or kill that seed.

## Required Task

Work in a concrete growing smooth-domain ledger, preferably:

```text
F = F_Q,
L = mu_n subset F^*,
n | Q-1,
k = n-j-t,
t=2,
j=2,
a=k+t=n-j,
```

or in a valid extension ledger if you keep `q_gen`, `q_line=Q`, and `q_chal`
separate.

Determine whether there are infinitely many source-valid, balanced,
transverse, quotient-separated, non-core, non-tangent `t=2,j=2` data for which

```text
#{ {s,s'} subset L : D(s+s',ss')=0, b({s,s'})!=0 }
-
binomial(n,2)/Q
```

is unbounded, ideally `Omega(sqrt(Q))`.

## What Counts As A Counterpacket

If you return `COUNTERPACKET`, include all of:

1. Explicit growing parameters `Q,n,L,k,t,j`.
2. Explicit or constructible transverse pencil `(u,v)` or equivalent
   residue-line datum.
3. Verification that the conic identity is the actual Cycle54/Cycle55
   determinant, not a relaxed curve-count surrogate.
4. Verification that the counted pairs are fully `L`-split monic squarefree
   locators.
5. Verification that `b(T)!=0` for the excess pairs or that discarded zeros are
   lower order.
6. Verification that the excess is not caused by:
   - common core or tangent packet;
   - same witness;
   - quotient/coset component;
   - low quotient-action rank `d_M(E)`;
   - imprimitive pullback through `X^M`;
   - contained support.
7. A source-valid MCA interpretation or a precise statement of which source
   hypothesis prevents promotion.

## What Counts As A Proof Instead

If the `Theta(sqrt(Q))` seed is false under the actual source hypotheses,
return `PROOF` or `ROUTE_CUT` and identify the exact missing condition. For
example:

- Does quotient separation force the relevant genus-one curve to have no large
  intersection with `mu_n x mu_n` beyond `O(1)`?
- Does the residue-line source force a split conic or genus-zero curve?
- Does `b(T)!=0` remove the entire Frobenius-trace fluctuation?
- Does transversality imply a hidden denominator compression?
- Does the official upper theorem only need an `O(sqrt(Q))` error because
  `sqrt(Q)/Q` is below the target field budget?

Be explicit. Do not leave this as an aesthetic objection.

## Checker Request

If possible, include a finite checker or exact algorithm that, for small
`Q,n`, computes:

```text
R_actual = #{ unordered pairs {s,s'} subset L : F(s,s')=0, b(T)!=0 },
R_base   = binomial(n,2)/Q,
excess   = R_actual - R_base,
```

and tags degenerate cases:

```text
core/tangent,
coset/quotient,
low d_M(E),
b(T)=0,
singular conic,
genus zero versus genus one.
```

The checker can be pseudocode if the field implementation is long, but the
mathematical test must be exact enough to implement.

## Required Output Options

Return one of:

1. `COUNTERPACKET`: a verified source-valid growing family with unbounded
   excess over `binomial(n,2)/Q`.
2. `PROOF`: a theorem showing the excess is `O(1)` under the real source
   hypotheses, despite the generic Weil `O(sqrt(Q))` curve bound.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction to a smaller exact
   theorem, preferably a named subgroup-curve intersection statement.
4. `ROUTE_CUT`: a precise reason the Cycle55 `sqrt(Q)` seed cannot be promoted
   or the `+O(1)` target was the wrong target.

## Do Not Do

- Do not use L2 anticollision as an upper bound.
- Do not count free-root or relaxed `F_Q`-points instead of split pairs in
  `L`.
- Do not ignore `b(T)!=0`.
- Do not ignore quotient-component packets.
- Do not promote this to a prize solve.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```
