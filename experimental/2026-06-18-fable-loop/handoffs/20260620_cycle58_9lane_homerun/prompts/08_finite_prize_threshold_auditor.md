# Lane 08: Finite Prize Threshold Auditor

Read `COMMON_CONTEXT.md` first.

## Target

Audit the finite prize threshold at:

```text
epsilon* = 2^-128,
rho in {1/2,1/4,1/8,1/16}.
```

Do not give a rate-only formula unless all finite constraints are cleared.

## Required Work

For both MCA and list challenges, identify which constraints dominate:

```text
entropy reserve
quotient profile
tangent floor
q/n field-size floor
universal cap
actual scalar list local limit
all-denominator MCA strata
interleaved projection/diagonalization
integer rounding
```

Produce a conditional finite threshold formula of the form:

```text
delta*_C(epsilon*) = 1-rho-reserve + error
```

only if justified. Otherwise state the exact missing finite theorem or checker.

## Output Format

Use:

```text
VERDICT
FINITE_LEDGER
MCA_THRESHOLD_STATUS
LIST_THRESHOLD_STATUS
DOMINANT_FLOORS
CONDITIONAL_FORMULA
EXACT_NEW_WALL
```
