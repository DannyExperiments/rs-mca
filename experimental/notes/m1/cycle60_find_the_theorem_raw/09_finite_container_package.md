# CONDITIONAL

The exact implication package can be formalized and proved, but its two central upper theorems are open. The route is **not close**. In particular, (d_R(E)) is not a canonical denominator-free definition of a quotient container; it is only an auxiliary certificate once a canonical short chart has been fixed.

There is also a new finite counterpacket: a projective-subline quotient packet satisfying the Cycle 58–59 official numerical caps, generated-field entropy margin, tangent bound, occupancy bound, and all fixed-coordinate monomial quotient-profile bounds. It forces equality-scale split-rational containers into any valid package.

## 1. Exact finite objects

Let
[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,\qquad r=n-k,
]
and fix reserve
[
\sigma\ge 1,\qquad a=k+\sigma,\qquad j=r-\sigma=n-a.
]

Write (q=|F|) for the actual code and MCA slope field. Unless a separate protocol theorem says otherwise, the exact target numerator is
[
T_F:=\left\lfloor\frac{q}{2^{128}}\right\rfloor.
]

Let (H\in F^{r\times n}) be an RS parity-check matrix, with column (h_x) at (x\in L), and
[
V_T=\operatorname{span}_F{h_x:x\in T}.
]

For an affine syndrome line (\ell(z)=u+zv), define
[
\operatorname{Bad}_\sigma(\ell)
===============================

\left{
z\in F:
\exists T\in\binom Lj,\quad
u+zv\in V_T,\quad v\notin V_T
\right}.
]
The exact MCA numerator is
[
M_C(\sigma)=\max_{u,v\in F^r}
|\operatorname{Bad}_\sigma(u+Fv)|.
]

For scalar lists, define
[
\nu_e^\circ(s)=
#\left{
(E,c):
E\in\binom Le,;
c\in(F^\times)^E,;
H_Ec=s
\right}.
]
Since (e<r), the coefficient vector is unique for a fixed (E). The exact scalar list numerator is
[
L_C(\sigma)=
\max_{s\in F^r}\sum_{e=0}^{j}\nu_e^\circ(s).
]

Thus safety at reserve (\sigma) is exactly
[
M_C(\sigma)\le T_F
\quad\text{or}\quad
L_C(\sigma)\le T_F.
]

No denominator degree occurs in either definition.

---

## 2. Canonical quotient containers

The canonical quotient object should be a block system on the evaluation domain, not a denominator equation.

### Definition 2.1: split-rational block system

A degree-(M) split-rational block system on (L) is a collection
[
\Pi={B_y:y\in\Omega}
]
for which there is a separable rational function
[
R=P/Q\in F(X),\qquad \deg R=M,\qquad Q(x)\ne0\quad(x\in L),
]
such that
[
B_y={x\in L:R(x)=y},
\qquad |B_y|=M
]
for every (y\in\Omega).

Two rational functions define the same quotient object when they define the same collection of full blocks. This makes the container invariant under postcomposition by (\operatorname{PGL}_2(F)), changes of formula for (R), and relabeling of the quotient values.

For a fixed defect (D\subseteq L), put
[
\Pi_D={B\in\Pi:B\cap D=\varnothing}.
]
For an integer (b), define the exact support container
[
\mathcal A(\Pi,D,b)
===================

\left{
D\sqcup\bigcup_{B\in\mathcal Y}B:
\mathcal Y\in\binom{\Pi_D}{b}
\right}.
]
Its full-profile weight is
[
\omega(\Pi,D,b)
===============

\min\left{
q,\binom{|\Pi_D|}{b}
\right}.
]

### MCA realization

At agreement size (a), require
[
|D|+Mb=a.
]
Define
[
\Gamma_{\Pi,D,b}(\ell)
======================

\left{
z:
\exists A\in\mathcal A(\Pi,D,b),\quad
\ell(z)\in V_{L\setminus A},\quad
v\notin V_{L\setminus A}
\right}.
]

For each fixed (A), the transverse line (\ell) meets (V_{L\setminus A}) in at most one point. Hence
[
\boxed{
|\Gamma_{\Pi,D,b}(\ell)|
\le
\omega(\Pi,D,b).
}
]

This is an exact finite theorem. It includes monomial, inversion, projective-subline, norm-one, additive-polynomial, and any other split-rational block systems without first classifying them.

### List realization

For a received word (y), let
[
A_y(P)={x\in L:P(x)=y(x)}.
]
At overagreement layer (h\ge0), require
[
|D|+Mb=a+h.
]
Define
[
\Lambda_{\Pi,D,b}(y)
====================

\left{
P\in F[X]_{<k}:
A_y(P)\in\mathcal A(\Pi,D,b)
\right}.
]

A full agreement support of size at least (a>k) determines the polynomial uniquely. Therefore
[
\boxed{
|\Lambda_{\Pi,D,b}(y)|
\le
\binom{|\Pi_D|}{b}.
}
]

This is an actual-list bound, not a raw-support bound.

### Role of (d_R(E))

If a canonical reduced short chart exists and (Q\bmod E) is a unit, one may define
[
\theta_R=[P]_E[Q]_E^{-1}\in F[X]/(E),
\qquad
d_R(E)=\deg\minpoly_F(\theta_R).
]

This is useful recognition metadata. If (E) is squarefree, (d_R(E)) counts the distinct (R)-values on the geometric roots of (E).

It is not the container definition because:

1. every syndrome line has high-degree noncanonical charts;
2. (d_R(E)) changes with the chart;
3. low action rank does not by itself specify the anchor line or the realized locator image;
4. full action rank in one affine coordinate does not exclude a projectively conjugated rank-one quotient.

The finite charge must therefore be the realized support-profile weight, or the exact locator-image/affine-line intersection, not merely (d_R(E)).

---

## 3. Canonical envelope containers

### MCA envelope

For a syndrome line put
[
U_\ell=\operatorname{span}*F{u,v}.
]
Its proper-envelope registry is
[
\mathcal R(\ell)=
\left{
R\subseteq L:
|R|<r,\quad U*\ell\subseteq V_R
\right}.
]

The line is envelope-free exactly when (\mathcal R(\ell)=\varnothing). This is line-intrinsic.

If (R) is a minimal envelope with
[
|R|=j+d<r,\qquad 0\le d<\sigma,
]
then witnesses with
[
|R\cup T|\le r
]
have a linear distinct-slope cap. In supported coordinates on (R), each such landing forces at least (d) coordinate functions (a_x+zb_x) to vanish. Distinct slopes have disjoint zero sets. Thus, for (d>0),
[
|\operatorname{Bad}^{\mathrm{internal}}_{\sigma,R}(\ell)|
\le
\left\lfloor\frac{j+d}{d}\right\rfloor;
]
at (d=0), the same coordinate argument gives the safe cap (j).

For external witnesses, (|R\cup T|>r), the Cycle 59 shortening is exact. With
[
P=T\setminus R,\qquad
A=(L\setminus R)\setminus P,\qquad
h=|P|-(\sigma-d)\ge1,
]
the slope is a transverse witness for
[
\operatorname{RS}[F,R,h]
]
at the same reserve (\sigma), after dividing the supported line by (L_A).

A canonical hereditary envelope container is therefore a finite shortening tree:

* each node uses a fixed minimal envelope (R);
* internal slopes receive the linear cap above;
* external slopes are partitioned by the exact child data ((A,h));
* child nodes have strictly smaller evaluation domains.

The tree terminates, but its branching can be enormous. Bounding its total weight is a genuine theorem, not bookkeeping.

### List common-core envelope

There is an exact list analogue.

Let (C_0\subseteq L), (c=|C_0|<k), and suppose all codewords in a sublist agree with (y) on (C_0). Let (I_{C_0}(y)) be the degree-(<c) interpolant on (C_0). Every such codeword has a unique form
[
P=I_{C_0}(y)+L_{C_0}R,
\qquad
\deg R<k-c.
]
On (L\setminus C_0), define
[
y_{C_0}(x)=
\frac{y(x)-I_{C_0}(y)(x)}{L_{C_0}(x)}.
]
Then
[
A_y(P)
======

C_0\sqcup A_{y_{C_0}}(R).
]

Hence a common-core list at reserve (\sigma) is exactly a list for
[
\operatorname{RS}[F,L\setminus C_0,k-c]
]
at the same reserve (\sigma). If (c\ge k), the container has size at most one.

This is the canonical hereditary envelope operation for scalar lists.

---

## 4. Canonical primitive objects

After quotient and envelope containers have been removed, “primitive” must mean the exact complement, not “generic-looking.”

### MCA primitive packet

For an envelope-free line, select one exact (j)-set witness for each remaining slope. Peel agreement supports containing a degree-one vertex; this loses at most (n) slopes. Strip the common error-coordinate core. The remaining locator matrix is
[
\begin{pmatrix}
P_1&\cdots&P_m\
z_1P_1&\cdots&z_mP_m
\end{pmatrix},
]
with a basepoint-free kernel splitting
[
\mathcal K\simeq
\bigoplus_{\nu=1}^{m-2}
\mathcal O_{\mathbf P^1}(-j_0-d_\nu).
]

Its exact realizability obstruction is
[
\operatorname{Exc}_\sigma
=========================

\sum_\nu(d_\nu-\sigma)*+.
]
A nonzero envelope-free packet necessarily has
[
\operatorname{Exc}*\sigma>0.
]

Thus the primitive MCA theorem is precisely a finite bound for basepoint-free, (\sigma)-separated, split-rational-block-free locator packets of positive (\sigma)-excess.

### List primitive packet

For one scalar syndrome with full-support representations (E_i), choose
[
b_i\le r-|E_i|,
\qquad
\sum_i b_i=r.
]
There is an exact locator syzygy
[
\sum_i A_iL_{E_i}=0,
\qquad
\deg A_i<b_i.
]

Taking
[
\ell_*=\left\lceil\frac r\sigma\right\rceil
]
and the standard critical (b_i)-allocation shows that every sufficiently large list contains a support-minimal critical seed.

The primitive list theorem is therefore a completion theorem: after common-core and split-rational quotient containers are removed, bound all additional full-support representations of the same syndrome that complete one critical seed.

---

## 5. The minimal finite prize-solving package

The following is sufficient and nonvacuous.

### Theorem MCA-CONT

For every allowed RS instance and reserve (\sigma), prove explicit integers
[
C_{\mathrm{occ}}\ge1,\qquad
D_{\mathrm{prim}},\qquad
Q_{\mathrm{split}},\qquad
E_{\mathrm{her}}
]
with the following properties.

For every envelope-free affine syndrome line:

1. all slopes belonging to large realized split-rational block containers admit a cover whose total full-profile weight is at most (Q_{\mathrm{split}});
2. the remaining primitive slopes satisfy
   [
   |\operatorname{Bad}^{\mathrm{prim}}*\sigma(\ell)|
   \le
   \left\lceil
   C*{\mathrm{occ}}
   \frac{\binom nj}{q^{\sigma-1}}
   \right\rceil
   +
   D_{\mathrm{prim}}.
   ]

For every enveloped line, its canonical shortening tree has total weight at most
[
E_{\mathrm{her}}.
]

Then
[
\boxed{
M_C(\sigma)
\le
U_{\mathrm{MCA}}(\sigma)
:=
\max\left{
E_{\mathrm{her}},
\left\lceil
C_{\mathrm{occ}}
\frac{\binom nj}{q^{\sigma-1}}
\right\rceil
+
D_{\mathrm{prim}}
+
Q_{\mathrm{split}}
\right}.
}
]

Consequently,
[
U_{\mathrm{MCA}}(\sigma)\le T_F
]
is an exact finite MCA safety certificate.

This is smaller and sharper than an additive six-branch denominator ledger. Residual and high-denominator charts disappear into the denominator-free primitive theorem; envelope children recursively consume the same theorem.

### Theorem LIST-CONT

Over a field (K), prove explicit integers
[
D_{\mathrm{list}},\qquad
Q_{\mathrm{list}},\qquad
E_{\mathrm{core}},
]
and an explicit constant (C_{\mathrm{list}}), such that every scalar list has:

1. common-core hereditary containers totaling at most (E_{\mathrm{core}});
2. realized split-rational quotient containers, over all overagreement layers, totaling at most (Q_{\mathrm{list}});
3. a primitive remainder bounded by
   [
   \left\lceil
   C_{\mathrm{list}}
   \frac{1}{|K|^r}
   \sum_{e=0}^{j}
   \binom ne(|K|-1)^e
   \right\rceil
   +
   D_{\mathrm{list}}.
   ]

Then
[
\boxed{
L_{C_K}(\sigma)
\le
U_K(\sigma)
:=
E_{\mathrm{core}}
+
Q_{\mathrm{list}}
+
\left\lceil
C_{\mathrm{list}}
\frac{1}{|K|^r}
\sum_{e=0}^{j}
\binom ne(|K|-1)^e
\right\rceil
+
D_{\mathrm{list}}.
}
]

No boundary-only quantity (\nu_j^\circ) is sufficient: all (e\le j) layers are included.

### Proof of sufficiency

For MCA, an affine line is either enveloped or envelope-free. The hereditary theorem bounds the first case. In the second case, the quotient cover and primitive complement partition the bad-slope set up to overlap, and the union bound gives the displayed sum.

For lists, the actual codewords are covered by the common-core, quotient, and primitive registries. The full-support condition prevents raw-support multiplicity. Summing the three exact caps proves the scalar bound.

Nothing else is needed on the safe side.

---

## 6. Matching lower/failure theorem at the previous reserve

Let (\widehat\sigma) be the proposed threshold reserve.

### MCA failure

At (\tau=\widehat\sigma-1), put
[
a_\tau=k+\tau,\qquad
j_\tau=n-k-\tau,\qquad
N_\tau=\binom n{a_\tau},
\qquad
\lambda_\tau=\frac{N_\tau}{q^\tau},
]
and
[
V_\tau=
\sum_{d=0}^{\tau-1}
\binom{a_\tau}{d}\binom{j_\tau}{d}
\left(q^{-d}-q^{-\tau}\right).
]

The theorem-grade same-field Bessel–Paley lower bound is
[
B_{\mathrm{BP}}(\tau)
=====================

\left\lceil
q\max\left{
\frac{\lambda_\tau}{\lambda_\tau+V_\tau},
\left(1-\frac{V_\tau}{\lambda_\tau}\right)_+
\right}
\right\rceil.
]

Thus
[
\boxed{
B_{\mathrm{BP}}(\widehat\sigma-1)>T_F
}
]
certifies failure at the previous reserve. If this inequality does not hold, an explicit line with more than (T_F) slopes is required.

### List failure

Let (B) be the field generated by the evaluation domain. Two exact lower bounds are
[
B_{\mathrm{ent}}(\tau)
======================

\left\lceil
\frac{\binom n{k+\tau}}{|B|^\tau}
\right\rceil
]
and, for multiplicative domains,
[
B_{\mathrm{quot}}(\tau)
=======================

\max_{\substack{M\mid\gcd(n,k)\M>\tau}}
\binom{n/M-1}{k/M}.
]

Explicit split-rational packets may be added to this maximum. Therefore
[
\boxed{
\max{
B_{\mathrm{ent}}(\widehat\sigma-1),
B_{\mathrm{quot}}(\widehat\sigma-1),
B_{\mathrm{split}}(\widehat\sigma-1)
}

> T_F
> }
> ]
> certifies list failure at the previous reserve.

If an upper certificate holds at (\widehat\sigma) and the corresponding lower certificate holds at (\widehat\sigma-1), monotonicity gives
[
\sigma_C^*=\widehat\sigma.
]

The largest safe grid radius is
[
1-\rho-\frac{\widehat\sigma}{n}.
]
The supremal real transition is
[
\boxed{
\delta_C^*
==========

1-\rho-\frac{\widehat\sigma-1}{n},
}
]
with the endpoint itself unsafe when (\widehat\sigma) is minimal.

---

## 7. Field-transfer hypotheses

These are load-bearing.

### MCA

There is no known general (B)-to-(F) transfer for affine syndrome lines. The MCA container theorem must therefore be proved over the actual slope field (F), unless a separate explicit transfer theorem is supplied.

Neither (q_{\mathrm{chal}}) nor (q_{\mathrm{line}}) may pay a generated-field structural bill merely by being larger.

### Lists

If LIST-CONT is proved directly over the actual alphabet (F), then
[
U_F(\sigma)\le T_F
]
solves every interleaving arity provided
[
\binom{U_F(\sigma)+1}{2}<|F|.
]
At the target level this follows from
[
U_F\le T_F,\qquad |F|\le2^{256}.
]

If (B\subseteq F), (L\subseteq B), and (d=[F:B]), then
[
\operatorname{RS}[F,L,k]
\cong
\operatorname{Int}(\operatorname{RS}[B,L,k],d)
]
with exact preservation of column agreements. A scalar (B)-bound (U_B) transfers without loss if
[
\boxed{
\binom{U_B+1}{2}<|B|.
}
]
A weaker sufficient transfer is
[
U_B^d\le T_F.
]

A large challenge field cannot replace the field over which the projection is performed.

---

## 8. New official-cap counterpacket

This strengthens the Cycle 59 Möbius packet to a finite instance inside the numerical cap model (k\le2^{40}), (|F|<2^{256}).

Let
[
p=2^{19}-1=524287,
\qquad
B=\mathbf F_{p^2},
\qquad
F=\mathbf F_{p^8}.
]
Let
[
H={x\in B^\times:x^{p+1}=1}.
]
Then
[
n=|H|=p+1=2^{19}.
]

Take
[
k=\frac n4=2^{17},
\qquad
M=\sigma=\frac n{32}=2^{14},
]
so
[
a=k+\sigma=9M,\qquad
j=n-a=23M.
]

The fields are
[
q_{\mathrm{gen}}=p^2,\qquad
q_{\mathrm{line}}=q_{\mathrm{chal}}=p^8.
]

Define
[
\psi(X)=\frac{X+2}{2X+1}.
]
For (x\in H), (x^p=x^{-1}), so
[
\psi(x)^p=\psi(x)^{-1}.
]
Hence (\psi(H)=H).

Let
[
\Omega=H^M,\qquad |\Omega|=32.
]
For (y\in\Omega), the block
[
B_y={x\in H:\psi(x)^M=y}
]
has size (M).

Choose (\vartheta\in F) and define
[
E_\vartheta(X)
==============

\frac{(X+2)^M-\vartheta(2X+1)^M}
{1-\vartheta2^M}.
]
For suitable (\vartheta), this is monic, squarefree, degree (M), and has no root on (H).

Modulo (E_\vartheta),
[
L_{B_y}(X)
\equiv
\frac{\vartheta-y}{1-y2^M}(2X+1)^M.
]

For every
[
\mathcal A\in\binom{\Omega}{9},
]
let
[
S_{\mathcal A}=\bigsqcup_{y\in\mathcal A}B_y.
]
Then
[
|S_{\mathcal A}|=9M=k+\sigma.
]

Put
[
B_{\mathrm{num}}
================

\operatorname{rem}*{E*\vartheta}(2X+1)^{9M},
\qquad
f(x)=x^k,
\qquad
g(x)=-\frac{B_{\mathrm{num}}(x)}{E_\vartheta(x)}.
]

For each (\mathcal A), define
[
\kappa_{\mathcal A}(\vartheta)
==============================

\prod_{y\in\mathcal A}
\frac{\vartheta-y}{1-y2^M},
\qquad
z_{\mathcal A}=-\kappa_{\mathcal A}(\vartheta).
]

The support locator (L_{S_{\mathcal A}}) and (E_\vartheta X^k) are both monic of degree (k+M). Therefore
[
Q_{\mathcal A}
==============

E_\vartheta X^k-L_{S_{\mathcal A}}
]
has degree (<k+M), and
[
Q_{\mathcal A}\equiv
z_{\mathcal A}B_{\mathrm{num}}
\pmod{E_\vartheta}.
]
Hence
[
P_{\mathcal A}
==============

\frac{Q_{\mathcal A}-z_{\mathcal A}B_{\mathrm{num}}}
{E_\vartheta}
]
has degree (<k) and agrees with (f+z_{\mathcal A}g) on (S_{\mathcal A}).

For distinct (\mathcal A,\mathcal A'), the collision equation
[
\kappa_{\mathcal A}(\vartheta)
==============================

\kappa_{\mathcal A'}(\vartheta)
]
has degree at most (9). The total number of forbidden (\vartheta)-values from all slope collisions is at most
[
9\binom{\binom{32}{9}}2<2^{53}.
]
The values causing a fixed-coordinate power collision on the roots of (E_\vartheta) number at most
[
2kM=2^{32}.
]
Since
[
|F|=p^8>2^{144},
]
one may choose (\vartheta) avoiding all of them.

Therefore
[
\boxed{
|\operatorname{Bad}_\sigma(\ell)|
\ge
\binom{32}{9}
=============

28{,}048{,}800.
}
]

For every (D\mid k),
[
d_D(E_\vartheta)=M,
]
so every fixed-coordinate monomial action rank is full. But for
[
R(X)=\psi(X)^M
]
one has
[
[R]*{E*\vartheta}=\vartheta,
\qquad
d_R(E_\vartheta)=1.
]

The line is proper-envelope-free. Indeed, if the anchor syndrome of (x^k) lay in (V_R) for (|R|<r), then (x^k) would agree with a degree-(<k) polynomial on more than (k) points, which is impossible.

The finite ledger is:

[
T_F
===

# \left\lfloor\frac{p^8}{2^{128}}\right\rfloor

# 2^{24}-256

16{,}776{,}960.
]

The tangent floor is
[
j=376{,}832<T_F.
]

Even charging every old monomial full profile at scales (D\ge M) gives only
[
\binom{31}{8}
+\binom{15}{4}
+\binom72
+\binom31
=========

7{,}890{,}114<T_F.
]

The occupancy term is below one:
[
\frac{\binom n{k+\sigma}}{q_{\mathrm{line}}^{\sigma-1}}<1.
]

The generated-field entropy surplus is over (65{,}000) bits:
[
\sigma\log_2q_{\mathrm{gen}}
----------------------------

\log_2\binom n{k+\sigma}

>

# 2^{14}\cdot36-2^{19}

65{,}536.
]

Thus
[
28{,}048{,}800>T_F
]
despite occupancy, tangent, generated-field entropy, proper-envelope, and every monomial action-rank/profile test clearing.

This is not a counterexample to the corrected split-rational package. It is exactly a projective-subline container at the equality scale
[
M=\sigma.
]

It proves that:

[
\boxed{
\text{split-rational closure and the equality scale }M=\sigma
\text{ are mandatory.}
}
]

---

## 9. Parameter and rate ledger

For MCA safety at a candidate reserve, the exact necessary comparison is
[
\max\left{
E_{\mathrm{her}},
\left\lceil
C_{\mathrm{occ}}\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
\right\rceil
+D_{\mathrm{prim}}+Q_{\mathrm{split}}
\right}
\le
T_F.
]

In particular, before discrepancy and template costs,
[
\sigma\log_2q-\log_2\binom n{k+\sigma}\gtrsim128
]
is necessary for the occupancy term.

For list decoding, at the four official rates the existing multiplicative quotient packets already force, subject to the stated dyadic divisibility:

[
\begin{array}{c|c|c}
\rho&\text{quotient universe}&\text{necessary reserve floor}\
\hline
1/2&256&n/256\
1/4&256&n/256\
1/8&256&n/256\
1/16&512&n/512
\end{array}
]

The corresponding packet logarithms are approximately
[
250.67,\quad203.15,\quad135.23,\quad168.82
]
bits, all above the worst allowed target (2^{128}).

The finite theorem package is sufficient for every official rate **code by code**. It does not produce a rate-only answer because the threshold also depends on
[
n,\quad q_{\mathrm{gen}},\quad q_{\mathrm{line}},\quad
\gcd(n,k),\quad
L,\quad
\text{and its split-rational block registry}.
]

No official rate is currently solved on the safe side.

---

## 10. Smallest known counterpackets to overstrong statements

| Overstrong statement                                                | Counterpacket                                                                                                                                                  |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Raw feasible supports measure actual list size                      | (n=4,k=2,\sigma=1), received word a codeword: all four (3)-sets are feasible, actual list size (1).                                                            |
| Support incidences may replace distinct slopes                      | (n=8,k=4,\sigma=1): one slope has (21) transverse support incidences.                                                                                          |
| A pure (O(n)) or (n^{1+o(1)}) term works without occupancy          | (F_{97},n=16,k=8,\sigma=2,t=3): (67>n) primitive-looking slopes, below the occupancy value (8008/97). The high-(j), (t=2) family gives the asymptotic version. |
| (Q^\sigma>\binom n{k+\sigma}) implies a small finite numerator      | The (F_{5^{64}},n=256,k=128,\sigma=2) Bessel packet has positive raw surplus but over (2^{100}) bad slopes.                                                    |
| (E\ne E_0(X^M)) means quotient-free                                 | (F_{97},n=16,k=8,M=4,t=3), with (d_4(E)=1), (E\ne E_0(X^4)), and slopes (96,9,80).                                                                             |
| Fixed-coordinate monomial action rank is a complete quotient ledger | The (p=2^{19}-1) packet above: all (d_D(E)) are full, yet (d_{\psi^M}(E)=1) and the line exceeds (T_F).                                                        |
| The smaller ((\beta/H_2))-quotient exponent pays arbitrary anchors  | Fixed-defect punctured-fiber packets attain the full profile (\binom{n/M-1}{k/M}).                                                                             |
| All quotient packets have (M>\sigma)                                | The new counterpacket has (M=\sigma).                                                                                                                          |
| Every (t>\sigma) line compresses to (t'\le\sigma)                   | (F_{17},n=8,k=2,\sigma=2), (g=-x^{-3}), minimal denominator (3); stronger (F_{97}) packet has (67) slopes and full action rank.                                |
| Minimal indices force a low-degree locator section                  | (F_{17},n=8,k=2,\sigma=2): eight envelope-free slopes, but no four locators lie on a degree-(\le2) polynomial section.                                         |
| Exact-boundary full-support control gives the complete list         | Quotient overagreement and tangent-petal packets can live entirely in layers (e<j).                                                                            |
| Common-core list contribution is (O(1))                             | A ((k-1))-point core with disjoint ((\sigma+1))-petals gives (\lfloor(n-k+1)/(\sigma+1)\rfloor) actual codewords.                                              |
| Multiplicative quotient profiles suffice on arbitrary domains       | The additive-subspace packet over (\mathbf F_{3^{103}}^\times) has actual list (\binom{80}{41}>T) and trivial active multiplicative profile.                   |
| (V_T\cap V_{T'}=V_{T\cap T'}) without an exchange restriction       | Over (F_7), (n=6,k=1,j=3), disjoint (3)-sets have spans meeting in dimension (1).                                                                              |
| Cycle 55 already supplies an (\Omega(\sqrt q)) conic counterexample | No such lower construction is in the packet; only an (O(\sqrt q))-type calculation exists.                                                                     |

---

## 11. Route-board impact

The smallest honest prize-solving package is:

1. the already proved exact syndrome and full-support reductions;
2. MCA-CONT over the actual line field;
3. LIST-CONT over the actual alphabet or generated field with an explicit transfer inequality;
4. the Bessel–Paley or explicit previous-reserve MCA failure certificate;
5. entropy/quotient/split-rational previous-reserve list failure;
6. exact integer comparison with (T_F).

The main route correction is:

[
\boxed{
\text{quotient container}
=========================

\text{realized split-rational block system},
}
]
not
[
\boxed{
\text{quotient container}
=========================

{E:d_M(E)<\deg E}.
}
]

The action rank remains important for detecting packets and predicting collision multiplicity, but it is subordinate to the support-theoretic container.

## 12. What remains open

The MCA theorem still requires three substantial ingredients:

1. a finite weighted cover theorem for all large realized split-rational block packets on one envelope-free line;
2. a finite occupancy/discrepancy theorem for block-free positive-syzygy-excess packets;
3. a bounded hereditary-envelope branching theorem valid on arbitrary punctured descendant domains.

The scalar list theorem independently requires:

1. a functional-quotient cover over every overagreement layer;
2. a common-core hereditary cover;
3. a primitive critical-seed completion theorem for full-support syndrome fibers.

Explicit constants must then fit below (T_F). None of these central bounds is currently proved.

## Do you see a route to a full solve?

Yes, but it is not close.

The next exact construction should be the **support-theoretic split-rational cover**, not another denominator classifier:

> For every envelope-free affine syndrome line, let (\mathsf Q_{>n}(\ell)) be the union of all realized fixed-defect split-rational block containers containing more than (n) slopes. Prove that (\mathsf Q_{>n}(\ell)) is coverable by a finite collection ({(\Pi_i,D_i,b_i)}) satisfying
> [
> \sum_i
> \min\left{
> q,\binom{|(\Pi_i)*{D_i}|}{b_i}
> \right}
> \le Q*{\mathrm{split}}(n,k,q,\sigma),
> ]
> with an explicit integer (Q_{\mathrm{split}}) small enough for the prize ledger. If no such cover exists, prove that the varying defects generate a proper hereditary envelope.

After that, the exact MCA lemma is:

[
\boxed{
|\operatorname{Bad}^{\mathrm{primitive}}*\sigma(\ell)|
\le
\left\lceil
C*{\mathrm{occ}}
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
\right\rceil
+
D_{\mathrm{prim}},
}
]
for every envelope-free, split-rational-block-free line, with explicit (C_{\mathrm{occ}}) and (D_{\mathrm{prim}}).

The scalar list critical-seed completion theorem remains a separate parallel wall. Thus the logical package has two master upper theorems, but mathematically it still contains at least four major inverse/cover problems.
