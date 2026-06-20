# Cycle 67 Prompt - Cross-Color Injectivity / Lower-Bound Shortcut

You are a theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve the assigned target. If you cannot fully solve it, progress
it as much as possible. No Internet. Take all the time to reason you need. Use
MAX reasoning.

Do not brainstorm from scratch. This prompt follows Cycle 66.

## Current Situation

Cycle 64 banked:

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-CONVOLUTION
```

and cut:

```text
prefix gadget charge -> scalar-list smallness
```

because exact prefix-gadget charge equals scalar support mass.

Cycle 65 banked:

```text
L-MODEL-GJ-THICKENED-FACTORIZATION
```

and cut the hoped symbolic collapse of thickened color to product color or
truncated jet.

Cycle 66 then banked:

```text
L-CYCLE66-OCCUPANCY-LOCATOR-EVALUATION-REFORMULATION
```

and corrected admissibility:

```text
mu_512(F_{17^16}) = mu_256(F_{17^16}),
beta admissible iff beta notin mu_256.
```

Cycle 66 did **not** compute the full occupancy and did **not** prove
`Occ(beta) >= 2^32`. It made the finite setup self-checkable.

The surviving exact finite wall is:

```text
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

The live target for this prompt is:

```text
L-CYCLE66-CROSS-COLOR-INJECTIVITY-LOWER-BOUND
```

## Read Order

Read from the project source copy:

1. `current_repo_snapshot/experimental/notes/m1/m1_cycle66_sevenfold_product_occupancy_audit.md`
2. `current_repo_snapshot/experimental/notes/m1/cycle66_sevenfold_product_occupancy_raw/response.md`
3. `current_repo_snapshot/experimental/scripts/cycle66_occupancy_selfcheck.py`
4. `current_repo_snapshot/experimental/notes/m1/m1_cycle65_thickened_gadget_color_audit.md`
5. `current_repo_snapshot/experimental/notes/m1/cycle65_thickened_gadget_color_raw/response.md`
6. `current_repo_snapshot/experimental/notes/m1/m1_cycle64_prefix_collision_gadget_audit.md`
7. `current_repo_snapshot/experimental/notes/m1/cycle64_prefix_collision_gadget_raw/response.md`
8. `current_repo_snapshot/experimental/notes/m1/m1_cycle63_round2_audit.md`
9. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/05_role05_near_split_collision_mass.md`

Treat planning/referee files as `AUDIT / PLAN / CONDITIONAL`, not proof,
unless a later audit explicitly banks the claim.

## Exact Finite Object

Work in the Role 05 model:

```text
F = F_{17^16}
H = mu_256 = <eta>
eta^16 = zeta = 3
K = <eta^8>, |K|=32
beta notin mu_256
```

The three local degree-8 polynomials are:

```text
P_1(X)=X^8+4X^5+5X^4+10X^3+4X^2+4X+6
P_2(X)=X^8+9X^5+5X^4+12X^3+14X^2+13X+14
P_3(X)=X^8+11X^5+5X^3+X^2+12X+4
```

For `t=1,...,7`, `i in {1,2,3}`, `a in Z/16`, define:

```text
u_t(i,a)=(-1)^a P_i(beta^2 zeta^{-a} eta^{-2t}).
```

The color contribution is:

```text
r(i,a)=s_i + 8(a mod 2) mod 16,
(s_1,s_2,s_3)=(15,9,12).
```

The occupied thickened-color count is:

```text
Occ(beta)
= #{ prod_{t=1}^7 u_t(i_t,a_t) :
      sum_{t=1}^7 r(i_t,a_t) == 4 mod 16 }.
```

Cycle 66 reformulates this as:

```text
Occ(beta) = #{rho_beta(T): T in P_0},
rho_beta(T)=prod_{x in T}(beta-x),
```

up to a global nonzero scalar.

The constants are:

```text
c_7(4)=25152,
|P_0|=25152*8^7=52,747,567,104=393*2^27,
2^32=4,294,967,296.
```

## Assignment

Prove or kill the proposed symbolic shortcut:

```text
Occ(beta) >= 8^7 * (# independent color classes)
```

in a form strong enough to imply:

```text
Occ(beta) >= 2^32
```

for an explicit admissible `beta`, preferably the Codex self-check beta
`beta=X+2` in the field model `X^16+X^8+3`.

You must do at least one of the following:

1. `PROOF` / `BANKABLE_LEMMA`: Prove a cross-color injectivity or lower-bound
   theorem that clears `2^32` for at least one admissible `beta`.
2. `COUNTERPACKET` / `ROUTE_CUT`: Kill the shortcut with an explicit collision
   mechanism between color classes, showing the proposed lower bound is false.
3. `EXACT_NEW_WALL`: Reduce the shortcut to a smaller exact algebraic target,
   such as a Newton-identity, resultant, or finite family of collision
   equations.
4. `AUDIT / PLAN`: If no proof or falsifier is possible, give an
   implementation-ready projected-power lower-bound verifier that is smaller
   than the full `52.7B` count and has explicit stop conditions.

## Hard Requirements

- No Internet.
- Do not use Sage or package installs.
- Keep model-level obstruction, official prize counterpacket, scalar-list, and
  `t=1` MCA claims separated.
- Do not promote a large model occupancy to prize-level relevance.
- Do not rely on genericity or random-map heuristics as proof.
- If you claim injectivity or a lower bound, state exactly which color classes
  or quotient classes are independent and why collisions cannot occur.
- If you kill the shortcut, give the actual algebraic source of collisions.
- If you propose computation, give field representation, memory/time budget,
  certificate format, and exact stop conditions.

## Desired Outputs

One of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. Formal theorem, falsifier, or reduced wall.
3. Full proof, collision construction, or implementation specification.
4. Parameter ledger and finite relevance.
5. What is bankable versus conditional.
6. Failure point if unresolved.
7. The next exact lemma, construction, or script to run.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```
