# Cycle 74 Prompt: Norm-Bucket Compiled Ladder Run

Try to fully solve the stated finite model target. If you cannot fully solve
it, progress it as much as possible. No Internet. Take all the time to reason
you need. Use MAX reasoning.

## Context

We are in the RS-MCA / Proximity Prize M1 scalar-apolar finite-model lane.
This is model-level arithmetic, not a prize-level MCA theorem.

Cycle 73 banked:

```text
L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL
L-CYCLE73-SOUND-NORM-BUCKET
L-CYCLE73-UNCONSTRAINED-D-DOMINATES
```

Codex locally checked:

```text
experimental/scripts/cycle73_prime_slot_norm_check.py
experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
```

The current model is:

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6X^9,
beta = X + 2,
xi = beta^2,
eta^16 = 3.
```

For each slot `t=1,...,7` and key `(i,a)`, the banked slot identity is:

```text
y_t = xi eta^(-2t),
u_t(i,a) = prod_{c in S_{i,a}} (y_t - c),
S_{i,a} = {3^(a+e mod 16) : e in E_i} subset F_17^*.
```

The false t-independent Cycle 70 collapse remains cut. The `(color, product)`
key remains cut. Norm bucketing is sound because `N(prod u_t)=prod N(u_t)` is
a function of the product itself.

## Read These Files First

Read in this order:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle73_compiled_product_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/cycle73_compiled_product_ladder_raw/response.md
current_repo_snapshot/experimental/scripts/cycle73_prime_slot_norm_check.py
current_repo_snapshot/experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle72_product_only_ladder_audit.md
current_repo_snapshot/experimental/scripts/cycle71_product_ladder_checker.py
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/BANKED_LEMMAS.md
current_repo_snapshot/CUTS_AND_FALSE_ROUTES.md
current_repo_snapshot/ACTIVE_WALLS.md
```

## Task

Your target is:

```text
V-CYCLE74-NORM-BUCKET-COMPILED-LADDER-RUN
```

This is an execution/certificate target. Produce one of:

1. An actual executable checker and completed certificate for product-only
   `k=3/k=4`, preferably `k=5`, using packed product keys and sound norm
   buckets.
2. An explicit product collision, with slot subset, preimage keys `(i,a)`,
   and shared field product, verified against the Cycle 68/73 arithmetic.
3. A proof that a smaller structural statement makes the computation
   unnecessary.

If your environment cannot execute code or write output files, say so
immediately and do **not** claim a pass. In that case, focus on a concrete
implementation plan or a proof/counterpacket, but mark code `UNRUN`.

## Required Certificate Fields

Any pass certificate must include:

```json
{
  "key": "packed_product_only",
  "bucket": "norm_function_of_product",
  "selfchecks": {
    "prime_field_identity_all_336": true,
    "eta16_equals_3": true,
    "false_collapse_fails_at": {"t":1,"i":1,"a":0},
    "norm_is_homomorphism": true
  },
  "ladder": [
    {"k": 1, "product_injective": true},
    {"k": 2, "product_injective": true},
    {"k": 3, "product_injective": true},
    {"k": 4, "product_injective": "<bool>"},
    {"k": 5, "product_injective": "<bool or omitted>"}
  ],
  "first_collision": "null or explicit preimage/value record",
  "displacement_energy_E_S": "optional exact support-energy table",
  "decision": "PRODUCT_ONLY_LADDER_PASSED_TO_KMAX or PARTIAL_COLLISION_FOUND"
}
```

## Hard Restrictions

- Do not use `(color, product)` as a duplicate key.
- Do not use the false Cycle 70 t-independent collapse.
- Do not treat unrun code as evidence.
- Do not promote this model-level result to the official prize problem.
- Preserve exact preimages for any collision.

## Required Output

Start with one label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. What was actually executed or proved.
3. Certificate or collision details.
4. Remaining wall.
5. Next exact lemma/construction.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

