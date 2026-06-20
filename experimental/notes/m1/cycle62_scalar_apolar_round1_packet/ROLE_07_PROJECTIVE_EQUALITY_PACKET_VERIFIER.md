# ROLE 07 - Projective Equality-Scale Packet Verifier

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
V-PROJECTIVE-SUBLINE-M-EQUAL-SIGMA
```

## Objective

Independently verify the Cycle 60 projective equality-scale packet with:

```text
p = 2^19 - 1
n = 2^19
k = 2^17
M = sigma = 2^14
psi(X) = (X+2)/(2X+1)
claimed distinct slopes = 28,048,800
claimed target T_F = 16,776,960
```

Check the block system, choice of `vartheta`, distinct-slope bound,
transversality, proper-envelope exclusion, full monomial action ranks, and
threshold comparison.

## Success Criteria

Output `AUDIT` with a machine-verifiable exact certificate for all algebraic
and numerical claims.

## Failure Criteria

Output `COUNTERPACKET` only if you find a repaired stronger packet. Otherwise
output `ROUTE_CUT` if any required packet claim fails: degree, squarefreeness,
collision bound, action rank, envelope exclusion, or threshold comparison.

