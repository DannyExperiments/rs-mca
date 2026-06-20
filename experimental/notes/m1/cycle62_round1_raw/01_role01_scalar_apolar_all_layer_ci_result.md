BANKABLE_LEMMA

# L-LIST-APOLAR-ALL-LAYER-CI

**Executive verdict.** The all-layer scalar apolar complete-intersection
foundation is correct. In fact, the proposed full-coordinate criterion admits
the stronger exact formula

\[
\gcd(U_E,V_E)\ \sim\ \prod_{x\in E:\,c_x=0}\ell_x,
\]

where \(s=\sum_{x\in E}c_xh_x\) is the unique syndrome representation and
\(\ell_x\) is the projective locator factor at \(x\). Thus the coefficient-pair
gcd records exactly, factor by factor, the padded/non-full coordinates.

**Confidence:** high.

## 1. Formal theorem

Let \(F\) be any field. Let

\[
C=\operatorname{GRS}[F,L,k],\qquad n=|L|,\qquad r=n-k\ge1,
\]

where \(L\subset \mathbf P^1(F)\) consists of distinct points. Ordinary affine
RS is the special case \(L\subset\mathbf A^1(F)\). Fix

\[
1\le \sigma\le r,\qquad j=r-\sigma,\qquad N=r-1,
\]

so \(0\le j\le N\). After arbitrary nonzero GRS column scaling, write the
parity-check columns as

\[
h_x=w_x\operatorname{ev}_x\in S_N^*,\qquad w_x\in F^\times,
\qquad S=F[X_0,X_1].
\]

Identify a syndrome \(s\) with the corresponding functional
\(\Lambda_s\in S_N^*\). Define the homogeneous apolar ideal by

\[
(I_s)_e=
\begin{cases}
\{P\in S_e:\Lambda_s(PQ)=0\text{ for every }Q\in S_{N-e}\},&0\le e\le N,\\
S_e,&e>N,
\end{cases}
\]

and put \(S_t=0\) for \(t<0\).

For \(x\in\mathbf P^1(F)\), choose a nonzero linear form \(\ell_x\) vanishing
at \(x\). For \(E\subseteq L\), put

\[
p_E=\prod_{x\in E}\ell_x\in S_{|E|}.
\]

Then the following hold.

### Theorem A: nonzero syndrome

Assume \(s\ne0\).

1. **Binary complete intersection.** There are coprime homogeneous forms
   \(A,B\), with
   \[
   I_s=(A,B),\qquad d:=\deg A\le b:=\deg B,
   \qquad d+b=r+1.
   \]

2. **All-layer locator criterion.** For every \(E\subseteq L\) of degree
   \(e=|E|\le j\),
   \[
   s\in\operatorname{span}\{h_x:x\in E\}
   \quad\Longleftrightarrow\quad
   p_E\in(I_s)_e.
   \]
   Since \(e\le N\), the syndrome representation on \(E\), when it exists,
   is unique.

3. **Unique coefficient pair.** For every \(e\le j\),
   \[
   (I_s)_e=A S_{e-d}\oplus B S_{e-b}.
   \]
   Hence every listed locator has a unique expression
   \[
   p_E=A U_E+B V_E,
   \qquad U_E\in S_{e-d},\quad V_E\in S_{e-b}.
   \]

4. **Exact non-full-coordinate divisor.** Write the unique syndrome
   representation as
   \[
   s=\sum_{x\in E}c_xh_x,
   \]
   and let \(Z_E=\{x\in E:c_x=0\}\). Then
   \[
   \boxed{\gcd(U_E,V_E)\sim p_{Z_E}.}
   \]
   Consequently the representation is full-coordinate exactly when
   \[
   \boxed{\gcd(U_E,V_E)=1.}
   \]

5. **Low-generator collapse.** If a listed locator is full-coordinate and
   \(e<b\), then
   \[
   \boxed{e=d\quad\text{and}\quad p_E\sim A.}
   \]
   Thus there is at most one full-coordinate locator below degree \(b\), and
   it exists only when \(A\) itself is squarefree and fully \(L\)-split.

6. **Layer-gap consequence.** If the full-support fiber up to degree \(j\)
   has at least two elements, then
   \[
   b\le j,
   \qquad
   d=r+1-b\ge r+1-j=\sigma+1.
   \]

### Theorem B: zero syndrome

If \(s=0\), then \(I_s=S\), so no proper complete-intersection assertion is
made. For every \(E\) with \(|E|\le j\), the unique representation of zero on
the independent columns \(\{h_x:x\in E\}\) is the zero vector. It is
full-coordinate only for \(E=\varnothing\). Hence the scalar list fiber has
exactly one member, the received codeword itself.

### Exact list-fiber corollary

For any received word with syndrome `s`, the map from nearby codewords to
their full error supports is bijective because every set of at most `j<r+1`
parity-check columns is independent. Consequently

\[
N_s(\sigma)=
\#\left\{
E\subseteq L:\ |E|\le j,\ p_E\in I_s,\ \gcd(U_E,V_E)=1
\right\},
\]

with `N_0(\sigma)=1`. This is the exact all-layer scalar list numerator; no
boundary padding or raw feasible-support multiplicity is present.

## 2. Proof

### 2.1 The apolar spaces form an ideal

Let \(P\in(I_s)_e\) and \(R\in S_f\). If \(e+f>N\), then \(PR\in(I_s)_{e+f}\)
by definition. If \(e+f\le N\), then for every \(Q\in S_{N-e-f}\),
\(RQ\in S_{N-e}\), so

\[
\Lambda_s(PRQ)=0.
\]

Thus \(PR\in(I_s)_{e+f}\). Therefore \(I_s\) is a homogeneous ideal.

### 2.2 Gorenstein quotient and complete-intersection structure

Put \(R_s=S/I_s\). For \(0\le e\le N\), multiplication followed by
\(\Lambda_s\) gives a pairing

\[
(R_s)_e\times(R_s)_{N-e}\longrightarrow F.
\]

It is perfect: if the class of \(P\in S_e\) is nonzero, then
\(P\notin(I_s)_e\), so by definition there is \(Q\in S_{N-e}\) with
\(\Lambda_s(PQ)\ne0\); symmetry gives nondegeneracy in the other factor.
Moreover,

\[
(R_s)_N=S_N/\ker\Lambda_s
\]

is one-dimensional, and \((R_s)_e=0\) for \(e>N\). If a nonzero homogeneous
class in degree \(e<N\) lay in the socle, multiplication by both \(X_0\) and
\(X_1\) would kill it, hence multiplication by every form in \(S_{N-e}\)
would kill it, contradicting the perfect pairing. Therefore

\[
\operatorname{Soc}(R_s)=(R_s)_N\cong F.
\]

So \(R_s\) is a standard graded Artinian Gorenstein algebra with socle degree
\(N\).

Because \(S=F[X_0,X_1]\) is a two-dimensional regular ring, a height-two
Artinian Gorenstein ideal is a complete intersection. Concretely, in the
minimal graded free resolution of \(R_s\), the final Betti number equals the
Cohen--Macaulay type, which is one. The rank identity over the fraction field
then forces two minimal generators of \(I_s\). A height-two ideal generated by
two elements is a regular sequence. Hence

\[
I_s=(A,B)
\]

with \(\gcd(A,B)=1\). If their degrees are \(d\le b\), the Koszul resolution
shows that the socle degree is \(d+b-2\). Since it is \(N=r-1\),

\[
d+b=N+2=r+1.
\]

This argument uses no differentiation, divided powers, separability, or
characteristic restriction.

### 2.3 The all-layer locator criterion

Fix \(E\subseteq L\) with \(|E|=e\le j\le N\). A degree-\(N\) binary form
vanishes at every point of \(E\) exactly when each pairwise nonassociate
linear form \(\ell_x\), \(x\in E\), divides it. Therefore the vanishing space
is

\[
\{F\in S_N:F|_E=0\}=p_ES_{N-e}.
\]

Every evaluation functional \(\operatorname{ev}_x\), \(x\in E\), annihilates
this space. These \(e\) evaluations are linearly independent on \(S_N\): for
a fixed \(x\in E\), the form

\[
\left(\prod_{y\in E\setminus\{x\}}\ell_y\right)m_x^{N-e+1},
\]

where \(m_x(x)\ne0\), vanishes on \(E\setminus\{x\}\) but not at \(x\).
Since \(p_ES_{N-e}\) has dimension \(N-e+1\), its annihilator has dimension
\(e\). Hence

\[
(p_ES_{N-e})^\perp
=
\operatorname{span}\{\operatorname{ev}_x:x\in E\}
=
\operatorname{span}\{h_x:x\in E\},
\]

where the last equality uses \(w_x\ne0\). Thus

\[
p_E\in(I_s)_e
\iff
\Lambda_s(p_EQ)=0\text{ for every }Q\in S_{N-e}
\iff
s\in\operatorname{span}\{h_x:x\in E\}.
\]

The same independence proves uniqueness of the coefficient vector on \(E\).

### 2.4 Unique decomposition below \(d+b\)

Surjectivity of

\[
S_{e-d}\oplus S_{e-b}\longrightarrow(I_s)_e,
\qquad (U,V)\longmapsto AU+BV,
\]

follows from \(I_s=(A,B)\). If \(AU+BV=0\), coprimality in the UFD
\(F[X_0,X_1]\) implies

\[
U=BW,
\qquad
V=-AW
\]

for some \(W\in S_{e-d-b}\). For \(e<d+b=r+1\), this space is zero. Since
\(e\le j\le r-1\), the map is injective throughout every relevant error
layer. This proves the direct sum and unique expression.

### 2.5 Exact gcd formula

Let

\[
s=\sum_{x\in E}c_xh_x,
\qquad
Z_E=\{x:c_x=0\},
\qquad
G=p_{Z_E}.
\]

Deleting the zero coordinates gives

\[
s\in\operatorname{span}\{h_x:x\in E\setminus Z_E\}.
\]

By the locator criterion,

\[
p_E/G=p_{E\setminus Z_E}\in I_s.
\]

Write

\[
p_E/G=AU_0+BV_0.
\]

Multiplying by \(G\) and using uniqueness of the degree-\(e\) decomposition
gives

\[
U_E=GU_0,
\qquad
V_E=GV_0.
\]

Thus \(G\mid\gcd(U_E,V_E)\).

Conversely, let \(D\) be a nonconstant common divisor of \(U_E,V_E\). Then
\(D\mid p_E=AU_E+BV_E\). Since \(p_E\) is squarefree and split into the
pairwise distinct factors \(\ell_x\), every irreducible factor of \(D\) is
some \(\ell_x\) with \(x\in E\). If \(\ell_x\mid D\), then

\[
p_E/\ell_x=A(U_E/\ell_x)+B(V_E/\ell_x)\in I_s.
\]

The locator criterion yields

\[
s\in\operatorname{span}\{h_y:y\in E\setminus\{x\}\}.
\]

By uniqueness of the representation on \(E\), this is equivalent to
\(c_x=0\). Therefore every factor of \(D\) lies in \(p_{Z_E}\), proving

\[
\gcd(U_E,V_E)\sim p_{Z_E}.
\]

The full-coordinate equivalence follows immediately.

### 2.6 Low-generator collapse

If \(e<b\), then \(S_{e-b}=0\), so \(V_E=0\) and

\[
p_E=AU_E.
\]

The exact gcd formula gives

\[
\gcd(U_E,0)\sim U_E.
\]

Full-coordinate therefore forces \(U_E\in F^\times\). Since
\(U_E\in S_{e-d}\), this is possible exactly when \(e=d\), and then
\(p_E\sim A\).

If two distinct full-coordinate locators occur with degrees at most \(j\), one
cannot have \(b>j\), because then both would lie below \(b\) and both would be
proportional to \(A\). Hence \(b\le j\), and

\[
d=r+1-b\ge r+1-j=\sigma+1.
\]

## 3. First nontrivial stratum

The first possible generator degrees for a fiber of size at least two are

\[
\boxed{d=\sigma+1,\qquad b=j=r-\sigma.}
\]

This stratum can occur only when \(\sigma+1\le j\), equivalently
\(r\ge2\sigma+1\).

### Unequal-degree case \(d<b=j\)

For \(e<j\), the only possible full-coordinate locator is \(A\) in degree
\(e=d\), and it occurs only if \(A\) is squarefree and fully \(L\)-split. At
the endpoint \(e=j\), every locator has the unique form

\[
p_E=AU_E+\lambda_E B,
\qquad
U_E\in S_{j-d},\quad \lambda_E\in F.
\]

Since \(j-d>0\),

\[
\gcd(U_E,\lambda_E)=1
\quad\Longleftrightarrow\quad
\lambda_E\ne0.
\]

Thus every non-low full-coordinate locator lies exactly on the boundary layer
\(e=j\) and has nonzero \(B\)-coefficient. This is the precise input needed by
the generalized-Jacobian route.

### Equal-degree edge \(d=b=j=\sigma+1\)

There are no listed locators below degree \(j\). In degree \(j\),

\[
p_E=\alpha_EA+\beta_EB,
\qquad (\alpha_E,\beta_E)\in F^2\setminus\{(0,0)\}.
\]

Both coefficients are constants, so their gcd is a unit. Consequently every
squarefree fully \(L\)-split nonzero member of the pencil
\(\mathbf P\langle A,B\rangle\) is automatically full-coordinate.

## 4. Generator changes

### Unequal degrees

When \(d<b\), the degree-\(d\) generator is unique up to scalar. Holding
\(A\) fixed, every admissible replacement of the second generator is

\[
B'=cB+AC,
\qquad c\in F^\times,
\quad C\in S_{b-d}.
\]

The coefficient pair changes by

\[
(U,V)\longmapsto
\left(U-\frac{C}{c}V,\frac1cV\right).
\]

This transformation and its inverse preserve the ideal \((U,V)\), hence
preserve the gcd up to a unit and preserve full-coordinate status. Allowing a
rescaling of \(A\) changes nothing.

### Equal degrees

When \(d=b\), every minimal generator pair is obtained by a matrix in
\(\operatorname{GL}_2(F)\). The coefficient column transforms by the inverse
matrix. Therefore \((U,V)\) and its gcd ideal are unchanged.

## 5. Edge-case ledger

- **Zero syndrome:** separated in Theorem B; exactly one full support, the empty
  support.
- **\(d=b\):** handled by the equal-degree pencil and \(\operatorname{GL}_2\)
  invariance.
- **Infinity:** for \(x=\infty=[0:1]\), take \(\ell_\infty=X_0\). All
  divisibility, annihilator, gcd, and deletion arguments are projective and
  unchanged.
- **Homogenization:** affine forms of degree at most \(m\) are elements of
  \(S_m\) after homogenization. A common factor \(X_0\) is exactly the
  projective factor at infinity, so degree deficits are not silently lost.
- **Non-split generators:** neither \(A\) nor \(B\) is assumed split. A
  low-layer locator exists only if the conclusion \(p_E\sim A\) forces \(A\)
  itself to be squarefree and \(L\)-split.
- **Small characteristic:** the proof uses multiplication pairings, linear
  algebra, UFD divisibility, and the codimension-two Gorenstein theorem. It
  uses no ordinary derivatives or factorial denominators.
- **Column scaling:** replacing \(\operatorname{ev}_x\) by
  \(w_x\operatorname{ev}_x\), \(w_x\ne0\), preserves spans and preserves the
  zero/nonzero pattern of representation coefficients.
- **Repeated roots:** actual RS error locators are reduced because evaluation
  positions are distinct. A repeated-root form describes a nonreduced divisor
  and its annihilator is an osculating/principal-parts space, not the span of
  ordinary RS columns. Such forms are therefore correctly excluded by the
  squarefree condition \(p_E\mid\prod_{x\in L}\ell_x\). If \(A\) has a
  repeated root, it simply contributes no low-layer listed locator.
- **Non-full representations:** exactly classified by
  \(\gcd(U_E,V_E)\sim p_{Z_E}\).
- **Endpoint \(e=j\):** safe because \(j\le r-1<d+b=r+1\), so both the locator
  annihilator and unique CI decomposition remain valid.

## 6. Finite audit

The deterministic verifier

```text
experimental/scripts/verify_scalar_apolar_ci_all_layers.py
```

exhaustively checked four projective prime-field cases, including infinity,
characteristic two, equal generator degrees, zero syndrome, every nonzero
functional, every reduced locator through degree \(N\), admissible shears, and
the reserve implication. The audit covered:

```text
660 nonzero functionals
26,555 locator/functionality comparisons
2,935 generator-change checks
```

All checks passed. The machine-readable report is

```text
experimental/scripts/scalar_apolar_ci_all_layers_audit.json
```

This computation is corroboration only; the proof above is field-uniform.

## 7. What is bankable and what remains open

**Bankable:** the complete-intersection structure, all-layer locator criterion,
unique decomposition, exact gcd/zero-coordinate formula, low-generator
collapse, generator-gauge invariance, and the complete first-stratum layer
classification.

**Not proved here:** the generalized-Jacobian subset-product equivalence, its
effective subgroup/Fourier count, and the quotient-conditioned local limit.
No failure remains inside this foundation.

## 8. Next exact lemma and route assessment

There is a coherent route onward. The next exact lemma is

```text
L-LIST-MINIMAL-CI-GJ-FIBER
```

in the unequal minimal stratum

\[
\deg A=\sigma+1,
\qquad
\deg B=j>\sigma+1.
\]

The result above reduces the entire all-layer fiber to the optional locator
\(A\) plus boundary forms

\[
p_T=AU_T+\lambda_TB,
\qquad \lambda_T\ne0.
\]

The next construction must prove that these boundary locators are exactly the
\(j\)-subsets disjoint from \(V(A)\) whose product class in
\(H^0(V(A),\mathcal O)^*/F^*\) equals the target class of \(B\), with the
count taken in the effective image subgroup and shown invariant under
\(B\mapsto cB+AC\).

That lemma would not finish the prize, but it is now the unique next algebraic
wall on the primary route; after it comes the finite quotient-conditioned
subset-product local limit.
