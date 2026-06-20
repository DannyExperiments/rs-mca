# Cycle 72 Prompt: Product-Only K3/K4 Ladder Or Lossless Color Proof

Try to fully solve the stated target. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

This is a narrow finite/model target. Do not brainstorm broadly.

## Read Order

Read these files from the project source snapshot first:

1. `ACTIVE_WALLS.md`
2. `CUTS_AND_FALSE_ROUTES.md`
3. `BANKED_LEMMAS.md`
4. `current_repo_snapshot/experimental/notes/m1/m1_cycle71_optimized_ladder_audit.md`
5. `current_repo_snapshot/experimental/scripts/cycle71_product_ladder_checker.py`
6. `current_repo_snapshot/experimental/notes/m1/cycle71_product_ladder_certificate.json`
7. `current_repo_snapshot/experimental/notes/m1/m1_cycle70_k3_k4_ladder_audit.md`
8. `current_repo_snapshot/experimental/scripts/cycle70_slot_normalization_checker.py`
9. `current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py`
10. `current_repo_snapshot/experimental/notes/m1/cycle71_optimized_ladder_run_raw/response.md`

## Current State

Cycle 69/70 locally verified product-injectivity through `k=2`.

Cycle 70 cut this false claim:

```text
u_t(i,a)=prod_{c in 3^a D_i}(beta^2-c).
```

Cycle 71 banked:

```text
L-CYCLE71-FULL-DISPLACEMENT
```

If every `(k-1)`-subset of slots is product-injective, then any `k`-subset
collision must differ in every one of the `k` slots.

Cycle 71 also returned Python code that keyed duplicates by:

```text
(color, packed_product)
```

That is insufficient for product-injectivity unless you separately prove:

```text
product equality => color equality.
```

The corrected local reference script keys by packed field product only and has
only been run through `k=2`.

## Your Task

Primary target:

```text
V-CYCLE71-PRODUCT-ONLY-K3-K4-LADDER-RUN
```

Give one of:

1. a product-only optimized exact verifier for all `k=3` and `k=4` slot
   subsets, with code and certificate schema;
2. a proof that product equality forces color equality, thereby validating the
   color-filtered verifier;
3. an explicit product collision for `k=3` or `k=4`, with slots, keys, and
   field product value checkable against `cycle68_slot_factorization_checker.py`.

Secondary target:

```text
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

If the product-only ladder passes through `k=4`, state the exact next
collision-energy computation needed to prove `D<=155`.

## Required Output

Start with exactly one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then include:

1. **Executive verdict.** Is product-only `k=3/k=4` proved, falsified, or still
   open?
2. **Forbidden shortcuts.** Explicitly state that you did not use the false
   t-independent collapse or the unproved `(color, product)` key.
3. **Exact code/proof/collision.** If code, make it product-only or prove the
   color key is lossless. If collision, give direct preimage data.
4. **Certificate schema.** Include exact JSON fields.
5. **Energy implication.** State what follows for support size, `D`, `m_max`,
   and `Occ(beta)`.
6. **Next exact lemma/construction.** Answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Guardrails

- Do not claim the prize problem is solved.
- Do not promote this finite model to an MCA theorem.
- Do not use probabilistic evidence as proof.
- Do not use the false Cycle 70 t-independent collapse.
- Do not use `(color, product)` as a duplicate key unless you prove it is
  lossless.

