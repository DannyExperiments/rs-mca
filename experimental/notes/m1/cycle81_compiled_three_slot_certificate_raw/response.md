This is a large project. Let me read the key files relevant to the immediate target. I'll start with the cycle80 checker and the model definitions.Let me read the core technical files: the cycle80 checker and the cycle80 mindist audit.Let me read the cycle80 mindist audit, cycle77 certificate, and cycle79 certificate.Let me check the environment and read the remaining context files (cycle79 involution + cycle80 raw response for the MITM L/R split).## Environment status

I have only a read-only `Read` tool in this harness. No shell, no file-creation, no code execution is exposed to me, and I cannot write into `output_files`. So I cannot produce a *computed* certificate this cycle. Per your discipline rules: I will not claim proof from unrun code, and every program below is marked `UNRUN`. I'll deliver the checker, schema, and MITM design inline.

I read the live files: the Cycle 81 override in `DIRECTOR_STATE.md`, the Cycle 80 mindist audit, `cycle80_three_slot_injectivity_checker.py`, `cycle68_slot_factorization_checker.py`, the Cycle 77 pairs certificate (28 subsets, all injective, min-dist ≥ 3), and the Cycle 79 involution certificate (K, τ, slot pairing constants).

## Is there a route to a full solve?

Yes for the immediate target, and it is computational, not a hand proof. The honest verdict matches your own Cycle 80 route-cut: the all-35-triples question is a bounded finite check (35 triples × 48³ = 3.87M field products), and the only thing missing in Cycle 80 was speed. The pure-Python `fmul_fast` is the bottleneck (~256 inner ops/mult × ~3.9M mults ≈ 10⁹ Python ops). The fix is to replace scalar field multiplication with a **vectorized batched polynomial multiply + fold-reduction**, which turns each triple into a handful of NumPy array ops. Expected wall time: seconds total, not minutes. That is the route to the full solve.

I do **not** see a clean closed-form algebraic proof of `(R_{t1}R_{t2}) ∩ R_{t3} = ∅` for all 35 triples. The objects are cyclotomic (roots `eta^{2t}·zeta^b`, `zeta=eta^16` a primitive 16th root, `xi=beta^2`), but a triple collision is a genuine multiplicative relation `r₁r₂r₃=1` among 8-fold products of `(xi − eta^{2t}zeta^b)`, and there is no visible degeneracy that forces emptiness uniformly. Attempting a hand proof here would be exactly the "broad hand proof" the audit told you to stop demanding. The executable certificate is the correct deliverable.

## The next exact lemma / construction

This is the precise rung to close, restating Cycle 80 `L-CYCLE80-RATIO-TRIPLE-REFORMULATION` as a decision procedure plus its consequence:

```text
L-CYCLE81-THREE-SLOT-INJECTIVITY (target)
  For every 3-subset {t1,t2,t3} ⊂ {1..7}, the slot-product map
      (S1,S2,S3) |-> u_{t1}(S1)·u_{t2}(S2)·u_{t3}(S3)
  is injective on 48^3, equivalently  (R_{t1}·R_{t2}) ∩ R_{t3} = ∅,
  equivalently there is no nontrivial r1 r2 r3 = 1 with r_i ∈ R_{ti}.

Consequence on PASS (L-CYCLE80-MINDIST-CERTIFICATE):
  Cycle 77 (all singletons+pairs injective) + L-CYCLE81 ⇒ any two distinct
  product-equal 7-tuples differ in ≥ 4 slots ⇒ product-fiber minimum
  Hamming distance ≥ 4. (Because a collision differing in ≤3 slots reduces,
  by cancelling agreeing nonzero slots, to a ≤3-slot collision, all of which
  are now excluded.)
```

The construction that decides it fast is the vectorized exact checker below. Equality key is the packed 16-coefficient field product only; color enters solely in a collision packet (matching your discipline).

## Deliverable 1 — `CHECKER.py` (UNRUN)

Reuses the audited Cycle 68 model builder, so the field/eta/beta are exactly the banked ones. The multiply is a batched Kronecker-free convolution with the same `X^16 = −X^8 − 3` fold as `fmul_fast`, so it is bit-identical arithmetic, just vectorized.

```python
#!/usr/bin/env python3
"""Cycle 81 compiled/vectorized three-slot product-injectivity decider. UNRUN.
Equality key = packed 16-coeff field product only. Color only in collisions.
Arithmetic is identical to cycle80 fmul_fast (X^16 = -X^8 - 3 over F_17),
but batched with NumPy so all 35 triples finish in seconds.
"""
from __future__ import annotations
import argparse, importlib.util, itertools, json
from pathlib import Path
import numpy as np

P, NDEG = 17, 16
SD = Path(__file__).resolve().parent
C68 = SD / "cycle68_slot_factorization_checker.py"

def load_c68():
    spec = importlib.util.spec_from_file_location("c68", C68)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def dense_arr(vals):                       # list of poly tuples -> (n,16) int64 mod 17
    a = np.zeros((len(vals), NDEG), dtype=np.int64)
    for r, v in enumerate(vals):
        for i, c in enumerate(v[:NDEG]):
            a[r, i] = c % P
    return a

def fold_reduce(conv):                      # conv: (n,31) -> (n,16) reduced mod field poly
    t = conv.copy() % P
    for d in range(30, NDEG - 1, -1):       # X^d = -X^{d-8} - 3 X^{d-16}, top-down
        c = t[:, d] % P
        t[:, d - 8] = (t[:, d - 8] - c) % P
        t[:, d - 16] = (t[:, d - 16] - 3 * c) % P
        t[:, d] = 0
    return t[:, :NDEG] % P

def batch_mul(A, B):                         # elementwise (n,16)x(n,16) -> (n,16)
    n = A.shape[0]
    conv = np.zeros((n, 2 * NDEG - 1), dtype=np.int64)
    for i in range(NDEG):                    # 16 vectorized multiply-adds
        conv[:, i:i + NDEG] += A[:, i][:, None] * B
    return fold_reduce(conv)

def all_combos_mul(A, B):                    # (nA,16)x(nB,16) -> (nA*nB,16), row=a*nB+b
    nA, nB = A.shape[0], B.shape[0]
    A2 = np.repeat(A, nB, axis=0)
    B2 = np.tile(B, (nA, 1))
    return batch_mul(A2, B2)

def keys_of(M):                              # (n,16) mod 17 -> structured byte keys
    return np.ascontiguousarray(M.astype(np.uint8)).view([('k', np.void, NDEG)]).ravel()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--size", type=int, default=3,
                                                    choices=(3,)); args = ap.parse_args()
    c = load_c68(); f = c.find_field_poly(); eta = c.find_eta(f); beta = c.find_beta(f)
    raw = c.build_u(f, eta, beta)
    slot = {t: dense_arr([raw[(t, k // 16 + 1, k % 16)] for k in range(48)])
            for t in range(1, 8)}
    color = {k: (c.S_COLOR[k // 16 + 1] + 8 * ((k % 16) % 2)) % 16 for k in range(48)}
    ia = {k: (k // 16 + 1, k % 16) for k in range(48)}

    results, all_ok, collision = [], True, None
    for (t1, t2, t3) in itertools.combinations(range(1, 8), 3):
        pair = all_combos_mul(slot[t1], slot[t2])          # (2304,16)
        full = all_combos_mul(pair, slot[t3])              # (110592,16)
        keys = keys_of(full)
        uniq, idx, cnt = np.unique(keys, return_index=True, return_counts=True)
        if cnt.max() > 1:                                   # collision
            r0 = int(idx[cnt.argmax()])
            dup = np.where(keys == keys[r0])[0]
            rA, rB = int(dup[0]), int(dup[1])
            def decode(r):
                k3 = r % 48; pp = r // 48; k2 = pp % 48; k1 = pp // 48
                return (k1, k2, k3)
            kA, kB = decode(rA), decode(rB)
            slots = (t1, t2, t3)
            def pack(M, r): return int("".join(f"{x:02d}" for x in M[r]))
            collision = {
                "slots": list(slots),
                "assignment_A": [{"slot": t, "k": k, "ia": list(ia[k]),
                                  "color": color[k]} for t, k in zip(slots, kA)],
                "assignment_B": [{"slot": t, "k": k, "ia": list(ia[k]),
                                  "color": color[k]} for t, k in zip(slots, kB)],
                "packed_product": list(map(int, full[rA])),
                "colorsum_A": sum(color[k] for k in kA) % 16,
                "colorsum_B": sum(color[k] for k in kB) % 16,
            }
            results.append({"slots": list(slots), "product_injective": False})
            all_ok = False; break
        results.append({"slots": list(slots), "product_injective": True,
                        "tuple_count": 48 ** 3, "distinct_products": int(uniq.size)})

    out = {"model": {"field_poly": list(f), "eta": list(eta), "beta": list(beta)},
           "key": "packed_product_only", "subset_size": 3,
           "subsets_checked": len(results),
           "all_checked_product_injective": all_ok, "results": results}
    if all_ok:
        out["decision"] = "ALL_3_SUBSETS_PRODUCT_INJECTIVE"
        out["fiber_min_distance_lower_bound"] = 4
    else:
        out["decision"] = "PRODUCT_COLLISION_FOUND"; out["collision_packet"] = collision
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
```

`UNRUN`. It is a drop-in replacement for `cycle80_three_slot_injectivity_checker.py --size 3`, requires only NumPy, and emits the same certificate vocabulary. A correctness self-test you should add before trusting it: assert `batch_mul` agrees with `cycle80.fmul_fast` on the 48 slot values of a random pair of slots (cheap, exact, kills any reduction-loop transcription bug). If NumPy is unavailable, the same `fold_reduce`/`batch_mul` logic runs in plain Python with Kronecker packing (one big-int multiply per element, base `2^13`, since conv coeffs `< 16·16² = 4096 < 2^13`), still ~5× faster than `fmul_fast`.

## Deliverable 2 — Certificate schema

On PASS:

```json
{
  "model": {"field_poly":[...17...], "eta":[...], "beta":[2,1]},
  "key": "packed_product_only",
  "subset_size": 3,
  "subsets_checked": 35,
  "all_checked_product_injective": true,
  "results": [{"slots":[t1,t2,t3], "product_injective":true,
               "tuple_count":110592, "distinct_products":110592}, ...],
  "decision": "ALL_3_SUBSETS_PRODUCT_INJECTIVE",
  "fiber_min_distance_lower_bound": 4
}
```

On FAIL (explicit collision packet):

```json
{
  "...": "...",
  "all_checked_product_injective": false,
  "decision": "PRODUCT_COLLISION_FOUND",
  "collision_packet": {
    "slots":[t1,t2,t3],
    "assignment_A":[{"slot":t,"k":k,"ia":[i,a],"color":c}, ...],
    "assignment_B":[{"slot":t,"k":k,"ia":[i,a],"color":c}, ...],
    "packed_product":[...16 coeffs...],
    "colorsum_A": c%16, "colorsum_B": c%16
  }
}
```

`distinct_products == tuple_count == 110592` on every triple is the witness of injectivity for that triple. `fiber_min_distance_lower_bound: 4` is only valid jointly with the banked Cycle 77 pairs certificate (it is the chained consequence, not a standalone claim of the size-3 run).

## Deliverable 3 — Secondary: compiled MITM `m_max(β) ≤ 12` census

If the all-triples certificate passes, here is the census design using the Cycle 78 L/R split and Cycle 79 τ-folding. It decides `m_max ≤ 12` exactly without enumerating all `52,747,567,104` tuples of `P_0`.

Split the 7 slots `L = {1,2,3}`, `R = {4,5,6,7}`. By Cycle 75 the L-product map is injective on `48³ = 110,592` tuples; by Cycle 76 the R-product map is injective on `48⁴ = 5,308,416` tuples. For a target value `v`,

```text
m(v) = #{ l ∈ L_img : v·l^{-1} ∈ R_img and colorL(l) + colorR(v·l^{-1}) ≡ 4 (mod 16) }.
```

Census procedure (`W-CYCLE80-COMPILED-MITM-MMAX-CENSUS`):

1. Build `L_img`: for each of 110,592 L-tuples compute packed product `l` and `colorL = (Σ color) mod 16`. Build a hash map `Rmap : packed R-product -> list of (colorR)` over the 5,308,416 R-tuples (store color multiset per packed key; R-map is injective so each key has one tuple, but keep color).
2. The set of attainable `Φ` values is `V = { l · r : l ∈ L_img, r ∈ R_img }` intersected with the color constraint. Rather than scan all `v`, iterate over the **smaller** side: for each `l ∈ L_img` and each `r ∈ R_img`, form `v = l·r`; increment a counter keyed by `v` **only when** `colorL(l) + colorR(r) ≡ 4 (mod 16)`. The per-`v` counter is exactly `m(v)`. Track the running max.
3. τ-folding (Cycle 79): since `Φ(τ(T)) = K/Φ(T)`, `τ(P_0)=P_0`, and `m(v)=m(K/v)`, you only need to visit one representative per `{v, K/v}` orbit, halving work and giving a free consistency check `m(v)==m(K/v)`. Fixed points `v² = K` are checked directly.
4. Decision: `m_max = max_v m(v)`. Emit `MMAX_CENSUS: m_max = <value>` with `decision = "MMAX_LE_12"` iff `m_max ≤ 12`, else a `thirteen_fold_packet` listing 13 distinct color-compatible `(l, r)` pairs with the common `v` (the explicit ≥13-fold collision in `P_0`).

Cost: the full join is `110,592 × 5,308,416 ≈ 5.9·10¹¹` pairs — too large to materialize naively. The compiled version instead buckets by the color residue and by a hash of `v`: for each `l`, you need `r` with `colorR(r) ≡ 4 − colorL(l)` and `l·r = v`. Fix `v` is wrong direction; instead, **group `R_img` into 16 color buckets**, and for counting `m(v)` you still need the value join. The tractable form: for each `l ∈ L_img` (110,592) and each `r ∈ R_img` in the single compatible color bucket (≈ 5.3M/16 ≈ 331,776), emit `v=l·r` into a counter. That is `110,592 × 331,776 ≈ 3.7·10¹⁰` packed multiplications — feasible in compiled C/Rust with a 16-byte-keyed open-addressing hash and τ-folding (halves it to ~1.8·10¹⁰), but past a heartbeat-local Python budget. Stage it as a Rust/C run with the same packed-product-only equality key and color-as-filter discipline.

The all-triples certificate (Deliverable 1) is the prerequisite gate: it upgrades the fiber-min-distance floor to 4 and rules out the cheap 3-slot collapse routes before paying for the `~10¹⁰`-scale MITM census.

## What I could not do

I could not execute `CHECKER.py` or write it into `output_files`, because this harness exposes only a read-only `Read` tool. The decision (`ALL_3_SUBSETS_PRODUCT_INJECTIVE` vs `PRODUCT_COLLISION_FOUND`) therefore remains open and must come from running the UNRUN checker above. I recommend the next cycle simply run it (Python+NumPy) for the size-3 certificate, then stage the MITM census as a compiled Rust/C job.