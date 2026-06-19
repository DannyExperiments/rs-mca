# Cycle 49 Syndrome Transverse-Secant Audit

Status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Model/run:

- Model: `claude-opus-4-8`
- Run: `2026-06-19T08-47-44-828Z-cycle49-syndrome-transverse-secant-inverse-7aeb3c2c`
- Preserved raw artifacts:
  `raw/cycle49_syndrome_transverse_secant_inverse/response.md`,
  `raw/cycle49_syndrome_transverse_secant_inverse/raw_response.jsonl`,
  `raw/cycle49_syndrome_transverse_secant_inverse/raw_response.json`,
  `raw/cycle49_syndrome_transverse_secant_inverse/run_result.json`,
  `raw/cycle49_syndrome_transverse_secant_inverse/input_manifest.json`,
  and `raw/cycle49_syndrome_transverse_secant_inverse/prompt_sent.md`.
- `output_files/` was empty in the source run.

The answer explicitly does **not** claim a proof of the positive upper theorem
and does **not** give a counterpacket. It banks an exact syndrome/Hankel normal
form, a Kronecker-pencil moving-core reduction, and a route cut for a tempting
but false low-degree-scroll shortcut.

## Verdict

Cycle49 is significant, but it is not a full solve.

The main upgrade is that the upper-side object is now much cleaner than the
residue-coordinate formulation. For a fixed Reed-Solomon code, every denominator
degree branch is represented by one syndrome-line incidence problem, and the
active inverse wall is compressed from the ambient syndrome dimension
`r = n-k` to a reduced moving space of dimension at most `2t`.

This is a strong organizing lemma for the safe-side MCA problem. It does not
prove that rich lines are only quotient/tangent templates.

## Bankable Lemma A: Hankel-Pencil Normal Form

Let `C = RS[F,L,k]`, `n=|L|`, `r=n-k`, and let `W_T` be the span of the parity
check columns indexed by a `j`-set `T`. Put

```text
t = r-j.
```

For a syndrome vector `w in F^r`, define the `t x (j+1)` Hankel matrix

```text
H(w)_{m,l} = w_{m+l},  0 <= m < t, 0 <= l <= j.
```

If `L_T(X)` is the monic degree-`j` complement locator and `ell_T` is its
coefficient vector, then

```text
u + z v in W_T  <=>  (H(u) + z H(v)) ell_T = 0.
```

Therefore the MCA numerator is exactly a problem of counting slopes `z` for
which the kernel of a Hankel pencil contains a squarefree fully-`L`-split monic
degree-`j` locator, with the transversality condition

```text
H(v) ell_T != 0.
```

This simultaneously covers the `t<sigma`, `t=sigma`, and `t>sigma` branches:
changing `j` changes `t=r-j`.

## Bankable Lemma B: Core/Moving Kronecker Reduction

For a line of syndromes `u+zv`, set

```text
K0 = ker H(u) cap ker H(v).
```

Then

```text
dim K0 >= j+1-2t.
```

For generic `z`, the kernel of `H(u)+zH(v)` decomposes as

```text
ker(H(u)+zH(v)) = K0 plus M_z,
```

with

```text
dim M_z <= t.
```

Thus the moving problem lives in

```text
V = F[X]_{<=j}/K0,   dim V <= 2t.
```

Kronecker pencil theory further gives right minimal indices
`eps_i` with

```text
sum_i eps_i <= t.
```

The moving kernels sweep a rational scroll of degree at most `t` in the reduced
space `P(V)`. This is the clean version of the prior locator-scroll/circuit
language: the common core is the contained/tangent part, while quotient
components appear as unbalanced minimal-index scrolls.

## Route Cut

Do **not** bank the shortcut:

```text
common core removal + scroll degree <= t => O(n) slopes.
```

The projected split-locator configuration is structured, not generic. A
low-degree scroll can still contain many projected split locators when it aligns
with a quotient structure such as `X^M`. This is exactly where the Cycle48
quotient-component and fixed-defect quotient-anchor packets live.

## Finite Accounting

Cycle49 preserves the Cycle48 finite correction. A safe-side finite theorem
cannot replace the random line-occupancy scale by a bare `n^{1+o(1)}` term.
The expected line scale is

```text
R_line = ceil(binomial(n,k+t) / Q^(t-1)).
```

A realistic finite upper shape is therefore

```text
Pi_j(C) <= U_quotient + R_line + A_theta(n),
```

where `U_quotient` charges quotient-component/fixed-defect packets and
`A_theta(n)` charges contained/tangent/common-envelope contributions.

## Exact New Wall

```text
W-MCA-REDUCED-MOVING-SCROLL-INCIDENCE
```

In the reduced space

```text
V = F[X]_{<=j}/K0,  dim V <= 2t,
```

with moving kernel `M_z` and Kronecker scroll of degree at most `t`, prove that
after removing unbalanced minimal-index quotient scrolls and the contained /
tangent core, the number of slopes satisfying

```text
M_z cap Proj_V(Split_L^sf) != empty
```

is at most

```text
R_line + A_theta(n).
```

## Next Prompt Target

The smallest clean next target is:

```text
W-MCA-REDUCED-MOVING-SCROLL-BALANCED-INDEX
```

Ask for either a proof or a counterpacket to:

```text
If the Hankel pencil H(u)+zH(v) has right minimal indices all within 1 of each
other, then

#{ z : M_z meets Proj_V(Split_L^sf) } <= R_line + (j+1).
```

This is the genuinely aperiodic balanced-index case. A proof here, combined
with the Cycle48 quotient-component classification, would move the positive
side much closer to matching the Cycle47 lower/failure branch. A counterpacket
here would be more serious than the Cycle48 quotient packets because it would
survive the current quotient/tangent explanations.

## Audit Note

Confidence is high for the linear-algebra reductions. Confidence is unknown for
the proposed inverse theorem. This result should be treated as a route
compression and wall sharpening, not as a prize-level proof.
