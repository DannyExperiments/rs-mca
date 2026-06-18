# Paper B Counterexample Comparison

Status: AUDIT / EXPERIMENTAL.

This note compares the recent experimental counterexamples and route cuts with
`tex/slackMCA_v3.tex` (Paper B). It is not a paper edit. The purpose is to
extract theory-side consequences before deciding which changes, if any, should
be promoted into Paper B.

## Executive Summary

Most recent counterexamples are not counterexamples to Paper B's corrected MCA
conjecture. They are counterexamples to stronger routes that one might have
tried to use:

- unrestricted same-numerator extension-line transfer;
- raw arbitrary support-fiber bounds;
- promoting monic-anchor residue reductions to arbitrary anchors;
- treating CA or ordinary line-decoding as identical to support-wise MCA;
- expecting quotient-removed finite-field prefix fibers to become injective.

The important exception is the raw arbitrary locator-fiber statement. As
currently worded, Paper B's arbitrary-word locator-fiber conjectures bound the
raw set `Fib_U(k+sigma)` for every received word `U`. That object is too large
when `U` is already a codeword. The list injection remains true, but the raw
fiber is not the right final local-limit object.

The theory-side gain is that the conjectural frontier should be sharpened from
"bound every raw fiber" to "bound a pruned/full-agreement support object, or
bound actual lists through a canonical support selector." For MCA, the
counterexamples mostly reinforce Paper B's existing residue-line normal form
and identify the balanced arbitrary-anchor residue cloud as the live wall.

## 1. Raw Arbitrary Locator Fibers

### Experimental input

`20260617_L1_LOCATOR_FIBER_COUNTEREXAMPLE_AUDIT.md` records a direct
counterexample to a raw arbitrary feasible-fiber local limit. If `U` is a
degree-`<k` codeword, then for every `s`-subset `S`,

```text
deg(U mod L_S) < k,
```

so every `s`-subset lies in `Fib_U(s)`. The actual list has one codeword, but
the raw feasible support fiber has size `binom(n,s)`.

The finite packet in the audit uses:

```text
p = 97, n = 16, k = 7, sigma = 4, s = 11, U = 0,
|Fib_0(11)| = binom(16,11) = 4368.
```

### Paper B comparison

Paper B's list injection remains correct:

```text
list size <= |Fib_U(s)|.
```

The issue is the conjectural positive formulation. The literal raw-fiber
versions of:

- `conj:arbitrary-local`,
- `conj:final-locator`,

are false if they assert `|Fib_U(k+sigma)| <= n^B` for every arbitrary `U`.

### Theory consequence

The arbitrary-word list conjecture should be repaired. Plausible repairs:

1. bound actual list size rather than raw feasible support count;
2. choose one canonical support per listed codeword;
3. use full agreement supports `A_U(c)={x:c(x)=U(x)}` with `|A_U(c)|>=a`;
4. use exact/full supports or maximal supports, not all contained `a`-subsets;
5. keep raw `Fib_U(a)` only as an upper-bound proxy with an explicit overcount
   factor.

The L2 note `l2_interleaved_support_bridge.md` already gives the right language:
full-agreement support profiles avoid the codeword-overcount pathology. This is
probably the most immediate Paper B repair.

### Does it refute Paper B's MCA conjecture?

No. It refutes a list-side raw support-fiber formulation, not residue-line MCA.
But Paper B's final list local limit should be revised before being treated as
the companion to the MCA conjecture.

## 2. Extension-Line Counterexamples

### Experimental input

`f1_fixed_rate_extension_counterexample.md` and the F1 audit folder give
genuinely extension-valued lines over `F/B`, with denominator

```text
E(X)=X-alpha,       alpha notin B.
```

For `B=F_p`, `F=F_{p^2}`, `H=B^*`, and

```text
f(x)=x^a/(x-alpha),       g(x)=-1/(x-alpha),
```

many supports produce bad slopes

```text
z_S = (X^a - L_S)(alpha).
```

At fixed rate this gives a forced extension-line numerator of order `p^2` in
quadratic extensions. The `sigma=1` and `sigma=2` constructions are
sub-reserve, but they decisively refute an unrestricted same-numerator lift
from base-field MCA to extension-field challenges.

### Paper B comparison

This does not contradict Paper B's `thm:subfield`. That theorem assumes
`f,g in B^D`. The counterexample uses `F`-valued `f,g`, so it lies exactly
outside the confinement theorem.

It also matches Paper B's `rem:explicitattack`, which says explicit
extension-valued attacks should live in the residue-line normal form with
denominators `E in F[X]` not defined over `B`.

### Theory consequence

Paper B is basically right here, but the experimental material suggests adding
or emphasizing:

- `thm:subfield` is only a `B`-valued line theorem;
- no certificate should divide a base-field MCA numerator by `|F|` for
  arbitrary `F`-valued lines;
- the extension-valued positive theorem, if true, must be a residue-line,
  multiplication-slice, or interleaved-base statement;
- fixed positive slack is not enough: the examples survive at `sigma=1,2`, far
  below the corrected `C n/log n` reserve.

### Does it refute Paper B's final MCA conjecture?

No. The examples are sub-reserve and are already outside subfield confinement.
They clarify the extension-transfer ledger and cut a dangerous proof route.

## 3. Arbitrary Anchors In The Residue-Line Normal Form

### Experimental input

`f1_arbitrary_anchor_locator_split.md` proves two useful facts.

For unbalanced residue-line data of degree `t<sigma`, bad slopes inject into an
ordinary list for `RS[F,D,k+t]` with residual slack `sigma-t`.

For balanced data `t=sigma`, arbitrary anchors are controlled by the residue
cloud

```text
Cloud_E(w,a) = { [Q_S^w]_E : |S|=a },
```

not only by monic locator residues such as `[L_S]`. The locator-split and
sunflower constructions show arbitrary anchors can split a single monic-anchor
class into several slopes. The sunflower floor is

```text
Lambda_NC >= floor((n-k)/sigma).
```

At corrected reserve this is only `O(log n)` at fixed rate, so it is compatible
with Paper B's `n^{1+o(1)}` tangent/aperiodic scale.

### Paper B comparison

This fits Paper B's `def:residue`, `thm:normalform`, `thm:closure`, and
`conj:B`. The normal form already allows arbitrary anchor words `w`.

The experimental result refutes only a possible shortcut: "prove the
monic-anchor/base-core case, then promote it to arbitrary anchors." That
shortcut is not a theorem in Paper B.

### Theory consequence

Paper B's live MCA conjecture can be sharpened into two branches:

1. `t<sigma`: reduce to a repaired list local limit for `RS[F,D,k+t]` at
   residual slack `sigma-t`;
2. `t=sigma`: prove a balanced arbitrary-anchor residue-cloud packing theorem.

This is a useful theoretical decomposition of `conj:B`. It makes the balanced
case the genuine F1 wall.

## 4. Aperiodic Prefix Collisions

### Experimental input

`l1_aperiodic_prefix_collision.md` gives a finite `F_17` monomial-prefix
collision packet:

```text
H=F_17^*, n=16, k=6, sigma=4, a=10.
```

There are forty two-point prefix fibers after quotient-core explanations are
empty. The note also gives a complement-prefix lemma and a divisor-gap graph
formulation.

### Paper B comparison

This does not refute `conj:prefix-local` or `conj:final-locator`. Paper B asks
for polynomial fiber bounds, not injectivity, and its Galois-amplified
no-collision theorem requires primes far above this tiny `p=17` regime.

It does refute a stronger proof route: quotient removal does not make
finite-field monomial-prefix collisions disappear at small primes.

### Theory consequence

The useful theoretical output is the complement-locator viewpoint:

```text
same prefix fiber <=> low-degree perturbation between complement locators.
```

This gives a concrete finite-field algebraic object for L1 scanners and may be
a better attack surface than raw support enumeration.

## 5. Tangent CA/MCA Separation

### Experimental input

`x1_tangent_ca_mca_separation.md` constructs a pair `(f,g)` that is already
close to `C^2` and hence invisible to the no-proximity-loss CA predicate for
that same pair, while still producing `floor(delta n)` support-wise MCA-bad
slopes.

### Paper B comparison

This is exactly Paper B's tangent floor `prop:floor`. It does not refute Paper
B; it explains why `conj:B` must carry an additive `n^{1+o(1)}/q` term.

### Theory consequence

Any list/CA/MCA equivalence has to include either:

- a tangent correction;
- a support-aware CA predicate;
- or a tangent-exclusion hypothesis.

This matters more for Paper C/protocol ledgers than for Paper B itself.

## 6. Line-Decoding Separation And Bridge

### Experimental input

`m2_line_decoding_mca_bridge.md` proves that the support-wise line-decoding
numerator equals the MCA numerator after translating radius to agreement size.
The companion small script shows that ordinary close-point line decoding and
support-wise noncontainment can separate if support data are forgotten.

### Paper B comparison

This supports Paper B's `thm:normalform`; it does not refute it. The positive
MCA conjecture should be translated only into support-wise line-decoding, not
into a weaker close-point list-decoding statement.

### Theory consequence

The M2 target should be stated as:

```text
bound exact-support residue-line noncontained slopes
<=> bound support-wise line-decoding numerator
<=> bound emca after division by q_line.
```

## Theory-Side Takeaways For Paper B

### Direct repair needed

Repair the arbitrary-word locator local limit:

- Do not conjecture a polynomial bound on raw `Fib_U(k+sigma)` for every `U`.
- Replace it with actual list size, selected supports, maximal/full agreement
  supports, or another pruned support object.
- Keep raw fibers only as an upper-bound proxy with an explicit overcount
  diagnostic.

This affects `conj:arbitrary-local` and `conj:final-locator`.

### Clarification worth adding

Near `thm:subfield` / `rem:explicitattack`, explicitly warn that the
confinement theorem does not justify same-numerator extension-line MCA for
arbitrary `F`-valued lines. The experimental counterexample is the model
failure mode.

### Conjecture decomposition worth adding

Near `def:residue`, `thm:normalform`, or `conj:B`, split the residue-line
problem into:

- unbalanced `t<sigma`, charged to the repaired list ledger at residual slack;
- balanced `t=sigma`, charged to the arbitrary-anchor residue-cloud packing
  problem.

This would make the live wall of `conj:B` much more explicit.

### What remains compatible

The following experimental counterexamples are compatible with Paper B's
current corrected MCA conjecture:

- extension-line examples: sub-reserve and outside `B`-valued confinement;
- arbitrary-anchor split: a warning against monic-anchor promotion, not a
  refutation of the arbitrary-anchor normal form;
- aperiodic prefix collisions: polynomial-sized toy collisions, not a
  contradiction to local-limit bounds;
- tangent separation: already included by Paper B's tangent floor;
- line-decoding separation: supports the support-wise formulation.

## Suggested Next Paper-B Work

1. Rewrite `conj:arbitrary-local` and `conj:final-locator` with a repaired
   arbitrary-word object.

2. Add a remark after `rem:explicitattack` summarizing the degree-one
   extension-line counterexample as the finite obstruction to
   same-numerator extension transfer.

3. Add a short "residue-line reduction ledger" after `thm:normalform`:
   tangent / quotient-periodic / unbalanced residual-list / balanced
   arbitrary-anchor cloud.

4. Promote the complement-prefix locator lemma, if checked, as a useful L1
   finite-scanner lemma or appendix item.

5. Keep the Fable-loop rank/determinant material experimental until the
   `Q==0` resonance branch is proved or turned into a verified counterpacket.
