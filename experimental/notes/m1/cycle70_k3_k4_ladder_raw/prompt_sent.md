# Cycle 70 Prompt: K3/K4 Injectivity Ladder Or Collision Energy

Try to fully solve the stated target. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do not brainstorm broadly. This is a narrow finite/model target under the
Cycle 66-69 scalar-apolar route. Preserve proof/counterexample discipline.

## Read Order

Read these files from the project source snapshot first:

1. `current_repo_snapshot/experimental/notes/m1/m1_cycle69_slot_log_independence_audit.md`
2. `current_repo_snapshot/experimental/scripts/cycle69_ladder_probe.py`
3. `current_repo_snapshot/experimental/notes/m1/cycle69_ladder_probe_certificate.json`
4. `current_repo_snapshot/experimental/notes/m1/m1_cycle68_collision_multiplicity_audit.md`
5. `current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py`
6. `current_repo_snapshot/experimental/notes/m1/cycle68_slot_factorization_certificate.json`
7. `current_repo_snapshot/experimental/notes/m1/cycle69_slot_log_independence_raw/response.md`
8. `ACTIVE_WALLS.md`
9. `BANKED_LEMMAS.md`

## Current Banked State

Cycle 68 banked the disjoint-coset factorization for the explicit finite model:

```text
rho_beta(T) = (beta - 1) prod_{t=1}^7 prod_{b in B_t}
  (beta^2 - eta^(2t + 16b)).
```

The model is:

```text
F = F_17[X]/(X^16 + X^8 + 3)
eta = 6 X^9
beta = X + 2
```

There are seven slots. Each slot has 48 options: three four-subset patterns
and sixteen rotations. The admissible set `P_0` has

```text
|P_0| = 52,747,567,104.
```

The decision target is still:

```text
m_max(beta) <= 12.
```

Cycle 69 banked the energy-to-multiplicity gate. Let

```text
m_v = #{T in P_0 : prod_t u_t(B_t)=v},
m_max = max_v m_v,
E = sum_v m_v^2,
D = E - |P_0| = sum_v m_v(m_v-1).
```

Then

```text
m_max(m_max - 1) <= D.
D <= 155 => m_max <= 12 => Occ(beta) >= |P_0|/12 > 2^32.
```

A 13-fold collision contributes at least `13*12=156` to the ordered
off-diagonal collision count `D`, so this threshold is sharp for the present
frontier.

Cycle 69 also banked the injectivity ladder:

```text
If every k-subset of slots is product-injective, every full collision has
slot support at least k+1.
```

Codex locally verified:

```text
k=1 product-injective: true
k=2 product-injective: true
slot complement oracle checks: 336
```

A pure-Python `k=3` run was attempted and interrupted for performance reasons.
That is not evidence of a collision.

## Your Task

Primary target:

```text
V-CYCLE69-K3-K4-INJECTIVITY-LADDER
```

Prove or kill product-injectivity for all `k=3` and `k=4` slot subsets.

You may proceed by:

1. a structural proof using the explicit field/table definitions;
2. an optimized exact verifier that is feasible on this finite instance;
3. an explicit partial collision if a rung fails.

Secondary target:

```text
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

If the ladder passes through `k=4`, push to one of:

1. prove `D <= 155`;
2. give an exact compiled verifier design/code path for `D`;
3. find an explicit 13-fold collision;
4. prove a support-5 collision-energy bound sufficient for `D <= 155`.

## Required Output

Start with exactly one verdict label:

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

1. **Executive verdict.** State whether `k=3/k=4` product-injectivity is proved,
   falsified, or still open.
2. **Exact finite model.** Restate the field, `eta`, `beta`, table, and
   admissibility constraints you actually used.
3. **Proof or counterpacket.** If a rung fails, give the explicit slots, keys,
   and product value. If it passes, give a proof or verifier certificate strong
   enough for independent reproduction.
4. **Energy consequence.** State exactly what this implies for collision
   support size, `D`, `m_max`, and `Occ(beta)`.
5. **Scripts/checkers.** If you propose code, make it self-contained or give a
   precise patch against the existing scripts. Include certificate schema.
6. **Next exact lemma/construction.** Answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Guardrails

- Do not claim the prize problem is solved.
- Do not promote this model calculation to an MCA theorem.
- Do not reuse the pure color shortcut unless it controls full-field product
  multiplicity.
- Do not report probabilistic evidence as proof.
- If a computation is too large, reduce it to a precise exact verifier plan and
  identify the first bottleneck.
- If you find a collision, make it directly checkable against
  `cycle68_slot_factorization_checker.py`.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-06-59-399Z-cycle70-k3-k4-ladder-f3125801/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---