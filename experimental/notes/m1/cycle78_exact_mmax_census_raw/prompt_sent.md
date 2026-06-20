# RS-MCA Cycle 78: Exact Mmax Census Or Product-Collision Certificate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

## Context

We are in the finite M1 scalar-apolar model:

```text
F = F_17[X] / (X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

There are seven slots, 48 values per slot. Product value:

```text
Phi(T)=prod_t u_t(k_t),  T=(k_1,...,k_7).
```

The constrained domain:

```text
P_0 = { T : sum_t color(k_t) = 4 mod 16 }.
```

Prize-route finite target:

```text
m_max(beta)=max_v #{T in P_0 : Phi(T)=v} <= 12.
```

## Banked Before This Prompt

Cycle 75:

```text
slots {1,2,3}: 48^3 = 110592 products, all distinct.
```

Cycle 76:

```text
slots {4,5,6,7}: 48^4 = 5308416 products, all distinct.
```

Cycle 77:

```text
all slot subsets of sizes 1 and 2 are product-injective;
every product fiber has Hamming distance >= 3.
```

Relevant mounted files:

```text
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/scripts/cycle76_fast_right_half_check.py
current_repo_snapshot/experimental/scripts/cycle77_subset_injectivity_check.py
current_repo_snapshot/experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle77_ab_product_maxfiber_audit.md
```

## Task

Attack:

```text
V-CYCLE78-EXACT-MMAX-CENSUS
W-CYCLE78-FULL-PRODUCT-INJECTIVITY-OR-13FOLD
```

Primary acceptable outcomes:

1. `PROOF`: exact certificate that `m_max(beta)<=12`.
2. `COUNTERPACKET`: explicit `13`-fold packet in `P_0`.
3. `BANKABLE_LEMMA`: compiled/executable product-collision certificate for
   all 3-subsets, all 4-subsets, or stronger, with exact output schema.
4. `ROUTE_CUT`: prove that this census route cannot certify the target without
   full enumeration, and give the next narrower wall.

## Hard Requirements

- Equality key is packed field product only.
- Color sum is a domain filter, never an equality key.
- Norms are legal shard keys only when they are functions of product.
- Do not claim proof from unrun code.
- If the environment is read-only, say so and mark code `UNRUN`.
- Prefer actual executable code/certificate over another proof sketch.

## Suggested Concrete Work

1. Produce fast C/Rust/Python-specialized code for either:

```text
all 4-subset product-injectivity;
exact m_max over P_0;
```

or both.

2. Use the special modulus:

```text
X^16 = -X^8 - 3
```

to multiply field elements.

3. Certificate schema:

```json
{
  "decision": "MMAX_CERTIFIED_LE_12 | THIRTEEN_FOLD_PACKET | SUBSET_COLLISION_FOUND",
  "m_max": "<int or null>",
  "subset_results": "...",
  "witness": null
}
```

If a collision or 13-fold fiber is found, include all slot keys and the packed
product value.

## Required Output

1. Executive verdict and confidence.
2. Exact proof/counterpacket/certificate or run-ready code marked clearly.
3. What remains open.
4. Next exact lemma or construction.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T11-09-56-381Z-cycle78-exact-mmax-census-9004d20e/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---