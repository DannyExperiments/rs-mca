# Cycle 54 Prompt: t=2 Slope-Summed Cosupport Cancellation

You are a theorem worker for the RS-MCA / Proximity Prize project.

Read the project source and recent loop material first, especially the Cycle 49
through Cycle 53 audits. Preserve the labels `PROOF`, `COUNTERPACKET`,
`BANKABLE_LEMMA`, `ROUTE_CUT`, and `EXACT_NEW_WALL` literally.

## Current Banked State

The positive/safe-side scalar MCA upper branch has been reduced to an exact
per-line finite-domain incidence problem.

For a fixed line in syndrome coordinates, with `Q=|F|`, `t=r-j`, and `ell_T`
the monic locator for a fully `L`-split `j`-set `T`,

```text
a(T)=H(u)ell_T,
b(T)=H(v)ell_T.
```

A transverse locator realizes a unique slope iff

```text
b(T) != 0 and rank[a(T)|b(T)] <= 1.
```

Cycle 53 banked the exact signed character identity:

```text
R(u,v)
= binomial(n,j)/Q^(t-1) - Q*K0_split + Err,

Err
= Q^{-t} sum_{z in F} sum_{y in F^t, y != 0} S(y,z),

S(y,z)
= sum_{T split} psi(<y,H(u+zv)ell_T>).
```

The phase rewrites in cosupport/evaluation form as

```text
<y,H(u+zv)ell_T>
= sum_{x in L\T} beta_x(z)Y(x) prod_{y' in T}(x-y'),
```

where `Y(X)=sum_{m<t} y_m X^m`.

Thus the desired landing upper bound

```text
R(u,v) <= R_line + O(j),
R_line=ceil(binomial(n,j)/Q^(t-1)),
```

follows from the one-sided cancellation estimate

```text
Err <= O(j).
```

## Active Wall

```text
W-MCA-T2-SLOPE-SUMMED-COSUPPORT-CANCELLATION
```

Attack the first nontrivial subcase `t=2`.

In this case the dual polynomial is

```text
Y(X)=y0+y1 X,
```

and the rank-one condition is one determinant

```text
a0(T)b1(T)-a1(T)b0(T)=0.
```

The slope-summed error is

```text
Err
= Q^{-2} sum_{z in F} sum_{(y0,y1) != (0,0)}
   sum_{T split}
   psi( sum_{x in L\T} beta_x(z)(y0+y1 x)
        prod_{y' in T}(x-y') ).
```

## Hypotheses To Respect

- `L` is a smooth multiplicative Reed-Solomon evaluation domain.
- Locators are monic, squarefree, and fully `L`-split.
- The pencil is transverse; contained/core/tangent templates are removed.
- The right Kronecker minimal indices are balanced.
- Proper quotient-action-rank defects are removed. In particular, for each
  proper divisor scale `M`, low `d_M(E)=deg minpoly([X^M]_E)` and bounded-defect
  quotient-component packets are excluded.
- Do not use random-anchor averaging as a deterministic upper theorem.

## Required Output Options

Return one of:

1. `PROOF`: a rigorous `t=2` proof of `Err<=O(j)` or directly
   `R(u,v)<=R_line+O(j)` under the stated balanced, transverse,
   quotient-separated hypotheses.
2. `COUNTERPACKET`: a source-valid `t=2`, balanced, transverse,
   quotient-separated, aperiodic family with `R>R_line+omega(j)` or many
   distinct slopes. The counterpacket must identify why it is not a quotient
   component, not tangent/contained, and not a same-witness artifact.
3. `BANKABLE_LEMMA / EXACT_NEW_WALL`: a strict reduction of the `t=2` problem
   to a smaller exact object, with the new wall stated precisely enough to
   prompt next.
4. `ROUTE_CUT`: a precise reason the Cycle53 character-sum reduction or this
   `t=2` specialization is malformed.

## Specific Questions

- Can the `t=2` phase be converted by Newton identities into a one-variable or
  two-variable Gauss/Kloosterman-type sum over the smooth multiplicative group?
- Does the slope sum over `z` eliminate one dual direction or create a
  usable orthogonality relation?
- What are the exact trivial or imprimitive character directions, and are they
  exactly the tangent/core and quotient-action-rank defects already excluded?
- If square-root cancellation fails, can you construct an explicit
  quotient-separated aperiodic resonance rather than a hidden `X^M` packet?
- Can you specify a finite checker for `t=2` that certifies the split between
  tangent, quotient, and genuinely aperiodic excess?

## Do Not Do

- Do not use L2 anticollision as an upper bound.
- Do not use free-root monodromy or a `1/j` totally-split density shortcut.
- Do not count raw arbitrary locator fibers as actual lists.
- Do not ignore quotient-component packets or low `d_M(E)`.
- Do not promote this to a final prize solve.

End with:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

