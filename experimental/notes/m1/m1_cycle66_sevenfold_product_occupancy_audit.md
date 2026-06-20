# Cycle 66 Sevenfold Product Occupancy Audit

## Executive Verdict

**Status:** `AUDIT / BANKABLE_LEMMA / EXACT_NEW_WALL`.

**Significance:** useful and route-sharpening, but not a solved verifier and
not a prize-level counterpacket. Cycle 66 did not compute the full
`52,747,567,104`-input occupancy, and did not prove `Occ(beta) >= 2^32`.
It did make the finite verifier target precise, corrected the admissibility
condition, and gave an implementation path plus a local self-checkable
reference oracle.

## Bankable Corrections And Lemmas

Cycle 66 banks the corrected admissibility condition:

```text
v_2(17^16 - 1) = 8,
mu_512(F_{17^16}) = mu_256(F_{17^16}).
```

Thus the Cycle 65 phrase `beta notin mu_512` should be read in this field as:

```text
beta notin mu_256 = <eta>.
```

This also gives the exact nonvanishing criterion:

```text
all 336 factors u_t(i,a) are nonzero
iff beta notin mu_256.
```

Cycle 66 also banks the locator-evaluation reformulation:

```text
Occ(beta) = #{ rho_beta(T) : T in P_0 },
rho_beta(T) = prod_{x in T}(beta - x),
```

up to the global nonzero scalar

```text
C = (beta - 1) 3^12.
```

So the sevenfold product count is exactly a distinct locator-value count for
the Role 05 support packet. This is a useful finite-object simplification,
not a smallness theorem.

Finally, Cycle 66 records and Codex locally verified the constants:

```text
c_7(4) = 25152,
|P_0| = 25152 * 8^7 = 52,747,567,104 = 393 * 2^27,
2^32 = 4,294,967,296.
```

The target line is therefore only about `8.14%` of the maximal possible
occupancy.

## Local Codex Verification

Codex added and ran:

```text
experimental/scripts/cycle66_occupancy_selfcheck.py
```

The script is a bounded setup verifier, not the full occupancy counter. It
constructs an explicit `F_{17^16}` model, finds `eta` of order `256` with
`eta^16=3`, chooses an admissible `beta`, checks the three degree-8 gadget
polynomials, checks the color constants and `c_7(4)`, and spot-checks the
Cycle 65 factorization

```text
rho_beta(T) = (beta - 1)3^12 prod_t u_t(i_t,a_t).
```

The run passed and emitted:

```text
field_poly = X^16 + X^8 + 3
eta = 6 X^9
beta = X + 2
factorization_oracle_spotchecks = 32
decision = SELF_CHECK_ONLY
```

The generated certificate is preserved at:

```text
experimental/notes/m1/cycle66_sevenfold_product_occupancy_raw/selfcheck_certificate.json
```

## What Is Not Proved

- No explicit `Occ(beta)` value is computed.
- No proof of `Occ(beta) >= 2^32` is supplied.
- No proof of `Occ(beta) < 2^32` is supplied.
- The proposed Python reference code is not a practical full counter: the
  full count needs either a compiled meet-in-the-middle/external-sort job or
  a sharper symbolic lower-bound lemma.
- The result remains model-level. It is not an official prize counterpacket,
  and finite frontier placement is still separate.

## Surviving Wall

The exact finite wall remains:

```text
W-MODEL-GJ-SEVENFOLD-POLY-PRODUCT-SET-OCCUPANCY
```

but now with a sharper verifier target:

```text
V-CYCLE66-OCCUPANCY-COUNT-OR-CERTIFIED-LOWER-BOUND
```

The worker estimates that exact counting requires roughly:

```text
48^3 left products,
48^4 right products,
~52.7 billion product combinations,
~40 GB packed hash or ~400 GB external-sort scale.
```

The answer also proposes a memory-bounded certified lower-bound route by
counting distinct projected powers `x -> x^d`, but leaves that backend as an
ellipsis rather than executable code.

## Recommended Next Step

Before spending on a large compiled count, attack the symbolic shortcut named
by the worker:

```text
L-CYCLE66-CROSS-COLOR-INJECTIVITY-LOWER-BOUND
```

Target form:

```text
Occ(beta) >= 8^7 * (# independent color classes),
```

or kill it with an explicit collision mechanism. If it succeeds, it can clear
`2^32` without the 52.7-billion product count. If it fails, the route should
move to an implementation-grade compiled/external-sort verifier or a
certified projected-power lower-bound counter.

In parallel, keep the finite frontier route alive:

```text
RS-PRIZE-FRONTIER-V1-REGISTRY-FIRST-RUN
```

because large model occupancy alone is not prize-relevant.

## Raw Provenance

Raw artifacts and checksums are preserved in:

```text
experimental/notes/m1/cycle66_sevenfold_product_occupancy_raw/
```
