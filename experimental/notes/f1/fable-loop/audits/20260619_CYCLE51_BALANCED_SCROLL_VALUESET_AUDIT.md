# Cycle 51 Balanced Scroll Value-Set Audit

Status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Model/run:

- Model: `claude-opus-4-8`
- Run: `2026-06-19T09-43-26-682Z-cycle51-balanced-scroll-valueset-vs-landing-fc07aeb3`
- Preserved raw artifacts:
  `raw/cycle51_balanced_scroll_valueset_vs_landing/response.md`,
  `raw/cycle51_balanced_scroll_valueset_vs_landing/raw_response.jsonl`,
  `raw/cycle51_balanced_scroll_valueset_vs_landing/raw_response.json`,
  `raw/cycle51_balanced_scroll_valueset_vs_landing/run_result.json`,
  `raw/cycle51_balanced_scroll_valueset_vs_landing/input_manifest.json`,
  and `raw/cycle51_balanced_scroll_valueset_vs_landing/prompt_sent.md`.
- `output_files/` was empty in the source run.

The answer does **not** prove the value-set bound and does **not** give a
counterpacket. It banks the exact inequality structure separating the distinct
slope image from total landings and cuts the attempted L2 route for safe-side
upper bounds.

## Verdict

Cycle51 is significant route hygiene.

It clarifies that the MCA numerator is the distinct slope image

```text
Z(u,v) = #{z : nu(z) >= 1},
```

not the landing count

```text
R(u,v) = sum_z nu(z).
```

Bounding `R` is sufficient for MCA but stronger than needed. More importantly,
the usual L2 anticollision machinery goes in the wrong direction for an upper
bound on `Z`.

## Bankable Lemma: Moment Sandwich

For

```text
nu(z) = #{T : z(T)=z},
R = sum_z nu(z),
Z = #{z : nu(z)>=1},
M2 = sum_z nu(z)^2,
```

one has the sharp inequalities

```text
Z <= R,
Z >= R^2/M2,
Z >= R/max_z nu(z),
M2 <= R max_z nu(z),
R-Z = sum_z (nu(z)-1)_+.
```

Consequences:

- a landing-count upper bound `R <= R_line+O(j)` implies the MCA numerator
  bound `Z <= R_line+O(j)`;
- an L2 upper bound on `M2` gives a lower bound on `Z`, not an upper bound;
- high landing multiplicity with small image is not a counterpacket to the
  distinct-slope bound.

## Bankable Decomposition

The `O(j)` term belongs to the tangent/core/common-envelope part:

```text
Z = Z_tan + Z_mov,
Z_tan = O(j)
```

by the earlier fixed-core/tangent packet bounds. The moving-scroll part is the
true unresolved piece:

```text
Z_mov = #{z : M_z meets Proj_V(Split_L^sf)}.
```

The finite random-incidence baseline remains

```text
R_line = ceil(binomial(n,k+t)/Q^(t-1)).
```

This is an averaged landing scale, not a deterministic per-line value-set
bound.

## Route Cut

Do not try to prove the safe-side value-set upper theorem using only an L2
anticollision estimate.

Cauchy-Schwarz gives

```text
Z >= R^2/M2.
```

Thus small `M2` pushes `Z` upward. It is the correct direction for the
Cycle44/Cycle47 lower/failure branch, where the goal is to show many slopes.
It is not a proof route for the safe-side upper branch, where the goal is to
show few slopes.

The upper branch needs either:

1. the stronger landing upper bound `R <= R_line+O(j)`; or
2. a direct value-set/splitting-density theorem for `Z`.

## Relation To Cycle44

In the matched residue ledger, Cycle44 and Cycle51 study the same multiplicity
function `nu`.

- Cycle44 uses `M2` to prove a lower bound on support size:
  `Z >= R^2/M2`.
- Cycle51 needs an upper bound on support size:
  `Z <= R_line+O(j)`.

So the L2 anticollision theorem cannot be recycled as the safe-side upper
theorem.

## Exact New Wall

```text
W-MCA-BALANCED-SCROLL-VALUESET-MONODROMY-DENSITY
```

Direct value-set version:

> For a transverse balanced, quotient-action-rank-separated Hankel pencil,
> bound the number of slopes whose moving fiber contains a fully split
> squarefree locator:
>
> ```text
> Z_mov = #{z : M_z cap Proj_V(Split_L^sf) != empty}
>        <= R_line + O(j).
> ```

The proposed route is monodromy/splitting-density, not L2:

```text
Z_mov = Q * delta_split(P) + error,
delta_split(P) <= 1/j + o(1)
```

after quotient and tangent templates are removed.

## Next Prompt Target

```text
W-MCA-BALANCED-SCROLL-TOTALLY-SPLIT-DENSITY
```

Ask for a proof or counterpacket to the density-decay claim:

```text
For a balanced quotient-separated moving scroll, the density of slopes whose
fiber contains a fully L-split squarefree locator is <= 1/j+o(1).
```

A counterpacket must have many distinct slopes and low fiber multiplicity. A
large landing count concentrated on few slopes is not sufficient.
