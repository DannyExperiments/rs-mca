# Cycle 65 Thickened Gadget Color Audit

## Executive Verdict

**Status:** `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL`.

**Significance:** high for route narrowing, not a prize solve. Cycle 65
converts the thickened `t=1` MCA color question from a broad structural wall
into one explicit finite product-set occupancy verifier. It also kills the
hope that the thickened color automatically collapses to the scalar product
color or the truncated jet.

## Bankable Lemmas

The worker banks the exact factorization:

```text
L-MODEL-GJ-THICKENED-FACTORIZATION
```

In the Role 05 characteristic-17 model,

```text
F_0 = F_{17^16},  H_0 = mu_256 = <eta>,  eta^16 = zeta = 3,
K = <eta^8>,  |K| = 32.
```

For the three local degree-8 polynomials

```text
P_1(X)=X^8+4X^5+5X^4+10X^3+4X^2+4X+6
P_2(X)=X^8+9X^5+5X^4+12X^3+14X^2+13X+14
P_3(X)=X^8+11X^5+5X^3+X^2+12X+4,
```

and each local state `A_{i,a}=zeta^a A_i`, the thickening factor satisfies

```text
v_{t,A_{i,a}}
= prod_{x in eta^t A~}(beta - x)
= (-1)^a 3^t P_i(beta^2 zeta^{-a} eta^{-2t}).
```

Thus each support

```text
T = {1} union union_{t=1}^7 eta^t A~_t
```

has

```text
rho_beta(T)
= prod_{x in T}(beta - x)
= C prod_{t=1}^7 u_t(i_t,a_t),
```

where `C=(beta-1)3^12` and

```text
u_t(i,a)=(-1)^a P_i(beta^2 zeta^{-a} eta^{-2t}).
```

The occupied-color count is exactly the constrained sevenfold product-set:

```text
Occ =
#{ prod_{t=1}^7 u_t(i_t,a_t) :
   (i_t,a_t) in {1,2,3} x Z/16,
   sum_t r_t == 4 mod 16 },
```

with

```text
r_t = s_{i_t} + 8(a_t mod 2) mod 16,
(s_1,s_2,s_3)=(15,9,12).
```

This is an exact finite object in `F_{17^16}^*`, or equivalently a constrained
sevenfold sumset after discrete logs.

## Route Cut

Cycle 65 cuts the easy collapse route. The thickening coordinate

```text
rho_beta(T)=beta^113 E_T(1/beta)
```

depends on the full locator coefficients, not just the truncated jet
`E_T mod z^6` and scalar product color. The Role 05 packet fixes only the
first five elementary coefficients and the product. Higher coefficients vary
across the 48-state gadgets, so no model-independent norm, trace, or jet
identity forces the thickened colors to collapse.

The worker also notes that a generic-`beta` union-bound certificate is not
available at this field size: the number of possible bad pair constraints is
larger than the field. So the wall cannot be closed by a symbolic genericity
argument alone.

## New Wall

The surviving exact wall is:

```text
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

The decision problem is now concrete:

1. Fix an explicit model of `F_{17^16}`.
2. Choose `eta` of order `256` with `eta^16=3`.
3. Choose admissible `beta notin mu_512`.
4. Build the `7 x 3 x 16` table
   `u_t(i,a)=(-1)^a P_i(beta^2 zeta^{-a} eta^{-2t})`.
5. Count distinct constrained sevenfold products with `sum r_t == 4 mod 16`.

The exact upper bound is the Cycle 64 scalar packet mass:

```text
Occ <= |P_0| = 52,747,567,104 = 393 * 2^27.
```

A single fixed color class contributes at most `8^7`, so any result above
`2^32` must use the union of many color classes rather than one local class.

## What Is Not Proved

- No official prize counterpacket is proved.
- No scalar-list local limit is proved.
- No full `t=1` MCA theorem is proved.
- No explicit admissible `(eta,beta)` occupancy count is computed.
- The finite frontier relevance of the `(n,sigma,j)=(256,6,113)` model stratum
  remains unresolved.

## Recommended Next Step

Launch or implement:

```text
V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER
```

The verifier should use meet-in-the-middle on the 7 active cosets:

```text
48^3 ~= 1.1e5, 48^4 ~= 5.3e6,
```

bucketed by color sum modulo `16`. It should return `Occ` for one explicit
admissible `(eta,beta)`, then optionally sweep representatives for `beta`.

Decision rule:

- If `Occ >= 2^32`, bank a model-level `t=1` MCA color obstruction and test
  finite frontier placement.
- If `Occ` is small for all admissible representatives tested, search for the
  hidden collapse identity and bank it separately.

In parallel, keep `RS-PRIZE-FRONTIER-V1-REGISTRY-FIRST-RUN` alive, because
even a large model occupancy is not prize-relevant until the finite reserve
ledger places the stratum.

## Raw Provenance

Raw artifacts and checksums are preserved in
`experimental/notes/m1/cycle65_thickened_gadget_color_raw/`.
