I'll start by reading the file index, then the core project files.I'll read the core orientation files and the directly relevant recent cycle material in parallel.Let me read the Cycle 54 full response, the directly-relevant Cycle 11 (t=2,j=2 line incidence) audit, and the orientation files.Let me verify my understanding against the banked cuts and the current director state before writing.I have enough to write the deliverable. The environment exposes only a read tool (no file creation or code execution), so — as the Cycle 50–54 workers did — I deliver inline and present the checker as an unrun block for the director.

I worked the conic out explicitly and cross-checked its $j=1$ specialization against the banked Cycle 54 formula (they match exactly), so I have high confidence in the algebra. Here is the result.

---

# Cycle 55 — t=2, j=2 Determinantal Conic Split-Pair Count

Classification: `BANKABLE_LEMMA` + `PROOF` (of a corrected `+O(√Q)` bound) + `ROUTE_CUT` (on the literal `+O(1)` target) + `EXACT_NEW_WALL` + a `COUNTERPACKET` **seed** (candidate, not banked).

Field ledger kept separate as in Cycle 11/54: `Q=q_line=|F|` is the line/extension field carrying the residues and slopes; base/generated quantities `q_gen` are untouched; `L=μ_n⊂F^*`, so `n | Q-1`.

Confidence: high on the explicit conic and its `(s,s')` curve (elementary, verified against the `j=1` banked case); high on the `+O(√Q)` Weil bound and on the genus-1 obstruction to `+O(1)`; medium on the counterpacket because I cannot execute source-validity checks here, so it is delivered as a seed with the exact finite checks attached.

## 0. Verdict

The conic is genuine and I compute it in closed form. Transforming `D(s+s',ss')=0` into a curve in `(s,s')∈μ_n×μ_n` gives a **symmetric bidegree-(2,2) curve `C`**, whose quotient by `s↔s'` is exactly the conic `{D=0}`. `C` is a **double cover of a conic branched at 4 points, hence generically an elliptic curve (genus 1)**. A multiplicative-character/Weil argument on `C`, after removing the coset (quotient) components and the tangent/core stratum, proves

```text
R(u,v) = binomial(n,2)/Q + O(sqrt(Q)),     so  R <= ceil(binomial(n,2)/Q) + O(sqrt(Q)).
```

This is strictly weaker than the wall's `+O(1)`, and the gap is real: for `L=μ_{Q-1}=F^*` the count is `binomial(n,2)/Q - a_C/2 + O(1)` where `a_C` is the Frobenius trace of the elliptic curve `C`, with `|a_C|≤2√Q`. So a source-valid transverse/balanced/aperiodic pencil whose `C` is geometrically irreducible of genus 1 with `a_C` of order `-√Q` gives excess `Θ(√Q)=ω(1)`. **The literal `+O(1)` is therefore almost certainly false; the correct deterministic constant is `+O(√Q)`.**

## 1. `BANKABLE_LEMMA` 55.A — the explicit conic

Use moment coordinates `u_0,…,u_3`, `v_0,…,v_3` (`r=j+2=4`), and write the `2×2` minors of the moment matrix `[u_a u_b; v_a v_b]`:

```text
M_{ab} = u_a v_b - u_b v_a.
```

For `T={s,s'}`, `ell_T=(e_2,-e_1,1)` with `e_1=s+s'`, `e_2=ss'`. Substituting `ell_T` into Cycle 54's `D(T)=sum_{l,l'} kappa_{l,l'}(ell_T)_l(ell_T)_{l'}`, `kappa_{l,l'}=u_l v_{l'+1}-u_{l+1} v_{l'}`, and collecting (the cross terms telescope) gives the canonical conic

```text
D(e_1,e_2) = M_{12} e_1^2  -  M_{02} e_1 e_2  +  M_{01} e_2^2
             -  M_{13} e_1  +  (M_{03}-M_{12}) e_2  +  M_{23}.
```

Verification hooks (both check out by hand):
- Diagonal/leading coefficients are consecutive minors: `[e_1^2]=M_{12}`, `[e_2^2]=M_{01}`, `[1]=M_{23}`.
- Setting `j=1` (`ell_T=(-x,1)`) the same `kappa`-expansion gives `D=M_{01}x^2-M_{02}x+M_{12}`, **identical to banked Cycle 54**.
- `[e_2^2]=M_{01}` is the Cycle 11 invariant `kappa=wedge([W]_E,[Bnum]_E)`: `M_{01}=0 ⟺` the conic loses its top product-term `⟺` tangent/core stratum (Cycle 11's `det≡0 ⟹ kappa=0`).

The conic's symmetric matrix (char `≠2`, e.g. `Q=p^2`, `p` odd) is

```text
        [  M_{12}        -M_{02}/2        -M_{13}/2      ]
 G  =   [ -M_{02}/2       M_{01}      (M_{03}-M_{12})/2  ]
        [ -M_{13}/2   (M_{03}-M_{12})/2     M_{23}       ].
```

The six `M_{ab}` obey the single Plücker relation `M_{01}M_{23}-M_{02}M_{13}+M_{03}M_{12}=0`; transversality is exactly `G≠0` (in fact non-degenerate off the tangent stratum).

## 2. `BANKABLE_LEMMA` 55.B — the (s,s') curve (answers Q1)

Substitute `e_1=s+s'`, `e_2=ss'`:

```text
F(s,s') = M_{12}(s+s')^2 - M_{02}(s+s')ss' + M_{01}(ss')^2
          - M_{13}(s+s') + (M_{03}-M_{12})ss' + M_{23}  =  0.
```

`F` is **symmetric of bidegree (2,2)**. Key geometry:

```text
C = {F=0} -- 2:1 --> C/(s<->s') = {D(e_1,e_2)=0}  (a conic, genus 0 if smooth),
```

branched at the diagonal `s=s'`, i.e. where `{D=0}` meets the Vieta parabola `{e_1^2=4e_2}`. By Bézout that is `<=4` points, so

```text
genus(C) = (#branch points)/2 - 1 <= 1,   generically = 1  (elliptic).
```

This is the answer to Q1, with a caveat: yes, it is a curve with a Weil bound — but the curve is genus 1, not rational, so the Weil error is `Θ(√Q)`, not `O(1)`.

## 3. `PROOF` of the corrected bound `R ≤ binomial(n,2)/Q + O(√Q)`

Write `d=(Q-1)/n` and let `χ` generate the character group of `F^*`; the characters trivial on `μ_n` are `{χ^{nb}}_{b=0}^{d-1}`, so `1_{μ_n}(x)=d^{-1}∑_{b<d}χ^{nb}(x)`.

Decompose `C` over `\bar F` into geometric components and split off:
- **coset components** lying in some `s^α s'^β=c`, `(α,β)≠0` (handled in §4 as quotient packets), and
- the **tangent/core** locus (`M_{01}=0`, or `{D=0}` tangent to `{e_1^2=4e_2}`; removed by hypothesis).

Let `C^{ap}` be the remaining part: each component absolutely irreducible and **not** a coset curve. For the ordered count over `μ_n×μ_n` on `C^{ap}`,

```text
N_ord = d^{-2} * sum_{a,b=0}^{d-1}  U(a,b),
U(a,b) = sum_{(s,s') in C^{ap}(F), s,s'!=0}  chi^{na}(s) chi^{nb}(s').
```

- `(a,b)=(0,0)`: `U(0,0)=|C^{ap}∩(F^*)^2| = (#F-rational abs.-irred. components)*Q + O(√Q)`. When `C` is absolutely irreducible (the generic transverse aperiodic case) this is `Q+O(√Q)`, and `U(0,0)/d^2 = n^2/Q + O(n^2 Q^{-1/2}/d^2)=n^2/Q+O(√Q)`.
- `(a,b)≠(0,0)`: because `C^{ap}` is not a coset curve, `χ^{na}(s)χ^{nb}(s')` is a **nontrivial** character along each component, so Weil for curves gives `|U(a,b)| ≤ c_0 √Q` with `c_0` absolute (bidegree `≤(2,2)`, genus `≤1`, bounded conductor). Hence `d^{-2}∑_{(a,b)≠0}|U(a,b)| ≤ c_0 √Q`.

Therefore `N_ord = n^2/Q + O(√Q)`. Removing the `O(1)` diagonal, `s s'=0`, and `b(T)=0` points (each a bounded fiber) and passing to unordered pairs,

```text
R(u,v) = binomial(n,2)/Q + O(sqrt(Q)).     [aperiodic, transverse, non-core]   QED
```

This uses neither L2 anticollision, nor free-root/monodromy density, nor raw locator fibers; quotient packets and `d_M(E)` are charged separately (§4).

## 4. Quotient separation = multiplicatively special components (answers Q2, Q3)

The components on which Weil gives **no** cancellation are exactly those where `χ^{na}(s)χ^{nb}(s')` is constant, i.e. `C` lies in a coset curve `s^α s'^β=c`. Classify them:

```text
(Q1)  e_2 = c  (fixed product s s'=c):  the involution s <-> c/s.  ~n/2 pairs.
(Q2)  s' = c s (fixed ratio rho=s'/s=c): in (e_1,e_2) the parabola e_1^2=lambda e_2,
       lambda=(1+c)^2/c.  ~n pairs.
(QM)  X^M pullback: D factors through (s^M,s'^M); a mu_M-coset-union family.
```

These are precisely the imprimitive/quotient packets: each can carry `Θ(n)` split pairs and must be excluded or charged. **Quotient separation ⟺ no component of `C` is a coset curve `s^α s'^β=c`; equivalently the ratio `s'/s` is not confined to a proper `μ_M` and `D` is not an `X^M`-pullback (large `d_M(E)`).** This answers Q2 affirmatively and exactly.

Degenerate-conic dictionary (Q3), via `det G` and the matrix in §1:
- **Two lines** (`rank G=2`): each line `α e_1+β e_2+γ=0` pulls back to a `(1,1)` curve `β ss'+α(s+s')+γ=0`, a Möbius map `s↦s'`. Dangerous **iff** that Möbius map is multiplicatively special (→ `(Q1)`/`(Q2)`), else `O(1)` points by the same Weil/Möbius–subgroup bound.
- **Tangent to Vieta `{e_1^2=4e_2}`**: branch points collide ⟹ this is the diagonal/repeated-root = **tangent/core**.
- **Vertical/horizontal** (`M_{01}=0` ⟹ no `e_2^2`; `M_{12}=0` ⟹ no `e_1^2`): `M_{01}=0` is exactly `kappa=0`, the **tangent/core** boundary (matches Cycle 11).
- **`X^M`-compatible**: **quotient/imprimitive** `(QM)`.

So: Vieta-tangent and `M_{01}=0` are already tangent/core; coset-line and `X^M` are quotient. No new degeneracy appears at `t=2,j=2`.

## 5. Exact character sum and nondegeneracy (answers Q4)

```text
U(a,b) = sum_{(s,s') in C(F)} chi^{na}(s) chi^{nb}(s'),     1<= a or b <= d-1.
```

Nondegeneracy required for square-root cancellation: (i) `C` (component) **absolutely irreducible**; (ii) `C` **not a coset curve** `s^α s'^β=c` for the relevant `(α,β)` — equivalently the projection of `C` to the ratio `s'/s` is dominant and `D` is not an `X^M`-pullback. Under (i)+(ii), `|U(a,b)| ≤ (2g+2\deg-2)√Q = O(√Q)`, `g≤1`.

## 6. `ROUTE_CUT` + `EXACT_NEW_WALL`

`ROUTE_CUT` (constant, not malformation): the literal target

```text
#{ {s,s'} : D=0, b!=0 }  <=  ceil(binomial(n,2)/Q) + O(1)
```

is **not** what the geometry yields. `C` is generically an elliptic curve, so the curve-Weil ceiling is `+O(√Q)`, and that fluctuation is genuine, not an artifact (it survives the `O(1)` diagonal/`b=0` removals). Restate the wall as:

```text
W-MCA-T2J2-CONIC-SPLIT-PAIR-COUNT (corrected)
  R = binomial(n,2)/Q + O(sqrt(Q)),   aperiodic + transverse + non-core,
  with the O(sqrt(Q)) = -a_C/2 + O(1) for L=mu_{Q-1}, a_C = Frobenius trace of C.
```

`EXACT_NEW_WALL` — the residual is a **regime dichotomy**, not a curve-Weil statement:
- **(A) small subgroup `n=O(√Q)`**: the trivial fiber bound is already `O(n)=O(√Q)`; getting `O(1)` here needs a Stepanov/sum–product subgroup-incidence bound for a fixed bidegree-(2,2) curve meeting `μ_n×μ_n`, *not* Weil. This is the genuinely open `+O(1)` sub-statement.
- **(B) large subgroup `n≍Q`**: `+O(1)` is false unless `C` degenerates to genus 0; the next lemma is to decide whether transversality+balance+aperiodicity force `C` reducible/rational. I argue they do **not** (they make `D` non-degenerate, i.e. push `C` toward smooth genus 1), so the honest wall in this regime is `+O(√Q)` and `+O(1)` is refuted by §7.

## 7. `COUNTERPACKET` seed (candidate — explicit growing family; answers Q5)

Construction (per growing prime power `Q=p^2`):
1. Take `L=μ_n` with `n=Q-1` (`μ_n=F^*`, full multiplicative RS domain), so `d=1`: **no character averaging**, `R=½(Q-a_C)+O(1)`.
2. Choose moments `(u_0..u_3),(v_0..v_3)∈F^4` (rows of a `2×4` matrix; Plücker automatic) so that the conic `G` is non-degenerate (`det G≠0`, `M_{01}≠0`: not tangent/core), the bidegree-(2,2) curve `C` is geometrically irreducible and **not** a coset curve, and `C` has Frobenius trace `a_C≤-√Q` (choose the moment matrix in the "many-points" Frobenius class).
3. Then excess over the random baseline is `R - binomial(n,2)/Q = -a_C/2 + O(1) = Θ(√Q) = ω(1)`.

Why it is not one of the excluded packets:
- **Not tangent/core**: `det G≠0`, `M_{01}≠0`, `C` not tangent to `{e_1^2=4e_2}`.
- **Not quotient/imprimitive**: `C` not a coset curve `s^α s'^β=c`; ratio `s'/s` not in a proper `μ_M`; pick `E` (deg-2 modulus) with `d_M(E)` large for all proper `M|n`.
- **Not same-witness**: distinct landing slopes `z(T)=-a_i(T)/b_i(T)` over the points.
- **Not hidden imprimitive**: irreducibility of `C` over `\bar F` certifies aperiodicity.

This is a **seed, not a banked COUNTERPACKET** (per the Cycle 30/31/35 norm: single instances and dimension heuristics are not banked). It needs the finite verification below, which I could not run here.

## 8. Finite checker (Q5; unrun — for the director)

Verifies the conic identity, the `+O(√Q)` law, and tests the seed (excess vs `a_C`). I could not execute it.

```python
# CHECKER.py  Cycle 55  t=2,j=2 determinantal-conic split-pair count over F=F_{p^2}
# (A) D(e1,e2) from minors == rank-one landing det; (B) R vs binom(n,2)/Q;
# (C) seed: excess ~ -a_C/2 for n=Q-1.  Needs sympy-free finite-field arithmetic.
import itertools
from math import comb

def Fp2(p):                         # F_{p^2}=F_p[a]/(a^2+1); requires p%4==3
    assert p%4==3
    A=lambda x,y:((x[0]+y[0])%p,(x[1]+y[1])%p)
    S=lambda x,y:((x[0]-y[0])%p,(x[1]-y[1])%p)
    Mu=lambda x,y:((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    Z=lambda x:x[0]%p==0 and x[1]%p==0
    return A,S,Mu,Z

def units(p):  return [(a,b) for a in range(p) for b in range(p) if not(a==0 and b==0)]

def run(p=7,n=None,trials=300,seed=1):
    import random; random.seed(seed)
    A,S,Mu,Z=Fp2(p); one=(1,0); zero=(0,0); Q=p*p
    F=units(p)
    if n is None: n=Q-1                     # full domain mu_{Q-1}=F^*  (the seed regime)
    def pw(x,e):
        r=one
        for _ in range(e): r=Mu(r,x)
        return r
    L=[x for x in F if pw(x,n)==one]; assert len(L)==n
    def minors(u,v):                        # M_{ab}=u_a v_b - u_b v_a, a<b in 0..3
        return {(a,b):S(Mu(u[a],v[b]),Mu(u[b],v[a])) for a in range(4) for b in range(a+1,4)}
    def D_from_minors(M,e1,e2):
        M12,M02,M01,M13,M03,M23=M[(1,2)],M[(0,2)],M[(0,1)],M[(1,3)],M[(0,3)],M[(2,3)]
        t=[Mu(M12,Mu(e1,e1)), S(zero,Mu(M02,Mu(e1,e2))), Mu(M01,Mu(e2,e2)),
           S(zero,Mu(M13,e1)), Mu(S(M03,M12),e2), M23]
        r=zero
        for z in t: r=A(r,z)
        return r
    def landing_det(u,v,s,sp):              # rank-one minor a0 b1 - a1 b0 of 2x3 Hankel
        e=[Mu(s,sp), S(zero,A(s,sp)), one]  # ell_T low->high = (e2,-e1,1)
        row=lambda w,m:A(A(Mu(w[m],e[0]),Mu(w[m+1],e[1])),Mu(w[m+2],e[2]))
        a0,a1,b0,b1=row(u,0),row(u,1),row(v,0),row(v,1)
        return S(Mu(a0,b1),Mu(a1,b0)),(b0,b1)
    pairs=list(itertools.combinations(range(n),2)); Rline=-(-comb(n,2)//Q)
    worst=0; info=None; idmismatch=0
    for _ in range(trials):
        u=[random.choice(F) for _ in range(4)]; v=[random.choice(F) for _ in range(4)]
        M=minors(u,v); R=0
        for i,k in pairs:
            s,sp=L[i],L[k]
            det,(b0,b1)=landing_det(u,v,s,sp)
            Dm=D_from_minors(M,A(s,sp),Mu(s,sp))
            if not Z(S(det,Dm)): idmismatch+=1          # (A) identity must hold
            if Z(b0) and Z(b1): continue                # b=0 removed
            if Z(det): R+=1
        if R-Rline>worst: worst=R-Rline; info=dict(R=R,Rline=Rline)
    print(f"p={p} Q={Q} n={n} binom={comb(n,2)} Rline={Rline}")
    print(f"identity_mismatches={idmismatch}  max_excess(R-Rline)={worst}  worst={info}")
    print("READ: idmismatch must be 0 (55.A correct). For n=Q-1, excess ~ -a_C/2 ~ O(sqrt Q):")
    print("      sustained growth of max_excess with p is the COUNTERPACKET signature vs +O(1).")

if __name__=="__main__":
    run(p=7); run(p=11); run(p=19); run(p=31)   # watch max_excess grow like ~sqrt(Q)
```

Expected: `idmismatch=0` always (confirms 55.A); `max_excess` growing roughly like `√Q` across `p=7,11,19,31` is the counterpacket signature refuting `+O(1)`; if instead `max_excess` stays `O(1)` for all aperiodic non-core lines, the conic is being forced to degenerate and `+O(1)` survives (then §6(A) is the only open piece).

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Partial yes, but it reshapes the wall. The `t=2,j=2` count is now an explicit, hand-checkable conic/curve object, and the honest deterministic bound is `binomial(n,2)/Q + O(√Q)` — proved here — not `+O(1)`. The next exact steps, in order:

```text
Lemma 56.A (decide the wall constant).  Run CHECKER.py over p=7,11,19,31,...:
  if max_excess ~ sqrt(Q) on an aperiodic non-core line, BANK the COUNTERPACKET and
  restate the wall as +O(sqrt(Q)); else prove C is forced reducible/rational under
  transversality+balance+aperiodicity (genus-0 dichotomy), salvaging +O(1).

Lemma 56.B (small-subgroup +O(1), the genuinely open piece).  For n=O(sqrt(Q)),
  prove a Stepanov/sum-product incidence bound:
    #{(s,s') in mu_n^2 : F(s,s')=0} = O(1)
  for a fixed absolutely irreducible non-coset bidegree-(2,2) curve F.  This is the
  curve-times-multiplicative-subgroup incidence problem (Heath-Brown-Konyagin /
  Bombieri-Bourgain-Garaev style), and it is the t=2,j=2 statement that curve-Weil
  cannot reach.
```

The mechanism that generalizes to higher `j` is the one made explicit here: land on a fixed determinantal hypersurface, peel the multiplicatively-special (coset / `X^M`) components as the quotient packets via `d_M(E)`, and bound the aperiodic remainder by curve/subgroup incidence — with the genus (here 1) controlling whether the constant is `O(1)` or `O(√Q)`.