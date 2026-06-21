# ROLE 05: Tensor Amplification Or Cut

The Cycle84 model is finite and local. Decide whether it can be amplified into
an official-scale or frontier-relevant family.

Required:

1. Formalize the tensor/block product of the Role05/Cycle84 support packet.
2. Track:

```text
n, k, sigma, j, q_line, q_gen, support size, color group, Delta^+ lift
```

under tensoring.
3. Decide whether occupied colors multiply:

```text
Occ_R >= Occ_1^R
```

or whether collisions, affine color identifications, quotient descent, or field
normalization break multiplicativity.
4. Compare the amplified numerator against the correct
`floor(q_line/2^128)` target.
5. State whether tensoring gives an official counterpacket, a model family, or
   a finite-irrelevant toy obstruction.

If tensor amplification fails, give the exact obstruction and the next repair
lemma.
