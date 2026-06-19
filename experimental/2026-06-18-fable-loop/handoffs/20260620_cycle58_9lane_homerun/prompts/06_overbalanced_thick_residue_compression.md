# Lane 06: Overbalanced Thick-Residue Compression

Read `COMMON_CONTEXT.md` first.

## Target

Attack the high-denominator branch:

```text
W-MCA-HIGH-DENOMINATOR-THICK-RESIDUE-COMPRESSION
```

For `t>sigma`, every witness polynomial on an `a=k+sigma` support has form:

```text
Q = I_S(w) + L_S H,
deg H < t-sigma.
```

The slope condition is:

```text
z[B]_E in [I_S(w)]_E + [L_S F[X]_{<t-sigma}]_E.
```

Noncontainment is:

```text
[B]_E notin [L_S F[X]_{<t-sigma}]_E.
```

## Required Work

1. Prove a high-cloud denominator-compression theorem:

```text
t>sigma and many slopes => equivalent datum with t'<=sigma
```

outside quotient/tangent/templates.

2. Or construct a reduced, source-valid `t>sigma` counterpacket at official
   constant rate.
3. Connect this branch to the syndrome transverse-secant formulation.
4. Explain whether high denominator can be ignored in the prize challenge.

## Output Format

Use:

```text
VERDICT
THICK_RESIDUE_NORMAL_FORM
COMPRESSION_THEOREM_OR_COUNTERPACKET
SOURCE_VALIDITY
EXACT_NEW_WALL
```
