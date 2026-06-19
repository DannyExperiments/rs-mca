# Cycle 53 Prompt: Per-Line Symmetric Determinantal Incidence

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project files and recent loop material first. Preserve the labels
`PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`, and
`EXACT_NEW_WALL` literally.

## Current Route State

Cycles 49-52 have narrowed the positive/safe-side MCA upper wall.

1. Syndrome/Hankel normal form:

   ```text
   u+zv in W_T  <=>  (H(u)+zH(v)) ell_T = 0,
   ```

   where `ell_T` is the coefficient vector of the monic locator
   `L_T(X)=prod_{x in T}(X-x)`, `|T|=j`, and `t=r-j`.

2. Core/moving reduction:

   ```text
   K0 = ker H(u) cap ker H(v),
   V = F[X]_{<=j}/K0,
   dim V <= 2t.
   ```

   The moving kernels `M_z` are pairwise disjoint after quotienting `K0`.

3. Rank-one incidence:

   ```text
   a(T)=H(u)ell_T,
   b(T)=H(v)ell_T.
   ```

   A transverse locator realizes a unique slope iff

   ```text
   b(T) != 0 and rank[a(T)|b(T)] <= 1.
   ```

4. Actual MCA numerator:

   ```text
   Z(u,v) = #{z : exists split T with z(T)=z}.
   ```

   Total landing count:

   ```text
   R(u,v) = #{T split : b(T)!=0, rank[a(T)|b(T)]<=1}.
   ```

   `Z<=R`. A bound on `R` is sufficient but stronger than the MCA numerator
   bound.

5. Cycle51 cut the L2 route for upper bounds:

   ```text
   Z >= R^2/M2.
   ```

   L2 anticollision lower-bounds image size. It does not upper-bound `Z`.

6. Cycle52 cut the free-root monodromy-density shortcut. The MCA object is the
   fixed finite `L`-supported locator configuration, not a cover over the
   slope line.

## Active Wall

```text
W-MCA-PER-LINE-SYMMETRIC-DETERMINANTAL-INCIDENCE
```

For a fixed transverse balanced right-minimal-index, quotient-action-rank
separated Hankel pencil, prove or refute the deterministic incidence bound:

```text
R(u,v)
= #{ T subset L, |T|=j :
     rank[H(u)ell_T | H(v)ell_T] <= 1,
     H(v)ell_T != 0 }
<= R_line + O(j),
```

where

```text
R_line = ceil(binomial(n,j)/Q^(t-1)).
```

Equivalently, the system is the vanishing of degree-2 symmetric determinants:

```text
a_i(T)b_l(T)-a_l(T)b_i(T)=0
```

in the elementary symmetric data of the selected support complement `T`.

## Hypotheses To Use

- `L` is a smooth multiplicative Reed-Solomon evaluation domain.
- The pencil is transverse; contained/core templates are removed.
- Right Kronecker minimal indices are balanced, e.g. all nonzero indices are
  `1` in the reserve-scale case.
- Proper quotient-action-rank defects are removed, including bounded-defect
  quotient-component packets `E | m(X^M)` and low
  `d_M(E)=deg minpoly([X^M]_E)`.
- Locators are monic, squarefree, and fully `L`-split.

## Required Output Options

Return one of:

1. `PROOF`: rigorous deterministic per-line incidence bound for `R(u,v)`.
2. `COUNTERPACKET`: a source-valid balanced-index, quotient-separated family
   exceeding `R_line+O(j)`, preferably with many distinct slopes and low fiber
   multiplicity.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction to a sharper exact
   character-sum, incidence, or inverse theorem.
4. `ROUTE_CUT`: explain why the deterministic symmetric-determinantal
   formulation is malformed or missing an essential hypothesis.

## Specific Questions

- Can the degree-2 symmetric determinant system be expressed as a character-sum
  over `T subset L` with enough cancellation under the balanced-index and
  quotient-separated hypotheses?
- Does balanced right-minimal-index imply a nondegenerate coefficient matrix
  for those symmetric quadrics?
- What exactly is the quotient main term in this determinant language, and how
  does `d_M(E)` remove it?
- If the first-moment bound is too hard, can one prove a weaker bound on the
  distinct slope image `Z(u,v)` directly without total landing control?
- Is there a finite checker for small smooth multiplicative groups that
  distinguishes genuine aperiodic concentration from quotient/tangent
  concentration?

## Do Not Do

- Do not use L2 anticollision to upper-bound the image.
- Do not use free-root monodromy density or a `1/j` cover argument for
  fixed-domain `Split_L`.
- Do not count raw arbitrary locator fibers as actual lists.
- Do not ignore quotient-component packets or bounded-defect `d_M(E)`.
- Do not promote this to a final prize solve.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```
