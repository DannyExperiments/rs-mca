I'll start by reading the file index and the key project files.The index is large. Let me read the key state and wall files the prompt requires.Let me read the remaining required files and the Cycle 43 response itself.Let me read the Cycle 43 response, the banked lemmas, cuts, and the two earlier audits.Let me read the Cycle 43 actual response and the banked lemmas / cuts files.I have a thorough picture now. Let me verify one structural computation before writing, then produce deliverables. The key derivation I'll rely on: with $D=\mathbb F_p$, $L_D=X^p-X$ has $L_D'\equiv -1$, which makes the residue $\rho(T)=[I_S]_E$ collapse to a clean ratio. Let me confirm the main-term arithmetic against the banked regimes mentally — $\binom{p}{j}/p^{2(t-1)}$ at $(j,t)=(2,2),(3,2),(4,2)$ gives $O(1)$, $O(p)$, $p^2/24$. That matches all three banked regimes including the exact $1/24$. Good. Writing deliverables.I've now read the full state: the route board, active walls, banked lemmas, cuts, the Cycle 42/43 audits, and the Cycle 44 prompt. One note before the result: my actual available tooling here is read-only (I cannot write into `output_files/`), so as in Cycle 43 I'm delivering the four artifacts inline. Everything below is derived only from the mounted source and banked state, with ledgers `q_gen=p`, `B=F_p`, `F=F_{p^2}`, `q_line=p^2`, `q_chal` unused.

The headline: I can convert Cycle 43's heuristic skeleton into an exact identity, and collapse both of its subtargets into a single cancellation object. That is a real BANKABLE_LEMMA advance plus a sharper EXACT_NEW_WALL. It is not a full solve.

---

# cycle44_cosupport_result.md

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Ledger: `q_gen=p`, `B=F_p`, `F=F_{p^2}`, `q_line=p^2`, `q_chal` unused, `D=F_p`, `n=p`, `deg E = t = sigma`, `E` source-valid separated with no roots on `D`, cosupport size `j=n-a`. `A=F[X]/E`, `dim_F A = t`, `dim_{F_p} A = 2t`. `xi=[X]_E`, `b=[Bnum]_E in A`, `ell=[X^p-X]_E in A`. Off `R0={[W]_E wedge [Bnum]_E=0}`.

## Lemma 1 (Moment Identity for the cosupport residue). BANKABLE_LEMMA.

Because `D=F_p`, `L_D=X^p-X` and `L_D' = -1` identically. For `|S|=a`, `T=D\S`, `|T|=j`, the locator quotient residue `rho(T)=[I_S]_E` has the closed form

```text
rho(T) = - ell * Lambda(T)^{-1} * N(T),
Lambda(T) = [L_T]_E  (a unit in A, since gcd(L_T,E)=1),
N(T)     = sum_{d in D} w(d) L_T(d) (xi - d)^{-1}.
```

Proof. Lagrange + `L_D=L_S L_T` give `L_S'(s) = L_D'(s)/L_T(s) = -1/L_T(s)` for `s in S`. Hence `I_S/L_S = sum_{s in S} w(s)/(L_S'(s)(X-s)) = - sum_{s in S} w(s) L_T(s)/(X-s)`. Reduce mod `E`, use `[L_S]_E = ell*Lambda^{-1}` and `[L_S/(X-s)]_E=[L_S]_E (xi-s)^{-1}` (valid since `E(s)!=0`), then extend the `S`-sum to all of `D` (the `T`-terms die because `L_T(d)=0` on `T`). ∎

Expanding `L_T(X)=sum_{m=0}^{j}(-1)^m tau_m X^{j-m}`, `tau_m=e_m(T)`, gives the key separation into `T`-independent moments:

```text
N(T)      = sum_{m=0}^{j} (-1)^m tau_m M_{j-m},   M_i := sum_{d in D} w(d) d^i (xi - d)^{-1} in A,
Lambda(T) = sum_{m=0}^{j} (-1)^m tau_m xi^{j-m}.
```

Both `N` and `Lambda` are `F_p`-affine-linear in `(tau_1,...,tau_j)` with `T`-independent `A`-coefficients `M_i` and `xi^{j-m}`.

Consistency check (source-alignment). With `iota := -ell N`, `mu := b*Lambda`, the landing condition `rho in Fb` is exactly `iota wedge_F mu = 0`. Using `u=[W]_E` and `W=L_S Q_S+I_S` one gets `ell[Q_S]_E = u*Lambda + ell*N`, so `u*Lambda - ell[Q_S]_E = -ell N = iota`. This reproduces the Cycle 30 gate `iota = u*lambda - ell[Q_S]_E`, `mu=b*lambda` verbatim, and additionally eliminates `Q_S` in favor of the closed moments `M_i`. So Lemma 1 is the Cycle 30/43 object, in solved form.

## Lemma 2 (Exact landing identity; main term is the banked skeleton). BANKABLE_LEMMA.

Fix nontrivial `psi:F_p->C^*`, pair `A` with itself by `Tr_{A/F_p}`. For `z in F`, `eta in A` set `a_m(eta,z)=Tr(eta V_m(z))`, `V_m(z) := -ell M_{j-m} - z b xi^{j-m}`. Define the symmetric-function exponential sum

```text
S_j(c_1,...,c_j) := sum_{T in binom(F_p,j)} psi( sum_{m=1}^{j} c_m e_m(T) ).
```

Then the exact landing count is

```text
#Land = binom(p,j)/p^{2(t-1)}  +  E,
E = p^{-2t} * sum_{z in F} sum_{eta != 0} psi(a_0(eta,z)) * S_j( c(eta,z) ),
c_m(eta,z) = (-1)^m a_m(eta,z).
```

Proof. `mu(T)=b*Lambda(T) != 0` off `R0`, so each landing `T` has a unique slope `z`; `#Land=sum_z nu(z)`, `nu(z)=#{T: -ell N(T) = z b Lambda(T)}`. The detected form `G_z(T)=-ell N - z b Lambda` is affine-linear in `tau`, so `Tr(eta G_z(T)) = a_0 + sum_{m>=1}(-1)^m a_m e_m(T)`. Orthogonality on `(A,+)~=F_p^{2t}` and summing over `z in F` (`p^2` values) isolates `eta=0`, `S_j(0)=binom(p,j)`, giving the main term `p^2 binom(p,j)/p^{2t} = binom(p,j)/p^{2(t-1)}`. ∎

This promotes the Cycle 43 heuristic `#Land(j,t) ~ binom(p,j)/p^{2(t-1)}` from a route-organizing skeleton to the exact main term of a closed character identity, with an explicit error `E`. At `t=2` it reproduces the banked regimes exactly: `j=2 -> O(1)`, `j=3 -> O(p)`, `j=4 -> p^2/24 + ...` (since `binom(p,4)/p^2 = p^2/24 + O(p)`), matching Cycle 42's `N_split=p^2/24+O(p^{3/2})`.

## Reduction of the slope count. BANKABLE_LEMMA (conditional structure).

`N_split = #{z : nu(z)>0}`. Cauchy–Schwarz gives `N_split >= #Land^2 / M_2`, `M_2 := sum_z nu(z)^2 = #{(T,T') : rho(T)=rho(T') in Fb}`. Hence a first-moment error bound plus a second-moment (anticollision) bound yields the banked skeleton conclusion

```text
N_split  >~  min( q_line, binom(p,j)/p^{2(t-1)} ).
```

So the reserve lift is now reduced to two cancellation statements (next file), not to a vague equidistribution wall.

## Reserve-threshold check (why this is the right object). AUDIT.

With `delta=j/p` and natural-log entropy `H`, `ln binom(p,j) ~ pH(delta)` and `ln p^{2(t-1)} ~ 2t ln p`. For `t=sigma>=C n/log n` one has `2t ln p ~ 2Cp`, so the main term is `exp(p(H(delta)-2C))`. It exceeds `q_line=p^2` exactly when `H(delta) > 2C`, i.e. above the banked entropy/codimension threshold `sigma ~ H_2(delta) n/(2 log n)`. The threshold falls out of the identity automatically. This is the strongest source-grounded statement I can justify: the entropy threshold is not an analogy, it is the `eta=0` term of an exact identity.

---

# cycle44_next_lemma_or_falsifier.md

Status: EXACT_NEW_WALL / AUDIT.

The new wall, replacing `W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION` with a single concrete object:

```text
W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION
```

Both Cycle 43 subtargets (cancellation in `e_j({chi(xi-d)})` and quotient decoupling of `[I_{D\T}]_E`) are special cases of cancellation for the one sum `S_j(c)` over the structured covector cone `{c(eta,z) : eta != 0, z in F}`. The denominator-only character sum is the sub-cone where `c` comes from the `Lambda`-part alone; the decoupling is the coupling of the `N`-part (`M_i`) with the `Lambda`-part (`xi^{j-m}`) inside the same `c(eta,z)`. One object now governs both.

## Lemma L1 (first-moment cancellation). EXACT_NEW_WALL.

Show `|E| = o( binom(p,j)/p^{2(t-1)} )`, equivalently

```text
sum_{z in F} sum_{eta != 0} | S_j(c(eta,z)) |  =  o( q_line * binom(p,j) ).
```

Square-root cancellation `|S_j| <~ binom(p,j)^{1/2}` on the cone suffices when `binom(p,j) >> p^{4t}`, i.e. `H(delta) > 4C` (a factor-2-lossy threshold). Reaching the sharp threshold `H(delta) > 2C` needs better-than-square-root cancellation on the structured cone, or the second-moment route below.

## Lemma L2 (anticollision / second moment). EXACT_NEW_WALL. Sharp threshold.

Show

```text
M_2 = #{(T,T') : rho(T)=rho(T') in Fb}  <=  #Land + (1+o(1)) #Land^2 / q_line.
```

The diagonal contributes `#Land`; the off-diagonal is a paired symmetric-function exponential sum `S_{j,j}` (joint equidistribution of `(rho(T),rho(T'))`). L1 + L2 give, via Cauchy–Schwarz, `N_split >~ min(q_line, binom(p,j)/p^{2(t-1)})` — a full reserve lift conditional only on L2 (and the mild L1).

This is the smallest exact missing object. Recommended primary target: L2, because it hits the sharp entropy threshold directly and only needs L1 in its mild form.

## Where it can break (honest falsifier list). AUDIT.

The danger, exactly as in the banked low-`j` resonance strata (Cycle 11 `Q_S` sum-only; Cycle 13/14 `Ra/Rb`), is a resonance covector set `Rcal subset {c(eta,z)}` on which `sum_m c_m e_m(T)` degenerates (depends on `T` through too few symmetric functions, or is constant on the split locus). On `Rcal`, `S_j` is large and `E`/`M_2` can spike. The route is cut if and only if `Rcal` is large enough to force `M_2 >> #Land^2/q_line` for all source-valid growing families. Concretely:

```text
FALSIFIER: exhibit a source-valid growing family (t=sigma=Theta(n/log n), j=Theta(n))
with max_z nu(z) >= #Land / p^{1+epsilon}, i.e. a slope of huge multiplicity,
forcing N_split = o(min(q_line, binom(p,j)/p^{2(t-1)})).
```

If such collapse is generic, declare `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION` a ROUTE_CUT. If multiplicities stay `O(p^{o(1)})`, L2 holds and the lift goes through above the entropy threshold.

Do not bank: a proof of L1 or L2; positive reserve density; any corrected-reserve, generated-field, MCA/list/line/curve-MCA, protocol, SNARK, prize, or COUNTERPACKET statement. Banked here is only the exact identity (Lemma 1, 2) and the reduction of the wall to L2 (+L1).

---

# cycle44_finite_checker_spec.md

Status: EXPERIMENTAL / AUDIT.

Purpose: decide empirically whether L2 (anticollision) holds or whether multiplicity collapse cuts the route. Pure arithmetic in `A=F_{p^2}[X]/E` with `E in F_p[X]` of degree `t` (so `dim_{F_p} A = 2t`); no external libraries.

Procedure:
- Sweep `t=2`, `j=4,5,6,...`; primes `p in {23,31,43}`; use the banked source-valid family `E=X^2+alpha*X+1`, `alpha^2=-1` (needs `p=3 mod 4`: 23, 31, 43 all qualify), `b=X`, fixed arbitrary base anchors `w=w0+alpha*w1`.
- For each `j`-subset `T` of `D=F_p` (or Monte-Carlo sample when `binom(p,j)` is large), compute `rho(T)= -ell*Lambda(T)^{-1}*N(T)` directly from Lemma 1 (validate against direct `[I_S]_E` on a small sample).
- Record: `#Land`, `|Slopes|/p^2`, `max_z nu(z)`, the full multiplicity histogram, and `M_2 = sum_z nu(z)^2`.

Quantities to test:
```text
(a) #Land  vs  binom(p,j)/p^{2}        (exact main term at t=2; expect ratio -> 1).
(b) M_2    vs  #Land + #Land^2/p^2     (L2 predicted upper bound).
(c) max_z nu(z)                        (collapse falsifier if it grows like #Land/p^{1+eps}).
(d) |Slopes|/p^2 as j crosses j*       (j* solves binom(p,j)/p^2 = p^2; e.g. p=23 -> j* ~ 8).
```

Decision rule: if `|Slopes|/p^2` climbs toward a positive constant past `j*` and `max_z nu(z)` stays `p^{o(1)}`, L2 is supported and the underdetermined reserve route is live. If `|Slopes|/p^2` stalls at `O(1/p)` while `#Land` keeps growing, hunt the resonance covector set `Rcal` driving the collapse and pivot to ROUTE_CUT. Finite data are evidence/falsifiers only, never proof.

---

# cycle44_next_prompt.md

Target the single lemma, not the wall:

```text
Attack W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION, specifically Lemma L2
(second-moment / anticollision):
  M_2 = #{(T,T'): rho(T)=rho(T') in Fb} <= #Land + (1+o(1)) #Land^2/q_line,
with rho(T) = -ell*Lambda(T)^{-1}*N(T), N(T)=sum_m (-1)^m e_m(T) M_{j-m}, from
the Cycle 44 exact identity. Either prove L2 for a source-valid growing family
(t=sigma=Theta(n/log n), j=Theta(n), E separated, no roots on D=F_p), or
produce the falsifier: a source-valid growing family with a slope of multiplicity
>= #Land/p^{1+eps}. Keep q_gen/q_line/q_chal/B/F separate. Use the finite checker
to pre-screen the resonance covector set Rcal before committing to proof or cut.
```

---

Do I see a route to a full solve? Yes, a conditional one, and it is now concrete rather than vague. The exact identity (Lemma 1+2) shows `N_split` is governed by the first and second moments of the cosupport residue `rho(T)`, with the entropy threshold `H(delta)>2C` emerging as the `eta=0` term. A full reserve lift follows from one lemma: the anticollision bound L2 (with the mild first-moment bound L1). The next exact object to prove or falsify is L2 — equivalently, that no source-valid growing family forces a single slope to absorb a `p^{1+eps}` share of all landings. That is the real remaining mathematics, and it is a standard-shaped (if hard) pair-correlation cancellation statement for the structured symmetric-function exponential sum `S_j`, not an open-ended equidistribution conjecture.