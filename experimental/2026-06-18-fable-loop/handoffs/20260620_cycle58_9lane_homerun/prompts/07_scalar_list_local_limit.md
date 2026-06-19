# Lane 07: Scalar List Full-Support Local Limit

Read `COMMON_CONTEXT.md` first.

## Target

Attack:

```text
W-LIST-FULL-SUPPORT-INTERSECTION-LOCAL-LIMIT
```

The interleaved list challenge at the official `epsilon*=2^-128` scale appears
to reduce to scalar list size by linear projection, provided the list threshold
is below about `sqrt(q)`.

The scalar arbitrary-word list theorem remains open.

## Required Work

1. State the exact scalar list/local-limit theorem needed above corrected
   entropy and quotient reserve.
2. Replace raw locator-fiber statements by actual list size or full agreement
   supports.
3. Prove the theorem, refute it, or identify the exact obstruction template.
4. Analyze quotient-periodic and overagreement packets separately.
5. Explain how this would settle the grand interleaved list challenge at
   `epsilon*=2^-128`.

## Output Format

Use:

```text
VERDICT
SCALAR_LIST_THEOREM
PROOF_OR_COUNTERPACKET
QUOTIENT_OVERAGREEMENT_STATUS
INTERLEAVED_CONSEQUENCE
EXACT_NEW_WALL
```
