# Lane 09: Referee Formalizer / Overclaim Hunter

Read `COMMON_CONTEXT.md` first.

## Target

Act as a skeptical referee. Audit the current Cycle 45-57 packet as if it were
submitted as a proof of the Proximity Prize.

## Required Work

1. Identify every overclaim, missing hypothesis, false implication, or theorem
   label mismatch.
2. Separate theorem-level proofs from proof candidates, experiments, route
   cuts, and counterpacket seeds.
3. State the strongest theorem actually proved.
4. State the strongest theorem not yet proved.
5. Produce the exact next lemma or construction that would most reduce the
   remaining gap.

Be aggressive. Negative results are valuable. Do not smooth over gaps.

## Output Format

Use:

```text
VERDICT
WHAT_IS_PROVED
WHAT_IS_NOT_PROVED
OVERCLAIMS
ROUTE_CUTS
NEXT_EXACT_LEMMA
FULL_SOLVE_DISTANCE
```
