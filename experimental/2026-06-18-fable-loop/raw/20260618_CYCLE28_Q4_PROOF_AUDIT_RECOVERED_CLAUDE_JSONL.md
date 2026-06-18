Code execution is disabled in this harness (permission denied), so I verified the algebra by hand symbolically rather than numerically. The computation is elementary enough to check rigorously on paper, and I did each step twice. Here is the audit.

---

PROOF (of the restricted-window `Q_4` facts and the `C2=O(p)` upper bound; not of anything above it)

## Field ledger

- `B = F_p`, `q_gen = p`. `F = F_{p^2} = B(α)`, `α^2 = θ` nonsquare, `q_line = p^2`. `q_chal` unused — kept separate from `q_gen`, `q_line`.
- `D = F_p`, `n = p`. `t = σ = 2`, `j = n−a = r−t = 3`. `η_reserve = σ/n = 2/n`, sub-reserve.
- `A = F[X]/E`, `E = X^2 + cX + d`, `ξ = [X]_E`, `u = [W]_E`, `b = [Bnum]_E`, `κ = u∧b`, `ℓ = [X^p−X]_E`.
- Off `R0` (`κ ≠ 0`); source-valid (`E` nonzero on `F_p`); separated (`gcd(E,E^τ)=1`); `c_b = −Q_E(b)/κ ≠ 0`.
- Conjugation `f̄ = f_0 − αf_1`, `Im(f)=f_1`, area form `⟨x,y⟩ = Im(x̄y) = x_0y_1 − x_1y_0`, with scaling law `⟨λx,λy⟩ = N(λ)⟨x,y⟩`.

## Proof / verification

I reconstructed the columns from Cycle 15/16 verbatim, `c_i(z) = s_i(z)u + t_i(z)b`:

```
s_1 = p1^1 − z q1^1,  t_1 = p2^1 − z q2^1
s_2 = p1^2 − z q1^2,  t_2 = p2^2 − z q2^2
s_3 = −1           ,  t_3 = z
s_0 = p1^0 − z q1^0,  t_0 = p2^0 − z q2^0
```

Writing `s_i = σ_i − zβ_i`, `t_i = γ_i − zδ_i`: `(β_1,β_2,β_0)=(q1^1,q1^2,q1^0)`, `β_3=0`; `(δ_1,δ_2,δ_0)=(q2^1,q2^2,q2^0)`, `δ_3=−1`.

**(Q1) Six-term expansion + degree-4 extraction.** In each of the six Cycle-25 terms the top `z`-part of `⟨s_i,s_j⟩` is `N(z)⟨β_i,β_j⟩` and of `⟨t_k,t_l⟩` is `N(z)⟨δ_k,δ_l⟩` (scaling law with `λ=z`). So the degree-4 part of `Q` is `N(z)^2 · Q_4` with

```
Q_4 = ⟨β_1,β_2⟩⟨δ_3,δ_0⟩ − ⟨β_1,β_3⟩⟨δ_2,δ_0⟩ + ⟨β_1,β_0⟩⟨δ_2,δ_3⟩
    + ⟨β_2,β_3⟩⟨δ_1,δ_0⟩ − ⟨β_2,β_0⟩⟨δ_1,δ_3⟩ + ⟨β_3,β_0⟩⟨δ_1,δ_2⟩.
```

`β_3=0` kills terms 2,4,6, leaving exactly the three Cycle-27 terms.

**I closed the "pending `q1`/`q2`" gap directly from the Cycle 20 wedge definitions** (`q1=(B0∧b)/κ`, `q2=(u∧B0)/κ`, `B0=λ_0 b`) using the banked expansion identity `(λ_0 x)∧y = λ_0^{(0)}(x∧y) − λ_0^{(1)} P_E(y,x)`, `λ_0^{(0)}=cd+dτ_1`, `λ_0^{(1)}=η=(c^2−d)+cτ_1+τ_2`:

- `(λ_0 b)∧b = −η P_E(b,b) = −η Q_E(b)` ⟹ `q1 = −(Q_E(b)/κ)η = c_b η`. So `(β_1,β_2,β_0)=c_b(c,1,w)`, `w=c^2−d`.
- `u∧(λ_0 b) = λ_0^{(0)}κ + η P_E(u,b)` ⟹ `q2 = λ_0^{(0)} + Pη`, `P=P_E(u,b)/κ`. Hence `q2^0=cd+Pw`, `q2^1=d+Pc`, `q2^2=P`.

This is the mechanical check Cycle 26/27 flagged as outstanding; it passes.

Substituting (scaling law on the `β`'s, `δ_3=−1` so `⟨·,δ_3⟩=±Im`):

```
Q_4 = N(c_b)·[ Im(c)·Im(q2^0) + Im(c̄w)·Im(q2^2) − Im(w)·Im(q2^1) ]
```

— reproducing the displayed Cycle 26 formula exactly.

**(Q3) `P`-cancellation and closed form.** The `P`-linear functional `φ(P)=Im(c)Im(Pw)+Im(c̄w)Im(P)−Im(w)Im(Pc)` is `B`-linear; `φ(1)=Im(c)Im(w)−Im(w)Im(c)=0` and `φ(α)=c_1w_0+(c_0w_1−c_1w_0)−w_1c_0=0`, so `φ≡0`. The cancellation is structural: `q2`'s `P`-part is `Pη`, collinear with `q1=c_b η`. The `P`-free remainder, in coordinates (`Im(w)=2c_0c_1−d_1`, `Im(cd)=c_0d_1+c_1d_0`):

```
Q_4/N(c_b) = Im(c)Im(cd) − Im(w)Im(d) = c_1^2 d_0 − c_0 c_1 d_1 + d_1^2.
```

And `Im(d)^2 − Im(c)Im(c̄d) = d_1^2 − c_1(c_0d_1−c_1d_0) = d_1^2 − c_0c_1d_1 + c_1^2 d_0`. **Identical.** Formula **VERIFIED**.

**(Q4) Locator identity.** For `a∈F_p`, `Im(E(a)) = c_1 a + d_1`. If `c∉B` (`c_1≠0`), `a^*=−d_1/c_1∈F_p` is the unique point with `E(a^*)∈B`, and
`c_1^2 E(a^*) = d_1^2 − c_0c_1d_1 + c_1^2 d_0 = Q_4/N(c_b)`, so

```
Q_4 = N(c_b)·Im(c)^2·E(−Im(d)/Im(c)),   Q_4=0 ⟺ E has an F_p-root ⟺ ∏_{a∈F_p}E(a)=N(ℓ)=0.
```

This is the **same** locator norm Cycle 24 attached to `D=N(ℓ)κ`. Two independent routes landing on `∏_{a∈F_p}E(a)` is strong corroboration of the column forms. **VERIFIED**.

**(Q5) Source-valid nonvanishing, both branches.**
- `c∉B`: source-valid ⟹ `E≠0` on `F_p` ⟹ `N(ℓ)≠0` ⟹ `E(a^*)≠0` ⟹ `Q_4≠0`.
- `c∈B` (`c_1=0`): `Q_4=N(c_b)Im(d)^2`; separatedness forbids `d∈B` (else `E^τ=E`), so `d_1≠0` ⟹ `Q_4≠0`.

So `separated + source-valid + off R0 + c_b≠0 ⟹ Q_4 ≠ 0` on **both** branches. **CONFIRMED**.

**(Q6) What is proved.** `N(z)=z_0^2−θz_1^2` is anisotropic, so `N(z)^2≢0` with no `B`-linear factor; `Q_4≠0` (scalar) ⟹ degree-4 part `≢0` ⟹ `deg Q=4` ⟹ `Q≢0`. The upper bound needs only the necessity direction `realized slope ⟹ Q(z)=0` (a solution forces column dependence), which holds unconditionally — no rank stratification required. A nonzero total-degree-`≤4` polynomial over `F_p` has `≤4p` zeros in `B^2`, so

```
C2 ≤ #{z∈F : Q(z)=0} ≤ 4p = O(p) = O(n).
```

The distinct split-cubic gate restricts realized slopes to a **subset** of `{Q(z)=0}`, so it can only shrink the count. The `Q≡0` counterpacket branch is therefore **empty** across the entire source-valid separated off-`R0` `t=2, j=3` window.

## Dependency list

- Cycle 15/16: column construction `c_i(z)=s_i u + t_i b`, fiber equation `L_z=ι−zμ=0`, Schwartz–Zippel safe side (`Q≢0 ⟹ C2≤4p`).
- Cycle 25: six-term Plücker/Laplace expansion of `Q`.
- Cycle 20: `q1=(B0∧b)/κ`, `q2=(u∧B0)/κ`, `B0=λ_0 b`, expansion identity, `c_b=−Q_E(b)/κ`; Cycle 12 `λ_0` coordinates `λ_0^{(0)}=cd+dτ_1`, `λ_0^{(1)}=η`.
- Cycle 24: `D=N(ℓ)κ`, `N(ℓ)=∏_{a∈F_p}E(a)` (cross-check, not load-bearing for `Q_4`).
- Necessity direction `realized ⟹ Q(z)=0` (Cycle 25), the only part used for the upper bound.

## Hidden assumptions

- The six-term Plücker expansion is taken from Cycle 25 with its stated signs. The `Q_4≠0`/`Q≢0` conclusion is **robust to any overall sign or nonzero-scalar error** in that expansion, since only nonvanishing is used.
- `λ_0^{(0)}, λ_0^{(1)}` and the expansion identity are taken from Cycle 12/20 banked forms; I re-derived `q1, q2` from them but did not re-derive them from the absolute raw `[W]_E`, `A0`, `B0` definitions.
- `O(p)` upper bound uses only necessity, so it does **not** depend on the Cycle 26 NONDEP rank stratification (that machinery is needed only for a converse/lower bound).
- Source-valid = `E` nonzero on `F_p`; separated = `gcd(E,E^τ)=1`; both `κ≠0` and `c_b≠0` assumed.
- Verification was by-hand symbolic (kernel execution was unavailable); a finite checker over `p=7,11,13` against raw Cycle 14/15 columns would convert "by-hand" to "machine-confirmed," but the algebra above is complete and self-contained.

## Rejected overclaims

- Not a corrected-reserve result (`η=2/n`, sub-reserve).
- No `q_gen`/`q_line` merge; `q_chal` untouched.
- No list-decoding, CA, MCA, line-decoding, curve-MCA, protocol, SNARK, or Proximity-Prize consequence.
- Does not assert the converse `Q(z)=0 ⟹ realized slope` (Cycle 25's rejected claim); only the upper bound is claimed.
- Does not claim `Q≡0` ⟹ `Θ(q_line)` anywhere — that branch is shown empty, not realized.
- Finite checks (if run) would be confirmation, never the proof.

## Verdict on Cycle 27

Cycle 27's `Q_4` derivation is **correct**: the formula `Q_4 = N(c_b)(Im(d)^2 − Im(c)Im(c̄d))`, the `P`-cancellation, the locator identity for `c∉B`, and source-valid nonvanishing on both branches all reproduce from the source/audit definitions. No bad sign, no missing hypothesis, no false source-validity implication, no `q2` failure, no source-valid `Q_4=0` example exists. Cycle 27's conservative `BANKABLE_LEMMA` self-label can be promoted: with the `q2` closed form now confirmed against the Cycle 20 wedge identity, the restricted `t=2, j=3` branch is a genuine **PROOF that `Q` is never identically zero and `C2=O(p)`** in this window.

## Route to a full solve

Yes — for this restricted line-incidence sub-problem the `t=2, j=3` wall is closed. The next exact lemma is the generalization the audits already name:

```
W-F1-AA-RES-T2-HIGHER-J-LOCATOR-NORM   (and the T3J2 companion)
```

Claim to prove: for `t=2` and arbitrary `j`, the top-degree coefficient of the slope-consistency determinant `Q` is a nonzero `B`-multiple of a power of the same Frobenius-locator norm `N(ℓ)=∏_{a∈F_p}E(a)`. The quotient `λ_0` has degree `j−1`, so the columns and the Plücker expansion scale accordingly; if the top symbol stays a power of `N(ℓ)`, source-validity kills `Q≡0` for the whole `t=2` family, giving `C2=O(p)` uniformly in the toy window. This remains strictly sub-reserve and yields no protocol, `q_gen`, MCA, or reserve consequence.

## Next exact wall

`W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL`: extract the top-degree coefficient of `Q` for `t=2, j=4` from the raw columns and decide whether it equals a nonzero `B`-scalar times `N(ℓ)^m` for some `m≥1`. Failure on a source-valid stratum is the precise seed for a growing-prime sub-reserve counterpacket; success extends the `C2=O(p)` proof to all `j` at `t=2`.
