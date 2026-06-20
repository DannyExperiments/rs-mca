# COUNTERPACKET

The proposed `W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION` is false. A previously uncharged **configuration-space quotient** fixes the constant coefficient—equivalently, the product/determinant character—of the split error locator. It produces a (t=1<\sigma), exact-full-support, (\sigma)-separated, envelope-free colored packet larger than occupancy by a factor (q/n).

At a same-field dyadic instance with (q<2^{256}), it gives at least (2^{215}) distinct slopes, versus occupancy below (2^{29}). A critical seed has 396 members. No Cycle 59 pure or reserve-fixed split-rational equal-fiber packet contains more than seven of its supports, and the tangent ceiling is 395.

## Exact counterpacket theorem

Let (F=\mathbb F_q), let (H\le F^\times) be cyclic of order (n), and put

[
a=k+\sigma<n,\qquad j=n-a,\qquad \sigma\ge 2.
]

For (T\in\binom Hj), set (S=H\setminus T) and write the two monic locators as

[
L_T(X)=X^j+c_{j-1}(T)X^{j-1}+\cdots+c_0(T),
]

[
L_S(X)=X^a+d_{a-1}(T)X^{a-1}+\cdots+d_0(T).
]

Since (L_TL_S=X^n-1),

[
c_0(T)d_0(T)=-1.
]

There exist (\gamma\in F^\times), a signature

[
\delta=(\delta_{k+2},\ldots,\delta_{a-1})\in F^{\sigma-2},
]

and a family (\mathscr B\subseteq\binom Hj) such that

[
c_0(T)=\gamma,\qquad
d_i(T)=\delta_i\quad(k+2\le i\le a-1)
]

for every (T\in\mathscr B), and

[
\boxed{
|\mathscr B|
\ge
\frac{\binom nj}{nq^{\sigma-2}}.
}
\tag{1}
]

Define

[
h(X)=-\gamma\sum_{i=k+2}^{a-1}\delta_iX^{i-1},
]

[
W(X)=X^{n-1}-\gamma X^{a-1}+h(X),
\qquad
w=W|_H,
]

and, for (T\in\mathscr B),

[
Q_T(X)=\gamma\sum_{i=1}^{k+1}d_i(T)X^{i-1}.
\tag{2}
]

Then:

1. (Q_T\in F[X]_{\le k}).
2. Its full agreement support with (w) is exactly (S=H\setminus T):
   [
   \boxed{A_w(Q_T)=S.}
   \tag{3}
   ]
3. Every error coordinate is nonzero.
4. Distinct (T,T'\in\mathscr B) have exchange distance
   [
   \boxed{|T\setminus T'|\ge \sigma.}
   \tag{4}
   ]
5. There exists (\beta\in F\setminus H) such that, for
   [
   E=X-\beta,\qquad B=1,\qquad
   U_{E,1}=E\mathcal P_k\oplus F=\mathcal P_{k+1},
   ]
   the number of distinct colors (z_T=Q_T(\beta)) satisfies
   [
   \boxed{
   |Z|
   \ge
   \frac23
   \min\left{
   \left\lfloor\frac{\binom nj}{nq^{\sigma-2}}\right\rfloor,
   \left\lfloor\frac{q-n}{2k}\right\rfloor
   \right}.
   }
   \tag{5}
   ]
6. The associated syndrome line is contained in no proper coordinate envelope.

Thus the missing support-scale term is at least

[
\boxed{
\mathsf{PC}(n,k,\sigma,q)
\asymp
\min\left{
\frac{\binom n{k+\sigma}}{nq^{\sigma-2}},
\frac qk
\right}.
}
\tag{6}
]

Before color collisions, its ratio to boundary occupancy is exactly

[
\frac{\binom nj/(nq^{\sigma-2})}
{\binom nj/q^{\sigma-1}}
========================

\boxed{\frac qn}.
\tag{7}
]

This is not raw-support multiplicity: every listed polynomial has exactly (a) agreements, so each actual-list element contributes one canonical support.

## Proof

### 1. Locator bucketing

The constant coefficient has the form

[
c_0(T)=(-1)^j\prod_{x\in T}x.
]

It therefore takes at most (n) values. The tuple

[
(d_{k+2},\ldots,d_{a-1})
]

has (\sigma-2) coordinates and at most (q^{\sigma-2}) values. Pigeonholing gives (1).

When (\gcd(j,n)=1), the product fibers are exactly equinumerous: multiplication by (\lambda\in H) sends (c_0(T)) to (\lambda^jc_0(T)), and (\lambda\mapsto\lambda^j) permutes (H).

### 2. Exact full-support identity

Fix (T\in\mathscr B). Since (c_0(T)=\gamma),

[
d_0(T)=-\gamma^{-1}.
]

For (x\in H), (x^{n-1}=x^{-1}). Hence

[
\begin{aligned}
-\gamma x^{-1}L_S(x)
&=
-\gamma x^{a-1}
-\gamma\sum_{i=1}^{a-1}d_i(T)x^{i-1}
-\gamma d_0(T)x^{-1}\
&=
x^{n-1}
-\gamma x^{a-1}
-\gamma\sum_{i=1}^{a-1}d_i(T)x^{i-1}\
&=W(x)-Q_T(x).
\end{aligned}
\tag{8}
]

The last equality uses the common high-coefficient signature to place all terms with (i\ge k+2) into (W), leaving the terms (i\le k+1) in (Q_T).

Now (L_S) vanishes exactly on (S). Since (x,\gamma\ne0),

[
W(x)-Q_T(x)=0
\iff x\in S.
]

This proves (3), exact full support, and nonzero error coordinates.

### 3. The packet is automatically (\sigma)-separated

Comparing the highest coefficients in

[
L_TL_S=X^n-1
]

shows triangularly that common values of

[
d_{a-1},d_{a-2},\ldots,d_{a-\sigma+2}
]

force common values of

[
c_{j-1},c_{j-2},\ldots,c_{j-\sigma+2}.
]

Therefore, for (T,T'\in\mathscr B),

[
\deg(L_T-L_{T'})\le j-\sigma+1,
\qquad
(L_T-L_{T'})(0)=0.
\tag{9}
]

Let (d=|T\setminus T'|). The common locator (L_{T\cap T'}), of degree (j-d), divides (L_T-L_{T'}).

If (d<\sigma-1), its degree is strictly larger than the right side of (9), forcing (L_T=L_{T'}).

If (d=\sigma-1), then

[
L_T-L_{T'}=\lambda L_{T\cap T'}.
]

The left side has constant coefficient zero, whereas

[
L_{T\cap T'}(0)\ne0
]

because (H\subset F^\times). Thus (\lambda=0), again giving (T=T').

Consequently distinct supports satisfy (d\ge\sigma).

### 4. Distinct-color extraction

Choose any (\mathscr A\subseteq\mathscr B) of size (m). For each (\beta\in F\setminus H), let

[
\nu_z(\beta)=
#{T\in\mathscr A:Q_T(\beta)=z}
]

and

[
C_\beta=\sum_z\binom{\nu_z(\beta)}2.
]

For (T\ne T'), the nonzero polynomial (Q_T-Q_{T'}) has degree at most (k). It therefore vanishes at at most (k) choices of (\beta). Summing over external evaluation points gives

[
\sum_{\beta\in F\setminus H}C_\beta
\le
k\binom m2.
]

Some (\beta\in F\setminus H) consequently satisfies

[
C_\beta\le\frac{k\binom m2}{q-n}.
]

Cauchy–Schwarz now yields

[
\begin{aligned}
|{Q_T(\beta):T\in\mathscr A}|
&\ge
\frac{m^2}{\sum_z\nu_z(\beta)^2}\
&=
\frac{m^2}{m+2C_\beta}\
&\ge
\frac{m}{1+k(m-1)/(q-n)}.
\end{aligned}
\tag{10}
]

Taking

[
m=
\min\left{
|\mathscr B|,
\left\lfloor\frac{q-n}{2k}\right\rfloor
\right}
]

makes the denominator at most (3/2), proving (5).

For (E=X-\beta),

[
Q=(X-\beta)G+Q(\beta),
]

so (Q(\beta)) is exactly the jet-residue color.

### 5. No proper syndrome envelope

Consider the base code

[
C_0=\operatorname{ev}_H((X-\beta)\mathcal P_k).
]

The syndrome direction is the syndrome of the constant polynomial (1). Suppose this direction lay in a column span (V_R) with

[
|R|<n-k.
]

Then there would be an error vector (e) supported on (R) such that

[
1-e=(X-\beta)G
]

on (H), for some (G\in\mathcal P_k). On (H\setminus R), which has at least (k+1) points,

[
1=(x-\beta)G(x).
]

But (1-(X-\beta)G(X)) has degree at most (k), so these (k+1) roots force the polynomial identity

[
1=(X-\beta)G(X),
]

which is impossible at (X=\beta).

Thus the direction lies in no proper column envelope. In particular, every support in the packet is transverse.

## Parameter ledger: same-field dyadic finite packet

Take

[
p=2^{31}-1=2,147,483,647,
\qquad
F=\mathbb F_{p^8},
\qquad
q=p^8.
]

Let

[
n=2^{34}=17,179,869,184
]

and take (H\le F^\times) of order (n).

Modulo (2^{34}),

[
p^2\equiv1-2^{32},\qquad
p^4\equiv1-2^{33}\ne1,\qquad
p^8\equiv1.
]

Thus

[
\operatorname{ord}_{2^{34}}(p)=8.
]

Hence (H) exists and generates (F) over (\mathbb F_p); this is genuinely same-field. Also,

[
2^{247}<q<2^{248}<2^{256}.
]

Use

[
\begin{aligned}
k&=2,143,399,963,\
\sigma&=38,037,280,\
t&=1,\
a=k+\sigma&=2,181,437,243,\
j=n-a&=14,998,431,941,\
j-\sigma&=14,960,394,661.
\end{aligned}
]

The four integers

[
k,\quad a,\quad j,\quad j-\sigma
]

are prime. Deterministic Pocklington certificates can be based on

[
\begin{aligned}
k-1&=2\cdot3\cdot11\cdot277\cdot117241,\
a-1&=2\cdot1090718621,\
j-1&=2^2\cdot5\cdot36073\cdot20789,\
j-\sigma-1&=2^2\cdot3\cdot5\cdot249339911,
\end{aligned}
]

with respective top-level witnesses (5,2,2,6).

The JR redundancy and critical arity are

[
R=n-k-1=15,036,469,220,
]

[
395(\sigma-1)=15,024,725,205<R,
]

[
396(\sigma-1)=15,062,762,484\ge R.
]

Therefore

[
\boxed{\ell_*=396.}
]

Robbins factorial bounds certify

[
27<
\log_2\left(\frac{\binom na}{q^{\sigma-1}}\right)
<28,
\tag{11}
]

while

[
241<
\log_2\left(\frac{\binom na}{nq^{\sigma-2}}\right)
<242.
\tag{12}
]

More precisely, the two logarithms are approximately

[
27.8596009401842
\quad\text{and}\quad
241.859600934810.
]

Thus:

[
\mu_{\le j}<2^{29},
]

whereas the support bucket contains more than (2^{241}) exact full supports.

Because (k<2^{31}) and

[
q-n>3\cdot2^{246},
]

we have

[
\left\lfloor\frac{q-n}{2k}\right\rfloor
\ge3\cdot2^{214}.
]

Equation (5) gives

[
\boxed{|Z|\ge2^{215}.}
\tag{13}
]

Consequently,

[
\frac{|Z|}{q}>2^{-33},
]

whereas normalized occupancy is below (2^{-219}). Also,

[
|Z|>2^{11}n^6.
]

A critical seed of 396 distinct colors therefore has more than

[
2^{215}-396
]

additional completions.

### Excluding the listed exceptional templates

The attached Cycle 59 point-fiber templates have supports consisting of full equal-size fibers, either with no defect or with the reserve-(\sigma) defect.

The primality choices eliminate them in either agreement-support or error-support orientation:

| Template orientation             |       Movable size | Consequence             |                              Packet cap |
| -------------------------------- | -----------------: | ----------------------- | --------------------------------------: |
| Pure agreement support           |          (a) prime | (M=a), one fiber        |                  (\lfloor n/a\rfloor=7) |
| Pure error support               |          (j) prime | (M=j), one fiber        |                  (\lfloor n/j\rfloor=1) |
| Agreement, fixed (\sigma)-defect | (a-\sigma=k) prime | (M=k), one fiber        |          (\lfloor(n-\sigma)/k\rfloor=7) |
| Error, fixed (\sigma)-defect     |   (j-\sigma) prime | (M=j-\sigma), one fiber | (\lfloor(n-\sigma)/(j-\sigma)\rfloor=1) |

Thus no pure or reserve-fixed equal-fiber split-rational packet can contain a 396-member seed.

For tangent/common-polynomial-line packets, the exact Cycle 59 ceiling is

[
\left\lfloor
\frac{n-k-t+1}{\sigma-t+1}
\right\rfloor
=============

# \left\lfloor\frac{n-k}{\sigma}\right\rfloor

395.

]

So a 396-member critical seed is not tangent. The preceding syndrome argument excludes every proper coordinate envelope, and the (\sigma)-separation excludes the pairwise close-support envelope branch.

The packet is therefore primitive relative to the canonical Cycle 59 exception list.

If “split-rational quotient” is broadened to include arbitrary maps on the configuration space of supports, then this packet is exactly such a newly required quotient. That is not a rescue of the old theorem; it is the required enlargement of the ledger.

## Formal asymptotic route cut

A separate family shows that the (n^{1+o(1)}) assertion is formally false without additional positive-rate or field-growth hypotheses.

For (s\ge3), take

[
n=2^s,\qquad
F_s=\mathbb F_{3^{2^{s-2}}},
\qquad q_s=3^{n/4}.
]

Since

[
\operatorname{ord}_{2^s}(3)=2^{s-2},
]

the order-(n) subgroup (H_s) generates (F_s). Set

[
k=1,\qquad \sigma=2,\qquad t=1,\qquad a=3,\qquad j=n-3.
]

There are no high-signature coefficients. Since (\gcd(j,n)=1), every product fiber has exactly

[
M_n=\frac1n\binom n3
=\frac{(n-1)(n-2)}6
]

supports. The color argument gives

[
|Z_n|
\ge
\frac{M_n}{1+(M_n-1)/(q_s-n)}
=============================

(1-o(1))\frac{n^2}{6}.
]

Meanwhile,

[
\frac{\binom n3}{q_s}=o(1),
]

and

[
\ell_*=n-2.
]

A pure active agreement-fiber quotient must have fiber size (3), hence has at most (n/3<\ell_*) supports; a reserve-two fixed-defect quotient has movable size one and does not exist. The tangent ceiling is (\lfloor(n-1)/2\rfloor<\ell_*), and the line is envelope-free.

Thus additional completions are (\Theta(n^2)), not (n^{1+o(1)}). This asymptotic family has exponential (q_s) and vanishing rate, so it does not by itself settle a version explicitly restricted to positive rate and (\log q=o(n)). The finite packet above lies in the intended positive-rate, (q<2^{256}), smooth same-field regime.

## Route-board impact

The proposed critical-kernel completion theorem is cut at its intended determinant-factorization step. Persistent degeneracy on a (\sigma)-separated split-support family need not factor through a pointwise map (X\mapsto X^M), a split-rational equal-fiber partition, or a common envelope.

There is a third mechanism:

[
\boxed{
T\longmapsto
c_0(L_T)
=(-1)^j\prod_{x\in T}x.
}
]

This is the determinant of multiplication by (X) on the split algebra (F[X]/(L_T)). It is a quotient on the divisor/configuration space (\operatorname{Sym}^j(H)), not a quotient of individual evaluation points.

The corrected ledger must therefore include at least

[
\boxed{
\text{occupancy}
+
\text{point-fiber quotients}
+
\text{divisor-norm/configuration characters}
+
\text{envelopes}
+
\text{remaining primitive discrepancy}.
}
]

For the basic product character, the finite charge must permit

[
\min\left{
q,,
\frac{q}{k},,
\frac{\binom n{k+\sigma}}{nq^{\sigma-2}}
\right},
]

up to absolute constants.

More generally, for a rational function (R) regular and nonzero on the domain, the canonical configuration character is

[
\chi_R(T)
=========

# \operatorname{Norm}_{F[X]/(L_T)/F}(R(X))

\prod_{x\in T}R(x).
]

If (\chi_R) has image of size (m_R), a one-condition-saving packet naturally has support scale

[
\frac{\binom nj}{m_Rq^{\sigma-2}},
]

not (\binom nj/q^{\sigma-1}).

## What remains open

The forward counterpacket is complete. The missing upper theorem is now an inverse classification problem:

1. Classify low-image divisor-norm characters (\chi_R) on smooth multiplicative domains, including their Möbius transforms, norm-one variants, and hereditary punctures.
2. Determine when several independent configuration characters save several jet conditions.
3. Prove that all character-structured completions on one affine syndrome line are coverable by a controlled number of canonical character packets.
4. Bound what remains after point-fiber quotients, configuration characters, and envelopes are removed.
5. Independently complete the (t>\sigma) thick-residue/affine-plane branch.

The finite example proves that calling the unexplained remainder “primitive finite discrepancy” without a quantitative character ledger is insufficient: the remainder can contain (2^{215}) slopes while occupancy is below (2^{29}).

## Do you see a route to a full solve?

Yes, but not through `W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION` as stated.

The next exact lemma should be:

### `W-JR-CORANK-ONE-DIVISOR-NORM-CHARACTER-TRICHOTOMY`

For a (\sigma)-separated, full-coordinate family of split locators through one (t<\sigma) JR syndrome, prove that persistent corank-one degeneration of the critical confluent-locator determinant has exactly three canonical outcomes:

[
\boxed{
\text{proper/common envelope}
\quad\text{or}\quad
\text{point-fiber split-rational quotient}
\quad\text{or}\quad
\text{low-image divisor-norm character } \chi_R.
}
]

The third outcome must be charged by

[
\min\left{
q,,
\frac{\binom nj}{|\operatorname{im}\chi_R|q^{\sigma-2}},
,
\frac qk
\right}.
]

After proving the corank-one trichotomy, the exact next step is to iterate it for multiple saved jet conditions and prove an (n^{o(1)}) cover theorem for the resulting configuration-character packets.
