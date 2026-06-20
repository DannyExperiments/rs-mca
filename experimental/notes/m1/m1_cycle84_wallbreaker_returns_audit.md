# Cycle 84 Wallbreaker Returns Audit

## Verdict

```text
PROOF / BANKABLE_LEMMA
```

Confidence: high that the Cycle84 finite wall is resolved, conditional on the
worker-provided full census outputs being accepted as executed artifacts. Codex
locally ran the lightweight verifier bundled with the strongest certificate and
it returned:

```json
{
  "decision": "CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED",
  "exact_true_m_max": 2,
  "exact_true_occupancy": 52747567092,
  "exact_true_ordered_offdiagonal_energy": 24,
  "projected_max_multiplicity": 2,
  "projected_ordered_offdiagonal_energy": 120,
  "slot_value_log_checks": 336,
  "true_collision_tau_orbits": 6,
  "true_double_fibers": 12
}
```

This is not a prize-level resolution. It closes the finite Cycle84 model wall:

```text
prove m_max(beta) <= 12
or find a 13-fold colored packet.
```

The answer is much stronger:

```text
m_max(beta) = 2.
```

## Raw Artifacts

Preserved in:

```text
experimental/notes/m1/cycle84_wallbreaker_returns_raw/
```

This directory includes:

- proof reports and certificates;
- C++ and Python checker sources;
- tau representative and fixed-bucket outputs;
- proof/checker bundles;
- `LOCAL_VERIFIER_RESULT.json`;
- `SHA256SUMS.txt`.

## Main Numerical Result

For the explicit Cycle66-84 seven-slot color-filtered model over

```text
F_17[X] / (X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
```

the claimed and locally-light-verified finite spectrum is:

```text
compatible pairs      = 52,747,567,104
distinct products     = 52,747,567,092
singleton fibers      = 52,747,567,080
double fibers         = 12
fibers of size >= 3   = 0
ordered off-diagonal D = 24
m_max(beta)           = 2
```

Thus:

```text
Occ(beta) = 52,747,567,092
          = 2^32 + 48,452,599,796.
```

## Independent/Complementary Returns

The nine-role round produced several aligned returns:

1. A full-shard certificate claiming `m_max=2`, with source hash
   `1ed541cb5b60629d6864082a006b672ad5b6c9f100dcd6e41d537ef0809b6189`.
2. A tau-folded/order-3 projected census proving projected max multiplicity
   `2`, then lifting 30 projected double bins to 6 true collision tau-orbits.
3. A weaker but decisive hash-domination certificate proving `m_max<=12`.
4. A tau-fixed-fiber certificate proving both self-dual fibers are empty.
5. A five-slot product-injectivity certificate upgrading the product-fiber
   distance guardrail to at least `6`.
6. A ratio-signature route that remains unresolved but is now superseded by
   the exact `m_max=2` certificate.
7. A referee/audit answer correctly identifying the dlog/tau quotient census as
   the right finite execution route.

## Codex Verification Performed

Codex did not rerun the full 26.37B projected census or the 52.7B direct census
on this Mac.

Codex did:

- inspect the downloaded certificates, manifests, and zip contents;
- verify the arithmetic consistency
  `D - 2(P-U) = 24 - 2*12 = 0`;
- inspect the lightweight verifier source for the strongest bundle;
- run the lightweight verifier locally from
  `cycle84_mmax2_certificate_bundle.zip`;
- confirm it returned `CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED`.

The local verifier directly checks the certificate chain, the 336 slot logs,
the projected census output, the kernel-3 lift, and all 30 lifted pairs in the
finite field. It does not itself regenerate the projected census.

## Route Consequence

The finite wall:

```text
W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION
```

is closed by:

```text
L-CYCLE84-EXACT-COLOR-FILTERED-MMAX
```

with:

```text
m_max(beta)=2.
```

The next exact target is:

```text
L-CYCLE85-EXACT-ROLE05-OCCUPANCY-TRANSFER
```

That means translating the finite spectrum through the banked Cycle65-68
locator-evaluation reduction and recording the official frontier-ledger entry:

```text
Occ(beta)=52,747,567,092 > 2^32.
```

This should be treated as a finite-model obstruction certificate, not as the
full RS-MCA/prize theorem.

