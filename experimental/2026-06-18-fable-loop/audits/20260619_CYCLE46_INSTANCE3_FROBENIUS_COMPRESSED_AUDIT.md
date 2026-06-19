# Cycle 46 Instance 3 Frobenius-Compressed Landing Supplement

Status: PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT / AUDIT

Raw provenance:

- `raw/cycle46_instance3_frobenius_supplement/07_INSTANCE4_BALANCED_ANCHOR_RESERVE_LIFT_CERTIFICATE.txt`
- `raw/cycle46_instance3_frobenius_supplement/08_INSTANCE3_FROBENIUS_COMPRESSED_LANDING_PASTE.md`

The first file is another Cycle 45 balanced/random-anchor restricted additive
certificate. It is consistent with the already banked Cycle 45 theorem and adds
no new route-board claim beyond confirming the pair-rank/L2 reserve lift in the
`D=F_p`, `F=F_{p^2}`, `q_line=p^2` branch.

The second file is the new material. It claims a Frobenius-compressed additive
construction by taking

```text
E = H(X)(X-theta),
B_num = H(X),
theta in F_{p^2} \ F_p,
H in F_p[X], deg H=t-1,
```

and restricting the anchor to `w:D -> F_p`. The Frobenius envelope

```text
J = lcm(E,E^(p)) = H(X)m_theta(X)
```

has degree `t+1`. Therefore the base-polynomial residue image

```text
U = { [P]_E : P in F_p[X] }
```

has `F_p`-dimension `t+1`, contains the full slope line `F_{p^2} b`, and every
cosupport residue lies in `U`.

## Source Check

The local residue-line definition in `tex/slackMCA_v3.tex` requires:

```text
deg E=t,
E nonzero on D,
deg B<t,
w:D -> F,
```

and does not impose `gcd(E,B)=1` or denominator minimality. On the supplied
local definition, this construction is literally admissible as a degree-`t`
residue-line datum.

The same local source also identifies the official smooth-domain setting as
smooth multiplicative subgroups/cosets, not the additive full base domain
`D=F_p`. Therefore this supplement is not a prize-level promotion by itself.

## Bankable Lemma Candidate: Frobenius Envelope Compression

Let `B=F_p`, `F=F_{p^2}`, and let `E in F[X]`. If

```text
J = lcm(E,E^(p)),
```

then the natural map

```text
B[X] -> F[X]/E
```

has kernel `(J)`. Thus the base-polynomial image has dimension

```text
dim_B U = deg J.
```

In the special construction `E=H(X)(X-theta)` with
`H in B[X]`, `deg H=t-1`, and `theta notin B`,

```text
dim_B U = deg(H m_theta) = t+1.
```

Moreover `b=[H]_E` maps to `(0,H(theta))` under

```text
F[X]/E ~= F[X]/H x F,
```

so `F b subset U`.

Classification: `BANKABLE_LEMMA`, pending a clean source-audited writeup.

## Proof Candidate: Compressed Additive All-Slope Branch

For `B`-valued random anchors on `D=F_p`, the compressed exchange-rank lemma is
the same interpolation rank statement over the modulus `J`, with effective
dimension

```text
tau = deg J = t+1.
```

For `N=binom(p,j)` and

```text
Lambda = N / p^(t+1),
```

the shell loss is at most

```text
exp(2 sqrt(aj/p)) <= exp(sqrt p) = 2^{o(p)}.
```

Thus if

```text
t = (C+o(1)) p/log_2 p,
C < H_2(rho),
```

then `Lambda/(p^2 exp(sqrt p)) -> infinity`, and a deterministic `F_p`-valued
anchor exists with

```text
nu_w(z) = (1+o(1)) binom(p,j)/p^(t+1)
```

uniformly for every `z in F_{p^2}`. This gives all `p^2` slopes in the
additive/base-field branch at the full `C < H_2(rho)` threshold.

Classification: `PROOF_CANDIDATE`, not final.

## Caveat: Nonminimal Denominator

The construction has

```text
gcd(E,B_num)=H.
```

The rational direction is therefore

```text
-B_num/E = -1/(X-theta).
```

Equivalently, after setting `y=w/H`, the same line is represented by the
reduced degree-one datum

```text
E_1=X-theta,
B_1=1,
w_1=y.
```

This does not invalidate the line-MCA obstruction under the local normal-form
definition, but it is exactly the issue a reviewer may call a packaging
artifact. The construction may be better interpreted as a low-denominator
line whose random base-field anchor produces many degree-`<k+1` interpolants
with prescribed external value `V(theta)=z`.

Therefore this supplement cuts the *literal* Frobenius-compression wall only
under the current nonminimal residue-datum definition. If the project imposes
reduced denominators or separates low-denominator/tangent-floor families, the
claim must be reclassified and the smooth-domain transfer remains the main
route.

## Route-Board Effect

This supplement strengthens the evidence that the `H_2(rho)/2` barrier was a
ledger/representation artifact, not an intrinsic MCA barrier. There are now two
routes to the full entropy threshold:

1. Domain-uniform prime-field smooth subgroup route:
   `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT`.
2. Frobenius-compressed additive route with nonminimal denominator:
   `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING-NONMINIMAL`.

The preferred prize-facing route remains the first one, because it targets the
official smooth multiplicative-domain setting directly and does not rely on a
common factor in `(E,B_num)`.

## Remaining Checks

1. Does the official challenge or project source require reduced denominator
   presentations?
2. Can the compressed construction be moved from `D=F_p` to a smooth
   multiplicative subgroup/coset `D subset F_p^*` without losing the
   `t+1`-dimensional envelope? Algebraically it appears yes, provided `H`
   is nonzero on `D`, but this needs a clean proof.
3. Is the resulting branch already covered by known low-denominator/tangent
   or list-volume mechanisms?
4. Does this give an MCA counterpacket at the challenge rates after the exact
   finite-size constraints `k<=2^40`, `|F|<2^256`, and `epsilon*=2^-128` are
   imposed?
