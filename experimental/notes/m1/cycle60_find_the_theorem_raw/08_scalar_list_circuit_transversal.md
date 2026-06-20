BANKABLE_LEMMA

**Confidence:** high for the scalar identity, circuit reduction, syzygy-bundle formula, projection theorem, and counterpacket below; moderate for the proposed route to the final structural cover theorem.

The full scalar theorem is not yet proved. The exact remaining obstruction is considerably narrower than the raw syndrome-fiber problem: one must cover low-arity dependencies among full agreement locators.

## Exact theorem package

Let
[
C=\operatorname{RS}[F,L,k],\qquad q=|F|,\qquad n=|L|,\qquad r=n-k,
]
and fix
[
a=k+\sigma,\qquad j=r-\sigma,\qquad \sigma\ge1.
]

For a received word (y), let (s=Hy^{\mathsf T}), where (H) is an RS parity-check matrix. For a listed codeword (P), put
[
A(P)={x\in L:P(x)=y(x)},
]
[
E(P)=L\setminus A(P),\qquad e(P)=|E(P)|,
]
and define its actual reserve
[
\tau(P):=r-e(P)=|A(P)|-k\ge \sigma.
]

### 1. Exact scalar full-support identity

For (s\in F^r), define
[
\nu_e^\circ(s)=
#\left{
E\subseteq L:
|E|=e,\
s=H_Ec\text{ for some }c\in(F^\times)^E
\right}.
]

Then
[
\boxed{
L_{\rm sc}(a)
=============

\max_{s\in F^r}
\sum_{e=0}^{r-\sigma}\nu_e^\circ(s).
}
]

This counts actual codewords, not feasible padded supports. Since (e<r), the RS/MDS property makes (H_E) injective, so the coefficient vector (c) is unique.

Full agreement supports are canonical: two listed codewords with the same (A(P)) are equal.

---

### 2. Full-support circuit reduction

Write
[
\Lambda_L(X)=\prod_{x\in L}(X-x).
]

For (P) in the scalar list, define the error and agreement locators
[
p_P(X)=\prod_{x\in E(P)}(X-x),\qquad
G_P(X)=\prod_{x\in A(P)}(X-x).
]
Thus
[
p_PG_P=\Lambda_L.
]

Associate to (P) the (\tau(P))-dimensional subspace
[
W_P:=p_PF[X]*{<\tau(P)}\subseteq F[X]*{<r}.
]

Under the standard syndrome pairing,
[
\boxed{W_P\subseteq s^\perp.}
]

A **full-support circuit** is a support-minimal family
(\mathcal I={P_1,\ldots,P_m}) for which there exist nonzero polynomials
(U_i), with
[
\deg U_i<\tau(P_i),
]
such that
[
\boxed{
\sum_{i=1}^m U_i(X)p_{P_i}(X)=0.
}
\tag{1}
]

Dividing by (\Lambda_L) gives the canonical full-agreement form
[
\boxed{
\sum_{i=1}^m\frac{U_i(X)}{G_{P_i}(X)}=0.
}
\tag{2}
]

This is the denominator-free scalar analogue of the split-locator obstruction. It involves the actual full agreement supports and automatically retains every overagreement layer.

#### Circuit-hitting theorem

Let (Z_s) be a set of listed codewords meeting every full-support circuit for syndrome (s). Then
[
\boxed{
\sum_{P\in\mathcal L_s\setminus Z_s}\tau(P)\le r-1.
}
\tag{3}
]

Consequently,
[
\boxed{
|\mathcal L_s|
\le
|Z_s|+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor.
}
\tag{4}
]

It is sufficient for (Z_s) to hit circuits of cardinality at most
[
\ell_\sigma:=\left\lceil\frac r\sigma\right\rceil.
]
Indeed, any (\ell_\sigma) remaining codewords have total reserve at least (r), forcing a relation (1) supported on at most those (\ell_\sigma) codewords.

Thus the scalar list problem has the exact finite reduction
[
\boxed{
L_{\rm sc}(a)
\le
U_{\rm circuit}
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor,
}
\tag{5}
]
where (U_{\rm circuit}) is an upper bound on a canonical template-charged circuit transversal.

This is stronger than separately summing all overagreement layers: a codeword with (h) extra agreements contributes (\sigma+h), not merely one unit, to (3).

---

### 3. Exact syzygy-bundle excess formula

Select distinct listed codewords (P_1,\ldots,P_m). Write
[
E_i=E(P_i),\qquad e_i=|E_i|,\qquad \tau_i=r-e_i.
]

Let
[
D=\bigcap_{i=1}^mE_i,\qquad d=|D|,\qquad r'=r-d,
]
and factor
[
p_{E_i}=p_D\widetilde p_i,\qquad
\deg\widetilde p_i=e_i-d=r'-\tau_i.
]

Then (\gcd(\widetilde p_1,\ldots,\widetilde p_m)=1). Homogenizing gives a basepoint-free sequence on (\mathbf P^1):
[
0\longrightarrow\mathcal K
\longrightarrow
\bigoplus_{i=1}^m\mathcal O_{\mathbf P^1}(-(e_i-d))
\xrightarrow{(\widetilde p_1,\ldots,\widetilde p_m)}
\mathcal O_{\mathbf P^1}
\longrightarrow0.
]

Write its Birkhoff–Grothendieck splitting as
[
\mathcal K
\simeq
\bigoplus_{\nu=1}^{m-1}\mathcal O_{\mathbf P^1}(-\delta_\nu).
]

Then
[
\sum_{\nu=1}^{m-1}\delta_\nu
============================

\sum_{i=1}^m(e_i-d),
]
and
[
\boxed{
\dim_F
\left(
\frac{\bigcap_iV_{E_i}}{V_D}
\right)
=======

\sum_{\nu=1}^{m-1}(\delta_\nu-r')_+.
}
\tag{6}
]

Because the same syndrome (s) has full-coordinate representations on all the distinct (E_i), its class modulo (V_D) is nonzero. Hence
[
\boxed{
\sum_{\nu=1}^{m-1}(\delta_\nu-r')_+\ge1.
}
\tag{7}
]

If
[
\sum_i\tau_i\ge r',
]
then
[
\frac1{m-1}\sum_\nu\delta_\nu
=============================

r'+\frac{r'-\sum_i\tau_i}{m-1}
\le r'.
]
Therefore (7) is a genuine splitting imbalance: at least one
[
\delta_\nu\ge r'+1
]
despite the average being at most (r').

This is the exact geometric obstruction that the scalar container theorem must classify. In particular, a dimension-critical packet with balanced splitting cannot occur in an actual full-support list.

---

### 4. Exclusive-agreement defect bound

For a support-minimal circuit (1), define the agreement points exclusive to (P_i) within the circuit:
[
X_i=
A(P_i)\setminus\bigcup_{h\ne i}A(P_h).
]

Then
[
\boxed{|X_i|\le\tau_i-1.}
\tag{8}
]

Indeed, evaluating (1) at (x\in X_i) kills every term except
(U_i(x)p_{E_i}(x)). Since (p_{E_i}(x)\ne0), one has (U_i(x)=0).

Thus every critical circuit is a low-defect, multiply covered system of full agreement supports. The private defect is automatically bounded by the actual overagreement reserve.

---

### 5. Exact common-core and quotient accounting

#### Common agreement core

Suppose a sublist has a common agreement core
[
C_0\subseteq\bigcap_PA(P),\qquad |C_0|=c<k.
]

Choose (P_0) in the sublist. Every other polynomial has a unique expression
[
P=P_0+L_{C_0}Q,\qquad \deg Q<k-c.
]

On (L'=L\setminus C_0), define
[
y_{C_0}(x)=\frac{y(x)-P_0(x)}{L_{C_0}(x)}.
]

Then
[
A_{y_{C_0}}(Q)=A_y(P)\setminus C_0,
]
and
[
|A_{y_{C_0}}(Q)|\ge(k-c)+\sigma.
]

Hence a common-core container is exactly a hereditary scalar-list instance
[
\boxed{
(n,k,\sigma)\longmapsto(n-c,k-c,\sigma).
}
\tag{9}
]

If (c\ge k), the sublist has size one.

#### Fixed split-rational packet

Let (R=P/Q\in F(X)) have no pole on the relevant part of (L), and suppose its split fibers
[
\mathcal F_\beta={x\in L:R(x)=\beta},
\qquad \beta\in\Omega,
]
all have size (M).

Fix a defect (T), and suppose an exact-reserve-(\tau) packet has full supports
[
A(P)=
T\sqcup\bigsqcup_{\beta\in B(P)}\mathcal F_\beta.
]

Let (c_T) be the number of fibers meeting (T), and put
[
b_\tau=\frac{k+\tau-|T|}{M}.
]

Then, whenever (b_\tau) is integral,
[
\boxed{
|\mathcal Q_{R,T,\tau}|
\le
\binom{|\Omega|-c_T}{b_\tau}.
}
\tag{10}
]

This follows because distinct codewords have distinct full supports. For agreement at least (k+\sigma), the fixed-packet charge is the corresponding sum of (10) over (\tau\ge\sigma).

The action rank
[
d_R(E)=\deg\minpoly([R(X)]\bmod E)
]
is a classifier for finding such packets. The actual scalar-list budget is the full support profile (10), not merely the action-rank integer.

---

## Proof of the circuit theorem

For every listed (P), the syndrome (s) lies in (V_{E(P)}). Therefore it annihilates
[
V_{E(P)}^\perp
==============

# p_PF[X]_{<r-e(P)}

W_P.
]
Hence (W_P\subseteq s^\perp).

Suppose (Z_s) meets every circuit. Then the sum map
[
\bigoplus_{P\in\mathcal L_s\setminus Z_s}W_P
\longrightarrow F[X]_{<r}
]
is injective: any nonzero kernel vector would have a support-minimal subrelation, producing a circuit disjoint from (Z_s).

Its image lies in the ((r-1))-dimensional hyperplane (s^\perp), so
[
\sum_{P\in\mathcal L_s\setminus Z_s}\dim W_P
============================================

\sum_{P\in\mathcal L_s\setminus Z_s}\tau(P)
\le r-1.
]
This proves (3) and (4).

If (s=0), then (y) is itself a codeword. Any other codeword agreeing with (y) on at least (k+\sigma\ge k+1) points would equal (y), so the list size is one.

---

## Exact projection to every interleaving arity

Let (C\subseteq F^n) be any linear code. Let (L_m(a)) be the worst (m)-interleaved list size at column agreement at least (a).

### Projection theorem

If
[
L_1(a)\le U
\qquad\text{and}\qquad
\binom{U+1}{2}<q,
]
then for every (m\ge1),
[
\boxed{L_m(a)\le U.}
\tag{11}
]

Suppose (U+1) distinct interleaved codeword tuples lie in one list. For
(\lambda\in F^m), project by
[
\pi_\lambda(c_1,\ldots,c_m)=\sum_{j=1}^m\lambda_jc_j.
]

For each pair of distinct tuples, the projections collide on a proper linear subspace of (F^m), containing at most (q^{m-1}) choices of (\lambda). The union of all collision subspaces contains fewer than
[
\binom{U+1}{2}q^{m-1}<q^m
]
vectors. A projection outside the union makes all (U+1) projected codewords distinct.

Every column agreement survives projection, producing (U+1) scalar listed codewords, a contradiction.

Conversely,
[
L_m(a)\ge L_1(a)
]
by the embedding
[
P\longmapsto(P,0,\ldots,0).
]

### The (2^{-128}) scale

Put
[
T_q=\left\lfloor\frac q{2^{128}}\right\rfloor.
]

When (q\le2^{256}),
[
\boxed{\binom{T_q+1}{2}<q.}
\tag{12}
]

Indeed, (T_q\le2^{128}), and for (T_q>0),
[
\frac{T_q(T_q+1)}2
<
2^{128}T_q
\le q.
]

Therefore, in the official same-field regime,
[
\boxed{
L_m(k+\sigma)\le T_q
\quad\Longleftrightarrow\quad
L_1(k+\sigma)\le T_q
}
\tag{13}
]
for every interleaving arity (m).

If the challenge and code fields differ, the exact condition is instead
[
T_{\rm chal}(T_{\rm chal}+1)<2q_{\rm code}.
]
A large challenge field cannot pay the projection collision bill over a smaller code field.

For (B\subseteq F) with (L\subseteq B), coordinate expansion gives
[
\operatorname{RS}[F,L,k]^{=m}
\cong
\operatorname{RS}[B,L,k]^{=m[F:B]}
]
with exact preservation of column agreement. Projection must then be paid over (B).

---

## Actual-list counterpacket to quotient-plus-common-core alone

A registry containing only fixed-defect split-rational packets and common agreement cores is false for general RS domains. A low-affine-rank envelope term is indispensable.

Let
[
K=\mathbb F_{2^h},\qquad F=\mathbb F_{2^{2h}},
]
and choose (\theta\in F\setminus K). Put (m=2^h), and for (u\in K) define
[
t_u=u+\theta u^3.
]

The set ({t_u:u\in K}) is additive Sidon: if
[
t_u+t_v=t_{u'}+t_{v'}
]
for (u\ne v) and (u'\ne v'), comparison in the (K)-basis
({1,\theta}) gives
[
u+v=u'+v',\qquad u^3+v^3=u'^3+v'^3.
]
Since in characteristic two
[
u^3+v^3=(u+v)^3+uv(u+v),
]
the sum and product of the pair are determined, so
[
{u,v}={u',v'}.
]

Take the evaluation domain
[
L={t_u+t_v:u,v\in K,\ u\ne v}.
]
Thus
[
n=\binom m2<|F|.
]

Use (k=2), and define
[
P_u(X)=t_uX+t_u^2.
]
At the coordinate (x_{uv}=t_u+t_v),
[
P_u(x_{uv})=P_v(x_{uv})=t_ut_v.
]
Define
[
y(x_{uv})=t_ut_v.
]

No third codeword agrees there: if (w\notin{u,v}), then
[
P_w-P_u=(t_w+t_u)(X+t_w+t_u),
]
whose unique root is (t_w+t_u\ne t_v+t_u).

Hence
[
\boxed{
A(P_u)={x_{uv}:v\ne u},
\qquad |A(P_u)|=m-1.
}
]

The (m) codewords are distinct, every agreement support is exact and full, and
[
\sigma=(m-1)-2=m-3.
]

There is no common agreement coordinate and no overagreement. Moreover, no nontrivial partition of (L) into equal fibers can make every support (A(P_u)) a union of fibers: the incidence vector of (x_{uv}) across the supports has ones exactly in positions (u,v), and these incidence vectors are all distinct. Thus every such fiber must be a singleton.

For (h=127),
[
q=2^{254},\qquad
T_q=2^{126},\qquad
|{P_u}|=2^{127}>T_q.
]

The evaluation domain generates (F), but its rate and domain shape are not official. This is therefore not an official-rate counterexample. It is a precise route cut:

[
\boxed{
\text{split-rational quotient + common-core alone is not a scalar container theorem.}
}
]

The missing packet is a low-affine-rank polynomial-envelope incidence family.

---

## Parameter ledger

| Quantity                            | Exact role                                   |      |                                             |
| ----------------------------------- | -------------------------------------------- | ---- | ------------------------------------------- |
| (q=                                 | F                                            | )    | Scalar alphabet and projection field        |
| (T_q=\lfloor q/2^{128}\rfloor)      | Exact prize list numerator                   |      |                                             |
| (r=n-k)                             | Syndrome dimension                           |      |                                             |
| (a=k+\sigma)                        | Minimum agreement                            |      |                                             |
| (j=r-\sigma)                        | Maximum error weight                         |      |                                             |
| (e(P))                              | Exact error weight                           |      |                                             |
| (\tau(P)=r-e(P))                    | Actual reserve, including overagreement      |      |                                             |
| (W_P=p_PF[X]_{<\tau(P)})            | Full-support syndrome-annihilator block      |      |                                             |
| (\ell_\sigma=\lceil r/\sigma\rceil) | Maximum arity needing circuit classification |      |                                             |
| (\lfloor(r-1)/\sigma\rfloor)        | Exact circuit-free list remainder            |      |                                             |
| (M)                                 | Split-rational fiber size                    |      |                                             |
| (N=                                 | \Omega                                       | )    | Number of usable quotient fibers            |
| (b_\tau=(k+\tau-                    | T                                            | )/M) | Number of selected fibers in an exact layer |
| (\binom{N-c_T}{b_\tau})             | Exact fixed-packet full-support charge       |      |                                             |

---

## Route-board impact

The interleaved projection wall is closed in the same-field official regime.

The scalar problem is now an exact **circuit transversal problem**, not an independent bound for every (\nu_e^\circ(s)). Overagreement is automatically weighted correctly by (\tau(P)).

The canonical finite scalar theorem would be:
[
\boxed{
U_{\rm quot}
+
U_{\rm core}^{\rm her}
+
U_{\rm env}^{\rm her}
+
U_{\rm prim}
+
\left\lfloor\frac{r-1}{\sigma}\right\rfloor
\le T_q,
}
\tag{14}
]
where the first four terms bound a canonical set of codewords meeting every full-support circuit of arity at most (\ell_\sigma).

Fixed split-rational packets have the exact support-profile charge (10). Common agreement cores descend exactly by (9). The star packet proves that affine/polynomial-envelope circuits cannot be omitted.

The Hilbert–Burch formula (6) supplies the intrinsic primitive diagnostic: after stripping common error cores, every actual dimension-critical packet has positive splitting excess above (r').

## What remains open

The unresolved scalar finite bound is now exactly
[
\boxed{
\max_{s\in F^r}
U_{\rm hit}(s)
\le
T_q-
\left\lfloor\frac{r-1}{\sigma}\right\rfloor,
}
\tag{15}
]
where (U_{\rm hit}(s)) is the size of a canonical quotient/core/envelope/primitive set meeting every low-arity full-support circuit for syndrome (s).

What is missing is not the projection theorem or the handling of overagreement. It is a finite cover theorem proving that all positive-excess circuits are collectively charged by:

[
\text{split-rational packets}
+\text{hereditary common cores}
+\text{low-affine-rank envelopes}
+\text{a bounded primitive exceptional registry}.
]

The fixed-packet profile is known, but a bounded-overlap cover across all rational maps, defects, cores, and envelopes is not.

To determine the exact prize threshold, one additionally needs an actual list of more than (T_q) codewords at the previous integer reserve.

## Do you see a route to a full solve?

Yes, with moderate confidence.

The next exact lemma is:

[
\boxed{
\texttt{W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER}.
}
]

For every official smooth same-field domain and every support-minimal relation
[
\sum_{i=1}^m\frac{U_i(X)}{G_i(X)}=0,
\qquad
\deg U_i<\tau_i,
\qquad
m\le\left\lceil\frac r\sigma\right\rceil,
]
where (G_i=L_{A(P_i)}), prove that after exact common-core descent, one of the following holds:

1. the packet lies in a bounded low-affine-rank polynomial envelope;
2. the (G_i) factor, up to explicitly charged defects, through the fibers
   [
   P(X)-\beta Q(X)
   ]
   of a split-rational map (R=P/Q), with its full support profile and (d_R)-certificate;
3. the circuit belongs to a primitive exceptional family whose total circuit-hitting number has an explicit finite bound.

The lemma must output a **global hitting set**, not merely classify one packet at a time, and must prove
[
|Z_s|
\le
T_q-\left\lfloor\frac{r-1}{\sigma}\right\rfloor
]
uniformly in (s). Combined with the circuit theorem and projection, that would solve the grand interleaved list challenge.
