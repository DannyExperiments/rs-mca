# Lane 01: Global Syndrome Transverse-Secant Inverse

Read `COMMON_CONTEXT.md` first.

## Target

Attack:

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

Let `C=RS[F,L,k]`, `|L|=n`, `r=n-k`, `a=k+sigma`, and `j=n-a`.
Let `syn:F^L -> F^r` be a syndrome map and let `h_x=syn(e_x)`. For each
`j`-set `T subset L`, put

```text
W_T = span{h_x : x in T}.
```

For syndrome vectors `u,v`, a slope `z` is MCA-bad on complement `T` exactly
when

```text
u+zv in W_T,       v notin W_T.
```

Prove or refute the following:

Above corrected entropy and quotient reserve, after quotient/tangent/common
envelope templates are removed, every affine syndrome line `{u+zv}` has at most
`n^{1+o(1)}` transverse intersections with `{W_T}`.

## Required Work

1. Give a precise theorem statement with all hypotheses.
2. Prove it, or identify the first false implication.
3. If false, construct a source-valid counterpacket.
4. If open, state the exact next lemma, not a vague strategy.
5. Explain how this formulation covers all denominator degrees.

## Output Format

Use:

```text
VERDICT
THEOREM_OR_COUNTERPACKET
PROOF_OR_FAILED_STEP
TEMPLATE_STATUS
EXACT_NEW_WALL
FULL_SOLVE_ASSESSMENT
```
