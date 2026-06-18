I have enough to reconstruct the determinant and settle the structural questions. Let me give the analysis inline (tool-writing of files isn't needed here).

## Cycle 25 attack: `W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT`

Ledger respected: `B=F_p`, `F=F_{p^2}`, `D=F_p`, `t=σ=2`, `j=3`, `η_reserve=2/n` sub-reserve, off `R0` (`κ=u∧b≠0`), working the restricted line-incidence/residue calculation only. No `q_gen`, protocol, list/CA/MCA/SNARK claims.

### 1. Exact reconstruction of `Q(z_0,z_1)` (confirms the Cycle 16 audit-only algebra)

From Cycle 15, the fiber map `L_z(τ)=ι(τ)-zμ(τ)=0` has, in the `{u,b}` basis of `A=F[X]/E` (with `u=[W]_E`, `b=[Bnum]_E`), the four columns written as `c_i(z)=s_i u + t_i b`, each `F`-coordinate affine of degree 1 in `z`:

```text
c1: s_1=p1^1 - z q1^1,  t_1=p2^1 - z q2^1     (τ_1 column)
c2: s_2=p1^2 - z q1^2,  t_2=p2^2 - z q2^2     (τ_2 column)
c3: s_3=-1,             t_3=z                 (τ_3 column)
c0: s_0=p1^0 - z q1^0,  t_0=p2^0 - z q2^0     (constant column)
```

Identify `A≅B^4` via the ordered `B`-basis `{u, αu, b, αb}`, so column `c_i` has `B^4`-coordinates `(s_i^0, s_i^1, t_i^0, t_i^1)` where `x=x^0+αx^1`. Define the `B`-symplectic form on `F`:

```text
⟨x,y⟩ := x^0 y^1 - x^1 y^0   (B-bilinear, alternating).
```

`Q` is the `4×4` `B`-determinant. Generalized Laplace expansion along the top two rows (the `s`-block) against the complementary bottom two rows (the `t`-block) gives the closed six-term form:

```text
Q = ⟨s_1,s_2⟩⟨t_3,t_0⟩ - ⟨s_1,s_3⟩⟨t_2,t_0⟩ + ⟨s_1,s_0⟩⟨t_2,t_3⟩
  + ⟨s_2,s_3⟩⟨t_1,t_0⟩ - ⟨s_2,s_0⟩⟨t_1,t_3⟩ + ⟨s_3,s_0⟩⟨t_1,t_2⟩.
```

Sign check: column-pair signs are `(-1)^{i+j+1}` for `(1,2),(1,3),(1,4),(2,3),(2,4),(3,4) = +,-,+,+,-,+`. This is exactly the Plücker/`Tr(m_{12}Φ_0^τ)+…` structure the Cycle 16 audit listed as "audit-only." **It is now verified algebraically**, so the Cycle 16 trace/Gram criterion can be upgraded from AUDIT to a banked identity (the criterion is just the statement that the `(z_0,z_1)`-coefficients of this expression all vanish).

To make coefficients explicit, write `s_i=α_i - zβ_i`, `t_i=γ_i - zδ_i`. The only `z`-bookkeeping needed is the operator `m_z` (multiply-by-`z`, a `B`-linear endomorphism of `F`):

```text
⟨m_z x, m_z y⟩ = N(z)⟨x,y⟩,   ⟨m_z x, y⟩+⟨x, m_z y⟩ = Tr(z)⟨x,y⟩,
```

so each `⟨s_i,s_j⟩` and `⟨t_k,t_l⟩` is a `B`-quadratic in `(z_0,z_1)` with coefficients built from `⟨α_i,α_j⟩, ⟨α_i,β_j⟩, ⟨β_i,β_j⟩` (and the `γ,δ` analogues). Hence `Q∈B[z_0,z_1]`, total degree `≤4`, with at most `15` coefficient functions of the source data.

### 2. Are `Q≡0` and `det M≠0` compatible? — Yes; Cycle 24 does not cover this branch

`det M` and `Q` are determinants of **different matrices in different variables**:

- `det M = (c_b/κ^2)·D` is the `3×3` determinant of the coefficient frame expressing `(q1, p1-q2, p2)` in `{η, Q^{(0)}, Q^{(1)}}`. It lives in the **source data only** (no `z`). Cycle 24 gives `D=N(ℓ)κ=κ·∏_{a∈F_p}E(a)`, so for source-valid `E` (nonzero on `F_p`) off `R0`, `D≠0`, hence `det M≠0`. This is a statement about the *coefficient map* `τ↦[q1:p1-q2:p2]∈P^2(F)` being non-degenerate.
- `Q(z_0,z_1)` is the `4×4` *fiber-consistency* determinant in the **slope variable** `z`. `Q(z)=0` ⟺ slope `z` is realizable (the `B^3`-system `L_z(τ)=0` is consistent).

There is no algebraic implication `Q≡0 ⟹ D=0`: `D` is not a coefficient of `Q`, and `det M≠0` (coefficient-frame non-degeneracy) is logically independent of `Q≡0` (every fiber consistent). **Therefore the Cycle 24 emptiness argument — which is exactly the `D=0` route — does not touch this branch.** The hypotheses `Q≡0`, `D≠0`, `det M≠0`, `c_b≠0`, `E` source-valid, off `R0` are mutually consistent as a *system of constraints*; this branch is genuinely live and is not a hidden re-run of an excluded degeneracy.

So the answer to question 2: **compatible**, not forced into an already-excluded degeneracy.

### 3. If `Q≡0` is realized, the image is `Θ(p^2)=Θ(q_line)` — not auto-`O(p)`

This is the sharp and slightly uncomfortable consequence. The Cycle 16 bound `C2≤4p` used `Q≢0` + Schwartz–Zippel. The complement is unambiguous: `Q(z)=0 ⟺ z∈C2`, so

```text
Q≡0  ⟹  every z∈F is a realizable slope  ⟹  C2 = |F| = p^2 = Θ(q_line).
```

Hence the `Q≡0` branch **cannot be dismissed as `O(p)`**. If a source-valid growing-prime family with `Q≡0` exists, it is *by definition* a `Θ(q_line)` counterpacket seed in this sub-reserve toy window. So question 3 reduces entirely to question 4: is `Q≡0` realizable by source-valid data? I did **not** find a proof of realizability, and single-prime scans are forbidden as proof, so I do **not** promote a counterpacket. But the framing "`Q≡0 ⟹ still `O(p)`" is false — there is no split-distinct rescue once `Q≡0`.

This corrects a tempting over-reading of Cycles 18–20: the `Δ1==0`/rank-one normal form gives slope formulas `w^± = (±√δ_z - A/κ)/(2 c_b η)`, but "rank-one in `η`" governs the *coefficient* map, not the *fiber* map; it does not by itself collapse `C2` once `Q≡0`.

### 4. Smallest exact decider (the residual `EXACT_NEW_WALL`)

The branch is decided by a finite elimination certificate. Let the source parameters be `c,d∈F` (with `E=X^2+cX+d`), the `W`-data `W_{n-1},W_{n-2},W_{n-3}`, and `u,b∈F`. Using the banked closed forms (Cycle 20/21):

```text
q1 = c_b η,            c_b = -Q_E(b)/κ,   η=(c^2-d)+cτ_1+τ_2,
q2 = λ0^(0) + P η,     P = P_E(u,b)/κ,    λ0^(0)=cd+dτ_1,
p1 = λ0^(0) - (c+P)η - A/κ,
p2 = (Q_E(u)/κ)η - A'/κ,
A  = (ℓ∧b)Q0 - P_E(b,ℓ)Q1,   A' = (u∧ℓ)Q0 + P_E(u,ℓ)Q1,
Q0 = (W_{n-3}-d W_{n-1}) - W_{n-2}τ_1 + W_{n-1}τ_2,
Q1 = (W_{n-2}-c W_{n-1}) - W_{n-1}τ_1,
ℓ  = [X^p-X]_E = μ(ξ+c/2)+δ_c,
```

extract the `15` coefficients `Q_{kl}(c,d,W,u,b)` of `Q(z_0,z_1)=Σ_{k+l≤4}Q_{kl}z_0^k z_1^l` via the `m_z` identities of §1. Let

```text
I_Q          = ideal generated by the 15 coefficients Q_{kl},
I_valid      = source-validity ideal/conditions:
               ∏_{a∈F_p}E(a) ≠ 0 (E nonzero on F_p),
               gcd(E,E^τ)=1 (separated),
               κ≠0 (off R0),
               c_b≠0,
               det M = (c_b/κ^2)N(ℓ)κ ≠ 0.
```

The exact question is:

```text
Is the variety  V(I_Q) ∩ {source-valid}  empty?
```

Decision routes, in increasing strength:

- **Emptiness ⟹ PROOF that `C2=O(p)`** on the whole regime (combine with Cycle 16). Certificate: `1 ∈ I_Q + I_valid` after Rabinowitsch-clearing the `≠0` conditions (`κ,c_b,det M,∏E(a)` inverted). This is a Gröbner/saturation computation in `B[c,d,W_{n-1},W_{n-2},W_{n-3},u_0,u_1,b_0,b_1]` — small (≤9 parameters), doable in a CAS over `Q` then specialized mod `p`, treating `p` symbolically where possible.
- **Nonemptiness with a growing-`p` source-valid family ⟹ COUNTERPACKET** (`C2=Θ(q_line)`). Requires a *symbolic* family, not a single prime.

Checker specification (deterministic, no `q_gen` merge):

```text
input : p, c,d∈F_{p^2}, W_{n-1},W_{n-2},W_{n-3}∈F_{p^2}? (residue-line data), u,b∈F
filter: ∏_{a∈F_p}E(a)≠0 ; gcd(E,E^τ)=1 ; κ≠0 ; c_b≠0 ; det M≠0
build : Q0,Q1,η,p_i,q_i ; columns c1,c2,c3,c0 ; Q = 4×4 B-det
emit  : { degQ, [Q_{kl}], Q_identically_zero:bool, C2=#{z:Q(z)=0}, status }
flag  : Q_identically_zero AND source-valid  → candidate Θ(q_line) seed (NOT proof)
```

The cleanest sub-target inside `I_Q`: the **top symbol**. The degree-4 part of `Q` is `N(z)^2·det_B[d_1|d_2|d_3|d_0]` where `d_i` are the `z`-linear parts of the columns. Because `q1=c_b η` is rank-one in `η`, the `u`-components `β_i=q1^i=c_b·x_i` with `x_i∈{c^2-d,c,1}` satisfy `⟨β_i,β_j⟩=N(c_b)⟨x_i,x_j⟩`; these are **not** all zero when `c∉B` (the source-valid case), so the top symbol is generically nonzero and `Q≢0` generically. The wall is therefore precisely the *non-generic* source-valid locus where all `15` coefficients collapse simultaneously while staying off `R0` with `det M≠0`. That simultaneous collapse is the exact algebraic event to certify empty or populate.

### Primary label

```text
BANKABLE_LEMMA
```

Banked (restricted `D=F_p, t=σ=2, j=3`, off `R0`):

1. The six-term Plücker/Laplace identity for `Q` (verifies and upgrades the Cycle 16 audit-only trace/Gram criterion).
2. `Q(z)=0 ⟺ z∈C2`, and `Q≡0 ⟹ C2=p^2=Θ(q_line)` (so the `Q≡0` branch is *not* automatically `O(p)`).
3. Compatibility lemma: `det M=(c_b/κ^2)D` is a `z`-free coefficient-frame invariant independent of the `z`-fiber invariant `Q`; `Q≡0` does **not** imply `D=0`, so the Cycle 24 `D=0` emptiness does **not** cover this branch. The branch is genuinely live.
4. The decision reduces to a `≤15`-coefficient elimination ideal `I_Q` saturated against the source-valid `≠0` conditions, with a generic non-vanishing top symbol `N(z)^2 N(c_b)·det_B[x_i\,|\,δ\text{-data}]` showing `Q≢0` *generically*.

Residual `EXACT_NEW_WALL`: `W-F1-AA-RES-T2J3-QZERO-IDEAL-SATURATION` — decide emptiness of `V(I_Q)∩{source-valid, det M≠0}`.

Not banked: any `O(p)` proof on the live branch, any counterpacket, any corrected-reserve/`q_gen`/protocol/list/CA/MCA/line-decoding/SNARK consequence, any finite-scan-as-proof.

### Route to a full solve?

Yes, a concrete one. The full solve is now a single bounded elimination problem, not an open-ended search. Next exact step:

**Lemma to prove (or refute):** `I_Q + I_valid` saturated at `(κ·c_b·det M·∏_{a∈F_p}E(a))` contains `1`.

Construct it by: (a) symbolically computing the `15` coefficients `Q_{kl}` from the §1/§4 closed forms with `α^2=` the chosen `F/B` generator relation; (b) running a Gröbner saturation over `Q[c,d,W,u,b]` with `p` carried symbolically via `ℓ=μ(ξ+c/2)+δ_c`, `N(ℓ)=∏E(a)`; (c) if `1` is in the saturated ideal ⟹ **PROOF** the branch is empty and `C2=O(p)` for the whole `t=2,j=3` regime; if instead the saturation has a positive-dimensional component, read off a one-parameter `c(p),d(p),W(p)` family from that component and verify `Q≡0`, `det M≠0`, source-validity symbolically ⟹ **COUNTERPACKET** `C2=Θ(q_line)`. The generic non-vanishing top symbol in §4 makes emptiness (PROOF) the more likely outcome, but it is not yet decided.
