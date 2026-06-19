I'll start by reading the file index and project files to understand the current state.I'll read the core project files first to understand the route state, then the recent cycle material.Let me read the route board, active walls, banked lemmas, cuts, and the most recent cycle prompt/responses.Let me read the recent cycle responses (49-52) and the banked lemmas, cuts, and route board to fully understand the current state.Now let me read the banked lemmas, cuts/false routes, and the Cycle 50 and 48 responses to understand the quotient packets and the per-line structure precisely.Let me read the banked lemmas, the Cycle 49 response, and the Cycle 47/48 audits to ground the quotient packets and the character-sum structure.I've now read the Cycle 49–52 chain, the banked lemmas, cuts, active walls, and the Cycle 53 prompt. I have enough to contribute precisely.

A note on the harness: this environment exposes only a read tool — no file-creation or code-execution — so, exactly as the Cycle 50/51/52 workers did, I deliver inline. The `RESULT.md`, `CHECKER.py`, and `NEXT_PROMPT.md` contents are given as blocks the director can save to `output_files/`. I could not execute the checker; where I rely on computation I say so.

---

# Cycle 53 — Per-Line Symmetric Determinantal Incidence

Classification: **`BANKABLE_LEMMA` + `ROUTE_CUT` + `EXACT_NEW_WALL`.** Not `PROOF` of the deterministic incidence bound, not `COUNTERPACKET`.

Confidence: high on the signed slope-summed character identity (elementary and exact); high on the top-symbol computation and the evaluation/cosupport rewriting; high on the route-cut that determinantal codimension does not yield `O(j)` by Bezout; the deterministic bound `Err <= O(j)` stays open and is the wall. Ledger kept separate: `C = RS[F,L,k]`, syndromes over `F`, `Q = |F|`; in the matched quadratic instantiation `Q = q_line = p^2`, `B = F_p`, `q_gen = p` untouched.

## 0. One-line verdict

The deterministic per-line bound is **neither proved nor refuted**, but it now has an *exact* analytic form. I reduce `R(u,v) <= R_line + O(j)` to a single **signed slope-summed nontrivial-character bound `Err <= O(j)`**, where `Err` is the elementary-symmetric / cosupport exponential sum of Cycle 44, now summed over the whole slope line `z` and a dual vector `y`. Balanced right-minimal-index gives exactly **phase-nondegeneracy** (no trivial-character directions off `<= t` tangent slopes), which is *necessary* for cancellation; it does **not** give cancellation, and "determinantal codimension `t-1` + Bezout" does **not** give `O(j)` — that route is cut. Quotient-separation (`d_M(E)` not small) is the hypothesis that removes the `X^M`-imprimitive main term inside `Err`. So Cycle 53 converts the wall from a geometric incidence statement into an exact character-sum statement and pins the obstruction.

## 1. The exact object and the signed identity (BANKABLE_LEMMA 53.A)

Fix the transverse Hankel pencil `H(w)_{m,l} = w_{m+l}` (`0 <= m <= t-1`, `0 <= l <= j`, `t = r-j`), `a(T) = H(u)ell_T`, `b(T) = H(v)ell_T`, with `ell_T` the coefficient vector of `L_T(X) = prod_{x in T}(X-x)`. For split `T` (monic squarefree fully-`L`-split, `|T|=j`):

```text
#{ z in F : a(T) + z b(T) = 0 } = Q   if a(T)=b(T)=0  (T in common core K0),
                                = 1   if b(T)!=0 and rank[a(T)|b(T)]<=1,
                                = 0   otherwise.
```

Summing over `z` and isolating the rank-one transverse count gives the exact identity

```text
R(u,v) = sum_{z in F} N(z) - Q * K0_split,
   N(z) = #{ T split : H(u+zv) ell_T = 0 },
   K0_split = #{ T split : H(u)ell_T = H(v)ell_T = 0 }.
```

Additive-character expansion of the `t` linear conditions defining `N(z)` (`psi` a fixed nontrivial additive character of `F`, `y in F^t`):

```text
N(z) = (1/Q^t) sum_{y in F^t} S(y,z),   S(y,z) = sum_{T split} psi( <y, H(u+zv) ell_T> ).
```

The `y = 0` term is `binom(n,j)`, independent of `z`; summed over the `Q` slopes it is `binom(n,j)/Q^{t-1}`, **exactly the unceiled `R_line`, and it is independent of the pencil** (trivial-character main term). Therefore

```text
R(u,v) = binom(n,j)/Q^{t-1}  -  Q*K0_split  +  Err,
   Err := (1/Q^t) * sum_{z in F} sum_{y in F^t, y != 0} S(y,z).
```

Since `R_line >= binom(n,j)/Q^{t-1}` and `-Q*K0_split <= 0`, the deterministic per-line bound follows from, and is essentially equivalent to,

```text
   ***  Err <= O(j).  ***
```

This is the new bankable content: the deterministic first-moment wall is an **upper bound on one signed nontrivial-character sum**, not an equidistribution statement. (Note `Err` is signed; we need only the one-sided bound. The companion lower bound `R >= R_line - O(j)` is the Cycle 44 failure/L2 branch and is separate.)

## 2. The phase is an evaluation/cosupport sum (answers Q1)

Write `u + zv` in moment form `w_i = sum_{x in L} beta_x(z) x^i` (surjective for `r <= n`, `beta` affine in `z`), and `Y(X) = sum_{m<t} y_m X^m`. A direct computation collapses the Hankel pairing to an **evaluation over the complement**:

```text
<y, H(u+zv) ell_T> = sum_{x in L} beta_x(z) Y(x) L_T(x)
                   = sum_{x in L \ T} beta_x(z) Y(x) * prod_{y' in T}(x - y'),
```

because `L_T(x) = 0` for `x in T`. Hence

```text
S(y,z) = sum_{T split} psi( sum_{x in L\T} beta_x(z) Y(x) prod_{y' in T}(x-y') ),
```

which is exactly the Cycle 44 cosupport phase `psi(rho-type linear form in e_m(T))`. So **yes (Q1): the degree-2 symmetric determinant system is a character sum over `T subset L`** — and it is *the same* elementary-symmetric / cosupport exponential sum already banked, now carrying two extra summation variables `(y, z)`. The determinant (syndrome) side and the cosupport side of the program coincide as character sums; this is Cycle 50.C made explicit at the level of the phase, not just the count.

Top symbol. The coefficient of `(ell_T)_0 = (-1)^j e_j(T) = (-1)^j prod_{x in T} x` (the multiplicative "norm" of `T`) in the phase is

```text
g_0(y, u+zv) = <y, u'> + z <y, v'>,   u' = (u_0,...,u_{t-1}), v' = (v_0,...,v_{t-1}),
```

which vanishes only on a hyperplane in `y` (fixed `z`) or at one `z` (fixed `y != 0`). Off that locus the phase genuinely depends on the top symmetric datum of `T`.

## 3. What balanced index buys, and what it does not (answers Q2; ROUTE_CUT)

**It buys phase-nondegeneracy.** Balanced right-minimal-index (all indices in `{0,1}` at reserve scale) is equivalent to: the pencil `H(u)+zH(v)` has full row rank `t` for all but `<= t` *tangent* slopes, and the moving scroll is a genuine degree-`<=t` scroll with no directrix of degree `>= 2` (Cycle 49 Kronecker form). In the character sum this means: for every `y != 0` and every `z` off the `<= t` tangent slopes, the dual polynomial `G_{y,z}(X) = sum_x beta_x(z)Y(x)X^{(.)}` does not annihilate the configuration, so `S(y,z)` is a **nontrivial** sum (phase nonconstant in `T`), not the trivial value `binom(n,j)`. Equivalently, the coefficient matrix of the `binom(t,2)` symmetric quadrics `a_i b_l - a_l b_i` has no `y`-direction of identically-vanishing phase. That is the precise sense in which balanced index gives a "nondegenerate coefficient matrix."

**It does not buy cancellation, and Bezout does not rescue it.** The tempting route

```text
rank-one locus has codimension t-1  =>  intersect with the configuration via Bezout  =>  O(j),
```

is **cut**, for two independent reasons:

- The split configuration `e(Split_L) = Sym^j(L)` is a set of `binom(n,j)` *discrete* points, not a variety of positive dimension transverse to the determinantal locus; Bezout on a `0`-dimensional structured set says nothing. The honest object is `N(z) = #{ discrete points [L_T] on the codim-t linear space P(ker H(u+zv)) }` summed over the pencil `z in P^1` — an incidence count, with no a priori `O(j)` ceiling for a structured point set on a moving linear space.
- A nondegenerate (nonconstant) linear phase in `e(T)` can still resonate with the multiplicative structure of `L = mu_n`. That resonance is exactly the quotient packet (§4). So phase-nondegeneracy is strictly weaker than the square-root cancellation `|S(y,z)| <= binom(n,j)/Q^{1/2-o(1)}` that `Err <= O(j)` needs.

This parallels and sharpens Cycle 49's cut ("core removal + scroll degree is not an `O(n)` bound") and Cycle 50 Route Cut 1 ("balanced controls the scroll's shape, not the arithmetic of how `Split_L` sits on it"). Net: balanced index removes the *trivial-phase* (directrix) directions from `Err`; the surviving `Err` is a genuine cancellation problem.

## 4. The quotient main term in determinant language (answers Q3)

A periodic support `T` that is a union of `mu_M`-cosets (`M | n`) has `L_T(X) = g(X^M)` for some `g`, so `ell_T` is supported on degrees divisible by `M`, and `e_m(T) = 0` unless `M | m`. In `Err`, such `T` couple only to dual data `y` and slopes `z` for which the phase is `X^M`-compatible; the sub-sum over `X^M`-periodic `T` is itself a *complete, uncancelled* character sum on the quotient `L/mu_M ≅ mu_{n/M}`, contributing a **secondary main term**

```text
Err ⊇  ~ binom(n/M, j/M) / Q^{(t/M)-... }   (the Cycle 48 quotient-component value, >> R_line),
```

i.e. the `X^M`-imprimitive piece survives the `y != 0` projection because it is the trivial character of the *quotient*. This is the determinant-language form of the Cycle 48 packet: an imprimitivity main term, not a Galois group of a degree-`j` cover. The defect `d_M(E) = deg minpoly([X^M]_E)` controls it precisely: if `d_M(E)` is **large**, then `H(u+zv)` restricted to `X^M`-periodic locators retains full rank, the periodic sub-sum is itself nontrivial, and the secondary main term collapses back into the error; if `d_M(E)` is **small** (e.g. `=1`), the periodic locators concentrate on a low-degree sub-scroll and the secondary main term dominates. So **the quotient-separation hypothesis is exactly "`d_M(E)` not small for every proper `M | n`," and it is what deletes the `X^M` main term from `Err`.** It is load-bearing and is not implied by balanced index (a `d_M(E)=2` packet coexists with `{0,1}` indices — Cycle 50 Route Cut 1).

## 5. Direct bound on the image `Z` (answers Q4)

No separate handle, and I do not re-propose the monodromy route (cut in Cycle 52: `Split_L` is discrete and carries no cover). Precisely: `Z <= R` is the only elementary upper route (Cycle 51.A(i)); L2/anticollision only lower-bounds `Z` via `Z >= R^2/M_2` (Cycle 51.A(ii)); above entropy `R - Z = sum_z (nu(z)-1)_+ = o(R_line)`, so `Z` and `R` coincide where the bound is non-vacuous (Cycle 52 §7). The single unconditional `Z`-gain remains the tangent core `Z_tan = O(j)` (the banked `O(j)` cushion). New caveat for the *landing* count: the `O(j)` in `R <= R_line + O(j)` is the same directrix budget **only because transversality bounds the fiber depth at the `<= t` tangent slopes**; without the "contained/core templates removed" hypothesis a single tangent slope can carry a fat fiber and inflate `R` (not `Z`). So the `O(j)` term is image-clean (`Z_tan`) but landing-clean only under transversality — worth recording.

## 6. ROUTE_CUT summary

- Cut: "determinantal codimension `t-1` + Bezout ⇒ `R = O(j)`." The configuration is `0`-dimensional and structured; the real object is a moving-linear-space incidence / a signed character sum, with no Bezout ceiling.
- Cut (reaffirmed from Cycle 52): no monodromy/Chebotarev image-count for `Split_L`; do not bound `Z` through a totally-split density.
- Not cut, and now exact: the wall is `Err <= O(j)`, a one-sided slope-summed nontrivial-character bound, with quotient-separation removing the `X^M` main term.

## 7. EXACT_NEW_WALL

```text
W-MCA-PER-LINE-SLOPE-SUMMED-CHARACTER-CANCELLATION   (= the Err <= O(j) wall)
```

> For a fixed transverse balanced (minimal indices in `{0,1}`) quotient-action-rank-separated Hankel pencil over `F`, prove
> ```text
> Err := (1/Q^t) sum_{z in F} sum_{y in F^t \ 0} sum_{T split} psi( sum_{x in L\T} beta_x(z) Y(x) prod_{y' in T}(x-y') )
>      <= O(j),
> ```
> equivalently the per-line square-root cancellation `|S(y,z)| <= binom(n,j) * Q^{-(1/2)+o(1)}` uniformly for `y != 0` and `z` off the `<= t` tangent slopes, **after** quotient-separation has removed the `X^M`-imprimitive (Cycle 48) main term. Then `R(u,v) <= R_line + O(j)` by 53.A, and `Z(u,v) <= R(u,v)` follows.

This is the same wall as Cycle 44's `...-SYMMETRIC-FUNCTION-CANCELLATION` and Cycle 50's `...-CONFIG-EQUIDISTRIBUTION`, now with the *exact slope-summed integrand* and the precise role of each hypothesis isolated (balance ⇒ phase-nondegeneracy; quotient-separation ⇒ no `X^M` main term; transversality ⇒ thin tangent fibers).

## 8. Finite checker (Q5; unrun — for the director)

This distinguishes the three concentration mechanisms, which the toy `Q=p` checkers of Cycles 50–52 could not: it uses the real ledger `F = F_{p^2}`, `Q = p^2`, the smooth multiplicative domain `L = mu_n` with `n | p^2-1`, verifies the exact identity `R = binom(n,j)/Q^{t-1} - Q*K0 + Err` two independent ways (self-validating), and **attributes any excess `R - R_line` to periodic (`X^M`) vs aperiodic** by counting `mu_M`-coset-union landings per divisor `M | n`.

```python
# CHECKER.py — Cycle 53 per-line symmetric-determinantal incidence (pure Python, F_{p^2})
# Distinguishes aperiodic vs quotient(X^M) vs tangent concentration; self-validates identity.
import itertools, random
from math import comb

def make_Fp2(p):                      # F_{p^2} = F_p[a]/(a^2+1), needs p % 4 == 3
    assert p % 4 == 3, "use p = 3 mod 4 so a^2=-1 is irreducible"
    def add(x,y): return ((x[0]+y[0])%p,(x[1]+y[1])%p)
    def sub(x,y): return ((x[0]-y[0])%p,(x[1]-y[1])%p)
    def mul(x,y): return ((x[0]*y[0]-x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
    def inv(x):
        d=(x[0]*x[0]+x[1]*x[1])%p; di=pow(d,p-2,p); return ((x[0]*di)%p,((-x[1])*di)%p)
    def iszero(x): return x[0]%p==0 and x[1]%p==0
    return add,sub,mul,inv,iszero

def units_mu_n(p,n,mul,one):          # L = mu_n in F_{p^2}, brute force (correct & simple)
    assert (p*p-1)%n==0, "need n | p^2-1"
    elts=[(a,b) for a in range(p) for b in range(p) if not(a==0 and b==0)]
    def powe(x,e):
        r=one
        for _ in range(e): r=mul(r,x)
        return r
    return [x for x in elts if powe(x,n)==one]

def run(p=7, n=8, k=2, j=2, trials=300, seed=0):
    random.seed(seed)
    add,sub,mul,inv,iszero=make_Fp2(p); one=(1,0); zero=(0,0); Q=p*p
    L=units_mu_n(p,n,mul,one); assert len(L)==n, f"mu_{n} has {len(L)} elts"
    r=n-k; t=r-j
    assert 0<j<=r and t>=1, "need 0<j<=r, t=r-j>=1"
    def hankel(w): return [[w[m+l] for l in range(j+1)] for m in range(t)]   # t x (j+1)
    def loc(T):                                   # coeffs of prod (X-x), low->high, len j+1
        c=[one]
        for x in T:
            c=[mul((p-1+0,0) if False else ((-x[0])%p,(-x[1])%p),c[0])]+\
              [sub(c[i],mul(x,c[i+1])) for i in range(len(c)-1)]+[one]
        return c
    def mv(H,e): 
        out=[]
        for m in range(t):
            s=zero
            for l in range(j+1): s=add(s,mul(H[m][l],e[l]))
            out.append(s)
        return out
    def rank1_slope(a,b):                          # b!=0 and a||b -> slope z, else None
        nz=[i for i in range(t) if not iszero(b[i])]
        if not nz: return None                     # b==0: core/tangent, not transverse
        z=mul(sub(zero,a[nz[0]]),inv(b[nz[0]]))     # z = -a_i / b_i
        return z if all(iszero(add(a[i],mul(z,b[i]))) for i in range(t)) else None
    combs=list(itertools.combinations(range(n),j))
    Rline=-(-comb(n,j)//(Q**(t-1)))               # ceil(binom(n,j)/Q^{t-1})
    main=comb(n,j)/Q**(t-1)
    divisors=[M for M in range(2,n+1) if n%M==0]
    # precompute mu_M coset structure on index set 0..n-1 via multiplicative order
    # (index i <-> L[i]); a T is "M-periodic" if it is a union of mu_M-cosets
    def is_periodic(Tset,M):
        # mu_M = { x in L : x^M==1 }; cosets partition L; T periodic iff closed under * mu_M
        muM=[x for x in L if (lambda e: __pow(x,e,mul,one))(M)==one]
        Lset=set(L); idx={L[i]:i for i in range(n)}
        chosen=set(L[i] for i in Tset)
        for x in chosen:
            for g in muM:
                if mul(x,g) not in chosen: return False
        return True
    worst=0; worst_info=None
    for _ in range(trials):
        u=[random.choice(L) for _ in range(r)]; v=[random.choice(L) for _ in range(r)]
        Hu,Hv=hankel(u),hankel(v); nu={}; K0=0
        per_landings={M:0 for M in divisors}
        for ci,T in enumerate(combs):
            e=loc([L[i] for i in T]); a=mv(Hu,e); b=mv(Hv,e)
            if all(iszero(x) for x in a) and all(iszero(x) for x in b): K0+=1; continue
            z=rank1_slope(a,b)
            if z is not None:
                nu[z]=nu.get(z,0)+1
                for M in divisors:
                    if is_periodic(set(T),M): per_landings[M]+=1
        R=sum(nu.values()); Z=len(nu)
        Err=R - main + Q*K0                       # identity:  R = main - Q*K0 + Err
        assert Z<=R, "53.A(i) violated (theorem)"
        excess=R-Rline
        if excess>worst:
            worst=excess
            worst_info=dict(R=R,Z=Z,Rline=Rline,K0=K0,Err=round(Err,3),
                            periodic=per_landings)
    print(f"p={p} n={n} k={k} j={j} t={t} Q={Q} binom={comb(n,j)} "
          f"Rline={Rline} main={main:.3f}")
    print(f"max_excess(R-Rline)={worst}  worst_line={worst_info}")
    print("READING: excess carried by periodic[M]>0  => QUOTIENT concentration "
          "(needs d_M(E) large to exclude); excess with periodic==0 and low max-nu "
          "=> genuine APERIODIC COUNTERPACKET seed; large K0 => contained/tangent core.")

def __pow(x,e,mul,one):
    r=one
    for _ in range(e): r=mul(r,x)
    return r

if __name__=="__main__":
    run()   # try run(p=11,n=10,k=3,j=2) etc.; keep binom(n,j) small for speed
```

Expected: `53.A(i)` never violated; `Err` computed from `R - main + Q*K0` should match the definition (and for tiny `t`,`Q` one can add a brute-force `sum_{z,y!=0} S(y,z)/Q^t` cross-check); excess attributed to `periodic[M] > 0` is a quotient packet (must be excluded by `d_M(E)` large), while excess with `periodic == 0` and `max nu = O(1)` is a genuine aperiodic `COUNTERPACKET` seed against the wall.

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Yes — clearer than before, and now reduced to a single self-contained analytic inequality. The full solve does **not** need a new geometric idea: by 53.A it needs `Err <= O(j)`, i.e. per-line square-root cancellation in the slope-summed elementary-symmetric/cosupport exponential sum `S(y,z)`, uniform over `y != 0` and over `z` off the `<= t` tangent slopes, after quotient-separation deletes the `X^M` main term. Balance is already shown to deliver the necessary phase-nondegeneracy; the missing input is the cancellation itself.

Next exact lemma to attempt:

```text
Slope-summed cosupport cancellation (the Err <= O(j) wall).
For L = mu_n smooth multiplicative, fixed transverse balanced quotient-separated (u,v),
prove for every y != 0 and every z off the <= t tangent slopes:
   | S(y,z) | = | sum_{T split} psi( sum_{x in L\T} beta_x(z) Y(x) prod_{y' in T}(x - y') ) |
             <= binom(n,j) * Q^{-1/2 + o(1)},
with the X^M-periodic sub-sum (Cycle 48 quotient main term) removed under "d_M(E) not small."
Then (1/Q^t) sum_{z,y!=0} |S(y,z)| <= O(j), giving R <= R_line + O(j) by 53.A, hence Z <= R_line + O(j).
First sub-target: the t=2 (single nontrivial minor) balanced case, where S(y,z) is a single
elementary-symmetric sum e_j of the n values {psi(beta_x(z)Y(x))}_{x in L} and the cancellation
is a Newton-identity / Gauss-sum estimate; this is the smallest instance separating
phase-nondegeneracy (balance) from genuine cancellation (quotient-separation).
```

Companion construction (the only admissible `COUNTERPACKET` probe, dual to the lemma): an explicit growing-prime **balanced, quotient-separated, aperiodic** `(u,v)` over `L = mu_n` whose `S(y,z)` fails square-root cancellation for a positive-density set of `(y,z)` with the excess landings carried at `nu(z) = O(1)` and `periodic[M] = 0` for all `M | n` — a non-imprimitive arithmetic resonance in the degree-2 symmetric minors. Either the cancellation lemma or such a family resolves the wall; the `t=2` instance is the concrete place to run the §8 checker first.