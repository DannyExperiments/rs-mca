# Cycle 50 Reduced Moving-Scroll Balanced-Index Audit

Status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Model/run:

- Model: `claude-opus-4-8`
- Run: `2026-06-19T09-06-20-338Z-cycle50-reduced-moving-scroll-balanced-index-b896e1af`
- Preserved raw artifacts:
  `raw/cycle50_reduced_moving_scroll_balanced_index/response.md`,
  `raw/cycle50_reduced_moving_scroll_balanced_index/raw_response.jsonl`,
  `raw/cycle50_reduced_moving_scroll_balanced_index/raw_response.json`,
  `raw/cycle50_reduced_moving_scroll_balanced_index/run_result.json`,
  `raw/cycle50_reduced_moving_scroll_balanced_index/input_manifest.json`,
  and `raw/cycle50_reduced_moving_scroll_balanced_index/prompt_sent.md`.
- `output_files/` was empty in the source run.

The answer explicitly does **not** claim `PROOF` and does **not** give a
`COUNTERPACKET`. It banks a useful rank-one/slope-map reduction and cuts the
idea that balanced minimal indices automatically prove the desired
deterministic line bound.

## Verdict

Cycle50 is positive progress, but it does not solve the balanced-index wall.

The most useful contribution is a sharper identification of what the reduced
moving-scroll incidence count actually is:

```text
split locator T -> (a(T),b(T)) = (H(u)ell_T, H(v)ell_T) in F^t x F^t.
```

Transverse slopes are the value set of the partial map determined by the
rank-one condition

```text
a(T)+z b(T)=0,  b(T) != 0.
```

This cleanly separates:

- total landings / rank-one split locators;
- distinct slope image;
- tangent/common-envelope core;
- quotient-aligned moving-scroll concentration.

## Bankable Lemma A: Rank-One Slope Fibration

For a fixed Hankel pencil `H(u)+zH(v)` and a split locator `ell_T`, define

```text
a(T)=H(u)ell_T,
b(T)=H(v)ell_T.
```

Then a transverse locator realizes a slope iff

```text
b(T) != 0
and
rank[a(T) | b(T)] <= 1.
```

When this holds, the realized slope is unique:

```text
z(T) = -a_m(T)/b_m(T)
```

for any coordinate `m` with `b_m(T) != 0`.

Therefore the distinct slope count is the image size of a partial map from
split locators to `F`, and it is bounded by the number of rank-one transverse
split locators.

## Bankable Lemma B: Disjoint Moving Fibers

Let

```text
K0 = ker H(u) cap ker H(v),
L_z = ker(H(u)+zH(v)),
M_z = L_z/K0.
```

For `z != z'`,

```text
M_z cap M_z' = 0.
```

Indeed, if a vector lies in both kernels, subtracting the two equations gives
`H(v)x=0`, hence also `H(u)x=0`, so `x in K0`.

This supports the Cycle49 view that, after quotienting by the core, a
transverse projected locator belongs to at most one moving fiber.

## Bankable Lemma C: `R_line` Is the Averaged Landing Baseline

The rank-one locus in `F^t x F^t` has codimension `t-1`, so for

```text
N = binomial(n,k+t) = binomial(n,j),
Q = |F|,
```

the expected total landing count under random-anchor averaging is

```text
N / Q^(t-1).
```

This is the finite correction already banked as

```text
R_line = ceil(N / Q^(t-1)).
```

Thus `R_line` is the correct finite random-incidence baseline. A bare
`n^{1+o(1)}` term immediately above the entropy equality is not the correct
finite statement.

## Route Cut 1: Balanced Index Is Not Enough

Balanced right minimal indices remove the extreme unbalanced-directrix
quotient-component packets, especially the `d_M(E)=1` punctured-fiber
coequalizer shape. They do **not** by themselves exclude all quotient or
bounded-defect quotient-action packets.

The separate quotient-action-rank hypothesis remains load-bearing:

```text
d_M(E)=deg minpoly([X^M]_E)
```

and its moving-scroll analogue still have to be controlled.

## Route Cut 2: Average Does Not Give Worst-Case Upper

Cycle47 gives an averaged random-anchor estimate. Cycle50 correctly observes
that `R_line` is the averaged landing scale, but this does not prove a
deterministic per-line upper bound for every balanced quotient-separated
pencil.

The missing theorem is a worst-case inverse theorem, not another expectation
identity.

## Audit Correction: Image vs Landing Count

Cycle50 sometimes treats the distinct slope image bound as equivalent to a
landing-count bound. That equivalence is too strong.

Let

```text
R(u,v) = #{T : rank[a(T)|b(T)] <= 1, b(T)!=0}
Z(u,v) = #{z : exists T with z(T)=z}.
```

Then

```text
Z(u,v) <= R(u,v).
```

So a first-moment landing bound

```text
R(u,v) <= R_line + (j+1)
```

would imply the desired distinct-slope bound, but the reverse need not hold.
A high-multiplicity collapse can make `R(u,v)` huge while `Z(u,v)` is small.

Therefore the exact next wall should not be phrased only as Cycle44 landing
first moment unless we explicitly choose the stronger sufficient theorem.

Likewise, a pure `L2` bound gives useful anticollision information but does not
by itself upper-bound the distinct slope image unless it is coupled with an
upper bound for total landings. Cauchy-Schwarz usually gives a lower bound on
image size from `L^2/M2`, not an upper bound.

## Exact New Wall

The wall exposed by Cycle50 is:

```text
W-MCA-BALANCED-SCROLL-CONFIG-EQUIDISTRIBUTION
```

Precise version:

> For a fixed transverse Hankel pencil with balanced right minimal indices and
> no quotient-action-rank defect, bound the value set
>
> ```text
> Z(u,v) = #{ z(T) : T split, b(T)!=0, rank[a(T)|b(T)]<=1 }
> ```
>
> by `R_line + O(j)` or produce a source-valid counterpacket.

A stronger sufficient theorem is:

```text
R(u,v) <= R_line + O(j).
```

But this stronger landing-count statement should not be confused with the
actual MCA numerator, which is the distinct slope image `Z(u,v)`.

## Next Prompt Target

The next round should force this distinction:

```text
W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING
```

Ask for either:

1. a proof that the distinct value set `Z(u,v)` is bounded by
   `R_line + O(j)` under balanced-index and quotient-separated hypotheses;
2. a proof of the stronger landing bound `R(u,v) <= R_line + O(j)`;
3. or a counterpacket where balanced-index quotient-separated pencils have
   `Z(u,v) > R_line + O(j)`.

The counterpacket must exceed the distinct **slope image**, not merely total
landing multiplicity.
