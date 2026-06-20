# ROLE 01 - Scalar Apolar Foundation Referee

Append this role prompt after `COMMON_PROMPT.md`.

## Wall

```text
L-LIST-APOLAR-ALL-LAYER-CI
```

## Objective

Independently prove or disprove the all-layer scalar apolar theorem for
`C = RS[F,L,k]`.

You must handle every error/locator degree `e <= j`, not just the boundary
layer. Prove the complete intersection structure of the apolar ideal, the
locator criterion, the unique decomposition

```text
p_E = A U_E + B V_E,
```

the full-coordinate criterion

```text
gcd(U_E,V_E)=1,
```

and the low-generator collapse

```text
e < deg B  =>  e = deg A and p_E is proportional to A
```

in the first nontrivial case relevant to the referee plan.

## Required Edge Cases

Check:

- zero syndrome;
- `deg A = deg B`;
- roots at infinity and homogenization;
- non-split generators;
- small characteristic;
- generator shear `B -> cB + AC`;
- repeated roots and non-full-coordinate representations;
- endpoint `e=j`.

## Success Criteria

Output `BANKABLE_LEMMA` if the theorem is proved with all edge cases.

## Failure Criteria

Output `COUNTERPACKET` or `ROUTE_CUT` if you find one explicit finite
`(F,L,k,s,E)` violating any claimed equivalence.

