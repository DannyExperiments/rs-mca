# COUNTERPACKET

**Confidence:** high for the construction and all finite counts; moderate that the eventual complete classifier is exactly the monodromy-genus package described below.

The proposed split-rational classifier is false unless its “exceptional family” clause is enlarged to include the full **elliptic/Lattès branch**. This is not a Möbius-conjugated monomial, an ordinary dihedral/inversion quotient, a projective-subline quotient, or a norm-one quotient.

There is an official dyadic same-field instance carrying an indecomposable degree-(113) split-rational quotient with (144) disjoint full fibers. It produces more than (2^{114}) envelope-free transverse MCA slopes, while:

[
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}<2^{-4335},
]

every fixed-coordinate monomial action rank is full, and the prize threshold is below (2^{113}).

The missing object is a prime-degree CM–Lattès map with geometric monodromy

[
C_{113}\rtimes C_4,
]

whose Galois closure has genus (1).

---

## 1. Exact counterpacket theorem

Let

[
p=65537=2^{16}+1,
\qquad
K=\mathbf F_{p^{15}},
\qquad
q=|K|=p^{15}.
]

Choose (\alpha\in K) of degree (15) over (\mathbf F_p), and put

[
H=\mathbf F_p^\times,
\qquad
L=\alpha H.
]

Then

[
n=|L|=p-1=2^{16},
\qquad
\mathbf F_p(L)=K.
]

Consider the Reed–Solomon code

[
C=\operatorname{RS}[K,L,k],
\qquad
k=\frac n{16}=4096.
]

Set

[
M=\sigma=113,
\qquad
a=k+\sigma=4209,
\qquad
j=n-k-\sigma=61327.
]

There exist:

1. a rational function (R_\alpha\in K(X)) of degree (113);
2. (144) distinct values (y\in\mathbf F_p), each with a full simple (113)-point fiber in (L);
3. a canonical reduced denominator (E\in K[X]) of degree (113), nonvanishing on (L);
4. an envelope-free affine word line
   [
   \mathcal L=f+Kg\subseteq K^L;
   ]
5. exactly
   [
   \Lambda=\binom{144}{37}
   =======================

   32{,}877{,}924{,}651{,}615{,}125{,}350{,}719{,}849{,}588{,}315{,}840

   > 2^{114}
   > ]
   > distinct transverse MCA-bad slopes at agreement (a=k+\sigma);

such that

[
d_{R_\alpha}(E)=1,
]

but, simultaneously,

[
d_D(E)=113
\qquad
\text{for every }D\mid\gcd(n,k)=4096.
]

Moreover, the geometric Galois closure of (R_\alpha) has genus (1) and monodromy group

[
G_{R_\alpha}\cong C_{113}\rtimes C_4.
]

Since (113) is prime, (R_\alpha) is indecomposable.

Thus (R_\alpha) is not generated, even after Möbius equivalence, by the listed genus-zero quotient symmetries.

---

# 2. Construction and proof

## 2.1 The CM elliptic curve

Start with

[
E_0:\quad y^2=x^3-x
]

over (\mathbf F_p). Since (p\equiv1\pmod 8), the elements

[
-1,\quad 2,\quad -2
]

are squares in (\mathbf F_p). The standard halving criterion for the three rational (2)-torsion points therefore gives

[
E_0[4]\subseteq E_0(\mathbf F_p).
]

The geometric endomorphism ring is

[
\operatorname{End}(E_0)=\mathbf Z[i].
]

Let (\pi_0) be Frobenius. It has Gaussian norm (p), and because Frobenius is the identity on (E_0[4]),

[
\pi_0\equiv1\pmod 4
\quad\text{in }\mathbf Z[i].
]

Since

[
p=1^2+256^2,
]

the only Gaussian integers of norm (p) congruent to (1\pmod4) are

[
\pi_0=1\pm256i.
]

Now take the square, non-fourth-power twist

[
E:\quad y^2=x^3-9x.
]

Indeed,

[
9^{(p-1)/4}=9^{16384}\equiv-1\pmod p.
]

Consequently this twist negates Frobenius:

[
\pi=-\pi_0=-1\pm256i.
]

Hence

[
#E(\mathbf F_p)
===============

# \operatorname{Norm}(\pi-1)

# \operatorname{Norm}(-2\pm256i)

65540.

]

Let (\iota) denote the order-four automorphism

[
\iota(x,y)=(-x,256y),
]

where (256^2=-1\pmod p).

Choose the sign (\varepsilon\in{\pm1}) for which

[
\pi=-1+\varepsilon256i.
]

Then

[
\pi-1
=====

# -2+\varepsilon256i

(7+\varepsilon8i)(18+\varepsilon16i).
]

Define the CM endomorphism

[
\phi=[7]+\varepsilon[8]\iota.
]

Its degree is

[
\deg\phi=7^2+8^2=113.
]

Because (\phi\mid(\pi-1)) in (\mathbf Z[i]),

[
\ker\phi\subseteq E(\mathbf F_p).
]

Thus (\ker\phi) is a rational cyclic subgroup of order (113).

The image has size

[
|\phi(E(\mathbf F_p))|
======================

# \frac{65540}{113}

580.

]

---

## 2.2 The degree-(113) Lattès map

The function

[
t=x^2
]

is invariant under (\langle\iota\rangle\cong C_4), and

[
\mathbf F_p(E)^{\langle\iota\rangle}=\mathbf F_p(t).
]

Because (\phi) commutes with (\iota), it induces a unique rational map

[
R\in\mathbf F_p(t)
]

satisfying

[
t(\phi(P))=R(t(P)).
]

The quotient map (E\to E/\langle\iota\rangle\simeq\mathbf P^1) has degree (4). Comparing degrees in

[
\begin{CD}
E @>{\phi}>> E\
@V{t}VV @VV{t}V\
\mathbf P^1 @>{R}>> \mathbf P^1
\end{CD}
]

gives

[
\deg R=\deg\phi=113.
]

Also (R(\infty)=\infty), so it has a reduced representation

[
R(T)=\frac{A_0(T)}{B_0(T)}
]

with

[
A_0\text{ monic},\qquad
\deg A_0=113,\qquad
\deg B_0<113.
]

### Monodromy

The composite (t\circ\phi:E\to\mathbf P^1) is Galois with group

[
G=\ker\phi\rtimes\langle\iota\rangle
\cong C_{113}\rtimes C_4.
]

The (C_4)-action on (C_{113}) is faithful: modulo the Gaussian prime (7+\varepsilon8i), the element (i) has order (4).

The complement (C_4) is core-free in (G). Therefore (E) itself is the geometric Galois closure of (R), and

[
g_{\mathrm{gal}}(R)=1.
]

In particular, (R) is not a genus-zero (\mathrm{PGL}_2) quotient.

It is also not ordinary dihedral. Ordinary degree-(113) dihedral monodromy is (C_{113}\rtimes C_2), whereas here the point stabilizer has order (4), and

[
|G|=452.
]

Finally, since (113) is prime, (R) cannot decompose nontrivially.

---

## 2.3 The (144) full fibers

Put

[
G_0=\phi(E(\mathbf F_p)).
]

The subgroup (G_0) is stable under (\iota) and has (580) points.

The points with nontrivial stabilizer under (C_4) are precisely (E[2]). Indeed,

[
\operatorname{Fix}(\iota^2)=E[2].
]

All four rational (2)-torsion points belong to (G_0); in fact (\phi) acts as the identity on (E[2]), because

[
[7]+\varepsilon[8]\iota\equiv[1]\pmod2.
]

Consequently, the number of free (C_4)-orbits in (G_0) is

[
\frac{580-4}{4}=144.
]

Define

[
Y={x(P)^2:P\in G_0\setminus E[2]}.
]

Then

[
|Y|=144.
]

Every (y\in Y) is nonzero and hence belongs to (H=\mathbf F_p^\times).

Fix (y=x(P)^2\in Y). The equation

[
R(x(Q)^2)=y
]

is equivalent to

[
\phi(Q)\in{P,\iota P,\iota^2P,\iota^3P}.
]

Each of the four equations has (113) solutions, all in (E(\mathbf F_p)), because both (P) and the kernel of (\phi) are rational. The four cosets are disjoint.

The (C_4)-action on these (452) points is free: a point with nontrivial stabilizer would lie in (E[2]), but its image under (\phi) would then also lie in (E[2]), contrary to the choice of (P).

Therefore these (452) points yield exactly

[
\frac{452}{4}=113
]

distinct values (x(Q)^2\in\mathbf F_p^\times).

Thus every (y\in Y) has a full simple (113)-point fiber inside (H), and the (144) fibers are disjoint.

---

## 2.4 Transport to a same-field official domain

Let

[
K=\mathbf F_{p^{15}}
]

and choose (\alpha) of degree (15). Set

[
L=\alpha H.
]

Because (1\in H), the element (\alpha) itself lies in (L), and hence

[
\mathbf F_p(L)=K.
]

Define

[
R_\alpha(X)=R(X/\alpha).
]

Write

[
R_\alpha(X)=\frac{A(X)}{B(X)}
]

where

[
A(X)=\alpha^{113}A_0(X/\alpha),
\qquad
B(X)=\alpha^{113}B_0(X/\alpha).
]

Then (A) is monic of degree (113), while (\deg B<113).

For each (y\in Y),

[
F_y(X)=A(X)-yB(X)
]

is the monic locator of a full (113)-point fiber in (L).

---

## 2.5 Choice of the denominator

There are (144\cdot113=16272) points in the union of the full fibers. Choose a fixed defect set

[
T\subseteq L\setminus\bigcup_{y\in Y}F_y^{-1}(0),
\qquad
|T|=28,
]

and let

[
D_T(X)=\prod_{x\in T}(X-x).
]

For (\mathcal A\in\binom{Y}{37}), define

[
\kappa_{\mathcal A}(Z)=\prod_{y\in\mathcal A}(Z-y).
]

The (\kappa_{\mathcal A}) are distinct monic polynomials of degree (37). Therefore, for (\mathcal A\neq\mathcal A'),

[
\kappa_{\mathcal A}-\kappa_{\mathcal A'}
]

is nonzero of degree at most (36).

Let

[
\Lambda=\binom{144}{37}.
]

Since

[
2^{114}<\Lambda<2^{115},
]

the number of field elements (\theta\in K) causing any slope collision is at most

[
36\binom{\Lambda}{2}<2^{235}.
]

We also exclude:

* the at most (n=2^{16}) values in (R_\alpha(L));
* the at most (2M-2=224) critical values;
* the monomial-action collision parameters discussed below.

But

[
q=p^{15}>2^{240}.
]

Hence a parameter (\theta\in K) exists satisfying all exclusions and for which all values

[
\kappa_{\mathcal A}(\theta)
]

are distinct.

Put

[
E(X)=A(X)-\theta B(X).
]

Then:

[
\deg E=M=113,
]

(E) is squarefree, and

[
E(x)\neq0\qquad(x\in L).
]

Moreover,

[
\gcd(E,B)=1.
]

Define

[
N(X)=\operatorname{rem}_{E}\bigl(D_T(X)B(X)^{37}\bigr).
]

Then

[
\deg N<113,
\qquad
\gcd(E,N)=1.
]

---

## 2.6 The MCA line

For each (\mathcal A\in\binom{Y}{37}), put

[
L_{\mathcal A}(X)
=================

D_T(X)\prod_{y\in\mathcal A}F_y(X).
]

Its degree is

[
\deg L_{\mathcal A}
===================

# 28+37\cdot113

# 4209

k+M.
]

Modulo (E),

[
A\equiv\theta B,
]

so

[
F_y=A-yB\equiv(\theta-y)B\pmod E.
]

Consequently,

[
L_{\mathcal A}
\equiv
\kappa_{\mathcal A}(\theta),N
\pmod E.
]

Set

[
z_{\mathcal A}=-\kappa_{\mathcal A}(\theta).
]

Define

[
Q_{\mathcal A}(X)
=================

E(X)X^k-L_{\mathcal A}(X).
]

Both terms are monic of degree (k+M), so

[
\deg Q_{\mathcal A}<k+M.
]

The residue congruence gives

[
Q_{\mathcal A}-z_{\mathcal A}N\equiv0\pmod E.
]

Therefore

[
P_{\mathcal A}(X)
=================

\frac{Q_{\mathcal A}(X)-z_{\mathcal A}N(X)}{E(X)}
]

is a polynomial satisfying

[
\deg P_{\mathcal A}<k.
]

Now define the word line

[
f(x)=x^k,
\qquad
g(x)=-\frac{N(x)}{E(x)}
\qquad(x\in L).
]

A direct calculation gives

[
f+z_{\mathcal A}g-P_{\mathcal A}
================================

\frac{L_{\mathcal A}}{E}.
]

Hence (f+z_{\mathcal A}g) agrees with the Reed–Solomon codeword (P_{\mathcal A}) exactly on

[
S_{\mathcal A}
==============

T\sqcup
\bigsqcup_{y\in\mathcal A}F_y^{-1}(0),
]

and

[
|S_{\mathcal A}|
================

# 28+37\cdot113

k+\sigma.
]

All (z_{\mathcal A}) are distinct, so the line has exactly

[
\binom{144}{37}>2^{114}
]

constructed bad slopes.

---

## 2.7 Transversality and envelope exclusion

Suppose the direction (g) agreed with a polynomial (G), (\deg G<k), on (S_{\mathcal A}). Then

[
EG+N
]

would vanish on (k+M) points, while

[
\deg(EG+N)<k+M.
]

Thus (EG+N) would vanish identically, contradicting

[
\gcd(E,N)=1.
]

Every incidence is therefore transverse.

The line is also proper-envelope-free. If the syndrome of (f=X^k) belonged to a coordinate span (V_U) with

[
|U|<r=n-k,
]

then (X^k) would agree with a polynomial of degree (<k) on more than (k) points of (L). Their nonzero degree-(k) difference cannot have that many roots.

Therefore

[
\operatorname{span}(\operatorname{syn}(f),\operatorname{syn}(g))
\nsubseteq V_U
\qquad
(|U|<r).
]

This packet is neither tangent nor a proper common-envelope descendant.

---

## 2.8 Canonical denominator and action ranks

The denominator degree (113) is intrinsic. Suppose (g), modulo an RS codeword, had a reduced representation with denominator (E') of degree (t'<113). Cross-multiplication would give a polynomial vanishing on all (n) points of (L), with degree less than

[
k+113+t'<4322<n.
]

It must vanish identically. Reducing modulo (E) and using (\gcd(E,N)=1) would imply

[
E\mid E',
]

which is impossible.

Thus (E) is the canonical reduced denominator.

For the Lattès action,

[
[R_\alpha]_E
============

# [A/B]_E

\theta,
]

and hence

[
\boxed{d_{R_\alpha}(E)=1.}
]

### Full monomial action rank

The map (R_\alpha) has no nontrivial scaling deck transformation. Group-theoretically,

[
\operatorname{Deck}(R_\alpha)
=============================

N_G(C_4)/C_4.
]

In (C_{113}\rtimes C_4), the complement (C_4) is self-normalizing because its action on (C_{113}\setminus{0}) is fixed-point-free. Therefore the deck group is trivial.

For each (D\mid4096) and each nontrivial (D)-th root of unity (\zeta), the equation

[
R_\alpha(\zeta X)=R_\alpha(X)
]

is consequently a nonzero rational equation of degree at most (2M). It gives at most (2M) bad values of (\theta).

Since

[
\sum_{D\mid4096}(D-1)<8192,
]

fewer than

[
2M\cdot8192<2^{21}
]

parameters cause a collision under any fixed-coordinate power action. These parameters were excluded when choosing (\theta).

Thus the map (x\mapsto x^D) is injective on the roots of (E), for every (D\mid4096). Since (E) is squarefree,

[
\boxed{
d_D(E)=\deg E=113
\quad\text{for every }D\mid4096.
}
]

The existing monomial action-rank ledger therefore declares the denominator quotient-free.

---

# 3. Parameter ledger

| Parameter                   |             Exact value or bound |
| --------------------------- | -------------------------------: |
| Base prime                  |                        (p=65537) |
| Code/slope/challenge field  |           (K=\mathbf F_{p^{15}}) |
| Field size                  |      (2^{240}<q<2^{241}<2^{256}) |
| Evaluation subgroup         |           (H=\mathbf F_p^\times) |
| Evaluation domain           | (L=\alpha H), (\mathbf F_p(L)=K) |
| Length                      |                 (n=65536=2^{16}) |
| Rate                        |                      (\rho=1/16) |
| Dimension                   |                         (k=4096) |
| Rational-map degree         |                          (M=113) |
| Reserve                     |                     (\sigma=113) |
| Agreement                   |                         (a=4209) |
| Error support size          |                        (j=61327) |
| Full fibers                 |                            (144) |
| Points per full fiber       |                            (113) |
| Fixed defect                |                      (28) points |
| Fibers selected per support |                             (37) |
| Distinct bad slopes         |        (\binom{144}{37}>2^{114}) |
| Lattès action rank          |              (d_{R_\alpha}(E)=1) |
| Every monomial action rank  |     (d_D(E)=113) for (D\mid4096) |
| Galois-closure genus        |                              (1) |
| Geometric monodromy         |             (C_{113}\rtimes C_4) |

### Occupancy term

Here

[
\frac a n=\frac{4209}{65536}
]

and

[
H_2(a/n)<0.344.
]

Therefore

[
\log_2\binom n a
<
65536(0.344)
<
22545.
]

On the other hand,

[
q^{\sigma-1}>2^{240\cdot112}=2^{26880}.
]

Hence

[
\boxed{
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
<
2^{-4335}.
}
]

This is not an occupancy fluctuation.

### Finite prize threshold

Since

[
q<2^{241},
]

the prize numerator threshold satisfies

[
T_{\mathrm{prize}}
==================

\left\lfloor\frac q{2^{128}}\right\rfloor
<
2^{113}.
]

But

[
|\operatorname{Bad}_\sigma(\mathcal L)|
\ge
\binom{144}{37}

>

2^{114}.
]

Thus

[
\boxed{
|\operatorname{Bad}_\sigma(\mathcal L)|

>

2T_{\mathrm{prize}}.
}
]

The construction respects both official finite caps:

[
k<2^{40},
\qquad
q<2^{256}.
]

---

# 4. Why this defeats the proposed classifier

The map is not in any of the stated genus-zero classes.

### Not monomial

Its monodromy is not cyclic, and (113\nmid |H|=2^{16}). Furthermore, all fixed-coordinate monomial action ranks on the selected denominator are full.

### Not ordinary dihedral/inversion

An ordinary prime-degree dihedral cover has geometric monodromy

[
C_{113}\rtimes C_2
]

and genus-zero Galois closure. Here the monodromy is

[
C_{113}\rtimes C_4
]

and the closure is the elliptic curve (E).

### Not a projective-subline or norm-one quotient

Because (p\nmid452), the tame finite subgroups of (\mathrm{PGL}_2) are cyclic, ordinary dihedral, (A_4), (S_4), and (A_5). The group

[
C_{113}\rtimes C_4
]

is none of these.

Equivalently, every projective-line quotient has genus-zero Galois closure, while this map has genus-one closure.

### Not generated by lower-degree allowed maps

The map has prime degree (113), so it is indecomposable.

### Not a finite sporadic exception

This is a CM–Lattès construction. More generally, elliptic isogenies followed by quotients by elliptic automorphism groups (C_e), with

[
e\in{2,3,4,6},
]

produce whole Lattès families. They are not a finite set of isolated exceptional rational maps.

If “another explicit finite exceptional family” was intended to include all Lattès maps, the statement is repairable, but the Lattès branch must be named and budgeted explicitly. It cannot be hidden inside a finite (\mathrm{PGL}_2)-stabilizer classification.

---

# 5. Bankable structural lemma

The counterpacket points to a canonical replacement for stabilizer classification.

## Galois-closure split-fiber bound

Let (R\in\mathbf F_s(X)) be separable, and let

[
\widetilde C_R\longrightarrow\mathbf P^1
]

be its geometric Galois closure, with group (G_R), genus (g_R), and constant field (\mathbf F_s).

Let (N_{\mathrm{split}}(R)) be the number of unramified values (y\in\mathbf P^1(\mathbf F_s)) for which the entire fiber of (R) splits into distinct (\mathbf F_s)-points.

Then

[
\boxed{
N_{\mathrm{split}}(R),|G_R|
\le
s+1+2g_R\sqrt s.
}
]

### Proof

A fully split unramified value has trivial Frobenius permutation on the roots of (R(X)-y). The geometric monodromy action is faithful, so its Frobenius in the Galois closure is the identity. Therefore the value splits completely in (\widetilde C_R), contributing exactly (|G_R|) rational points.

The fibers over distinct values are disjoint. Hence

[
N_{\mathrm{split}}(R)|G_R|
\le
|\widetilde C_R(\mathbf F_s)|.
]

Apply Hasse–Weil.

For the map above,

[
g_R=1,
\qquad
|G_R|=452,
\qquad
N_{\mathrm{split}}=144,
]

and

[
144\cdot452=65088.
]

This is a genus-one main-term phenomenon, not a small exceptional discrepancy.

---

# 6. Route-board impact

The wall

[
\texttt{W-MCA-PROJECTIVE-SPLIT-RATIONAL-ACTION-RANK-INVERSE}
]

is underspecified. Projective stabilizers do not classify the relevant maps.

The quotient ledger needs at least the following trichotomy.

### Genus-zero quotient templates

These are subgroup-chain covers on (\mathbf P^1):

[
H_0\le G\le\mathrm{PGL}_2,
]

including cyclic, ordinary dihedral, platonic, projective-subline, norm-one and wild additive cases.

### Genus-one quotient templates

These are Lattès/isogeny covers. Over characteristic (>3), their Galois groups have the form

[
A\rtimes C_e,
\qquad
e\in{2,3,4,6},
]

where (A) is a finite elliptic translation subgroup.

The packet above is the case

[
A=C_{113},
\qquad
e=4.
]

Each such map must be charged by

[
d_R(E)=\deg\minpoly([R]_E)
]

and its actual full-fiber support profile.

### Higher-genus discrepancy

Maps with Galois-closure genus at least (2) belong to the primitive finite-discrepancy branch. Their split fibers must be bounded through explicit point counts on their Galois closures or the appropriate subgroup-restricted/Kummer covers.

Thus the natural invariant is not merely the rational formula or the stabilizer of (L), but something like

[
\boxed{
\bigl(
g_{\mathrm{gal}}(R),
G_R,
H_R,
d_R(E),
\text{full-fiber profile}
\bigr).
}
]

The local action-rank idea survives. The proposed finite classifier does not.

---

# 7. What remains open

The counterpacket settles the following point:

[
\boxed{
\text{A genus-zero/projective-stabilizer split-rational classifier is false.}
}
]

It does not yet prove the complete repaired quotient theorem. The remaining issues are:

1. classify and canonically normalize all genus-one Lattès templates relevant to a given smooth domain;
2. prove a bounded-overlap fixed-defect cover for their packets on one affine syndrome line;
3. formulate the subgroup-restricted analogue of the Galois-closure split count for a proper cyclic subgroup (H\subsetneq\mathbf F_s^\times);
4. bound the higher-genus branch by an explicit finite discrepancy small enough for (2^{-128});
5. integrate these templates with hereditary envelope descent;
6. repeat the container step for scalar full-support lists.

## Do you see a route to a full solve?

Yes, but the route is through **monodromy genus**, not through (\mathrm{PGL}_2)-stabilizers alone.

The next exact lemma should be:

[
\boxed{\texttt{W-SRQ-GENUS-0/1-MONODROMY-CONTAINER}}
]

> Let (R:\mathbf P^1\to\mathbf P^1) be a separable split-rational map and let (\widetilde C_R) be its geometric Galois closure.
>
> 1. If (g(\widetilde C_R)=0), prove that (R) is induced by a subgroup chain in a finite subgroup of (\mathrm{PGL}_2), and place it in the cyclic/dihedral/platonic/subline/unit-circle ledger.
> 2. If (g(\widetilde C_R)=1), prove that (R) is induced by a subgroup chain
>    [
>    H_0\le A\rtimes C_e,
>    \qquad e\in{2,3,4,6},
>    ]
>    on an elliptic curve, and place it in an explicit Lattès action-rank ledger.
> 3. Charge every classified packet by
>    [
>    d_R(E)
>    \quad\text{and}\quad
>    \binom{N_R-c_T}{h_R},
>    ]
>    with exact finite overlap accounting.
>
> After this, prove that the (g\ge2) remainder is bounded by the primitive finite-discrepancy term using the Galois-closure point-count bound and its cyclic-domain/Kummer refinement.

The construction above shows that the genus-one clause is mandatory.
