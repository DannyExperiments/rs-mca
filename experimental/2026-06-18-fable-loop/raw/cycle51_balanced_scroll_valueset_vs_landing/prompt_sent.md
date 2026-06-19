# Cycle 51 Prompt: Balanced Scroll Value Set vs Landing Count

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project files and recent loop material first. Preserve the labels
`PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and
`EXACT_NEW_WALL` literally.

## Current Route State

Cycles 47-50 established the following source-local picture:

1. The lower/failure branch is banked at theorem-candidate level:
   domain-uniform Bessel/pair-rank gives smooth-domain scalar MCA failure in
   the strict entropy-subcritical range `c < H_2(rho)`.

2. Cycle48 cut the naive positive upper route. Literal quotient-pullback
   exclusion is too narrow. Quotient-component denominators with
   `E | m(X^M)` and fixed-defect quotient anchors must be charged by broader
   quotient-action invariants, e.g.

   ```text
   d_M(E) = deg minpoly([X^M]_E).
   ```

3. Cycle49 reformulated the upper wall exactly in syndrome/Hankel coordinates.
   For `C=RS[F,L,k]`, `r=n-k`, `|T|=j`, `t=r-j`, and syndrome vector `w`,

   ```text
   H(w)_{m,l} = w_{m+l},  0 <= m < t, 0 <= l <= j.
   ```

   If `ell_T` is the coefficient vector of the monic locator
   `L_T(X)=prod_{x in T}(X-x)`, then

   ```text
   u+zv in W_T  <=>  (H(u)+zH(v)) ell_T = 0.
   ```

4. Cycle49 also gave the core/moving reduction:

   ```text
   K0 = ker H(u) cap ker H(v),
   V = F[X]_{<=j}/K0,
   dim V <= 2t.
   ```

   The moving kernels `M_z` are swept by a Kronecker rational scroll of degree
   at most `t`.

5. Cycle50 banked the rank-one value-map formulation. For each split locator,

   ```text
   a(T)=H(u)ell_T,
   b(T)=H(v)ell_T.
   ```

   A transverse locator realizes a unique slope iff

   ```text
   b(T) != 0 and rank[a(T)|b(T)] <= 1.
   ```

   The actual MCA numerator is the distinct value set

   ```text
   Z(u,v) = #{ z(T) : T split, b(T)!=0, rank[a(T)|b(T)]<=1 }.
   ```

   The total landing count is

   ```text
   R(u,v) = #{ T split : b(T)!=0, rank[a(T)|b(T)]<=1 }.
   ```

   Always `Z(u,v) <= R(u,v)`, but they are not equivalent.

6. The finite random-incidence baseline is

   ```text
   R_line = ceil(binomial(n,k+t) / Q^(t-1)).
   ```

   Do not replace it by a bare `n^{1+o(1)}` near the entropy boundary.

## Active Wall

```text
W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING
```

The Cycle50 audit corrected a possible overclaim: bounding total landings
`R(u,v)` is sufficient but stronger than bounding the actual MCA numerator
`Z(u,v)`.

## Your Task

Resolve, sharpen, or refute the value-set version.

Assume a fixed transverse Hankel pencil `H(u)+zH(v)` satisfying:

- the common core `K0=ker H(u) cap ker H(v)` has been quotiented or charged to
  tangent/common-envelope templates;
- all selected incidences are transverse (`b(T)!=0`);
- right Kronecker minimal indices are balanced, e.g. all nonzero indices are
  `1` or all indices differ by at most `1`;
- proper quotient-action-rank defects are excluded, including bounded-defect
  quotient-component packets, not only syntactic pullbacks;
- locators are monic, squarefree, fully split over the evaluation domain
  `L`.

Prove or refute:

```text
Z(u,v) <= R_line + O(j)
```

with a finite version strong enough to imply the safe-side MCA numerator.

You may instead prove the stronger sufficient statement:

```text
R(u,v) <= R_line + O(j),
```

but if you do, explicitly state that it is stronger than the required MCA
value-set bound.

## Required Output Options

Return one of:

1. `PROOF`: rigorous value-set bound for `Z(u,v)`.
2. `PROOF`: rigorous stronger landing bound for `R(u,v)`, with the distinction
   from `Z(u,v)` made explicit.
3. `COUNTERPACKET`: a source-valid balanced-index, quotient-separated family
   with `Z(u,v) > R_line + O(j)`. A high landing multiplicity with small
   distinct slope image is **not** enough.
4. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction to a sharper named
   wall.
5. `ROUTE_CUT`: explain why the value-set formulation is malformed or missing
   an essential hypothesis.

## Specific Questions To Answer

- Is `Z(u,v) <= R_line+O(j)` strictly easier than `R(u,v)<=R_line+O(j)` in this
  setting, or does quotient/tangent separation make them essentially
  equivalent?
- Can balanced Kronecker index plus quotient-action-rank separation force
  slope fibers `nu(z)` to be small enough that image and landing count are
  comparable?
- Does a per-line `L2` bound help upper-bound `Z(u,v)`, or only lower-bound it
  through Cauchy-Schwarz? Be precise.
- What is the exact counterpacket target if the bound is false?
- How does this relate back to the Cycle44 fixed-anchor anticollision wall?

## Do Not Do

- Do not claim that an averaged random-anchor first or second moment proves a
  deterministic per-line upper bound.
- Do not use a total landing counterpacket as a value-set counterpacket unless
  it also has many distinct slopes.
- Do not ignore quotient-component packets `E | m(X^M)` or bounded-defect
  `d_M(E)`.
- Do not promote this to a final prize solve, protocol result, SNARK result, or
  generated-field theorem.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---