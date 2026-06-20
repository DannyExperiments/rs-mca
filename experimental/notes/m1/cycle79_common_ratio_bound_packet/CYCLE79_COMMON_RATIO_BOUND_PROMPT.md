# RS-MCA Cycle 79: Common-Ratio Bound Or 13-Fold Witness

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
Phi(T)=prod_t u_t(k_t),  T=(k_1,...,k_7).
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

The color-free upper bound is:

```text
max_v |L_img cap v R_img^{-1}|.
```

## This Prompt's Exact Wall

Attack:

```text
V-CYCLE79-COMMON-RATIO-BOUND-OR-CENSUS
W-CYCLE79-COHERENT-RATIO-SET-SIZE
```

A product fiber of size `m` gives left products `l_1,...,l_m` and right products
`r_i=v/l_i`. After normalizing by one member, it gives a coherent ratio set:

```text
Delta = {delta_i = l_i/l_1 = r_1/r_i}
        subset Ratios(L_img) cap Ratios(R_img).
```

Moreover the ratios are coherent: the same base `l_1` satisfies
`l_1 delta in L_img`, and the same base `r_1` satisfies `r_1 delta^{-1} in
R_img` for all `delta in Delta`; color compatibility also holds in the
original `P_0` target.

## Task

Primary proof target:

```text
Every coherent Delta has size <= 12
```

or, depending on normalization:

```text
every nontrivial coherent ratio set has at most 11 additional ratios.
```

Counterpacket target:

```text
Construct an explicit coherent Delta of size 13 and recover the 13 tuples
in P_0.
```

If neither is reachable, produce a strictly smaller theorem/checker target.

## Required Discipline

- Equality key is packed field product only.
- Color is a domain filter, not an equality key.
- Do not claim proof from unrun code.
- If your environment is read-only, say so and mark code `UNRUN`.
- Prefer a finite theorem/counterpacket over broad census planning.

## Useful Mounted Files

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle76_fast_right_half_check.py
current_repo_snapshot/experimental/scripts/cycle77_subset_injectivity_check.py
current_repo_snapshot/experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle78_exact_mmax_census_audit.md
```

## Required Output

1. Executive verdict and confidence.
2. Proof, counterpacket, or bankable reduction.
3. If code appears, mark whether it was run.
4. What remains open.
5. Next exact lemma or construction.
