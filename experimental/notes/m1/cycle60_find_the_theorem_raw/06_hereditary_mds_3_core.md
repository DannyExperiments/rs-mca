# BANKABLE_LEMMA

The full affine-secant container theorem is not yet proved, and no quotient-free, envelope-free packet in the supplied context beats the corrected occupancy-plus-finite-floor target.

What can be proved is a canonical hereditary inverse theorem: every envelope-free packet exceeding an explicit linear floor contains a low-degree split-locator syzygy supported on a hereditary “MDS 3-core.” This gives a deterministic maximum-over-lines primitive bound and isolates the remaining occupancy problem much more sharply.

## 1. Exact theorem

Let
[
C=\operatorname{RS}[F,L,k],\qquad |F|=q,\quad |L|=n,
]
and write
[
r=n-k,\qquad j=r-\sigma,\qquad \sigma\ge1.
]

For an affine syndrome line
[
\ell(z)=u+zv,
]
select distinct transverse bad slopes (z_1,\dots,z_m), with exact (j)-set witnesses (T_i):
[
u+z_iv\in V_{T_i},\qquad v\notin V_{T_i}.
]

Put
[
p_i(X)=\prod_{x\in T_i}(X-x),\qquad S_i=L\setminus T_i.
]

Assume the syndrome plane (\langle u,v\rangle) is contained in no proper column envelope. Apply the banked leaf-peeling and common-root stripping procedure. It deletes at most (n) slopes and produces a reduced packet
[
\mathcal P_0={(z_i,T_i)}_{i=1}^{m_0}
]
over a reduced domain (L_0), with
[
m_0\ge m-n,\qquad j_0\le j,\qquad r_0=j_0+\sigma,
]
such that every point of (L_0) belongs to at least two agreement supports (S_i).

For (I\subseteq[m_0]), define
[
d_I(x)=#{i\in I:x\in S_i},
]
and the low-two boundary
[
\partial_2(I)
=============

\sum_{\substack{x\in L_0\1\le d_I(x)\le2}}d_I(x).
\tag{1}
]

### Hereditary MDS-3-core theorem

If (m_0\ge4), then there exist:

* a subset (I\subseteq[m_0]), with (|I|\ge3);
* an integer
  [
  d\le
  \left\lfloor
  \frac{2j_0-\sigma-1}{m_0-3}
  \right\rfloor;
  \tag{2}
  ]
* nonzero coefficient polynomials (A_i\in F[X]_{\le d}), (i\in I);

such that
[
\sum_{i\in I}A_i(X)p_i(X)=0,
\qquad
\sum_{i\in I}z_iA_i(X)p_i(X)=0.
\tag{3}
]

Moreover,
[
\boxed{\partial_2(I)\le d|I|.}
\tag{4}
]

More strongly, if
[
Z_i={x\in L_0:A_i(x)=0},
\qquad |Z_i|\le d,
]
then the thinned agreement sets
[
S_i^\circ=S_i\setminus Z_i
]
form an exact 3-core:
[
\boxed{
#{i\in I:x\in S_i^\circ}\in{0}\cup{3,4,\ldots}
\quad\text{for every }x\in L_0.
}
\tag{5}
]

Thus every sufficiently large packet contains a subpacket that becomes a minimum-degree-three cover after deleting at most (d<\sigma) points from each agreement support.

### Explicit primitive corollary

Call a reduced packet **(\sigma)-H2-primitive** when
[
\partial_2(I)\ge\sigma|I|
\qquad
\text{for every }I\subseteq[m_0],\ |I|\ge3.
\tag{6}
]

Then
[
\boxed{
m_0\le
\max\left{
3,;
2+\left\lfloor\frac{2j_0-1}{\sigma}\right\rfloor
\right}.
}
\tag{7}
]

Consequently, before leaf peeling,
[
\boxed{
m\le
n+
\max\left{
3,;
2+\left\lfloor\frac{2j-1}{\sigma}\right\rfloor
\right}.
}
\tag{8}
]

Since (j\le n-\sigma), a bound depending only on (n,\sigma) is
[
\boxed{
m\le
P_{\mathrm{H2}}(n,\sigma)
:=
n+\max\left{
3,;
\left\lfloor\frac{2n-1}{\sigma}\right\rfloor
\right}.
}
\tag{9}
]

Hence the requested form holds for this canonically defined hereditary-primitive residue with
[
C_{\mathrm{occ}}=0,
]
and therefore also, less sharply, with
[
\boxed{
C_{\mathrm{occ}}=1,\qquad
P(n,\sigma)=P_{\mathrm{H2}}(n,\sigma).
}
\tag{10}
]

That is,
[
|\operatorname{Bad}^{\mathrm{H2\text{-}primitive}}_\sigma(\ell)|
\le
\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
+
n+\max\left{
3,\left\lfloor\frac{2n-1}{\sigma}\right\rfloor
\right}.
\tag{11}
]

This is deterministic and maximum-over-lines.

---

## 2. Proof

### Step 1: Split-locator syzygy excess

For the reduced packet, homogenize the locators (p_i) to binary forms (P_i) of degree (j_0), and form
[
M=
\begin{pmatrix}
P_1&\cdots&P_{m_0}\
z_1P_1&\cdots&z_{m_0}P_{m_0}
\end{pmatrix}.
]

The two-core property makes (M) rank two at every point of (\mathbf P^1). Hence
[
0\longrightarrow\mathcal K
\longrightarrow
\mathcal O(-j_0)^{m_0}
\longrightarrow
\mathcal O^2
\longrightarrow0,
]
with
[
\mathcal K
\simeq
\bigoplus_{\nu=1}^{m_0-2}
\mathcal O(-j_0-d_\nu),
]
where
[
d_\nu\ge0,\qquad
\sum_{\nu=1}^{m_0-2}d_\nu=2j_0.
\tag{12}
]

The exact Macaulay calculation gives
[
\dim\mathcal C(\mathcal P_0)
============================

\sum_{\nu=1}^{m_0-2}(d_\nu-\sigma)_+.
\tag{13}
]

The reduced packet is realized by a nonzero syndrome pair, so
[
\max_\nu d_\nu\ge\sigma+1.
\tag{14}
]

Choose (\nu_*) with (d_{\nu_*}\ge\sigma+1). Since (m_0\ge4), there is at least one other syzygy summand. Let (d) be the smallest degree among the other (m_0-3) summands. Then
[
(m_0-3)d
\le
\sum_{\nu\ne\nu_*}d_\nu
=======================

2j_0-d_{\nu_*}
\le
2j_0-\sigma-1.
]
This proves (2).

### Step 2: Extract an actual low-degree syzygy

The summand (\mathcal O(-j_0-d)\subseteq\mathcal K) is represented by a vector of homogeneous forms (A_i) of degree (d), not all zero, satisfying
[
\sum_iA_iP_i=0,\qquad
\sum_i z_iA_iP_i=0.
]

Let
[
I={i:A_i\ne0}.
]

One cannot have (|I|=1). One also cannot have (|I|=2): if the only indices were (i,h), then
[
A_iP_i+A_hP_h=0,
]
[
z_iA_iP_i+z_hA_hP_h=0.
]
Subtracting (z_h) times the first identity from the second gives
[
(z_i-z_h)A_iP_i=0,
]
contradicting (z_i\ne z_h). Therefore (|I|\ge3).

Dehomogenizing gives (3).

### Step 3: Local MDS argument

Fix (x\in L_0), and define
[
c_i(x)=A_i(x)p_i(x).
]

The two syzygy identities imply
[
\sum_{i\in I}c_i(x)=0,\qquad
\sum_{i\in I}z_ic_i(x)=0.
\tag{15}
]

The matrix
[
\begin{pmatrix}
1&1\
z_i&z_h
\end{pmatrix}
]
is nonsingular whenever (i\ne h). Consequently a nonzero vector satisfying (15) cannot have Hamming weight one or two.

But
[
c_i(x)\ne0
\iff
x\in S_i\quad\text{and}\quad A_i(x)\ne0.
]

Therefore, after deleting the roots of (A_i) from (S_i), the number of surviving active sets at (x) is either zero or at least three. This proves (5).

If (d_I(x)=1), the unique active (A_i) must vanish at (x). If (d_I(x)=2), both active coefficient polynomials must vanish. Thus every incidence counted in (\partial_2(I)) is a root-incidence of one of the nonzero (A_i).

Each (A_i) has at most (d) roots in (L_0), so
[
\partial_2(I)
\le
\sum_{i\in I}|Z_i|
\le d|I|.
]
This proves (4).

### Step 4: Bound the hereditary-primitive residue

Suppose the reduced packet is (\sigma)-H2-primitive. Applying (6) to the extracted support (I) gives
[
\sigma|I|
\le \partial_2(I)
\le d|I|,
]
and hence
[
d\ge\sigma.
]

Combining this with (2),
[
(m_0-3)\sigma
\le
2j_0-\sigma-1.
]
Therefore
[
m_0
\le
3+\left\lfloor
\frac{2j_0-\sigma-1}{\sigma}
\right\rfloor
=============

2+\left\lfloor
\frac{2j_0-1}{\sigma}
\right\rfloor.
]

The cases (m_0\le3) give (7). Adding the at most (n) peeled slopes gives (8), and (j\le n-\sigma) gives (9).

---

## 3. Canonical hereditary container construction

The preceding theorem gives an actual deterministic decomposition rule.

Fix the official ordering of (L), slopes, and (j)-subsets. After quotient and envelope tags have been applied:

1. Select the least exact witness for each remaining slope.
2. Perform the canonical leaf peel and common-core reduction.
3. If some (I) satisfies
   [
   \partial_2(I)<\sigma|I|,
   ]
   choose the inclusion-minimal such (I), resolving ties lexicographically.
4. Tag (I) as an **H2-defective hereditary container**, remove it, and repeat.
5. The final residue is (\sigma)-H2-primitive and hence satisfies (7).

This procedure is finite, deterministic and hereditary. It does not depend on a denominator chart, an averaging anchor or a choice of a syzygy splitting basis.

The important caveat is that an H2-defective container is not automatically a quotient packet. Occupancy-generic packets can also have dense three-cores. Therefore H2-defect is a canonical obstruction certificate, not yet a freely discardable exception.

---

## 4. Canonical critical-seed lemma

There is also an exact seed reduction that should be banked with the hereditary theorem.

For each selected pair ((z_i,T_i)), define the (\sigma)-dimensional block
[
W_i
===

\left{
(p_iQ,z_ip_iQ):Q\in F[X]*{<\sigma}
\right}
\subseteq F[X]*{<r_0}^{,2}.
\tag{16}
]

Let
[
W(\mathcal P_0)=\sum_iW_i,
\qquad
e=\operatorname{codim}W(\mathcal P_0)
=\dim\mathcal C(\mathcal P_0)
=\operatorname{Exc}_\sigma(\mathcal P_0).
]

Process the blocks in the official order and retain a block precisely when it strictly increases the current span. Let (B) be the resulting canonical seed. Then
[
W(B)=W(\mathcal P_0).
]

If (h=|B|), write the successive rank increments as
[
1\le\Delta_b\le\sigma,
]
and define the block defect
[
D_B=\sum_{b\in B}(\sigma-\Delta_b).
]

Then
[
\boxed{
\sigma h-D_B=2r_0-e,
\qquad
h=\frac{2r_0-e+D_B}{\sigma}.
}
\tag{17}
]

Every nonseed completion satisfies
[
\boxed{W_i\subseteq W(B).}
\tag{18}
]

When (e=1), the seed determines the compatible syndrome line projectively. Thus the entire maximum-over-lines problem has been reduced to counting split-locator blocks contained in one canonically generated codimension-one seed span.

The frequently suggested seed size (2r_0/\sigma) is valid only when the block defect (D_B) is controlled. Equation (17), not (h\approx2r_0/\sigma) unconditionally, is the exact statement.

---

## 5. Parameter ledger

Let
[
N_\sigma=\binom nj=\binom n{k+\sigma},
\qquad
B_{\mathrm{occ}}=\frac{N_\sigma}{q^{\sigma-1}}.
]

For the H2-primitive residue:

[
C_{\mathrm{occ}}=0,
]
[
P_{\mathrm{rate}}(n,k,\sigma)
=============================

n+\max\left{
3,;
2+\left\lfloor
\frac{2(n-k-\sigma)-1}{\sigma}
\right\rfloor
\right}.
]

A (k)-independent version is
[
P(n,\sigma)
===========

n+\max\left{
3,\left\lfloor\frac{2n-1}{\sigma}\right\rfloor
\right}.
]

If the original packet is already a basepoint-free two-core with no common locator factor, the initial (n) term disappears:
[
P_0
===

\max\left{
3,;
2+\left\lfloor\frac{2j-1}{\sigma}\right\rfloor
\right}.
]

At reserve
[
\sigma\asymp\frac{n}{\log q},
]
the reduced finite floor is
[
P_0=O(\log q).
]
The currently banked leaf peel contributes the additional (n).

The result is independent of the smoothness or multiplicative structure of (L). Those hypotheses are needed only to classify or count the extracted H2-defective containers.

---

## 6. Route-board impact

This establishes the following exact alternative for every quotient-clean, envelope-free line:

[
\boxed{
\begin{array}{c}
\text{small finite residue}[2mm]
\text{or}[2mm]
\text{a support-minimal degree-}<\sigma
\text{ split-locator syzygy}\
\text{whose thinned agreement hypergraph is a 3-core.}
\end{array}
}
]

Accordingly, the previous wall

[
\text{“classify arbitrary positive syzygy excess”}
]

can be replaced by the narrower wall

[
\boxed{
\texttt{W-MCA-FINITE-CRITICAL-SEED-H2-DEFECT-CHARGE}.
}
]

A large packet cannot remain mysterious merely because its bundle is unbalanced. It must exhibit an explicit hereditary subpacket with:

* a degree (d<\sigma) syzygy;
* at most (d) deleted agreement points per locator;
* local multiplicity zero or at least three;
* containment of every associated block in one canonical critical-seed span.

This also explains why pairwise exchange separation is insufficient: the obstruction has minimum local arity three.

The result does not contradict the Cycle 58 occupancy packet. Such a large occupancy-scale packet necessarily falls into the H2-defective branch. Nor does it contradict the finite (\mathbb F_{17}) mixed-scroll packet, which lies at the unavoidable linear finite floor and does not beat the corrected target.

---

## 7. What remains open

The full requested theorem still requires a finite charge for the canonically extracted H2-defective containers.

In particular, quotient/envelope removal alone does not currently imply H2-primitivity. One must prove that, inside a fixed critical-seed span, an H2-defective 3-core is one of:

1. a split-rational quotient/action-rank packet;
2. a proper-envelope descendant under shortening;
3. an occupancy-generic packet whose total distinct slopes are bounded by
   [
   \frac{\binom n{k+\sigma}}{q^{\sigma-1}}
   ]
   plus an explicit finite floor.

The difficult issue is the third branch. A dense three-core is not itself algebraic structure; random occupancy packets also produce it. Thus simply naming H2-defect as a “template” without charging it would be vacuous.

No supplied construction gives a quotient-free, envelope-free packet exceeding
[
C_{\mathrm{occ}}\frac{\binom n{k+\sigma}}{q^{\sigma-1}}
+\operatorname{poly}(n,\sigma)
]
for every fixed (C_{\mathrm{occ}}) and reasonable finite floor. Therefore there is presently no counterpacket to the corrected theorem.

# Do you see a route to a full solve?

Yes, with moderate confidence.

The next exact lemma should be:

> **Critical-seed H2-defect inverse.**
> Let (B) be the canonical seed of an envelope-free two-core packet, with
> [
> \operatorname{codim}W(B)=1.
> ]
> Let (\mathcal H(B)) be the set of transverse split-locator completions
> [
> W(z,T)\subseteq W(B)
> ]
> assigned to inclusion-minimal H2-defective subpackets. After removing all split-rational quotient/action-rank packets and all proper-envelope descendants, prove
> [
> |\mathcal H(B)|
> \le
> \left\lceil
> \frac{\binom n{k+\sigma}}{q^{\sigma-1}}
> \right\rceil
> +2r.
> \tag{19}
> ]

Combined with (8), this would give the full primitive bound with
[
C_{\mathrm{occ}}=1
]
and, for example,
[
P(n,\sigma)
===========

n+2r+
\max\left{
3,\left\lfloor\frac{2n-1}{\sigma}\right\rfloor
\right}
\le
3n+
\max\left{
3,\left\lfloor\frac{2n-1}{\sigma}\right\rfloor
\right}.
]

The algebraic object to attack is now explicit. A support-minimal extracted syzygy has
[
\sum_iA_ip_i=\sum_i z_iA_ip_i=0,\qquad \deg A_i<\sigma,
]
and, after deleting the roots of (A_i), its pointwise coefficient vectors are nonzero codewords of the ([|I|,|I|-2,3]) MDS code with parity checks ((1,z_i)). Proving that excess many fully split locator columns in one critical-seed span force either split-rational coefficient synchronization or a proper-envelope descent is the next exact step.
