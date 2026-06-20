COUNTERPACKET

# W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT

## 1. Executive verdict

**Verdict.** The proposed model local-limit route is false with the declared
`Q_per`, under the only nonvacuous interpretation that “proper subgroup” means
**nontrivial proper subgroup**.  There is an exact same-field, rate-`1/2`,
`q<2^256` counterpacket in the required minimal scalar stratum

\[
\deg A=\sigma+1=5,\qquad \deg B=j=124,
\]

containing at least

\[
7{,}045{,}058{,}086{,}196{,}679
\]

full-coordinate listed words in one generalized-Jacobian fiber.  Every support
in the packet has trivial multiplicative stabilizer in the cyclic domain.  The
periodic-character quotient term declared in Role 03 is nevertheless less than
`1/882`, and the exact prize target is only `21`.

The counterpacket does **not** invalidate the minimal-CI/generalized-Jacobian
fiber equivalence.  It invalidates the proposed next step: replacing
configuration-level block relations by the quotient generated from periodic
**one-atom character pullbacks**.

**Confidence:** high (`0.99`) for the finite construction and route cut;
moderate (`0.75`) for the proposed repair in Section 10.

---

## 2. Formal official-rate counterpacket

Let

\[
q=21\cdot 2^{128}+1
 =7145929705339707732730866756067132440577.
\]

This is prime.  Let

\[
n=256,\qquad k=128,\qquad r=n-k=128,
\qquad \sigma=4,\qquad j=r-\sigma=124.
\]

Let `5` be the primitive element certified in Section 3 and put

\[
\omega=5^{(q-1)/256}
=3280346933828309263869282213710358210492\in\mathbb F_q.
\]

Then `omega` has order `256`.  Set

\[
H=\langle\omega\rangle\subset \mathbb F_q^\times,
\qquad K=\langle\omega^{64}\rangle,
\qquad |K|=4.
\]

For `a in Z/64Z`, write

\[
C_a=\omega^aK,
\qquad
P_{C_a}(X,Z)=\prod_{x\in C_a}(X-xZ)
              =X^4-\omega^{4a}Z^4.
\]

Choose the fixed defect

\[
D=\{1,\omega^{64},\omega,\omega^{65}\}.
\]

It occupies only the two `K`-cosets `C_0,C_1`, and it contains no pair
`{x,-x}`.  Define

\[
\mathcal A=
\left\{
S\subset\{2,3,\ldots,63\}:
|S|=30,\quad \sum_{a\in S}a\equiv15\pmod {64}
\right\}.
\]

For `S in mathcal A`, let

\[
T_S=D\ \cup\!\bigcup_{a\in S}C_a,
\]

and let its monic homogeneous locator be

\[
P_S(X,Z)=
\prod_{d\in D}(X-dZ)
\prod_{a\in S}(X^4-\omega^{4a}Z^4).
\tag{2.1}
\]

Then `|T_S|=4+30*4=124=j`.  Take

\[
S_0=\{3,4,\ldots,30,32,33\};
\qquad \sum_{a\in S_0}a\equiv15\pmod {64},
\]

put

\[
A_0(X,Z)=XZ^4,
\qquad B(X,Z)=P_{S_0}(X,Z),
\tag{2.2}
\]

and let `s` be the binary inverse-system element whose apolar ideal is

\[
I_s=(A_0,B).
\tag{2.3}
\]

### Theorem A

For the Reed-Solomon code `RS[F_q,H,128]` and syndrome `s` above:

1. `I_s` is a complete intersection with
   \[
   \deg A_0=5=\sigma+1,\qquad \deg B=124=j,
   \qquad \gcd(A_0,B)=1.
   \]
2. Every `T_S`, `S in mathcal A`, is a distinct full-coordinate
   representation of `s` of weight `j`.
3. No representation supported in `H` has weight below `j`; hence the packet
   lies in the required minimal listed stratum.
4. Every `T_S` has trivial stabilizer under multiplication by `H`.  Thus this
   is not merely a packet of periodic supports.
5. All `T_S` have exactly the same class in the generalized Jacobian for
   \[
   \Delta=[0]+4[\infty]=V(XZ^4).
   \]
6. The packet has exact size
   \[
   |\mathcal A|=7{,}045{,}058{,}086{,}196{,}679.
   \tag{2.4}
   \]
7. For the declared periodic quotient,
   \[
   |G_{\rm eff}|=256q^3,
   \qquad |\ker\pi_{\rm per}|=2q^2,
   \tag{2.5}
   \]
   and, for every target,
   \[
   \frac{N_{Q_{\rm per}}(\pi b)}{|\ker\pi_{\rm per}|}
   \le \frac{\binom{256}{124}}{2q^2}
   <\frac1{882}.
   \tag{2.6}
   \]
8. The exact finite target is
   \[
   T_q=\left\lfloor\frac q{2^{128}}\right\rfloor=21,
   \]
   so the minimal-stratum scalar list exceeds the target by more than
   `7.0*10^15`.

---

## 3. Field and domain certificate

The complete factorization is

\[
q-1=2^{128}\cdot3\cdot7.
\]

The single Pocklington base `5` satisfies

\[
5^{q-1}\equiv1\pmod q,
\]

and the residues for the distinct prime divisors of `q-1` are

\[
\begin{array}{c|c|c}
\ell&5^{(q-1)/\ell}\bmod q&
\gcd(5^{(q-1)/\ell}-1,q)\\ \hline
2&7145929705339707732730866756067132440576&1\\
3&6926644114561205365636538732032677850943&1\\
7&819384134099699443468573954699378903498&1.
\end{array}
\]

Since the certified factor `q-1` is larger than `sqrt(q)`, Pocklington proves
that `q` is prime.  The same three order tests show that `5` has order `q-1`.
Consequently `omega=5^((q-1)/256)` has exact order `256`; explicitly,

\[
\omega^{128}=-1,\qquad \omega^{256}=1.
\]

Thus `H` is a smooth cyclic evaluation domain of the required size.

---

## 4. Equality of all generalized-Jacobian restrictions

Write

\[
R_D(X,Z)=\prod_{d\in D}(X-dZ).
\]

For every `S in mathcal A`, equation (2.1) gives

\[
P_S=R_D\prod_{a\in S}(X^4-\omega^{4a}Z^4).
\]

### Infinity jet

Modulo `Z^4`, each block factor is `X^4`.  Hence

\[
P_S\equiv R_DX^{120}\pmod {Z^4},
\tag{4.1}
\]

independently of `S`.  Therefore every difference `P_S-P_{S_0}` is divisible
by `Z^4`.

### Value at zero

The product of the four defect points is

\[
\prod_{d\in D}d=\omega^{0+64+1+65}=\omega^{130}.
\]

Also

\[
\prod_{x\in C_a}x=-\omega^{4a}.
\]

Since there are `30` blocks and their label sum is `15 mod 64`,

\[
P_S(0,1)
=\omega^{130}\omega^{4\cdot15}
=\omega^{190},
\tag{4.2}
\]

again independently of `S`.  Thus `X` divides `P_S-P_{S_0}`.
Combining (4.1) and (4.2), and using `gcd(X,Z)=1`, gives

\[
P_S-P_{S_0}\in(XZ^4).
\tag{4.3}
\]

Therefore there is a homogeneous form `U_S` of degree `119` with

\[
P_S=A_0U_S+B.
\tag{4.4}
\]

In particular, `P_S` and `B` have the same restriction to
`Delta=V(A_0)`.  For any linear form `L_*` nonvanishing on `Delta`,

\[
\left[\left.\frac{P_S}{L_*^{124}}\right|_\Delta\right]
=
\left[\left.\frac{B}{L_*^{124}}\right|_\Delta\right]
=b_\Delta.
\]

Equivalently,

\[
\prod_{x\in T_S}\alpha_\Delta(x)=b_\Delta.
\]

This proves the exact generalized-Jacobian fiber condition.

---

## 5. Complete intersection, syndrome, and full-coordinate verification

The form `B=P_{S_0}` is monic, squarefree, and split over `H`.  Every one of
its roots is finite and nonzero.  Hence

\[
\gcd(XZ^4,B)=1.
\]

The quotient

\[
\mathbb F_q[X,Z]/(A_0,B)
\]

is therefore an Artinian complete intersection with socle degree

\[
5+124-2=127=r-1.
\]

Because `q>127`, ordinary binary apolarity and divided-power apolarity agree in
all relevant degrees.  Macaulay duality gives a nonzero binary form/functional
`s` of degree `127`, unique up to scalar, with exact annihilator

\[
I_s=(A_0,B).
\]

The `128`-row Vandermonde parity-check matrix on `H` has full row rank, so this
`s` is an actual syndrome of `RS[F_q,H,128]`.

For every `S in mathcal A`, (4.4) shows `P_S in I_s`.  The squarefree apolarity
lemma therefore places `s` in the span of the `124` Veronese/parity-check
columns indexed by `T_S`.  Since `124<128`, those columns are linearly
independent, so the coefficient vector on `T_S` is unique.

Suppose one of its coordinates, at `x in T_S`, were zero.  Then `s` would be
represented on `T_S minus {x}`, so its degree-`123` locator

\[
P_{S,x}=\prod_{y\in T_S\setminus\{x\}}(X-yZ)
\]

would lie in `I_s`.  But the degree-`123` component of the complete
intersection is

\[
(I_s)_{123}=A_0\,\mathbb F_q[X,Z]_{118},
\]

because `deg B=124`.  Thus `XZ^4` would divide `P_{S,x}`.  This is impossible:
all roots of `P_{S,x}` are distinct points of `H subset F_q^*`, so it has
neither the root `0` nor a root at infinity.  Hence every representation
coordinate is nonzero.

The same degree argument proves more.  Any `H`-split locator in `I_s` of degree
less than `124` would have to be divisible by `XZ^4`, which is impossible.
Thus there is no lower-weight representation on `H`.  The low generator
`A_0` itself is not an admissible full-coordinate locator: it has a quadruple
root at infinity and the root `0`, neither yielding a squarefree `H`-support.

This verifies the required minimal-stratum and full-coordinate conditions
without merely counting supports.

---

## 6. Exact packet cardinality

Let `c_ell(s;m)` denote the number of `ell`-subsets of
`{2,3,...,m}` whose element sum is `s mod 64`.  The exact finite recurrence is

\[
D_1(0,0)=1,
\]

and, on adjoining a label `a`,

\[
D_a(\ell,s)
=D_{a-1}(\ell,s)+D_{a-1}(\ell-1,s-a).
\tag{6.1}
\]

All sum arguments are modulo `64`.  Evaluating (6.1) through labels
`2,...,63` gives

\[
\sum_{s\in\mathbb Z/64\mathbb Z}D_{63}(30,s)
=\binom{62}{30}
=450883717216034179,
\]

and

\[
D_{63}(30,15)=7045058086196679.
\]

This is in fact the maximum sum bucket.  Distinct label sets give disjoint
unions of `K`-cosets, hence distinct locators and distinct full-coordinate
error vectors.  This proves (2.4).

The supplied verifier evaluates (6.1) using exact integers only.

---

## 7. The supports themselves are nonperiodic

Every nontrivial subgroup of the cyclic `2`-group `H` contains its unique
order-`2` element `-1=omega^128`.  The variable part

\[
\bigcup_{a\in S}C_a
\]

is invariant under multiplication by `-1`, because `-1 in K`.

By construction, however,

\[
D=\{\omega^0,\omega^{64},\omega^1,\omega^{65}\}
\]

while

\[
-D=\{\omega^{128},\omega^{192},\omega^{129},\omega^{193}\}.
\]

The latter four points lie in the excluded cosets `C_0,C_1`, and none belongs
to `D`.  Consequently `T_S` is not invariant under `-1`.  It therefore cannot
be invariant under any nontrivial subgroup of `H`.

Thus every support in the official packet has trivial subgroup stabilizer.
The surviving concentration is a configuration-level fixed-defect/block-trade
phenomenon, not literal periodicity of the supports.

---

## 8. Exact `G_eff` and `Q_per`

For

\[
\Delta=[0]+4[\infty],
\]

the coordinate algebra is

\[
H^0(\Delta,\mathcal O_\Delta)
\cong \mathbb F_q\times \mathbb F_q[t]/(t^4).
\]

After quotienting by diagonal scalars,

\[
G_\Delta
\cong \mathbb F_q^\times
       \times (1+t\mathbb F_q[t]/t^4).
\]

As `q` is prime and `q>3`, truncated logarithm identifies the second factor
with the additive group `F_q^3`.

Fix `x_0 in H`.  Up to inversion and nonzero scalar changes in the three
additive coordinates, the atom differences are

\[
\alpha_\Delta(x)\alpha_\Delta(x_0)^{-1}
\longmapsto
\left(
\frac{x}{x_0},
 x-x_0,
 x^2-x_0^2,
 x^3-x_0^3
\right).
\tag{8.1}
\]

The multiplicative projection of the generated subgroup is all of `H`.  The
three additive coordinates span `F_q^3`: if

\[
c_1x+c_2x^2+c_3x^3
\]

were constant on all `256` points of `H`, a degree-at-most-`3` polynomial would
have `256` roots after subtracting that constant, forcing all coefficients to
vanish.  Since `256` and `q` are coprime, the two projections imply

\[
G_{\rm eff}\cong H\times\mathbb F_q^3,
\qquad |G_{\rm eff}|=256q^3.
\tag{8.2}
\]

### Periodic characters

A character of `G_eff` can be indexed by

\[
(a,c_1,c_2,c_3)\in\mathbb Z/256\mathbb Z\times\mathbb F_q^3.
\]

Up to an irrelevant constant, its pullback to `H` has the form

\[
f(x)=\rho_a(x)\,
\psi(c_1x+c_2x^2+c_3x^3),
\tag{8.3}
\]

where `rho_a` is a multiplicative character of `H` and `psi` is a fixed
nontrivial additive character of the prime field.

Every nontrivial subgroup of `H` contains `-1`; hence a pullback is constant on
cosets of some nontrivial proper subgroup iff it is invariant under `x -> -x`.
From (8.3),

\[
\frac{f(-x)}{f(x)}
=(-1)^a\psi(-2c_1x-2c_3x^3).
\]

If `a` is odd, this cannot equal `1` for all `x`, because `-1` is not a
`q`-th root of unity.  If `a` is even, invariance forces the degree-`3`
polynomial `-2c_1X-2c_3X^3` to vanish on all `256` elements of `H`, so
`c_1=c_3=0`.  Conversely these conditions clearly suffice.  Therefore the
periodic-character subgroup is exactly

\[
\mathcal S_{\rm per}
=
\{(a,0,c_2,0):a\equiv0\pmod2,\ c_2\in\mathbb F_q\},
\]

with

\[
|\mathcal S_{\rm per}|=128q.
\]

The corresponding quotient has this order, and its kernel has order

\[
|\ker\pi_{\rm per}|
=\frac{256q^3}{128q}=2q^2.
\]

Since a quotient fiber contains at most all `binom(256,124)` supports,

\[
\frac{N_{Q_{\rm per}}(\pi b)}{|\ker\pi_{\rm per}|}
\le
\frac{\binom{256}{124}}{2q^2}.
\]

The exact integer check is

\[
882\binom{256}{124}<2q^2,
\]

which proves (2.6).  Meanwhile

\[
\frac{\binom{256}{124}}{|G_{\rm eff}|}
<\frac1{21^3 2^{136}}
\approx5.46\times10^{-47}.
\tag{8.4}
\]

Thus the declared quotient-conditioned term pays less than `0.00114` for a
fiber containing more than `7*10^15` full-coordinate members.

### Literal-subgroup edge case

If the phrase “proper subgroup” is read literally to include the identity
subgroup, every function is constant on its singleton cosets.  Then every
character is declared periodic, `Q_per=G_eff`, and the first term is the exact
fiber itself.  The theorem becomes tautological.  The only mathematically
useful reading is therefore “nontrivial proper subgroup,” which is the reading
used above.

---

## 9. Generator shear and other edge cases

An admissible generator change has the form

\[
B' = cB+A_0C,\qquad c\ne0.
\]

It leaves the ideal unchanged.  On `Delta`, `B'` restricts to `cB`; the scalar
`c` disappears in

\[
G_\Delta=H^0(\Delta,\mathcal O_\Delta)^\times/\mathbb F_q^\times.
\]

Hence `b_Delta`, the generalized-Jacobian fiber, every support representation,
and the full-coordinate property are all unchanged.  The packet is not a
choice-of-generator artifact.

Other required edge cases are also clean:

* `s` is nonzero because its inverse-system annihilator is a proper Artinian
  complete intersection with one-dimensional socle.
* `deg A_0=5<124=deg B`; there is no equal-degree ambiguity.
* Roots at infinity are handled homogeneously by the factor `Z^4`.
* The repeated infinity root is intentional and rules out `A_0` as a
  squarefree lower locator.
* The characteristic is larger than every relevant degree, so factorial and
  logarithm denominators `2,3` are invertible.
* Every packet locator is squarefree because its `124` roots are distinct
  elements of `H`.

---

## 10. Parameterized route cut

The official packet already exceeds the finite target.  The following family
also rules out every version of the proposed inequality with a fixed constant
`C_4` and a polynomial correction `P_4(n)`.

### Theorem B

Let `N=2^m >= 8`, set

\[
n=4N,\quad k=r=2N,\quad \sigma=4,
\quad j=2N-4,
\]

and take a prime field `F_q` with `n | q-1`.  Let `H=<omega>` have order `n`,
let `K=<omega^N>` have order `4`, and define

\[
D_N=\{1,\omega^N,\omega,\omega^{N+1}\}.
\]

Exclude the two `K`-cosets labelled `0,1`.  Put

\[
L=N/2-2.
\]

For at least one residue `s mod N`, the supports

\[
D_N\cup\bigcup_{a\in S}\omega^aK,
\qquad
S\subset\{2,\ldots,N-1\},
\quad |S|=L,
\quad \sum_{a\in S}a=s,
\]

form one full-coordinate minimal-CI generalized-Jacobian fiber of size

\[
M_N\ge \frac1N\binom{N-2}{N/2-2}.
\tag{10.1}
\]

Every one of these supports has trivial subgroup stabilizer.

Moreover,

\[
M_N\ge \frac{2^{N-3}}{N(N-1)},
\tag{10.2}
\]

so `M_N` exceeds every fixed polynomial in `n` for all sufficiently large
`N`.

#### Proof

The same block identity

\[
\prod_{x\in\omega^aK}(X-xZ)=X^4-\omega^{4a}Z^4
\]

shows that fixing the label sum fixes the value at zero and kills the first
three infinity jets.  Pigeonhole over the `N` possible sums proves (10.1).
The CI and full-coordinate arguments in Sections 4-5 apply verbatim.  Since
`H` is a cyclic `2`-group and the defect omits its negatives, the stabilizer is
trivial.

For (10.2), the coefficient in (10.1) is adjacent to the central coefficient
of row `N-2`.  It is at least half that central coefficient, while the central
coefficient is at least `2^(N-2)/(N-1)`.  Dividing by `N` gives (10.2).

For fixed `n`, primes `q congruent 1 mod n` can be made arbitrarily large by an
elementary order argument.  Given a bound `B`, take an integer `a` divisible by
all primes at most `B` and let `q` be any prime divisor of

\[
a^{n/2}+1.
\]

Then `q>B`, and the order of `a mod q` is exactly `n`, because `n` is a power
of `2`; hence `n | q-1`.

For these prime fields,

\[
|G_{\rm eff}|=nq^3,
\qquad |\ker\pi_{\rm per}|=2q^2.
\]

Now suppose constants `C_4` and a polynomial `P_4(n)` made the Role-03 bound
valid for every model instance.  Choose `N` so large that

\[
M_N>P_4(4N)+2.
\]

Then choose `q congruent 1 mod 4N` so large that

\[
\frac{\binom n j}{2q^2}<1,
\qquad
C_4\frac{\binom n j}{nq^3}<1.
\]

At the packet target, the proposed right side is less than `P_4(n)+2`, while
the left side is at least `M_N`, a contradiction.

Thus no quotient-conditioned local limit of the proposed form can hold with a
fixed `C_4` and polynomial `P_4`.

If `P_4` is allowed to be an arbitrary exponential function as large as the
entire support space, the statement is formally salvageable but mathematically
vacuous.

---

## 11. Exhaustive small-field discovery check

The structural seed was found by exact enumeration in

\[
\mathbb F_{257},\qquad H=\mu_{16},\qquad \sigma=4,\qquad j=8.
\]

For an exponent set `E subset Z/16Z`, the model fiber key is

\[
\left(
\sum_{e\in E}e\bmod16,
\sum_{e\in E}\omega^e,
\sum_{e\in E}\omega^{2e},
\sum_{e\in E}\omega^{3e}
\right).
\]

Enumeration of all `binom(16,8)=12870` subsets finds the collision

\[
\{0,1,4,5,8,9,12,13\}
\]

and

\[
\{2,3,6,7,10,11,14,15\}.
\]

Both are unions of two `mu_4`-cosets and have key `(4,0,0,0)`.  This exposed
the block identity used above.  The fixed-defect promotion then destroys every
support stabilizer while preserving the same configuration relation.

---

## 12. Parameter ledger and finite relevance

| Quantity | Exact value |
|---|---:|
| Field | `F_q`, `q=7145929705339707732730866756067132440577` prime |
| Field bit length | `133` |
| Domain | `H=<omega>`, `|H|=256` |
| `omega` | `3280346933828309263869282213710358210492` |
| Code dimension | `k=128` |
| Redundancy | `r=128` |
| Rate | `1/2` |
| Slack | `sigma=4` |
| Boundary weight | `j=r-sigma=124` |
| CI degrees | `(5,124)`, sum `129=r+1` |
| Socle/syndrome degree | `127=r-1` |
| Packet size | `7,045,058,086,196,679` |
| Prize target | `floor(q/2^128)=21` |
| Effective group | `|G_eff|=256q^3` |
| Periodic quotient kernel | `2q^2` |
| Declared quotient charge | `<1/882` |
| Raw occupancy | `<1/(21^3*2^136)` |
| Official caps | `q<2^256`, `k<=2^40` |

---

## 13. Bankable conclusions versus conditional conclusions

### Bankable

1. The explicit prime/domain certificate.
2. The exact fixed-defect block packet and its cardinality.
3. Equality of all restrictions to `Delta=[0]+4[infinity]`.
4. Existence of the CI syndrome with generator degrees `(5,124)`.
5. Full-coordinate status and absence of lower `H`-supported representations.
6. Trivial stabilizer of every packet support.
7. Exact computations `|G_eff|=256q^3` and
   `|ker pi_per|=2q^2`.
8. The finite threshold comparison.
9. The parameterized obstruction to every polynomial-error version of the
   proposed local limit.

### Conditional or definitional

1. The nonvacuous analysis assumes “proper subgroup” excludes the identity.
   Including the identity makes `Q_per=G_eff` and the theorem tautological.
2. The route cut concerns the exact `Q_per` declared in Role 03.  A larger,
   configuration-level block-profile charge can absorb this packet.
3. The parameterized contradiction rules out fixed `C_4` plus polynomial
   `P_4(n)` (indeed any correction asymptotically smaller than (10.1)); it does
   not rule out a deliberately exponential catch-all term.

---

## 14. Exact failure point

The failure is the implication

```text
all coherent exceptional Fourier mass
    comes from characters whose one-atom pullbacks are periodic on H.
```

That implication is false.  For `K=mu_4`, the **four-atom block product**

\[
\beta_K(cK)=\prod_{u\in K}\alpha_\Delta(cu)
\]

has all three additive jet coordinates equal to zero, because

\[
\sum_{u\in K}u^m=0\qquad (m=1,2,3).
\]

It depends only on the toric block label `c^4`.  This is a degree-`4`
configuration relation.  Most individual characters detecting the missing
jet directions are not periodic when pulled back along the one-atom map
`alpha_Delta`, yet they become perfectly coherent after atoms are assembled
into `K`-blocks.  The quotient `Q_per` is therefore formed at the wrong level.

---

## 15. Next exact lemma/construction

The next wall should be

```text
L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE
```

A useful exact statement is:

> For `Delta=[0]+sigma[infinity]`, cyclic `H`, and every subgroup
> `K<=H` of order `M>=sigma`, define
> \[
> \beta_K(cK)=\prod_{u\in K}\alpha_\Delta(cu).
> \]
> Prove that `beta_K` has no jet coordinates of degrees `1,...,sigma-1`
> and depends only on the toric coordinate `c^M`.  For every fixed defect
> `D`, charge exactly the support profile
> \[
> D\cup\bigcup_{cK\in S}cK
> \]
> by its finite subset-product count on `H/K`.  Then give a canonical,
> shear-invariant assignment to a unique maximal `(K,D)` so overlapping block
> systems are not double-counted, and prove a local limit only on the
> complement.

The first block-collapse assertion is already proved by

\[
\prod_{u\in K}(X-cuZ)=X^M-c^MZ^M
\equiv X^M\pmod {Z^\sigma}
\qquad(M\ge\sigma).
\]

The genuinely new work is the **canonical maximal block/defect assignment and
overlap bound**.  Without that configuration-level charge, another
one-atom-character quotient will fail for the same reason.

---

## 16. Route to a full solve

**Yes, conditionally.**  The generalized-Jacobian fiber formulation remains a
credible base, but the current `Q_per` local-limit route is closed.  A route to
a full scalar solve is:

1. replace output-character periodicity by exact configuration-level
   block-trade profiles;
2. canonically charge maximal block-plus-defect families without overlap;
3. prove a finite local limit for the residual configuration map;
4. sum the resulting charges across all CI strata.

The next exact lemma is
`L-MODEL-GJ-MAXIMAL-BLOCK-TRADE-CHARGE`, specifically the unique maximal
`(K,D)` assignment and its finite overlap theorem.
