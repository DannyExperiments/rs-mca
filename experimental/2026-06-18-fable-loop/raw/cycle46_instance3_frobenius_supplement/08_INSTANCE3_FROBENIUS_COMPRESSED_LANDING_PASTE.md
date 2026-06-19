# Instance 3 Frobenius-Compressed Landing Paste

Source: user-pasted chat output on 2026-06-19 after the Cycle 46 targeted
wallbreaker audit. This was not provided as a local attachment file. This file
preserves the mathematical content and caveats for provenance.

## Verdict

Yes. Under the literal residue-datum definition in the packet, this appears to
close

```text
W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING
```

in the additive/base-field branch. The construction gives

```text
dim_{F_p} U = t+1,
F_{p^2} b subset U,
```

every cosupport residue lies in `U`, the residue multiset is `L^2`-balanced
over `U`, and the fibers over `F_{p^2} b` are pointwise balanced for

```text
t = (C+o(1)) p/log_2 p,
C < H_2(rho).
```

The key claim is that the effective modulus for `F_p`-valued anchors has degree
`t+1`, not `2t`.

## Construction

Let

```text
B = F_p,
F = F_{p^2},
D = B.
```

Choose `theta in F \ B`, and let

```text
m_theta(X) = (X-theta)(X-theta^p) in B[X]
```

be its quadratic minimal polynomial.

Choose a monic polynomial

```text
H in B[X], deg H = t-1,
```

with `H(d) != 0` for `d in B` and `gcd(H,m_theta)=1`. For the asymptotic
family, take `H` irreducible of degree `t-1>2`.

Set

```text
E(X) = H(X)(X-theta),
B_num(X) = H(X),
b = [H]_E in A=F[X]/E.
```

Then `deg E=t`, `E` is nonzero on `D`, and `b != 0`. Define

```text
U = { [P]_E : P in B[X] } subset A.
```

## Frobenius Envelope

For monic `E in F[X]`, let `E^(p)` be coefficientwise Frobenius conjugation
and let

```text
J = lcm(E,E^(p)).
```

The natural map `B[X] -> F[X]/E` has kernel exactly `(J)`: if `P in B[X]` is
divisible by `E`, then conjugation shows `P` is divisible by `E^(p)`, hence by
`J`; the converse is immediate.

Therefore

```text
U ~= B[X]/J,
dim_B U = deg J.
```

For this construction,

```text
E^(p) = H(X)(X-theta^p),
J = H(X)m_theta(X),
deg J = (t-1)+2 = t+1.
```

Thus

```text
dim_B U = t+1.
```

Equivalently,

```text
dim_B U = 2t - deg gcd(E,E^(p)) = 2t-(t-1)=t+1.
```

## Why `F b subset U`

Chinese remaindering gives

```text
A ~= F[X]/H x F,
[P]_E -> ([P]_H, P(theta)).
```

Under this identification,

```text
U ~= B[X]/H x F.
```

Moreover,

```text
b=[H]_E -> (0,H(theta)).
```

Since `H(theta) != 0`,

```text
F b = {0} x F subset U.
```

So

```text
dim_B(Fb)=2,
codim_U(Fb)=t-1.
```

## Every Cosupport Residue Lands in `U`

Choose an anchor from the base field:

```text
w:D -> B.
```

For `T subset D`, let `S=D\T` and `I_S=interp_S(w)`. Since interpolation
points and values lie in `B`,

```text
I_S in B[X].
```

Therefore

```text
R_T(w)=[I_S]_E in U
```

for every `T`.

Under `U ~= B[X]/J`, the compressed residue is

```text
Rtilde_T(w)=[I_S]_J.
```

## Compressed Exchange-Rank Lemma

Let `S,S' subset D` both have size `a`, with cosupports `T,T'`, and set

```text
r = |T\T'| = |S\S'|,
C0 = S cap S',
tau = deg J = t+1.
```

Assume `a >= tau`. Then

```text
rank_B( w -> (Rtilde_T(w), Rtilde_T'(w)) ) = tau + min(tau,r).
```

The proof is the same interpolation-difference proof: `P-P'` vanishes on
`C0`, so it equals `L_C0 h`, `deg h<r`; conversely choose a representative of
one residue of degree `<tau` and add `L_C0 h`. Since `J` has no roots in `D`,
`[L_C0]_J` is a unit, and the difference space has dimension `min(tau,r)`.

## Random-Anchor Balance

Take `w` uniformly from `B^D`. Let

```text
a=k+t,
j=p-a,
N=binom(p,j),
Lambda=N/p^(t+1).
```

For `u in U`, define

```text
eta_w(u)=#{T: Rtilde_T(w)=u}.
```

For `z in F`, define

```text
nu_w(z)=#{T: R_T(w)=z b}.
```

Each single residue is uniform on `U`, so

```text
E eta_w(u)=Lambda,
E nu_w(z)=Lambda.
```

For fixed `T`, the number of `T'` at exchange distance `r` is

```text
K_r=binom(j,r)binom(a,r).
```

The compressed rank lemma gives the fixed-output probability

```text
Pr(Rtilde_T=u, Rtilde_T'=u) = p^(-(t+1)-min(t+1,r)).
```

Thus

```text
Var eta_w(u), Var nu_w(z)
<= Lambda * sum_{r<t+1} K_r p^(-r).
```

Since

```text
K_r p^(-r) <= (aj/p)^r/(r!)^2
```

and `a+j=p`, the loss is bounded by

```text
C_p <= exp(2 sqrt(aj/p)) <= exp(sqrt p) = 2^{o(p)}.
```

## Deterministic Anchor

Set

```text
Phi_U(w)=sum_{u in U}(eta_w(u)-Lambda)^2,
Phi_F(w)=sum_{z in F}(nu_w(z)-Lambda)^2.
```

The variance bounds imply

```text
E Phi_U <= C_p N,
E Phi_F <= p^2 C_p Lambda.
```

Averaging the normalized quantity

```text
Phi_U/p^(t+1) + Phi_F/p^2
```

gives a deterministic `B`-valued anchor with

```text
Phi_U(w) <= 2 C_p N,
Phi_F(w) <= 2 p^2 C_p Lambda.
```

Consequently, if `Lambda/C_p -> infinity`, the residues are `L^2`-balanced
over `U`. If

```text
Lambda/(p^2 e^(sqrt p)) -> infinity,
```

then

```text
nu_w(z) = (1+o(1)) Lambda
```

uniformly for every `z in F`; in particular, all `p^2` slopes occur.

## Entropy Threshold

Take

```text
k=floor(rho p),
t=floor(C p/log_2 p),
a=k+t,
j=p-a.
```

Since `t=o(p)`,

```text
log_2 binom(p,j) = (H_2(rho)+o(1))p.
```

Therefore

```text
log_2 Lambda
= log_2 binom(p,j) - (t+1)log_2 p
= (H_2(rho)-C+o(1))p.
```

For every strict `C < H_2(rho)`, `Lambda` grows exponentially while
`p^2 e^(sqrt p)=2^{o(p)}`. The selected anchor satisfies

```text
nu_w(z) = (1+o(1)) binom(p,j)/p^(t+1)
```

for every `z in F`.

Thus

```text
#Land = (1+o(1)) p^2 Lambda
      = (1+o(1)) binom(p,j)/p^(t-1),
sum_z nu_w(z)^2 = (1+o(1)) #Land^2/p^2.
```

## Source Validity and Noncontainment

Suppose `R_T(w)=z b`, set `S=D\T`, and let `I_S=interp_S(w)`. Then

```text
I_S equiv zH mod H(X-theta).
```

Hence `H | I_S`; write

```text
I_S = H V.
```

Since `deg I_S<k+t` and `deg H=t-1`,

```text
deg V < k+1.
```

The remaining congruence gives

```text
V(theta)=z.
```

Thus `Q_z=I_S` satisfies

```text
deg Q_z<k+t,
Q_z equiv zB_num mod E,
Q_z=w on S.
```

Noncontainment is automatic: if `G in F[X]_<k` agreed with

```text
-B_num/E = -1/(X-theta)
```

on `S`, then `(X-theta)G+1` would have at least `k+t` roots while having
degree at most `k`, impossible.

## Caveat

The formal degree-`t` datum has

```text
gcd(E,B_num)=H.
```

The supplied source definition does not impose coprimality or minimal
denominator degree, so the construction is literally source-valid. But the
rational direction reduces to

```text
-B_num/E = -1/(X-theta).
```

Let

```text
y(d)=w(d)/H(d) in B.
```

The same witnesses give the reduced degree-one datum

```text
E1=X-theta,
B1=1,
w1=y,
```

because a landing is exactly a polynomial `V in B[X]_<k+1` satisfying

```text
V=y on S,
V(theta)=z.
```

The associated line is

```text
u_z(d)=(y(d)-z)/(d-theta).
```

Thus a later requirement that residue data be reduced would invalidate the
degree-`t` packaging, but not the actual all-slope additive-domain line
construction.

Within the Frobenius-envelope strategy, this common factor is essentially
forced: obtaining

```text
deg lcm(E,E^(p)) = t+1
```

requires a shared Frobenius factor of degree `t-1`, and placing an entire
`F`-line inside the compressed `B`-polynomial image puts `b` on the exceptional
factor.

Confidence in the pasted answer: high for the algebra, pair-rank formula,
variance estimate, and literal source validity; moderate-high for calling the
named wall fully closed until the project confirms that nonminimal denominator
presentations are admissible. The smooth-domain admissibility wall and the
interleaved-list wall remain untouched.
