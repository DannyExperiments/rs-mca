# Cycle 71 Optimized Ladder Audit

## Verdict

```text
BANKABLE_LEMMA / PLAN / ROUTE_CUT
```

Confidence: high for the full-displacement lemma; high that the returned
Python color-key verifier is insufficient for product-injectivity; unknown for
the still-open `k=3/k=4` ladder.

Cycle 71 does **not** prove or kill:

```text
V-CYCLE70-K3-K4-OPTIMIZED-LADDER-RUN
```

No verifier was executed by the worker and no collision was found.

## Banked Lemma

### L-CYCLE71-FULL-DISPLACEMENT

If every `(k-1)`-subset of slots is product-injective, then any `k`-subset
collision must differ in every one of the `k` slots.

Proof: if a collision agrees on one slot, cancel that common nonzero slot value
and get a collision on the remaining `(k-1)` slots. Product-injectivity at
level `k-1` then forces equality in every remaining slot, contradicting that
the original pair was a collision.

Since `k<=2` is locally certified from Cycle 69/70, any first `k=3` collision
must be fully displaced across its three slots.

## Route Cut

The returned Python ladder code uses a key of the form:

```text
(color, packed_product)
```

This is not a valid product-injectivity check unless product equality is already
known to force color equality. That implication is not banked. A product
collision with different color would be missed. Therefore the Python verifier
as written is cut as insufficient.

The returned C verifier keys only the packed field product and is closer to the
correct finite task, but it was not executed here and does not recover
preimages on a collision without an additional rerun.

## Local Follow-Up

Codex added a corrected product-only reference script:

```text
experimental/scripts/cycle71_product_ladder_checker.py
```

and locally ran it only through `k=2`, saving:

```text
experimental/notes/m1/cycle71_product_ladder_certificate.json
```

This preserves the already banked `k<=2` certificate and confirms the script
path, but does not attempt the expensive `k=3/k=4` rungs.

## Active Wall

The active wall remains:

```text
V-CYCLE71-PRODUCT-ONLY-K3-K4-LADDER-RUN
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

The next useful step is no longer another symbolic shortcut. It is an actual
product-only optimized run, with collision preimage recovery if any duplicate
appears.

