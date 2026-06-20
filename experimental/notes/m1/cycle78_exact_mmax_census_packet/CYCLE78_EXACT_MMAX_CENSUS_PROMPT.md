# RS-MCA Cycle 78: Exact Mmax Census Or Product-Collision Certificate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Context

We are in the finite M1 scalar-apolar model:

```text
F = F_17[X] / (X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

There are seven slots, 48 values per slot. Product value:

```text
Phi(T)=prod_t u_t(k_t),  T=(k_1,...,k_7).
```

The constrained domain:

```text
P_0 = { T : sum_t color(k_t) = 4 mod 16 }.
```

Prize-route finite target:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

## Banked Before This Prompt

Cycle 75:

```text
slots {1,2,3}: 48^3 = 110592 products, all distinct.
```

Cycle 76:

```text
slots {4,5,6,7}: 48^4 = 5308416 products, all distinct.
```

Cycle 77:

```text
all slot subsets of sizes 1 and 2 are product-injective;
every product fiber has Hamming distance >= 3.
```

Relevant mounted files:

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle76_fast_right_half_check.py
current_repo_snapshot/experimental/scripts/cycle77_subset_injectivity_check.py
current_repo_snapshot/experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle77_ab_product_maxfiber_audit.md
```

## Task

Attack:

```text
V-CYCLE78-EXACT-MMAX-CENSUS
W-CYCLE78-FULL-PRODUCT-INJECTIVITY-OR-13FOLD
```

Primary acceptable outcomes:

1. `PROOF`: exact certificate that `m_max(beta)<=12`.
2. `COUNTERPACKET`: explicit `13`-fold packet in `P_0`.
3. `BANKABLE_LEMMA`: compiled/executable product-collision certificate for
   all 3-subsets, all 4-subsets, or stronger, with exact output schema.
4. `ROUTE_CUT`: prove that this census route cannot certify the target without
   full enumeration, and give the next narrower wall.

## Hard Requirements

- Equality key is packed field product only.
- Color sum is a domain filter, never an equality key.
- Norms are legal shard keys only when they are functions of product.
- Do not claim proof from unrun code.
- If the environment is read-only, say so and mark code `UNRUN`.
- Prefer actual executable code/certificate over another proof sketch.

## Suggested Concrete Work

1. Produce fast C/Rust/Python-specialized code for either:

```text
all 4-subset product-injectivity;
exact m_max over P_0;
```

or both.

2. Use the special modulus:

```text
X^16 = -X^8 - 3
```

to multiply field elements.

3. Certificate schema:

```json
{
  "decision": "MMAX_CERTIFIED_LE_12 | THIRTEEN_FOLD_PACKET | SUBSET_COLLISION_FOUND",
  "m_max": "<int or null>",
  "subset_results": "...",
  "witness": null
}
```

If a collision or 13-fold fiber is found, include all slot keys and the packed
product value.

## Required Output

1. Executive verdict and confidence.
2. Exact proof/counterpacket/certificate or run-ready code marked clearly.
3. What remains open.
4. Next exact lemma or construction.
