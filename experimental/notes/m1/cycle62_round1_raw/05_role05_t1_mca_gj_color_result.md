BANKABLE_LEMMA

# t=1 MCA generalized-Jacobian support-plus-color theorem

## 1. Executive verdict and confidence

**Verdict.** The wall `L-JR-T1-GJ-FIBER-AND-COLOR` closes after one necessary correction: the degree-\(\sigma\) modulus
\(\Delta=V(A)\) controls supports, but colors are controlled by the one-point thickening

\[
\Delta^+=\Delta+[\beta],
\]

where \(\beta\) is the external evaluation point of the shifted \(t=1\) slice. The old generalized-Jacobian fiber is the union of the colored fibers lying above it under

\[
\pi:G_{\Delta^+}\longrightarrow G_\Delta.
\]

The reduced MCA color is an explicit projective-linear coordinate on this lift fiber. Consequently, two generalized-Jacobian supports give the same MCA slope exactly when they have the same \(\Delta^+\)-lift.

The proposed identity

\[
\chi(T,c)=-\lambda_Tc
\]

is correct as the definition of reduced color. What is not always correct is the stronger implicit claim that this color is determined by the scalar comparison
\(P_T|_\Delta=\gamma_TB|_\Delta\). That scalar determines the color only when
\(\beta\notin\operatorname{Supp}\Delta\). When \(\beta\in\operatorname{Supp}\Delta\), \(\gamma_T\) is constant on the entire support fiber and the color is the new infinitesimal coordinate supplied by \(\Delta^+\).

**Confidence:** high. The proof is finite-dimensional algebra and works in arbitrary characteristic, for reduced or nonreduced \(\Delta\), and for nonsplit closed points. A complete \(\mathbf F_{11}\) counterexample to the unthickened scalar-color claim is included below.

---

## 2. Setup and normalization

Let \(F=\mathbf F_q\), let \(D\subset \mathbf P^1(F)\) have size \(n\), and let
\(\beta\in\mathbf P^1(F)\setminus D\) be the external point in the shifted \(t=1\) normal form. Put

\[
R=n-k-1,
\qquad
j=n-k-\sigma,
\qquad
R=j+\sigma-1,
\qquad
j\ge \sigma\ge1.
\]

After a projective change sending \(\beta\) to infinity and the standard nonzero GRS column rescaling, write \(D\subset F\) and take

\[
h_x=(1,x,\ldots,x^{R-1})^{\mathsf T},
\qquad
\lambda_x=x^R.
\]

Thus, for an error vector supported on \(T\) with rescaled nonzero coordinates
\(c=(c_x)_{x\in T}\),

\[
H_Tc=s=(s_0,\ldots,s_{R-1}),
\qquad
\lambda_Tc=\sum_{x\in T}c_xx^R.
\]

The reduced color and actual slope are

\[
\chi(T,c):=-\lambda_Tc,
\qquad
z(T,c)=\lambda(w)+\chi(T,c).
\]

Changing the augmented parity-check row by
\(\lambda\mapsto a\lambda+\varphi H\), \(a\ne0\), changes all reduced colors for the fixed syndrome by the same affine bijection

\[
\chi\mapsto a\chi-\varphi(s).
\]

Hence the normalization above preserves all color collisions and the exact number of distinct slopes.

The zero syndrome has no nonzero full-coordinate representation of weight at most \(j<R\), by the MDS column-independence property, so its numerator is zero. Henceforth let the syndrome be nonzero.

Let the apolar ideal of the nonzero syndrome be

\[
I_s=(A,B),
\qquad
\deg A=\sigma,
\qquad
\deg B=j,
\qquad
\gcd(A,B)=1.
\]

Here \(B\) is the degree-\(j\) apolar generator, not the numerator denoted \(B\) in some jet-residue presentations. Write the affine dehomogenizations

\[
A(X)=\sum_{i=0}^{\sigma}a_iX^i,
\qquad
B(X)=\sum_{i=0}^{j}b_iX^i.
\]

The top coefficients \(a_\sigma\) or \(b_j\) are allowed to vanish: the forms retain homogeneous degrees \(\sigma\) and \(j\).

---

## 3. Formal theorem

### Theorem A — uncolored generalized-Jacobian support fiber

Let

\[
\Delta=V(A),
\qquad
D^\circ=D\setminus\operatorname{Supp}\Delta,
\qquad
G_\Delta=H^0(\Delta,\mathcal O_\Delta)^\times/F^\times.
\]

Choose a linear form \(L_*\) nonvanishing on \(\Delta\). For \(x\in D^\circ\), let

\[
\alpha_\Delta(x)=
\left[
\left.\frac{L_x}{L_*}\right|_\Delta
\right],
\qquad
b_\Delta=
\left[
\left.\frac{B}{L_*^j}\right|_\Delta
\right].
\]

For \(T\in\binom Dj\), let

\[
P_T(X)=\prod_{x\in T}(X-x)
\]

be the monic locator. Except for the separate locator \(A\), the following are equivalent:

\[
\begin{aligned}
& T\text{ is a full-coordinate representation of }s,\\
& T\subseteq D^\circ
\quad\text{and}\quad
\prod_{x\in T}\alpha_\Delta(x)=b_\Delta
\quad\text{in }G_\Delta.
\end{aligned}
\]

For every such \(T\), there is a unique \(\gamma_T\in F^\times\) and a unique
\(U_T\in F[X]_{\le j-\sigma}\) such that

\[
P_T=A U_T+\gamma_TB,
\tag{3.1}
\]

and equivalently

\[
\left.\frac{P_T}{L_*^j}\right|_\Delta
=
\gamma_T
\left.\frac{B}{L_*^j}\right|_\Delta.
\tag{3.2}
\]

The only full-coordinate representation of weight less than \(j\) is the locator \(A\), and it occurs precisely when \(A\) is a scalar multiple of a squarefree locator split completely over \(D\).

### Theorem B — exact external-color matrix

For (3.1), define

\[
u_T=[X^{j-\sigma}]U_T.
\]

Define two syndrome-dependent scalars

\[
\eta_A:=\sum_{i=0}^{\sigma-1}a_i s_{i+j-1},
\qquad
\eta_B:=\sum_{i=0}^{j-1}b_i s_{i+\sigma-1},
\tag{3.3}
\]

and the matrix

\[
\mathcal M_s=
\begin{pmatrix}
 a_\sigma & b_j\\
 \eta_A & \eta_B
\end{pmatrix}.
\tag{3.4}
\]

Then

\[
\boxed{
\mathcal M_s
\binom{u_T}{\gamma_T}
=
\binom{1}{\chi(T,c_T)}
}
\tag{3.5}
\]

for the unique full-coordinate coefficient vector \(c_T\), and

\[
\boxed{
\det\mathcal M_s\ne0.
}
\tag{3.6}
\]

Therefore two degree-\(j\) supports \(T,T'\) give the same MCA slope if and only if

\[
(u_T,\gamma_T)=(u_{T'},\gamma_{T'}).
\tag{3.7}
\]

There are two exact cases.

#### Case 1: \(\beta\notin\operatorname{Supp}\Delta\)

Then \(a_\sigma\ne0\), and

\[
\chi_A:=\frac{\eta_A}{a_\sigma},
\qquad
\kappa:=\eta_B-\frac{b_j\eta_A}{a_\sigma}
e0.
\]

Hence

\[
\boxed{
\chi(T,c_T)=\chi_A+\kappa\gamma_T.
}
\tag{3.8}
\]

Thus the old scalar lift \(\gamma_T\) determines the color, but only up to a noncanonical affine change. After translating the color by \(-\chi_A\) and rescaling the degree-\(j\) generator, one may normalize the relation to \(\chi=\gamma_T\) or \(\chi=-\gamma_T\).

If \(A\) is a squarefree \(D\)-split locator, its lower-weight representation has color \(\chi_A\). No degree-\(j\) full-coordinate support has this color.

#### Case 2: \(\beta\in\operatorname{Supp}\Delta\)

Then \(a_\sigma=0\), while \(b_j\ne0\), and monicity forces

\[
\gamma_T=b_j^{-1}
\]

for every degree-\(j\) support in the old generalized-Jacobian fiber. Moreover

\[
\eta_A\ne0,
\qquad
\boxed{
\chi(T,c_T)=\eta_Au_T+\eta_Bb_j^{-1}.
}
\tag{3.9}
\]

Thus \(\gamma_T\) is constant and carries no color information. The missing color coordinate is the next local jet \(u_T\) at \(\beta\).

### Theorem C — colored generalized-Jacobian lift

Let \(E_\beta=X_0\) be the linear form vanishing at \(\beta=[0:1]\), and put

\[
\Delta^+=V(AE_\beta)=\Delta+[\beta],
\qquad
G_{\Delta^+}=H^0(\Delta^+,\mathcal O_{\Delta^+})^\times/F^\times.
\]

Restriction induces a surjection

\[
\pi:G_{\Delta^+}\twoheadrightarrow G_\Delta.
\tag{3.10}
\]

Its kernel is

\[
\ker\pi\cong
\begin{cases}
F^\times,&\beta\notin\operatorname{Supp}\Delta,\\
(F,+),&\beta\in\operatorname{Supp}\Delta,
\end{cases}
\qquad
|\ker\pi|=
\begin{cases}
q-1,&\beta\notin\operatorname{Supp}\Delta,\\
q,&\beta\in\operatorname{Supp}\Delta.
\end{cases}
\tag{3.11}
\]

Choose \(L_*\) nonvanishing on \(\Delta^+\), and define

\[
\alpha_{\Delta^+}(x)=
\left[
\left.\frac{L_x}{L_*}\right|_{\Delta^+}
\right]
\qquad(x\in D^\circ).
\]

For each \(\chi\in F\), let \((u_\chi,\gamma_\chi)\) be the unique solution of

\[
\mathcal M_s
\binom{u_\chi}{\gamma_\chi}
=
\binom{1}{\chi}.
\tag{3.12}
\]

When \(\gamma_\chi\ne0\), set

\[
Q_\chi=
\gamma_\chi B+u_\chi A X_1^{j-\sigma}
\]

and

\[
b_\chi^+=
\left[
\left.\frac{Q_\chi}{L_*^j}\right|_{\Delta^+}
\right]
\in G_{\Delta^+}.
\tag{3.13}
\]

Then

\[
\boxed{
T\in\binom{D^\circ}{j}
\text{ is full-coordinate of reduced color }\chi
\iff
\prod_{x\in T}\alpha_{\Delta^+}(x)=b_\chi^+.
}
\tag{3.14}
\]

Moreover,

\[
\boxed{
\chi\longmapsto b_\chi^+
}
\tag{3.15}
\]

is a bijection from \(\{\chi:\gamma_\chi\ne0\}\) onto the entire lift fiber

\[
\pi^{-1}(b_\Delta).
\tag{3.16}
\]

Thus the external colors are exactly the generalized-Jacobian lifts above the old support target.

---

## 4. Exact support, color, and slope numerators

For \(g\in G_{\Delta^+}\), define the exact lifted subset-product fiber

\[
N^+_{\Delta^+,j}(g)
:=
\#\left\{
T\in\binom{D^\circ}{j}:
\prod_{x\in T}\alpha_{\Delta^+}(x)=g
\right\}.
\tag{4.1}
\]

Let

\[
\varepsilon_A=
\mathbf 1_{\{A\text{ is squarefree and completely }D\text{-split}\}}.
\]

Then the number of full-coordinate support representations is

\[
\boxed{
R_{\mathrm{supp}}(s)
=
\varepsilon_A
+
\sum_{g\in\pi^{-1}(b_\Delta)}
N^+_{\Delta^+,j}(g)
=
\varepsilon_A+N_{\Delta,j}(b_\Delta).
}
\tag{4.2}
\]

The exact distinct-color, hence distinct-slope, numerator is instead

\[
\boxed{
M_{t=1,d=\sigma}(s)
=
\varepsilon_A
+
\#\left\{
g\in\pi^{-1}(b_\Delta):
N^+_{\Delta^+,j}(g)>0
\right\}.
}
\tag{4.3}
\]

For a fixed \(g=b_\chi^+\), the number
\(N^+_{\Delta^+,j}(g)\) is exactly the number of support representations colliding at the one slope \(\lambda(w)+\chi\). In particular,

\[
\boxed{
T,T'\text{ have the same slope}
\iff
\prod_{x\in T}\alpha_{\Delta^+}(x)
=
\prod_{x\in T'}\alpha_{\Delta^+}(x).
}
\tag{4.4}
\]

Formula (4.3), not (4.2), is the MCA numerator.

---

## 5. Effective subgroup conditioning and exact Fourier formula

If \(|D^\circ|<j\), every degree-\(j\) fiber below is empty and the formulas are immediate. Otherwise fix \(x_0\in D^\circ\), and define

\[
G_{\mathrm{eff}}^+
=
\left\langle
\alpha_{\Delta^+}(x)\alpha_{\Delta^+}(x_0)^{-1}:
 x\in D^\circ
\right\rangle
\le G_{\Delta^+},
\tag{5.1}
\]

\[
G_{\mathrm{eff}}=\pi(G_{\mathrm{eff}}^+),
\qquad
K_{\mathrm{col}}=G_{\mathrm{eff}}^+\cap\ker\pi.
\tag{5.2}
\]

Then

\[
1\longrightarrow K_{\mathrm{col}}
\longrightarrow G_{\mathrm{eff}}^+
\xrightarrow{\pi}G_{\mathrm{eff}}
\longrightarrow1,
\tag{5.3}
\]

so

\[
|G_{\mathrm{eff}}^+|=|G_{\mathrm{eff}}|\,|K_{\mathrm{col}}|.
\tag{5.4}
\]

All \(j\)-fold products lie in the coset
\(\alpha_{\Delta^+}(x_0)^jG_{\mathrm{eff}}^+\). If the old support fiber is nonempty, all accessible colored lifts lie in one coset of \(K_{\mathrm{col}}\). Consequently,

\[
\boxed{
M_{t=1,d=\sigma}(s)-\varepsilon_A
\le |K_{\mathrm{col}}|.
}
\tag{5.5}
\]

This is the exact effective-color correction. The old support denominator is
\(|G_{\mathrm{eff}}|\); a fixed-color fiber lives on the larger group
\(G_{\mathrm{eff}}^+\); and the number of accessible colors is governed by the kernel
\(K_{\mathrm{col}}\), not automatically by all of \(F\).

Put

\[
h_x=\alpha_{\Delta^+}(x)\alpha_{\Delta^+}(x_0)^{-1}.
\]

For \(g\in\pi^{-1}(b_\Delta)\), let

\[
t_g=g\alpha_{\Delta^+}(x_0)^{-j}.
\]

If \(t_g\notin G_{\mathrm{eff}}^+\), then \(N^+_{\Delta^+,j}(g)=0\). Otherwise finite Fourier inversion gives

\[
\boxed{
N^+_{\Delta^+,j}(g)
=
\frac1{|G_{\mathrm{eff}}^+|}
\sum_{\psi\in\widehat{G_{\mathrm{eff}}^+}}
\psi(t_g)^{-1}
\,e_j\bigl(\psi(h_x):x\in D^\circ\bigr),
}
\tag{5.6}
\]

where \(e_j\) is the \(j\)-th elementary symmetric polynomial. Summing (5.6) over the lift fiber recovers the old support-fiber formula over \(G_{\mathrm{eff}}\); replacing the sum by the occupied-target indicator gives the distinct-slope formula (4.3).

---

## 6. Proof

### 6.1 Support equivalence

Since

\[
(I_s)_j=A S_{j-\sigma}\oplus FB,
\]

every degree-\(j\) locator has a unique decomposition

\[
P_T=A U_T+\gamma_TB.
\]

The full-coordinate gcd criterion is

\[
\gcd(U_T,\gamma_T)=1.
\]

For \(j>\sigma\), this is equivalent to \(\gamma_T\ne0\). When \(j=\sigma\), the only \(\gamma_T=0\) possibility is \(P_T\sim A\), which is handled separately.

Restricting to \(\Delta=V(A)\) gives

\[
P_T|_\Delta=\gamma_TB|_\Delta.
\]

After division by \(L_*^j\) and quotienting by \(F^\times\), this is the product equation in \(G_\Delta\). Conversely, equality in \(G_\Delta\) means that

\[
P_T|_\Delta=\gamma B|_\Delta
\]

for a unique \(\gamma\in F^\times\). Scheme-theoretic vanishing on \(V(A)\) gives

\[
A\mid P_T-\gamma B,
\]

hence the required decomposition and full-coordinate representation. This argument is unchanged for nonreduced \(\Delta\) and nonsplit closed points.

If \(e<j\), then \((I_s)_e=A S_{e-\sigma}\). A full-coordinate locator in this space must have constant cofactor, so \(e=\sigma\) and the locator is \(A\). This proves the lower-weight statement.

### 6.2 Color formula

Let

\[
P_T(X)=\sum_{i=0}^jp_iX^i,
\qquad p_j=1.
\]

Because \(P_T(x)=0\) for every \(x\in T\),

\[
0
=
\sum_{x\in T}c_xx^{\sigma-1}P_T(x)
=
\sum_{i=0}^{j-1}p_is_{i+\sigma-1}
+
\lambda_Tc.
\]

Therefore

\[
\chi(T,c)
=-\lambda_Tc
=
\sum_{i=0}^{j-1}p_is_{i+\sigma-1}.
\tag{6.1}
\]

Write

\[
U_T(X)=\sum_{h=0}^{j-\sigma}u_hX^h,
\qquad u_T=u_{j-\sigma}.
\]

Since \(A\in I_s\),

\[
\sum_{i=0}^{\sigma}a_is_{i+m}=0
\qquad(0\le m\le j-2).
\tag{6.2}
\]

Substituting \(AU_T\) into (6.1), every term with
\(h<j-\sigma\) vanishes by (6.2). The last term contributes exactly
\(u_T\eta_A\). The \(B\)-term contributes \(\gamma_T\eta_B\). Thus

\[
\chi(T,c_T)=\eta_Au_T+\eta_B\gamma_T.
\]

The leading coefficient of \(P_T\) is one, so

\[
a_\sigma u_T+b_j\gamma_T=1.
\]

This proves (3.5).

### 6.3 Invertibility of the color matrix

The first row of \(\mathcal M_s\) is nonzero, because
\(a_\sigma=b_j=0\) would make both homogeneous generators divisible by the linear form vanishing at \(\beta\), contradicting \(\gcd(A,B)=1\).

Suppose \(\det\mathcal M_s=0\). Then for some \(r\in F\),

\[
(\eta_A,\eta_B)=r(a_\sigma,b_j).
\]

Append the moment \(s_R=-r\) to \(s_0,\ldots,s_{R-1}\). The old apolar equations already put \(A\) and \(B\) in the annihilator in all previous shifts. The one new equation for \(A\) is

\[
\eta_A+a_\sigma s_R=0,
\]

and the one new equation for \(B\) is

\[
\eta_B+b_js_R=0.
\]

Hence the degree-\(R\) apolar ideal of the augmented functional contains \((A,B)\). But

\[
\deg A+\deg B=\sigma+j=R+1,
\]

so the complete intersection \(S/(A,B)\) has socle degree \(R-1\), and therefore

\[
(A,B)_R=S_R.
\]

The augmented functional would vanish on all of \(S_R\), contradicting the nonzero restriction \(s\). Thus \(\det\mathcal M_s\ne0\).

### 6.4 Thickened-modulus equivalence

Because \(u_T\) is the value of the homogeneous cofactor \(U_T\) at
\(\beta=[0:1]\),

\[
U_T-u_TX_1^{j-\sigma}
\]

is divisible by \(E_\beta=X_0\). Therefore

\[
P_T
\equiv
\gamma_TB+u_TAX_1^{j-\sigma}
\pmod{AE_\beta}.
\tag{6.3}
\]

For \((u_\chi,\gamma_\chi)\) solving (3.12), the form \(Q_\chi\) has value one at \(\beta\), because its top coefficient is

\[
a_\sigma u_\chi+b_j\gamma_\chi=1.
\]

If (3.14) holds in \(G_{\Delta^+}\), then for some scalar \(c\in F^\times\),

\[
P_T|_{\Delta^+}=cQ_\chi|_{\Delta^+}.
\]

Evaluating at the added point \(\beta\) gives \(1=c\), so (6.3) holds with the exact pair \((u_\chi,\gamma_\chi)\). Equation (3.5) then gives color \(\chi\). The converse is immediate from (6.3).

The restriction map (3.10) is surjective. If \(\beta\notin\operatorname{Supp}\Delta\), Chinese remaindering gives

\[
H^0(\Delta^+,\mathcal O_{\Delta^+})
\simeq
H^0(\Delta,\mathcal O_\Delta)\times F,
\]

and the kernel after quotienting by diagonal scalars is \(F^\times\). If \(\beta\) already has multiplicity \(m\) in \(\Delta\), the new local kernel is

\[
1+F t^m\pmod{t^{m+1}},
\]

which is canonically additive and has size \(q\). This proves (3.11).

The map \(\chi\mapsto b_\chi^+\) is injective by (3.5) and (6.3). When
\(\beta\notin\operatorname{Supp}\Delta\), exactly one \(\chi\) has
\(\gamma_\chi=0\), leaving \(q-1\) values; when
\(\beta\in\operatorname{Supp}\Delta\), \(b_j\gamma_\chi=1\), so all \(q\) values remain. These cardinalities equal \(|\ker\pi|\), proving the bijection onto \(\pi^{-1}(b_\Delta)\).

### 6.5 Gauge and generator invariance

Let

\[
B'=rB+AC,
\qquad
r\in F^\times,
\qquad
\deg C=j-\sigma.
\]

Put \(c_\infty=[X^{j-\sigma}]C\). The same locator has coordinates

\[
\gamma_T'=\gamma_T/r,
\qquad
u_T'=u_T-(\gamma_T/r)c_\infty.
\]

The new top/color column of the matrix is

\[
\binom{b_j'}{\eta_{B'}}
=
r\binom{b_j}{\eta_B}
+c_\infty\binom{a_\sigma}{\eta_A}.
\]

Consequently

\[
\mathcal M_s'
\binom{u_T'}{\gamma_T'}
=
\mathcal M_s
\binom{u_T}{\gamma_T}
=
\binom{1}{\chi(T,c_T)}.
\]

Moreover,

\[
\gamma_T'B'+u_T'AX_1^{j-\sigma}
\equiv
\gamma_TB+u_TAX_1^{j-\sigma}
\pmod{AE_\beta},
\]

because \(C-c_\infty X_1^{j-\sigma}\) is divisible by \(E_\beta\). Thus the colored lift class, all fiber counts, and the numerator are invariant under every admissible shear and scaling preserving the chosen generator line \(FA\). Changing \(L_*\) merely changes trivializations, and changing the augmented row by \(\lambda\mapsto a\lambda+\varphi H\) affinely relabels colors without changing collisions.

At the equal-degree edge \(j=\sigma\), the same proof applies with \(C\) scalar. A full \(\mathrm{GL}_2\)-change that also changes the line \(FA\) changes the modulus \(\Delta\); the theorem then applies to the new ordered generator pair and gives the same intrinsic slope set.

### 6.6 Noncontainment

In the shifted \(t=1\) presentation, write the one-dimensional extension as

\[
E\mathcal P_k\oplus FB_0,
\qquad
\deg E=1,
\qquad
\gcd(E,B_0)=1.
\]

If the direction were contained in a support with agreement set of size
\(a=k+\sigma\), some \(G_0\in\mathcal P_k\) would make

\[
EG_0-B_0
\]

vanish at all \(a\) agreement points. But

\[
\deg(EG_0-B_0)<k+1\le k+\sigma=a,
\]

so the polynomial would be zero, contradicting \(\gcd(E,B_0)=1\). Thus every slope counted by (4.3) is automatically noncontained/transverse.

---

## 7. Counterpacket to the unthickened scalar-color claim

Take

\[
F=\mathbf F_{11},
\quad
D=\{0,1,2,3,4,5,6\},
\quad
k=2,
\quad
\sigma=2,
\quad
j=3,
\quad
R=4,
\quad
\beta=\infty.
\]

Use parity-check columns \((1,x,x^2,x^3)^{\mathsf T}\), color row
\(\lambda_x=x^4\), and syndrome

\[
s=(9,0,0,2).
\]

Its apolar ideal is

\[
I_s=(A,B),
\qquad
A=X_0X_1
\quad(A(X)=X),
\qquad
B=X_0^3+X_1^3
\quad(B(X)=1+X^3).
\]

The two supports

\[
T_1=\{1,2,5\},
\qquad
T_2=\{4,5,6\}
\]

have full-coordinate coefficient vectors

\[
c_1=(6,7,7),
\qquad
c_2=(3,4,2),
\]

and both satisfy \(H_{T_i}c_i=s\). Their locators are

\[
P_{T_1}=1+6X+3X^2+X^3=B+A(6+3X),
\]

\[
P_{T_2}=1+8X+7X^2+X^3=B+A(8+7X).
\]

Thus both have the same old scalar lift

\[
\gamma_{T_1}=\gamma_{T_2}=1.
\]

However,

\[
\lambda_{T_1}c_1=5,
\qquad
\lambda_{T_2}c_2=8,
\]

so their reduced colors are

\[
\chi(T_1,c_1)=6,
\qquad
\chi(T_2,c_2)=3.
\]

Here \(\beta=\infty\in\operatorname{Supp}\Delta\). The missing thickened coordinates are

\[
u_{T_1}=3,
\qquad
u_{T_2}=7.
\]

Indeed \(\eta_A=2\), \(\eta_B=0\), and (3.9) gives

\[
\chi=2u.
\]

This explicitly kills any theorem asserting that the old scalar
\(\gamma_T\), or the unthickened support class alone, determines the MCA color.

---

## 8. Parameter ledger and finite relevance

| Quantity | Exact value / object |
|---|---|
| shifted stratum | \(t=1\) |
| extension code | \(\operatorname{RS}[F,D,k+1]\) |
| redundancy | \(R=n-k-1=j+\sigma-1\) |
| boundary error weight | \(j=n-k-\sigma\) |
| minimal apolar degrees | \((\sigma,j)\) |
| support modulus | \(\Delta=V(A)\), degree \(\sigma\) |
| colored modulus | \(\Delta^+=\Delta+[\beta]\), degree \(\sigma+1\) |
| support group | \(G_\Delta\) |
| colored lift group | \(G_{\Delta^+}\) |
| full support target | \(b_\Delta\in G_\Delta\) |
| color targets | full fiber \(\pi^{-1}(b_\Delta)\) |
| raw support count | sum of \(N^+(g)\) over the lift fiber |
| distinct-slope count | number of occupied \(g\)'s in the lift fiber |
| external kernel size | \(q-1\) if \(\beta\notin\Delta\), \(q\) if \(\beta\in\Delta\) |
| effective color capacity | \(|K_{\mathrm{col}}|\) |
| lower-weight term | one slope iff \(A\) is squarefree and \(D\)-split |
| noncontainment loss | zero |

For a finite prize certificate, one must use (4.3). Replacing it by the support multiplicity (4.2) is safe only as an upper bound and can be arbitrarily wasteful. Replacing \(|G_{\mathrm{eff}}^+|\) by the ambient group order, or replacing \(|K_{\mathrm{col}}|\) by \(q\), can also lose the exact finite margin.

---

## 9. Bankable versus conditional

### Bankable

1. The uncolored generalized-Jacobian support equivalence at
   \(\deg A=\sigma,\deg B=j\).
2. The explicit color matrix (3.5) and its nonzero determinant.
3. The dichotomy between multiplicative color when
   \(\beta\notin\Delta\) and additive jet color when \(\beta\in\Delta\).
4. The thickened-modulus equivalence (3.14).
5. The exact distinct-slope numerator (4.3).
6. The exact effective subgroup and Fourier formulas (5.3)--(5.6).
7. Automatic noncontainment for the shifted \(t=1\) slice.
8. Invariance under auxiliary-form change, augmented-row affine gauge, and admissible generator shear
   \(B\mapsto rB+AC\), \(r\ne0\). Under this shear the coordinate pair changes contragrediently, while \((1,\chi)\), the class \(b_\chi^+\), and all fiber counts remain unchanged.

### Still conditional / open

No finite local-limit estimate for the occupied lift set has been proved here. The theorem identifies the correct finite object but does not bound

\[
\#\{g\in\pi^{-1}(b_\Delta):N^+_{\Delta^+,j}(g)>0\}
\]

at official parameters after quotient and periodic-character extraction.

---

## 10. Failure point and next exact lemma

The old backup route failed only at its color object: \(G_\Delta\) forgets one external coordinate. The one-point thickening repairs that defect exactly.

The next wall should be renamed

```text
W-JR-T1-GJ-PLUS-QUOTIENT-CONDITIONED-COLOR-OCCUPANCY
```

and should prove a finite, quotient-conditioned bound for the number of occupied points in

\[
\pi^{-1}(b_\Delta)\cap
\alpha_{\Delta^+}(x_0)^jG_{\mathrm{eff}}^+,
\]

with all coherent characters charged jointly through quotients of
\(G_{\mathrm{eff}}^+\), and with the remaining primitive contribution explicit. The corresponding checker should enumerate \(\Delta^+\)-lift fibers, not merely the old scalar \(\gamma_T\).

## Do I see a route to a full solve?

**Yes, conditionally.** This wall is now exact and closed. The next theorem is a finite local-limit/inverse theorem on the thickened effective generalized Jacobian, followed by the already identified \(d>\sigma\) rational-pair branch and the all-line assembly. The immediate exact construction is a corrected `mca_t1_gj_color_scan` whose state space is \(G_{\Delta^+}\) and whose MCA numerator is (4.3).
