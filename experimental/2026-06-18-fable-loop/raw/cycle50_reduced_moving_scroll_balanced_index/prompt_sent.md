# Cycle 50 Prompt: Reduced Moving-Scroll Balanced-Index Incidence

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project files and recent loop material first. Preserve the labels
`PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and
`EXACT_NEW_WALL` literally.

## Context

The current state after Cycles 47-49 is:

1. **Lower/failure branch:** the domain-uniform Bessel/pair-rank theorem is
   banked at source-local level. For smooth multiplicative domains and
   `E=X^t`, the random-anchor construction gives MCA failure throughout the
   strict entropy-subcritical range `c < H_2(rho)`.

2. **Upper branch is not solved.** Cycle48 cut the naive matching upper theorem:
   literal quotient-pullback exclusion is too narrow. Quotient-component
   denominators with `E | m(X^M)` and fixed-defect quotient anchors produce
   large clouds unless charged by a broader quotient invariant such as
   `d_M(E)=deg minpoly([X^M]_E)`.

3. **Cycle49 reformulated the upper wall in syndrome/Hankel coordinates.**
   For `C=RS[F,L,k]`, `r=n-k`, `|T|=j`, and `t=r-j`, define the Hankel matrix
   of a syndrome `w in F^r` by

   ```text
   H(w)_{m,l} = w_{m+l},  0 <= m < t, 0 <= l <= j.
   ```

   If `ell_T` is the coefficient vector of the monic locator
   `L_T(X)=prod_{x in T}(X-x)`, then

   ```text
   u+zv in W_T  <=>  (H(u)+zH(v)) ell_T = 0.
   ```

   Transversality is `H(v)ell_T != 0`.

4. **Cycle49 core/moving reduction.** Let

   ```text
   K0 = ker H(u) cap ker H(v).
   V = F[X]_{<=j}/K0.
   ```

   Then `dim V <= 2t`; after quotienting by `K0`, the moving kernels `M_z`
   have dimension `<=t` and are swept by a Kronecker rational scroll of degree
   at most `t`. The common core accounts for contained/tangent/common-envelope
   behavior. The moving part contains the quotient-component obstruction.

5. **Finite accounting must retain**

   ```text
   R_line = ceil(binomial(n,k+t) / Q^(t-1)).
   ```

   A bare `n^{1+o(1)}` bound just above the entropy equality is not the
   correct finite statement.

The active wall is:

```text
W-MCA-REDUCED-MOVING-SCROLL-INCIDENCE
```

## Your Target

Attack the first genuinely aperiodic subwall:

```text
W-MCA-REDUCED-MOVING-SCROLL-BALANCED-INDEX
```

Here is the candidate lemma:

> Let `L` be a smooth multiplicative Reed-Solomon evaluation domain,
> `C=RS[F,L,k]`, and let `H(u)+zH(v)` be a Hankel pencil as above. Suppose:
>
> - the intrinsic common core `K0=ker H(u) cap ker H(v)` has been quotiented;
> - contained/tangent/common-envelope incidences have been removed;
> - the selected incidences are transverse;
> - the pencil has right Kronecker minimal indices all within `1` of each
>   other, so there is no unbalanced quotient-component scroll;
> - no proper quotient-action-rank defect occurs, meaning for every proper
>   quotient scale `M`, the projected split-locator configuration is not
>   collapsed by `X^M` and the moving scroll is not aligned with low
>   `d_M(E)`.
>
> Prove, or refute by source-valid counterpacket, that
>
> ```text
> #{ z : M_z cap Proj_V(Split_L^sf) != empty } <= R_line + (j+1).
> ```

This is deliberately narrower than the whole grand upper theorem. I want the
balanced-index case only.

## Required Output

Return one of:

1. `PROOF`: a rigorous proof of the balanced-index incidence bound.
2. `COUNTERPACKET`: an explicit source-valid family exceeding
   `R_line+(j+1)` while satisfying the balanced-index and quotient-separated
   hypotheses.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: if the full statement is still open,
   give the sharpest exact lemma that reduces it further, and name the next
   wall.
4. `ROUTE_CUT`: if the statement is malformed, explain precisely which
   hypothesis is wrong or insufficient.

## Things To Check Explicitly

- Does "balanced right minimal indices" actually exclude the Cycle48
  quotient-component packets, including `E | m(X^M)` and punctured-fiber
  coequalizers?
- Can a balanced-index scroll still contain many projected split locators by a
  nonquotient mechanism?
- Is the `R_line` term the correct random/incidence baseline in the reduced
  `<=2t`-dimensional moving space?
- Does the statement need squarefree/fully split locator hypotheses beyond
  `Proj_V(Split_L^sf)`?
- Is there a finite exact version, not just an asymptotic one?

## Do Not Do

- Do not promote this to a protocol, SNARK, prize, or final grand-MCA solve.
- Do not ignore `t<sigma` or `t>sigma`; explain why the Hankel `t=r-j`
  formulation either covers them or why another wall remains.
- Do not use raw arbitrary locator-fiber counts as list bounds.
- Do not collapse `q_gen`, `q_line`, and the syndrome field unless the source
  ledger actually permits it.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---