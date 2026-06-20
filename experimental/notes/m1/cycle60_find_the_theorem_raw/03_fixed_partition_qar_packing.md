# BANKABLE_LEMMA

**Verdict on `W-MCA-QAR-FIXED-DEFECT-COVER`:** the literal packet-cover statement remains unproved and is stronger than necessary. Its prize-relevant numerical conclusion follows from an exact double-counting theorem, once the split-rational **fiber partition** is fixed.

Confidence: **high**.

## Exact theorem

### Fixed-partition QAR packing theorem

Let
[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,
]
and put
[
r=n-k,\qquad j=r-\sigma.
]

Let
[
\ell(z)=u+zv
]
be an affine syndrome line.

Fix an equipartition
[
\pi:L\longrightarrow\Omega
]
whose fibers all have cardinality (M). Write
[
N=|\Omega|=\frac nM,\qquad b=\frac kM.
]

This applies to a monomial quotient, a Möbius-conjugated quotient, or any split-rational quotient; only its induced fiber partition is used.

Suppose (Z_\pi\subseteq F) is a set of retained transverse bad slopes such that for every (z\in Z_\pi) we have selected:

[
D_z\subseteq L,\qquad |D_z|=\sigma,
]
and
[
A_z\in\binom{\Omega\setminus\pi(D_z)}b,
]
with agreement support
[
S_z=D_z\sqcup\pi^{-1}(A_z)
]
and error support
[
J_z=L\setminus S_z,\qquad |J_z|=j,
]
such that
[
\ell(z)\in V_{J_z}.
]

Assume the selected witnesses are envelope-clean: for distinct (z,z'\in Z_\pi),
[
\operatorname{span}(u,v)\not\subseteq V_R
\quad
\text{for every }|R|<r.
]
In particular, this holds whenever the entire syndrome line is contained in no proper secant envelope.

Then
[
\boxed{
|Z_\pi|
\le
\frac n\sigma\binom{N-1}{b}.
}
]

Including the slope-field bound,
[
\boxed{
|Z_\pi|
\le
\min\left{
|F|,
\frac n\sigma
\binom{n/M-1}{k/M}
\right}.
}
\tag{1}
]

The theorem is independent of:

* the denominator degree;
* the action rank (d_R(E));
* the anchor (\Phi);
* whether the packet is rank one or higher rank;
* how many distinct defect sets occur;
* collisions internal to a fixed packet.

It therefore applies after the Cycle 59 split-rational repair.

---

## Proof

Assign each slope (z\in Z_\pi) exactly one selected packet witness
[
(D_z,A_z).
]

Consider the set
[
\mathcal I
==========

{(z,x):z\in Z_\pi,\ x\in D_z}.
]
Since every (D_z) has cardinality (\sigma),
[
|\mathcal I|=\sigma|Z_\pi|.
]

Define
[
\Psi:\mathcal I\longrightarrow
\left{
(x,A):
x\in L,
A\in\binom{\Omega\setminus{\pi(x)}}b
\right}
]
by
[
\Psi(z,x)=(x,A_z).
]

We claim that (\Psi) is injective.

Suppose
[
\Psi(z,x)=\Psi(z',x').
]
Then
[
x=x'
\quad\text{and}\quad
A_z=A_{z'}=:A.
]

Let
[
U_A=\pi^{-1}(A).
]
Because (A\cap\pi(D_z)=A\cap\pi(D_{z'})=\varnothing),
[
S_z=D_z\sqcup U_A,\qquad
S_{z'}=D_{z'}\sqcup U_A.
]

If (z\ne z'), their exchange distance is
[
d
=

# |S_z\setminus S_{z'}|

# |D_z\setminus D_{z'}|

\sigma-|D_z\cap D_{z'}|.
]
Both defect sets contain (x), so
[
d\le \sigma-1.
]

Passing to the complementary error supports,
[
|J_z\cup J_{z'}|
================

j+d
\le
j+\sigma-1
==========

r-1.
]

But
[
u+zv\in V_{J_z},
\qquad
u+z'v\in V_{J_{z'}}.
]
Since (z\ne z'),
[
\operatorname{span}(u,v)
========================

\operatorname{span}(u+zv,u+z'v)
\subseteq
V_{J_z}+V_{J_{z'}}
==================

V_{J_z\cup J_{z'}}.
]

This is a proper envelope because
[
|J_z\cup J_{z'}|<r,
]
contrary to the envelope-clean hypothesis. Hence (z=z'), and then the two elements of (\mathcal I) are identical. Thus (\Psi) is injective.

For each fixed (x), the set (A) must avoid (\pi(x)), so there are exactly
[
\binom{N-1}{b}
]
possible images. Consequently,
[
\sigma|Z_\pi|
=============

|\mathcal I|
\le
n\binom{N-1}{b}.
]

This proves (1).

---

## Exact finite aggregation over quotient partitions

Let (\Pi) be any collection of inequivalent equal-fiber quotient partitions. Assign every retained quotient slope to one partition witnessing it. Applying the theorem separately gives
[
\boxed{
|Z_\Pi|
\le
\min\left{
|F|,
\frac n\sigma
\sum_{\pi\in\Pi}
\binom{N_\pi-1}{b_\pi}
\right}.
}
\tag{2}
]

If
[
L_{\max}
========

\max_{\pi\in\Pi}
\binom{N_\pi-1}{b_\pi},
]
then
[
\boxed{
|Z_\Pi|
\le
\frac n\sigma,|\Pi|,
\min{|F|,L_{\max}}.
}
\tag{3}
]

Indeed, if (|F|\le L_{\max}), the right side is at least (|F|); otherwise (2) is at most ((n/\sigma)|\Pi|L_{\max}).

Thus, if
[
\frac n\sigma=n^{o(1)}
\qquad\text{and}\qquad
|\Pi|=n^{o(1)},
]
then
[
\boxed{
|Z_\Pi|
\le
n^{o(1)}
\min{|F|,2^{Q_H(\sigma/n)}}.
}
]

This is exactly the numerical conclusion sought from the proposed cover theorem.

---

## Monomial and dihedral quotient ledger

For the ordinary monomial partitions
[
\pi_M(x)=x^M,
\qquad
M\mid\gcd(n,k),
]
let (\mathcal M_\sigma) denote the active scales. Then
[
\boxed{
|Z_{\rm mon}|
\le
\frac n\sigma
\sum_{M\in\mathcal M_\sigma}
\binom{n/M-1}{k/M}.
}
\tag{4}
]

Consequently,
[
|Z_{\rm mon}|
\le
\frac n\sigma,|\mathcal M_\sigma|,
\min{|F|,2^{Q_H(\sigma/n)}}.
\tag{5}
]

For a power-of-two domain,
[
|\mathcal M_\sigma|\le 1+\log_2n.
]

If
[
\sigma\ge c\frac n{\log_2 n},
]
then
[
\boxed{
|Z_{\rm mon}|
\le
\frac{(\log_2n)(1+\log_2n)}c
\min{|F|,2^{Q_H(\sigma/n)}}.
}
\tag{6}
]

The prefactor is (n^{o(1)}).

Scaling and inversion of a multiplicative coset do not create new fiber partitions: they merely relabel quotient values. Thus (6) also handles the generic dihedral closure of the monomial ledger.

---

## What can be proved about a literal packet cover

For a fixed partition (\pi), assign each slope to one fixed-defect packet (P), and let
[
m(P)
]
be the number of assigned slopes in that packet. Put
[
L_\pi=\binom{N-1}{b}.
]

The packing theorem implies
[
\sum_P m(P)\le\frac n\sigma L_\pi.
]

Therefore, for every threshold (\lambda>0),
[
\boxed{
#{P:m(P)\ge\lambda}
\le
\frac n\sigma\frac{L_\pi}{\lambda}.
}
\tag{7}
]

In particular, if “quotient-structured” is defined canonically to mean
[
m(P)\ge\frac{L_\pi}{\Lambda},
]
then all such heavy slopes are covered by at most
[
\boxed{
\frac n\sigma\Lambda
}
\tag{8}
]
fixed-defect packets.

For
[
\frac n\sigma=n^{o(1)},\qquad
\Lambda=n^{o(1)},
]
this is the desired (n^{o(1)}) cover theorem.

What is not proved is that every nonempty QAR packet is heavy. A packet may contain only one or a few accidental slopes. The present packet axioms supply no positive lower bound on (m(P)). Hence the literal claim covering **all** packet-representable slopes by (n^{o(1)}) packets does not follow from action rank plus envelope removal.

The distinction matters:

[
\text{large quotient packet}
\neq
\text{one slope admitting a quotient-shaped witness}.
]

The latter can be an occupancy event and should not automatically be assigned to the quotient ledger.

---

## Parameter ledger

For one quotient partition:
[
\begin{aligned}
q&=|F|,\
n&=|L|,\
k&=\dim C,\
r&=n-k,\
\sigma&=\text{reserve},\
j&=r-\sigma,\
M&=\text{fiber cardinality},\
N&=n/M,\
b&=k/M,\
D_z&=\text{defect set of size }\sigma,\
A_z&=\text{(b)-subset of quotient values},\
S_z&=D_z\sqcup\pi^{-1}(A_z),\
J_z&=L\setminus S_z.
\end{aligned}
]

The exact packet-independent profile is
[
L_\pi=\binom{N-1}{b}.
]

The fixed-partition factor is
[
\frac n\sigma.
]

At the official reserve
[
\sigma=(C+o(1))\frac n{\log_2n},
]
this is
[
\frac n\sigma
=============

\left(\frac1C+o(1)\right)\log_2n.
]

For (K) canonical quotient partitions,
[
|Z_{\rm quot}|
\le
\frac n\sigma K
\min{|F|,2^{Q_{\rm split}}}.
]

No generated-field/line-field transfer is used.

---

## Route-board impact

The fixed-defect multiplicity problem is not the main quotient obstruction.

For a fixed fiber partition, arbitrarily many defect anchors cannot increase the distinct-slope contribution beyond
[
\frac n\sigma
\binom{N-1}{b}.
]
The proof is purely syndrome-geometric and survives the full split-rational repair.

Therefore the route board should replace

[
\texttt{W-MCA-QAR-FIXED-DEFECT-COVER}
]

as a required numerical step by the banked theorem

[
\boxed{
\texttt{W-MCA-QAR-FIXED-PARTITION-PACKING}.
}
]

The correct quotient ledger is not

[
(\text{number of defect sets})
\times
(\text{worst packet profile}),
]
but
[
\boxed{
\frac n\sigma
\sum_{\text{canonical quotient partitions }\pi}
\binom{N_\pi-1}{b_\pi}.
}
]

This isolates the true unresolved issue:

[
\textbf{How many inequivalent split-rational fiber partitions can one line genuinely require?}
]

The Cycle 59 Möbius counterpacket changes the allowed partition family, but it does not invalidate the fixed-partition packing theorem.

---

## What remains open

The literal all-packet cover statement remains unresolved. No envelope-free RS counterpacket with superpolynomial **minimum packet-cover number** is presently constructed here.

The following points remain:

1. A line-intrinsic definition of canonical split-rational quotient partitions.
2. Consolidation of maps having the same fiber partition.
3. Control of exceptional norm-one/projective-subline partition families.
4. A weighted bound on the quotient partitions actually required by one line.
5. Canonical witness selection on lines having hereditary common envelopes.
6. The quotient-free primitive finite affine-secant theorem.
7. The scalar full-support list container theorem.

The important reduction is that varying defect sets no longer need a separate inverse theorem. Their total mass is already bounded once the partition is fixed.

# Do you see a route to a full solve?

Yes, but the next lemma is not the original fixed-defect cover statement.

The next exact target is:

[
\boxed{
\texttt{W-MCA-SPLIT-RATIONAL-PARTITION-SUM}
}
]

Let (\Pi_{\min}(\ell)) be a canonical minimal family of inequivalent split-rational fiber partitions needed to assign all envelope-clean quotient slopes on (\ell). Prove
[
\boxed{
\sum_{\pi\in\Pi_{\min}(\ell)}
\binom{N_\pi-1}{b_\pi}
\le
n^{o(1)},2^{Q_{\rm split}(\sigma/n)}.
}
\tag{9}
]

The fixed-partition packing theorem would then immediately give
[
|\operatorname{QAR}(\ell)\setminus\operatorname{TE}(\ell)|
\le
n^{o(1)}
\min{|F|,2^{Q_{\rm split}(\sigma/n)}}.
]

The corresponding exact counterconstruction is also sharper than the old request: construct one envelope-free affine syndrome line for which every valid assignment requires a family of inequivalent split-rational fiber partitions whose weighted sum in (9) is super-(n^{o(1)}) times the maximal profile. Merely producing many defect sets for one partition cannot work, by the theorem above.
