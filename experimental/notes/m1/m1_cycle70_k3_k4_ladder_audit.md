# Cycle 70 K3/K4 Ladder Audit

## Verdict

```text
ROUTE_CUT / BANKABLE_LEMMA / PLAN
```

Confidence: high for the local falsification of the worker's strongest
normalization claim; high for the surviving Cycle 68 t-dependent evaluation
identity; unknown for the still-open `k=3/k=4` ladder.

Cycle 70 does **not** prove or kill:

```text
V-CYCLE69-K3-K4-INJECTIVITY-LADDER
```

It gives a useful verifier route, but its headline `t`-independent slot-value
collapse is false as stated.

## Route Cut

### False Claim Cut

For the Cycle 66/68 model

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
xi = beta^2,
```

and slot patterns `E_i`, define

```text
D_i = {3^e : e in E_i} subset F_17^*,
Q_i(Y)=prod_{d in D_i}(Y-d).
```

Then the normalized Cycle 68 slot value satisfies

```text
u_t(i,a) = prod_{c in 3^a D_i} (beta^2 - c).
```

This is false. The local checker records the first counterexample at
`(t,i,a)=(1,1,0)`. The mistake is dropping the `eta^(-2t)` dependence inside
the argument after pulling out the factor `(eta^(2t))^8=3^t`.

## Surviving Identity

The correct t-dependent identity is:

```text
u_t(i,a)=(-1)^a Q_i(beta^2 eta^(-2t) 3^(-a)).
```

This is already the Cycle 68 polynomial-evaluation table identity, now
rechecked locally on all 336 slot values.

## Local Verification

Codex added:

```text
experimental/scripts/cycle70_slot_normalization_checker.py
```

The local certificate is:

```text
experimental/notes/m1/cycle70_slot_normalization_certificate.json
```

It verifies all 336 slot values against the Cycle 68 table and checks the
surviving t-dependent identity, records a counterexample to the false
t-independent collapse, and checks the ladder through `k=2`. It does not
attempt `k=3/k=4`.

## Remaining Wall

The active wall remains:

```text
V-CYCLE69-K3-K4-INJECTIVITY-LADDER
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

The next exact execution target is:

```text
V-CYCLE70-K3-K4-OPTIMIZED-LADDER-RUN
```

Run an optimized/compiled verifier for the `k=3` and `k=4` product-injectivity
rungs. If `k=4` passes, the next theorem target is:

```text
L-CYCLE70-SUPPORT-5-ENERGY-BOUND
```

If a rung fails, the first partial collision should be banked and inspected
against the Cycle 68 table.

## Guardrail

This is a model-level finite arithmetic result only. It is not an MCA theorem,
not a prize result, and not a proof of `Occ(beta)>2^32`.
