# Cycle 53 Slope-Summed Character Audit

Status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Raw run:

- `raw/cycle53_per_line_symmetric_determinantal_incidence/response.md`
- `raw/cycle53_per_line_symmetric_determinantal_incidence/raw_response.jsonl`
- `raw/cycle53_per_line_symmetric_determinantal_incidence/raw_response.json`
- `raw/cycle53_per_line_symmetric_determinantal_incidence/run_result.json`
- `raw/cycle53_per_line_symmetric_determinantal_incidence/input_manifest.json`
- `raw/cycle53_per_line_symmetric_determinantal_incidence/prompt_sent.md`

Harness note: `run_result.json` reports `OK_WITH_NONFATAL_STREAM_WARNING`, with
one malformed stream-json line and usable answer text. No `output_files/` were
created by the worker.

## Verdict

Cycle 53 does not prove the deterministic per-line upper theorem and does not
give a source-valid counterpacket. It does bank an exact analytic reduction:
the per-line landing bound is equivalent to a one-sided bound for a signed
slope-summed nontrivial-character error term.

The new wall is:

```text
W-MCA-PER-LINE-SLOPE-SUMMED-CHARACTER-CANCELLATION
```

## Bankable Lemma

Let `Q=|F|`, let `t=r-j`, and let

```text
a(T)=H(u) ell_T,
b(T)=H(v) ell_T,
```

where `ell_T` is the monic complement locator for a fully `L`-split `j`-set
`T`. Let

```text
N(z)=#{T split : H(u+zv) ell_T = 0},
K0_split=#{T split : H(u)ell_T=H(v)ell_T=0}.
```

Then the total transverse landing count satisfies the exact identity

```text
R(u,v)=sum_z N(z)-Q*K0_split.
```

Expanding `N(z)` by additive characters gives

```text
N(z)=Q^{-t} sum_{y in F^t} S(y,z),
S(y,z)=sum_{T split} psi(<y,H(u+zv)ell_T>).
```

The `y=0` term contributes exactly the unceiled random-incidence baseline

```text
binomial(n,j)/Q^(t-1).
```

Therefore

```text
R(u,v)
= binomial(n,j)/Q^(t-1) - Q*K0_split + Err,

Err
= Q^{-t} sum_{z in F} sum_{y in F^t, y != 0} S(y,z).
```

Since `-Q*K0_split <= 0`, the desired landing upper bound

```text
R(u,v) <= R_line + O(j),
R_line=ceil(binomial(n,j)/Q^(t-1)),
```

follows from the one-sided estimate

```text
Err <= O(j).
```

## Phase Rewriting

Writing `u+zv` in moment/evaluation form as

```text
w_i(z)=sum_{x in L} beta_x(z) x^i
```

and `Y(X)=sum_{m<t} y_m X^m`, the phase collapses to the cosupport form

```text
<y,H(u+zv)ell_T>
= sum_{x in L\T} beta_x(z) Y(x) prod_{y' in T}(x-y').
```

This identifies the per-line symmetric-determinantal incidence wall with the
Cycle44-style elementary-symmetric/cosupport character-sum wall, now summed over
the slope parameter `z` and dual vector `y`.

## Route Cuts

The route

```text
determinantal codimension + Bezout => O(j)
```

is cut. The target configuration is a finite, structured set of fully
`L`-split locators; it is not a positive-dimensional free-root cover where
Bezout or monodromy density gives the required fixed-domain count.

Balanced minimal-index hypotheses buy phase nondegeneracy only. They remove
trivial directrix/tangent degeneracy but do not by themselves imply cancellation
of `S(y,z)`.

Quotient separation remains load-bearing. If `X^M` has small quotient-action
rank modulo the denominator, the `X^M`-periodic subconfiguration contributes a
secondary main term inside `Err`. Large `d_M(E)=deg minpoly([X^M]_E)` is the
right way to remove that imprimitive main term.

## Exact New Wall

The next exact lemma is a slope-summed cosupport cancellation theorem:

```text
For balanced, transverse, quotient-separated pencils over a smooth
multiplicative domain L, prove

Err = Q^{-t} sum_z sum_{y != 0} sum_{T split}
      psi(sum_{x in L\T} beta_x(z)Y(x)prod_{y' in T}(x-y'))
    <= O(j),

after deleting the <=t tangent slopes and the quotient-action-rank packets.
```

The smallest useful subtarget is the `t=2` case, where the nontrivial phase is
the first place that phase nondegeneracy and actual cancellation separate.

## Audit Decision

Bank:

- the exact signed identity for `R`;
- the cosupport character phase;
- the role split: balance gives nondegeneracy, quotient separation removes
  imprimitive main terms, transversality controls tangent fibers.

Do not bank:

- a deterministic upper theorem;
- any proof of `Err<=O(j)`;
- any prize-level MCA threshold.
