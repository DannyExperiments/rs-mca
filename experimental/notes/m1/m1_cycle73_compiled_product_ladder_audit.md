# Cycle 73 Compiled Product Ladder Audit

## Verdict

```text
BANKABLE_LEMMA / PLAN
```

Confidence: high for the two new local algebraic reductions; unknown for the
`k=3/k=4/k=5` product-injectivity rungs and for `D<=155`.

Cycle 73 again does **not** execute a compiled verifier and does **not** prove
or falsify:

```text
V-CYCLE72-COMPILED-PRODUCT-ONLY-LADDER-AND-ENERGY
```

The worker had read-only tools and marked its code `UNRUN`. No collision was
found.

## Banked Lemmas

### L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL

For the Cycle 66/68 model, let

```text
F = F_17[X]/(X^16 + X^8 + 3),
eta = 6X^9,
beta = X+2,
xi = beta^2.
```

The worker observed, and Codex locally checked, that:

```text
eta^16 = 3.
```

Writing

```text
y_t = xi eta^(-2t),
S_{i,a} = {3^(a+e mod 16) : e in E_i} subset F_17^*,
```

the slot values satisfy the prime-field polynomial form:

```text
u_t(i,a) = prod_{c in S_{i,a}} (y_t - c).
```

This was checked against the banked Cycle 68 table on all 336 entries with:

```text
experimental/scripts/cycle73_prime_slot_norm_check.py
experimental/notes/m1/cycle73_prime_slot_norm_certificate.json
```

The same local checker confirms the cut Cycle 70 t-independent collapse fails
at `(t,i,a)=(1,1,0)` and, in fact, mismatches all 336 entries in this
comparison.

### L-CYCLE73-SOUND-NORM-BUCKET

For any subfield `K <= F`, the norm map `N_{F/K}` is multiplicative. Therefore

```text
N(prod_t u_t(T_t))
```

is a function of the product alone. Bucketing by a norm value is lossless for
detecting product collisions: equal products always land in the same norm
bucket. This is the sound replacement for the cut `(color, product)` key.

Codex locally spot-checked the `F/F_17` norm homomorphism on 288 adjacent slot
pairs. This is not a ladder certificate, but it verifies the arithmetic path
used by the proposed memory-bounded verifier.

### L-CYCLE73-UNCONSTRAINED-D-DOMINATES

The `D` in the unconstrained seven-slot product map dominates the constrained
color-zero energy used in the Role 05 model packet. Hence proving

```text
D_unconstrained <= 155
```

suffices for the existing gate:

```text
m_max <= 12 => Occ(beta) > 2^32.
```

This lets the next computation ignore the color constraint while remaining
safe for an upper bound on constrained multiplicity.

## Still Open

The product-only ladder remains certified only through `k=2`:

```text
experimental/notes/m1/cycle71_product_ladder_certificate.json
```

No `k=3`, `k=4`, `k=5`, six-slot energy, or full seven-slot energy certificate
has been produced.

## Next Target

The next exact target is no longer another proof-only prompt. It is an
execution-focused finite checker:

```text
V-CYCLE74-NORM-BUCKET-COMPILED-LADDER-RUN
```

Use the prime-field slot polynomial form and sound norm buckets to produce an
actual certificate for:

1. product-only `k=3/k=4`, preferably `k=5`;
2. if `k=5` passes, the six-slot and seven-slot fully displaced energies;
3. otherwise, the first explicit collision with preimages and shared product.

No unrun code should be treated as evidence.

