# Cycle 76 Prompt: Right-Half And Direct Mmax Census

Try to fully solve the stated finite model target. If you cannot fully solve
it, progress it as much as possible. No Internet. Take all the time to reason
you need. Use MAX reasoning.

## Context

We are in the RS-MCA / Proximity Prize M1 scalar-apolar finite-model lane.
This is model-level arithmetic, not a prize-level MCA theorem.

Cycle 75 banked:

```text
L-CYCLE75-MITM-SUBFIELD-NORM-SHARD-CENSUS
W-CYCLE75-CONSTRAINED-ENERGY-IS-THE-RIGHT-SCALE
W-CYCLE75-LADDER-CANNOT-FINISH
```

Codex locally executed the bounded MITM left half:

```text
slots {1,2,3}: 48^3 = 110592 tuples, 110592 distinct products.
```

with:

```text
experimental/scripts/cycle75_mitm_half_rung_check.py
experimental/notes/m1/cycle75_mitm_half_rung_certificate.json
```

The right half `{4,5,6,7}` remains unrun.

The real target remains:

```text
m_max(beta) = max_v #{T in P_0 : product(T)=v} <= 12.
```

The direct census should use:

- packed field product as the equality key;
- color sum constraint as the `P_0` domain filter;
- a multiplicative subfield norm, preferably `N_{F/F_{17^8}}`, as a lossless
  shard.

## Read These Files First

Read in this order:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle75_direct_mmax_fiber_audit.md
current_repo_snapshot/experimental/notes/m1/cycle75_direct_mmax_fiber_raw/response.md
current_repo_snapshot/experimental/scripts/cycle75_mitm_half_rung_check.py
current_repo_snapshot/experimental/notes/m1/cycle75_mitm_half_rung_certificate.json
current_repo_snapshot/experimental/notes/m1/m1_cycle74_norm_bucket_ladder_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle73_compiled_product_ladder_audit.md
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/BANKED_LEMMAS.md
current_repo_snapshot/CUTS_AND_FALSE_ROUTES.md
current_repo_snapshot/ACTIVE_WALLS.md
```

## Task

Your target is:

```text
V-CYCLE76-RIGHT-HALF-AND-MMAX-CENSUS
W-CYCLE74-DIRECT-MMAX-BUCKET-BOUND
```

Produce one of:

1. An executed certificate, or an actually executable compiled verifier with
   exact schema, for product-only injectivity of right half `{4,5,6,7}`.
2. A compiled/sharded direct max-fiber census plan strong enough to certify
   `m_max(beta)<=12`, with memory/time estimates and exact output schema.
3. An explicit 13-fold collision packet in the constrained domain `P_0`.
4. A proof reducing `m_max<=12` to smaller verified subroutines.

## Hard Rules

- If you cannot execute code, say so and mark code `UNRUN`.
- Do not use `(color, product)` as an equality key.
- Do not use the false t-independent Cycle 70 collapse.
- Do not claim `m_max<=12` without proof or an executed certificate.
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
2. What was actually proved or executed.
3. Certificate or collision details.
4. What remains open.
5. Next exact lemma/construction.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T10-13-45-839Z-cycle76-right-half-mmax-9dded5c6/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---