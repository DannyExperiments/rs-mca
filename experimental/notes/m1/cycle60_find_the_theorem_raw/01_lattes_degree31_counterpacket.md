# COUNTERPACKET

**Confidence: high.**

The proposed classifier is false under its natural, nonvacuous interpretation in which “projective-subline quotient” means an intermediate quotient by finite subgroups of the projective stabilizer. The missing family is the **genus-one generalized Lattès/isogeny family**.

There is an explicit same-field, rate-(1/4), dyadic RS instance and an indecomposable degree-(31) split-rational map with (131) disjoint full fibers. It produces more than (2^{127}) noncontained MCA-bad slopes, while:

[
\frac{\binom{n}{k+\sigma}}{|F|^{\sigma-1}}<2^{-325},
]

the line lies in no proper syndrome envelope, and all ordinary monomial and toric-dihedral action ranks are full. Its correct charge is

[
d_R(E)=1
]

for a genus-one Lattès map (R), with full support profile (\binom{131}{67}).

The original finite list can be repaired, but only by replacing it with:

[
\boxed{
\text{genus-zero }PGL_2\text{ quotients}
;+;
\text{genus-one Lattès quotients}
;+;
\text{genus}\ge2\text{ finite discrepancy}.
}
]

---

## 1. The canonical finite theorem package

### Theorem 1: three full subline fibers force descent

Let (K=\mathbb F_{q_0}), let (\Omega/K) be finite, and let

[
R\in \Omega(X),\qquad \deg R=M.
]

Suppose there are three distinct values (y_1,y_2,y_3\in\mathbf P^1(\Omega)) such that each fiber

[
R^{-1}(y_i)
]

consists of (M) distinct points of (\mathbf P^1(K)).

Then there are (\mu\in PGL_2(\Omega)) and

[
R_0\in K(X)
]

such that

[
\mu\circ R=R_0.
]

Thus, after source-conjugating a projective-subline domain to (\mathbf P^1(K)), only three full fibers already force the map to descend to (K), up to target Möbius transformation.

#### Proof

Let (\sigma) be the (q_0)-Frobenius on (\Omega), applied coefficientwise. For every (x\in R^{-1}(y_i)),

[
R^\sigma(x)=R(x)^\sigma=y_i^\sigma,
]

because (x\in\mathbf P^1(K)).

Let (\tau\in PGL_2(\Omega)) be the unique transformation satisfying

[
\tau(y_i)=y_i^\sigma,\qquad i=1,2,3.
]

The rational maps (R^\sigma) and (\tau\circ R), both of degree (M), agree on the (3M) distinct points in the three fibers. The cross-difference of two degree-(M) rational maps has degree at most (2M). Therefore

[
R^\sigma=\tau\circ R.
]

Iteration gives a (PGL_2)-descent cocycle. Since the Brauer group of a finite field is trivial—or equivalently by Lang’s theorem for (PGL_2)—there is a (\mu) satisfying

[
\mu^\sigma\circ\tau=\mu.
]

Consequently

[
(\mu\circ R)^\sigma
===================

# \mu^\sigma\circ R^\sigma

# \mu^\sigma\circ\tau\circ R

\mu\circ R,
]

so (\mu\circ R\in K(X)). ∎

This removes a major ambiguity from the projective-subline branch: a packet-scale number of full fibers does not merely suggest descent; it forces it.

---

### Theorem 2: split-fiber Galois-closure budget

Let (R\in K(X)) be separable of degree (M). Let (X_R) be the arithmetic Galois closure curve of

[
K(X)/K(R),
]

with arithmetic Galois group (G), point stabilizer (H), and genus (g_R). Thus

[
[G:H]=M.
]

Let (s_R) be the number of (K)-rational values whose fibers consist of (M) distinct (K)-rational points. Then

[
\boxed{
s_R|G|
\le
#X_R(K)
\le
q_0+1+2g_R\sqrt{q_0}.
}
]

Equivalently,

[
\boxed{
s_R
\le
\frac{q_0+1+2g_R\sqrt{q_0}}{M|H|}.
}
]

#### Proof

For a full split value (y), Frobenius fixes all (M) sheets, hence acts trivially on (G/H). The action on (G/H) is faithful because (X_R) is the Galois closure, so the Frobenius element is the identity in (G). Thus (y) splits completely in (X_R), contributing (|G|) distinct (K)-rational points.

Different values contribute disjoint point sets. The second inequality is Hasse–Weil. ∎

For a fixed-defect packet using (b) full fibers, this immediately gives the finite profile charge

[
|\Gamma_{R,T}|
\le
\min\left{
|F|,
\binom{s_R-c_T}{b}
\right}
\le
\min\left{
|F|,
\binom{U_R-c_T}{b}
\right},
]

where

[
U_R=
\left\lfloor
\frac{q_0+1+2g_R\sqrt{q_0}}{|G|}
\right\rfloor
]

and (c_T) counts full fibers met by the defect set.

---

### Theorem 3: the low-genus classification

Assume (s_R>0), so (X_R(K)\neq\varnothing).

If (g_R=0), then (X_R\simeq\mathbf P^1_K), and (R) is, up to source and target Möbius transformations, an intermediate quotient

[
\mathbf P^1/H\longrightarrow \mathbf P^1/G
]

for finite subgroups

[
H\le G\le PGL_2(K).
]

This is the genus-zero ledger. Dickson’s list gives the cyclic, nonsplit-cyclic/norm-one, dihedral, polyhedral, affine, and subfield (PSL_2/PGL_2) cases.

If (g_R=1), then (X_R) is an elliptic curve after choosing a rational point. Its finite automorphism group has the form

[
A\rtimes C,
]

where (A) is a finite translation subgroup and (C\le\operatorname{Aut}(E,0)). Hence (R) is an intermediate quotient

[
E/H\longrightarrow E/G,
]

with both quotients genus zero. These are precisely the **generalized Lattès/isogeny maps**.

Therefore the first two canonical quotient branches are not “monomial plus sporadic exceptions.” They are:

[
\boxed{
g_R=0:\text{ finite }PGL_2\text{ quotients},
\qquad
g_R=1:\text{ generalized Lattès quotients}.
}
]

---

### Lemma 4: the prime-dihedral dichotomy

Let (\ell) be an odd prime, with characteristic not dividing (2\ell). Suppose a degree-(\ell) rational map has geometric Galois group (D_{2\ell}) in its natural degree-(\ell) action.

Then precisely two branch signatures are possible:

[
(\ell,2,2),
\qquad\text{or}\qquad
(2,2,2,2).
]

The first has genus-zero Galois closure and is the toric/Chebyshev/Rédei case. The second has genus-one Galois closure and is the Lattès case.

#### Proof

A nontrivial rotation has permutation index (\ell-1). A reflection has index ((\ell-1)/2). If there are (m) rotational and (r) reflection branch points, Riemann–Hurwitz for the degree-(\ell) source (\mathbf P^1) gives

[
m(\ell-1)+r\frac{\ell-1}{2}=2(\ell-1),
]

hence

[
2m+r=4.
]

Generation excludes the rotations-only case. Thus either

[
(m,r)=(1,2)
]

or

[
(m,r)=(0,4).
]

Riemann–Hurwitz for the Galois closure gives genus (0) and (1), respectively. ∎

Thus “dihedral monodromy” is not a sufficiently precise quotient template. The toric and elliptic signatures must be charged separately.

---

## 2. Exact explicit counterpacket

### Field and dyadic domain

Set

[
p=8191=2^{13}-1.
]

This is prime; the Lucas–Lehmer sequence for exponent (13) ends

[
\ldots,3470,128,0\pmod{8191}.
]

Let

[
F=\mathbb F_{p^{18}},
\qquad
q=|F|=8191^{18}.
]

Then

[
2^{233}<q<2^{234}<2^{256}.
]

Since (2\mid18), (F) contains (\mathbb F_{p^2}). Choose (i\in\mathbb F_{p^2}) with

[
i^2=-1,\qquad i^p=-i.
]

Let

[
H={h\in\mathbb F_{p^2}^{\times}:h^{p+1}=1}.
]

Then

[
|H|=p+1=8192=2^{13}.
]

Choose a primitive (\alpha\in F^\times) and set

[
L=\alpha H.
]

Because (\alpha\in L), the field generated by (L) is all of (F). Hence

[
q_{\rm gen}=q_{\rm line}=q_{\rm chal}=q.
]

The Cayley map

[
\beta(t)=\alpha\frac{t-i}{t+i}
]

is a bijection

[
\mathbf P^1(\mathbb F_p)\longrightarrow L.
]

Indeed,

[
\left(\frac{t-i}{t+i}\right)^p
==============================

# \frac{t+i}{t-i}

\left(\frac{t-i}{t+i}\right)^{-1}.
]

Consequently

[
\boxed{
\operatorname{Stab}_{PGL_2(F)}(L)
=================================

\beta,PGL_2(\mathbb F_p),\beta^{-1}.
}
]

This is an exceptional projective-subline domain, not a generic torus coset.

For a dyadic projective subline of size (2^m) in odd characteristic, the subfield size must be (2^m-1). If (2^m-1=r^e) is a prime power, elementary factorization shows (e=1); hence the subfield size is necessarily a Mersenne prime. The present (8191) case is therefore exactly one of the genuine exceptional stabilizer cases.

---

### The elliptic isogeny

Consider

[
E:\qquad Y^2=X^3+X+459
]

over (\mathbb F_{8191}).

Its discriminant is

[
-16(4+27\cdot459^2)\equiv4136\not\equiv0\pmod{8191}.
]

The exact finite character sum is

[
\sum_{x\in\mathbb F_{8191}}
\chi(x^3+x+459)=-39,
]

so

[
#E(\mathbb F_p)
===============

# p+1-39

# 8153

31\cdot263.
]

The point

[
G=(0,7904)
]

satisfies

[
[263]G=(8050,6188),\qquad
[31]G=(3434,924),
]

both nonzero. Hence (G) has order (8153). Let

[
K=\langle(8050,6188)\rangle.
]

Then

[
|K|=31.
]

Let

[
\phi:E\longrightarrow E'=E/K
]

be the degree-(31) Vélu isogeny.

The induced map on the quotients by inversion is

[
\lambda:\mathbf P^1_x=E/{\pm1}
\longrightarrow
\mathbf P^1_{x'}=E'/{\pm1},
\qquad
x(\phi(P))=\lambda(x(P)).
]

It has degree (31).

An exact rational-function specification is available directly from Vélu. Put

[
f(X)=X^3+X+459
]

and let the (x)-coordinates of the fifteen nonzero ({\pm1})-orbits in (K) be

[
\begin{aligned}
U={&
814,1493,2194,2615,2698,2895,3776,4279,\
&5486,5537,6235,7216,7905,8013,8050
}.
\end{aligned}
]

Then, with arithmetic modulo (8191),

[
\boxed{
\lambda(X)
==========

X+
\sum_{u\in U}
\left(
\frac{2(f(X)+f(u))}{(X-u)^2}
-2X-4u
\right).
}
]

Its denominator is

[
\prod_{u\in U}(X-u)^2,
]

of degree (30), and its numerator has degree (31).

---

### The (131) full fibers

The rational image group is

[
\phi(E(\mathbb F_p)),
]

of order

[
\frac{8153}{31}=263.
]

For every nonzero

[
P'\in\phi(E(\mathbb F_p)),
]

the fiber of (\lambda) over (x(P')) is

[
{x(Q):\phi(Q)=P'\text{ or }-P'}.
]

The two rational (K)-cosets contain (62) points. Inversion pairs them without fixed points, since (P') has odd order. Thus the fiber consists of exactly

[
31
]

distinct points of (\mathbf P^1(\mathbb F_p)).

There are

[
\frac{263-1}{2}=131
]

such values. Directly, the rational-fiber distribution of (\lambda) is

[
31^{131},\qquad 16^1,\qquad 1^{4115},
]

whose total is

[
131\cdot31+16+4115=8192.
]

To make the map pole-free on the evaluation domain, use

[
\eta(Y)=\frac1{Y-\alpha}.
]

Since

[
\lambda(\mathbf P^1(\mathbb F_p))
\subseteq\mathbf P^1(\mathbb F_p)
]

and (\alpha\notin\mathbb F_p), (\eta\circ\lambda) has no pole on the subline.

Define

[
\boxed{
R=\eta\circ\lambda\circ\beta^{-1}\in F(X).
}
]

Then:

[
\deg R=31,
]

its denominator is nonzero on (L), and it has (131) disjoint full (31)-point fibers inside (L).

---

## 3. Why this map is outside the proposed finite ledger

The geometric Galois closure of (\lambda) is (E). Its group is

[
K\rtimes{\pm1}\simeq D_{62},
]

and its branch signature is

[
(2,2,2,2).
]

Thus its Galois-closure genus is (1). It is not Möbius-equivalent to:

[
X^{31},
]

a Chebyshev/Dickson map, a Rédei/norm-one torus quotient, or any other genus-zero cyclic or dihedral quotient.

The deck group of (\lambda) is trivial. Indeed, in (D_{62}), the normalizer of a reflection subgroup is the reflection subgroup itself. Hence the map is not a quotient by a nontrivial projective automorphism of its source.

It is also not a projective-subline group quotient. Such a degree-(31) quotient would require an index-(31) subgroup inside

[
PGL_2(\mathbb F_{8191}),
]

and hence (31) would divide

[
|PGL_2(\mathbb F_{8191})|
=========================

8191\cdot8190\cdot8192.
]

But the three factors are respectively congruent to

[
7,\ 6,\ 8\pmod{31},
]

so

[
31\nmid |PGL_2(\mathbb F_{8191})|.
]

Finally, (\deg R=31) is prime, so (R) is indecomposable.

Therefore:

[
\boxed{
R\text{ is an indecomposable genus-one Lattès quotient,
not a genus-zero toric or }PGL_2\text{ quotient.}
}
]

If “projective-subline quotient” is instead defined to include every rational map that descends to the subfield, then the term becomes tautological and does not provide a finite classifier.

---

## 4. MCA packet construction

Take

[
C=\operatorname{RS}[F,L,k],
\qquad
n=8192,
\qquad
k=2048.
]

Set

[
\sigma=M=31.
]

Then the agreement size and error size are

[
a=k+\sigma=2079,
\qquad
j=n-a=6113.
]

Thus

[
\delta=\frac{6113}{8192}.
]

Let (B_0) be the set of the (131) full-fiber values of (R).

Choose

[
b=67,
\qquad
d=2.
]

Then

[
d+bM=2+67\cdot31=2079=k+\sigma.
]

The union of all (131) full fibers has size

[
131\cdot31=4061,
]

so its complement in (L) has (4131) points. Choose a fixed two-point set

[
T\subseteq L
]

outside this union.

Write

[
R(X)=\frac{P(X)}{Q(X)}
]

in reduced form, with (Q) nonzero on (L). For (y\in B_0), let

[
L_y(X)=\frac{P(X)-yQ(X)}{a_y},
]

where (a_y) is the leading coefficient. Then (L_y) is the monic locator of the corresponding (31)-point fiber.

Choose (\theta\in F) outside:

[
R(L),
\quad
\operatorname{Br}(R),
\quad
{R(\infty)},
]

and the finite action-collision loci described below. Define

[
E(X)=\frac{P(X)-\theta Q(X)}{a_\theta}.
]

Then (E) is monic, squarefree, has degree (31), and has no root in (L).

Let

[
L_T(X)=\prod_{x\in T}(X-x)
]

and let (B(X)), of degree (<31), represent

[
L_T(X)Q(X)^{67}\pmod E.
]

Because (E) is coprime to (L_TQ),

[
[B]_E\in(F[X]/E)^\times.
]

For

[
A\in\binom{B_0}{67},
]

put

[
S_A=T\sqcup\bigcup_{y\in A}R^{-1}(y)
]

and

[
L_A=L_T\prod_{y\in A}L_y.
]

Then (L_A) is monic of degree (2079=k+31). Modulo (E),

[
L_A
\equiv
\kappa_A(\theta)B,
]

where

[
\kappa_A(\theta)
================

\prod_{y\in A}\frac{\theta-y}{a_y}.
]

Set

[
z_A=-\kappa_A(\theta).
]

Now define

[
N_A=EX^k-L_A.
]

The leading terms cancel, so

[
\deg N_A<k+31.
]

Furthermore,

[
N_A-z_AB\equiv0\pmod E.
]

Hence

[
C_A=\frac{N_A-z_AB}{E}
]

is a polynomial of degree (<k).

On (S_A), (L_A=0), so

[
C_A(x)
======

x^k-z_A\frac{B(x)}{E(x)}.
]

Thus on the affine word line

[
f=X^k,
\qquad
g=-\frac BE,
]

the slope (z_A) agrees with the RS codeword (C_A) on the (2079)-point set (S_A).

Therefore every distinct (z_A) is MCA-bad at reserve (31).

---

### Transversality

Suppose (g) agreed with a degree-(<k) polynomial (G) on (S_A). Then

[
EG+B
]

would vanish on (k+31) points while having degree (<k+31). Hence it would be identically zero, contradicting

[
\gcd(E,B)=1.
]

Thus the syndrome direction is not in the witness subspace:

[
v\notin V_{L\setminus S_A}.
]

All witnesses are transverse.

---

### No proper common envelope

Suppose the syndrome of (X^k) lay in (V_R) for some

[
|R|<n-k=6144.
]

Then (X^k) would agree with a polynomial of degree (<k) on more than (k) evaluation points. Their difference is a nonzero polynomial of degree (k), impossible.

Therefore the entire line is contained in no proper syndrome envelope.

---

### Exact denominator degree

The presentation

[
g=-B/E
]

is reduced. If it admitted another reduced denominator (E') with

[
\deg E'\le31,
]

then

[
k+\deg E+\deg E'
\le
2048+62
<
8192.
]

Canonical denominator uniqueness therefore forces (E') to be associated to (E). The intrinsic denominator degree is exactly (31).

---

## 5. Number of distinct slopes

Let

[
L_0=\binom{131}{67}
===================

183062151498210163887302260440097215750.
]

For (A\neq A'), the polynomials

[
\prod_{y\in A}\frac{T-y}{a_y}
\quad\text{and}\quad
\prod_{y\in A'}\frac{T-y}{a_y}
]

are distinct and have degree (67). Hence their difference has at most (67) roots.

The good set of (\theta)'s has size (>q/2). Summing all pair-collision incidences and averaging gives a (\theta) for which the number of colliding unordered pairs is at most

[
\left\lfloor
\frac{67L_0(L_0-1)}q
\right\rfloor
=============

81509318.

]

Deleting repetitions therefore leaves at least

[
\begin{aligned}
L_0-81509318
&=
183062151498210163887302260440015706432\
&>2^{127}
\end{aligned}
]

distinct noncontained bad slopes.

Thus

[
\boxed{
|\operatorname{Bad}_{31}(u,v)|>2^{127}.
}
]

---

## 6. Action-rank audit

By construction,

[
P\equiv\theta Q\pmod E.
]

Since (Q) is a unit modulo (E),

[
[R]_E=\theta.
]

Therefore

[
\boxed{
d_R(E)=\deg\minpoly([R]_E)=1.
}
]

In contrast, (\theta) may be chosen so that every ordinary monomial action has full rank.

Let (D\mid k=2048). If two roots (r_1,r_2) of (E) satisfy

[
r_1^D=r_2^D,
]

then

[
r_2=\zeta r_1
]

for some (\zeta\in\mu_D\subseteq\mu_{2048}). Both roots lie in the same (R)-fiber, so (r_1) solves

[
R(\zeta X)=R(X).
]

For (\zeta\neq1), this is not an identity because (R) has trivial deck group. It has at most (2\deg R=62) solutions. Taking the union over (\mu_{2048}) excludes fewer than (62\cdot2048) values of (\theta).

The same argument applies to the natural toric-dihedral relations

[
r_2=\zeta\frac{\alpha^2}{r_1}.
]

Consequently (\theta) can simultaneously satisfy

[
\boxed{
d_{X^D}(E)=31
\quad\text{for every }D\mid2048,
}
]

and full rank for the corresponding multiplicative inversion invariants.

Thus the packet is invisible to the monomial and natural toric-dihedral action-rank ledgers.

---

## 7. Occupancy and finite-threshold ledger

The unavoidable occupancy scale is

[
\frac{\binom{8192}{2079}}{q^{30}}.
]

With

[
\rho=\frac{2079}{8192},
\qquad
H_2(\rho)=0.817220999\ldots,
]

and

[
\log_2q=233.9968298\ldots,
]

the entropy bound gives

[
\begin{aligned}
\log_2
\frac{\binom{8192}{2079}}{q^{30}}
&\le
8192H_2(\rho)-30\log_2q\
&<
-325.23.
\end{aligned}
]

Hence

[
\boxed{
\frac{\binom{8192}{2079}}{q^{30}}<2^{-325}.
}
]

This packet is not an occupancy fluctuation.

The exact target numerator is

[
T_q
===

# \left\lfloor\frac q{2^{128}}\right\rfloor

80951559894234747884481262824352
<
2^{106}.
]

The packet has more than (2^{127}) bad slopes, exceeding the target by more than (21) bits. Its normalized bad-slope fraction satisfies

[
\frac{|\operatorname{Bad}_{31}(u,v)|}{q}

>

# \frac{2^{127}}{2^{234}}

2^{-107}

>

2^{-128}.
]

---

## 8. Parameter ledger

| Quantity              |                                            Exact value |
| --------------------- | -----------------------------------------------------: |
| Prime subfield        |                                      (p=8191=2^{13}-1) |
| Code field            |                              (F=\mathbb F_{8191^{18}}) |
| Field size            |                            (2^{233}<q<2^{234}<2^{256}) |
| Domain                | (L=\alpha H), (H=\ker N_{\mathbb F_{p^2}/\mathbb F_p}) |
| Domain size           |                                        (n=8192=2^{13}) |
| Generated field       |                                             (F_p(L)=F) |
| Rate                  |                                                  (1/4) |
| Dimension             |                                               (k=2048) |
| Reserve / map degree  |                                          (\sigma=M=31) |
| Agreement             |                                               (a=2079) |
| Errors                |                                               (j=6113) |
| Full fibers           |                                                (s=131) |
| Fibers per support    |                                                 (b=67) |
| Fixed defect          |                                                  (d=2) |
| Raw profile           |                   (\binom{131}{67}=2^{127.1056\ldots}) |
| Distinct bad slopes   |                                             (>2^{127}) |
| Prize threshold       |                                          (T_q<2^{106}) |
| Occupancy             |                                            (<2^{-325}) |
| Galois closure        |                              genus (1), group (D_{62}) |
| Correct action rank   |                                             (d_R(E)=1) |
| Monomial action ranks |                               (31) for all (D\mid2048) |

---

## 9. The two-point defect is not essential

On the same field and domain, take

[
E_0:\quad Y^2=X^3-X.
]

Since (8191\equiv3\pmod4),

[
#E_0(\mathbb F_p)=8192.
]

Moreover,

[
E_0(\mathbb F_p)\simeq \mathbb Z/2\mathbb Z\times\mathbb Z/4096\mathbb Z.
]

The point

[
(6,7577)
]

has order (4096), and

[
(2644,2777)=[128](6,7577)
]

has order (32). Quotienting by its order-(32) subgroup gives a degree-(32) Lattès map with (126) full rational fibers.

Now

[
k=64\cdot32,
\qquad
\sigma=32,
\qquad
k+\sigma=65\cdot32.
]

Thus supports are pure unions of (65) fibers; there is no fixed core:

[
d=0.
]

The same construction gives

[
|\operatorname{Bad}_{32}(u,v)|>2^{122},
]

while

[
\frac{\binom{8192}{2080}}{q^{31}}<2^{-557}.
]

This companion packet occurs at

[
\delta=\frac{6112}{8192}=\frac{191}{256}
]

and shows that the Lattès phenomenon is not an artifact of the two-point defect in the prime-degree construction.

---

## 10. Projective RS automorphisms

For completeness, if

[
\varphi(X)=\frac{aX+b}{cX+d}
]

preserves (L), then (cx+d\neq0) on (L), and the corresponding monomial automorphism of the RS code is

[
(v_x)*{x\in L}
\longmapsto
\left(
(cx+d)^{k-1}v*{\varphi(x)}
\right)_{x\in L},
]

up to a global scalar.

Indeed, for (\deg f<k),

[
(cx+d)^{k-1}
f!\left(\frac{ax+b}{cx+d}\right)
]

is a polynomial of degree at most (k-1).

Therefore quotient classification must be invariant under the projective stabilizer of (L). In the present example that stabilizer is the full conjugate of (PGL_2(\mathbb F_{8191})), not merely the torus normalizer.

---

## Route-board impact

The proposed split-rational classifier needs the following changes.

1. **Add a genus-one Lattès branch.** This is an infinite algebraic family parametrized by elliptic curves, finite translation subgroups, origin automorphisms, and intermediate quotient groups. It is not a sporadic correction.

2. **Classify by Galois-closure geometry, not only by formulas.**

   [
   \begin{array}{c|c}
   g_R=0 & PGL_2\text{-group quotients}\
   g_R=1 & \text{generalized Lattès/isogeny quotients}\
   g_R\ge2 & \text{primitive finite discrepancy}
   \end{array}
   ]

3. **Distinguish the two dihedral signatures.** Toric dihedral maps have signature ((M,2,2)); elliptic Lattès maps have signature ((2,2,2,2)). Abstract group (D_{2M}) does not determine the quotient template.

4. **Bank the three-fiber descent lemma.** On an exceptional projective subline, packet-scale splitting automatically descends the map to the subfield after a target Möbius transformation.

5. **Replace the current wall by two walls:**

   [
   \texttt{W-MCA-LATTES-SPLIT-RATIONAL-QAR-COVER}
   ]

   and

   [
   \texttt{W-SRQ-HIGH-GENUS-FROBENIUS-DISCREPANCY-CONTAINER}.
   ]

This is not a counterexample to an upper theorem already containing all split-rational maps. It is a counterpacket to the proposed finite genus-zero quotient ledger and identifies the exact missing family.

---

## What remains open

The low-genus taxonomy is now canonical, but three substantial steps remain.

First, the genus-one classification must be converted into a line-level finite cover theorem: all Lattès witnesses on one affine syndrome line must be grouped into a controlled number of fixed-defect Lattès-QAR packets.

Second, the (g_R\ge2) branch remains. For an individual map the exact finite bound

[
s_R
\le
\left\lfloor
\frac{q_0+1+2g_R\sqrt{q_0}}{|G_R|}
\right\rfloor
]

is bankable, but summing these profiles over all primitive pencils occurring on one line is not controlled.

Third, one still needs the extraction theorem connecting a large syndrome transverse-secant family to a bounded collection of maximal split pencils (R=P/Q). Action rank is a valid invariant after a pencil has been found; it is not yet a line-level classifier.

## Do you see a route to a full solve?

Yes, but not through the original genus-zero list.

The next exact construction is a **Lattès fixed-defect QAR registry**. A certificate should consist of

[
(K,E,A,H,G,T,R),
]

where (E/K) is elliptic, (A) is a finite translation subgroup, (H\le G\le A\rtimes\operatorname{Aut}(E,0)), (E/H\simeq E/G\simeq\mathbf P^1), (T) is the defect set, and (R:E/H\to E/G) is the resulting rational map. For each certificate, the exact packet charge is

[
\left|
\mathcal P_{R,T}^{(b)}(E_{\rm den})
\cap
\bigl(\Phi([R]) + F\Psi([R])\bigr)
\right|
\le
\min\left{
|F|,
\binom{s_R-c_T}{b}
\right},
]

refined by

[
d_R(E_{\rm den})
================

\deg\minpoly([R]*{E*{\rm den}}).
]

After this registry is banked, the next genuinely hard lemma is:

> **Primitive high-genus split-pencil discrepancy lemma.**
> After removing all genus-zero and genus-one quotient packets and all proper syndrome envelopes, every remaining maximal split pencil has Galois-closure genus (g\ge2), and the sum of its realized full-fiber profiles over one affine syndrome line is bounded by the explicit Hasse–Frobenius discrepancy budget, rather than by the raw binomial profiles.

A counterexample to that lemma would need a genus-(\ge2), indecomposable rational pencil on a dyadic domain that clears occupancy, has no low-genus common right factor, and still realizes more than the finite primitive discrepancy allowance. That is now the exact unresolved construction target.
