EXACT_NEW_WALL

I worked the `t=2, j=4` case by hand against the banked Cycle 11/12/16/20/24/25/28 objects (kernel execution is disabled in this harness, so no finite checker was run; flagged below). The headline finding is a clean structural break: the Cycle 28 mechanism does **not** extend to `j=4`, and the reason is exact and bankable.

## Field and parameter ledger

- `B = F_p`, `q_gen = p`. `F = F_{p^2} = B(alpha)`, `alpha^2 = theta` nonsquare, `q_line = p^2`. `q_chal` unused, kept separate.
- `D = F_p`, `n = p`. `t = sigma = 2`, now `j = n-a = r-t = 4`; hence `a = n-4`, `k = n-6`. `eta = sigma/n = 2/n`, sub-reserve.
- `A = F[X]/E`, `E = X^2+cX+d`, `xi = [X]_E`, `xi_m = [X^m]_E`, `u = [W]_E`, `b = [Bnum]_E`, `ell = [X^p-X]_E = [L_D]_E`, `kappa = u wedge b`.
- Off `R0` (`kappa != 0`); source-valid (`E` nonzero on `F_p`); separated (`gcd(E,E^tau)=1`); `c_b = -Q_E(b)/kappa != 0`.
- Conjugation `fbar = f_0 - alpha f_1`, `Im(f)=f_1`, `N = N_{F/B}`, `w = c^2-d`.

This is a restricted residue-line/bad-slope incidence calculation only.

## 1. The `t=2, j=4` quotient and affine system

Co-support `T = D\S`, `|T| = 4`, with `tau_i = e_i(T)`, `i=1..4`. Euclidean division `W = L_S Q_S + I_S`, `deg Q_S <= j-1 = 3`, `L_S = L_D/L_T`, `L_D = X^p - X`. Using `L_S L_T = X^p-X` the sub-leading coefficients of `L_S` are the complete homogeneous symmetrics `h_i(T)` (`h_1=tau_1`, `h_2=tau_1^2-tau_2`, `h_3=tau_1^3-2tau_1 tau_2+tau_3`), and the division recursion gives the closed form (valid for `p` past the first few coefficients, `deg W = n-1`):

```text
Q_S = W_{n-1} X^3
    + (W_{n-2} - W_{n-1} tau_1) X^2
    + (W_{n-3} - W_{n-2} tau_1 + W_{n-1} tau_2) X
    + (W_{n-4} - W_{n-3} tau_1 + W_{n-2} tau_2 - W_{n-1} tau_3),
```

i.e. `[X^{j-1-i}]Q_S = sum_{m=0}^{i} (-1)^m W_{n-1-i+m} tau_m` (`tau_0=1`). This reproduces the Cycle 11 (`j=2`) and Cycle 12 (`j=3`) forms exactly, and confirms the family pattern: **`Q_S` depends on `tau_1,...,tau_{j-1}` only** (here `tau_1,tau_2,tau_3`, not `tau_4`).

The locator residue is affine in **all four** parameters:

```text
lambda = [L_T]_E = xi_4 - tau_1 xi_3 + tau_2 xi_2 - tau_3 xi_1 + tau_4,
mu  = b*lambda,          iota = u*lambda - ell*[Q_S]_E,
L_z(tau) = iota - z*mu = sum_{i=1}^{4} tau_i C_i(z) + C_0(z) = 0  in A ~= B^4.
```

Co-support parameters and columns `C_i(z) = P_i - z R_i`:

```text
C_4 = (u) - z(b)
C_3 = (-u xi + W_{n-1} ell) - z(-b xi)
C_2 = (u xi_2 - ell(W_{n-1} xi + W_{n-2})) - z(-b xi_2)   [R_2 = +b xi_2]
C_1 = (-u xi_3 + ell(W_{n-1} xi_2 + W_{n-2} xi + W_{n-3})) - z(-b xi_3)
```

with `R_i = (-1)^i b xi_{4-i}`.

## 2. What replaces `Q` — the parameter count meets the ambient dimension

At `j=3`: 3 parameters `(tau_1,tau_2,tau_3)`, ambient `dim_B A = 2t = 4`. Consistency = "`-C_0` lies in the 3-dim column span" = one codimension-1 equation, the `4x4` determinant `Q(z)=det_B[C_1|C_2|C_3|C_0]`. That is the incidence obstruction whose `Q_4 != 0` gave `C2 <= 4p`.

At `j=4`: **4 parameters `(tau_1,...,tau_4)`, ambient still `B^4`** (since `t` is unchanged). The coefficient matrix

```text
M(z) = [C_1(z) | C_2(z) | C_3(z) | C_4(z)]   is already 4x4 over B.
```

So `Q` (the augmented `4x4` det) has **no direct analogue**: the augmented matrix `[C_1|C_2|C_3|C_4|C_0]` is `4x5`, and when `det_B M(z) != 0` the system `M(z)tau = -C_0(z)` has a **unique** solution `tau(z) in B^4` — affine consistency holds for *every* such `z`. The natural determinant is now the **square coefficient determinant `det_B M(z)`**, whose role has flipped: it is the *uniqueness/invertibility* locus, **not** an incidence obstruction. This is the "missing-determinant" failure mode of task item 6.

## 3-4. Top symbol and locator factorization

Each `C_i(z) = P_i - z R_i`; the degree-4-in-`z` part (top symbol) takes every `-zR_i`:

```text
TopSym = det_B[ m_z(-R_1) | ... | m_z(-R_4) ] = det_B(m_z) * det_B[-R_1|-R_2|-R_3|-R_4],
```

`m_z` = multiplication by `z in F` on `A`. As a B-map on `A ~= B^4`, `det_B(m_z) = N(z)^2` (same `N(z)^2` prefactor as Cycle 28). The sign bookkeeping `R_i=(-1)^i b xi_{4-i}` gives `det_B[-R_1|..|-R_4] = det_B[b xi_3 | b xi_2 | b xi_1 | b xi_0] = det_B(m_b)*det_B[xi_3|xi_2|xi_1|xi_0]`. With `xi_0=(1,0)`, `xi_1=(0,1)`, `xi_2=(-d,-c)`, `xi_3=(cd, c^2-d)` over `{1,xi}`, the `4x4` B-determinant collapses to

```text
det_B[xi_3|xi_2|xi_1|xi_0] = -( Im(c) Im(cd) - Im(d) Im(w) ) = -(Q_4 / N(c_b)),
```

the **same degree-1 locator factor** as Cycle 28 (`Q_4/N(c_b) = c_1^2 d_0 - c_0 c_1 d_1 + d_1^2`). With `det_B(m_b) = N(Q_E(b)) = N(c_b)N(kappa)`:

```text
TopSym( det_B M(z) ) = - N(kappa) * N(z)^2 * Q_4
                     = - N(kappa) N(c_b) Im(c)^2 * N(z)^2 * E(-Im(d)/Im(c))   (c notin B).
```

So **yes, the top symbol factors as a source-valid-nonzero B-scalar times `N(z)^2` times the locator factor**, and the locator content is exactly the Cycle 28 `Q_4`-quantity: `TopSym = 0 iff E has an F_p-root iff N(ell)=prod_{a in F_p}E(a)=0`. By Cycle 28 (`c notin B`: `Q_4 = N(c_b)Im(c)^2 E(a*)`, `a*=-Im(d)/Im(c)`; `c in B`: `Q_4 = N(c_b)Im(d)^2`, nonzero by separatedness) the factor is **source-validly nonzero on both branches**. `N(kappa) != 0` off `R0`.

Exponent: the locator enters to **`m=1` (the same single active evaluation `E(a*)` as `j=3`), not a growing power**, and is multiplied by `N(z)^2` (also unchanged from `j=3`). The literal full norm `N(ell)` is degree-`p`; the top symbol is not literally `N(ell)^m` but the single factor `E(a*)` whose zero locus equals that of `N(ell)`.

## 5-6. Consequence: the mechanism does NOT extend; exact new wall

The clean top symbol proves `det_B M(z) not identically zero`, hence `M(z)` is invertible off a degree-`<=4` curve (`<= 4p` slopes). **But this does NOT give `C2 = O(p)`.** Unlike `j=3`, `det_B M` is the uniqueness determinant: for all but `<= 4p` slopes there is a *unique* affine pre-image `tau(z) = M(z)^{-1}(-C_0(z))`, so **affine consistency is generically automatic and imposes no slope bound**. The bound must now come entirely from the gate that was slack at `j<=3`:

```text
W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE:
bound  #{ z in F : tau(z) = (e_1,e_2,e_3,e_4) of a distinct 4-subset T subset F_p }.
```

Two structural warnings fall out, and I deliberately do not resolve them:

- The unique-pre-image fact is a *fiber* statement (`<=1` co-support per slope off the curve), which is the **opposite** of a fiber-collapse bound. There are `~ C(p,4) ~ p^4/24` split quartics but only `p^2` slopes, so the affine layer no longer obstructs `C2` from reaching `Theta(p^2)=Theta(q_line)`. This is a genuine **sub-reserve counterpacket seed** — exactly the failure mode Cycle 28's "route to full solve" flagged — but it is NOT a counterpacket: no growing-prime family, no proven surjectivity onto a positive-density slope set, and single-prime scans would be experimental only.
- The top-symbol mechanism (locator-controlled, source-valid nonzero, with constant exponents `N(z)^2`, locator `m=1`) **persists**; what fails is its slope-bounding *consequence*, because the determinant it is the top symbol of changed meaning when `#params` rose from `j-1<2t` to `j=2t`.

## Bankable sub-lemma (inside this wall)

In the restricted `D=F_p`, `t=sigma=2`, `j=4`, off-`R0`, source-valid separated `c_b!=0` window: the `j=4` quotient closed form above; the affine system has 4 parameters with square coefficient matrix `M(z)=[C_1|C_2|C_3|C_4]`; and `TopSym(det_B M) = -N(kappa)N(z)^2 Q_4`, source-validly nonzero, with `Q_4` the Cycle 28 locator quantity (vanishing iff `N(ell)=0`). Hence `det_B M not identically zero`, so the slope -> co-support map is generically a well-defined degree-`<=4` rational map `z -> tau(z)`.

## Dependency list

- Cycle 11/12: family pattern for `Q_S`, `[e_j^?]`-independence, `lambda` reduction, `Delta`/`L_z` setup.
- Cycle 16: `c_i(z)=s_i u + t_i b` columns, `Q ≢ 0 => C2<=4p` (necessity direction only).
- Cycle 20: `q1=c_b eta`, `q2=lambda_0^(0)+P eta`, expansion identity, `c_b=-Q_E(b)/kappa`, gate `det M=(c_b/kappa^2)D`.
- Cycle 24: `D=N(ell)kappa`, `N(ell)=prod_{a in F_p}E(a)`; source-valid nonvanishing.
- Cycle 25: six-term Plucker/Laplace shape and the `det M` (z-free) vs `Q(z)` (fiber) separation.
- Cycle 28: `Q_4 = N(c_b)(Im(d)^2 - Im(c)Im(cbar d))`, `Q_4 ∝ E(a*)`, source-valid nonvanishing both branches.

## Hidden assumptions

- `Q_S` closed form uses `p` large enough that `W_{n-1..n-4}` are genuine top coefficients and the `-X` tail of `L_D=X^p-X` does not reach the top `j` quotient coefficients (Cycle 11/12 style hypothesis).
- The `lambda_0`/expansion-identity inputs are taken from banked Cycle 12/20 forms; I re-derived `Q_S`, the columns, and `det_B[xi_3|xi_2|xi_1|xi_0]` directly, but reused the `Q_4` closed form from Cycle 28 rather than re-deriving it from raw `A0/B0`.
- `det_B(m_z)=N(z)^2` and `det_B(m_b)=N(Q_E(b))=N(c_b)N(kappa)` use `det_B = N_{F/B} o det_F` for F-linear endomorphisms of `A`.
- No finite checker was run (kernel disabled). A by-`p` scan over `p=7,11,13` against raw Cycle 14/15 columns would convert this from "by-hand" to "machine-confirmed"; recommended before any promotion.

## Rejected overclaims

- NOT a `C2=O(p)` proof for `j=4`: the top symbol does not bound slopes once the affine determinant becomes the uniqueness determinant.
- NOT a counterpacket: the `Theta(q_line)` risk is unproven (no growing-prime family, no split-quartic image lower bound).
- No claim the top symbol equals `N(ell)^m`; it is scalar`* N(z)^2 *`(single locator factor `E(a*)`, zero-locus `= {N(ell)=0}`), exponent `m=1`.
- Sub-reserve (`eta=2/n`), local only. No corrected-reserve, `q_gen`/`q_line` merge, `q_chal`, list/CA/MCA/line-decoding/curve-MCA/protocol/SNARK, or Proximity-Prize consequence.
- No converse `det_B M(z)=0 => realized slope`.

## Next exact wall

`W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE`: with `tau(z)=M(z)^{-1}(-C_0(z))` the unique affine pre-image (off the `<=4p` curve `det_B M(z)=0`), bound `#{z in F : X^4 - tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z)` splits into 4 distinct roots in `F_p\S}`. Prove either (i) this image is `O(p)` (extending the `t=2` law to `j=4`), or (ii) exhibit a source-valid growing-prime family realizing `Theta(p^2)=Theta(q_line)` distinct slopes (the sub-reserve counterpacket seed).

## Do I see a route to a full solve?

Not a clean one at `j=4` via the `j<=3` mechanism — it provably stops here. The honest next lemma is the split-quartic image-count, framed as a curve-meets-split-locus problem: the degree-`<=4` rational slope-to-co-support map `z -> tau(z)` lands in the space of monic quartics; the question is how often it hits the totally-split-distinct `F_p` locus. A natural attack is to compose `z -> tau(z)` with the discriminant and the `p`-power "split over `F_p`" condition (each root in `F_p` is a `Frobenius`-fixed condition), turning the gate into incidence of a fixed low-degree curve with the Frobenius/split stratification — but I have not reduced that to a banked bound, and the abundance of split quartics (`~p^4` vs `p^2` slopes) means the counterpacket direction is live and must be settled by a growing-prime family, not asserted.
