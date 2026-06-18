# Cycle 26 attack: `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`

Ledger respected: `B=F_p` (`q_gen=p`), `F=F_{p^2}` (`q_line=p^2`), `q_chal` unused, `D=F_p` (`n=p`), `t=sigma=2`, `j=3`, `eta_reserve=2/n` sub-reserve, off `R0` (`kappa=u∧b≠0`). Restricted line-incidence/residue calculation only; no `q_gen`/protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK claim.

I worked the realized-slope condition `c_0(z) ∈ span_B(c_1(z),c_2(z),c_3(z))` directly, in the `F`-plane model. The result corrects a gap in how Cycle 25's audit framed the rank-drop strata, and isolates a single explicit scalar obstruction.

## Setup I use

Off `R0`, `{u,b}` (`u=[W]_E`, `b=[Bnum]_E`) is an `F`-basis of `A=F[X]/E`, so the `F`-linear iso `A≅F^2`, `c=su+tb ↦ (s,t)`, carries each column to a vector `v_i(z)=(s_i(z),t_i(z))∈F^2`, and `F^2≅B^4` via `{1,α}`. From Cycle 25/20:

```text
v_1=(p1^1 - z q1^1,  p2^1 - z q2^1),   v_2=(p1^2 - z q1^2,  p2^2 - z q2^2),
v_3=(-1, z),                           v_0=(p1^0 - z q1^0,  p2^0 - z q2^0),
q1 = c_b·η,  η=(c^2-d)+cτ_1+τ_2  ⟹  q1^1=c_b c, q1^2=c_b, q1^0=c_b(c^2-d).
```

Realizable slope `z` ⟺ `v_0(z) ∈ span_B(v_1(z),v_2(z),v_3(z)) ⊆ F^2≅B^4`. Write `⟨x,y⟩:=Im_α(x̄y)` for the alternating `B`-area form (so `⟨x,y⟩=0 ⟺ x,y` are `B`-proportional). Let `C(z)=[v_1|v_2|v_3]∈Mat_{4×3}(B)`.

## The rank stratification, done correctly

Define the two strata by the `3×3` minors of `C(z)` as polynomials in `(z_0,z_1)`:

```text
DEP    := all 3x3 minors of C(z) vanish identically  (rank_B C(z) <= 2 for all z),
NONDEP := some 3x3 minor of C(z) is not identically zero (rank_B C(z)=3 generically).
```

**Lemma 1 (when `c∉B`, the branch is always NONDEP).** The `z`-leading symbols of columns `1,2` are `â_1=-q1^1=-c_b c` and `â_2=-q1^2=-c_b`. A universal `B`-dependence `β_1v_1+β_2v_2+β_3v_3≡0` forces, on the `s`-coordinate `z`-leading part, `c_b(β_1 c+β_2)=0`; with `c_b≠0` and `c∉B` this gives `β_1=β_2=0`, then the `t`-coordinate `z`-leading part gives `β_3=0`. So no universal dependence ⟹ NONDEP. (When `c∈B,d∉B`, separatedness still holds but `1,c` are `B`-dependent, so DEP becomes possible — that is the one residual sub-case below.)

**Lemma 2 (NONDEP collapses the wall to a single Q-decision; rank-drop is negligible).** On NONDEP the rank-drop locus `{rank_B C(z)≤2}` is the common zero set of finitely many nonzero bounded-degree polynomials in `(z_0,z_1)`, hence `O(p)` points. For every `z` off that locus, `rank_B C(z)=3`, so `Q(z)=0` is necessary **and sufficient**. Therefore

```text
NONDEP, Q ≢ 0  ⟹  C2 ⊆ {Q=0} ∪ {rank-drop} = O(p) + O(p) = O(p)   [Cycle 16],
NONDEP, Q ≡ 0  ⟹  every z off the O(p) rank-drop locus is realizable ⟹ C2 = p^2 - O(p) = Θ(p^2).
```

This is the precise correction to the Cycle 25 audit. The audit worried that rank-drop strata might make `Q≡0` insufficient and secretly rescue `O(p)`. On NONDEP that worry is void: rank-drop is only `O(p)` values of `z`, so the augmented-minor conditions there cannot change the asymptotic count. On NONDEP the wall is exactly "`Q ≡ 0`?" — no rank subtlety survives. (I do **not** assert `Q≡0` happens; and the `Θ(p^2)` conclusion is still gated by the distinct-split-cubic requirement, see below.)

**Lemma 3 (DEP *restricts*, it does not expand).** If DEP holds (`rank_B C(z)≤2` for all `z`), then `Q≡0` automatically and carries no information. Realizability is `v_0(z)∈U(z)` with `U(z)=span_B C(z)` of `B`-dimension `≤2`, i.e. **two** independent `B`-linear conditions `ℓ_1(z)·v_0(z)=ℓ_2(z)·v_0(z)=0`, each a bounded-degree polynomial in `(z_0,z_1)`. Their common zero set is `O(p)` (a proper subvariety) **unless both vanish identically**. So a rank drop makes the realizable set *smaller*, never `Θ(p^2)`, except in the single degenerate event where the augmented `4×4` matrix `[c_1|c_2|c_3|c_0]` has `rank_B≤2` identically.

Net structural statement (rank-correct, replaces the false "`Q≡0 ⟹ every slope realized`"):

```text
C2 = Θ(p^2)  ⟺  the realizable locus {z: c_0(z)∈span_B C(z)} is 2-dimensional
             ⟺  (NONDEP and Q ≡ 0)  or  (DEP and the two augmented conditions ≡ 0).
Otherwise C2 = O(p).
```

## The explicit first obstruction (degree-4 coefficient of `Q`)

Using `s_i=a_i+m_z(â_i)`, `t_i=c_i+m_z(t̂_i)` and `⟨m_z x,m_z y⟩=N(z)⟨x,y⟩`, the degree-4 part of `Q` factors as `N(z)^2·Q_4` with `N(z)=z·z̄` the (nonzero, anisotropic) norm form. Since `â_3=0` (column 3 is `z`-constant in `s`), three of the six Plücker terms drop and

```text
Q_4 = N(c_b)·[ Im_α(c)·Im_α(q2^0) + Im_α(c̄·w)·Im_α(q2^2) − Im_α(w)·Im_α(q2^1) ],
w = c^2 − d,   q2^2 = P,  q2^1 = d + Pc,  q2^0 = cd + P·w,   P = P_E(u,b)/κ.
```

Because `N(z)^2 ≢ 0`:

```text
Q_4 ≠ 0  ⟹  Q ≢ 0  ⟹  C2 = O(p)   (on NONDEP, hence on the entire c∉B branch).
```

The factor `N(c_b)≠0` (source-valid `c_b≠0`) and the appearance of `Im_α(c)≠0` (`c∉B`) make `Q_4` generically nonzero. So a `Θ(p^2)` seed on the `c∉B` branch **requires** the explicit scalar equation `Q_4=0` *plus* all lower-order coefficients of `Q` to vanish, *plus* the split-cubic gate. This is strictly sharper than "is `Q≡0`": it is rank-stratified, and it pins the first vanishing coefficient in closed form. (I present `Q_4` as computed from the banked closed forms; the deterministic checker below should confirm it before it is treated as more than a guide.)

## Where `det M` sits (kept separate, per Cycle 25)

`det M=(c_b/κ^2)D`, with `D=N(ℓ)κ=κ∏_{a∈F_p}E(a)≠0` (Cycle 24), is the **`z`-free coefficient-frame** determinant of `τ↦[q1:p1−q2:p2]∈P^2(F)`. It governs whether the witnessing co-support `τ(z)` exists and is non-degenerate (relevant to the distinct-`D`-split-cubic gate `X^3−τ_1X^2+τ_2X−τ_3` splitting with distinct roots in `F_p`), but it is logically independent of the `z`-fiber object `Q`. It neither forces NONDEP nor decides `Q≡0`. So this branch is genuinely live and is not a disguised re-run of the Cycle 24 `D=0` cut.

## Answers to the three questions

1. Not fully proved. But the rank stratification is resolved: rank-drop can only *reduce* `C2` (Lemma 2 on NONDEP, Lemma 3 on DEP). So `O(p)` holds on NONDEP whenever `Q≢0`, in particular whenever `Q_4≠0`; and `c∉B` source-valid data are always NONDEP.
2. Not produced, and not citing scans. A `Θ(p^2)` seed is now pinned to a measure-zero event: `(NONDEP & Q≡0)` forcing `Q_4=0` and all lower coefficients, **or** the single DEP-degenerate locus with `c∈B,d∉B`.
3. Smallest exact decider isolated below.

## Smallest exact decider (checker / elimination ideal)

```text
I_Q     = ideal of the <=15 coefficients Q_{kl} of Q(z_0,z_1) (top coeff = N-form * Q_4 above),
I_aug   = ideal of the augmented-rank conditions for the DEP locus (3x3 minors of [C|c_0]),
I_valid = (∏_{a∈F_p}E(a))·κ·c_b·detM inverted (Rabinowitsch), + gcd(E,E^τ)=1 (separated).

Decide:  is V(I_Q) ∩ {NONDEP} ∩ {source-valid}  empty,  AND
         is V(I_aug) ∩ {DEP, c∈B,d∉B} ∩ {source-valid} empty?
If both empty  ⟹ PROOF: C2 = O(p) on the whole branch.
```

```text
checker(p):
  input : c,d∈F ; W_{n-1},W_{n-2},W_{n-3} ; u,b∈F (residue-line data)
  filter: ∏_{a∈F_p}E(a)≠0 ; gcd(E,E^τ)=1 ; κ≠0 ; c_b≠0 ; detM≠0
  build : η,P,q_i,p_i,c_b ; columns v_0..v_3 ; 4x4 B-det Q ; 3x3 minors of C and of [C|c_0]
  emit  : stratum∈{NONDEP,DEP}, degQ, Q_4, [Q_{kl}], Q_identically_zero,
          rankdrop_count, augmented_ideal_dim, C2=#{z: c_0(z)∈span_B C(z)},
          split_distinct_count among witnessing τ(z), status
  flag  : (NONDEP & Q≡0) OR (DEP & augmented≡0), source-valid, split cubics retained
          → candidate Θ(q_line) seed (NOT proof)
```

## Primary label

```text
BANKABLE_LEMMA
```

Banked (restricted `D=F_p`, `t=σ=2`, `j=3`, off `R0`, source-valid):

1. **DEP/NONDEP dichotomy via `C(z)`-minors**, with `c∉B ⟹ NONDEP` (leading symbols `c_b c, c_b` are `B`-independent).
2. **NONDEP reduction**: rank-drop is `O(p)` points, so `Q≢0⟹C2=O(p)` and `Q≡0⟹C2=Θ(p^2)`; the rank-stratification adds nothing on NONDEP. This corrects the Cycle 25 audit's open worry.
3. **DEP restriction**: a universal rank drop turns realizability into two augmented `B`-conditions, giving `O(p)` unless they vanish identically; rank drop never manufactures `Θ(p^2)` except in that explicit degenerate locus.
4. **Explicit degree-4 obstruction**: `deg-4` part of `Q` is `N(z)^2·Q_4` with the closed `Q_4` above; `Q_4≠0 ⟹ Q≢0 ⟹ C2=O(p)`, and `Q_4` is generically nonzero (`N(c_b)Im_α(c)` factor).

Residual `EXACT_NEW_WALL`: `W-F1-AA-RES-T2J3-QZERO-RANK-IDEAL` — decide emptiness of `V(I_Q)∩{NONDEP,source-valid}` and of the DEP/`c∈B,d∉B`/augmented-identically-zero locus, both saturated at `κ·c_b·detM·∏_aE(a)`.

Not banked: any `O(p)` proof on the full live branch, any counterpacket, any corrected-reserve/`q_gen`/protocol/list/CA/MCA/line-decoding/SNARK consequence, any finite-scan-as-proof. I did **not** repeat `Q≡0 ⟹ every slope realized`: the `Θ(p^2)` conclusion is conditional on NONDEP, carries an `O(p)` rank-drop correction, and remains gated by the distinct-split-cubic requirement.

## Route to a full solve?

Yes, and it is now a single bounded inequation plus one narrow locus, not the open-ended "is `Q≡0`."

Next exact lemma to prove (or refute): **on NONDEP source-valid data, `Q_4 ≠ 0`.** Concretely, show the `≤9`-parameter system

```text
Im_α(c)·Im_α(cd+Pw) + Im_α(c̄ w)·Im_α(P) − Im_α(w)·Im_α(d+Pc) = 0,
c∉B,  κ≠0,  c_b≠0,  ∏_{a∈F_p}E(a)≠0,  P=P_E(u,b)/κ
```

has no source-valid solutions (Gröbner saturation over `Q`, `p` carried symbolically via `N(ℓ)=∏E(a)`). If so, `Q≢0` on the entire `c∉B` branch ⟹ `C2=O(p)` there, and the whole wall reduces to the lone `c∈B, d∉B` DEP-degenerate locus, where Cycle 22/24's `Im_α` decoupling identities (`Im_α(J_A)=2Im_α(d)+Im_α(c)f_2`) are the natural next tool. The `N(c_b)Im_α(c)` structure of `Q_4` makes emptiness (PROOF, `C2=O(p)`) the more likely outcome, but it is not yet decided.
