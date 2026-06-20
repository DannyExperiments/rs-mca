# Cycle 69 Slot-Log Independence Audit

## Verdict

```text
BANKABLE_LEMMA / PLAN
```

Confidence: high for the elementary lemmas and verifier plan; unknown for the
final target `m_max(beta) <= 12`.

Cycle 69 does not prove `m_max(beta) <= 12` and does not find a 13-fold
collision. It banks two useful exact gates below Cycle 68 and gives a sharper
verification path.

## Banked Lemmas

### Energy-To-Multiplicity Gate

Let

```text
m_v = #{T in P_0 : prod_t u_t(B_t)=v},
m_max = max_v m_v,
E = sum_v m_v^2,
D = E - |P_0| = sum_v m_v(m_v-1).
```

Then

```text
m_max(m_max - 1) <= D.
```

Therefore:

```text
D <= 155 => m_max <= 12 => Occ(beta) >= |P_0|/12 > 2^32.
```

This is sharp for the current threshold because a 13-fold collision contributes
at least `13*12=156` to the ordered off-diagonal collision count `D`.

### Injectivity Ladder

For `J subset {1,...,7}`, say `J` is product-injective if the partial products

```text
prod_{t in J} u_t(B_t)
```

are pairwise distinct over the `48^|J|` slot choices.

If every `k`-subset `J` is product-injective, then every full collision has
slot support at least `k+1`.

The Cycle 68 checker already proved the `k=1` rung via single-slot
injectivity. Cycle 69 proposes checking `k=2,3,4` as a cheap certificate ladder
before the full multiplicity count.

### Slot Complement Oracle

For `B^c = Z/16 \\ B`,

```text
S_t(B) * S_t(B^c) = beta^32 - 3^(2t).
```

This follows from the Cycle 68 full slot-product oracle and gives another
self-check for future compiled verifiers.

## Local Verification

Codex added:

```text
experimental/scripts/cycle69_ladder_probe.py
```

It reuses `cycle68_slot_factorization_checker.py`, checks the complement oracle,
and tests product-injectivity rungs. The default local run checks through
`k=2`. A pure-Python `k=3` run was attempted and interrupted for local
performance reasons; that is not mathematical evidence of failure. The `k=3`
and `k=4` rungs should be handled by a compiled/optimized verifier or by a
structural proof.

Certificate path:

```text
experimental/notes/m1/cycle69_ladder_probe_certificate.json
```

The saved certificate verifies:

```text
k=1 product-injective: true
k=2 product-injective: true
complement oracle checks: 336
```

## Remaining Wall

The decision target remains:

```text
m_max(beta) <= 12.
```

The Cycle 69 formulation says it is enough to prove the scalar collision gate:

```text
D <= 155.
```

The next exact wall is:

```text
V-CYCLE69-K3-K4-INJECTIVITY-LADDER
```

If that ladder verifies product-injectivity through `k=4`, the next theorem is
`L-CYCLE69-SUPPORT-5-ENERGY-BOUND`; otherwise the first failed rung gives a
concrete partial-collision object to inspect.

## Next Action

Stage Cycle 70 against the optimized ladder / energy gate. The requested output
should be one of:

1. a proof or optimized verifier for the `k=3` and `k=4` injectivity rungs;
2. the first explicit partial collision if a rung fails;
3. a proof of `D <= 155`;
4. an explicit 13-fold collision;
5. a compiled verifier specification or code path that counts `D` exactly.

Keep the result model-level only.
