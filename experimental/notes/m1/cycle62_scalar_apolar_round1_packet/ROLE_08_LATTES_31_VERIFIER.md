# ROLE 08 - Degree-31 Lattes Packet Verifier

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
V-LATTES-31
```

## Objective

Verify the degree-31 Lattes/isogeny packet only. Do not build a full Lattes
registry.

Check:

- elliptic curve order;
- 31-isogeny kernel;
- explicit rational map;
- separability;
- full-fiber distribution;
- field/domain admissibility;
- pole removal/normalization;
- slope distinctness;
- transversality;
- envelope exclusion;
- exact target comparison.

## Success Criteria

Output `AUDIT` with a complete machine-readable packet certificate.

## Failure Criteria

Output `ROUTE_CUT` if any arithmetic, constant-field, fiber, regularity,
transversality, or noncontainment claim fails.

Do not verify the degree-113 packet unless degree 31 fails in a way that makes
degree 113 uniquely relevant.

