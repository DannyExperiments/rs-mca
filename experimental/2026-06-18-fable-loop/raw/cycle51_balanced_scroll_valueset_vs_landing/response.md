I'll start by reading the file index, then the project files.I'll read the core project files first, then focus on the recent cycle material (49, 50, 51) and the Cycle44 anticollision wall.Now let me read the key recent cycle audits (49, 50) and the Cycle 44 anticollision audit, plus the active walls.Let me read the Cycle 50 full response, the active walls, and the Cycle 51 prompt that was actually sent.Let me read the Cycle 48 audit (quotient packets), Cycle 47 (variance/Bessel), the Cycle 44 response, and BANKED_LEMMAS to be precise about the L2 structure and the quotient hypotheses.I have the full picture: the Cycle 49 Hankel/scroll normal form, the Cycle 50 audit that split landing `R` from image `Z`, the Cycle 47 Bessel second-moment machinery, the Cycle 48 quotient-packet counterpacket, and the Cycle 44 cosupport L2-anticollision wall. Note this harness exposes only `Read` (no file-creation or execution tools), so — exactly as the Cycle 50 worker did — I deliver inline, with the checker as a runnable block for the director.

---

# Cycle 51 — Balanced Scroll Value Set vs Landing Count

Status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL`. Not `PROOF` of either bound, not `COUNTERPACKET`.

Confidence: high on the moment geometry (elementary), high on the decomposition and the direction-of-L2 route-cut, high on the Cycle 44 duality. The residual per-line bound stays open. Ledger kept separate: `C=RS[F,L,k]`, syndromes over `F`, `Q=|F|`; in the matched quadratic instantiation `Q=q_line=p^2`, `B=F_p`, `q_gen=p` untouched.

## 0. One-line verdict

`Z(u,v) <= R_line + O(j)` is, as a formal statement, strictly weaker than the landing bound `R(u,v) <= R_line + O(j)`. But **the weakening buys nothing with the tools currently in hand**, because every moment method (first moment, L2) bounds `R` or `M_2`, and the only elementary upper route to the image is `Z <= R`. The value-set version becomes genuinely easier than the landing version *only* if one switches to a direct image-count (monodromy / totally-split-density) method that does not pass through `R`. So this cycle reduces `W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING` to two named pieces and pins down exactly where the easier-ness can live.

## 1. Objects and the exact moment geometry

Fix the transverse Hankel pencil `P(z)=H(u)+zH(v)` (`t x (j+1)`), `t=r-j`. For a split locator `T` (monic squarefree fully-`L`-split, `|T|=j`), `a(T)=H(u)ell_T`, `b(T)=H(v)ell_T`. By Cycle 50 Lemma A a transverse `T` (`b(T)!=0`) realizes a *unique* slope `z(T)=-a(T)_m/b(T)_m`, so `z(.)` is a partial function on split locators. Define the fiber-multiplicity function on slopes `z in F`:

```text
nu(z) = #{ T split : b(T)!=0, rank[a(T)|b(T)]<=1, z(T)=z }.
R(u,v) = sum_z nu(z)        (total landings, L1 norm of nu)
Z(u,v) = #{ z : nu(z)>=1 }  (distinct slope image = MCA numerator, |supp nu|)
M_2     = sum_z nu(z)^2     (L2 norm squared)
```

### BANKABLE_LEMMA 51.A (moment sandwich; the only inequalities available)

```text
(i)   Z <= R                       [1[nu>=1] <= nu pointwise; equality iff nu in {0,1}]
(ii)  Z >= R^2 / M_2               [Cauchy-Schwarz: R = sum_{nu>0} nu*1 <= M_2^{1/2} Z^{1/2}]
(iii) Z >= R / max_z nu(z)         [R = sum nu <= Z * max nu]
(iv)  M_2 <= R * max_z nu(z)
(v)   R - Z = sum_z (nu(z)-1)_+    [the excess; this is the entire gap]
```

These are sharp: when `nu` is flat (all positive values equal) (i)-(iii) are equalities. This lemma is the spine of everything below.

The decisive structural fact: **`Z` is sandwiched as `R^2/M_2 <= Z <= R`, and BOTH walls of the sandwich are controlled by `R` (and `M_2`), never by an independent handle on the image.** There is no elementary inequality that upper-bounds `Z` from `M_2`.

## 2. Where `R_line` and `O(j)` come from: core/transverse split

By Cycle 50 Lemma B the moving fibers `M_z = ker P(z)/K0` are pairwise trivial-intersecting, so each transverse projected locator sits in exactly one `M_z`. Decompose the support of `nu` by the geometry of the realizing locators:

```text
Z = Z_tan + Z_mov,
Z_tan = #{ realized z whose locators meet the bounded core/directrix template }
Z_mov = #{ realized z carried by generic rulings of the degree-<=t moving scroll }.
```

`Z_tan` is the banked Cycle 48 template contribution: a fixed `k`-point tangent core, or a bounded-degree osculating/common-envelope directrix, contributes at most `(deg)*(j+1)` slopes. With degree `O(1)` after balanced reduction, `Z_tan = O(j)`. **This is exactly the `O(j)` term, and here the value-set framing is genuinely and unconditionally easier:** the template bounds the *image* `Z_tan <= j+1` directly, while the *landing* contribution of the same core is unbounded (a tangent core hosts arbitrarily many locators all landing on `<= j+1` slopes). So for the core, `R` is hopeless but `Z` is banked.

`Z_mov` is the transverse scroll part, whose anchor-averaged scale is `R_line`:

### BANKABLE_LEMMA 51.B (`R_line` is the averaged transverse landing, not a per-line image bound)

With `lambda = N/Q^t`, `N = binom(n,k+t)=binom(n,j)`, Cycle 47's first moment `E_w nu_w(z)=lambda` summed over the `Q` slopes gives

```text
sum_z E_w[nu_w(z)] = Q*lambda = N/Q^{t-1},
R_line = ceil(N/Q^{t-1}) = ceil( E_w[R(u,v)] ).
```

So `R_line` is the anchor-*expectation* of the transverse landing count, hence (by `Z<=R`) an averaged ceiling for `Z_mov` only on average. The deterministic per-line statement is not implied (Cycle 50 Route Cut 2). The conjecture `Z <= R_line + O(j)` is therefore precisely `Z_mov <~ R_line` (open) plus `Z_tan = O(j)` (banked).

## 3. ROUTE_CUT — L2 is the wrong direction; only `R` upper-bounds `Z`

This answers the L2 question with full precision and is the central cut of the cycle.

A per-line L2 / anticollision bound is a statement `M_2 <= B`. Feed it into Lemma 51.A: it can only enter through (ii) or (iv), and both yield

```text
Z >= R^2 / M_2 >= R^2 / B        (a LOWER bound on Z).
```

It is *consistent with* `Z = R` (flat `nu`, the equality case of (ii)). **Therefore an L2/anticollision bound gives no upper bound on `Z` whatsoever.** Concretely: small `M_2` means multiplicities are mostly `1`, which forces `Z` *up* toward `R`; it never forces `Z` down. The L2 estimate is a tool for showing the image is *large*, not small.

Consequence: to prove `Z <= R_line + O(j)` one must either

```text
(A) bound R(u,v) <= R_line + O(j)         (the stronger landing statement, Z<=R), or
(B) count the image |supp nu| directly    (a non-moment, structural/monodromy method).
```

There is no third elementary route. In particular, **the value-set bound is not accessible by the first-and-second-moment program at all** unless that program is used to bound `R` (route A), in which case one has proved the stronger statement anyway. This is the exact sense in which "weaker statement" does not mean "easier proof" here.

## 4. Are `Z`-bound and `R`-bound equivalent? (answers Q1, Q2)

The gap is `R - Z = sum_z (nu(z)-1)_+` (51.A(v)). It is nonzero exactly when some fiber has `nu(z) >= 2`, i.e. when a single ruling `M_z` of the moving scroll carries `>= 2` split locators. So:

- **They differ only through fiber multiplicity.** `R/max_z nu(z) <= Z <= R` (51.A i,iii). If `max_z nu(z) <= m`, then `Z` and `R` agree up to the factor `m`.

- **A high fiber `nu(z)` is a rich linear section.** `nu(z) = #(M_z cap Proj_V Split_L^sf)` is the number of fully-split squarefree degree-`j` locators on one ruling (dim `<= t`) of the reduced moving scroll. A ruling carrying `>> lambda` split locators is precisely a *locator-scroll-section* or a quotient/contained structure — the object of `W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT`.

- **What the hypotheses do.** Balanced minimal indices kill the *geometric* mechanism for a distinguished rich ruling (all indices in `{0,1}` in reserve scale, so no directrix of degree `>= 2`); no-quotient-action-rank-defect kills the *arithmetic* mechanism (`X^M` / bounded-defect `d_M(E)`). So the hypotheses are aimed exactly at `max_z nu(z)`, i.e. at the gap. **If they delivered `max_z nu(z) = n^{o(1)}`, then `Z` and `R` would be comparable up to `n^{o(1)}` and the two walls would coincide.** But (Cycle 50 Route Cut 1) balanced index alone does not exclude bounded-defect quotient packets, so this fiber bound is *not* delivered by the stated hypotheses — it is itself the open scroll-section inverse theorem.

Net answer to Q1/Q2. The honest dichotomy:

```text
- Tangent/core part:  Z_tan = O(j) is unconditionally easier than its R-part (banked template).
- Transverse part:    Z_mov-bound and R_mov-bound are NOT separable with present tools.
                      Comparability (Z~R) IS what quotient/balanced separation targets, but
                      proving it is the open wall, and even Z~R does not upper-bound either
                      without a separate handle on R.
```

So: value-set is strictly easier *only on the tangent core* (which is where multiplicity collapse genuinely lives and is already handled). On the transverse scroll, quotient/tangent separation makes `Z` and `R` *morally* equivalent without giving an upper bound on either.

## 5. EXACT_NEW_WALL — the only route that makes `Z` genuinely easier

The escape from §3 route (A) is route (B): count distinct slopes directly. The image is

```text
Z_mov = #{ z in F : ker(H(u)+zH(v)) contains a squarefree fully-L-split monic deg-j locator }.
```

This is a *splitting-type* count: the number of `z` for which the moving scroll's fiber over `z` meets the totally-split locus of `Split_L^sf`. That is a Chebotarev / Lang-Weil count for the family `z |-> P(z)`, indexed by the monodromy of the moving scroll over `F` — an honest image count that **never references `nu(z)` and so bypasses `R` and `M_2` entirely.**

```text
W-MCA-BALANCED-SCROLL-VALUESET-MONODROMY-DENSITY

Fix a transverse balanced (minimal indices in {0,1}) quotient-action-rank-
separated Hankel pencil over F. Let delta_split(P) be the F-density of slopes z
whose moving fiber M_z carries a fully-L-split squarefree degree-j locator.
Prove   Z_mov = Q * delta_split(P) + O(sqrt(Q) * deg)   <=   R_line + O(j),
i.e. bound the totally-split-fiber density of the degree-<=t moving scroll
directly, rather than through the landing count.
```

This is the route where the value-set version is *strictly* easier than the landing version, and it is exactly the machinery of Cycles 32-38 (quartic `S_4` monodromy, splitting-type histograms, finite-place certificates) — but used in the opposite direction. Cycle 43 already recorded the relevant phenomenon: along the balanced diagonal `j=2t -> infinity`, totally-split monodromy density is `<= 1/j -> 0`. **That `1/j` decay is a direct upper bound on `Z_mov`, not on `R`,** and it is the concrete reason to expect the value-set bound to hold even where the landing bound is delicate. The fixed-`t=2,j=4` `S_4` work gave positive split density (the *failure* direction, Cycle 43 cut its reserve-scaling); the balanced-diagonal density decay is the *safe* direction and is the right reserve-scale target.

## 6. Counterpacket target (answers Q4)

A valid `COUNTERPACKET` must violate the *image* bound, not the landing bound:

```text
Source-valid family (growing p), balanced minimal indices in {0,1}, no quotient-
action-rank defect (check d_M(E) for all proper M, not just syntactic X^M pullback),
core quotiented to tangent/common-envelope, all incidences transverse (b(T)!=0),
locators monic squarefree fully-L-split, with

   Z(u,v) > R_line + C*j     for every constant C,

and crucially the excess slopes carried with multiplicity nu(z)=O(1)
(so they are genuinely distinct transverse slopes, Z_mov large), NOT a tangent
core with huge R and Z_tan<=j+1.
```

Forbidden cheap versions (explicitly not counterpackets): (a) a tangent/common-envelope core with `R >> Z` but `Z <= j+1` — high landing multiplicity, small image; (b) a quotient/bounded-defect packet `E | m(X^M)` realizing `~binom(n/M-1,k/M)` slopes — these have many distinct slopes but are excluded by hypothesis and must be charged to `U_quotient`. The genuine target is an *aperiodic, non-tangent, balanced* moving scroll whose split locators populate `> R_line + O(j)` distinct rulings — an anti-equidistributed scroll section with no quotient symmetry. Equivalent monodromy phrasing: a balanced degree-`<=t` family with totally-split-fiber density bounded below by `> R_line/Q + O(j/Q)`, contradicting the `1/j` heuristic.

## 7. Relation to the Cycle 44 fixed-anchor anticollision wall (answers Q5)

They are **dual, on opposite sides of the entropy boundary, and the L2 estimate serves the other side**:

- Cycle 44 wants `N_split` (= image `Z`) *large* (the failure/lower branch, `c < H_2(rho)`). It uses `Z >= #Land^2/M_2` (51.A(ii)) and bounds `M_2` from above (the L2-anticollision `M_2 <= #Land + (1+o(1))#Land^2/q_line`). This is the *correct* direction for a lower bound on the image.

- Cycle 51 wants `Z` *small* (the safe/upper branch, above entropy). By §3 the very same L2 bound gives `Z >= R^2/M_2` — a lower bound — and is *useless* for the upper bound. The Cycle 44 anticollision wall, no matter how strong, cannot feed the Cycle 51 upper bound.

- The dictionary is exact (Cycle 50 Lemma 50.C): in the matched ledger `R(u,v)=#Land`, `nu` coincides, `R_line` equals the Cycle 44 banked main term `binom(p,j)/p^{2(t-1)}`. So Cycle 44 and Cycle 51 study the *same* `nu`, one pushing its support up via L2, the other needing its support pushed down via `R` or monodromy. The shared object is `nu`; the asymmetry is that L2 is one-directional (51.A(ii)).

This is the precise sense in which the fixed-anchor L2-anticollision program and the value-set-vs-landing program meet: identical multiplicity function, opposite quantifier, and the L2 tool only serves the failure branch.

## 8. Falsification / verification checker (unrun — for the director)

Tests 51.A (the sandwich, especially that L2 never upper-bounds `Z`), the core/transverse split, and searches a balanced quotient-separated family for `Z > R_line + Cj` with low-multiplicity excess (a `COUNTERPACKET` seed). I could not execute it here.

```python
# CHECKER.py — Cycle 51 value-set vs landing (pure Python, small fields)
import itertools, random

def run(p=7, k=2, t=2, trials=400, C=3):
    n=p; r=n-k; j=r-t
    assert t==r-j and 0<j<=r
    inv=[0]+[pow(a,p-2,p) for a in range(1,p)]
    def hankel(w):                       # t x (j+1)
        return [[w[m+l] for l in range(j+1)] for m in range(t)]
    def loc(T):                          # monic prod (X-x), low->high, len j+1
        c=[1]
        for x in T:
            c=[(-x*c[0])%p]+[(c[i]-x*c[i+1])%p for i in range(len(c)-1)]+[1]
        return c
    def mv(H,e): return tuple(sum(H[m][l]*e[l] for l in range(j+1))%p for m in range(t))
    def slope(a,b):                      # b!=0 ; return z if a||b else None
        nz=[i for i in range(t) if b[i]%p]
        if not nz: return None
        z=(-a[nz[0]]*inv[b[nz[0]]])%p
        return z if all((a[i]+z*b[i])%p==0 for i in range(t)) else None
    combs=list(itertools.combinations(range(n),j))
    Rline=-(-len(combs)//(p**(t-1)))     # ceil(C(n,j)/Q^{t-1}); toy Q=p
    bad=0
    for _ in range(trials):
        u=[random.randrange(p) for _ in range(r+ j)]  # enough syndrome entries
        v=[random.randrange(p) for _ in range(r+ j)]
        Hu,Hv=hankel(u),hankel(v)
        nu={}
        for T in combs:
            e=loc(T)
            a=mv(Hu,e); b=mv(Hv,e)
            z=slope(a,b)
            if z is not None: nu[z]=nu.get(z,0)+1
        R=sum(nu.values()); Z=len(nu); M2=sum(x*x for x in nu.values())
        assert Z<=R, "51.A(i) violated (theorem)"
        if R>0: assert Z*M2>=R*R, "51.A(ii) violated (theorem)"
        # value-set candidate with LOW-multiplicity excess (genuine Z-counterpacket)
        if Z>Rline+C*j and (max(nu.values()) if nu else 0)<=2:
            bad+=1; print("Z-COUNTERPACKET SEED: Z",Z,"Rline",Rline,"j",j,
                           "maxnu",max(nu.values()))
    print(f"p={p} k={k} t={t} j={j} Rline={Rline} trials={trials} seeds={bad}")

# Real ledger: replace toy Q=p with F_{p^2} (Q=p^2) and compute the slope via the
# Cycle 44 residue rho(T)=-ell*Lambda(T)^{-1}*N(T) so R(u,v)=#Land exactly (Lemma 50.C).
# A seed counts ONLY if max-multiplicity stays O(1) (else it is a landing artifact, not Z).
if __name__=="__main__": run()
```

Expected: 51.A(i),(ii) never violated (theorems); `seeds=0` for balanced quotient-separated lines supports the wall; any seed with `maxnu=O(1)` is a genuine value-set `COUNTERPACKET` lead.

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Yes, and this cycle clarifies which route. The value-set framing does not lower the bar on the transverse scroll via moments — §3 shows the moment program only reaches `R` and `M_2`, and `Z`'s upper face is `Z <= R`. The genuine easier-ness lives in two places: (1) the tangent/core part, where `Z_tan = O(j)` is already banked while `R` is hopeless; (2) the direct image-count, where the totally-split-fiber density of the balanced moving scroll is bounded *without* `nu`. So a full solve should stop trying to upper-bound `Z` through `R` and instead bound the splitting density directly.

Next exact lemma to attempt:

```text
Balanced-scroll totally-split density decay.
For a transverse balanced (minimal indices in {0,1}) quotient-action-rank-
separated Hankel pencil P(z)=H(u)+zH(v) over F, let X -> A^1_z be the cover whose
fiber over z is the intersection of the moving ruling M_z with the split-locator
locus. Compute the geometric monodromy G_geom of this degree-<=t family and prove
   delta_split(P) = (#{g in G_geom : g totally split-compatible}/|G_geom|) + o(1)
   <= 1/j + o(1)        (Cycle 43 balanced-diagonal heuristic),
so that  Z_mov = Q*delta_split + O(sqrt Q * deg) <= R_line + O(j)  by Lang-Weil,
WITHOUT bounding R(u,v). Pair this with the banked Z_tan=O(j) template.
```

Companion construction (the dual `COUNTERPACKET` probe): an explicit growing-prime balanced quotient-separated `(u,v)` whose moving scroll has anomalously high totally-split density (`delta_split >> 1/j`) with `O(1)` fiber multiplicity. Either the density-decay lemma or such a family resolves `W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING`; the monodromy machinery of Cycles 32-38, re-aimed at density decay in reserve scale rather than fixed-regime positive density, is the concrete next tool.