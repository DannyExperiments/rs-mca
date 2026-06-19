# Cycle 52 Prompt: Balanced Scroll Totally-Split Density

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project files and recent loop material first. Preserve the labels
`PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and
`EXACT_NEW_WALL` literally.

## Current State

The lower/failure branch is banked at source-local level by the
domain-uniform Bessel/pair-rank theorem. The positive/safe-side upper branch is
still open.

Cycles 49-51 converted the upper wall into a value-set question:

1. For `C=RS[F,L,k]`, `r=n-k`, `|T|=j`, and `t=r-j`, the syndrome/Hankel
   condition is

   ```text
   u+zv in W_T  <=>  (H(u)+zH(v)) ell_T = 0,
   ```

   where `ell_T` is the coefficient vector of the monic locator
   `L_T(X)=prod_{x in T}(X-x)`.

2. After quotienting the common core

   ```text
   K0 = ker H(u) cap ker H(v),
   V = F[X]_{<=j}/K0,
   dim V <= 2t,
   ```

   the moving kernels `M_z` are swept by a Kronecker rational scroll of degree
   at most `t`.

3. For each split locator, put

   ```text
   a(T)=H(u)ell_T,
   b(T)=H(v)ell_T.
   ```

   A transverse locator realizes a unique slope iff

   ```text
   b(T) != 0 and rank[a(T)|b(T)] <= 1.
   ```

4. The actual MCA numerator is the distinct slope image

   ```text
   Z(u,v) = #{ z : exists split T with z(T)=z }.
   ```

   It is not the landing count

   ```text
   R(u,v)=sum_z nu(z).
   ```

5. Cycle51 cut the L2 route for safe-side upper bounds. Since

   ```text
   Z >= R^2/M2,
   ```

   L2 anticollision lower-bounds the image. It cannot upper-bound `Z`.

6. Therefore the current live wall is direct value-set counting:

   ```text
   W-MCA-BALANCED-SCROLL-VALUESET-MONODROMY-DENSITY.
   ```

The finite baseline remains

```text
R_line = ceil(binomial(n,k+t)/Q^(t-1)).
```

## Target Wall

```text
W-MCA-BALANCED-SCROLL-TOTALLY-SPLIT-DENSITY
```

Try to prove or refute the following:

> For a transverse balanced right-minimal-index Hankel pencil with quotient
> action-rank defects removed, the density of slopes `z` such that the moving
> fiber `M_z` contains a monic squarefree fully-`L`-split degree-`j` locator is
> at most `1/j+o(1)` in the reserve-scale regime.

Equivalently, prove a direct value-set bound

```text
Z_mov = #{z : M_z cap Proj_V(Split_L^sf) != empty}
        <= R_line + O(j),
```

without passing through the total landing count `R(u,v)` or L2 anticollision.

## Required Output Options

Return one of:

1. `PROOF`: a rigorous totally-split density decay theorem, with finite error
   terms strong enough to imply `Z_mov <= R_line+O(j)`.
2. `COUNTERPACKET`: a source-valid balanced-index, quotient-separated family
   with many distinct slopes, low fiber multiplicity, and
   `Z_mov > R_line+O(j)`.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction to a sharper
   monodromy, resolvent, or finite-field splitting wall.
4. `ROUTE_CUT`: explain why the density formulation is malformed or missing a
   necessary hypothesis.

## Specific Questions

- What is the correct geometric object whose fiber over `z` is
  `M_z cap Proj_V(Split_L^sf)`?
- Is there a natural cover over the `z`-line whose monodromy controls whether a
  fiber contains a fully split locator?
- Can the Cycles 32-38 monodromy/splitting-type machinery be adapted from
  fixed `t,j` to the reserve-scale balanced diagonal?
- Is the heuristic density `<=1/j+o(1)` correct, or should the decay scale be
  different?
- Where exactly do quotient-component packets appear in monodromy language?
- If a counterpacket exists, does it have many distinct slopes with `nu(z)=O(1)`
  rather than just high landing multiplicity?

## Do Not Do

- Do not use L2 anticollision to upper-bound the image.
- Do not use a total landing counterpacket unless it also has many distinct
  slopes.
- Do not ignore quotient-component packets `E | m(X^M)` or bounded-defect
  `d_M(E)`.
- Do not promote this to a final prize solve.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---