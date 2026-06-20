# RS-MCA Cycle 82: Four-Slot Certificate Or Direct MITM Mmax Census

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Current Finite Model

We are in the M1 scalar-apolar finite model:

```text
F = F_17[X] / (X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

Seven slots, 48 values per slot:

```text
Phi(T)=prod_{t=1}^7 u_t(k_t).
```

Constrained domain:

```text
P_0 = {T : sum_t color(k_t)=4 mod 16}.
```

Target:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

## Banked Facts

Cycle 75:

```text
slots {1,2,3}: 48^3 tuples, product map injective.
```

Cycle 76:

```text
slots {4,5,6,7}: 48^4 tuples, product map injective.
```

Cycle 78:

```text
m(v)=#{ l in L_img : v l^{-1} in R_img
        and colorL(l)+colorR(v l^{-1})=4 mod 16 }.
```

Cycle 79:

```text
Phi(tau(T)) = K / Phi(T),  tau(P_0)=P_0,  m(v)=m(K/v).
```

Cycle 80:

Three-slot injectivity is equivalent to:

```text
(R_t1 R_t2) cap R_t3 = empty.
```

Cycle 81:

Codex locally ran the vectorized exact checker:

```text
current_repo_snapshot/experimental/scripts/cycle81_vectorized_three_slot_checker.py
current_repo_snapshot/experimental/notes/m1/cycle81_three_slot_injectivity_certificate.json
```

It passed:

```text
ALL_3_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
fiber_min_distance_lower_bound = 4
```

So every product fiber has Hamming distance at least `4`.

## This Prompt's Exact Wall

Attack:

```text
V-CYCLE82-FOUR-SLOT-OR-MITM-MMAX-CERTIFICATE
L-CYCLE82-FOUR-SLOT-PRODUCT-INJECTIVITY
W-CYCLE82-COLOR-FILTERED-MITM-MMAX-CENSUS
```

## Task

Primary target:

```text
Choose and execute the next finite-certificate step.
```

Preferred outcomes, in order:

1. A theorem-grade compiled/vectorized certificate that all 35 four-slot
   product maps are injective, proving product-fiber minimum distance at least
   `5`; or an explicit four-slot collision packet.
2. A direct compiled MITM census certificate for `m_max(beta)<=12`, using:
   the Cycle 75/76 L/R split, the Cycle 78 incidence formula, the Cycle 79
   tau symmetry, and the Cycle 81 min-distance floor.
3. If neither can be closed inside your environment, produce a smaller exact
   executable certificate target that strictly reduces the remaining
   `m_max<=12` wall.

## Required Discipline

- Equality key is packed field product only.
- Color is a domain filter or collision annotation, not an equality key.
- Do not claim proof from unrun code.
- If your environment is read-only, say so and mark code `UNRUN`.
- Avoid broad planning. The target is a finite certificate, explicit collision,
  or a strictly smaller executable wall.

## Useful Mounted Files

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle81_vectorized_three_slot_checker.py
current_repo_snapshot/experimental/notes/m1/cycle81_three_slot_injectivity_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle81_compiled_three_slot_certificate_audit.md
current_repo_snapshot/experimental/notes/m1/cycle81_compiled_three_slot_certificate_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle78_exact_mmax_census_audit.md
```
