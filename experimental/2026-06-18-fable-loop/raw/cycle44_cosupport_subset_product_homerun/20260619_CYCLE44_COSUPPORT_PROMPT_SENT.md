# Cycle 44 Homerun Prompt: Cosupport Subset-Product Equidistribution

Try to fully solve the reserve lift through the cosupport subset-product /
equidistribution wall. If you cannot fully solve it, progress it as much as
possible by reducing it to the next exact lemma, obstruction, or falsifier. No
Internet.

Take all the time to reason you need. Use MAX reasoning. Do not optimize for a
quick audit. Work as a skeptical mathematical co-director trying to crack the
actual wall.

Work only from mounted repository/context files. Do not use web access. Keep
these ledgers separate:

- `q_gen`
- `q_line`
- `q_chal`
- `B`
- `F`

Do not promote any statement to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, prize, or final `COUNTERPACKET`
status unless the exact source hypotheses are proved.

## Current Target

Attack exactly:

```text
W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION
```

Cycle 42 banked a restricted fixed local closure:

```text
q_gen = p,
B = F_p,
F = F_{p^2},
q_line = p^2,
D = F_p,
t = sigma = 2,
j = 4,
N_split(p) = p^2/24 + O(p^(3/2)).
```

Cycle 43 then cut the literal route of directly amplifying that fixed
`t=2,j=4` quartic/S4 mechanism to reserve scale. The fixed branch is the
square point `j=2t`; reserve scale has

```text
t = sigma = Theta(n/log n),
j = Theta(n),
j >> 2t.
```

So the reserve-scale object is not a single square Cramer/quartic monodromy
problem. Cycle 43 redirected the wall to cosupport landing:

```text
rho(T) = [I_{D\T}]_E,
Land = {T : rho(T) in F*b},
Slopes = {z in F : exists T, rho(T)=z b}.
```

The route skeleton is:

```text
N_split <= #Land(j,t),
#Land(j,t) heuristically ~ binom(p,j)/p^{2(t-1)},
N_split heuristically ~ min(q_line, binom(p,j)/p^{2(t-1)}).
```

This matches the banked fixed regimes:

```text
j=2,t=2 -> O(1);
j=3,t=2 -> O(p);
j=4,t=2 -> p^2/24 + lower terms.
```

But the reserve-scale cancellation/equidistribution theorem is not proved.

## Read First

Read these files before answering:

- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `ROUTE_BOARD_CURRENT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE41_CHAR0DELTA_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`

Use `.tex` source files only if you need exact source hypotheses or
definitions. Do not infer generated-field, corrected-reserve, or protocol
conclusions from the restricted branch without checking the source definitions.

## The Mathematical Wall

The live object is cancellation / decoupling / anticollision for subset-product
moments such as

```text
e_j({chi(xi-d)}_{d in F_p}),
xi = [X]_E,
chi nontrivial on (F[X]/E)^*.
```

The target reserve lift would require a source-valid growing-degree family

```text
deg E = t = sigma >= C n/log n,
j = Theta(n),
E has no roots on D=F_p,
source-valid separated denominator/cosupport data,
positive noncontained split-slope density or a comparable reserve-scale
lower bound.
```

## Required Mathematical Decision

Give the strongest source-grounded result you can justify. One of these would
be valuable:

1. **PROOF / BANKABLE_LEMMA:** prove a reserve-scale lift through cosupport
   subset-product equidistribution. Construct a source-valid growing-degree
   denominator/cosupport family and prove enough landing equidistribution and
   slope anticollision to get positive noncontained split-slope density, or the
   strongest reserve-scale lower bound available.
2. **BANKABLE_LEMMA / EXACT_NEW_WALL:** reduce the reserve lift to one precise
   theorem-sized lemma. Examples: cancellation in
   `e_j({chi(xi-d)})`, quotient decoupling for `[I_{D\T}]_E`, a maximum landing
   multiplicity bound, a Hilbert/Chebotarev uniformity statement over the
   cosupport surface, or a separated-family construction lemma.
3. **ROUTE_CUT:** prove a theorem-sized obstruction showing that the
   cosupport subset-product route cannot give reserve-scale progress. Examples:
   unavoidable character-sum bias, landing multiplicity collapse, slope
   containment, generated-field ledger collision, or source-validity failure
   for all growing-degree denominator families.
4. **COUNTERPACKET:** only if every original corrected-reserve/source
   hypothesis is actually checked. Do not use this label speculatively.

If a proof is out of reach, name the smallest exact missing object below
`W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`. I want the next
prompt to be aimed at a concrete lemma or falsifier, not at a vague wall.

## Optional Finite/Computational Lens

If a finite check is the fastest way to falsify or sharpen the wall, specify it
precisely. A useful starter experiment is:

```text
fix t=2,
sweep j=4,5,6,...,
p in {23,31,43},
measure #Land, |Slopes|/p^2, and max_z #{T in Land : rho(T)=z b}.
```

Finite data are evidence or falsifiers only; they are not proof unless the
source-valid symbolic theorem is also supplied.

If you can write deliverables, write only under `output_files/`.

Preferred deliverables:

- `output_files/cycle44_cosupport_result.md`
- `output_files/cycle44_next_lemma_or_falsifier.md`
- `output_files/cycle44_finite_checker_spec.md`
- `output_files/cycle44_next_prompt.md`

Use these labels literally:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `EXPERIMENTAL`

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---