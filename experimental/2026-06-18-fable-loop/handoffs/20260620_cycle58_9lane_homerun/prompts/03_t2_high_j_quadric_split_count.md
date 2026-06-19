# Lane 03: t=2 High-j Determinantal Quadric Split Count

Read `COMMON_CONTEXT.md` first.

## Target

Attack:

```text
W-MCA-T2-HIGH-J-DETERMINANTAL-QUADRIC-SPLIT-COUNT
```

Cycle 54 banked that for `t=2`, the landing condition is a determinant/quadric
equation in complement-locator coefficients. Cycle 55 analyzed `j=2`, but
Cycle 56 cut it as official-rate progress because `t=2,j=2` implies
`rho -> 1`.

Now take official constant rate:

```text
rho in {1/2,1/4,1/8,1/16},
k=floor(rho n),
t=2,
j=n-k-2 = Theta(n).
```

After removing quotient/tangent/same-witness/core templates, determine whether
the number of split locators satisfying the `t=2` determinant equation is
`n^{1+o(1)}` or can be superlinear.

## Required Work

1. Write the exact `t=2` high-`j` determinant equation.
2. Interpret it on the split-locator variety of `j`-subsets of a smooth
   multiplicative domain.
3. Prove a nonquotient `n^{1+o(1)}` bound, or construct a fixed-rate
   counterpacket.
4. Decide whether the `O(sqrt(Q))` conic fluctuation can compound at high `j`.
5. State the next exact lemma if the problem reduces to a subgroup-variety
   incidence theorem.

## Output Format

Use:

```text
VERDICT
T2_HIGH_J_NORMAL_FORM
COUNTING_THEOREM_OR_COUNTERPACKET
QUOTIENT_TANGENT_STATUS
EXACT_NEW_WALL
```
