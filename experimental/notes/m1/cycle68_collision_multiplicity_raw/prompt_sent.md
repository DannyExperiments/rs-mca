# Cycle 68: Collision Multiplicity Proof / Collision Packet / Verifier

Try to fully solve the target below. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

You are working inside the RS-MCA / Proximity Prize repository context. Follow
the repository labels literally:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Do not promote model-level finite occupancy evidence to a prize-level MCA
theorem or counterpacket. Keep official finite-frontier placement separate.

## Read Order

Read these files first:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle67_cross_color_injectivity_audit.md
current_repo_snapshot/experimental/notes/m1/cycle67_cross_color_injectivity_raw/response.md
current_repo_snapshot/experimental/notes/m1/m1_cycle66_sevenfold_product_occupancy_audit.md
current_repo_snapshot/experimental/scripts/cycle66_occupancy_selfcheck.py
current_repo_snapshot/experimental/notes/m1/m1_cycle65_thickened_gadget_color_audit.md
```

Then use any older context only if needed.

## Banked Setup

The explicit finite model is:

```text
F = F_17[X] / (X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2.
```

Cycle 66 verified:

```text
v_2(17^16 - 1) = 8,
mu_512(F) = mu_256(F),
beta admissible iff beta notin mu_256,
c_7(4)=25152,
|P_0|=25152 * 8^7 = 52,747,567,104.
```

Cycle 67 banked:

```text
Occ(beta) = #{P_T(beta) : T in P_0},
Occ(beta) * m_max(beta) >= |P_0|,
m_max(beta) = max_v #{T in P_0 : P_T(beta)=v}.
```

Therefore:

```text
m_max(beta) <= 12  =>  Occ(beta) >= |P_0|/12
                    = 4,395,630,592
                    > 2^32.
```

This threshold is sharp at this scale:

```text
|P_0|/13 < 2^32.
```

Cycle 67 also banked the shared-jet reduction:

```text
deg(P_T - P_T') <= 107
```

for distinct locators in `P_0`, and a collision is exactly:

```text
(P_T - P_T')(beta) = 0.
```

## Exact Target

Attack:

```text
W-CYCLE67-COLLISION-MULTIPLICITY
```

Prove or kill:

```text
m_max(beta) <= 12.
```

Equivalent failure certificate:

```text
Find 13 distinct tuples T_1,...,T_13 in P_0
with P_{T_1}(beta)=...=P_{T_13}(beta).
```

Equivalent energy target:

```text
E = #{(T,T') in P_0^2 : P_T(beta)=P_T'(beta)}
```

and it is enough to prove:

```text
E <= 12.28 * |P_0|.
```

## What Counts As Success

Any one of the following is valuable:

1. **PROOF:** a structural proof that `m_max(beta) <= 12` for the explicit
   model.
2. **COUNTERPACKET:** an explicit 13-fold collision packet, preferably with
   enough data for Codex to verify locally.
3. **BANKABLE_LEMMA:** a sharper reduction that turns `m_max<=12` into a
   smaller algebraic object, for example a slotwise injectivity theorem, a
   rank/circuit obstruction, or a low-degree relation-lattice certificate.
4. **PLAN with verifier:** an executable bounded-multiplicity verifier design
   that can certify `m_max<=12` without materializing all `>2^32` occupied
   values. Include pseudocode, memory/time estimates, certificate schema, and
   exact self-checks. If feasible, write a prototype or output-file spec.

## What Not To Do

- Do not retry the pure color-class shortcut unless you control full field
  collision multiplicity, not only `Z/16` color.
- Do not claim random-map heuristics as proof.
- Do not claim the full distinct-value count unless actually computed or
  certified.
- Do not turn this model-level wall into an official prize counterpacket.

## Required Output Structure

Start with one of:

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

1. Executive verdict and confidence.
2. Exact theorem, counterpacket, or reduced wall.
3. Proof or failed proof attempt.
4. If computational: exact verifier/certificate design and self-checks.
5. Consequence for `Occ(beta) >= 2^32`.
6. What should be banked.
7. Do you see a route to a full solve? If yes, what is the next exact lemma or
   construction?

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-21-25-677Z-cycle68-collision-multiplicity-bf75bf4d/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---