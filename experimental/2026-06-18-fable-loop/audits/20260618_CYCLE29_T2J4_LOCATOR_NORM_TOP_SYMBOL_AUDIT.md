# Cycle 29 T2J4 Locator-Norm Top-Symbol Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is source-audited against the previously banked Cycle 11/12/16/20/24/25/28 objects.

Source artifacts:

- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RAW.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RUN_RESULT.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2}`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, now `j = n-a = r-t = 4`.
- Branch: off `R0`, `kappa = u wedge b != 0`, source-valid separated
  quadratic `E=X^2+cX+d` nonzero on `F_p`, with `c_b != 0`.

This is a residue-line / bad-slope incidence calculation only. It is not a
list-decoding, CA, MCA, line-decoding, curve-MCA, protocol, `q_gen`, or SNARK
claim.

## Banked Narrow Lemma

In the restricted ledger above, the `j=4` quotient has the closed form

```text
Q_S = W_{n-1} X^3
    + (W_{n-2} - W_{n-1} tau_1) X^2
    + (W_{n-3} - W_{n-2} tau_1 + W_{n-1} tau_2) X
    + (W_{n-4} - W_{n-3} tau_1 + W_{n-2} tau_2 - W_{n-1} tau_3).
```

Thus `Q_S` depends on `tau_1,tau_2,tau_3` and not on `tau_4`. The locator
residue

```text
lambda = [L_T]_E
       = xi_4 - tau_1 xi_3 + tau_2 xi_2 - tau_3 xi_1 + tau_4
```

still gives an affine bad-line system

```text
L_z(tau) = iota - z mu = C_1(z)tau_1+C_2(z)tau_2+C_3(z)tau_3+C_4(z)tau_4+C_0(z)=0
```

in `A=F[X]/E`, viewed as a four-dimensional `B`-space.

The important change from `j=3` is dimensional: `j=4` supplies four affine
co-support parameters and the ambient space also has `dim_B A = 4`. Therefore
the coefficient matrix

```text
M(z)=[C_1(z)|C_2(z)|C_3(z)|C_4(z)]
```

is square. When `det_B M(z) != 0`, affine consistency is automatic and gives a
unique parameter vector

```text
tau(z)=M(z)^(-1)(-C_0(z)).
```

The Cycle 28 augmented determinant obstruction has no direct analogue at
`j=4`; the new determinant is an invertibility/uniqueness determinant, not an
incidence obstruction.

## Top-Symbol Audit

Cycle 29 computes the highest-degree-in-slope symbol of this square determinant
as

```text
TopSym(det_B M(z)) = -N(kappa) * N(z)^2 * Q_4,
```

where `Q_4` is the Cycle 28 locator quantity

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

Equivalently, in the `c notin B` branch,

```text
Q_4 = N(c_b) * Im(c)^2 * E(-Im(d)/Im(c)).
```

and in the `c in B` branch,

```text
Q_4 = N(c_b) * Im(d)^2.
```

Thus the top symbol is source-validly nonzero under the same hypotheses as
Cycle 28. It contains the same single active locator factor, not a growing
power of the full degree-`p` locator norm `prod_{a in F_p}E(a)`.

This banks only the structural top-symbol/invertibility fact. It does not bank
an `O(p)` slope bound for `j=4`.

## Exact New Wall

The Cycle 28 mechanism stops at `j=4` for a structural reason:

```text
j=3: 3 parameters in B^4 -> one augmented determinant obstruction.
j=4: 4 parameters in B^4 -> square system; generic slopes have one affine preimage.
```

Consequently, off the degree-`<=4` noninvertibility curve, affine consistency
does not bound slopes. The remaining source-correct object is the distinct
split-quartic gate:

```text
W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE
```

with

```text
tau(z)=M(z)^(-1)(-C_0(z)),
```

bound

```text
#{ z in F :
   X^4 - tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z)
   splits into four distinct roots in F_p }.
```

Either this set is `O(p)`, extending the restricted `t=2` law, or there is a
possible growing-prime sub-reserve counterpacket with `Theta(p^2)` realized
slopes. Cycle 29 does not prove either direction.

## Dependencies

- Cycle 11/12: quotient pattern and elementary co-support parameters.
- Cycle 16: determinant safe side for `j=3`, used only as contrast.
- Cycle 20: wedge/column conventions for `q1`, `q2`, `lambda_0`, and `c_b`.
- Cycle 24: locator norm identity `N(ell)=prod_{a in F_p}E(a)`.
- Cycle 25: separation of consistency determinant from unrelated `z`-free invariants.
- Cycle 28: verified `Q_4` formula and source-valid nonvanishing.

## Hidden Assumptions

- The displayed quotient form assumes `p` is large enough that the top
  coefficient recursion is not affected by the `-X` tail of `X^p-X`.
- The top-symbol calculation is by-hand from the recovered structured answer;
  no finite checker was run in Cycle 29.
- The determinant comparison uses the same Cycle 20/25 column conventions and
  `det_B(m_x)=N(x)^2` for multiplication by `x` on the two-dimensional
  `F`-algebra `A`.

## Rejected Overclaims

- Not a proof of `C2=O(p)` for `j=4`.
- Not a source-valid counterpacket.
- Not a corrected-reserve theorem.
- No `q_gen` / `q_line` merge.
- No `q_chal`, list-decoding, CA, MCA, line-decoding, curve-MCA, protocol,
  SNARK, or Proximity Prize consequence.
- No claim that the top symbol is literally `N(ell)^m`; it is a scalar times
  `N(z)^2` times the single active locator factor already seen in Cycle 28.

## Next Prompt

Attack `W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE` directly. The question is no
longer whether the top symbol is nonzero; it is whether the rational map
`z -> tau(z)` hits the totally split distinct quartic locus only `O(p)` times
or whether a source-valid growing-prime family realizes `Theta(q_line)` slopes.
