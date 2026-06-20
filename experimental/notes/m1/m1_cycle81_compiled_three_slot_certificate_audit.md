# Cycle 81 Compiled Three-Slot Certificate Audit

## Verdict

```text
PROOF / BANKABLE_LEMMA / PLAN
```

Confidence: high for the finite certificate and the minimum-distance
consequence.

Cycle 81 itself returned an unrun NumPy checker because the worker had read
access only. Codex converted it into an executable local verifier with an
exact scalar self-test and ran it successfully.

## Banked Lemma

### L-CYCLE81-THREE-SLOT-PRODUCT-INJECTIVITY

For every three-slot subset

```text
{t1,t2,t3} subset {1,...,7},
```

the product map

```text
(k1,k2,k3) |-> u_t1(k1) u_t2(k2) u_t3(k3)
```

is injective on `48^3` tuples.

Codex added and ran:

```text
experimental/scripts/cycle81_vectorized_three_slot_checker.py
experimental/notes/m1/cycle81_three_slot_injectivity_certificate.json
```

The certificate decision is:

```text
ALL_3_SUBSETS_PRODUCT_INJECTIVE
```

with:

```text
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 4
self_test = scalar_pair_12_matches_vectorized
```

The self-test compares the vectorized multiplication against the scalar
`cycle80_three_slot_injectivity_checker.py` multiplication on the full
slots `{1,2}` product table before accepting the batch arithmetic.

## Consequence

Together with the Cycle 77 certificate that all singleton and pair slot-product
maps are injective, this proves:

```text
L-CYCLE81-PRODUCT-FIBER-MINDIST-GE-4
```

Any two distinct product-equal seven-tuples differ in at least four slots.

Reason: if a collision differed in at most three slots, cancel all agreeing
nonzero slots. The remaining equality would be a product collision on one,
two, or three slots. Cycles 77 and 81 exclude all such collisions.

## What This Does Not Prove

This does **not** prove:

```text
m_max(beta) <= 12
```

and it does not decide the color-filtered maximum fiber. It only removes all
low-weight product collisions through weight `3`.

## Remaining Wall

The next finite wall is:

```text
V-CYCLE82-FOUR-SLOT-OR-MITM-MMAX-CERTIFICATE
L-CYCLE82-FOUR-SLOT-PRODUCT-INJECTIVITY
W-CYCLE82-COLOR-FILTERED-MITM-MMAX-CENSUS
```

There are two viable next targets:

1. Certify all four-slot product maps are injective, proving product-fiber
   minimum distance at least `5`.
2. Move directly to the color-filtered L/R MITM census for `m_max(beta)<=12`,
   using the Cycle 75/76 injective split, Cycle 78 incidence formula, Cycle 79
   tau symmetry, and Cycle 81 min-distance floor.

The second target is the actual prize-local finite target; the first is a
smaller guardrail that may simplify or falsify parts of the census.

## What To Do Next

Stage Cycle 82 against a compiled four-slot certificate or direct MITM
`m_max` census. Avoid another broad proof prompt; the route is now explicitly
finite-certificate driven.
