# Lane 02: Locator Scroll Circuit Inverse

Read `COMMON_CONTEXT.md` first.

## Target

Attack:

```text
W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT
```

Balanced residue data give complement locators

```text
p_i = Lambda_{T_i},       deg p_i = j,
```

and distinct slopes `z_i`. A superlinear cloud forces an `E`-resonant locator
circuit:

```text
sum_i c_i p_i = 0,
sum_i c_i z_i p_i = E H != 0,
sum_i c_i P_i p_i = -B H.
```

The missing inverse theorem is that many such circuits must synchronize into
quotient pullback, fixed tangent/core, nonminimal denominator, or another
explicit template.

## Required Work

1. Prove the resonant-circuit extraction carefully, including minimal support.
2. Try to prove the inverse classification for smooth multiplicative domains.
3. If classification is false, build a reduced aperiodic counterpacket.
4. Use root sets of `p_i`, not just abstract vector-space dimension.
5. Explain whether entropy enters through circuit abundance, locator
   divisibility, or quotient structure.

## Output Format

Use:

```text
VERDICT
BANKABLE_LEMMA
INVERSE_ATTEMPT
COUNTERPACKET_SEARCH
FAILED_STEP_IF_ANY
EXACT_NEW_WALL
```
