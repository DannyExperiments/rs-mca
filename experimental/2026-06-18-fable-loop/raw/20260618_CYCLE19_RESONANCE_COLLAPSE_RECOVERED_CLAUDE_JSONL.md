I have the full reduction chain and the source-level algebra. Code execution is denied in this harness (as in Cycles 14–18), so this is an analytic run worked directly from the banked Cycle 12/14 multiplication identities in `A=F[X]/E`. I pushed the slope forms to closed form and found the image-dimension question is sharper — and more dangerous — than the Cycle 18 framing assumed.

```text
BANKABLE_LEMMA
```

## Ledger (kept strictly separate)

```text
B=F_p, q_gen=p ;  F=F_{p^2}=B+alpha B, alpha^2=g nonsquare, q_line=p^2 ;  q_chal unused
D=F_p, n=p ;  t=sigma=2, j=3, a=n-3, k=n-5 ;  eta=2/n SUB-RESERVE
Work off R0={kappa:=[W]_E wedge [Bnum]_E = 0}. Line-incidence/residue calc only.
E=X^2+cX+d monic, c,d in F, separated (E^tau != E), nonzero on D ;  xi=[X]_E ;  xi^2=-c xi-d
u:=[W]_E, b:=[Bnum]_E (deg<2 so b=b0+b1 xi), ell:=[L_D]_E=[X^p-X]_E (tau-independent).
```

## What I verified from source (Cycle 12/14, exact, no experiment)

From `lambda_0 = xi^3 - tau_1 xi^2 + tau_2 xi` and `Q=[Q_S]_E` (Cycle 12), reducing mod `E` and changing to the `{u,b}` basis via the alternating form `x wedge y = x^(0)y^(1)-x^(1)y^(0)`, the four Cycle-14 affine forms are **exactly**:

```text
lambda_0^(1) =: eta = (c^2-d) + c tau_1 + tau_2          [the rank-one form]
q1 = -(Q_E(b)/kappa) * eta                               Q_E(x)=x0^2 - c x0 x1 + d x1^2
q2 = lambda_0^(0) + (P_E(u,b)/kappa) * eta                P_E(x,y)=x0 y0 - c x0 y1 + d x1 y1
p1 = lambda_0^(0) - (c + P_E(u,b)/kappa) eta - (1/kappa)(ell Q wedge b)
p2 = (1/kappa)[ Q_E(u) eta - (u wedge ell Q) ]
```

The two `Q`-dependent terms are affine in `(tau_1,tau_2)`:
`(ell Q) wedge b = (ell wedge b)Q^(0) - P_E(b,ell)Q^(1)`, `u wedge (ell Q) = (u wedge ell)Q^(0) + P_E(u,ell)Q^(1)`, with `Q^(0)=W_{n-3}-dW_{n-1} -W_{n-2}tau_1 + W_{n-1}tau_2`, `Q^(1)=(W_{n-2}-cW_{n-1}) - W_{n-1}tau_1`.

## Lemma 1 (rank-one leading coefficient)

`q1 = -(Q_E(b)/kappa)*eta` is a scalar multiple of the single affine form `eta`. So the **leading coefficient of the slope quadratic is rank-one** in `(tau_1,tau_2)`, vanishing exactly on the `F`-line `eta=0`. Note `lambda_0^(0)=cd+d tau_1` **cancels** out of all three slope-forms `q1, p1-q2, p2` (it survives only in the non-slope trace `p1+q2`). Proof: `(lambda_0 b) wedge b = -eta·Q_E(b)` by direct 2x2 expansion; divide by `kappa`. ∎

## Lemma 2 (quadric-case slope normal form — the `Delta1==0` case demanded)

In the quadric stratum `Delta1==0` (i.e. `Delta in B[tau]`), the two `B`-conditions are `p1+q2 in B[tau]` and `det P := p1q2-p2q1 in B[tau]`. Hence the slope-quadratic **discriminant descends to the base field**:

```text
delta_z := (p1-q2)^2 + 4 q1 p2 = (p1+q2)^2 - 4 det P  in  B[tau_1,tau_2].
```

Writing `c_b=-Q_E(b)/kappa`, `A:=(ell Q) wedge b`, the slopes are, up to a fixed `F`-translation (which preserves cardinality),

```text
z = const_F + w,   w^± = ( ±sqrt(delta_z) - A/kappa ) / ( 2 c_b * eta ),   delta_z in B[tau].
```

Therefore in the quadric case **`C2 = O(p)` iff the image of `w^±` is 1-dimensional over `B`**, i.e. the two `B`-coordinates of `w` are algebraically dependent as functions on `B^2`.

## The correction (this tempers Cycle 18)

Cycle 18 banked the collapse as "plausible." The normal form shows it is **not generic**. `w = (±sqrt(delta_z) - A/kappa)/(2c_b·eta)` is a ratio of `F`-valued functions on `B^2`; `eta` is rank-one and `delta_z in B`, but `A=(ell Q) wedge b` is a generic rank-two `F`-affine form. A generic such ratio has **2-dimensional** `B`-image, i.e. `C2=Theta(p^2)`. So collapse can only come from the resonance constraints forcing `A` (and the numerator `±sqrt(delta_z)-A/kappa`) into rank-one alignment with `eta`. Concretely:

```text
COLLAPSE (C2=O(p))  <=>  on the Delta1==0 stratum, A/kappa and sqrt(delta_z) are
                         functions of eta alone (mod the B-line structure),
                         equivalently  d w ^ d eta == 0  on the surface.
```

This is the same `tau`-independent obstruction in disguise: writing the three slope-forms in the basis `{eta, Q^(0), Q^(1)}`, the `P^2(F)`-image degenerates iff

```text
D := (ell wedge b) P_E(u,ell) + P_E(b,ell)(u wedge ell)  vanishes,
```

and `D` is **not** identically zero (e.g. `u=ell` gives `D=(ell wedge b)Q_E(ell) != 0` generically). So `D` (built only from `E, u, b, ell`) is a real, computable scalar gate; the residual wall is whether the resonance conditions on `(p1+q2, det P)` force the `B`-level dependence (not merely the `P^2`-level `D=0`). The Cycle 15 `p=7` datum (`C2<=6` on forced `R_a`) is **consistent with** the gate firing on the resonance stratum, but it is single-prime EXPERIMENTAL and does not decide it.

## Why not the other labels

- Not PROOF: I did not show the resonance conditions force `dim_B Im(w)=1`. The normal form makes plain that collapse is a non-generic degeneration that must be forced; I cannot certify it by hand and code is denied.
- Not COUNTERPACKET: dually, I did not exhibit source-valid `(E,Bnum,W)` with `Delta1==0` and `dim_B Im(w)=2` over a growing-`p` family. Asserting one would violate the no-finite-scan / sub-reserve guards.
- Not ROUTE_CUT: every Cycle 12–18 step checks out against the source multiplication identities; the monicity lemma and safe side are correct. The only thing I corrected is an over-optimistic *expectation* of collapse, not a false step.

## Sharpened exact wall + exact next step

```text
W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE  (sharpened, both branches)

Quadric branch Delta1==0: with q1=c_b·eta (rank one), delta_z in B[tau], and
w^± = (±sqrt(delta_z) - A/kappa)/(2 c_b eta),  A=(ell Q) wedge b,
prove  dim_B Im(w)=1  on every source-valid (p1+q2, det P) in B[tau] stratum
(=> C2=O(p)), OR build source-valid data with dim_B Im(w)=2 over growing p.

Graph branch deg_{tau3} g=1: same question after substituting tau3=-h/s.
```

Exact next step — a **finite symbolic** check that needs no growing prime: on the `Delta1==0` locus, compute `dw ^ deta` (equivalently `Res_{tau3}(Delta0,Delta1)` factor structure, or the gate `D` together with the two `B`-descent conditions). `dw ^ deta ≡ 0` ⟺ collapse ⟺ closes corrected local F1 T2J3 in this window (still sub-reserve `eta=2/n`). A nonzero `dw ^ deta` on a source-valid stratum is the precise counterpacket seed; only then run a growing-`p` family (`p=11,13,17,19,23`) filtered to `Delta1==0` watching `C2/p^2`.

## Non-claims (explicit)

No solve/disproof of the Proximity Prize; no `conj:B`; no proof of collapse and no `Theta(q_line)` counterpacket; nothing at or above corrected reserve (`eta=2/n` sub-reserve, so even a `Theta(q_line)` here would not refute corrected MCA); no `q_gen` statement and no `q_gen`/`q_line` merge; no protocol/denominator saving; no conversion to list/line/curve decoding, CA, MCA, or SNARK; finite scans cited only as EXPERIMENTAL; malformed terminal text not used.

```text
What to bank: Lemma 1 (rank-one q1, lambda_0^(0) cancellation), Lemma 2 (quadric
normal form with delta_z in B and the w^± ratio), the gate scalar D, and the
correction that collapse is non-generic. Do NOT bank collapse or a counterpacket.
```
