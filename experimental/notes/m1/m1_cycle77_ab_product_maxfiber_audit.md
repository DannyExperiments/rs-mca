# Cycle 77 AB Product Max-Fiber Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / PLAN
```

Confidence: high for the algebraic reductions; high that the answer does not
prove `m_max(beta)<=12`; unknown for the final finite max-fiber value.

Cycle 77 does **not** prove:

```text
m_max(beta) <= 12.
```

It also does not give a `13`-fold counterpacket. Its value is that it cuts the
idea of a short hand proof at the constant `12` and names the remaining object
more exactly.

## Banked Lemmas

### L-CYCLE77-CONFIG-EVALUATION-REDUCTION

The seven-slot product can be rewritten as a product over disjoint eta-coset
configuration atoms:

```text
Phi(T) = 3^{-28} prod_{c in S(T)} (beta^2 - c),
```

where each `S(T)` is a union of one admissible 8-subset from each of seven
disjoint cosets. Therefore product collisions are exactly collisions of this
configuration-evaluation map.

This is equivalent to the `A cap v B^{-1}` max-intersection formulation but is
more structural: it exposes the legal norm shard keys and the seven-block
subset-sum view.

### L-CYCLE77-FIBER-IS-A-CODE

For any fixed product value, the fiber is a code of length `7` over alphabet
`[48]`. If two tuples in the same product fiber differ exactly on a slot set
`D`, then the product map on `D` is non-injective.

Consequently, if all product maps on subsets of size at most `s` are injective,
then every product fiber has Hamming distance at least `s+1`.

This is a genuine structural reduction, but it does not reach the prize target
alone. Even strong subset-injectivity ladders give bounds such as `m_max<=48`,
not `m_max<=12`.

## Route Cut

The constant `12` appears to require an exact finite census or a substantially
new product-set incidence theorem. Cycle 77 gives no hand proof and no
source-valid shortcut. The route should not ask another worker to re-prove
`<=12` abstractly without either:

1. executing a theorem-grade census;
2. proving a new max-intersection theorem for this exact seven-block
   configuration map; or
3. finding an explicit `13`-fold packet.

## Local Follow-Up

Codex added:

```text
experimental/scripts/cycle77_subset_injectivity_check.py
```

The attempted all-triples check was too slow in Python for heartbeat cadence and
was stopped without banking a certificate. Codex then ran the bounded check over
all slot subsets of sizes `1` and `2`. Certificate:

```text
experimental/notes/m1/cycle77_subset_injectivity_pairs_certificate.json
```

The result is:

```text
all 28 subsets of sizes 1 and 2 are product-injective;
fiber minimum distance >= 3.
```

This banks an actual executed rung supporting the fiber-as-code lemma, but it
does not close `m_max<=12`.

## Remaining Wall

```text
V-CYCLE78-EXACT-MMAX-CENSUS
W-CYCLE78-FULL-PRODUCT-INJECTIVITY-OR-13FOLD
```

The next exact target is to compute the finite `m_max` exactly, or at least run
the next subset-injectivity frontier:

```text
all 3-subsets, all 4-subsets, all 5-subsets, all 6-subsets,
```

preferably in compiled code. If a collision occurs, preserve the explicit slot
keys and product. If all pass through size `6`, the product fibers have
distance at least `7`, giving `m_max<=48`; a final census is still needed to
reach `12`.

## What To Do Next

Stage Cycle 78 against an execution-focused target:

- produce a compiled all-4-subset certificate or collision;
- better, produce a compiled exact `m_max` census with certificate schema;
- if the worker remains read-only, require detailed C/Rust code and a local
  bounded Codex execution plan, not another abstract plan.
