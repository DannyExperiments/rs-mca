# Lane 05: All-Denominator MCA Auditor

Read `COMMON_CONTEXT.md` first.

## Target

Audit whether a balanced `t=sigma` upper theorem would imply the full scalar
MCA upper theorem.

The exact normal form maximizes over all denominator degrees:

```text
1 <= t <= n-k.
```

The three strata are:

```text
t < sigma    residual-list / jet-residue regime
t = sigma    balanced point-cloud regime
t > sigma    thick residue affine-plane regime
```

## Required Work

1. Prove exactly what balanced upper controls.
2. Prove the residual-list injection for `t<sigma`, and identify what actual
   list theorem is still needed.
3. Analyze `t>sigma` as affine-plane incidence:

```text
z[B]_E in [I_S(w)]_E + [L_S F[X]_{<t-sigma}]_E.
```

4. Decide whether a denominator-compression lemma can reduce high `t` to
   `t'<=sigma`.
5. Produce a corrected theorem assembly or a route cut.

## Output Format

Use:

```text
VERDICT
ALL_DENOMINATOR_LEDGER
T_LESS_SIGMA
T_EQUALS_SIGMA
T_GREATER_SIGMA
ASSEMBLY_OR_ROUTE_CUT
EXACT_NEW_WALL
```
