# Cycle 73 Prompt: Compiled Product-Only Ladder And Displacement Energy

Try to fully solve the stated finite model target. If you cannot fully solve
it, progress it as much as possible. No Internet. Take all the time to reason
you need. Use MAX reasoning.

## Context

We are in the RS-MCA / Proximity Prize M1 scalar-apolar finite-model lane.
This is **model-level arithmetic**, not a prize-level MCA theorem.

The current explicit model is the Cycle 66/68 Role 05 model over

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
xi = beta^2.
```

There are seven slots `t=1,...,7`, each with 48 choices indexed by
`(i,a)` where `i in {1,2,3}` and `a in Z/16Z`. The banked Cycle 68/70
slot-value formula is the t-dependent one:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

Equivalently, using the exponent sets in the checker,

```text
u_t(i,a) = prod_{e in E_i}(xi * eta^(-2t) - 3^((a+e) mod 16)).
```

The false Cycle 70 shortcut

```text
u_t(i,a)=prod_{c in 3^a D_i}(beta^2-c)
```

is cut. It fails already at `(t,i,a)=(1,1,0)`.

The Cycle 71 color-key verifier is also cut. Duplicate detection must be keyed
by the packed field product alone, not by `(color, product)`, unless you prove
that product equality forces color equality.

Banked facts:

- Product-only injectivity is locally certified through `k=2`.
- `L-CYCLE71-FULL-DISPLACEMENT`: if every `(k-1)` slot subset is
  product-injective, then any first `k`-slot collision is fully displaced.
- `L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION`: with
  `D=sum_v m_v(m_v-1)`, the off-diagonal collision energy decomposes as

```text
D = sum_S 48^(7-|S|) E_S,
```

where `E_S` is the ordered fully displaced product-collision energy on slot set
`S`. If the ladder passes through `k=4`, then only `|S|=5,6,7` survive. A
single five-slot collision gives `D>=2304>155`, so `k=5` injectivity becomes
mandatory for the `D<=155` route.

The model target is:

```text
D <= 155 => m_max(beta) <= 12 => Occ(beta) >= |P_0|/12 > 2^32.
```

## Read These Files First

Read in this order:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle72_product_only_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/cycle72_product_only_ladder_raw/response.md
current_repo_snapshot/experimental/scripts/cycle71_product_ladder_checker.py
current_repo_snapshot/experimental/notes/m1/cycle71_product_ladder_certificate.json
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/notes/m1/m1_cycle68_collision_multiplicity_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle69_slot_log_independence_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle70_k3_k4_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle71_optimized_ladder_audit.md
current_repo_snapshot/ACTIVE_WALLS.md
current_repo_snapshot/BANKED_LEMMAS.md
current_repo_snapshot/CUTS_AND_FALSE_ROUTES.md
```

## Task

Your target is:

```text
V-CYCLE72-COMPILED-PRODUCT-ONLY-LADDER-AND-ENERGY
```

Produce one of the following:

1. A source-valid proof that product-only injectivity passes for `k=3` and
   `k=4`, and if possible `k=5`.
2. A genuinely executable compiled verifier design for `k=3/k=4`, preferably
   extended to `k=5`, with exact collision preimage recovery and a precise
   certificate schema. The verifier must key by product only.
3. An explicit product collision, with slots, preimage keys `(i,a)`, and the
   shared field value, verified against the Cycle 68 arithmetic.
4. A stronger finite-energy plan that directly computes or bounds
   `D<=155` using the displacement-energy decomposition.

## Hard Restrictions

- Do **not** claim a rung passes unless you either prove it or provide a
  verifier/certificate that actually establishes it.
- Do **not** use the false t-independent Cycle 70 collapse.
- Do **not** use `(color, product)` as a duplicate key for a pass.
- Do **not** promote this model-level finite result to a prize-level theorem.
- If you provide code, make it deterministic, exact, and self-checking.
  Include the exact expected certificate fields.
- If you cannot execute code in your environment, say so explicitly and mark
  code as `UNRUN`.

## Required Output Format

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
2. What is proved, what is only planned, and what remains open.
3. Any explicit collisions or exact certificates.
4. Exact code or pseudocode, if relevant.
5. The next exact lemma or construction.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

