# Cycle 71 Prompt: Optimized K3/K4 Ladder Run Or Partial Collision

Try to fully solve the stated target. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

This is a narrow finite/model target. Do not brainstorm broadly.

## Read Order

Read these files from the project source snapshot first:

1. `ACTIVE_WALLS.md`
2. `CUTS_AND_FALSE_ROUTES.md`
3. `current_repo_snapshot/experimental/notes/m1/m1_cycle70_k3_k4_ladder_audit.md`
4. `current_repo_snapshot/experimental/scripts/cycle70_slot_normalization_checker.py`
5. `current_repo_snapshot/experimental/notes/m1/cycle70_slot_normalization_certificate.json`
6. `current_repo_snapshot/experimental/notes/m1/m1_cycle69_slot_log_independence_audit.md`
7. `current_repo_snapshot/experimental/scripts/cycle69_ladder_probe.py`
8. `current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py`
9. `current_repo_snapshot/experimental/notes/m1/cycle70_k3_k4_ladder_raw/response.md`

## Current State

Cycle 69 banked:

```text
D <= 155 => m_max(beta) <= 12 => Occ(beta) >= |P_0|/12 > 2^32.
```

Cycle 69/Codex locally verified product-injectivity through `k=2`.

Cycle 70 did not close `k=3/k=4`. It also proposed the false t-independent
collapse:

```text
u_t(i,a) = prod_{c in 3^a D_i}(beta^2-c).
```

Codex cut this with a local counterexample at `(t,i,a)=(1,1,0)`.

The surviving exact identity is:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

Do not reuse the false t-independent collapse.

## Your Task

Primary target:

```text
V-CYCLE70-K3-K4-OPTIMIZED-LADDER-RUN
```

Give one of:

1. an optimized exact verifier for product-injectivity of all `k=3` and `k=4`
   slot subsets, preferably executable as Python+NumPy, C, Rust, or another
   precise compiled path;
2. a structural proof of `k=3/k=4` injectivity that does not rely on the false
   Cycle 70 collapse;
3. an explicit partial collision if any rung fails, including slots, keys, and
   product value, checkable against `cycle68_slot_factorization_checker.py`.

Secondary target:

```text
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

If you can push beyond the ladder, give one of:

1. a proof of `D <= 155`;
2. an explicit 13-fold collision;
3. an exact heavy-bucket / external-sort / compiled collision-energy verifier
   with certificate schema.

## Required Output

Start with exactly one label:

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

1. **Executive verdict.** Is `k=3/k=4` proved, falsified, or still open?
2. **Use of Cycle 70 cut.** Explicitly state that the t-independent collapse is
   false and that your argument/code avoids it.
3. **Exact code or proof.** If code, provide self-contained source or a patch
   against existing scripts. If proof, give a line-by-line finite algebra
   argument. If collision, give direct check data.
4. **Certificate schema.** State exact JSON fields for independent validation.
5. **Energy implication.** State what follows for support size, `D`, `m_max`,
   and `Occ(beta)`.
6. **Next exact lemma/construction.** Answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Guardrails

- Do not claim the prize problem is solved.
- Do not promote this finite model to an MCA theorem.
- Do not use probabilistic evidence as proof.
- Do not use the false Cycle 70 t-independent collapse.
- If computation is still too large, name the first bottleneck and give the
  smallest exact verifier that would break it.

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T08-35-43-418Z-cycle71-optimized-ladder-run-3584358e/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---