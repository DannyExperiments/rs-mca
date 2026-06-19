I'll start by reading the file index and project source files.I'll read the core orientation files first, then the cycle-specific context.Let me read the cycle 49 prompt, the recent cycle 47/48 audits, and the key state files in parallel.Now the cycle 47 and 48 audits, plus the active walls and banked lemmas.Now the active walls, banked lemmas, and false routes.Let me read the agents instructions, the false routes ledger, and the cycle 47 audit.Now the cycle 47 audit, false routes, and route board.Let me read the route board, banked lemmas, and the cycle 48 detailed outputs.# Cycle 49 — Syndrome Transverse-Secant Inverse: Theorem-Worker Answer

I have read the Cycle 47/48 audits, the active walls, banked lemmas, the route board, and the cut ledger. Here is my contribution. I do **not** claim a `PROOF` of the inverse theorem or a `COUNTERPACKET`; both would be prize-level and neither is honestly in hand. I bank an exact normal form and a genuine dimension-reduction of the wall, cut one tempting route, and state the next exact wall.

Status: `BANKABLE_LEMMA` / `ROUTE_CUT` / `EXACT_NEW_WALL`. Confidence: high on the linear-algebra reductions (they are elementary or follow from Kronecker pencil theory); the residual inverse theorem is open.

Field ledger kept separate throughout: `C = RS[F,L,k]`, syndromes live over `F`, `Q=|F|=q_line` in the instantiation, `B`/`q_gen` untouched. No ledger is merged.

---

## 1. The exact object, made concrete (recall + sharpening)

For `RS[F,L,k]` the standard parity check has columns `h_x = lambda_x v(x)`, `v(x)=(1,x,...,x^{r-1})^T`, `lambda_x = prod_{y!=x}(x-y)^{-1}`, `r=n-k`. The scalars `lambda_x` do not move spans, so for `T subset L`, `|T|=j`,

```text
W_T = span{ v(x) : x in T },     dim W_T = j   (distinct points on the rational normal curve),
W_T^perp = L_T * F[X]_{<sigma_T}  with  L_T = prod_{x in T}(X-x),  inside F[X]_{<r}.
```

The codimension of `W_T` is exactly `r - j = t`. **This is the answer to the required `t<sigma`/`t=sigma`/`t>sigma` check:** the denominator degree is `t = r - j`, and varying `j` in `Pi_j(C)` runs through *all* denominator degrees in one object. The reserve-balanced case is `j_0 = r - sigma` (i.e. `t=sigma`); `j>j_0` is `t<sigma`, `j<j_0` is `t>sigma`. The syndrome formulation genuinely subsumes the three cases — they are single instances of the same `Pi_j`, not separate problems.

Pairing `<g,w> = sum_i g_i w_i` for `deg g < r`, the membership `u+zv in W_T` is

```text
< X^m L_T , u+zv > = 0,   m = 0,...,t-1.
```

Writing `L = sum_{l=0}^{j} ell_l X^l` (monic, `ell_j=1`) one has `<X^m L, w> = sum_l ell_l w_{m+l}`. Hence the realizability of a slope is governed by a **Hankel matrix**.

---

## 2. BANKABLE_LEMMA A — Hankel-pencil normal form for `Pi_j`

Define the `t x (j+1)` Hankel matrix of a syndrome `w in F^r` (`t = r-j`):

```text
H(w)_{m,l} = w_{m+l},   0 <= m <= t-1,  0 <= l <= j.
```

`H` is `F`-linear in `w`, so `H(u+zv) = H(u) + z H(v)` is a **`t x (j+1)` Hankel matrix pencil**. Then exactly:

```text
u + zv in W_T   <=>   H(u+zv) * ell_T = 0,   ell_T = coeff vector of L_T.
```

Therefore

```text
Pi_j(C) = max_{u,v}  #{ z in F :  ker( H(u)+zH(v) )  contains a squarefree, monic,
                                   fully-L-split, degree-j polynomial L_T,
                                   with H(v) ell_T != 0 (transversality v notin W_T) }.
```

A transverse split locator `ell_T` lies in `ker(H(u)+zH(v))` for a **unique** `z` (the common ratio `z = -(H(u)ell_T)_m / (H(v)ell_T)_m`); the degenerate case `H(u)ell_T = H(v)ell_T = 0` is "realized for all z" and is the contained/common-envelope template. This is exact, covers all `t = r-j`, and replaces the residue-line/co-support `e`-coordinate description (Cycle 44) by a single classical Berlekamp–Massey/Hankel pencil. It is the precise finite form of "transverse intersections of a line with the `j`-secant subspace arrangement."

---

## 3. BANKABLE_LEMMA B — Core/moving splitting (the dimension reduction)

This is the part that **materially shrinks the wall**.

**Intrinsic common core.** Set

```text
K0 := intersection_{z} ker(H(u)+zH(v)) = ker H(u) ∩ ker H(v).
```

By the trivial subspace-dimension bound (no pencil theory needed),

```text
dim K0 >= 2(j+1-t) - (j+1) = j + 1 - 2t.
```

**Moving part.** For generic `z`, `dim ker(H(u)+zH(v)) = j+1-t` (full row rank = the non-tangent/non-contained hypothesis; rank-deficiency is the tangent template). Write

```text
L_z := ker(H(u)+zH(v)) = K0 ⊕ M_z,    dim M_z = (j+1-t) - dim K0 <= t.
```

So the moving locator family `M_z` lives in the quotient

```text
V := F[X]_{<=j} / K0,    dim V = (j+1) - dim K0 <= 2t,
```

and has dimension `<= t` there.

**Kronecker refinement.** As a `t x (j+1)` pencil of generic rank `t`, by Kronecker's canonical form the kernel is spanned by `p = j+1-t` polynomial-in-`z` vectors of right minimal indices `eps_1,...,eps_p` with

```text
sum_i eps_i  <=  t.
```

Hence `#{ i : eps_i >= 1 } <= t` (so `dim M_z <= t`, recovering the above), the constant (`eps_i=0`) generators span `K0`, and the **moving locator scroll**

```text
S := closure( union_z M_z )  ⊂  P(V)
```

is a rational normal scroll of **degree `<= t`** and dimension `<= dim M_z + 1 <= t+1`.

**Consequence (the reduction).** The slope of a transverse split locator depends only on its image `bar ell_T in V` (project out `K0`), and is recovered as a degree-`<= t` scroll coordinate `pi : S --> P^1`. Therefore

```text
Pi_j(C)  <=  #{ z in F :  M_z  ∩  Proj_V(Split_L^sf)  != empty } + (contained-core slopes),
```

where `Proj_V(Split_L^sf)` is the image in the `<=2t`-dimensional space `V` of the `binom(n,j)` squarefree split locators.

**What this buys.** The inverse problem is transported from the ambient dimension `r = Theta(n)` down to the reduced moving space of dimension `<= 2t = 2 sigma = Theta(n/log Q)`, with the slope a degree-`<= t` rational function of the projected locator. This is the exact, basis-free sharpening of the Cycle 48 "support-syndrome space of dimension `sigma`" and "locator-scroll circuit": the circuit is now the Kronecker minimal-index structure, and "the locator span does not meet `E F[X]_{<=j-t}`" becomes "`M_z` avoids `Proj_V(Split_L)` off a degree-`<=t` scroll."

---

## 4. ROUTE_CUT — core removal + scroll-degree is *not* by itself an `O(n)` bound

It is tempting to conclude from "scroll degree `<= t`" and "common core `K0` removed" that the realized slopes are roots of one bounded-degree resultant, hence `O(n)`. **This is false / not source-valid**, and must be removed as a route:

- The scroll `S` has codimension `t-1` and degree `<= t` in `P(V)`, but `Proj_V(Split_L^sf)` is a **structured** configuration, not in general position. A codimension-`(t-1)` degree-`t` variety can contain an unbounded number of structured points (e.g. a sub-configuration lying on a linear section of the scroll).
- Concretely, when `L` is a smooth multiplicative domain and the moving scroll aligns with a quotient `X^M`, the projection `Proj_V(Split_L^sf)` collapses with high multiplicity onto a low-dimensional sub-scroll, and the realized-slope count is the Cycle 48 quotient-component value `~ binom(n/M-1, k/M)`, which exceeds any `O(n)` and even `n^{1+o(1)}` above the ambient entropy boundary.

So core-removal handles only the contained/tangent/common-envelope template (the `K0` part); the **moving** problem in `V` is exactly where the quotient-component and fixed-defect quotient-anchor packets live. Do not bank "core removal ⟹ linear slope count."

---

## 5. Quotient identification + finite numerator

The Cycle 48 invariant matches the pencil invariants exactly:

```text
quotient-component packet  <=>  unbalanced right minimal indices of H(u)+zH(v):
                                 one large eps_i carrying almost all of sum eps_i <= t,
                                 i.e. the moving scroll S is (close to) a cone over a
                                 low-degree directrix aligned with the multiplicative
                                 quotient X^M; equivalently d_M(E) small.
```

The extreme `d_M(E)=1` (punctured-fiber coequalizer) is the maximally unbalanced index `(eps_1,...) = (t,0,...,0)`: the moving part is a single degree-`t` rational curve and `Proj_V(Split_L)` concentrates on it.

Finite numerator (replacing any `n^{1+o(1)}`): with `N = binom(n,k+t) = binom(n,j)` and the random line-occupancy scale `R_line = ceil(N/Q^{t-1})`, the conjectural finite shape is

```text
Pi_j(C) <= U_quotient + R_line + A_theta(n),
```

with `A_theta(n)` the contained/tangent budget `<= (j+1)·#{common-envelope templates}` charged to `K0`, and `U_quotient` charged to the unbalanced-index scrolls. At the center `Q^t = N`, `R_line = Q` and the statement is vacuous, as required.

---

## 6. EXACT_NEW_WALL

```text
W-MCA-REDUCED-MOVING-SCROLL-INCIDENCE
```

In the reduced space `V = F[X]_{<=j}/K0` (`dim V <= 2t`), with `M_z ⊂ V` the moving kernel of `dim <= t` swept by the degree-`<= t` Kronecker scroll `S`, prove:

> After removing unbalanced-minimal-index (quotient-component) scrolls and the `K0` (contained/tangent) core, the number of slopes `z` with `M_z ∩ Proj_V(Split_L^sf) != empty` is at most `R_line + A_theta(n)`.

Equivalently, in the labelled-subspace-design form `W_{E,B}=F^L/(E·RS[F,L,k]+F·B)`: classify support-families whose projected label `bar ell_T |-> pi(bar ell_T) in P^1` takes more than `R_line + A_theta(n)` distinct values; the only allowed outcomes are (i) a low-`eps` quotient scroll (multiplicative quotient packet), (ii) a fixed-defect quotient-anchor packet (large `K0` aligned to a coset profile), or (iii) a bounded tangent/common-envelope template `K0`.

The first concrete sublemma I would attack next is **balanced-index incidence**: when all right minimal indices are equal/balanced (the genuinely aperiodic case, no quotient), show `Proj_V(Split_L^sf)` is in "general enough" position with respect to the balanced scroll that incidence is `<= R_line + (j+1)`. This is the smallest missing object and is a clean Hankel-pencil-vs-configuration statement, free of the residue-coordinate bookkeeping.

---

## Do you see a route to a full solve?

Partially, and more clearly than before, but not a closed route yet. The syndrome reformulation plus the core/moving Kronecker reduction turn the positive-side wall into one well-posed problem in a `<= 2sigma`-dimensional space: bound transverse incidences of a degree-`<= sigma` moving scroll with the projected split-locator configuration, after deleting unbalanced (quotient) scrolls and the contained core. That is a real compression of the `r ≈ n` ambient problem and it correctly contains the Cycle 48 counterpacket as the unbalanced-index degeneration.

Next exact lemma/construction:

```text
Prove the balanced-minimal-index case of W-MCA-REDUCED-MOVING-SCROLL-INCIDENCE:
if H(u)+zH(v) has all right minimal indices within 1 of each other, then
  #{ z : M_z meets Proj_V(Split_L^sf) }  <=  R_line + (j+1),
with R_line = ceil(binom(n,k+t)/Q^{t-1}).
```

A proof of the balanced case plus the already-banked quotient-component classification would give the two-sided entropy transition (matching the Cycle 47 lower branch); a balanced-index source-valid family exceeding `R_line + A_theta(n)` would instead be a genuine `COUNTERPACKET` not covered by any existing template. Either resolves the wall.