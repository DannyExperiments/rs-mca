# Cycle 75 Prompt: Direct Maximum-Fiber Census

Try to fully solve the stated finite model target. If you cannot fully solve
it, progress it as much as possible. No Internet. Take all the time to reason
you need. Use MAX reasoning.

## Context

We are in the RS-MCA / Proximity Prize M1 scalar-apolar finite-model lane.
This is model-level arithmetic, not a prize-level MCA theorem.

The old sufficient gate

```text
D <= 155 => m_max(beta) <= 12
```

is probably too strong. Cycle 74 estimates unconstrained total collision
energy near `7000` for a random map:

```text
(48^7)^2 / (17^16 - 1) ~= 7082.63.
```

This does not threaten the actual target, because the desired condition is a
maximum-fiber bound:

```text
m_max(beta) = max_v #{T in P_0 : product(T)=v} <= 12.
```

The sharp threshold remains:

```text
|P_0| = 52747567104,
|P_0|/12 = 4395630592 > 2^32,
|P_0|/13 < 2^32.
```

Thus a 13-fold fiber is the real obstruction.

Banked tools:

```text
L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL
L-CYCLE73-SOUND-NORM-BUCKET
L-CYCLE73-UNCONSTRAINED-D-DOMINATES
L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION
L-CYCLE71-FULL-DISPLACEMENT
```

The model is:

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6X^9,
beta = X + 2,
xi = beta^2,
eta^16 = 3.
```

Slot values satisfy:

```text
y_t = xi eta^(-2t),
u_t(i,a) = prod_{c in S_{i,a}} (y_t-c),
S_{i,a} subset F_17^*.
```

Norm bucketing is sound because `N(product)` is a function of the product.
Color alone is not sound as a duplicate key, but the Role 05 domain `P_0`
itself includes a `Z/16` color constraint, so color can be used as a domain
filter/shard, not as a proof of product equality.

## Read These Files First

Read in this order:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle74_norm_bucket_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/cycle74_norm_bucket_ladder_raw/response.md
current_repo_snapshot/experimental/notes/m1/m1_cycle73_compiled_product_ladder_audit.md
current_repo_snapshot/experimental/scripts/cycle73_prime_slot_norm_check.py
current_repo_snapshot/experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/notes/m1/m1_cycle67_cross_color_injectivity_audit.md
current_repo_snapshot/BANKED_LEMMAS.md
current_repo_snapshot/CUTS_AND_FALSE_ROUTES.md
current_repo_snapshot/ACTIVE_WALLS.md
```

## Task

Your target is:

```text
V-CYCLE75-DIRECT-MMAX-FIBER-CENSUS
W-CYCLE74-DIRECT-MMAX-BUCKET-BOUND
```

Produce one of:

1. An exact executable design and certificate schema for proving
   `m_max(beta)<=12` directly without materializing all `>5e10` domain points.
2. A proof reducing `m_max<=12` to smaller product-ladder or meet-in-middle
   checks.
3. An explicit 13-fold collision packet in the constrained domain `P_0`, with
   all seven-slot preimages and the shared product.
4. A decisive route cut showing direct `m_max<=12` is false or infeasible under
   the current model.

## Requirements

- Distinguish clearly between:
  - product equality keys;
  - norm buckets, which are lossless shards;
  - color constraints, which filter the domain but are not product-equality
    certificates.
- Do not claim a finite pass unless it is proved or accompanied by an actually
  executed certificate.
- If your environment is read-only, say so and mark code `UNRUN`.
- Keep this model-level; do not promote to the official prize theorem.

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
2. Exact direct-`m_max` route or counterpacket.
3. Certificate schema or explicit collision packet.
4. What remains open.
5. Next exact lemma/construction.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

