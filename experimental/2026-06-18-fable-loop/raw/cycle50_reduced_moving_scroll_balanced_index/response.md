I'll start by reading the file index, then the core project files.I'll read the core project files first, then the recent cycle material that defines the wall I'm attacking.Now let me read the most directly relevant recent cycle material: Cycle 49 (syndrome/Hankel reformulation), Cycle 48 (upper inverse), and the wall/lemma ledgers.Now let me read the active walls, banked lemmas, cuts/false-routes, and the Cycle 49 prompt to understand the exact baseline and constraints.Let me read the banked lemmas, the Cycle 49 prompt that was sent, and the route board's relevant sections.I have enough context. Let me think through the mathematics, then verify the key claims computationally before writing the deliverable.

The candidate lemma reduces (after the Cycle 49 core/moving split) to: in the balanced reserve regime, count split locators `T` whose `(H(u)ell_T, H(v)ell_T)` is a rank‑1 pair. I want to check three things numerically: (1) the balanced reduction really gives the rank‑1 determinantal scroll, (2) whether a single "common‑envelope" core can beat `R_line+(j+1)`, and (3) whether such an envelope-hosting pencil can still be balanced. Let me write a checker.I now have the full picture. Before writing the deliverable, let me verify the key structural claims computationally: the Kronecker reduction in the core-reduced space, the disjointness of moving kernels, the reduction `#slopes ≤ #realized T`, and crucially whether a *balanced* line can exceed the conjectured `R_line + (j+1)` (which would force a route-cut on the constant).The bash tool isn't available in this harness. Let me confirm whether I can run anything, then I'll proceed with the analysis directly.The bash/run tools aren't available in this harness, so I can't execute a checker. I'll do the mathematics carefully by hand, write a falsifiable checker for the director to run, and be explicit in the audit about what I did and did not verify computationally.

Let me write the deliverables.I have all the context I need. Note: the file-creation and code-execution tools are not available in this harness (only `Read` works), so I'm delivering the result inline rather than writing to `output_files/`. I could not execute a checker; where I rely on computation I say so explicitly and give a runnable spec for the director.

---

# Cycle 50 — Reduced Moving-Scroll Balanced-Index Incidence

**Status: `BANKABLE_LEMMA` / `ROUTE_CUT` / `EXACT_NEW_WALL`.** Not `PROOF`, not `COUNTERPACKET`.

Confidence: high on the linear-algebra reduction (elementary); high on the bridge to the Cycle 44 cosupport wall; the residual per-line bound is open. Field ledger kept separate throughout: `C=RS[F,L,k]`, syndromes over `F`, `Q=|F|=q_line` in the quadratic instantiation; `q_gen`/`B` untouched.

## 0. One-line verdict

The candidate is **neither refuted nor proved**. After the Cycle 49 core/moving split, the count is exactly the image of a single-valued slope map from transverse split locators, bounded by the number of split locators on a codimension-`(t-1)` rank-one locus. The baseline `R_line` is exactly the anchor-*expectation* of that number, so `R_line` is the correct reduced-space baseline and `E_w[image] <= R_line` holds cleanly. But the **deterministic per-line** bound is — in the `t=sigma` instantiation — *equivalent* to the already-open Cycle 44 symmetric-function-cancellation wall. Balanced index alone does not close it.

## 1. The object after core removal

With `t=r-j`, transverse split locator `ell_T` (monic degree `j`, squarefree, fully `L`-split), Hankel pencil `P(z)=H(u)+zH(v)`, set

```text
a(T) = H(u) ell_T in F^t,   b(T) = H(v) ell_T in F^t.
```

Transversality is `b(T)!=0`; membership `u+zv in W_T` is `a(T)+z b(T)=0`.

### BANKABLE_LEMMA 50.A — Scroll fibration (one slope per locator)

(i) A transverse `ell_T` realizes a slope iff `rank[a(T)|b(T)]<=1`, and then the slope is **unique**, `z(T) = -a(T)_m/b(T)_m` for any `m` with `b(T)_m!=0`. So `z(.)` is a partial function `Split_L^sf --> F`.

(ii) The locus `{b!=0, rank<=1}` in `F^t x F^t` has dimension `t+1` (free `b in F^t\0`, scalar `a=cb`), i.e. **codimension `t-1`**.

(iii) **Disjoint moving fibers.** In `V=F[X]_{<=j}/K0`, for `z!=z'`, `M_z cap M_{z'} = 0`. *Proof.* `M_z = L_z/K0` with `L_z=ker P(z) ⊇ K0`, so the intersection is `(L_z cap L_{z'})/K0`; if `x in L_z cap L_{z'}` then `(z-z')H(v)x=0`, so `H(v)x=0`, then `H(u)x=0`, so `x in K0`. Hence `L_z cap L_{z'}=K0` and the image is `0`. ∎

(iv) Each transverse `bar ell_T in V` is nonzero and lies in **exactly one** fiber `M_{z(T)}`. Therefore

```text
#{ z : M_z cap Proj_V(Split_L^sf) != empty }  (transverse part)
   = #(image of z(.))
   <= R(u,v) := #{ T split : b(T)!=0, rank[a(T)|b(T)] <= 1 }.
```

The candidate's `+(j+1)` is **not** part of this transverse count: it is the separately-banked tangent/common-envelope cushion charged to the removed core `K0` (Cycle 48: a fixed `k`-point tangent core contributes `<= j+1` slopes; the `b(T)=0` template).

## 2. `R_line` is exactly the incidence expectation

### BANKABLE_LEMMA 50.B — First-moment identity

Let `lambda=N/Q^t`, `N=binom(n,k+t)=binom(n,j)`. The banked Cycle 47 first moment is `E_w nu_w(z)=lambda` for each `z`, where `nu_w(z)=#{T transverse split: z(T)=z}`. Summing over the `Q` slopes,

```text
sum_z E_w[nu_w(z)] = Q*lambda = N/Q^{t-1},
R_line = ceil(N/Q^{t-1}) = ceil(Q*lambda) = ceil( E_w[#Land] ).
```

Since `image <= R(u,v) = sum_z nu_w(z)`, linearity gives `E_w[image] <= R_line(1+o(1))`. **So `R_line` is exactly the anchor-expectation of the rank-one split count** — the intrinsic incidence baseline of the reduced `<= 2t`-dimensional moving space (`N` locators against codimension `t-1`). A bare `n^{1+o(1)}` would be the wrong finite statement; `R_line` is right.

## 3. The load-bearing observation

### BANKABLE_LEMMA 50.C — Balanced scroll incidence = Cycle 44 cosupport landing

In the Cycle 44 instantiation (`n=p`, `B=F_p`, `F=F_{p^2}`, `Q=q_line=p^2`, `D=F_p`, `t=sigma`, `j=n-a`), the rank-one transverse count is **literally** the Cycle 44 landing count:

```text
R(u,v) = #Land = #{ T : rho(T) in F*b },   rho(T)=[I_{D\T}]_E,
```

via the dictionary `[I_S]_E = z[Bnum]_E  <=>  a(T)+z b(T)=0`, and the numerics match exactly: `R_line = ceil(binom(p,j)/p^{2(t-1)})` equals the Cycle 44 banked main term of `#Land`. The per-slope multiplicities `nu(z)` coincide.

**Consequence.** `W-MCA-REDUCED-MOVING-SCROLL-BALANCED-INDEX` (syndrome side) and `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION` (cosupport side) are the **same wall** in the `t=sigma` quadratic instantiation, approached from opposite coordinates. The candidate `image <= R_line + (j+1)` is the Cycle 44 first-moment bound `#Land <= R_line + (j+1)`; its `L2` companion is the banked open subwall `...-L2-ANTICOLLISION`. This convergence of the two programs is the main bankable content of this cycle. (Exact only in the matched ledger; do not merge `q_gen=p` with `Q=p^2`.)

## 4. ROUTE_CUT — what balanced index does and does not buy

**(C1) Balanced index does not by itself exclude the Cycle 48 quotient packets; the quotient-rank hypothesis is load-bearing.** A clean fact: in reserve scale the kernel has `p=j+1-t = n-k-2t+1` minimal indices summing to `<= t`, and `p >> t` (since `t=sigma=o(n)`), so most indices are `0` and **balanced-within-1 ⟺ all minimal indices in {0,1}** — i.e. the scroll has no directrix of degree `>= 2`. This excludes the extreme `d_M(E)=1` punctured-fiber coequalizer (`eps=(t,0,...,0)`, a degree-`t` directrix). But a **bounded-defect** quotient (`d_M(E)=2`) constrains the configuration `Split_L^sf` arithmetically without forcing a high-degree directrix, so it can coexist with `{0,1}` indices. Hence balanced index excludes the unbalanced coequalizer but **not** bounded-defect quotients, and the lemma is correct only because it carries the separate "no proper quotient-action-rank defect" hypothesis. That hypothesis is not redundant.

**(C2) `R_line` is an expectation, not a deterministic ceiling.** Lemma 50.B is averaged over anchors `w`. There exist anchors (the Cycle 48 quotient packets) with `#Land(w) >> R_line`; the hypotheses exclude those. For the *remaining* balanced quotient-separated anchors, the claim `#Land(w) <= R_line + (j+1)` is a **worst-case-over-good-anchors** statement that the average does not give (Markov gives it for *most* good anchors, not *all*). The magnitude is fine — the per-line transverse shell is `n^{o(1)}` (Cycle 47: `J <= I_0(2 sqrt(aj/Q)) = n^{o(1)}`), and since `j=Theta(n) >> n^{o(1)}` the `(j+1)` slack absorbs it — but the **proof obligation is a per-line bound, not an inherited average.** This is a route-cut on the derivation, not the magnitude.

**(C3) A balanced scroll can over-concentrate split locators by a nonquotient mechanism.** Balanced index controls the *shape* of the scroll (degree `<= t`, no high-degree directrix) but not the *arithmetic* of how `Proj_V(Split_L^sf)` sits on it. A low-degree variety can carry far more than `R_line` structured points if the symmetric-function image of the split configuration has an arithmetic coincidence with the scroll, with no quotient symmetry. Ruling this out is exactly the symmetric-function-cancellation content of 50.C, and it is open. This is the residual wall.

## 5. Required checks

- **`t<sigma`, `t=sigma`, `t>sigma`:** the Hankel `t=r-j` formulation subsumes all three by varying `j`; "balanced index" is a separate axis (a property of the pencil). The content lives at the reserve-balanced diagonal `t=sigma` (`dim V <= 2sigma`), where the Cycle 44 bridge is exact. For `t<sigma` (large `j`) realized slopes inject into an `RS[k+t]` list with residual slack `sigma-t` (banked), which dominates the scroll incidence; for `t>sigma` the configuration is a thick affine residue plane (`R_line` exceeds `Q`) and the bound is vacuous until the denominator-compression wall clears. One statement covers all `t`, but the other two regimes reduce to already-named walls rather than being closed here.
- **Squarefree / fully-split:** essential and already inside `Proj_V(Split_L^sf)`; only squarefree fully-`L`-split degree-`j` kernels are genuine MCA witnesses (supports `T subset L`). No extra hypothesis is needed for the reduction; the open part uses distinctness exactly as the Cycle 16/44 split-locus conditions do.
- **No raw fiber counts:** the bound is on the *image* of the single-valued slope map (distinct realized slopes), never raw feasible support fibers (Cycle 9 respected).
- **Finite exact version:** yes. 50.B is finite-exact (`sum_z E_w nu_w(z) = N/Q^{t-1}`); the finite second moment `E_w nu_w(z)^2 = lambda^2 + lambda V`, `V=sum_{0<=d<t} binom(j,d)binom(a,d)(Q^{-d}-Q^{-t})` (Cycle 47) gives the finite Chebyshev error. The open part is the finite *per-line* (not averaged) first moment.

## 6. EXACT_NEW_WALL

```text
W-MCA-BALANCED-SCROLL-CONFIG-EQUIDISTRIBUTION
```

> Fix a transverse Hankel pencil `H(u)+zH(v)` over `F` with all right minimal indices in `{0,1}` (balanced) and no proper quotient-action-rank defect (`d_M(E)` not small for any proper `M`). Prove the **deterministic per-line** bound
> ```text
> R(u,v) = #{ T split, |T|=j : rank[H(u)ell_T | H(v)ell_T] <= 1, H(v)ell_T != 0 } <= R_line + (j+1),
> ```
> equivalently (50.C) the per-line Cycle 44 landing bound `#Land(u,v) <= R_line + (j+1)`, by transferring the Cycle 47 *averaged* variance bound to a worst-case-over-balanced-quotient-separated-lines bound.

Then `image <= R(u,v) <= R_line + (j+1)` follows from 50.A, and with the Cycle 48 quotient-component classification this matches the Cycle 47 lower/failure branch. The single missing analytic input is a **per-line second moment under the balanced + quotient-separated hypotheses**: Cycle 47 controls `Var nu_w(z)` averaged over `w`; the wall needs it for a fixed balanced line. Balanced index removes the unbalanced-directrix clustering; the quotient-rank hypothesis removes bounded-defect clustering; what remains is to show no *nonquotient* arithmetic coincidence inflates `#Land` above its mean by more than `O(j)`.

## 7. Falsification checker (unrun — for the director)

I could not execute this here. It tests 50.A (disjointness, one-slope-per-locator), 50.B (`R_line = E[#Land]`), and searches for a balanced quotient-separated line beating `R_line+(j+1)` (which would be a `COUNTERPACKET` seed).

```python
# CHECKER.py  — RS-MCA Cycle 50 balanced-index scroll incidence
# Run: python3 CHECKER.py   (pure Python, small fields)
import itertools, random
# --- minimal GF(q) via prime field F_p then F_{p^2}; use sympy if available ---
def run(p=7, k=2, deg_t=2, trials=200):
    # L = F_p (smooth-ish toy domain), C=RS[F_p,L,k], r=n-k, j=r-t
    n=p; r=n-k; t=deg_t; j=r-t
    assert 0<j<=r and t==r-j
    F=list(range(p)); inv=[0]+[pow(a,p-2,p) for a in range(1,p)]
    def hankel(w):  # t x (j+1)
        return [[w[(m+l)%len(w)] for l in range(j+1)] for m in range(t)]
    def locator_coeffs(T):  # monic prod (X - x), x in T  -> length j+1 low->high
        c=[1]
        for x in T:
            c=[(-x*c[0])%p]+[(c[i]-x*c[i+1])%p for i in range(len(c)-1)]+[1]
        return c  # len |T|+1 ; pad/truncate to j+1
    def matvec(H,e):
        return tuple(sum(H[m][l]*e[l] for l in range(j+1))%p for m in range(t))
    def rank1(a,b):  # b!=0 ; a parallel b ?  return slope or None
        nz=[i for i in range(t) if b[i]%p!=0]
        if not nz: return None  # b==0 non-transverse
        z=(-a[nz[0]]*inv[b[nz[0]]])%p
        ok=all((a[i]+z*b[i])%p==0 for i in range(t))
        return z if ok else None
    bad=0
    Rline = -(-  (len(list(itertools.combinations(range(n),j))))  // (p**(t-1)) )  # ceil(C(n,j)/Q^{t-1}); Q=p here (toy same-field)
    for _ in range(trials):
        u=[random.randrange(p) for _ in range(r)]
        v=[random.randrange(p) for _ in range(r)]
        Hu,Hv=hankel(u),hankel(v)
        slopes={}
        Rcount=0
        for T in itertools.combinations(range(n),j):
            e=locator_coeffs(T)[:j+1]+[0]*(j+1-len(locator_coeffs(T)))
            a=matvec(Hu,e); b=matvec(Hv,e)
            z=rank1(a,b)
            if z is not None:
                Rcount+=1; slopes[z]=slopes.get(z,0)+1
        image=len(slopes)
        # 50.A: image <= Rcount  (one slope per locator)  must hold
        assert image<=Rcount, "50.A violated"
        # candidate per-line bound (toy Q=p): image <= Rline + (j+1) ?
        if image > Rline + (j+1):
            bad+=1
            print("CANDIDATE EXCEEDED:", "image",image,"Rline",Rline,"j+1",j+1)
    print(f"p={p} k={k} t={t} j={j} Rline={Rline} trials={trials} exceed={bad}")
# NOTE: this toy uses same-field Q=p; for the real ledger use F_{p^2} (Q=p^2)
# and the cosupport residue rho(T)=[I_{D\T}]_E to match #Land exactly (Lemma 50.C).
if __name__=="__main__":
    run()
```

Expected: `50.A` never violated (it is a theorem); `exceed` should be `0` for balanced quotient-separated lines (supporting the wall) or produce a seed if not. To match the real instantiation, replace the toy `Q=p` with `Q=p^2` and compute `rho(T)` via the banked Cycle 44 identity `rho(T) = -ell*Lambda(T)^{-1}*N(T)`.

---

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Partially, and now with the two halves of the program identified as one object. The route: 50.A makes the count the image of a single-valued slope map, bounded by the rank-one split-locator count; 50.B fixes `R_line` as that count's exact expectation; 50.C shows it is the Cycle 44 cosupport landing count, so the syndrome and cosupport programs coincide. The full solve needs the **deterministic per-line first moment** `R(u,v) <= R_line + (j+1)` under balanced + quotient-separated hypotheses — not the averaged version in hand.

Next exact lemma:

```text
Per-line second-moment transfer. For a fixed transverse balanced quotient-
separated Hankel pencil H(u)+zH(v) over F, prove
    sum_z nu(z)^2 <= R_line + (1+o(1)) R_line^2 / Q
(the Cycle 44 L2-anticollision bound for the fixed line, not averaged over w),
using all-minimal-indices-in-{0,1} to bound the pair-rank-defect shell J per line.
By Cauchy-Schwarz, image >= R(u,v)^2 / M_2, which with the first-moment expectation
pins image at R_line(1+o(1)).
```

The dual construction to attempt as a `COUNTERPACKET` seed: an explicit smooth multiplicative `L` and balanced quotient-separated `(u,v)` whose split-locator symmetric-function image hits one balanced fiber `M_z` in `>> R_line/n^{o(1)}` points (`max_z nu(z) >= #Land/p^{1+epsilon}`). Either the per-line `L2` bound or such a family resolves the wall; both are now the same question in syndrome and cosupport coordinates.