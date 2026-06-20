# ROLE 09 - Two-Block-System Overlap Kill Test

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
W-MCA-TWO-BLOCK-COMMON-UNION-RIGIDITY
```

## Objective

Run the restricted kill test for the deprioritized MCA support-overlap route.

For two separable maps `R,S` with no common right factor, study exact supports
that are simultaneously unions of full `R`-fibers and full `S`-fibers.

Either:

1. prove a finite bound on the number of connected components/common unions in
   the block-incidence graph strong enough to make the support-overlap route
   precise; or
2. construct many nontrivial common unions on one envelope-free syndrome line,
   showing that pairwise support overlap cannot be charged by a bounded
   registry without an additional invariant.

## Required Checks

- common right factor/refinement exclusion;
- block-incidence graph construction;
- component count;
- common-union support count;
- weighted cover lower/upper bound;
- whether the packet lies on a proper envelope or tangent/common-core template.

## Success Criteria

Output `ROUTE_CUT` if you produce an explicit family showing the route needs a
new invariant.

Output `BANKABLE_LEMMA` if you prove a usable finite two-system rigidity bound.

