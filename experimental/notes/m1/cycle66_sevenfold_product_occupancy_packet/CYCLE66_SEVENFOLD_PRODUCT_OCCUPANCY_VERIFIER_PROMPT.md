# Cycle 66 Prompt - Sevenfold Product Occupancy Verifier

You are a theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve the assigned finite verifier target. If you cannot fully
solve it, progress it as much as possible. No Internet. Take all the time to
reason you need. Use MAX reasoning.

Do not brainstorm from scratch. This prompt follows Cycle 65.

## Current Situation

Cycle 64 banked:

```text
L-MODEL-GJ-PREFIX-COLLISION-GADGET-CONVOLUTION
```

and cut the route

```text
prefix gadget charge -> scalar-list smallness
```

because the exact gadget charge equals scalar support mass.

Cycle 65 then banked:

```text
L-MODEL-GJ-THICKENED-FACTORIZATION
```

and cut the hoped symbolic collapse of thickened color to product color or
truncated jet.

The surviving exact finite wall is:

```text
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

The desired verifier target is:

```text
V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER
```

## Read Order

Read from the project source copy:

1. `current_repo_snapshot/experimental/notes/m1/m1_cycle65_thickened_gadget_color_audit.md`
2. `current_repo_snapshot/experimental/notes/m1/cycle65_thickened_gadget_color_raw/response.md`
3. `current_repo_snapshot/experimental/notes/m1/m1_cycle64_prefix_collision_gadget_audit.md`
4. `current_repo_snapshot/experimental/notes/m1/cycle64_prefix_collision_gadget_raw/response.md`
5. `current_repo_snapshot/experimental/notes/m1/m1_cycle63_round2_audit.md`
6. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/05_role05_near_split_collision_mass.md`
7. `current_repo_snapshot/experimental/notes/m1/cycle63_round2_raw/08_role08_t1_color_transfer.md`
8. `current_repo_snapshot/experimental/notes/m1/m1_cycle62_round1_audit.md`
9. Main source only as needed:
   - `current_repo_snapshot/tex/slackMCA_v3.tex`
   - `current_repo_snapshot/tex/RS_disproof_v3.tex`
   - `current_repo_snapshot/tex/cs25_cap_v4.tex`
   - `current_repo_snapshot/tex/snarks_v4.tex`

Treat planning/referee files as `AUDIT / PLAN / CONDITIONAL`, not proof,
unless a later audit explicitly banks the claim.

## Exact Object To Decide

Work in the Role 05 model:

```text
F_0 = F_{17^16}
H_0 = mu_256 = <eta>
eta^16 = zeta = 3
K = <eta^8>, |K| = 32
```

Cycle 65 gives three local degree-8 polynomials:

```text
P_1(X)=X^8+4X^5+5X^4+10X^3+4X^2+4X+6
P_2(X)=X^8+9X^5+5X^4+12X^3+14X^2+13X+14
P_3(X)=X^8+11X^5+5X^3+X^2+12X+4
```

For an admissible `beta notin mu_512`, define

```text
u_t(i,a)=(-1)^a P_i(beta^2 zeta^{-a} eta^{-2t})
```

for

```text
t = 1,...,7,  i in {1,2,3},  a in Z/16.
```

The color contribution is

```text
r_t = s_i + 8(a mod 2) mod 16,
(s_1,s_2,s_3) = (15,9,12).
```

The occupied thickened-color count is

```text
Occ(beta) =
#{ prod_{t=1}^7 u_t(i_t,a_t) :
   sum_{t=1}^7 r_t == 4 mod 16 }.
```

The upper bound is

```text
Occ(beta) <= 52,747,567,104 = 393 * 2^27.
```

The model-level finite line of interest is:

```text
2^32.
```

## Assignment

Prove, kill, or make executable:

```text
V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER
```

You must do at least one of the following:

1. Give a complete proof that there exists an admissible `beta` with
   `Occ(beta) >= 2^32`.
2. Give a complete proof that `Occ(beta) < 2^32` for every admissible `beta`.
3. Produce an implementation-ready finite verifier that Codex/PRZ can run
   without Sage and without Internet, including:
   - an explicit representation of `F_{17^16}`;
   - a method to find `eta` with `eta^16=3` and order `256`;
   - a method to choose or sweep admissible `beta`;
   - exact finite-field arithmetic;
   - meet-in-the-middle product counting bucketed by color sum;
   - memory/time estimates;
   - a certificate format for `Occ(beta)`;
   - self-check identities proving the script implements Cycle 65 formulas.
4. If the verifier target is ill-posed, identify the exact missing datum and
   state the smallest corrected target.

If the harness permits writing output files, write a verifier script and a
README/certificate spec into `output_files/`. If not, include the code or
pseudocode in the answer.

## Hard Requirements

- No Internet.
- Do not use Sage as a dependency. Pure Python is preferred; C/Rust pseudocode
  is acceptable only if the exact arithmetic is specified.
- Do not use package installs.
- Keep model-level obstruction, official prize counterpacket, scalar-list, and
  `t=1` MCA claims separated.
- Do not promote a large `Occ(beta)` to a prize counterpacket unless finite
  frontier placement is also established.
- If you use a random or primitive element search, give deterministic fallback
  and verification checks.
- If you use discrete logs, explain how they are computed or avoided. Direct
  field-element set counting is allowed.
- State exact stop conditions for the verifier:
  `Occ >= 2^32`, `Occ < 2^32`, memory exhaustion, or discovered collapse.

## Desired Outputs

One of:

1. `COUNTERPACKET`: explicit admissible `beta` or theorem with
   `Occ(beta) >= 2^32`, model-level only unless frontier placement is supplied.
2. `BANKABLE_LEMMA`: verified collapse or upper bound below `2^32`.
3. `EXACT_NEW_WALL`: a smaller finite arithmetic target than the sevenfold
   product occupancy count.
4. `AUDIT / PLAN`: implementation-ready verifier if the count cannot be
   resolved symbolically.

## Required Output Format

Start with exactly one of:

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
2. Formal theorem, verifier, or counterpacket statement.
3. Full construction/proof or exact implementation specification.
4. Parameter ledger and finite relevance.
5. What is bankable versus conditional.
6. Failure point if unresolved.
7. The next exact lemma, construction, or script to run.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```

