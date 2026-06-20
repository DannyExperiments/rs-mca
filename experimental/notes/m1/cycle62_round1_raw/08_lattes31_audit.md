AUDIT

# V-LATTES-31: complete degree-31 packet verification

## 1. Executive verdict and confidence

**Verdict:** the degree-31 Lattès/isogeny packet passes. No arithmetic, constant-field, fiber, pole, regularity, transversality, envelope, or target-comparison failure was found.

**Confidence:** high.

A self-contained exact Python verifier and a JSON certificate accompany this audit. The verifier uses no network access, no probabilistic primality test, and no floating-point verdict. It also supplies a concrete field model and the full coefficient vectors of the transported degree-31 map.

The original slope-deletion estimate is valid. The exact exclusion count sharpens the collision deletion from `81,509,318` to `40,754,659`, but the packet's stated weaker lower bound is retained as the certified comparison value.

## 2. Formal packet theorem

Let

\[
p=8191,
\qquad
F=\mathbf F_p[z]/(z^{18}+57z+1),
\qquad
q=p^{18},
\]

and put \(\alpha=z+1\). Then \(z^{18}+57z+1\) is irreducible over \(\mathbf F_p\), \(\alpha\) has multiplicative order \(q-1\), and

\[
2^{233}<q<2^{234}<2^{256}.
\]

Set

\[
i=\alpha^{(q-1)/4},
\qquad
h=\alpha^{(q-1)/(p+1)},
\qquad
H=\langle h\rangle,
\qquad
L=\alpha H.
\]

Then \(i^2=-1\), \(i^p=-i\), \(|H|=p+1=8192\), and

\[
\beta(t)=\alpha\frac{t-i}{t+i}
\]

is a bijection \(\mathbf P^1(\mathbf F_p)\to L\). Since \(\alpha\in L\) and \(\alpha\) is primitive, \(L\) generates all of \(F\).

On

\[
E:\ y^2=x^3+x+459
\]

over \(\mathbf F_p\), let \(G=(0,7904)\) and \(K=\langle[263]G\rangle\). Then

\[
\#E(\mathbf F_p)=8153=31\cdot263,
\qquad
\operatorname{ord}(G)=8153,
\qquad
|K|=31.
\]

The fifteen nonzero \(x\)-coordinates modulo sign in \(K\) are

\[
\{814,1493,2194,2615,2698,2895,3776,4279,
5486,5537,6235,7216,7905,8013,8050\}.
\]

For \(f(X)=X^3+X+459\), define the Vélu map

\[
\lambda(X)=X+
\sum_{u\in U}
\left(
\frac{2(f(X)+f(u))}{(X-u)^2}-2X-4u
\right).
\]

It is reduced and separable of degree \(31\), and together with
\(y'=\lambda'(x)y\) gives the normalized isogeny

\[
E\longrightarrow E':\quad y^2=x^3+36x+7292.
\]

Its rational fiber-cardinality distribution on \(\mathbf P^1(\mathbf F_p)\) is exactly

\[
31^{131},\qquad16^1,\qquad1^{4115}.
\]

Let

\[
\eta(Y)=\frac1{Y-\alpha},
\qquad
R=\eta\circ\lambda\circ\beta^{-1}\in F(X).
\]

Then \(R\) is reduced and separable of degree \(31\), has no pole on \(L\), and has exactly \(131\) disjoint full \(31\)-point fibers in \(L\). Its geometric and arithmetic Galois closure is the genus-one curve \(E_F\), with group \(D_{62}=K\rtimes\{\pm1\}\), branch signature \((2,2,2,2)\), trivial source deck group, and constant field \(F\).

For the Reed--Solomon code

\[
C=\operatorname{RS}[F,L,2048],
\qquad n=8192,
\qquad \sigma=31,
\]

there exist a two-point set \(T\subset L\), a squarefree monic degree-31 polynomial \(E_\theta\) with no root in \(L\), and a reduced direction \(g=-B_\theta/E_\theta\), such that the affine line

\[
f+z g,
\qquad f=X^{2048},
\]

has at least

\[
183062151498210163887302260440015706432>2^{127}
\]

distinct transverse MCA-bad slopes at agreement \(2079\), error count \(6113\), and reserve \(31\). The line lies in no proper syndrome envelope, and

\[
183062151498210163887302260440015706432
>
\left\lfloor\frac q{2^{128}}\right\rfloor
=
80951559894234747884481262824352.
\]

The exact exclusion count in this audit yields the stronger lower bound

\[
183062151498210163887302260440056461091,
\]

but the theorem above records the packet's original claimed number.

## 3. Verification and proof

### 3.1 Base field, extension field, and domain

Primality of \(8191\) was checked directly. Rabin's irreducibility criterion verifies \(z^{18}+57z+1\):

\[
z^{p^{18}}\equiv z\pmod{z^{18}+57z+1},
\]

and the two required gcd tests for the prime divisors \(2,3\mid18\), at exponents \(p^9\) and \(p^6\), are both one.

The exact factorization of \(q-1\) was checked, every listed factor was certified prime, and \(\alpha^{(q-1)/\ell}\ne1\) was checked for every prime \(\ell\mid q-1\). Hence \(\alpha=z+1\) is primitive.

The verifier exhaustively compares all \(8192\) Cayley values with the coset \(\alpha\langle h\rangle\). Thus the domain is exactly a multiplicative coset of power-of-two order, and not merely abstractly isomorphic to one. Since the value at \(t=\infty\) is \(\alpha\), the generated-field condition is immediate.

### 3.2 Curve order and kernel

The discriminant is

\[
-16(4+27\cdot459^2)\equiv4136\not\equiv0\pmod{8191}.
\]

The exhaustive Legendre-symbol sum is \(-39\), so

\[
\#E(\mathbf F_p)=p+1-39=8153.
\]

Exact group arithmetic gives

\[
[263]G=(8050,6188),
\qquad
[31]G=(3434,924),
\qquad
[8153]G=O.
\]

Both proper prime-factor multiples are nonzero, so \(G\) has order \(8153\). Enumerating the thirty nonzero multiples of \([263]G\) gives precisely the stated fifteen \(x\)-coordinates.

### 3.3 Vélu map and separability

Putting the displayed summands over the common denominator gives a monic denominator of degree \(30\) and a monic numerator of degree \(31\); their gcd is one. The full coefficient vectors are in the JSON certificate.

The target coefficients computed from Vélu's sums are

\[
A'=36,
\qquad
B'=7292.
\]

With \(N/D=\lambda\) and \(W=N'D-ND'\), the verifier checks the polynomial identity

\[
W^2(X)(X^3+X+459)
=
D(X)\bigl(N(X)^3+36N(X)D(X)^2+7292D(X)^3\bigr).
\]

Hence \((x,y)\mapsto(\lambda(x),\lambda'(x)y)\) lands exactly on \(E'\). The Wronskian has degree \(60\), is nonzero, and is squarefree, so the map is separable with simple ramification. This also agrees with the four order-two branch points of the Lattès cover.

### 3.4 Complete fiber distribution

The verifier evaluates \(\lambda\) at every point of \(\mathbf P^1(\mathbf F_p)\) and obtains exactly

\[
131\text{ fibers of size }31,
\quad
1\text{ fiber of size }16,
\quad
4115\text{ fibers of size }1.
\]

There is also a conceptual check. The image \(\phi(E(\mathbf F_p))\) has order \(263\). Every nonzero image point modulo sign gives one full \(31\)-point \(x\)-fiber, hence \((263-1)/2=131\) such fibers. The fiber over the identity consists of \(O\) plus the fifteen nonzero kernel \(x\)-coordinates, hence cardinality \(16\). The anti-rational subgroup has order

\[
p+1+39=8231,
\]

and the isogeny is injective on it because its rational odd-order kernel intersects it trivially. Modulo sign this supplies \((8231-1)/2=4115\) singleton fibers. The rational and anti-rational images cannot overlap away from the identity because that would produce rational two-torsion, while \(\#E'(\mathbf F_p)\) is odd.

### 3.5 Galois closure, regularity, and trivial deck group

The composite

\[
E\longrightarrow E/K=E'\longrightarrow E'/\{\pm1\}\simeq\mathbf P^1
\]

is Galois of degree \(62\), with translations by \(K\) and inversion generating \(D_{62}\). The intermediate source \(E/\{\pm1\}\simeq\mathbf P^1\) corresponds to a reflection subgroup. For odd \(31\), that reflection subgroup is core-free and self-normalizing in \(D_{62}\). Therefore:

- the Galois closure of \(\lambda\) is exactly \(E\);
- the deck group of the degree-31 map is trivial;
- the closure has genus one and signature \((2,2,2,2)\).

All kernel translations and inversion are defined over \(\mathbf F_p\). Since \(E\) is geometrically integral and has the rational point \(O\), the closure is regular with constant field \(\mathbf F_p\); after base change, its constant field is exactly \(F\).

### 3.6 Explicit transported rational map and pole removal

The verifier uses

\[
\beta^{-1}(X)=i\frac{\alpha+X}{\alpha-X}.
\]

Writing \(\lambda=N/D\) and homogenizing to degree \(31\), the transported map is

\[
R(X)=\frac{D_h(U,V)}{N_h(U,V)-\alpha D_h(U,V)},
\qquad
U=i(\alpha+X),\quad V=\alpha-X.
\]

The resulting numerator and denominator both have degree \(31\), are coprime, and have nonzero Wronskian. Their complete coefficient arrays, in the basis \(1,z,\dots,z^{17}\), have SHA-256

```text
2553e26a88c5cbf6599d192993bfd47d38e669822922fef3528341ec3bfebb50
```

under the certificate's canonical JSON encoding.

For every one of the \(8192\) points of \(L\), the verifier cross-multiplies the explicit coefficient map against \(\eta(\lambda(t))\). The denominator is nonzero at every point. Conceptually this is forced because \(\lambda(t)\in\mathbf P^1(\mathbf F_p)\), while \(\alpha\notin\mathbf F_p\); at \(\lambda(t)=\infty\), \(\eta(\infty)=0\), not a pole.

### 3.7 Exact \(\theta\)-exclusion and slope count

The exact rational image size is

\[
|R(L)|=131+1+4115=4247.
\]

Choose \(\theta\in F\) outside:

1. \(R(L)\): at most \(4247\) values;
2. the four branch values;
3. \(R(\infty)\), ensuring \(\deg(P-\theta Q)=31\);
4. \(R(0)\), ensuring the roots are nonzero for toric invariants;
5. all monomial and toric-dihedral action-collision values.

For the last item, there are \(2047\) nonidentity maps \(X\mapsto\zeta X\) and \(2048\) maps \(X\mapsto\zeta\alpha^2/X\), with \(\zeta\in\mu_{2048}\). None is a deck transformation. For each map, the nonzero rational equation

\[
R(m(X))=R(X)
\]

has at most \(2\deg R=62\) projective solutions. Thus

\[
|F\setminus G_\theta|
\le
4247+4+2+4095\cdot62
=258143,
\]

so

\[
|G_\theta|\ge q-258143>q/2.
\]

For each \(67\)-subset \(A\) of the \(131\) full values, let

\[
F_A(T)=\prod_{y\in A}\frac{T-y}{a_y}.
\]

The \(F_A\) are pairwise distinct: equality would force equality of their root sets. Hence every difference \(F_A-F_{A'}\) is a nonzero polynomial of degree at most \(67\), and has at most \(67\) roots in \(F\). With

\[
L_0=\binom{131}{67}
=183062151498210163887302260440097215750,
\]

the total pair-collision incidence is at most

\[
67\binom{L_0}{2}.
\]

Averaging over \(G_\theta\) gives a \(\theta\) with at most

\[
\left\lfloor
\frac{67\binom{L_0}{2}}{q-258143}
\right\rfloor
=40754659
\]

colliding unordered pairs. Therefore the number of distinct slopes is at least

\[
L_0-40754659
=
183062151498210163887302260440056461091.
\]

In particular, the packet's weaker estimate

\[
L_0-
\left\lfloor\frac{67L_0(L_0-1)}q\right\rfloor
=
183062151498210163887302260440015706432
>2^{127}
\]

is correct.

The same exclusion proves the stated action ranks. Distinct roots of \(E_\theta\) cannot have equal \(D\)-th powers, nor equal toric-dihedral invariant values, for any \(D\mid2048\). Hence all those action ranks are \(31\). On the other hand,

\[
[R]_{E_\theta}=\theta,
\]

so the Lattès action rank \(d_R(E_\theta)\) is exactly \(1\).

### 3.8 Support identity and codeword construction

Take the explicit defect set

\[
T=\{\beta(5),\beta(8)\};
\]

both points lie in singleton fibers, hence outside the union of the \(131\) full fibers.

Write \(R=P/Q\), put

\[
E_\theta=\frac{P-\theta Q}{a_\theta},
\]

and let \(B_\theta\), of degree less than \(31\), represent

\[
L_TQ^{67}\pmod{E_\theta}.
\]

Because \(E_\theta\) has no root in \(L\), and \(P,Q\) are coprime, \([B_\theta]\) is a unit modulo \(E_\theta\).

For a \(67\)-subset \(A\) of full values, define

\[
S_A=T\sqcup\bigcup_{y\in A}R^{-1}(y),
\qquad
L_A=L_T\prod_{y\in A}L_y.
\]

Then \(|S_A|=2+67\cdot31=2079\), and modulo \(E_\theta\),

\[
L_A\equiv
\left(\prod_{y\in A}\frac{\theta-y}{a_y}\right)B_\theta
=\kappa_A(\theta)B_\theta.
\]

Set \(z_A=-\kappa_A(\theta)\) and

\[
C_A=rac{E_\theta X^{2048}-L_A-z_AB_\theta}{E_\theta}.
\]

The numerator is divisible by \(E_\theta\). The two monic degree-2079 leading terms cancel, so \(\deg C_A<2048\). On \(S_A\),

\[
C_A(x)=x^{2048}-z_A\frac{B_\theta(x)}{E_\theta(x)}.
\]

Thus the slope \(z_A\) is bad on the line \(f=X^{2048}\), \(g=-B_\theta/E_\theta\).

### 3.9 Transversality, envelope exclusion, and denominator uniqueness

If \(g\) agreed with a polynomial \(G\) of degree below \(2048\) on \(S_A\), then

\[
E_\theta G+B_\theta
\]

would have at least \(2079\) roots but degree at most

\[
31+2047=2078.
\]

It would vanish identically, contradicting that \(B_\theta\) is a unit modulo \(E_\theta\). Every witness is therefore transverse.

For any polynomial \(G\) of degree below \(2048\), the nonzero polynomial \(X^{2048}-G\) has degree \(2048\), and hence at most \(2048\) roots. It cannot agree on the required \(2079\) points. Therefore the anchor syndrome lies in no proper agreement envelope, so the entire affine line lies in no proper common syndrome envelope.

Finally, \(g=-B_\theta/E_\theta\) is reduced. Any second reduced presentation with denominator degree at most \(31\) would give, after clearing denominators, a polynomial of degree below

\[
2048+31+31=2110<8192
\]

vanishing on all of \(L\). It is therefore the zero polynomial; reduction modulo \(E_\theta\) forces \(E_\theta\) to divide the second denominator. Thus the intrinsic denominator degree is exactly \(31\).

### 3.10 Exact finite target

The verifier checks by integer arithmetic that

\[
\binom{8192}{2079}2^{325}<q^{30},
\]

so

\[
\frac{\binom{8192}{2079}}{q^{30}}<2^{-325}.
\]

It also checks

\[
\left\lfloor\frac q{2^{128}}\right\rfloor
=80951559894234747884481262824352<2^{106},
\]

and the certified packet lower bound exceeds this target. Equivalently, the normalized bad-slope fraction is strictly greater than \(2^{-128}\).

## 4. Parameter ledger

| Quantity | Exact value |
|---|---:|
| Base prime | \(8191\) |
| Code field | \(\mathbf F_{8191^{18}}\) |
| Explicit field modulus | \(z^{18}+57z+1\) |
| Primitive coset multiplier | \(\alpha=z+1\) |
| Field interval | \(2^{233}<q<2^{234}<2^{256}\) |
| Domain size | \(8192\) |
| Dimension | \(2048\) |
| Rate | \(1/4\) |
| Reserve / map degree | \(31\) |
| Agreement | \(2079\) |
| Errors | \(6113\) |
| Full fibers | \(131\) |
| Fibers per support | \(67\) |
| Defect size | \(2\) |
| Raw support profile | \(\binom{131}{67}\) |
| Packet slope lower bound | \(183062151498210163887302260440015706432\) |
| Sharpened slope lower bound | \(183062151498210163887302260440056461091\) |
| Exact target | \(80951559894234747884481262824352\) |
| Occupancy | \(<2^{-325}\) |
| Galois closure | genus one, \(D_{62}\) |
| Lattès action rank | \(1\) |
| Monomial/toric-dihedral ranks | \(31\) for every \(D\mid2048\) |

## 5. Bankable versus conditional

### Bankable

- The explicit field model, primitive element, Cayley domain, and generated-field claim.
- The curve order, full-order point, order-31 kernel, and kernel coordinate list.
- The exact Vélu map, target curve, separability, ramification, and complete rational fiber distribution.
- The regular genus-one \(D_{62}\) Galois closure, branch signature, and trivial deck group.
- The single transported degree-31 rational map over the code field, including full coefficient vectors and pole-free evaluation on all \(8192\) domain points.
- Existence of an admissible \(\theta\) with the certified distinct-slope lower bound.
- The support construction, transversality, envelope exclusion, intrinsic denominator degree, action ranks, occupancy comparison, and exact \(2^{-128}\) target failure.

### Conditional or non-explicit

The selected \(\theta\) is certified existentially by exact finite averaging; the certificate does not name one particular field element. This is not a logical gap in the packet theorem, but it means the certificate is a proof-of-existence certificate rather than an enumerated slope-list witness. Every other object, including the code field, domain, curve, kernel, rational map, and defect points, is explicit.

## 6. Failure point

None. The wall closes as an audit pass.

The only correction to the raw narrative is positive: the good-\(\theta\) set can be bounded below by \(q-258143\), so the slope-deletion loss is about half the packet's conservative value.

## 7. Next exact lemma or construction

Do not spend another worker on degree \(113\) unless the finite frontier checker proves it uniquely relevant. The exact next Lattès-side lemma, if this branch must be used in an upper theorem, is:

> **Fixed-degree Lattès packet cover lemma.** For the explicit degree-31 block system on \(L\), group all fixed-defect witnesses on one affine syndrome line by the induced \(131\)-block support system and prove an exact weighted charge in terms of realized \(67\)-subsets, with common-right-factor and duplicate-support deduplication.

For the project-wide route chosen by the Master Referee, this certificate should now be consumed by the finite frontier checker while theorem effort remains on `L-LIST-MINIMAL-CI-GJ-FIBER`.

## 8. Route to a full solve

This packet does not itself give a full solve. It closes a parallel guard and proves that genus-one Lattès packets are genuine finite obstructions, not arithmetic artifacts. A route to a full solve still runs through the scalar apolar complete-intersection/generalized-Jacobian theorem, with the verified Lattès packet entered as a mandatory exception-profile test.
