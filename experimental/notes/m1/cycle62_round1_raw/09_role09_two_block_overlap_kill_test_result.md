ROUTE_CUT

# W-MCA-TWO-BLOCK-COMMON-UNION-RIGIDITY

## 1. Executive verdict and confidence

The right-factor/refinement form of two-block overlap rigidity is false.
Even with fixed coprime map degrees, no nonconstant common right factor, and
only the discrete common refinement, the block-incidence graph can have an
arbitrarily large number of connected components.  It then has exponentially
many common unions.  A fixed-size layer of those common unions can be realized
as pairwise distinct, exact, transverse MCA agreement supports on one affine
RS syndrome line contained in no proper syndrome envelope.

The missing invariant is the **common left composite / common component
color**

\[
W=A\circ R=B\circ S,
\]

not a common right factor.  In the counterfamily below,

\[
R=X^M,\qquad S=X^N,\qquad
W=A\circ R=B\circ S=X^{MN},
\quad A(T)=T^N,\ B(T)=T^M.
\]

Thus the proposed registry must be closed under common coarsenings/common
colors, or the support-overlap route must be replaced by a direct
support-plus-color theorem.

**Confidence: high.**  The construction is exact and parameterized; a concrete
finite instance is independently checked by the accompanying script.

## 2. Formal counterpacket theorem

### Theorem (coprime-monomial common-left-composite counterpacket)

Fix coprime integers

\[
M,N\ge 2,
\]

integers

\[
c\ge 3,\qquad 2\le h\le c-1,
\]

and a finite field \(K\) of characteristic prime to \(cMN\) containing
\(\mu_{cMN}\).  Let \(F/K\) be a finite extension containing an element
\(\theta\) with

\[
[K(\theta):K]=D>h.
\]

Put

\[
L=\mu_{cMN}\subset K^\times\subset F^\times,
\]

and define separable maps

\[
R(X)=X^M,\qquad S(X)=X^N,\qquad W(X)=X^{MN}.
\]

Then:

1. \(R\) and \(S\) have no nonconstant common right factor over
   \(\overline F\).  Their induced partitions on \(L\) have no nontrivial
   common refinement.
2. The bipartite block-incidence graph of the full \(R\)-fibers and full
   \(S\)-fibers on \(L\) is the disjoint union of exactly \(c\) copies of
   \(K_{N,M}\).
3. A subset of \(L\) is simultaneously a union of full \(R\)-fibers and full
   \(S\)-fibers iff it is a union of the \(c\) fibers of \(W|_L\).  Hence the
   total number of common unions is \(2^c\), and the number of nontrivial ones
   is \(2^c-2\).
4. Set

   \[
   n_0=cMN,\qquad \sigma=MN,\qquad k=(h-1)MN,
   \]

   so

   \[
   r=(c-h+1)MN,\qquad j=(c-h)MN,\qquad k+\sigma=hMN.
   \]

   In the code \(\mathcal C=\operatorname{RS}[F,L,k]\), there is one affine
   syndrome line carrying exactly

   \[
   \binom ch
   \]

   distinct slopes whose exact agreement supports are the \(h\)-component
   common unions.
5. Every one of these witnesses is transverse, the syndrome line is contained
   in no proper syndrome envelope, the full packet has no common agreement
   core, and it is not contained in one tangent affine polynomial line.
6. For the repository weight

   \[
   W_\sigma(\mathscr F)
   =\min\left\{|\mathscr F|,
   \left\lfloor\frac r\sigma\right\rfloor\kappa_k(\mathscr F)\right\},
   \]

   the fixed-size common-union family \(\mathscr F_h\) satisfies the exact
   identity

   \[
   W_\sigma(\mathscr F_h)=\binom ch.
   \]

In particular, for fixed \(M,N\), the component count and common-union weight
are unbounded as \(c\to\infty\).  No degree-only common-right-factor overlap
bound is possible.

## 3. Proof

### 3.1 Existence of the fields

Choose any prime \(p\nmid cMN\).  For some \(e\),

\[
cMN\mid p^e-1,
\]

so \(K=\mathbf F_{p^e}\) contains \(\mu_{cMN}\).  For any \(D>h\), take
\(F=\mathbf F_{|K|^D}\) and choose an element \(\theta\) of full degree \(D\)
over \(K\).

### 3.2 No common right factor and no nontrivial common refinement

Since \(\gcd(M,N)=1\), choose integers \(a,b\) with

\[
aM+bN=1.
\]

In the rational function field,

\[
X=(X^M)^a(X^N)^b,
\]

where negative powers are allowed.  Therefore

\[
\overline F(X^M,X^N)=\overline F(X).
\]

If \(R=R_0\circ T\) and \(S=S_0\circ T\) for a rational map \(T\) of degree
larger than one, then

\[
\overline F(R,S)\subseteq \overline F(T)\subsetneq \overline F(X),
\]

contradicting the displayed equality.  Thus there is no nonconstant common
right factor.

At the support level, if \(x,y\in L\) lie in both the same \(R\)-fiber and the
same \(S\)-fiber, then

\[
(x/y)^M=(x/y)^N=1.
\]

Coprimality gives \(x=y\).  Hence every intersection of an \(R\)-block and an
\(S\)-block has size at most one, so the common refinement is the discrete
partition.

### 3.3 Exact block-incidence graph

Make a bipartite graph whose left vertices are the full \(R\)-fibers on \(L\),
whose right vertices are the full \(S\)-fibers on \(L\), and whose edge indexed
by \(x\in L\) joins the two fibers containing \(x\).

Moving inside an \(R\)-fiber multiplies \(x\) by an element of \(\mu_M\), and
moving inside an \(S\)-fiber multiplies it by an element of \(\mu_N\).  Since

\[
\langle\mu_M,\mu_N\rangle=\mu_{MN},
\]

two edges \(x,y\) lie in the same connected component iff

\[
x/y\in\mu_{MN},
\]

equivalently iff

\[
x^{MN}=y^{MN}.
\]

Thus the components are

\[
C_t=\{x\in L:x^{MN}=t\},\qquad t\in\mu_c.
\]

There are exactly \(c\) of them, each of size \(MN\).  Inside one component
there are \(N\) \(R\)-blocks and \(M\) \(S\)-blocks.  The map

\[
x\longmapsto (x^M,x^N)
\]

is injective, and both the component and the Cartesian product of those two
vertex sets have size \(MN\).  Hence every component is \(K_{N,M}\).

### 3.4 Common unions are component unions

For any two partitions of a finite set, represent each point by the edge
joining its two blocks.  A point set is a union of blocks of the first
partition iff its edge indicator is constant around every left vertex; it is
a union of blocks of the second partition iff the indicator is constant
around every right vertex.  Both conditions hold iff the indicator is constant
on each connected component.

Therefore the common unions here are exactly

\[
S_A=\bigcup_{t\in A}C_t,
\qquad A\subseteq\mu_c.
\]

There are \(2^c\) in total and \(2^c-2\) nontrivial ones.  The common unions of
size \(hMN\) are exactly those with \(|A|=h\), so there are \(\binom ch\).

### 3.5 One envelope-free syndrome line carrying all fixed-size common unions

For \(A\in\binom{\mu_c}{h}\), define

\[
F_A(T)=\prod_{t\in A}(T-t),
\qquad
P_A(X)=F_A(W(X))=\prod_{t\in A}(X^{MN}-t).
\]

The polynomial \(P_A\) is the monic locator of \(S_A\), of degree

\[
\deg P_A=hMN=k+\sigma.
\]

Put

\[
E(X)=W(X)-\theta=X^{MN}-\theta,
\qquad
f(X)=X^k,
\qquad
g(X)=-\frac1{E(X)}.
\]

Because \(\theta\notin K\), \(E\) has no zero on \(L\).  It is squarefree
because the characteristic is prime to \(MN\).

For every \(A\), set

\[
z_A=-F_A(\theta)
\]

and define

\[
Q_A(X)
=X^k-rac{F_A(W(X))-F_A(\theta)}{W(X)-\theta}.
\]

The divided difference is a polynomial.  Since \(F_A\) is monic of degree
\(h\), that divided difference is monic of degree \(h-1\) in \(W\); its
leading term is

\[
W^{h-1}=X^{(h-1)MN}=X^k.
\]

The leading terms cancel, so

\[
\deg Q_A<k.
\]

Thus \(Q_A\) is an RS codeword polynomial.  On the affine word line

\[
w_z=f+zg,
\]

one has the exact identity

\[
w_{z_A}(X)-Q_A(X)
=
\frac{F_A(W(X))}{W(X)-\theta}
=
\frac{P_A(X)}{E(X)}.
\]

Since \(E\) is nonzero on \(L\), the zero set on \(L\) is exactly \(S_A\).
Hence \(S_A\) is the **full exact agreement support**, not merely a selected
subset of a larger support.

### 3.6 Distinct slopes

If \(z_A=z_B\), then

\[
F_A(\theta)=F_B(\theta).
\]

The difference \(F_A-F_B\in K[T]\) has degree at most \(h<D\).  Since
\(\theta\) has degree \(D\) over \(K\), the difference must be zero.  Unique
factorization then gives \(A=B\).  Therefore all \(\binom ch\) slopes are
distinct.

### 3.7 Transversality

Suppose the direction word \(g=-1/E\) agreed on \(S_A\) with a polynomial
\(G\) of degree below \(k\).  Then

\[
EG+1
\]

would vanish on the \(k+\sigma\) points of \(S_A\), while

\[
\deg(EG+1)\le \sigma+k-1=k+\sigma-1.
\]

It would be identically zero, impossible because the nonconstant polynomial
\(E\) cannot divide \(1\).  Thus the syndrome direction is not in the witness
span for any \(S_A\).

### 3.8 No proper syndrome envelope

Let \(u=\operatorname{syn}(f)\).  If \(u\in V_T\) for some \(|T|<r\), then
\(f=X^k\) would agree with a polynomial of degree below \(k\) on

\[
|L\setminus T|>n_0-r=k
\]

points.  Their difference is a nonzero degree-\(k\) polynomial, a
contradiction.  Therefore the anchor syndrome lies in no proper secant
envelope, and consequently the whole affine syndrome line is contained in no
proper envelope.

### 3.9 No common core and no tangent affine polynomial line

Because \(h<c\), every component is omitted by some \(h\)-subset \(A\).  Hence

\[
\bigcap_{|A|=h}S_A=\varnothing,
\qquad
\gcd_{|A|=h}P_A=1.
\]

Now suppose all the codeword polynomials lay on one tangent affine line

\[
Q_A=Q_0+z_A G.
\]

Using \(P_A=E(w_{z_A}-Q_A)\), this would imply

\[
P_A=E(f-Q_0)+z_A(Eg-EG),
\]

so all locators \(P_A\) would be collinear in the polynomial vector space.
They are not.  Fix a set \(B\subset\mu_c\) of size \(h-2\) and distinct
\(a,b,d\notin B\).  Writing \(P_B(W)=\prod_{t\in B}(W-t)\),

\[
P_{B\cup\{a,b\}}-P_{B\cup\{a,d\}}
=(d-b)P_B(W)(W-a),
\]

whereas

\[
P_{B\cup\{a,b\}}-P_{B\cup\{b,d\}}
=(d-a)P_B(W)(W-b).
\]

These two differences are not scalar multiples.  Thus the full packet is not
contained in one tangent affine polynomial line.

The packet does lie on the quotient/color template \(W=X^{MN}\).  That is
precisely the additional invariant exposed by the counterpacket.

### 3.10 Exact weighted-cover value

Let

\[
\mathscr F_h=\{S_A:A\in\tbinom{\mu_c}{h}\}.
\]

A \(k\)-subset \(U\subseteq L\) contained in some \(S_A\) has size

\[
|U|=(h-1)MN.
\]

Since each component has size \(MN\), \(U\) meets at least \(h-1\) components.
If it meets exactly \(h-1\), it must fill all of them and is contained in at
most

\[
c-h+1
\]

members of \(\mathscr F_h\).  If it meets \(h\) components, it determines the
unique containing support.  Thus every \(k\)-core covers at most \(c-h+1\)
supports, and

\[
\kappa_k(\mathscr F_h)
\ge
\left\lceil
\frac{\binom ch}{c-h+1}
\right\rceil.
\]

But

\[
\left\lfloor\frac r\sigma\right\rfloor=c-h+1.
\]

Therefore

\[
\left\lfloor\frac r\sigma\right\rfloor
\kappa_k(\mathscr F_h)
\ge \binom ch.
\]

Since the other entry in the minimum defining \(W_\sigma\) is exactly
\(|\mathscr F_h|=\binom ch\),

\[
\boxed{W_\sigma(\mathscr F_h)=\binom ch.}
\]

There is no fixed-core weighted compression of this overlap packet.

## 4. Parameter ledger and finite relevance

The two original block systems have:

\[
|\Pi_R|=cN,\qquad |\Pi_S|=cM.
\]

Every support in \(\mathscr F_h\) uses

\[
hN\quad R\text{-blocks},
\qquad
hM\quad S\text{-blocks}.
\]

The common-component system \(\Pi_W\) has \(c\) blocks, and each support uses
exactly \(h\) of them.  Its raw profile count is the exact packet count
\(\binom ch\).

The construction can be placed at each official rate \(\rho=1/d\),
\(d\in\{2,4,8,16\}\): choose \(c\) divisible by \(d\), large enough that \(c/d+1\le c-1\), and set

\[
h=\frac cd+1.
\]

Then

\[
\frac{k}{n_0}
=
\frac{(h-1)MN}{cMN}
=
\frac1d.
\]

This is a structural route cut, not by itself a \(2^{-128}\) unsafe-reserve
certificate.  Its exact finite consequence is that the pairwise overlap term
can be as large as \(\binom ch\) even for fixed map degrees and an
envelope-free line.

### Concrete checked instance

Take

\[
M=2,\quad N=3,\quad c=8,\quad h=5,
\]

\[
K=\mathbf F_{97},\qquad L\le K^\times,\quad |L|=48,
\]

and let \(F=K(\theta)\) where \(\theta\) has degree \(6\), for example a root
of

\[
T^6+70T^5+53T^4+81T^3+58T^2+6T+3
\]

over \(\mathbf F_{97}\).  Then

\[
(n_0,k,\sigma,j)=(48,24,6,18).
\]

The incidence graph is eight disjoint copies of \(K_{3,2}\).  It has

\[
2^8=256
\]

common unions, \(254\) nontrivial common unions, and

\[
\binom85=56
\]

distinct exact common-union slopes at agreement \(30=k+\sigma\).  The exact
weighted cover is also \(56\).

## 5. Bankable versus conditional

### Bankable

- The block-incidence/common-union lemma for two finite partitions.
- The coprime monomial no-common-right-factor proof.
- The exact component decomposition into \(cK_{N,M}\).
- The parameterized RS syndrome-line construction.
- Exact support, distinct-slope, transversality, and envelope-free proofs.
- Exact weighted-cover identity.
- The conclusion that common-right-factor/refinement closure alone is
  insufficient.

### Conditional / not proved here

- A repaired global theorem after adding all common left composites or finite
  component colors.
- A bound on how many inequivalent common-color systems can be heavy on one
  syndrome line.
- Any full MCA safe-side bound or Proximity Prize certificate.

## 6. Failure point of the old route

The old rigidity heuristic confuses two opposite composition directions:

- a **common right factor** gives a common refinement of the two block systems;
- a **common left composite** gives a common coarsening, namely the connected
  components of the block-incidence graph.

Large common-union families are controlled by the second object.  Excluding
the first does not control the second.  In the counterpacket, the common color
is

\[
\chi_R(y)=y^N,
\qquad
\chi_S(z)=z^M,
\]

and

\[
\chi_R(R(x))=x^{MN}=\chi_S(S(x)).
\]

Any registry that records only right factors/refinements will count two
apparently incompatible systems while missing the canonical component color
that organizes their entire overlap.

## 7. Next exact lemma

The next repair target should be:

```text
L-MCA-TWO-BLOCK-COMMON-COLOR-CLOSURE
```

A narrow statement is:

> For two separable support block systems on one envelope-free syndrome line,
> form the canonical component partition of their bipartite incidence graph.
> If the fixed-size common-union packet has weighted mass above an explicit
> finite threshold, prove that the component labels are induced by bounded-
> degree maps \(A,B\) satisfying
> \(A\circ R=B\circ S\) on the realized domain; after an explicit point-count
> threshold, promote this to a global rational identity.  Charge the overlap
> once to the resulting common-coarsening/color class.  Otherwise give the
> explicit residual common-union bound.

For the present packet,

\[
A(Y)=Y^N,
\qquad B(Z)=Z^M,
\qquad W=A\circ R=B\circ S.
\]

## Final question

A full solve does not follow from this wall.  There is a plausible repaired
route only after replacing common-right-factor overlap rigidity by a canonical
common-color/common-left-composite theorem and then proving a finite aggregate
bound for those color classes.  The next exact lemma is
`L-MCA-TWO-BLOCK-COMMON-COLOR-CLOSURE` above.
