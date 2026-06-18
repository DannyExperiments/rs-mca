Both `Write` and code execution are denied in this harness — the same operational wall the Cycle 16/17 audits recorded (`output_files/` could not be produced; deliverables were given inline). I cannot create files under `output_files/` or run the scanner, so per the established fallback I deliver the research artifact inline. The mathematical content below is what matters, and it does not depend on execution: it is a hand proof read directly off the banked Cycle 14/15 column construction.

---

# Cycle 18 Research Artifact — W-F1-AA-RES-T2J3-RANK-DET-SPLIT

## Exact status label

```text
EXACT_NEW_WALL   (primary)
BANKABLE_LEMMA   (secondary: the monicity lemma + safe-side O(p), below)
```

I did **not** reach `PROOF` (full collapse) or `COUNTERPACKET`. I made the largest source-valid leap available without computation: a structural lemma that removes the `τ3` variable from the dangerous stratum and reduces the residual wall from a 3-variable surface problem to a single 2-variable rational-map image-dimension question.

## Parameters / ledger (kept strictly separate)

```text
B = F_p,        q_gen  = p
F = F_{p^2},    q_line = p^2
q_chal          unused
B-subfield = F_p ;  F = ambient extension ;  tower F/B degree 2
D = F_p,        n = p
t = sigma = 2,  j = n-a = r-t = 3,  a = n-3,  k = n-5
rho = k/n = (n-5)/n
eta = sigma/n = 2/n   (SUB-RESERVE)
quotient order = 3 (monic cubic co-support L_T) ; arity = 2-term line MCA test
Work off R0 = { kappa := wedge([W]_E,[Bnum]_E) = 0 }.
delta : T2J3-slice agreement radius (not invoked).
Source deps (all internal/banked): Cycle 9 W=L_S Q_S+I_S ; Cycle 12 closed form
Q_S(e1,e2) indep. of e3 ; Cycle 13 base-quadric split Delta=Delta0+alpha Delta1 ;
Cycle 14/15 columns + affine forms p_i,q_i ; Cycle 16 safe-side bound.
No external (Crites–Stewart/ABF) import is used.
```

## The new bankable lemma (monicity in `τ3`)

Off `R0`, `{[W]_E, b}` (with `b=[Bnum]_E`) is an `F`-basis of `A=F[X]/E`. Write the landing 2-form in that basis (the determinant of coordinates, so leading coefficient is a literal `1`, not the code's un-normalized `κ`-scaled `wedge`; the two differ by the nonzero scalar `κ∈F` off `R0` and have the **same zero locus**):

```text
iota = A0 - tau3 [W]_E = (p1 - tau3)[W]_E + p2 b,
mu   = B0 - tau3 b     = q1 [W]_E + (q2 - tau3) b,
Delta(tau) := wedge_{W,b}(iota, mu)
            = (p1 - tau3)(q2 - tau3) - p2 q1,
```

where `p_i,q_i` are the Cycle-14 affine forms in `(tau1,tau2)`.

**Lemma (monicity).** As a polynomial in `τ3`, `Delta` is monic of degree exactly 2 with leading coefficient `1 ∈ B`. Consequently, splitting `Delta = Delta0 + α Delta1` with `Delta0,Delta1 ∈ B[τ1,τ2,τ3]`:

```text
deg_{tau3} Delta0 = 2  (monic, leading coeff 1),
deg_{tau3} Delta1 <= 1.
```

**Proof.** `[L_T]_E = ν(τ1,τ2) − τ3·1_A` because `L_T = X^3 − τ1 X^2 + τ2 X − τ3` and only the constant term carries `τ3`, linearly with coefficient `−1`; reduction mod the monic quadratic `E` preserves this. Hence `iota,mu` are affine in `τ3` with `τ3`-coefficients exactly `−[W]_E, −b` (this is precisely the identity `affine_pq` asserts as a fail-loud check in the Cycle 17 scanner: `iota − (A0 − τ3[W]_E)=0`, `mu − (B0 − τ3 b)=0`). The `τ3^2` coefficient of `Delta` is `wedge_{W,b}(−[W]_E, −b) = wedge_{W,b}([W]_E,b) = 1` in the `{W,b}`-basis. The leading coefficient is therefore `1∈B`; splitting over `F=B⊕αB` sends a `B`-coefficient `1` entirely to `Delta0`, so `Delta1` has zero `τ3^2`-coefficient. ∎

This is bankable (no experiment, no imported theorem, no reserve claim, no ledger merge).

## Safe-side corollary (re-derives and tightens Cycle 13/16)

Landing locus `L = {Delta = 0} = {Delta0 = 0} ∩ {Delta1 = 0} ⊂ B^3`.

**Corollary.** If `gcd(Delta0, Delta1) = 1` in `B[τ1,τ2,τ3]`, then `L` is at most a curve, `#L = O(p)`, and `C2 = O(p) = O(n)`.

**Proof.** Coprime `Delta0,Delta1` define surfaces with no common component, so `L` has dimension `≤ 1`; with `deg Delta0 = 2`, `deg Delta1 ≤ 2` (each `p_i,q_i` affine in `(τ1,τ2)`), Bézout bounds `deg L ≤ 4`, giving `#L ≤ O(p)` points over `F_p`. Each landing point yields one slope `z=(p1−τ3)/q1`, so `C2 ≤ #L = O(p)`. ∎

This recovers the Cycle 16 `C2 ≤ 4p` regime intrinsically (the "`Q≢0`" condition is implied by `gcd=1`), without the AUDIT-only trace/Gram criterion.

## Sharpened exact wall (the leap on lens 3)

The only way to leave the `O(p)` regime is `gcd(Delta0,Delta1) ≠ 1` (this is exactly the Cycle 13 resonance `Ra/Rb`, now given intrinsically). The monicity lemma **controls that common factor**:

```text
g := gcd(Delta0, Delta1),  g nonconstant.
Since deg_{tau3} Delta1 <= 1:
  either  Delta1 ≡ 0           (Delta = Delta0 in B[tau], full monic quadric surface),
  or      deg_{tau3} g = 1,    g = s·tau3 + h,  s,h in B[tau1,tau2], deg s<=1, deg h<=2.
```

In the second case the resonance surface is the **graph** `τ3 = −h/s`, so substituting into the slope formula eliminates `τ3` entirely:

```text
z(tau1,tau2) = (p1 - tau3)/q1 = (p1 + h/s)/q1   on the resonance graph,
```

a rational map `B^2 ⇢ F` of bounded degree. Equivalently (Cycle 14 slope quadratic), every landing slope is a root of

```text
q1 z^2 - (p1 - q2) z - p2 = 0,
```

so the slope map factors through the coefficient map

```text
mu_coef : (tau1,tau2)  |-->  [ q1 : (p1 - q2) : p2 ]  in  P^2(F).
```

**Therefore the residual wall reduces to one image-dimension question:**

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT (sharpened):
On a source-valid resonance stratum (gcd(Delta0,Delta1) != 1), does the
2-variable map  (tau1,tau2) |-> z  (equivalently mu_coef into P^2(F))
have 1-dimensional image  =>  C2 = O(p) = O(n)  (collapse),
or generically-finite (0-dim) fibers  =>  C2 = Theta(p^2) = Theta(q_line)?
```

This is a strict reduction: from "count slopes on a `Θ(p^2)`-point surface in `B^3`" to "is a fixed bounded-degree rational map `B^2 ⇢ F` fibered by curves." It is decidable by one Jacobian/resultant identity (`dz ∧ d(anything) ≡ 0` modulo the resonance relations, i.e. functional dependence of `z` on a single coordinate), which is exactly what the unrun Cycle 17 scanner would sample but which a symbolic check can settle outright.

## What is NOT proved (explicit)

- No proof that the resonance slope map has 1-dim image (no collapse proof) and no `C2=Θ(q_line)` counterpacket. The dichotomy above is open.
- No proof of `conj:B`, no Proximity-Prize claim; source hypotheses undischarged.
- Nothing at or above corrected reserve: `eta=2/n` is sub-reserve, so **even a `Θ(q_line)` counterpacket here would not refute corrected MCA.**
- No `q_gen` statement (the `Θ(p^2)` would be a `q_line` phenomenon; never paid into `q_gen`).
- No CA / MCA / list-decoding / line-decoding / protocol / SNARK consequence; the T2J3 object is a curve-/line-incidence count and no conversion is claimed.
- The Cycle 16 trace/Gram criterion is still not verified; not used here.
- The Cycle 15 forced-`Ra` `p=7` datum (`C2≤6`) leans against a counterpacket but is single-prime, sub-reserve EXPERIMENTAL evidence and is **not** promoted.

## Other lenses (brief)

- Lens 1 (full positive): blocked exactly on the image-dimension question above.
- Lens 2 (full negative): not constructed; the only finite evidence argues against it.
- Lens 4 (reserve): ledger is `eta=sigma/n=2/n`, sub-reserve. The open sub-question that decides relevance: does the `gcd(Delta0,Delta1)≠1` resonance obstruction persist as `sigma` grows (`deg E = t = sigma`), where the analogous landing form is monic of degree `sigma` in the top symmetric variable? If yes, the wall is on-route; if it is special to `sigma=2`, it is a toy.
- Lens 5: T2J3 line-incidence ≠ line-decoding ≠ CA; kept separate, no conversion used.
- Lens 6: for this wall the single blocking dependency is the (currently un-runnable) symbolic image-dimension check, not an imported theorem; Paper D's Crites–Stewart/ABF conditionality is orthogonal here.

## Exact next step

Settle the image dimension of `mu_coef:(τ1,τ2)↦[q1:(p1−q2):p2] ∈ P^2(F)` on each source-valid resonance stratum, in two equivalent forms:
1. Symbolic: compute `J = ∂(z, w)/∂(τ1,τ2)` for an auxiliary coordinate `w`, or the resultant `Res_{τ3}(Delta0,Delta1)` and its factor structure; `image is a curve ⟺ z is functionally dependent on one coordinate ⟺ a fixed `≤O(1)`-degree relation `R(z)≡0` holds`.
2. Finite (when execution is restored): run the banked Cycle 17 `rank_det_split_scanner.py` on `p=7,11,13,17,19,23`, filtered to `Delta1≡0` and `deg_{τ3}gcd=1` strata separately, watching `C2/p^2`. Single primes remain EXPERIMENTAL; only a growing family with `C2/p^2` bounded below would be a counterpacket candidate (sub-reserve).

---

```text
Do you see a plausible route to a full solve from here? YES.
If YES, what is the next exact lemma or construction:
Prove the RESONANCE SLOPE-MAP COLLAPSE LEMMA — on every source-valid stratum
with gcd(Delta0,Delta1) != 1 (D=F_p, t=sigma=2, j=3, off R0), the rational
slope map (tau1,tau2) |-> z = (p1 + h/s)/q1  [resp. the quadric case Delta1==0]
has 1-dimensional image, equivalently the three F-affine forms q1, (p1-q2), p2
satisfy a fixed bounded-degree functional dependence forcing
#image(mu_coef) = O(p). This yields C2 = O(p) on all resonance strata and,
combined with the monicity lemma's safe side, closes the corrected local F1
T2J3 statement in this window (still sub-reserve eta=2/n). The contrapositive
construction — exhibiting source-valid q1,(p1-q2),p2 with generically-finite
mu_coef over a growing-p family — is the exact counterpacket to build if the
collapse fails.
```
