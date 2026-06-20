# RS-MCA Cycle 77: AB Product Max-Fiber / Max-Intersection Wall

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Context

We are in the M1 scalar-apolar finite model route for the RS-MCA / Proximity
Prize project.

The field/model is the Cycle 66/68 model:

```text
F = F_17[X] / (X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
eta^16 = 3
```

The seven slots have 48 values each:

```text
u_t(k),  t=1..7,  k=0..47.
```

The constrained domain is:

```text
P_0 = { (k_1,...,k_7) : sum_t color(k_t) = 4 mod 16 }.
```

The target is:

```text
m_max(beta) = max_v #{T in P_0 : prod_t u_t(k_t)=v} <= 12.
```

This would imply:

```text
Occ(beta) >= |P_0|/12 > 2^32.
```

## Newly Banked Cycle 76 Facts

Cycle 75 locally certified product-only injectivity for:

```text
left slots {1,2,3}: 48^3 = 110592 products, all distinct.
```

Cycle 76 now locally certifies product-only injectivity for:

```text
right slots {4,5,6,7}: 48^4 = 5308416 products, all distinct.
```

Certificate files in the mounted project source:

```text
current_repo_snapshot/experimental/notes/m1/cycle75_mitm_half_rung_certificate.json
current_repo_snapshot/experimental/scripts/cycle75_mitm_half_rung_check.py
current_repo_snapshot/experimental/scripts/cycle76_fast_right_half_check.py
current_repo_snapshot/experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle76_right_half_mmax_audit.md
```

Thus define honest sets:

```text
A = { prod_{t=1}^3 u_t(k_t) : k_t in [0,47] }, |A|=110592
B = { prod_{t=4}^7 u_t(k_t) : k_t in [0,47] }, |B|=5308416
```

Both maps are injective. The remaining target has the clean upper bound:

```text
m_max(beta) <= max_v |A cap v B^{-1}|.
```

The color condition in `P_0` only decreases this upper bound.

## Task

Attack:

```text
V-CYCLE77-AB-PRODUCT-MAXFIBER
W-CYCLE77-MAX-INTERSECTION-A-B-INVERSE
```

Primary goal:

```text
prove max_v |A cap v B^{-1}| <= 12
```

or stronger:

```text
prove m_max(beta) <= 12 directly with colors.
```

Counterpacket goal:

```text
find an explicit 13-fold product fiber in P_0.
```

If neither is possible, produce a smaller exact lemma or construction. Do not
return broad plans only.

## Required Discipline

- Equality key is packed field product only.
- The color sum is a domain filter, never an equality key.
- A subfield norm is only a shard key if it is a function of the product.
- Do not claim finite proof from unrun code.
- If your environment has only `Read`, say so explicitly and mark code `UNRUN`.
- Use labels literally: `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`,
  `ROUTE_CUT`, `EXACT_NEW_WALL`, `AUDIT`, `PLAN`.

## Suggested Lines Of Attack

1. Use the slot-polynomial/coset structure:

```text
u_t(i,a) = P_i(beta^2 eta^{-2t} 3^{-a}) * sign(a)
```

with `eta^16=3`, so slot arguments lie on disjoint eta-cosets.

2. Convert `a in A cap v B^{-1}` to an algebraic relation between a 3-slot
support product and a 4-slot support product. Try to show more than 12
solutions forces a forbidden low-degree identity.

3. Use multiplicative characters/norms only when they preserve product fibers.

4. If proving is out of reach, specify an exact compiled/sharded certificate
whose output would be theorem-grade:

```text
MMAX_CERTIFIED_LE_12
```

or an explicit `THIRTEEN_FOLD_PACKET` with all keys, colors, and product value.

## Required Output

1. Executive verdict and confidence.
2. Exact theorem/proof, counterpacket, or bankable reduction.
3. If code appears, mark whether it was run.
4. What remains open.
5. Next exact lemma or construction.
