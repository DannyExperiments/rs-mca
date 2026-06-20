BANKABLE_LEMMA

# Model generalized-Jacobian quotient-conditioned finite local limit

## 1. Executive verdict

The full all-field inequality requested in
`W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT` is not proved here.
What is proved is the following exact finite packet.

1. The model generalized-Jacobian map for
   \(\Delta=[0]+\sigma[\infty]\) is written explicitly, including the exact
   effective group, Fourier formula, and quotient-character charge.
2. When \(p>\sigma-1\), the exact size of \(G_{\rm eff}\) and the declared
   periodic-character quotient are computed over arbitrary extension fields.
3. An unconditional cyclotomic-rank cap is proved in every odd
   characteristic.  It yields polynomial fibers at corrected reserve for
   every fixed characteristic.
4. An explicit norm-rigidity criterion is proved.  Under it, the requested
   inequality holds with
   \[
   C_\sigma=0,
   \qquad
   P_\sigma(n)=
   \binom{n/M_0}{\lfloor n/(2M_0)\rfloor},
   \qquad
   M_0=2^{\lceil\log_2\sigma\rceil}.
   \]
5. A matching structural lower floor is constructed.  It proves that the
   declared character quotient \(Q_{\rm per}\) does not absorb the ordinary
   whole-block quotient packet; a residual of dyadic block scale is
   unavoidable.
6. A tensorized \(\mathbb F_{17}\) construction proves that, outside the
   norm-rigid range, the product coordinate does not restore
   characteristic-zero quotient rigidity: many distinct \(M_0\)-classes can
   merge into one model fiber.

**Confidence:** high (0.96) for the proved statements.  The remaining
near-split finite-field local limit is genuinely unresolved by this packet.

Throughout, “proper subgroup” in the definition of \(Q_{\rm per}\) means a
**nontrivial proper subgroup**.  If the identity subgroup is allowed, every
function is constant on its cosets and \(Q_{\rm per}\) becomes tautological.

---

## 2. Model coordinates and exact Fourier decomposition

Let
\[
F=\mathbb F_q,\qquad \operatorname{char}F=p,\qquad
n=2^m\mid(q-1),\qquad H=\alpha\mu_n\subset F^\times,
\]
and assume
\[
1\le \sigma<n,\qquad s:=\sigma-1,\qquad 0\le j\le n.
\]
For a \(j\)-subset \(T\subset H\), write
\[
E_T(z):=\prod_{x\in T}(1-xz)
       =\sum_{r=0}^j(-1)^r e_r(T)z^r.
\]

### Theorem 2.1 (exact model boundary map)

For \(\Delta=[0]+\sigma[\infty]\),
\[
G_\Delta=H^0(\Delta,\mathcal O_\Delta)^\times/F^\times
\cong F^\times\times U_s,
\qquad
U_s:=1+zF[z]/(z^{s+1}),
\]
and
\[
|G_\Delta|=(q-1)q^s.
\]
After translating the target by a fixed element depending only on the
auxiliary form \(L_*\), the boundary map is
\[
\beta(x)=(-x,1-xz),
\]
so that
\[
\Phi_\sigma(T):=\prod_{x\in T}\beta(x)
 =\left((-1)^j\prod_{x\in T}x,
 E_T(z)\bmod z^{s+1}\right).
\]
Consequently a model fiber fixes exactly
\[
\prod_{x\in T}x,
\qquad e_1(T),\ldots,e_s(T).
\]

#### Proof

At the reduced point \(0\), the local algebra is \(F\).  At the length
\(\sigma=s+1\) point at infinity, with local parameter \(z\), it is
\(F[z]/(z^{s+1})\).  Thus
\[
H^0(\Delta,\mathcal O_\Delta)^\times
\cong F^\times\times(F[z]/(z^{s+1}))^\times.
\]
Quotienting by diagonal constants and normalizing the second component to
constant term one gives \(F^\times\times U_s\), with the displayed order.

Take \(L_x=X-xZ\) and, for example, \(L_*=X+Z\).  At \(0\),
\(L_x/L_*=-x\); at infinity,
\[
\frac{L_x}{L_*}=\frac{1-xz}{1+z}.
\]
Multiplying every point image by the fixed element \((1,1+z)\) only
translates every degree-\(j\) target by its \(j\)-th power.  This gives
\(\beta(x)=(-x,1-xz)\) and the product formula. \(\square\)

Fix \(x_0\in H\), put
\[
a_x:=\beta(x)\beta(x_0)^{-1},
\qquad
G_{\rm eff}:=\langle a_x:x\in H\rangle\le G_\Delta,
\]
and, for a target \(b\) in the correct translate of \(G_{\rm eff}\), put
\[
g:=b\,\beta(x_0)^{-j}\in G_{\rm eff}.
\]

### Theorem 2.2 (effective Fourier formula)

The exact model-fiber count is
\[
N_\Delta(b)
 =\frac1{|G_{\rm eff}|}
   \sum_{\chi\in\widehat{G_{\rm eff}}}
   \chi(g)^{-1}
   e_j\bigl(\chi(a_x):x\in H\bigr).
\]

If \(\mathcal S\le\widehat{G_{\rm eff}}\), let
\[
K=\mathcal S^\perp,
\qquad Q=G_{\rm eff}/K,
\qquad \pi:G_{\rm eff}\to Q,
\]
and let \(N_Q(y)\) count \(j\)-subsets after projection to \(Q\).  Then the
entire Fourier contribution of \(\mathcal S\) is exactly
\[
\frac1{|G_{\rm eff}|}
\sum_{\chi\in\mathcal S}
 \chi(g)^{-1}e_j(\chi(a_x):x\in H)
 =\frac{N_Q(\pi g)}{|K|}.
\]

#### Proof

The first identity is character orthogonality applied to
\(\prod_{x\in T}a_x=g\).  Since \(\widehat Q\) identifies with
\(\mathcal S\), Fourier inversion on \(Q\) gives
\[
N_Q(\pi g)=\frac1{|Q|}
\sum_{\chi\in\mathcal S}
 \chi(g)^{-1}e_j(\chi(a_x):x\in H).
\]
Now \(|G_{\rm eff}|=|Q||K|\). \(\square\)

---

## 3. Exact \(G_{\rm eff}\) and \(Q_{\rm per}\) when \(p>s\)

For \(r\in\mathbb Z/n\mathbb Z\), let
\[
C_p(r)=\{p^kr\bmod n:k\ge0\}
\]
be its \(p\)-cyclotomic orbit.  Define
\[
Z_s(p,n)=\bigcup_{1\le r\le s}C_p(r),
\qquad D_s(p,n)=|Z_s(p,n)|,
\]
and split it by parity:
\[
Z_s^{\rm ev}=\bigcup_{\substack{1\le r\le s\\r\text{ even}}}C_p(r),
\qquad
Z_s^{\rm odd}=\bigcup_{\substack{1\le r\le s\\r\text{ odd}}}C_p(r),
\]
with cardinalities \(D_s^{\rm ev},D_s^{\rm odd}\).  Since \(p\) is odd,
parity is preserved by multiplication by \(p\), so
\[
D_s=D_s^{\rm ev}+D_s^{\rm odd}.
\]

### Theorem 3.1 (exact effective group in the logarithmic range)

Assume \(p>s\).  Then
\[
|G_{\rm eff}|=n\,p^{D_s(p,n)}.
\]

#### Proof

The truncated logarithm is an isomorphism
\[
\log:U_s\longrightarrow zF[z]/(z^{s+1})
\]
because \(1,\ldots,s\) are invertible in \(F\).  Up to nonzero coordinate
scalings,
\[
\log\frac{1-xz}{1-x_0z}
 =-\sum_{r=1}^s\frac{x^r-x_0^r}{r}z^r.
\]
Thus the local effective image is the \(\mathbb F_p\)-span of the differences
\[
(x^r-x_0^r)_{1\le r\le s},\qquad x\in H.
\]
The moment matrix with rows \(0,1,\ldots,s\) has \(\mathbb F_p\)-rank
\(1+D_s\): its nonzero Fourier frequencies are precisely the union of the
\(p\)-cyclotomic orbits meeting \(1,\ldots,s\), while frequency \(0\) is a
separate orbit.  Restricting the coefficient vectors to total sum zero
therefore gives local difference-span dimension \(D_s\).

The toric projection of \(G_{\rm eff}\) is \(\mu_n\).  The toric part has
order \(n\), while the local part is a \(p\)-group.  A subgroup surjecting to
both factors is their direct product because their orders are coprime.
Hence \(|G_{\rm eff}|=np^{D_s}\). \(\square\)

### Theorem 3.2 (exact declared periodic-character quotient)

Assume \(p>s\) and \(n\ge4\).  Let \(\mathcal S_{\rm per}\) be the subgroup
of \(\widehat{G_{\rm eff}}\) generated by characters whose pullback to \(H\)
is constant on cosets of a nontrivial proper subgroup of \(H\).  Then
\[
|\mathcal S_{\rm per}|
 =\frac n2\,p^{D_s^{\rm ev}},
\qquad
|\ker\pi_{\rm per}|
 =2p^{D_s^{\rm odd}}.
\]

#### Proof

Every nontrivial subgroup of the dyadic group \(H\) contains \(-1\).
Therefore a pullback is periodic on some nontrivial subgroup only if it is
invariant under \(x\mapsto-x\); conversely invariance under \(-1\) makes it
constant on \(\mu_2\)-cosets.

On the toric factor, invariance under \(-1\) means that the character exponent
is even, giving \(n/2\) choices.  Under logarithm, the local effective space
splits into its even- and odd-frequency eigenspaces under \(x\mapsto-x\), of
dimensions \(D_s^{\rm ev}\) and \(D_s^{\rm odd}\).  An invariant local
character must annihilate the odd eigenspace, giving \(p^{D_s^{\rm ev}}\)
choices.  Thus the displayed size of \(\mathcal S_{\rm per}\) follows, and
\[
|\ker\pi_{\rm per}|=
\frac{|G_{\rm eff}|}{|\mathcal S_{\rm per}|}
=2p^{D_s^{\rm odd}}.
\]
\(\square\)

### Split-prime specialization

If \(q=p\) and \(p\equiv1\pmod n\), every cyclotomic orbit is a singleton, so
\[
D_s=s,
\quad D_s^{\rm ev}=\lfloor s/2\rfloor,
\quad D_s^{\rm odd}=\lceil s/2\rceil,
\]
and hence
\[
|G_{\rm eff}|=np^s,
\qquad
|\ker\pi_{\rm per}|=2p^{\lceil s/2\rceil}.
\]
Equivalently, after choosing logarithmic coordinates, characters are indexed
by
\[
(a,c_1,\ldots,c_s)\in\mathbb Z/n\mathbb Z\times\mathbb F_p^s,
\]
and the periodic-character subgroup is exactly
\[
a\equiv0\pmod2,
\qquad c_r=0\quad(r\text{ odd}).
\]

### Endpoint \(\sigma=1\)

Here \(s=0\) and the model fixes only the product.  For \(n\ge4\) and
\(0<j<n\), the quotient identity is exact with no residual:
\[
N_\Delta(b)=\frac{N_{Q_{\rm per}}(\pi b)}2.
\]
Indeed the nonperiodic characters are the odd exponents; their values on \(H\)
run through all \(n\)-th roots of unity, and
\[
\prod_{x\in H}(1+Y\chi(x))=1-(-Y)^n
\]
has zero \(Y^j\)-coefficient for \(0<j<n\).

---

## 4. Unconditional cyclotomic-rank cap

### Theorem 4.1 (finite-field rank cap)

In every odd characteristic, with no size hypothesis on \(p\),
\[
\boxed{
N_\Delta(b)\le 2^{\,n-D_s(p,n)}.
}
\]
This holds for every target \(b\) and every \(j\).

#### Proof

Equality of \(e_1,\ldots,e_s\) implies equality of the first \(s\) power sums
in every characteristic: Newton's recurrence has coefficient \(1\) on the
new power sum, so no division is required in this direction.

Identify \(H\) with \(\mu_n=\langle\omega\rangle\), absorbing the scalar
\(\alpha^r\) in each moment coordinate.  For an indicator vector
\(y=(y_a)_{a\in\mathbb Z/n\mathbb Z}\in\mathbb F_p^n\), define
\[
\mathcal M_s(y)=
\left(\sum_a y_a\omega^{ar}\right)_{1\le r\le s}.
\]
The kernel consists of polynomials
\(Y(X)=\sum_a y_aX^a\) vanishing at \(\omega^r\), \(1\le r\le s\).  Since
\(Y\) has coefficients in \(\mathbb F_p\), it also vanishes at every
Frobenius conjugate \(\omega^{rp^k}\).  Conversely those are all the forced
zeros.  Because \(X^n-1\) is squarefree, the kernel is the cyclic code whose
generator is the product of the distinct minimal polynomials indexed by
\(Z_s(p,n)\).  Its dimension is therefore
\[
n-D_s(p,n).
\]
A model fiber is contained in one affine fiber of \(\mathcal M_s\), hence in
an affine \(\mathbb F_p\)-subspace of dimension \(n-D_s\).  Every affine
\(d\)-subspace of \(\mathbb F_p^n\) has at most \(2^d\) points in
\(\{0,1\}^n\): choose \(d\) coordinate positions on which projection is
injective.  Constant weight and the product constraint only reduce the count.
\(\square\)

### Corollary 4.2 (explicit fixed-characteristic polynomial cap)

Let
\[
L_p:=v_2(p^2-1),
\qquad R_p:=2^{L_p}-1.
\]
Assume \(s\ge R_p\), put
\[
a:=\left\lfloor\log_2\frac{s}{R_p}\right\rfloor,
\qquad B:=2^{a+1}.
\]
Then \(B\mid n\) and
\[
D_s(p,n)\ge n-\frac nB,
\qquad
\boxed{N_\Delta(b)\le 2^{n/B}}.
\]
In particular, for every integer \(D\ge1\), the exact hypothesis
\[
s\ge \frac{R_p n}{D\log_2 n}
\]
implies
\[
N_\Delta(b)\le n^D.
\]

#### Proof

For every \(r\ge L_p\), the subgroup generated by \(p^2\) modulo \(2^r\)
is exactly the kernel of reduction
\[
(\mathbb Z/2^r\mathbb Z)^\times
 \longrightarrow(\mathbb Z/2^{L_p}\mathbb Z)^\times.
\]
Indeed LTE gives
\[
v_2\big((p^2)^{2^k}-1\big)=L_p+k,
\]
so \(p^2\) has order \(2^{r-L_p}\), equal to the kernel size.  Hence every
\(p\)-cyclotomic orbit on odd residues modulo any power of two has an odd
representative at most \(R_p\).

Write a nonzero frequency as \(2^vu\), with \(u\) odd.  If \(v\le a\), its
orbit has a representative at most
\[
2^vR_p\le2^aR_p\le s,
\]
so that entire orbit lies in \(Z_s(p,n)\).  The only possibly uncovered
frequencies, together with frequency \(0\), are multiples of \(2^{a+1}=B\),
of which there are \(n/B\).  Thus \(n-D_s\le n/B\), and Theorem 4.1 applies.
Finally \(B>s/R_p\), so \(n/B<nR_p/s\le D\log_2n\). \(\square\)

This closes the corrected-reserve model fiber in every fixed
characteristic.  The remaining regime is necessarily near-split in the
2-adic sense: \(v_2(p^2-1)\) must grow with \(n\).

---

## 5. Explicit norm-rigid finite local limit

Let
\[
M_0:=\min\{2^a:2^a>s\}
     =2^{\lceil\log_2\sigma\rceil},
\qquad N_0:=n/M_0.
\]
For every dyadic \(M\mid n\) with \(M\le s\), put
\[
N_M:=n/M,
\qquad t_M:=\lfloor s/M\rfloor,
\qquad f_M:=\operatorname{ord}_{N_M}(p).
\]
Let
\[
A_M:=
\#\left\{
\ell\langle p\rangle:
1\le\ell\le t_M,
\ \ell\text{ odd}
\right\}
\]
where the classes are taken in
\((\mathbb Z/N_M\mathbb Z)^\times/\langle p\rangle\).

### Theorem 5.1 (exact norm-rigidity criterion)

Assume that for every dyadic \(M\le s\),
\[
\boxed{
 p^{f_MA_M}>N_M^{\varphi(N_M)}.
}
\tag{NR}
\]
Then any two equal-size subsets of \(H\) with equal
\(e_1,\ldots,e_s\) differ by a function constant on \(\mu_{M_0}\)-cosets.
Consequently every model generalized-Jacobian fiber satisfies
\[
\boxed{
N_\Delta(b)
 \le
P_{\rm block}(n,\sigma)
 :=\binom{N_0}{\lfloor N_0/2\rfloor}.
}
\]
Therefore the requested quotient-conditioned inequality holds, under
\((\mathrm{NR})\), with the explicit integers
\[
\boxed{
C_\sigma=0,
\qquad
P_\sigma(n)=\binom{n/M_0}{\lfloor n/(2M_0)\rfloor}.
}
\]

#### Proof

Let \(S,T\subseteq H\) have equal first \(s\) elementary coefficients.  After
scaling by \(\alpha^{-1}\), write their exponent sets in
\(\mathbb Z/n\mathbb Z\), and set
\[
F(X)=\sum_{a\in S}X^a-\sum_{b\in T}X^b\in\mathbb Z[X],
\qquad \deg F<n.
\]
Equality of elementary coefficients implies equality of power sums, hence
\[
F(\omega^r)=0\quad(1\le r\le s)
\]
in characteristic \(p\).

For dyadic \(M\mid n\), define
\[
Q_M(X)=1+X^{n/M}+\cdots+X^{(M-1)n/M}.
\]
Choose the largest \(M\) for which \(Q_M\mid F\) in \(\mathbb Z[X]\).  If
\(M>s\), then \(M\ge M_0\), and the coefficients of \(F\) are constant on
residue classes modulo \(n/M\); this is exactly invariance on
\(\mu_M\)-cosets, hence on \(\mu_{M_0}\)-cosets.

Suppose instead that \(M\le s\).  Write
\[
F=Q_MG,
\qquad \deg G<N_M.
\]
Because multiplication by \(Q_M\) merely repeats the coefficients of \(G\)
in \(M\) disjoint blocks, every coefficient of \(G\) lies in
\(\{-1,0,1\}\).  Let \(\zeta_{N_M}=\zeta_n^M\).  Maximality of \(M\) gives
\[
G(\zeta_{N_M})\ne0;
\]
otherwise \(\Phi_{N_M}=X^{N_M/2}+1\) would divide \(G\), and
\(Q_{2M}=Q_M\Phi_{N_M}\) would divide \(F\).

For \(1\le\ell\le t_M\), evaluation at \(r=M\ell\) yields
\[
0=F(\omega^{M\ell})
 =M\,G((\omega^M)^\ell),
\]
and \(M\) is invertible because \(p\) is odd.  Let \(\mathfrak p\) be the
prime of \(\mathbb Z[\zeta_{N_M}]\) induced by
\(\zeta_{N_M}\mapsto\omega^M\).  Its norm is \(p^{f_M}\).  Distinct cosets
\(\ell\langle p\rangle\) give distinct conjugate primes over \(p\).  Hence
\[
p^{f_MA_M}
 \mid
\left|\operatorname{Norm}_{\mathbb Q(\zeta_{N_M})/\mathbb Q}
       G(\zeta_{N_M})\right|.
\]
Every conjugate of \(G(\zeta_{N_M})\) has absolute value at most
\(\|G\|_1\le N_M\), so
\[
0<\left|\operatorname{Norm}G(\zeta_{N_M})\right|
 \le N_M^{\varphi(N_M)},
\]
contradicting \((\mathrm{NR})\).  Thus \(M>s\), proving
\(\mu_{M_0}\)-invariance.

Fix one set \(T_0\) in a fiber.  A partially occupied \(M_0\)-coset is frozen:
a constant difference \(+1\) or \(-1\) would leave the Boolean cube.  If
\(T_0\) has \(a\) full and \(b\) empty \(M_0\)-cosets, another equal-weight
set in the same class is obtained by emptying \(u\) full cosets and filling
\(u\) empty cosets.  Hence the class size is
\[
\sum_u\binom au\binom bu
 =\binom{a+b}{a}
 \le\binom{N_0}{\lfloor N_0/2\rfloor}.
\]
The product condition can only reduce this count. \(\square\)

### Corollary 5.2 (simpler checkable sufficient conditions)

The number of selected odd integers is
\[
L_M:=\left\lceil\frac{\lfloor s/M\rfloor}{2}\right\rceil.
\]
Each \(p\)-orbit has at most \(f_M\) elements, so
\[
f_MA_M\ge L_M.
\]
Thus it is enough to check
\[
\boxed{
 p^{L_M}>(n/M)^{n/(2M)}
\quad\text{for every dyadic }M\le s.
}
\tag{NR'}
\]
A single still simpler sufficient condition is
\[
\boxed{p^{2s}>n^{3n}.}
\tag{NR''}
\]
Indeed
\[
L_M\ge \frac{s}{3M},
\]
and \((\mathrm{NR}'')\) gives
\[
p^{s/(3M)}>n^{n/(2M)}\ge(n/M)^{n/(2M)}.
\]
For split primes \(p\equiv1\pmod n\), \((\mathrm{NR}')\) is the exact
prime-norm test obtained from this argument.

### Corrected-reserve consequence

If
\[
\sigma\ge\frac{n}{D\log_2n}
\]
for an integer \(D\ge1\), then, under \((\mathrm{NR})\),
\[
N_\Delta(b)
 \le2^{n/M_0}
 \le2^{n/\sigma}
 \le n^D.
\]
All inequalities here are finite and exact.

---

## 6. The dyadic block residual is unavoidable

### Theorem 6.1 (exact structural floor after the declared quotient)

Assume \(\sigma\ge2\), let \(M_0\) and \(N_0=n/M_0\) be as above, and suppose
\(N_0\ge2\).  For every
\[
0\le\ell\le N_0-1,
\qquad j=1+M_0\ell,
\]
there is a model target \(b\) with
\[
\boxed{
N_\Delta(b)
 \ge
B(N_0,\ell)
 :=\left\lceil
   \frac1{N_0}\binom{N_0-1}{\ell}
  \right\rceil.
}
\]
The supports in this packet have trivial multiplicative stabilizer.

Moreover, in split prime fields, any inequality of the requested form with a
fixed nonnegative integer \(C_\sigma\) and an integer residual
\(P_\sigma(n)\) valid for all \(p\equiv1\pmod n\) must satisfy
\[
\boxed{
P_\sigma(n)\ge B(N_0,\ell).
}
\]

#### Proof

Partition \(H\) into its \(N_0\) cosets of \(\mu_{M_0}\).  Fix one coset
\(C_0\) and one point \(r\in C_0\).  For every \(\ell\)-subset \(\mathcal A\)
of the other cosets, put
\[
T_{\mathcal A}=\{r\}\cup\bigcup_{C\in\mathcal A}C.
\]
For a coset \(C=y\mu_{M_0}\),
\[
\prod_{x\in C}(1-xz)=1-y^{M_0}z^{M_0}.
\]
Since \(M_0>s\),
\[
E_{T_{\mathcal A}}(z)
 \equiv1-rz\pmod{z^{s+1}},
\]
independently of \(\mathcal A\).  Thus all first \(s\) elementary
coefficients agree.  The product is
\[
(-1)^\ell r\prod_{C=y\mu_{M_0}\in\mathcal A}y^{M_0},
\]
and takes at most \(N_0\) values.  Pigeonhole gives the displayed fiber.

There is exactly one partially occupied \(M_0\)-coset, namely \(C_0\), and its
occupied part is the singleton \(\{r\}\).  A multiplicative stabilizer must
fix \(C_0\), hence lie in \(\mu_{M_0}\), and then fix \(r\); it is therefore
trivial.

Now take \(q=p\equiv1\pmod n\).  By Theorems 3.1 and 3.2,
\[
|G_{\rm eff}|=np^s,
\qquad
|\ker\pi_{\rm per}|=2p^{\lceil s/2\rceil}.
\]
For every target,
\[
\frac{N_{Q_{\rm per}}(\pi b)}{|\ker\pi_{\rm per}|}
 \le\frac{\binom nj}{2p^{\lceil s/2\rceil}},
\qquad
C_\sigma\frac{\binom nj}{|G_{\rm eff}|}
 =C_\sigma\frac{\binom nj}{np^s}.
\]
There are arbitrarily large primes \(p\equiv1\pmod n\).  If
\(P_\sigma(n)\le B(N_0,\ell)-1\), choose such a prime so large that the sum of
the two displayed terms is less than \(1\).  The requested inequality then
contradicts the constructed fiber. \(\square\)

This proves a structural defect in the declared quotient: whole-block support
rearrangements are produced by coherent sums of many nonperiodic characters,
not by the subgroup of characters whose individual pullbacks are periodic.
They must be paid by the residual or by a support/configuration quotient.

---

## 7. Product does not eliminate finite-characteristic aperiodic collisions

The next construction is not larger than the dyadic block residual, but it is
an exact obstruction to extending the norm-rigid **one quotient class per
fiber** conclusion to all finite fields.

### Theorem 7.1 (tensorized \(\mathbb F_{17}\) model collision)

In \(\mathbb F_{17}^\times=\mu_{16}\), let
\[
A=\{1,2,3,4,5,6,7,9,10,12\},
\]
\[
B=\{1,2,3,8,10,11,13,14,15,16\}.
\]
Then
\[
(e_1,e_2,e_3,e_4)(A)
 =(e_1,e_2,e_3,e_4)(B)
 =(8,12,13,7),
\]
while
\[
\prod A=4,
\qquad \prod B=2,
\qquad \frac{\prod A}{\prod B}=2,
\]
and \(2\) has order \(8\) in \(\mathbb F_{17}^\times\).

Let \(M,L\) be powers of two, set
\[
n=16ML,
\qquad \sigma=5M,
\qquad s=5M-1,
\qquad j=10ML=5n/8,
\]
and take
\[
q=17^{\operatorname{ord}_n(17)},
\qquad H=\mu_n\subset\mathbb F_q^\times.
\]
Then some model fiber has size at least
\[
\boxed{
F_8(L):=
\max_{r\in\mathbb Z/8\mathbb Z}
\sum_{\substack{0\le w\le L\\w\equiv r\pmod8}}
\binom Lw
\ge\left\lceil\frac{2^L}{8}\right\rceil.
}
\]
Every two distinct supports in this packet lie in distinct
\(\mu_{M_0}\)-rearrangement classes, where
\[
M_0=8M.
\]

#### Proof

Inside \(K=\mu_{16M}\), define the inflated sets
\[
\widetilde A_M=\{x\in K:x^M\in A\},
\qquad
\widetilde B_M=\{x\in K:x^M\in B\}.
\]
Since
\[
E_{\widetilde A_M}(z)=E_A(z^M),
\qquad
E_{\widetilde B_M}(z)=E_B(z^M),
\]
the two generating polynomials agree modulo \(z^{5M}\).  Their products still
have ratio \(2\).

Choose representatives \(\lambda_1,\ldots,\lambda_L\) for the cosets of
\(K\) in \(H\).  For \(\varepsilon\in\{0,1\}^L\), let
\[
T_\varepsilon
 =\bigcup_{i=1}^L
 \lambda_i
 \begin{cases}
 \widetilde A_M,&\varepsilon_i=1,\\
 \widetilde B_M,&\varepsilon_i=0.
 \end{cases}
\]
Every block has the same truncated generating polynomial, so all
\(T_\varepsilon\) have the same first \(5M-1\) elementary coefficients.
Their products differ only by
\[
2^{|\varepsilon|}.
\]
Thus all vectors with the same Hamming weight modulo \(8\) lie in one model
fiber, proving the count.

For the base difference \(1_A-1_B\), on the \(\mu_8\)-coset
\[
\{1,2,4,8,9,13,15,16\}
\]
the values include \(0,1,-1\), so it is not constant.  Under inflation, each
\(\mu_{8M}\)-coset maps onto a \(\mu_8\)-coset with kernel \(\mu_M\); hence
the inflated difference is not constant on \(\mu_{8M}\)-cosets.  If two
orientation vectors differ, this nonconstant pattern appears in at least one
\(K\)-coset.  Therefore their global difference is not
\(\mu_{8M}=\mu_{M_0}\)-invariant. \(\square\)

Thus finite-field collision multiplicity cannot be removed by adding the
product coordinate.  Any all-field proof must bound the total entropy of
merged aperiodic classes, not assert that such mergers do not occur.

---

## 8. Exact remaining wall

Let \(\sim_{M_0}\) be the characteristic-zero block equivalence on
\(j\)-subsets:
\[
S\sim_{M_0}T
\quad\Longleftrightarrow\quad
1_S-1_T\text{ is constant on every }\mu_{M_0}\text{-coset}.
\]
Every such class has size at most
\[
P_{\rm block}(n,\sigma)
 =\binom{n/M_0}{\lfloor n/(2M_0)\rfloor}.
\]
Theorem 5.1 says that under \((\mathrm{NR})\), each finite model fiber is
contained in one class.  Theorem 7.1 shows this fails in general.

For a target \(b\), partition its fiber into these classes, with sizes
\(m_1,\ldots,m_R\), and let \(E_b\) be the number of unordered pairs in the
fiber that lie in different classes.  Then, exactly,
\[
E_b
 =\frac12\left(N_\Delta(b)^2-\sum_i m_i^2\right)
 \ge\frac12\left(N_\Delta(b)^2
                 -P_{\rm block}N_\Delta(b)\right),
\]
so
\[
\boxed{
N_\Delta(b)
 \le
\frac{P_{\rm block}
 +\sqrt{P_{\rm block}^2+8E_b}}2.
}
\]
This is a correct reduction, but pair counting alone is not the final theorem:
Theorem 7.1 has many cross-class pairs while its total fiber still lies below
the block residual.  The exact missing input is therefore an **entropy/mass
bound for the union of finite-characteristic collision classes**, not merely
pairwise noncollision.

A precise remaining wall is:

```text
W-LIST-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS
```

It is needed only after excluding:

1. the norm-rigid range of Theorem 5.1; and
2. the cyclotomic-rank-safe range of Theorem 4.1 / Corollary 4.2.

Equivalently, the hard regime has both
\[
p^{f_MA_M}\le(n/M)^{\varphi(n/M)}
\]
for at least one dyadic \(M\le s\), and
\[
n-D_s(p,n)
\]
large enough that \(2^{n-D_s}\) does not fit the finite ledger.  This is the
near-split, below-norm-threshold regime.

---

## 9. Parameter ledger

| Object | Exact value or definition |
|---|---|
| Model jet depth | \(s=\sigma-1\) |
| Ambient generalized Jacobian | \(|G_\Delta|=(q-1)q^s\) |
| Model boundary | product plus \(e_1,\ldots,e_s\) |
| Effective group, \(p>s\) | \(|G_{\rm eff}|=np^{D_s(p,n)}\) |
| Split-prime effective group | \(|G_{\rm eff}|=np^s\) |
| Periodic quotient kernel, \(p>s\) | \(2p^{D_s^{\rm odd}}\) |
| Split-prime periodic kernel | \(2p^{\lceil s/2\rceil}\) |
| Least structural block | \(M_0=2^{\lceil\log_2\sigma\rceil}\) |
| Number of structural blocks | \(N_0=n/M_0\) |
| Stable residual cap | \(\binom{N_0}{\lfloor N_0/2\rfloor}\) |
| Unconditional rank cap | \(2^{n-D_s(p,n)}\) |
| Exact norm test | \(p^{f_MA_M}>(n/M)^{\varphi(n/M)}\) for all \(M\le s\) |
| Simple norm test | \(p^{\lceil\lfloor s/M\rfloor/2\rceil}>(n/M)^{n/(2M)}\) |
| One-line sufficient norm test | \(p^{2s}>n^{3n}\) |
| Necessary block floor | \(\lceil\binom{N_0-1}{\ell}/N_0\rceil\) at \(j=1+M_0\ell\) |
| Fixed-char orbit constant | \(R_p=2^{v_2(p^2-1)}-1\) |
| Fixed-char cap | \(2^{n/B}\), \(B=2^{1+\lfloor\log_2(s/R_p)\rfloor}\) |

---

## 10. Bankable versus conditional

### Bankable

- The exact model boundary coordinates and group order.
- Fourier inversion over \(G_{\rm eff}\).
- Exact quotient-character charge \(N_Q/|\ker\pi|\).
- Exact \(|G_{\rm eff}|\) and \(Q_{\rm per}\) sizes when \(p>s\).
- The unconditional cyclotomic-rank cap.
- The fixed-characteristic polynomial corollary.
- The exact norm-rigidity theorem with explicit integer residual.
- The dyadic block lower floor after \(Q_{\rm per}\) conditioning.
- The tensorized \(\mathbb F_{17}\) product-conditioned aperiodic collision.

### Not proved

No uniform constant \(C_\sigma\) is proved for the remaining near-split,
below-norm-threshold regime.  In particular, this packet does not prove the
all-field inequality with the sharp block residual.

---

## 11. Failure point and next exact lemma

The declared character quotient is not the correct complete structural charge:
whole-block support packets survive almost entirely in the residual, and
finite-characteristic aperiodic prefix collisions can tensor while preserving
the product.

The next exact theorem should be one of the following equivalent forms.

```text
L-MODEL-GJ-NEAR-SPLIT-COLLISION-CLASS-MASS
```

For the regime not covered by Theorems 4.1 and 5.1, prove an explicit finite
bound
\[
N_\Delta(b)
\le
\frac{N_{Q_{\rm per}}(\pi b)}{|\ker\pi_{\rm per}|}
+C_\sigma\frac{\binom nj}{|G_{\rm eff}|}
+\binom{n/M_0}{\lfloor n/(2M_0)\rfloor}.
\]
A Fourier-sufficient version is an exact averaged elementary-symmetric bound
for all characters outside \(\mathcal S_{\rm per}\); a support-sufficient
version is a mass/entropy bound for the union of all finite-characteristic
\(M_0\)-collision classes.

The parallel kill test is also exact: search for a finite base gadget whose
product-conditioned fiber has normalized entropy strictly exceeding one bit
per \(M_0\)-block.  The inflation-and-replication construction of Theorem 7.1
would then promote it to a parameterized counterpacket.

## 12. Route to a full solve

**Yes, conditionally.**  The model wall is now reduced to the near-split
collision-class-mass lemma above.  A proof of that lemma closes the model
finite local limit; a base gadget with normalized entropy greater than one
kills the proposed residual and forces a different support/configuration
quotient.  The next work should target that exact dichotomy rather than expand
individual character taxonomies.
