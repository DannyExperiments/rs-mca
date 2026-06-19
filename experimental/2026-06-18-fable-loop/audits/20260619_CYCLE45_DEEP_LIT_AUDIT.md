# Cycle 45 Deep Literature Audit

Status: AUDIT / ROUTE_CUT / EXACT_NEW_WALL

Raw provenance:

- `raw/cycle45_deep_lit_audit/20260619_CYCLE45_DEEP_LIT_AUDIT_RAW.txt`

Target context:

- Cycle 45 random-anchor pair-rank theorem in the restricted additive
  residue-line branch.
- Grand Proximity Prize MCA and list-decoding challenge admissibility.

## Conservative Verdict

The literature audit supports the current route-board interpretation:

1. The exact Cycle 45 pair-rank formula

   ```text
   rank_F(w -> (R_T(w), R_T'(w))) = t + min(t, |T\T'|)
   ```

   was not identified as a stated theorem in the surveyed literature.

2. Several nearby traditions exist: proximity-gap correlated agreement,
   function-field/formal-variable rank arguments, folded Reed-Solomon and
   multiplicity-code decoding, subspace-polynomial lower bounds, and
   interleaved Reed-Solomon syndrome-rank methods. These are `RELATED BUT
   DIFFERENT`, not duplicates of the exchange-distance pair-rank theorem.

3. The main prize-level issue remains domain admissibility. The restricted
   branch uses

   ```text
   D = F_p subset F_{p^2}
   ```

   which is additive/subfield-structured. The prize statement says "smooth
   evaluation domain"; protocol usage and surrounding literature usually point
   toward multiplicative smooth domains/cosets. Thus Cycle 45 should not be
   promoted as a full grand MCA solve without an admissibility ruling or a
   transfer to the intended smooth/generated domain.

4. No direct transfer theorem from the additive-subfield branch to smooth
   multiplicative domains was identified.

5. The grand interleaved-list challenge remains unsolved by Cycle 45.

## Important Correction to the Lit-AI Output

The lit-audit output has a notation error in Task 6. It treats `C^{equiv m}`
as if it were a Reed-Muller or multiplicity-code object in one paragraph.
In the local source, `C^{equiv m}` is the `m`-interleaved Reed-Solomon code
with column distance:

```text
C^{equiv s} = { (c^(1),...,c^(s)) : c^(i) in C }.
```

Therefore the list-decoding challenge should stay framed as an interleaved
Reed-Solomon list-size problem, not as a Reed-Muller/multiplicity-code
challenge. Multiplicity-code literature may be related, but it is not the
literal object.

## Route Cut

The following promotion is cut:

```text
Cycle45 restricted additive theorem => full grand MCA challenge solve
```

This implication is unsupported until either:

1. `D=F_p subset F_{p^2}` is accepted as an admissible smooth evaluation
   domain for the official challenge; or
2. the Cycle 45 mechanism is transferred to the intended smooth/generated
   multiplicative domain.

## Exact New Walls

Primary:

```text
W-F1-AA-RES-SMOOTH-DOMAIN-ADMISSIBILITY
```

Decide whether the official "smooth evaluation domain" includes the additive
subfield `F_p subset F_{p^2}` for the purposes of the grand MCA challenge.

Secondary:

```text
W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING
```

Transfer or compress the Cycle 45 construction to the generated-field /
smooth-domain scale. The target is to reduce the landing codimension from
`2(t-1)` `B`-dimensions to `t-1`, moving the threshold from
`C < H_2(rho)/2` toward `C < H_2(rho)`.

List-side wall:

```text
W-F1-LIST-INTERLEAVED-BRIDGE
```

Determine whether the Cycle 45 MCA construction yields any rigorous lower
bound or obstruction for

```text
|Lambda(C^{equiv m}, delta)|
```

for constant `m`. No such implication is banked.

## Next Director Move

Do not launch a generic homerun prompt. The next model calls should be
role-split against the exact post-lit walls:

1. source/admissibility auditor for official challenge wording;
2. smooth-domain transfer proof-builder;
3. Frobenius-compressed landing proof-builder;
4. transfer obstruction/counterpacket hunter;
5. interleaved-list bridge auditor;
6. formal theorem writer for the restricted branch.

Confidence:

- Pair-rank novelty support: moderate, not proved by the lit audit.
- Domain-admissibility issue: high.
- List challenge still unsolved: high.
