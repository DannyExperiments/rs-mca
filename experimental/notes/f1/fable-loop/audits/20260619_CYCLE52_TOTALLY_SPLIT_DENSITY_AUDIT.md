# Cycle 52 Totally-Split Density Audit

Status: `ROUTE_CUT / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.

Model/run:

- Model: `claude-opus-4-8`
- Run: `2026-06-19T10-02-44-964Z-cycle52-balanced-scroll-totally-split-density-6d643df3`
- Harness: `OK_WITH_NONFATAL_STREAM_WARNING`; `response.md` and raw JSONL were
  produced. The warning is recorded but not fatal.
- Preserved raw artifacts:
  `raw/cycle52_balanced_scroll_totally_split_density/response.md`,
  `raw/cycle52_balanced_scroll_totally_split_density/raw_response.jsonl`,
  `raw/cycle52_balanced_scroll_totally_split_density/raw_response.json`,
  `raw/cycle52_balanced_scroll_totally_split_density/run_result.json`,
  `raw/cycle52_balanced_scroll_totally_split_density/input_manifest.json`,
  and `raw/cycle52_balanced_scroll_totally_split_density/prompt_sent.md`.
- `output_files/` was empty in the source run.

The answer does **not** prove the safe-side upper theorem and does **not** give
a counterpacket. It cuts the proposed monodromy-density route as malformed for
the actual `L`-supported locator configuration, while preserving a useful
determinantal incidence formulation.

## Verdict

Cycle52 is useful bad news.

The proposed density wall

```text
delta_split <= 1/j+o(1)
```

is not the right object for the reserve-scale MCA upper problem. The `1/j`
totally-split heuristic belongs to a relaxed/free-root or square-regime cover,
not to the fixed finite evaluation-domain locator configuration.

The route returns to the deterministic symmetric-function incidence wall.

## Bankable Lemma A: Discrete Scroll Incidence

Let

```text
Config = Proj_V(Split_L^sf),
S = union_z M_z.
```

Then

```text
I = {(z,T) : ell_T in M_z}
```

is the same as

```text
Config cap S,
```

and projection to the locator side is injective because the moving fibers
`M_z` are pairwise disjoint after quotienting the common core.

Thus:

```text
R(u,v) = #(Config cap S),
Z(u,v) = image size of the ruling map on Config cap S.
```

This is a discrete incidence problem over the fixed set of `binomial(n,j)`
fully `L`-split locators.

## Bankable Lemma B: Symmetric Determinantal Form

For each split locator `T`,

```text
a(T)=H(u)ell_T,
b(T)=H(v)ell_T.
```

The moving-scroll incidence condition is

```text
rank[a(T)|b(T)] <= 1,
b(T) != 0.
```

Equivalently, all minors vanish:

```text
a_i(T)b_l(T)-a_l(T)b_i(T)=0.
```

Since `a(T)` and `b(T)` are linear in the locator coefficients, and locator
coefficients are elementary symmetric functions of `T`, the condition is a
system of degree-2 symmetric equations in the elementary symmetric data of the
selected evaluation points.

This identifies the reduced moving-scroll wall with the Cycle44
symmetric-function incidence wall.

## Route Cut: No `1/j` Monodromy Cover For `Split_L`

A Chebotarev/Lang-Weil monodromy argument needs a positive-dimensional cover
over the `z`-line. The MCA object here is not such a cover. It is a finite
configuration:

```text
Split_L^sf = {monic squarefree locators with all roots in fixed L}.
```

The relaxed problem with roots free in `F` may have a monodromy cover and a
totally-split density such as `1/j`. That is not the same as counting
`L`-supported witness complements.

Thus:

```text
W-MCA-BALANCED-SCROLL-TOTALLY-SPLIT-DENSITY
```

is cut as the wrong formulation for the reserve-scale fixed-domain MCA upper
problem.

## Correct Scale

The right averaged intensity is still

```text
lambda = binomial(n,j)/Q^t,
R_line/Q = binomial(n,j)/Q^t.
```

The proposed `1/j` density is not equivalent to the target

```text
Z_mov <= R_line + O(j).
```

Near the entropy boundary it can be much stronger than the target and
inconsistent with the already banked lower/failure behavior. Therefore it
should not be used as the next exact wall.

## Exact New Wall

Return to:

```text
W-MCA-BALANCED-SCROLL-CONFIG-EQUIDISTRIBUTION
```

Equivalent deterministic incidence statement:

> For a transverse balanced right-minimal-index, quotient-action-rank-separated
> Hankel pencil, prove
>
> ```text
> #{T subset L, |T|=j :
>   rank[H(u)ell_T | H(v)ell_T] <= 1,
>   H(v)ell_T != 0}
> <= R_line + O(j).
> ```

This is stronger than the distinct-slope value-set bound, but in the
above-entropy regime the value-set and landing count should be close unless a
quotient/tangent fiber concentration survives. The proof must be deterministic
and per-line, not averaged over anchors.

## Next Prompt Target

```text
W-MCA-PER-LINE-SYMMETRIC-DETERMINANTAL-INCIDENCE
```

Ask for a proof or counterpacket to the deterministic incidence bound for the
degree-2 symmetric minors, under:

- balanced right minimal indices;
- quotient-action-rank separation;
- tangent/core templates removed;
- fixed smooth multiplicative evaluation domain `L`;
- finite baseline `R_line=ceil(binomial(n,j)/Q^(t-1))`.

A counterpacket must produce many distinct slopes or at least many incidences
not charged to quotient/tangent templates. A monodromy density answer over
free-root locators is not sufficient.
