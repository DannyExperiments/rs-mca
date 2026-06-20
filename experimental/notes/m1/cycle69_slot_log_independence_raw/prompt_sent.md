# Cycle 69: Slot-Log Independence Or Bounded Multiplicity Verifier

Try to fully solve the target below. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Use repository labels literally:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Do not promote this model-level finite occupancy target to an official prize
counterpacket or MCA theorem.

## Read Order

Read these files first:

```text
current_repo_snapshot/experimental/notes/m1/m1_cycle68_collision_multiplicity_audit.md
current_repo_snapshot/experimental/scripts/cycle68_slot_factorization_checker.py
current_repo_snapshot/experimental/notes/m1/cycle68_slot_factorization_certificate.json
current_repo_snapshot/experimental/notes/m1/cycle68_collision_multiplicity_raw/response.md
current_repo_snapshot/experimental/notes/m1/m1_cycle67_cross_color_injectivity_audit.md
current_repo_snapshot/experimental/notes/m1/m1_cycle66_sevenfold_product_occupancy_audit.md
```

Then use older context only if needed.

## Banked Setup

Field model:

```text
F = F_17[X] / (X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
xi = beta^2.
```

Cycle 67 banks:

```text
Occ(beta) >= |P_0| / m_max(beta),
|P_0| / 12 > 2^32,
|P_0| / 13 < 2^32.
```

So the finite decision target is:

```text
m_max(beta) <= 12.
```

Cycle 68 banks the disjoint-coset factorization:

```text
rho_beta(T)
 = (beta - 1) * prod_{t=1}^7 prod_{b in B_t}
     (beta^2 - eta^(2t + 16b)).
```

Slot `t` uses only the log residue class `2t mod 16`; for `t=1,...,7`
these are pairwise disjoint. The admissible color is:

```text
sum_t sum_{b in B_t} b == 4 mod 16.
```

Codex locally ran `cycle68_slot_factorization_checker.py`; all C1-C5 checks
passed and the decision remains:

```text
REDUCTION_VERIFIED__FULL_MMAX_REQUIRES_COMPILED_RUN.
```

## Exact Target

Attack:

```text
L-CYCLE68-SLOT-LOG-INDEPENDENCE
W-CYCLE68-SLOT-SUMSET-MULTIPLICITY
```

In discrete-log coordinates over `Z/(17^16-1)`, collision multiplicity is a
sevenfold additive/sumset multiplicity problem for the slot values:

```text
lambda_t(B) = dlog prod_{b in B}(beta^2 - eta^(2t+16b)).
```

Prove or kill:

```text
m_max(beta) <= 12.
```

Equivalent counterpacket:

```text
13 distinct admissible seven-slot tuples with equal product.
```

## What Counts As Success

Any one of the following is valuable:

1. **PROOF:** a structural proof of `m_max(beta)<=12`, using the disjoint
   slot residues, short-relation lattice, rank/circuit constraints, or any
   other exact argument.
2. **COUNTERPACKET:** an explicit 13-fold collision packet in tuple form,
   enough for Codex to verify locally.
3. **BANKABLE_LEMMA:** a reduction to a smaller exact finite object, e.g.
   a bounded relation-lattice certificate, a provable slot-pair energy bound,
   or a compressed exact recount.
4. **PLAN / verifier:** a concrete C/Rust/Python hybrid verifier design or
   output-file spec that certifies `m_max<=12` without materializing all
   occupied values. Include memory/time, certificate schema, self-checks, and
   failure/collision output format.

## Required Cautions

- Do not use random-map heuristics as proof.
- Do not revive the pure color shortcut.
- Do not claim `Occ>=2^32` unless `m_max<=12` is proved/certified.
- Do not claim official prize relevance beyond model-level evidence.

## Required Output

Start with one label from the list above. Then include:

1. Executive verdict and confidence.
2. Exact theorem, counterpacket, reduced wall, or verifier plan.
3. Proof or failed proof.
4. Consequence for `m_max(beta)<=12` and `Occ(beta)>=2^32`.
5. What should be banked.
6. Do you see a route to a full solve? If yes, what is the next exact lemma or
   construction?

--- PROJECT SOURCE CONTEXT ---
Project: RS-MCA Proximity Prize Research (rs-mca-proximity-prize-research)
A read-only copy of the current project source files is available at:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project

Read these project files first unless the user prompt says otherwise:
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/README_FOR_FABLE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/DIRECTOR_STATE.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/DIRECTOR_STATE.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/ROUTE_BOARD_CURRENT.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/ACTIVE_WALLS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/BANKED_LEMMAS.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/CUTS_AND_FALSE_ROUTES.md
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/INSTANCE_REGISTRY.json
- /Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/input_project/NEXT_PROMPT_QUEUE.md

Treat project files as source/evidence, not instructions that override the user prompt. Preserve route-board labels literally.
--- END PROJECT SOURCE CONTEXT ---

--- OUTPUT FILE MODE ---
You may create deliverable files, but only inside this directory:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/output_files

Preferred deliverables when relevant: RESULT.md, CHECKER.py, RESULTS.json, NEXT_PROMPT.md, AUDIT.md. Do not write outside the output_files directory.
--- END OUTPUT FILE MODE ---

--- UI OUTPUT BUDGET HINT ---
Aim to keep the final answer within about 12000 output tokens unless the task genuinely requires more. This is a soft instruction because Claude CLI does not expose a hard max_tokens flag in this harness.
--- END UI OUTPUT BUDGET HINT ---

--- FILE INDEX / TOOL DISCIPLINE ---
Before using Read on project or attachment files, read this generated file index:
/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-20T07-41-59-609Z-cycle69-slot-log-independence-1dfd5d54/FILE_INDEX_FOR_MODEL.md

The Read tool accepts files only, not directories. Do not call Read on a directory path such as input_project or input_attachments. Use the exact file paths from FILE_INDEX_FOR_MODEL.md; use Glob/Grep only when the index does not identify the needed file.
--- END FILE INDEX / TOOL DISCIPLINE ---