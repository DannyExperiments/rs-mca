# RS-MCA Cycle 83: MITM Mmax Threshold Certificate Or 13-Fold Packet

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Current finite model

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

## Banked finite facts

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

Cycle 81:

```text
ALL_3_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
fiber_min_distance_lower_bound = 4
```

Cycle 82, just banked by Codex local execution:

```text
ALL_4_SUBSETS_PRODUCT_INJECTIVE
subsets_checked = 35
all_checked_product_injective = true
fiber_min_distance_lower_bound = 5
self_test = scalar_pair_12_matches_vectorized
```

Therefore every product fiber has Hamming distance at least `5`.

## Structural reduction from Cycle 82

Cycle 82 identified the scalar exponent-set formulation:

```text
u_t(i,a) = inv3t(t) prod_{b in bset(i,a)}
           (xi - eta^(2t+16b)).
```

The exponent supports for different slots lie in disjoint cosets:

```text
C_t = 2t + 16 Z / 256Z,   t=1,...,7.
```

Thus each seven-slot tuple corresponds to a 56-element balanced exponent set,
eight exponents in each of seven disjoint cosets, and:

```text
Phi(T) = const * g_M(xi),
g_M(Y)=prod_{e in M}(Y-eta^e).
```

Use this only if it gives a genuine reduction. Do not turn it into another
abstract planning note.

## Exact wall for this prompt

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

Primary task:

```text
Certify m_max(beta) <= 12, or produce an explicit 13-fold colored collision
packet in P_0.
```

## Preferred execution route

Use the L/R split:

```text
L_img = products on slots {1,2,3}, size 48^3 = 110592.
R_img = products on slots {4,5,6,7}, size 48^4 = 5308416.
```

Bucket `R_img` by color. For each `l in L_img`, only probe:

```text
colorR = 4 - colorL(l) mod 16.
```

Run a threshold census capped at `13`:

```text
count[v] += 1
abort and output packet as soon as count[v] reaches 13.
```

It is enough to prove no value reaches `13`. A complete histogram is not
required.

Use Cycle 79's involution only if it soundly reduces work without complicating
the certificate. A simple exact threshold census is preferable to a clever but
unverifiable argument.

## Required output

Return one of:

1. `PROOF / BANKABLE_LEMMA`: a reproducible certificate proving
   `m_max(beta)<=12`, with exact code or a machine-checkable certificate.
2. `COUNTERPACKET`: an explicit 13-fold packet listing the 13 seven-slot
   assignments, colors, and common packed-product key.
3. `EXACT_NEW_WALL / PLAN`: only if neither is possible, a strictly smaller
   executable wall with concrete implementation details, resource estimate,
   and no unsupported proof claim.

## Discipline

- Equality key is packed field product only.
- Color is a domain filter or collision annotation, not an equality key.
- Do not claim proof from unrun code.
- If your environment is read-only, say so and mark code `UNRUN`.
- Do not spend the answer re-proving Cycles 75-82.
- Do not output broad route planning. The only acceptable plan is an
  implementation-ready threshold census or a sharper finite obstruction.

## Useful mounted files

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle81_vectorized_three_slot_checker.py
current_repo_snapshot/experimental/scripts/cycle82_four_slot_product_checker.py
current_repo_snapshot/experimental/notes/m1/cycle82_four_slot_product_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle82_four_slot_or_mitm_mmax_audit.md
current_repo_snapshot/experimental/notes/m1/cycle82_four_slot_or_mitm_mmax_raw/response.md
current_repo_snapshot/experimental/notes/m1/cycle81_three_slot_injectivity_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle79_involution_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle78_exact_mmax_census_audit.md
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 64000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T13-27-48-949Z-cycle83-mitm-mmax-threshold-2ed7493f/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---