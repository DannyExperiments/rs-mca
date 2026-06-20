ROUTE_CUT

The literal fixed-defect packet-cover statement is stronger than necessary and is not presently a well-defined theorem because “quotient-structured” and packet maximality are unspecified. Its required numerical consequence follows from a different, denominator-free theorem: transpose the count from fixed defects to fixed (k)-point quotient cores.

## Exact theorem: fixed-core petal bound

Let
[
C=\operatorname{RS}[F,L,k],\qquad |L|=n,\qquad r=n-k,
]
and let
[
\ell(z)=u+zv
]
be an affine syndrome line. Choose word representatives (f,g\in F^L) with syndromes (u,v).

Fix an information set (U\subseteq L) with (|U|=k). Let (p_U,q_U\in F[X]_{<k}) be the unique polynomials satisfying
[
p_U|_U=f|_U,\qquad q_U|_U=g|_U.
]

Define the common extra-agreement core
[
C_U=
{x\in L\setminus U:
f(x)=p_U(x),\ g(x)=q_U(x)},
\qquad c_U=|C_U|.
]

For (s\ge1), let (Z_U(s)) be the set of slopes (z\in F) for which some RS codeword agrees with (f+zg) on (U) and on at least (s) additional coordinates.

### Theorem 1 — information-set petal theorem

If (c_U<s), then
[
\boxed{
|Z_U(s)|
\le
\left\lfloor\frac{r-c_U}{s-c_U}\right\rfloor.
}
]

If (c_U>0) and (Z_U(s)) contains at least two slopes, then
[
\boxed{
u,v\in V_{L\setminus(U\cup C_U)},
\qquad
|L\setminus(U\cup C_U)|=r-c_U<r.
}
]
Thus (C_U) gives an explicit proper common-envelope certificate.

Consequently, on a syndrome line contained in no proper common envelope,
[
\boxed{
|Z_U(s)|\le \left\lfloor\frac rs\right\rfloor.
}
\tag{1}
]

This statement is independent of denominator degree, action rank, quotient map, or rational coordinate.

## Proof

Any polynomial agreeing with (f+zg) on (U) is unique, because (U) is an information set. It must therefore be
[
p_z=p_U+zq_U.
]

Put
[
A_z=
{x\in L\setminus U:
f(x)+zg(x)=p_U(x)+zq_U(x)}.
]

For two distinct slopes (z\ne z'), a point (x\in A_z\cap A_{z'}) satisfies
[
f(x)+zg(x)=p_U(x)+zq_U(x),
]
[
f(x)+z'g(x)=p_U(x)+z'q_U(x).
]
Subtracting gives
[
g(x)=q_U(x),
]
and substitution then gives
[
f(x)=p_U(x).
]
Hence
[
A_z\cap A_{z'}=C_U.
]

Therefore the petals
[
A_z\setminus C_U
]
are pairwise disjoint. Every (z\in Z_U(s)) has
[
|A_z|\ge s,
]
so every petal has at least (s-c_U) points. All petals lie in
[
L\setminus(U\cup C_U),
]
which has (r-c_U) points. Thus
[
|Z_U(s)|(s-c_U)\le r-c_U,
]
proving the first assertion.

If (c_U>0), then (f-p_U) and (g-q_U) are both supported on
[
R=L\setminus(U\cup C_U).
]
Since (p_U,q_U) are codewords,
[
u=\operatorname{syn}(f-p_U)\in V_R,
\qquad
v=\operatorname{syn}(g-q_U)\in V_R.
]
Because (|R|=r-c_U<r), this is a proper envelope certificate. Therefore an envelope-free line has (c_U=0), giving (1).

The same proof allows overagreement: only (|A_z|\ge s) is used.

---

## Exact QAR corollary

Consider one equal-fiber quotient system
[
\Pi={F_y:y\in\Omega},
\qquad
|F_y|=M,\qquad |\Omega|=N,
]
with
[
M\mid k,\qquad b=\frac{k}{M}.
]

Its quotient cores are
[
U_A=\bigcup_{y\in A}F_y,
\qquad
A\in\binom{\Omega}{b}.
]
Each (U_A) has exactly (k) points.

Let (\operatorname{QAR}_\Pi(\ell)) denote all slopes having a witness support of the form
[
S=U_A\sqcup T,
\qquad
|T|\ge s.
]
This contains every fixed-defect packet for (\Pi), regardless of its action rank (d_R(E)).

### Theorem 2 — finite fixed-core QAR bound

For an envelope-free affine syndrome line,
[
\boxed{
|\operatorname{QAR}_\Pi(\ell)|
\le
\min\left{
|F|,
\left\lfloor\frac rs\right\rfloor
\binom Nb
\right}.
}
\tag{2}
]

More generally, for a registry (\mathfrak P) of quotient fiber systems,
[
\boxed{
\left|
\bigcup_{\Pi\in\mathfrak P}\operatorname{QAR}*\Pi(\ell)
\right|
\le
\min\left{
|F|,
\left\lfloor\frac rs\right\rfloor
\sum*{\Pi\in\mathfrak P}\binom{N_\Pi}{b_\Pi}
\right}.
}
\tag{3}
]

### Proof

For fixed (A), apply Theorem 1 with (U=U_A). There are at most
[
\left\lfloor r/s\right\rfloor
]
slopes having (U_A) as their (k)-point quotient core. Summing over the (\binom Nb) possible cores proves (2). Summing over the registry proves (3).

No multiplication by the number of defect anchors occurs.

---

## Monomial quotient ledger: unconditional explicit bound

For the multiplicative domain, let
[
\mathfrak M_s=
{M:M\mid\gcd(n,k),\ M>s},
]
and write
[
N_M=\frac nM,\qquad b_M=\frac kM.
]

Use the Cycle 59 full quotient profile
[
Q_H(s/n)=
\max_{M\in\mathfrak M_s}
\log_2\binom{N_M-1}{b_M}.
]

Since (b_M/N_M=\rho=k/n),
[
\binom{N_M}{b_M}
================

\frac{1}{1-\rho}
\binom{N_M-1}{b_M}.
]
Also
[
\frac{\lfloor r/s\rfloor}{1-\rho}
\le
\frac ns.
]

Therefore (3) gives the completely explicit finite estimate
[
\boxed{
|\operatorname{QAR}_{\mathrm{mon}}(\ell)|
\le
|\mathfrak M_s|
\left\lceil\frac ns\right\rceil
\min\left{|F|,2^{Q_H(s/n)}\right}.
}
\tag{4}
]

Because
[
|\mathfrak M_s|
\le \tau(\gcd(n,k))
\le \tau(n)
=n^{o(1)},
]
equation (4) implies
[
\boxed{
|\operatorname{QAR}_{\mathrm{mon}}(\ell)|
\le
n^{o(1)}
\min\left{|F|,2^{Q_H(s/n)}\right}
}
]
whenever
[
\frac ns=n^{o(1)}.
]
In particular, at corrected reserve
[
s=\Theta!\left(\frac n{\log n}\right),
]
the prefactor is
[
O(\log n)\tau(n)=n^{o(1)}.
]

Thus the desired global quotient charge is proved for all monomial quotient scales. It does not require a fixed-defect packet-cover theorem.

---

## A genuine fixed-defect cover for heavy packets

There is nevertheless a precise form of the proposed cover theorem.

Work in the balanced reduced locator chart
[
[L_S]_E=\alpha-z\beta
\quad\text{in }A_E=F[X]/(E),
]
where
[
\deg E=s,\qquad \beta\in A_E^\times.
]

Fix one quotient-core family (\mathscr U), and identify cores having the same locator residue ([L_U]_E). Let (R_0) be the number of resulting core-residue classes.

For a defect (T), let (\Gamma_T) be its distinct packet slopes. Put
[
h=\alpha\beta^{-1}\in A_E.
]

### Lemma 3 — multiplicative rectangle rigidity

If (h\notin F), the incidence graph between defect locators and core-residue classes is (K_{2,2})-free.

Indeed, four incidences give
[
a_i b_j=\alpha-z_{ij}\beta,
]
where
[
a_i=[L_{T_i}]*E,\qquad b_j=[L*{U_j}]*E.
]
Commutativity gives
[
(\alpha-z*{11}\beta)(\alpha-z_{22}\beta)
========================================

(\alpha-z_{12}\beta)(\alpha-z_{21}\beta).
]
After division by (\beta^2),
[
(h-z_{11})(h-z_{22})
====================

(h-z_{12})(h-z_{21}).
]
Since (1,h) are linearly independent over (F), the two unordered slope pairs are equal. One matching forces (a_1=a_2), hence (T_1=T_2); the other forces (b_1=b_2). There is no nondegenerate rectangle.

Consequently, if
[
H=\left\lceil\frac{R_0}{K}\right\rceil\ge2,
]
the number (m_H) of fixed-defect packets satisfying
[
|\Gamma_T|\ge H
]
obeys
[
\boxed{
m_H\binom H2\le\binom{R_0}{2},
\qquad
m_H\le
\frac{R_0(R_0-1)}{H(H-1)}
<2K^2.
}
\tag{5}
]

If (h\in F), shifting the slope makes (\alpha=0). Each defect packet then uses only one projective core-residue class. A projective class can correspond to at most (\lfloor n/s\rfloor) defect locators: locators in one projective residue class form a pencil whose distinct split members have disjoint root sets. Hence
[
\boxed{
m_H\le
\left\lfloor\frac ns\right\rfloor
\left\lceil\frac{R_0}{H}\right\rceil
\le
\left\lfloor\frac ns\right\rfloor K.
}
\tag{6}
]

Thus packets having at least a (1/K) fraction of the available quotient-core profile are coverable by
[
O!\left(K^2+K\frac ns\right)
]
fixed-defect packets. Taking (K=n^{o(1)}) gives the desired (n^{o(1)}) heavy-packet cover.

The remaining light packets do not need a cover: their total slope mass is already bounded by Theorem 2.

This is the correct finite package:

[
\boxed{
\text{heavy fixed-defect cover}
;+;
\text{light fixed-core mass bound}.
}
]

Demanding that every singleton or low-density quotient certificate belong to one of (n^{o(1)}) fixed-defect packets is unnecessary and has no canonical meaning.

---

## Parameter ledger

[
\begin{array}{c|l}
\text{Parameter} & \text{Meaning}\ \hline
q=|F| & \text{slope field size}\
n=|L| & \text{evaluation-domain size}\
k & \text{RS dimension}\
r=n-k & \text{redundancy}\
s=\sigma & \text{reserve / defect size}\
a=k+s & \text{agreement size}\
M & \text{quotient-fiber size}\
N=n/M & \text{number of quotient fibers}\
b=k/M & \text{number of full fibers in a quotient core}\
D_s=\lfloor r/s\rfloor & \text{maximum petals per fixed core}\
\mathfrak M_s & \text{active monomial quotient scales}\
Q_H(s/n) &
\displaystyle\max_{M\in\mathfrak M_s}
\log_2\binom{n/M-1}{k/M}
\end{array}
]

The exact monomial prefactor is
[
|\mathfrak M_s|\left\lceil\frac ns\right\rceil.
]

For a split-rational registry (\mathfrak P), the canonical finite quantity is not the number of defect packets. It is the total quotient-core profile
[
\boxed{
\mathcal Q_{\mathrm{core}}(\mathfrak P)
=======================================

\log_2
\left(
\sum_{\Pi\in\mathfrak P}
\binom{N_\Pi}{b_\Pi}
\right).
}
\tag{7}
]
Equation (3) becomes
[
|\operatorname{QAR}*{\mathfrak P}(\ell)|
\le
\left\lfloor\frac rs\right\rfloor
\min\left{|F|,2^{\mathcal Q*{\mathrm{core}}(\mathfrak P)}\right}.
]

---

## Route-board impact

1. **The monomial fixed-defect cover wall is removed.** The full monomial QAR contribution already satisfies the required
   [
   n^{o(1)}\min{|F|,2^{Q_H}}
   ]
   bound.

2. **Action rank remains useful locally, but is unnecessary for the global union bound.** It predicts how many quotient cores one fixed defect meets. Transposing the count prevents multiplication by the number of possible defects.

3. **The correct global object is the quotient-core registry.** For split-rational maps, the maximum single-map profile is sufficient only if the number of inequivalent fiber systems, or their total core entropy, is (n^{o(1)}).

4. **The proposed all-packet cover should be replaced by heavy-cover plus light-mass.** Equations (5)–(6) supply the actual heavy cover; equation (3) charges everything else.

5. **This does not solve the primitive branch.** The quotient-free, envelope-free finite discrepancy theorem and the scalar full-support list theorem remain open.

## What remains open

The unresolved quotient statement is now:

### `W-MCA-SPLIT-RATIONAL-CORE-REGISTRY`

Let (\mathfrak P(\ell)) be the maximal inequivalent split-rational fiber systems actually supporting rich transverse packets on one envelope-free syndrome line. Prove
[
\boxed{
\sum_{\Pi\in\mathfrak P(\ell)}
\binom{N_\Pi}{b_\Pi}
\le
n^{o(1)}
\max_{\Pi\in\mathfrak P(\ell)}
\binom{N_\Pi-1}{b_\Pi}.
}
\tag{8}
]

It is enough to count distinct core-locator residue families rather than syntactically distinct rational maps.

If (8) is false, the required counterpacket is sharper than the one requested in the prompt: one envelope-free line carrying superprofile many pairwise non-refining split-rational core systems. Merely producing many defect anchors inside one fiber system will not work, because Theorem 1 already bounds their total contribution.

## Do you see a route to a full solve?

Yes. The next exact lemma is `W-MCA-SPLIT-RATIONAL-CORE-REGISTRY`, equation (8), not an all-defect packet cover.

A viable proof route is:

[
\text{projective/split-rational classifier}
;\longrightarrow;
\text{identify maximal fiber systems}
;\longrightarrow;
\text{use rectangle rigidity to merge common refinements}
;\longrightarrow;
\text{bound total core entropy}.
]

Once (8) is proved, Theorem 2 closes the complete quotient contribution. The remaining MCA wall is then the primitive finite affine-secant discrepancy theorem after quotient and hereditary-envelope removal.
