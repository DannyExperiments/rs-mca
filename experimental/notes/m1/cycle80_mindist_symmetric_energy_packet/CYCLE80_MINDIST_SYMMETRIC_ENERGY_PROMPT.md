# RS-MCA Cycle 80: Exact Minimum Distance Or Tau-Symmetric Energy Bound

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

There are seven slots and 48 values per slot:

```text
Phi(T)=prod_{t=1}^7 u_t(k_t),  T=(k_1,...,k_7).
```

The constrained domain is:

```text
P_0 = {T : sum_t color(k_t)=4 mod 16}.
```

The target is:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

## Banked Facts

Cycle 75:

```text
L(k_1,k_2,k_3)=u_1u_2u_3
```

is product-injective on `48^3=110592` tuples.

Cycle 76:

```text
R(k_4,k_5,k_6,k_7)=u_4u_5u_6u_7
```

is product-injective on `48^4=5308416` tuples.

Cycle 77:

All singleton and pair slot-product maps are injective; product fibers have
minimum distance at least `3`.

Cycle 78:

For each value `v`,

```text
m(v) =
#{ l in L_img : v l^{-1} in R_img
   and colorL(l)+colorR(v l^{-1})=4 mod 16 }.
```

Cycle 79:

The 48 legal 8-subsets are closed under complement. There is an involution

```text
tau(1,a) = (2,a+6)
tau(2,a) = (1,a+10)
tau(3,a) = (3,a+8)
```

such that

```text
u_t(k) u_t(tau(k)) = 3^(-2t)(beta^32 - 9^t),
Phi(tau(T)) = K / Phi(T),
tau(P_0)=P_0,
m(v)=m(K/v).
```

Codex locally verified these identities with:

```text
current_repo_snapshot/experimental/scripts/cycle79_involution_verifier.py
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
```

## This Prompt's Exact Wall

Attack:

```text
V-CYCLE80-MINDIST-OR-SYMMETRIC-ENERGY
L-CYCLE79-MINDIST-EXACT
W-CYCLE79-SYMMETRIC-ENERGY-BOUND
```

The product-fiber code has distance at least `3`. Decide the next exact rung:

```text
Is there a product collision supported on exactly three slots?
```

Equivalently, for some slot triple `S`, do two distinct assignments on those
three slots have the same product, with the other four slots fixed/cancelled?

## Task

Primary target:

```text
Prove or disprove exact three-slot product-injectivity for all 35 slot triples.
```

Acceptable outputs, in priority order:

1. A theorem-grade proof that all three-slot product maps are injective, giving
   product-fiber minimum distance at least `4`.
2. An explicit three-slot collision packet: slot triple, two assignments,
   matching packed field product, colors, and how it feeds the coherent-ratio
   route.
3. A genuinely optimized checker/certificate design that can decide the
   three-slot question locally, with exact file format and no hidden heuristic.

Secondary target if the three-slot question is closed:

```text
Use tau symmetry to prove a multiplicity/energy bound approaching
m_max(beta)<=12, or isolate the next exact finite check.
```

In additive-log language, each slot image is symmetric:

```text
W_t(k) + W_t(tau(k)) = c_t.
```

Try to exploit this together with product-injectivity of pairs and the
left/right MITM split.

## Required Discipline

- Equality key is packed field product only.
- Color is a domain filter, not an equality key.
- Do not claim proof from unrun code.
- If your environment is read-only, say so and mark code `UNRUN`.
- Prefer an explicit proof/counterpacket/certificate over broad census
  planning.
- The full 48^7 census is not the task. The first task is the exact three-slot
  product-collision question.

## Useful Mounted Files

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle77_subset_injectivity_check.py
current_repo_snapshot/experimental/scripts/cycle79_involution_verifier.py
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle79_common_ratio_bound_audit.md
current_repo_snapshot/experimental/notes/m1/cycle79_common_ratio_bound_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
```
