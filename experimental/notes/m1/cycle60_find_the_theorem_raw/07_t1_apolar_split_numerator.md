BANKABLE_LEMMA

**Confidence:** high for the exact reductions below; unknown for the proposed primitive finite bound. I found neither a proof of that bound nor a primitive packet violating it.

## Exact theorem package

### Theorem 1 — Critical-seed collapse

Let (H\in F^{R\times n}) be the jet–residue parity-check matrix, let (\lambda\in(F^n)^*) be its color functional, and suppose every set of at most (j) columns of (H) is independent. For a syndrome (s\in F^R), define

[
\mathscr R(s):=
\left{
(T,c):
|T|\le j,\quad
c\in(F^\times)^T,\quad
H_Tc=s
\right},
]

and define the reduced color

[
\chi(T,c):=-\lambda_Tc.
]

The additive constant (\lambda(w)) in the actual slope is irrelevant to distinctness. Put

[
Z(s):={\chi(T,c):(T,c)\in\mathscr R(s)}.
]

Let

[
\mathfrak S=((T_i,c_i))_{i=1}^{\ell}
]

be any full-coordinate, distinct-color seed with

[
H_{T_i}c_i=s_0.
]

Then the set of additional distinct-color completions through the seed is exactly

[
\boxed{
\operatorname{Comp}(\mathfrak S)
================================

Z(s_0)\setminus
{\chi(T_1,c_1),\ldots,\chi(T_\ell,c_\ell)}.
}
]

In particular,

[
\boxed{
|\operatorname{Comp}(\mathfrak S)|=|Z(s_0)|-\ell.
}
\tag{1}
]

Conversely, any syndrome (s_0) with (|Z(s_0)|\ge\ell) produces a seed of size (\ell), by selecting one full-coordinate representation for each of (\ell) colors.

Consequently, for any proposed bound (B),

[
\boxed{
\begin{aligned}
&\text{every size-(\ell) seed has at most (B) completions}\
&\qquad\Longleftrightarrow\
&|Z(s)|\le B+\ell
\quad\text{for every syndrome admitting such a seed.}
\end{aligned}}
\tag{2}
]

For the critical arity

[
\ell_*=
\left\lceil\frac{R}{\sigma-1}\right\rceil,
\qquad
R=n-k-1=j+\sigma-1,
]

this says that `W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION` is, up to the additive (O(\ell_*)) term, precisely the original colored full-secant local-limit theorem.

It is not a logically weaker intermediate theorem.

---

### Proof

Once one seed element ((T_i,c_i)) is specified, its common syndrome is already known:

[
s_0=H_{T_i}c_i.
]

Adding another block ((T,c)) to the block-kernel certificate means exactly

[
H_Tc=s_0.
]

No equation involving the other seed members remains. Distinctness from the existing slopes is exactly the condition that (\chi(T,c)) avoid their colors. This proves (1).

Conversely, choosing representations of any (\ell) colors in (Z(s_0)) gives a common-syndrome block-kernel vector. The dimension-critical inequality

[
\ell_*j\le(\ell_*-1)R
]

makes this vector an algebraically exceptional kernel vector relative to generic supports, but it does not impose an additional condition after the coefficients (c_i) are included in the seed.

Thus the critical kernel remains valuable as a support-only inverse certificate, but conditioning on a full-coordinate seed does not reduce the completion problem.

---

## The (t=1) canonical normal form

The lowest jet–residue stratum already contains a canonical version of the unresolved wall.

Choose

[
t=1,\qquad E=X-\beta,\qquad \beta\notin D,\qquad B=1.
]

Then

[
U_{E,1}=(X-\beta)\mathcal P_k\oplus F
=\mathcal P_{k+1},
]

because polynomial division at (X=\beta) gives uniquely

[
Q=(X-\beta)G+Q(\beta).
]

Hence:

[
\boxed{
t=1\text{ jet–residue decoding is ordinary }
\operatorname{RS}[F,D,k+1]
\text{ decoding, with color }Q\mapsto Q(\beta).
}
\tag{3}
]

Its parameters are

[
R=n-k-1,\qquad
j=n-k-\sigma,\qquad
R-j=\sigma-1.
]

Thus the (t=1) stratum is the scalar RS problem for dimension (k+1) at reserve (\sigma-1), enhanced by an external evaluation color.

This stratum has an exact apolar complete-intersection description.

---

### Theorem 2 — Apolar complete-intersection completion normal form

After the standard nonzero GRS column rescaling, take the parity-check columns of (\operatorname{RS}[F,D,k+1]) to be

[
h_x=(1,x,\ldots,x^{R-1})^{\mathsf T}.
]

Let (S=F[X_0,X_1]), and identify a nonzero syndrome (s\in F^R) with a linear functional

[
\Lambda_s:S_{R-1}\longrightarrow F.
]

For each degree (e), define

[
(I_s)*e:=
\left{
P\in S_e:
\Lambda_s(PQ)=0
\text{ for every }Q\in S*{R-1-e}
\right}.
\tag{4}
]

These spaces form a homogeneous Artinian ideal (I_s\subset S).

For a (j)-set (T\subseteq D), write its homogeneous locator as

[
P_T(X_0,X_1)=
\prod_{x\in T}(X_1-xX_0).
]

Then:

#### 1. Exact locator criterion

[
\boxed{
s\in V_T
\iff
P_T\in (I_s)_j.
}
\tag{5}
]

#### 2. Complete-intersection structure

There are coprime homogeneous forms (A,B), unique up to the usual changes of complete-intersection generators, such that

[
\boxed{
I_s=(A,B),
}
\tag{6}
]

with

[
\deg A=d,\qquad
\deg B=R+1-d=j+\sigma-d,
\tag{7}
]

where the generators may be ordered so that

[
1\le d\le\frac{R+1}{2}.
]

#### 3. Exact envelope dichotomy

If

[
d<\sigma,
]

then (\deg B>j), and therefore

[
\boxed{
(I_s)*j=A,S*{j-d}.
}
\tag{8}
]

If any (D)-split locator (P_T) occurs, then (A\mid P_T). Consequently (A) is itself a squarefree (D)-split locator

[
A\sim P_{\Delta}
]

for some (\Delta\subseteq D), (|\Delta|=d), and

[
\boxed{
s\in V_\Delta,\qquad
\Delta\subseteq T
\text{ for every completion}.
}
\tag{9}
]

Thus:

[
\boxed{
\text{envelope-free syndrome}
\Longrightarrow d\ge\sigma.
}
\tag{10}
]

#### 4. Primitive two-generator slice

If (d\ge\sigma), put

[
b:=j+\sigma-d,\qquad
u:=j-d,\qquad
v:=d-\sigma.
]

Then

[
u,v\ge0,\qquad u+v=j-\sigma,
]

and

[
\boxed{
(I_s)_j
=======

A,S_u\oplus B,S_v.
}
\tag{11}
]

Hence every completion locator has a unique expression

[
\boxed{
P_T=A,U_T+B,V_T,
\qquad
\deg U_T=u,\quad
\deg V_T=v,
}
\tag{12}
]

where lower degrees are allowed by homogenization.

#### 5. Full-coordinate criterion

The representation on (T) has every error coefficient nonzero if and only if

[
\boxed{
\gcd(U_T,V_T)=1.
}
\tag{13}
]

#### 6. Rational-approximation interpretation

For a coprime pair ((U_T,V_T)), every (x\in T) belongs to exactly one of the following:

[
A(x)=V_T(x)=0,
\tag{14}
]

or

[
A(x)V_T(x)\ne0,
\qquad
\frac{U_T(x)}{V_T(x)}
=====================

-\frac{B(x)}{A(x)}.
\tag{15}
]

Thus

[
\boxed{
T=
Z_D(A,V_T)
;\dot\cup;
\left{
x\in D:
A(x)V_T(x)\ne0,;
U_T(x)/V_T(x)=-B(x)/A(x)
\right},
}
\tag{16}
]

and the defect satisfies

[
|Z_D(A,V_T)|\le d-\sigma.
\tag{17}
]

#### 7. Exact pair separation

For two distinct full-coordinate completions (T_i,T_h), put

[
C_{ih}:=U_iV_h-U_hV_i.
]

Then (C_{ih}\ne0),

[
\deg C_{ih}\le u+v=j-\sigma,
]

and every point of (T_i\cap T_h) is a root of (C_{ih}). Therefore

[
\boxed{
|T_i\cap T_h|\le j-\sigma,
\qquad
|T_i\setminus T_h|\ge\sigma.
}
\tag{18}
]

This recovers the far-support condition without a separate pair-rank calculation.

---

## Proof of Theorem 2

For (5), the degree-((R-1)) forms vanishing on (T) are exactly

[
P_T S_{R-1-j}=P_T S_{\sigma-2}.
]

These are (V_T^\perp) under the syndrome pairing. Hence (s\in V_T) exactly when (\Lambda_s) annihilates (P_TS_{\sigma-2}), which is (P_T\in(I_s)_j).

The quotient (S/I_s) has perfect multiplication pairings

[
(S/I_s)*e\times(S/I_s)*{R-1-e}\longrightarrow F,
\qquad
(P,Q)\longmapsto\Lambda_s(PQ).
]

It is therefore an Artinian graded Gorenstein algebra of codimension two and socle degree (R-1). Its minimal graded resolution has type one. By the height-two Hilbert–Burch structure, its defining ideal has two generators forming a regular sequence. If their degrees are (d\le b), the socle degree of the complete intersection is

[
d+b-2=R-1,
]

so

[
d+b=R+1.
]

This proves (6)–(7).

If (d<\sigma), then

[
b=j+\sigma-d>j,
]

so only multiples of (A) occur in degree (j). If (A\mid P_T) and (P_T) is squarefree and split over (D), every factor of (A) is a distinct (D)-linear factor. Moreover (A\in I_s) means that (s) annihilates

[
A S_{R-1-d}=V_\Delta^\perp,
]

giving (s\in V_\Delta). This proves the envelope statement.

If (d\ge\sigma), both generators contribute in degree (j). Their degree-(j) multiples cannot intersect nontrivially, since a common multiple would be divisible by (AB), whose degree is

[
\deg AB=j+\sigma>j.
]

This proves the direct sum (11).

Now let (P_T=AU+BV). If a nonconstant split factor (G) divides both (U) and (V), then

[
P_T/G=A(U/G)+B(V/G)\in I_s.
]

Thus (s) is represented on the proper subset obtained by deleting a root of (G), and the unique coefficient vector on (T) has a zero coordinate.

Conversely, if the coefficient at (x\in T) vanishes, then

[
s\in V_{T\setminus{x}},
]

so (P_T/(X_1-xX_0)\in I_s). Multiplying its (A,B)-decomposition by (X_1-xX_0) and using uniqueness in (11) shows that this linear factor divides both (U) and (V). This proves (13).

Equation (16) follows directly from (AU+BV=0). If (V(x)=0) and (A(x)\ne0), coprimality gives (U(x)\ne0), so (x) cannot be a root. Hence the only exceptional roots satisfy (A(x)=V(x)=0), of which there are at most (\deg V=d-\sigma).

Finally,

[
V_hP_i-V_iP_h=A(U_iV_h-U_hV_i)=AC_{ih},
]

and

[
U_hP_i-U_iP_h=-B,C_{ih}.
]

At a common root of (P_i,P_h), both (AC_{ih}) and (BC_{ih}) vanish. Since (\gcd(A,B)=1), the point is a root of (C_{ih}). If (C_{ih}=0), the two coprime pairs represent the same rational function and are scalar multiples; monicity then gives (P_i=P_h). This proves (18).

---

## Canonicality consequence

The canonical object is not a chosen rational function (B/A). It is the graded complete-intersection ideal

[
I_s=(A,B)
]

and its split degree-(j) slice.

When (\deg B>\deg A), replacing

[
B\longmapsto cB+AC
]

induces the compensating change

[
(U,V)\longmapsto
\left(U-\frac{C}{c}V,\frac{V}{c}\right)
]

and leaves (AU+BV) unchanged. Thus (B/A) is subject to a polynomial shear, not merely a constant Möbius transformation.

Therefore a canonical quotient exception cannot be defined solely from one selected ratio (R=B/A) or from its action rank. It must be defined on the split-numerator module, or equivalently on the family of supports generated by the degree slice ((I_s)_j). At the equal-degree point, the ambiguity becomes the expected projective (GL_2/PGL_2) ambiguity.

This is the exact (t=1) version of the line-intrinsic quotient-classifier problem identified in Cycle 59.

---

## External-color separation

The (t=1) stratum is also quantitatively close to the scalar full-support list problem.

Let (\mathcal L\subseteq\mathcal P_{k+1}) contain (L) distinct polynomials. For (\beta\in F\setminus D), let

[
m(\beta)=|{Q(\beta):Q\in\mathcal L}|.
]

For a fixed pair (Q\ne Q'), the polynomial (Q-Q') has degree at most (k), and therefore the pair collides at at most (k) field points. Summing collision pairs over (\beta\in F\setminus D) gives

[
\sum_{\beta\notin D}
\sum_y\binom{|{Q:Q(\beta)=y}|}{2}
\le
k\binom L2.
]

Consequently, if (q>|D|=n), some (\beta\notin D) satisfies

[
\boxed{
m(\beta)
\ge
\frac{L}
{1+\dfrac{k(L-1)}{q-n}}.
}
\tag{19}
]

For this (\beta), setting (E=X-\beta) converts those (m(\beta)) codewords into distinct jet–residue colors without changing their full agreement supports.

Thus, whenever (kL\ll q-n), the (t=1) colored wall contains the scalar list wall with negligible loss. No such near-injective conclusion follows when (D) nearly fills (F), and this field-size caveat is essential.

---

## Parameter ledger

| Quantity                         |                                                   Exact value |
| -------------------------------- | ------------------------------------------------------------: |
| Original agreement               |                                                  (a=k+\sigma) |
| Error weight                     |                                                (j=n-k-\sigma) |
| Low stratum                      |                                                         (t=1) |
| Jet depth                        |                                                    (\sigma-1) |
| Extension code                   |                                  (\operatorname{RS}[F,D,k+1]) |
| Redundancy                       |                                          (R=n-k-1=j+\sigma-1) |
| Scalar reserve relative to (k+1) |                                                    (\sigma-1) |
| Critical arity                   |                            (\ell_*=\lceil R/(\sigma-1)\rceil) |
| Apolar socle degree              |                                              (R-1=j+\sigma-2) |
| CI generator degrees             |                                              (d,\ j+\sigma-d) |
| Envelope-free range              |                                                  (d\ge\sigma) |
| Numerator degree                 |                                                       (u=j-d) |
| Denominator degree               |                                                  (v=d-\sigma) |
| Rational-code degree sum         |                                                (u+v=j-\sigma) |
| Maximum individual defect        |                                                    (d-\sigma) |
| Pairwise intersection ceiling    |                                                    (j-\sigma) |
| Exact boundary occupancy         | (\displaystyle \mu_j=\frac{\binom nj(q-1)^j}{q^{j+\sigma-1}}) |
| Simplified occupancy scale       |                        (\displaystyle \binom nj/q^{\sigma-1}) |

For exact weights (e<j), the same apolar theorem applies with (j) replaced by (e) and complementary constraint dimension (R-e). Those layers must ultimately be summed; boundary padding is not a substitute for full-coordinate treatment.

---

## Route-board impact

1. **The proposed critical-seed theorem is not the next lemma.** Once the coefficient vectors are included, fixing a seed merely fixes the syndrome. Its completion count is the original colored syndrome-fiber count minus (\ell_*).

2. **Seed-local exceptions are insufficient.** “The seed descends to a quotient” must be replaced by a canonical classification of the entire completion fiber, or by a bounded-overlap partition of that fiber. Otherwise a seed selected from one component gives no control over exceptional completions in other components.

3. **The (t=1) stratum is already a major inverse problem.** It is ordinary RS decoding for dimension (k+1), with an external evaluation color. A proof based only on fat-infinity determinant manipulation cannot bypass this base case.

4. **There is now a canonical finite object.** For (t=1), it is

   [
   \operatorname{Split}^{\circ}_D\bigl((I_s)_j\bigr),
   ]

   the monic, squarefree, fully (D)-split elements of the degree-(j) slice of the apolar complete intersection, satisfying the coprime/full-coordinate condition and a distinct-color condition.

5. **The quotient ledger must be module-level.** A single ratio (R=B/A) is gauge-dependent. Split-rational quotient structure has to mean that a large part of the split-numerator family (AU+BV) is a pullback through a split map, up to fixed defects and the generator changes above.

6. **The primitive conjecture is not disproved.** I found no quotient-free, envelope-free, full-coordinate, color-injective family exceeding the occupancy-plus-linear target. The exact normal form instead identifies what such a counterpacket must look like.

---

## What remains open

The unresolved (t=1) theorem is now the following finite split-form problem.

Let (I_s=(A,B)) be envelope-free, so (d\ge\sigma). Count a color-injective family of coprime pairs

[
(U_i,V_i)\in S_{j-d}\times S_{d-\sigma}
]

for which

[
P_i=A U_i+B V_i
]

is monic, squarefree, and splits completely over (D).

One must prove

[
|\mathcal F_{\mathrm{primitive}}|
\le
P_{\mathrm{fin}}(n,\sigma)
+
C_{\mathrm{occ}}(n,\sigma)
\frac{\binom nj}{q^{\sigma-1}},
]

with explicit finite (P_{\mathrm{fin}}) and (C_{\mathrm{occ}}), unless a large subfamily has one of these intrinsic structures:

[
\begin{aligned}
&\text{a common split factor;}\
&\text{a fixed defect }Z_D(A,V_i);\
&\text{a pullback through a split-rational map with calibrated action rank;}\
&\text{a hereditary descendant of one of those packets.}
\end{aligned}
]

The general (1<t<\sigma) problem should be a fat-infinity or level-algebra analogue of this complete-intersection slice. That analogue has not yet been derived here.

## Do you see a route to a full solve?

Yes, for isolating the (t<\sigma) branch, but the next step is not the originally named seed-completion lemma.

The next exact lemma should be:

[
\boxed{
\texttt{W-JR-T1-PRIMITIVE-APOLAR-SPLIT-NUMERATOR-INVERSE}.
}
]

It should assert that, on every official smooth multiplicative domain, an envelope-free apolar complete intersection

[
I_s=(A,B),\qquad
\deg A=d\ge\sigma,\qquad
\deg B=j+\sigma-d,
]

cannot contain more than

[
n^{1+o(1)}
+
n^{o(1)}
\frac{\binom nj}{q^{\sigma-1}}
]

full-coordinate, distinct-color, completely split degree-(j) numerators

[
AU+BV
]

unless a large subfamily is a common-factor, fixed-defect, or split-rational pullback packet.

A counterconstruction must now be equally specific: coprime (A,B), coprime pairs ((U_i,V_i)), completely (D)-split (AU_i+BV_i), distinct colors, no common factor, no bounded fixed-defect cover, no split-rational pullback cover, and cardinality above the occupancy-plus-linear scale.

Proving or killing this (t=1) theorem is the next exact move. Only after it is resolved is it rational to build the general fat-infinity (1<t<\sigma) completion theorem.
