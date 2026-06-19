# Cycle 55 t=2,j=2 Conic Split-Pair Audit

Status: `BANKABLE_LEMMA / PROOF / ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.

Raw run:

- `raw/cycle55_t2j2_determinantal_conic_split_pair/response.md`
- `raw/cycle55_t2j2_determinantal_conic_split_pair/raw_response.jsonl`
- `raw/cycle55_t2j2_determinantal_conic_split_pair/raw_response.json`
- `raw/cycle55_t2j2_determinantal_conic_split_pair/run_result.json`
- `raw/cycle55_t2j2_determinantal_conic_split_pair/input_manifest.json`
- `raw/cycle55_t2j2_determinantal_conic_split_pair/prompt_sent.md`

Harness note: `run_result.json` reports `OK_WITH_NONFATAL_STREAM_WARNING`, with
one malformed stream-json line and usable `response.md`. No `output_files/`
were created.

## Verdict

Cycle55 is significant but not a full safe-side proof. It cuts the literal
`+O(1)` target for the `t=2,j=2` conic split-pair count in the large-domain
regime and replaces it with a corrected `+O(sqrt(Q))` Weil-type wall.

The counterpacket in the response is not banked as a final `COUNTERPACKET`
because it is a seed: it still needs finite checker execution and exact
source-validity verification. The route cut and corrected wall are banked.

## Bankable Lemma: Explicit Conic

For `T={s,s'}`, set

```text
e_1=s+s',
e_2=ss',
ell_T=(e_2,-e_1,1).
```

With moment minors

```text
M_ab=u_a v_b-u_b v_a,
```

the `t=2,j=2` determinant is the conic

```text
D(e_1,e_2)
= M_12 e_1^2 - M_02 e_1 e_2 + M_01 e_2^2
  - M_13 e_1 + (M_03-M_12)e_2 + M_23.
```

This is consistent with the Cycle54 `j=1` formula and identifies the first open
subcase as a conic incidence problem in the Vieta coordinates.

## Bankable Lemma: Split-Pair Curve

Substituting `e_1=s+s'` and `e_2=ss'` gives a symmetric bidegree `(2,2)` curve

```text
F(s,s')=D(s+s',ss')=0.
```

Modulo the involution `s<->s'`, this curve double-covers the conic. Generically
the cover is branched at four points, so the curve has genus one. This is the
geometric reason a Weil bound gives `O(sqrt(Q))`, not `O(1)`.

## Bankable Proof: Corrected Weil Bound

After removing tangent/core and multiplicatively special quotient components,
the aperiodic component satisfies the standard curve character-sum bound:

```text
R(u,v)=binomial(n,2)/Q + O(sqrt(Q)).
```

The proof uses multiplicative-character expansion for membership in
`mu_n x mu_n`; nontrivial characters on absolutely irreducible non-coset
components have Weil-size `O(sqrt(Q))`.

This is not the originally requested `+O(1)` theorem. It is a corrected
deterministic upper bound in the `t=2,j=2` case.

## Route Cut

The literal target

```text
R <= ceil(binomial(n,2)/Q)+O(1)
```

is cut in the large-domain/genus-one regime. A generic aperiodic conic lift is
elliptic, and its Frobenius trace can contribute fluctuations of size
`Theta(sqrt(Q))`. Thus `+O(1)` is not the right global wall unless additional
hypotheses force rational/reducible genus-zero geometry or restrict to a
small-subgroup regime where a separate subgroup-incidence theorem applies.

## Quotient and Degeneracy Accounting

The dangerous non-Weil-cancelling components are multiplicative coset curves:

```text
s^alpha (s')^beta = c.
```

These are precisely the quotient/imprimitive packets to charge through the
`d_M(E)` quotient-action-rank ledger. Tangent-to-Vieta and `M_01=0` degeneracies
belong to the tangent/core side already separated in earlier cycles.

## Exact New Wall

The corrected wall is:

```text
W-MCA-T2J2-CONIC-SPLIT-PAIR-COUNT-CORRECTED
```

with two branches:

1. Large-domain branch:

   ```text
   R=binomial(n,2)/Q+O(sqrt(Q))
   ```

   after tangent/core and quotient/coset components are removed.

2. Small-subgroup branch:

   prove a Stepanov/sum-product style bound for

   ```text
   #{(s,s') in mu_n^2 : F(s,s')=0}
   ```

   on absolutely irreducible non-coset bidegree `(2,2)` curves when
   `n=O(sqrt(Q))`.

## Counterpacket Seed

The response proposes a seed against the literal `+O(1)` target:

```text
L=mu_{Q-1}=F^*
```

and choose transverse balanced moments so that the associated bidegree `(2,2)`
curve is geometrically irreducible, non-coset, and has Frobenius trace
`a_C` of size `-Theta(sqrt(Q))`. Then the excess over the random baseline is
`Theta(sqrt(Q))`.

This remains a seed, not a banked `COUNTERPACKET`, until a local checker and
source-validity audit verify the hypotheses for an explicit growing family.

## Next Exact Target

Before launching another broad proof attempt, the next exact construction is:

```text
W-MCA-T2J2-CONIC-SQRT-COUNTERPACKET-CHECK
```

Run or write a finite checker that:

- verifies the conic identity;
- searches for non-core, non-coset `t=2,j=2` examples with excess
  `~sqrt(Q)`;
- distinguishes quotient/coset packets from genuinely aperiodic elliptic
  examples;
- reports whether the seed can be promoted to `COUNTERPACKET` or only to a
  corrected `O(sqrt(Q))` wall.

Do not promote:

- full scalar MCA upper theorem;
- full prize threshold;
- final `COUNTERPACKET` without source-validity checks.
