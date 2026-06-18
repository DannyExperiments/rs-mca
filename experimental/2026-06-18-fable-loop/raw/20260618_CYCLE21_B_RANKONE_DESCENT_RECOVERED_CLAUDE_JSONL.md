Both code tools are blocked in this harness (same constraint Cycles 19–20 worked under), so this is an analytic audit derived directly from the banked Cycle 12/14/20 multiplication identities, not a CAS run. I re-derived the load-bearing steps by hand.

---

## Primary label

```text
BANKABLE_LEMMA
```

Secondary: `EXACT_NEW_WALL` (a strictly sharper, explicit criterion below `dw∧dη==0`).

The exact question — "do the two descent equations force `dw∧dη==0`?" — has answer **No, not by themselves.** I prove `dw∧dη≡0` is governed by the Cycle‑20 gate `D` (as an explicit `2×2` resultant) together with an alignment of the leading `W`-data, and that the descent equations do not control that combination. This is exactly the "smaller exact implication involving the descent equations, `D`, `dw∧dη`, and the resultant structure" bullet.

## Ledger (kept separate)

`B=F_p`, `q_gen=p`; `F=F_{p^2}=B+αB`, `q_line=p^2`; `q_chal` unused. `D=F_p`, `n=p`. `t=σ=2`, `j=3`. `η_reserve=2/n`, sub-reserve. Off `R0={κ=u∧b=0}`. Restricted line-incidence/residue calculation only.

## Setup recap (source-checked, off `R0`)

With `c_b=-Q_E(b)/κ`, `A=(ℓQ)∧b`, `A'=u∧(ℓQ)`, `P=P_E(u,b)/κ`, `L_c=λ0^{(0)}=cd+d τ1`, `Q_u=Q_E(u)`, the banked forms give

```text
q1 = c_b η,                       q2 = L_c + P η,
p1 = L_c - (c+P)η - A/κ,          p2 = (Q_u/κ)η - A'/κ,
w^± = (±√δ_z - A/κ)/(2 c_b η),    δ_z ∈ B[τ1,τ2] on Δ1==0.
```

I take the audit's proxy `dw∧dη==0` (the `F`-valued 2-form, `η=(c^2-d)+cτ1+τ2`) as the definition of `dim_B Im(w)=1`, and work with the wedge operator `L(f):=[df∧dη]=∂_1 f - c∂_2 f`, which is an `F`-linear derivation with `L(η)=0` (so `L` kills any function of `η`).

## Lemma A — differential reduction (exact identity)

Because the denominator of `w^±` is `2c_b η`, `d(2c_bη)∧dη=0`, so the quotient rule collapses:

```text
2 c_b η · (dw^± ∧ dη) = ±(1/(2√δ_z)) (dδ_z∧dη) - (d(A/κ)∧dη).
```

Writing `J_δ:=L(δ_z)`, `J_A:=L(A/κ)` (constant, since `A/κ` is affine), this is

```text
dw^± ∧ dη = 0   ⟺   J_δ = ±2√δ_z · J_A.            (A)
```

Proof: `w=N/M`, `M=2c_bη`, `N=√δ_z - A/κ`; `dw∧dη=(1/M)dN∧dη` since `dM∧dη=0`; and `d√δ_z=dδ_z/(2√δ_z)`. ∎

Requiring **both** branches `w^+,w^-` to collapse (the condition relevant to `C2`, since both quadratic roots are realized) forces, by adding/subtracting (A) with `√δ_z≠0`,

```text
dw^+∧dη ≡ 0  and  dw^-∧dη ≡ 0   ⟺   J_δ = 0  and  J_A = 0.   (A')
```

## Lemma B — collapse reduces to two scalar gates

From the closed forms, `δ_z = C_2 η^2 + 2(c+2P)(A/κ)η - 4c_b(A'/κ)η + (A/κ)^2` with `C_2` constant in `τ`. Applying `L` (Leibniz, `L(η)=0`):

```text
J_δ = [2(c+2P)J_A - 4 c_b J_{A'}] η + 2 J_A (A/κ),   J_{A'}:=L(A'/κ).
```

Hence `J_A=0 ⟹ J_δ=-4c_b J_{A'}η`, and with `c_b≠0`, `η≢0`:

```text
{J_δ=0 and J_A=0}   ⟺   {J_A=0 and J_{A'}=0}.            (B)
```

So **both-branch collapse `⟺ J_A=0 ∧ J_{A'}=0`**: i.e. both `A/κ=(ℓQ)∧b/κ` and `A'/κ=u∧(ℓQ)/κ` are affine functions of `η`.

## Lemma C — the gate `D` is the resultant of the two collapse gates

From Cycle 12 (`D=F_p`): `Q0=(W_{n-3}-dW_{n-1})-W_{n-2}τ1+W_{n-1}τ2`, `Q1=(W_{n-2}-cW_{n-1})-W_{n-1}τ1`, so `L(Q0)=-(W_{n-2}+cW_{n-1})`, `L(Q1)=-W_{n-1}`. With `A/κ=((ℓ∧b)Q0-P_E(b,ℓ)Q1)/κ`, `A'/κ=((u∧ℓ)Q0+P_E(u,ℓ)Q1)/κ`, set `m:=W_{n-2}+cW_{n-1}`, `w_1:=W_{n-1}`:

```text
κ J_A   = -(ℓ∧b) m + P_E(b,ℓ) w_1,
κ J_{A'} = -(u∧ℓ) m  - P_E(u,ℓ) w_1.
```

These are two `F`-linear forms in `(m,w_1)`. A nonzero `(m,w_1)` annihilating both exists **iff** the determinant vanishes, and that determinant is exactly the Cycle‑20 gate:

```text
det [ (ℓ∧b)   -P_E(b,ℓ) ;  (u∧ℓ)   P_E(u,ℓ) ]
   = (ℓ∧b)P_E(u,ℓ) + P_E(b,ℓ)(u∧ℓ) = D.
```

Therefore, **assuming `W_{n-1}≠0` (so `(m,w_1)≠0`):**

```text
dw∧dη ≡ 0 (both branches) ⟺ J_A=J_{A'}=0 ⟺ D=0 AND (W_{n-2}+cW_{n-1} : W_{n-1}) on ker(I,II).
```

In particular `dw∧dη≡0 ⟹ D=0`, and `D≠0 ⟹ dw∧dη≢0`. ∎

## Direct answer to the exact question

**No.** The descent equations `Im_α(p1+q2)=0`, `Im_α(det P)=0` (which are conditions on the `τ`-dependence of `δ_z`) do **not** force `dw∧dη≡0`. By Lemma C, collapse is forced exactly by the `τ`-independent gate `D=0` *plus* alignment of the leading `W`-data with `ker(I,II)`. Since `D` depends only on `(E,u,b,ℓ)` while the descent conditions can be satisfied by tuning the lower coefficients of `W` (which move `L_c,A/κ,A'/κ,δ_z` but leave `D` fixed), the two are independent conditions. Hence:

- The forcing implication asked for is **false as stated** — collapse is a non-generic degeneration that must be *forced by `D`*, not by descent.
- Conversely, `dw∧dη≡0` is **not necessary for `C2=O(p)`**: on `D≠0` Cycle 16's `Q≢0 ⟹ C2≤4p` already gives `O(p)` even though `dw∧dη≢0`. So `C2=O(p)` holds on `D≠0` by the curve-in-`(z_0,z_1)` mechanism, not by `η`-functional-dependence.

This relocates any possible `Θ(q_line)` seed entirely onto the gate locus `D=0`.

## Secondary EXACT_NEW_WALL (strictly below `dw∧dη==0`)

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT
On Δ1==0 ∧ D==0, off R0, with W_{n-1}≠0:
  dw∧dη≡0  ⟺  (W_{n-2}+c W_{n-1} : W_{n-1})  ∝  ker[ (ℓ∧b), -P_E(b,ℓ) ; (u∧ℓ), P_E(u,ℓ) ].
Counterpacket seed = source-valid (E,Bnum,W) with Δ1==0, D=0, Q≡0, W_{n-1}≠0,
leading data OFF that kernel line, and enough distinct D-split cubics; there
dw∧dη≢0 is the precise non-collapse seed for C2=Θ(p^2)=Θ(q_line).
```

## What is banked vs not

Bank (proven, exact, off `R0`, restricted `D=F_p,t=σ=2,j=3`): Lemma A (differential reduction `dw^±∧dη=0 ⟺ J_δ=±2√δ_z J_A`); Lemma B (`both-branch collapse ⟺ J_A=J_{A'}=0`); Lemma C (`D` is the `2×2` resultant of the two collapse gates; `dw∧dη≡0 ⟹ D=0`; `D≠0 ⟹ dw∧dη≢0`, given `W_{n-1}≠0`); and the observation that `dw∧dη≡0` is sufficient-but-not-necessary for `C2=O(p)`.

Do **not** bank: collapse or non-collapse on `D=0`; nonemptiness of the seed stratum (not exhibited — no scans); any `C2` bound on `Δ1==0∧D=0`; any `Θ(q_line)` counterpacket; anything at/above corrected reserve; any `q_gen`, protocol, list/line/curve-decoding, CA, MCA, or SNARK consequence.

## Forbidden-upgrade compliance

No Prize solve/disproof; `η=2/n` stays sub-reserve; `q_gen`/`q_line` separate; no protocol denominator saving; no list/line/CA/MCA upgrade; no internet; no finite scan cited as proof (none run).

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Not a full Prize solve — this is the sub-reserve `η=2/n` toy window, so even a clean resolution closes only restricted `t=2,j=3` local F1. But there is a concrete, code-free route to closing the window, now sharply localized by Lemmas A–C. The next exact lemma is the **`D=0` resonance compatibility test**:

```text
NEXT EXACT LEMMA (finite symbolic; needs a CAS but no asymptotics):
On D==0, parametrize ker(I,II) by a single F-direction (m:w_1)=κ_dir.
Impose the descent equations Im_α(p1+q2)=Im_α(det P)=0 as identities in B[τ1,τ2],
treating (W_{n-1},W_{n-2},W_{n-3}, c,d, u, b, ℓ) as source unknowns with
E separated/aperiodic, [Bnum]_E≠0, W_{n-1}≠0. Then decide:
  (a) does Δ1==0 ∧ D==0 force (W_{n-2}+cW_{n-1}:W_{n-1}) ONTO κ_dir
      (=> dw∧dη≡0, window closed, C2=O(p)); or
  (b) is there a source-valid solution OFF κ_dir with Q≡0 and ≥cp^2 distinct
      D-split cubics realized (=> the first Θ(q_line) seed)?
Equivalently: compute Res_{τ_3}(Δ0,Δ1) and test whether, modulo (I),(II) and D=0,
it carries the η-rank-one factor; this is a finite Gröbner/resultant problem in
B[τ1,τ2] with the leading-data alignment as the single decisive coordinate.
```

This is the single decisive construction: it either banks `C2=O(p)` for the full `t=2,j=3` window or exposes the first source-valid `Θ(q_line)` seed — and Lemma C has reduced "where to look" from the whole `Δ1==0` surface to the explicit one-coordinate alignment test on `D=0`.
