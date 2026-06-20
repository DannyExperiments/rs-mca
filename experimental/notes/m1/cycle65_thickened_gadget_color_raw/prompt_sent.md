# Cycle 65 Prompt - Thickened Gadget Color Occupancy

You are a theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve the assigned wall. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do not brainstorm from scratch. This prompt follows Cycle 64.

## Current Situation

Cycle 64 banked the exact prefix-collision gadget convolution and cut its
use as a scalar smallness certificate.

Banked from Cycle 64:

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-CONVOLUTION
```

The Role 05 characteristic-17 near-split packet is absorbed descriptively by
seven local gadget-class enumerators plus one marker:

```text
F_0 = F_{17^16}
H_0 = mu_256
sigma = 6
j = 113
K = <eta^8>, |K| = 32
W_t(Y) = 8 Y^t (Y^1 + Y^4 + Y^7 + Y^9 + Y^12 + Y^15)
[Y^0] prod_{t=1}^7 W_t(Y) = 52,747,567,104 > 2^32.
```

Cycle 64 also proves the route cut:

```text
total prefix-gadget charge = scalar support mass.
```

Therefore prefix gadgets do not by themselves prove scalar-list smallness.
The next prize-relevant object is thickened MCA color occupancy.

## Read Order

Read from the project source copy:

1. `current_repo_snapshot/experimental/notes/m1/m1_cycle64_prefix_collision_gadget_audit.md`
2. `current_repo_snapshot/experimental/notes/m1/cycle64_prefix_collision_gadget_raw/response.md`
3. `current_repo_snapshot/experimental/notes/m1/m1_cycle64_local_prefix_gadget_scout.md`
4. `current_repo_snapshot/experimental/notes/m1/m1_cycle63_round2_audit.md`
5. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/05_role05_near_split_collision_mass.md`
6. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/08_role08_t1_color_transfer.md`
7. `current_repo_snapshot/experimental/notes/m1/m1_cycle62_round1_audit.md`
8. `current_repo_snapshot/experimental/notes/m1/cycle62_round1_raw/05_role05_t1_mca_gj_color_result.md` if present; otherwise use the Cycle 62 audit's Role 05 summary.
9. Main source only as needed:
   - `current_repo_snapshot/tex/slackMCA_v3.tex`
   - `current_repo_snapshot/tex/RS_disproof_v3.tex`
   - `current_repo_snapshot/tex/cs25_cap_v4.tex`
   - `current_repo_snapshot/tex/snarks_v4.tex`

Treat planning/referee files as `AUDIT / PLAN / CONDITIONAL`, not proof,
unless a later audit explicitly banks the claim.

## Target Wall

Prove or kill:

```text
W-MODEL-GJ-THICKENED-GADGET-COLOR-OCCUPANCY
```

Cycle 64 defines the thickened color map for

```text
Delta^+ = Delta + [beta]
```

as

```text
rho_beta(T) = prod_{x in T}(beta - x).
```

For the Role 05 packet, one must push the seven gadget enumerators by
`rho_beta` and count occupied colors, not mass:

```text
Occ(b_0) =
|supp of the pushed sevenfold product at the fixed scalar boundary b_0|.
```

The concrete finite falsifier/check is:

1. Work in the Role 05 model over `F_{17^16}` with `H=mu_256`, `K=<eta^8>`,
   and `eta^16=3` as given in Role 05.
2. For each active coset `t=1,...,7`, compute or characterize the 48 values

```text
v_{t,A} = prod_{x in eta^t A~}(beta - x)
        = E_{eta^t A~}(1/beta) beta^16.
```

3. Count or sharply bound the number of distinct sevenfold products

```text
prod_{t=1}^7 v_{t,A_t}
```

subject to the product-color constraint from Role 05.

4. Decide whether this occupied-color count is large enough to cut the
scalar-apolar-to-`t=1` MCA spine at the model level, or whether a hidden
identity collapses these colors so the packet is absorbed.

## Hard Requirements

- Keep support mass and occupied thickened colors separate.
- Do not use `n^{1+o(1)}` as a finite prize certificate.
- Do not promote the model packet to an official prize counterpacket unless
  finite frontier placement is also established.
- If you claim occupancy is large, give an exact finite construction, lower
  bound, or verifier specification strong enough for Codex/PRZ to implement.
- If you claim occupancy collapses, state the exact identity causing collapse.
- If the result depends on the choice of `beta`, state whether it holds for
  generic `beta`, all `beta notin H`, or only an explicit admissible `beta`.
- Keep scalar-list, `t=1` MCA, and full MCA claims separated.
- If the Role 05 field model is underspecified, state the missing data exactly
  and give a model-independent theorem in terms of the 48 local states.

## Desired Outcomes

One of the following is acceptable:

1. `COUNTERPACKET`: the Role 05 thickened colors are numerous, giving a
   model-level `t=1` MCA color obstruction.
2. `BANKABLE_LEMMA`: a collapse theorem shows the thickened color support is
   controlled by product color / norm / trace / another explicit invariant.
3. `ROUTE_CUT`: the problem cannot be decided from the current packet because
   required field/`beta` data are absent; state exactly what finite verifier
   or source datum is needed.
4. `EXACT_NEW_WALL`: reduce the problem to a smaller named finite algebraic
   object, such as a sevenfold product-set lower bound in a cyclic or
   generalized-Jacobian color group.

## Required Output Format

Start with exactly one of:

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
2. Formal theorem, reduction, or counterpacket statement.
3. Full proof/construction, with edge cases.
4. Parameter ledger and finite relevance.
5. What is bankable versus conditional.
6. Failure point if unresolved.
7. The next exact lemma or construction.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T06-28-17-528Z-cycle65-thickened-gadget-color-occupancy-80b449fb/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---