# ROLE 08: Field Normalization And Threshold

The most likely place to overclaim is the threshold comparison.

Audit all field sizes and denominators.

Required:

1. Identify the field in which the product occupancy lives:

```text
F = F_17[X]/(X^16 + X^8 + 3)
```

2. Identify the slope-line field for the corresponding MCA statement.
3. Decide whether `Occ(beta)>2^32` is:

```text
native prize comparison
research benchmark
tensor block benchmark
wrong denominator
```

4. Compute exact values where possible:

```text
17^16
floor(17^16 / 2^128)
2^32
Occ(beta)
```

5. Explain what field extension or product/tensor construction would make the
   numerator threshold official.
6. State the exact corrected comparison that the ledger should record.

Return a pointed `AUDIT`, `ROUTE_CUT`, or `BANKABLE_LEMMA`.
