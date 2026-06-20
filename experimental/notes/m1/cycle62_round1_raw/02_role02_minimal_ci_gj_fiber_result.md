BANKABLE_LEMMA

# 1. Executive verdict and confidence

The wall `L-LIST-MINIMAL-CI-GJ-FIBER` is true as stated, subject only to the explicit hypotheses already present in the wall: the nonzero syndrome has a binary apolar complete intersection

\[
I_s=(A,B),\qquad d:=\deg A=\sigma+1,\qquad \deg B=j=r-\sigma>d,
\qquad \gcd(A,B)=1,
\]

and a linear form \(L_*\) nonvanishing on \(\Delta=V(A)\) has been chosen.

**Confidence: high (0.99).**

The proof is scheme-theoretic and therefore covers nonreduced \(\Delta\), nonsplit closed points, roots at infinity, and arbitrary characteristic. The strict inequality \(j>d\) is essential: it rules out the equal-degree exceptional locator \(A\) inside the degree-\(j\) slice.

# 2. Formal theorem

Let \(F=\mathbf F_q\), let \(S=F[X_0,X_1]\), and let

\[
C=\operatorname{RS}[F,L,k],\qquad r=n-k,\qquad j=r-\sigma.
\]

Let \(s\ne0\) have apolar ideal

\[
I_s=(A,B),\qquad \deg A=d=\sigma+1,\qquad \deg B=j>d,
\qquad \gcd(A,B)=1.
\]

For \(x\in L\subset \mathbf P^1(F)\), choose a nonzero linear locator \(L_x\) vanishing at \(x\). Put

\[
\Delta=V(A),\qquad
D=L\setminus\operatorname{Supp}(\Delta).
\]

Choose a linear form \(L_*\) nonvanishing on \(\Delta\), and define

\[
R_\Delta=H^0(\Delta,\mathcal O_\Delta),\qquad
G_\Delta=R_\Delta^\times/F^\times,
\]

\[
\alpha_\Delta(x)=
\left[\left.\frac{L_x}{L_*}\right|_\Delta\right]
\quad(x\in D),
\qquad
b_\Delta=
\left[\left.\frac{B}{L_*^j}\right|_\Delta\right].
\]

For \(b\in G_\Delta\), write

\[
N_{\Delta,j}(b)=
\#\left\{T\in\binom Dj:
\prod_{x\in T}\alpha_\Delta(x)=b\right\}.
\]

Then:

1. A full-coordinate listed locator of degree \(e<j\) exists if and only if \(e=d\) and its locator is proportional to \(A\). Consequently there is exactly one such support precisely when \(\Delta\) is reduced and supported on \(L\), equivalently when \(A\) is squarefree and fully \(L\)-split. Under the fixed monic locator normalization, that locator is \(A\).

2. For every \(T\in\binom Lj\),

\[
T\text{ is a full-coordinate representation of }s
\]

if and only if

\[
T\cap\operatorname{Supp}(\Delta)=\varnothing
\quad\text{and}\quad
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta
\quad\text{in }G_\Delta.
\]

3. If \(N_s(\sigma)\) denotes the number of full-coordinate supports of sizes at most \(j\), then

\[
\boxed{
N_s(\sigma)=
\mathbf 1_{\{A\text{ squarefree and fully }L\text{-split}\}}
+N_{\Delta,j}(b_\Delta).
}
\]

4. If

\[
\Delta=\sum_{i=1}^u m_iP_i,
\qquad f_i=[\kappa(P_i):F],
\qquad d=\sum_i m_if_i,
\]

then

\[
\boxed{
|G_\Delta|
=\frac1{q-1}\prod_{i=1}^u q^{(m_i-1)f_i}(q^{f_i}-1)
=q^{d-1}\frac{\prod_i(1-q^{-f_i})}{1-q^{-1}}.
}
\]

5. Suppose \(D\ne\varnothing\), choose \(x_0\in D\), and put

\[
G_{\mathrm{eff}}=
\left\langle
\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1}:x\in D
\right\rangle.
\]

This subgroup is independent of \(x_0\). Every \(j\)-fold product lies in the single coset

\[
\alpha_\Delta(x_0)^jG_{\mathrm{eff}}.
\]

Writing

\[
\beta_x=\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1},
\qquad
h_b=b\alpha_\Delta(x_0)^{-j},
\]

one has the exact finite Fourier formula

\[
\boxed{
N_{\Delta,j}(b)=
\begin{cases}
\displaystyle
\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi\in\widehat{G_{\mathrm{eff}}}}
\chi(h_b^{-1})
[z^j]\prod_{x\in D}\bigl(1+z\chi(\beta_x)\bigr),
& h_b\in G_{\mathrm{eff}},\\[2.2ex]
0,&h_b\notin G_{\mathrm{eff}}.
\end{cases}
}
\]

The trivial-character term is exactly

\[
\frac{\binom{|D|}{j}}{|G_{\mathrm{eff}}|}.
\]

If \(D=\varnothing\), then \(j>0\) and \(N_{\Delta,j}(b)=0\).

6. All statements are independent of \(L_*\) and invariant under every admissible change

\[
A\mapsto aA,\qquad B\mapsto cB+AC,
\]

where \(a,c\in F^\times\) and \(C\in S_{j-d}\).

# 3. Full proof

## 3.1 Apolar locator and full-coordinate lemmas

For \(E\subseteq L\), \(|E|=e\le j<r\), let

\[
p_E=\prod_{x\in E}L_x\in S_e.
\]

After the standard nonzero GRS column normalization, the parity-check columns are the rational-normal-curve evaluation functionals on \(S_{r-1}\). If \(V_E\) is their span, then

\[
V_E^\perp
=\{Q\in S_{r-1}:Q(x)=0\text{ for every }x\in E\}
=p_ES_{r-1-e}.
\]

Thus, by the definition of the apolar ideal,

\[
s\in V_E
\iff
p_E\in(I_s)_e.
\tag{3.1}
\]

Since \(e<r\), the columns indexed by \(E\) are independent, so the representation of \(s\) on \(E\), if it exists, is unique.

Because \(I_s=(A,B)\) and \(e\le j<d+j=r+1\),

\[
(I_s)_e=AS_{e-d}\oplus BS_{e-j},
\tag{3.2}
\]

with \(S_t=0\) for \(t<0\). The sum is direct: if \(AU=BV\), coprimality gives \(B\mid U\), while

\[
\deg U=e-d<j=\deg B,
\]

so \(U=V=0\).

Write uniquely

\[
p_E=AU_E+BV_E.
\tag{3.3}
\]

For \(x\in E\), the coefficient of the parity-check column at \(x\) vanishes exactly when \(s\in V_{E\setminus\{x\}}\). By (3.1), this is equivalent to

\[
\frac{p_E}{L_x}\in(I_s)_{e-1}.
\]

Using uniqueness in (3.2), this occurs exactly when \(L_x\) divides both \(U_E\) and \(V_E\). Since every common divisor of \(U_E,V_E\) also divides the squarefree split form \(p_E\), every nonconstant common divisor contains one of the factors \(L_x\). Hence

\[
E\text{ is full-coordinate}
\iff
\gcd(U_E,V_E)=1.
\tag{3.4}
\]

This also proves the convention \(\gcd(U,0)=U\) needed below.

## 3.2 The lower-degree collapse

Let \(e<j\). Then \(S_{e-j}=0\), so (3.3) is

\[
p_E=AU_E.
\]

By (3.4), full-coordinate means \(U_E\in F^\times\). Therefore

\[
e=d,\qquad p_E\sim A.
\]

Conversely, if \(p_E\sim A\), then the coefficient pair is a nonzero scalar and zero, whose gcd is a unit, so the support is full-coordinate.

A squarefree locator proportional to \(A\) exists exactly when the divisor \(V(A)\) is reduced and all of its closed points are the distinct rational points indexed by a subset of \(L\). The support is then unique. With monic normalization, the locator equals \(A\).

## 3.3 The degree-\(j\) slice

At degree \(j\), (3.2) becomes

\[
(I_s)_j=AS_{j-d}\oplus FB.
\]

Thus every degree-\(j\) listed locator has a unique expression

\[
p_T=AU+cB,
\qquad U\in S_{j-d},\quad c\in F.
\tag{3.5}
\]

Because \(j-d>0\), (3.4) gives

\[
p_T\text{ is full-coordinate}
\iff c\ne0.
\tag{3.6}
\]

Indeed, if \(c\ne0\), then \(\gcd(U,c)=1\); if \(c=0\), then \(U\) has positive degree and \(\gcd(U,0)=U\) is not a unit.

## 3.4 Scheme-theoretic boundary congruence

The form \(L_*\) trivializes \(\mathcal O_{\mathbf P^1}(1)|_\Delta\). For any \(F_1,F_2\in S_j\),

\[
\left.\frac{F_1}{L_*^j}\right|_\Delta
=
\left.\frac{F_2}{L_*^j}\right|_\Delta
\iff
F_1-F_2\in AS_{j-d}.
\tag{3.7}
\]

This follows from the exact ideal-sheaf sequence

\[
0\longrightarrow\mathcal O_{\mathbf P^1}(j-d)
\xrightarrow{\cdot A}
\mathcal O_{\mathbf P^1}(j)
\longrightarrow
\mathcal O_\Delta(j)
\longrightarrow0.
\]

In particular, equality in the quotient group \(G_\Delta=R_\Delta^\times/F^\times\) gives

\[
\left[
\left.\frac{F_1}{L_*^j}\right|_\Delta
\right]
=
\left[
\left.\frac{F_2}{L_*^j}\right|_\Delta
\right]
\iff
F_1-cF_2\in AS_{j-d}
\text{ for some }c\in F^\times.
\tag{3.8}
\]

Coprimality of \(A,B\) implies that \(B|_\Delta\) is a unit. This is true at every nonreduced local factor: the image of \(B\) in the residue field at each support point is nonzero, hence its image in the corresponding Artin local ring is invertible.

For \(T\subseteq D\), every \(L_x|_\Delta\) is a unit and

\[
\left.\frac{p_T}{L_*^j}\right|_\Delta
=
\prod_{x\in T}
\left.\frac{L_x}{L_*}\right|_\Delta.
\tag{3.9}
\]

Therefore

\[
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta
\]

if and only if, by (3.8),

\[
p_T=AU+cB
\quad\text{for some }c\in F^\times.
\]

By (3.6), this is equivalent to a full-coordinate representation.

Conversely, if \(T\) is full-coordinate, (3.5)-(3.6) give such a nonzero \(c\), and restriction to \(\Delta\) gives the product equation. Moreover, \(p_T|_\Delta=cB|_\Delta\) is a unit, so \(T\) cannot contain a point of \(\operatorname{Supp}\Delta\). This proves the exact equivalence, including nonreduced and nonsplit \(\Delta\).

## 3.5 Exact count

Every full-coordinate locator of degree at most \(j\) lies either below degree \(j\) or at degree \(j\). Section 3.2 gives at most the single locator \(A\); Section 3.4 identifies the degree-\(j\) locators with the fiber of \(b_\Delta\). Since \(d<j\), the two classes are disjoint. Hence

\[
N_s(\sigma)=
\mathbf 1_{\{A\text{ squarefree and fully }L\text{-split}\}}
+N_{\Delta,j}(b_\Delta).
\]

## 3.6 Order of the generalized-Jacobian group

Decompose the finite scheme into its local components:

\[
R_\Delta\cong\prod_i R_i,
\qquad
R_i=H^0(m_iP_i,\mathcal O_{m_iP_i}).
\]

The reduction map \(R_i^\times\to\kappa(P_i)^\times\) is surjective. Its kernel is \(1+\mathfrak m_i\), of cardinality

\[
q^{(m_i-1)f_i}.
\]

Thus

\[
|R_i^\times|=q^{(m_i-1)f_i}(q^{f_i}-1).
\]

The constant subgroup \(F^\times\) embeds in \(R_\Delta^\times\), so division by \(q-1\) yields the displayed formula for \(|G_\Delta|\).

## 3.7 Effective subgroup and Fourier inversion

Assume \(D\ne\varnothing\) and choose \(x_0\in D\). Put

\[
a_0=\alpha_\Delta(x_0),\qquad
\beta_x=\alpha_\Delta(x)a_0^{-1}.
\]

Then \(\beta_x\in G_{\mathrm{eff}}\), and for every \(T\in\binom Dj\),

\[
\prod_{x\in T}\alpha_\Delta(x)
=a_0^j\prod_{x\in T}\beta_x
\in a_0^jG_{\mathrm{eff}}.
\]

If \(y_0\in D\), every generator relative to \(y_0\) is a quotient of two generators relative to \(x_0\), and conversely. Hence \(G_{\mathrm{eff}}\) is independent of the basepoint. The coset \(a_0^jG_{\mathrm{eff}}\) is likewise independent of it.

For \(h_b=ba_0^{-j}\in G_{\mathrm{eff}}\), character orthogonality gives

\[
\mathbf 1_{\{g=h_b\}}
=\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi\in\widehat{G_{\mathrm{eff}}}}
\chi(gh_b^{-1}).
\]

Summing this over \(g=\prod_{x\in T}\beta_x\), \(T\in\binom Dj\), gives

\[
N_{\Delta,j}(b)
=\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi}
\chi(h_b^{-1})
\sum_{T\in\binom Dj}\prod_{x\in T}\chi(\beta_x).
\]

The inner sum is the elementary symmetric coefficient

\[
[z^j]\prod_{x\in D}(1+z\chi(\beta_x)).
\]

If \(h_b\notin G_{\mathrm{eff}}\), the target is outside the unique product coset and the count is zero. This proves the exact finite Fourier formula.

## 3.8 Independence of \(L_*\)

Let \(L_*'\) also be nonvanishing on \(\Delta\), and put

\[
u=
\left[\left.\frac{L_*}{L_*'}\right|_\Delta\right]
\in G_\Delta.
\]

Then

\[
\alpha_\Delta'(x)=u\alpha_\Delta(x),
\qquad
b_\Delta'=u^jb_\Delta.
\]

Thus

\[
\prod_{x\in T}\alpha_\Delta'(x)=b_\Delta'
\iff
u^j\prod_{x\in T}\alpha_\Delta(x)=u^jb_\Delta,
\]

so the fiber is unchanged. Ratios \(\alpha_\Delta'(x)\alpha_\Delta'(x_0)^{-1}\) equal the old ratios, and

\[
b_\Delta'\alpha_\Delta'(x_0)^{-j}
=b_\Delta\alpha_\Delta(x_0)^{-j}.
\]

Hence the effective group and every term of the normalized Fourier formula are independent of \(L_*\).

## 3.9 Generator shear

Let

\[
B'=cB+AC,
\qquad c\in F^\times,\quad C\in S_{j-d}.
\]

On \(\Delta\),

\[
B'|_\Delta=cB|_\Delta,
\]

so

\[
\left[\left.\frac{B'}{L_*^j}\right|_\Delta\right]
=
\left[\left.\frac{B}{L_*^j}\right|_\Delta\right]
=b_\Delta
\]

in the quotient by \(F^\times\). Thus the generalized-Jacobian target is shear-invariant.

At the coefficient-pair level,

\[
p=AU+BV
=A\left(U-c^{-1}CV\right)+B'\left(c^{-1}V\right).
\]

The two coefficient pairs generate the same ideal in \(S\), so the gcd/full-coordinate condition is unchanged. Scaling \(A\) by a nonzero scalar leaves the divisor \(\Delta\) unchanged.

# 4. Parameter ledger and finite relevance

\[
\begin{array}{c|c}
\text{parameter}&\text{exact value or role}\\ \hline
q&|F|\\
n&|L|\\
r&n-k\\
d&\sigma+1\\
j&r-\sigma\\
d+j&r+1\\
j>d&r>2\sigma+1\\
\deg\Delta&d\\
D&L\setminus\operatorname{Supp}\Delta\\
\text{lower-layer contribution}&0\text{ or }1\\
\text{degree-}j\text{ contribution}&N_{\Delta,j}(b_\Delta)\\
\text{ambient finite group}&G_\Delta\\
\text{effective Fourier group}&G_{\mathrm{eff}}\le G_\Delta
\end{array}
\]

The exact baseline term in the effective Fourier expansion is

\[
\binom{|D|}{j}/|G_{\mathrm{eff}}|,
\]

not \(\binom nj/q^\sigma\), not \(\binom nj/|G_\Delta|\), and not an asymptotic surrogate. All deviations are the explicitly displayed nontrivial-character terms.

# 5. Bankable versus conditional

## Bankable

- The lower-degree collapse to the unique possible locator \(A\).
- The exact degree-\(j\) generalized-Jacobian fiber equivalence.
- The exact list-count identity.
- The group-order formula for arbitrary reduced, nonreduced, split, or nonsplit \(\Delta\).
- The effective product coset and exact Fourier expansion.
- Independence of \(L_*\), locator scaling, and the basepoint \(x_0\).
- Invariance under all admissible unequal-degree generator changes.

## Conditional / not supplied by this lemma

- No bound is proved for the nontrivial Fourier terms.
- No quotient-character classification is proved.
- No local-limit or prize-threshold certificate follows merely from the fiber identity.
- The statement assumes the specified minimal CI degree stratum and the existence of a chosen \(L_*\) nonvanishing on \(\Delta\).

# 6. Failure point and edge boundaries

There is no failure point in the claimed lemma.

The strict hypothesis \(j>d\) is necessary for the displayed count in this form. If \(j=d\), then both \(U\) and \(V\) are scalars in degree \(j\), and the locator proportional to \(A\) is itself full-coordinate with \(V=0\). It must then be separated from the unit-boundary fiber to avoid omission or double counting. That edge is excluded here by \(j>\sigma+1=d\).

# 7. Next exact lemma and route to a full solve

Yes, conditionally, there is a route to a full solve. This lemma closes the algebraic reduction of the minimal scalar stratum. The next exact wall is

```text
W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT
```

in the model modulus \(\Delta=[0]+\sigma[\infty]\): define the canonical quotient generated jointly by all periodic pullback characters, and prove a finite bound for the remaining nontrivial terms in

\[
\frac1{|G_{\mathrm{eff}}|}
\sum_{\chi\ne1}
\chi(h^{-1})[z^j]\prod_{x\in D}(1+z\chi(\beta_x)).
\]

The theorem must retain the exact occupancy term \(\binom{|D|}{j}/|G_{\mathrm{eff}}|\), use a disjoint or bounded-overlap quotient charge, and give explicit integer constants. After that, the route still requires extension from the model modulus to arbitrary \(\Delta\), then to the higher minimal-generator strata, before the finite scalar/interleaved certificate closes.
