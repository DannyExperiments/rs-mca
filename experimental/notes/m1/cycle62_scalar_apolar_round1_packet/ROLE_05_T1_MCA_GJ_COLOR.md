# ROLE 05 - Backup t=1 MCA Support-Plus-Color Theorem

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-JR-T1-GJ-FIBER-AND-COLOR
```

## Objective

Work on the backup MCA route.

For the shifted `t=1` MCA slice with

```text
deg A = sigma,
deg B = j,
```

prove the generalized-Jacobian support equivalence and derive the exact
external-color map

```text
chi(T,c) = -lambda_T c
```

or correct it.

The key issue: support multiplicity is not the MCA numerator. You must
characterize when two generalized-Jacobian supports yield the same MCA slope.

## Required Output

Give an exact formula for the distinct-color / distinct-slope numerator.
Separate:

- support fibers;
- color fibers;
- slope collisions;
- noncontainment;
- effective subgroup conditioning.

## Success Criteria

Output `BANKABLE_LEMMA` if you prove an exact support-plus-color theorem.

## Failure Criteria

Output `COUNTERPACKET` or `ROUTE_CUT` if color collisions destroy support-fiber
control or contradict the proposed formula.

