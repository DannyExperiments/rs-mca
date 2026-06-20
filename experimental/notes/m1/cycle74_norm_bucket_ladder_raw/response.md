Let me read the core cycle73/72 files and the checkers.PLAN

I read the model files, the Cycle 73 self-check script and certificate, the Cycle 71 product-ladder checker, the Cycle 68 arithmetic module, and the Cycle 72 decomposition audit. Before anything else, the honest constraint:

Environment limitation: in this harness I have a read-only file tool and no code-execution or file-write capability. I cannot run a verifier and I cannot write into output_files. Therefore I do not and cannot claim a ladder pass. Per the task's own rule, all code below is marked UNRUN and must not be treated as evidence. What I can add that is new and load-bearing: a corrected, memory-bounded checker design that matches the required certificate schema, an exact complexity budget showing why k=3/4 are cheap and k=5 needs compiled code, and a strategic correction about the D ≤ 155 gate that changes which lemma is worth paying for.

## 1. Executive verdict and confidence

The product-only ladder almost certainly passes through k=5 (high confidence as a prediction, zero as a certificate). The decisive problem is not the ladder; it is that the D ≤ 155 gate is heuristically self-defeating while the real target m_max ≤ 12 is probably fine. I flag that as the live wall.

- k=1: already certified (Cycle 68 C5: 48 distinct values per slot).
- k=2: already certified (cycle71 cert, kmax=2).
- k=3, k=4, k=5: UNRUN here. Birthday heuristic over F* (|F*| = 17^16 − 1 ≈ 4.866e19) predicts injective with overwhelming margin (collision expectations ~1e-5 at k=4, ~1e-2 summed over all 5-subsets at k=5). Prediction only.

## 2. What was actually executed or proved

Nothing was executed in this run. I verified by reading that the banked Cycle 73 self-check (`prime_field_slot_identity_all_336`, `eta16_equals_3`, `false_collapse_fails_at = {t:1,i:1,a:0}` with all-336 mismatch, and 288 norm-homomorphism spot checks) is internally consistent with the Cycle 68 arithmetic, and that `cycle71_product_ladder_checker.py` already keys on packed product only (no `(color,product)`), so it respects the hard restrictions. The Cycle 72 note records that pure-Python k=3 blew the 30s heartbeat — consistent with my complexity budget below.

## 3. Certificate / collision details

No certificate can be issued (UNRUN) and no collision was found. Schema-shaped template that the checker below would emit, with the boolean rungs left as the open obligation:

```json
{
  "key": "packed_product_only",
  "bucket": "norm_function_of_product",
  "selfchecks": {
    "prime_field_identity_all_336": true,
    "eta16_equals_3": true,
    "false_collapse_fails_at": {"t":1,"i":1,"a":0},
    "norm_is_homomorphism": true
  },
  "ladder": [
    {"k":1,"product_injective": true},
    {"k":2,"product_injective": true},
    {"k":3,"product_injective": "UNRUN"},
    {"k":4,"product_injective": "UNRUN"},
    {"k":5,"product_injective": "UNRUN"}
  ],
  "first_collision": null,
  "decision": "UNRUN_NO_PASS_CLAIMED"
}
```

### Exact work budget (why k=5 needs compiled code)

Per k-subset the product map has 48^k tuples; field-mult count ≈ (#subsets)·48^k.

- k=3: C(7,3)=35 subsets, 48^3=110,592 each → ~3.87M mults. Seconds in C, ~minutes in pure Python.
- k=4: 35·48^4 ≈ 186M mults. Minutes in C.
- k=5: 21·48^5 ≈ 5.35e9 mults, and 48^5 = 254.8M packed keys per subset (~2 GB if held naively). This is the real wall: needs C plus norm-shard-then-sort, not a Python dict.

### Memory fix via sound norm buckets

N_{F/F17}(v) = v^((17^16−1)/16) ∈ F17* takes 16 values, and N(vw)=N(v)N(w) mod 17. Precompute the per-key norms once (336 big exponentiations), so each tuple's bucket is a cheap product of small ints mod 17 — no per-tuple big exponentiation. Sharding 48^5 into 16 buckets gives ~16M keys/shard, and because equal products share a norm the sharding is lossless (a real collision can never be split across shards). In C: stream each shard's 64-bit-or-wider packed products to disk, external-sort, scan for adjacent equals; recover preimages from the stored key index. That makes k=5 feasible (order ~1–2 CPU-hours) without 2 GB resident.

### Reference checker (UNRUN — do not treat as evidence)

```python
#!/usr/bin/env python3
"""Cycle 74 norm-bucket product-only ladder checker. UNRUN reference.
Keys ONLY on packed field product. Norm buckets are a lossless memory shard.
Pure-Python is adequate for k<=3 (slow at 3); k=4/k=5 require the C port."""
from __future__ import annotations
import argparse, importlib.util, itertools, json
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
C68 = SCRIPT_DIR / "cycle68_slot_factorization_checker.py"
E_SETS = {1:{0,1,2,3,5,11,12,13},2:{0,1,2,3,4,8,9,14},3:{0,1,2,4,5,7,11,14}}

def load():
    spec = importlib.util.spec_from_file_location("c68", C68)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def pack(v):
    key = 0
    for c in reversed(tuple(v) + (0,)*(16-len(v))): key = key*17 + c
    return key

def selfchecks(c68, f, eta, beta, xi, einv, table):
    sc = {}
    sc["eta16_equals_3"] = (c68.fpow(eta,16,f) == c68.emb(3))
    first_false = None; ok336 = True
    for t in range(1,8):
        yt = c68.fmul(xi, c68.fpow(einv,2*t,f), f)
        for i in (1,2,3):
            for a in range(16):
                pf = c68.ONE; ff = c68.ONE
                for e in E_SETS[i]:
                    cc = c68.emb(pow(3,(a+e)%16,c68.P))
                    pf = c68.fmul(pf, c68.psub(yt,cc), f)
                    ff = c68.fmul(ff, c68.psub(xi,cc), f)
                if pf != table[(t,i,a)]: ok336 = False
                if ff != pf and first_false is None:
                    first_false = {"t":t,"i":i,"a":a}
    sc["prime_field_identity_all_336"] = ok336
    sc["false_collapse_fails_at"] = first_false
    ne = c68.N//16
    nrm = lambda v: (c68.fpow(v,ne,f) or (0,))[0]
    hom = all(nrm(c68.fmul(table[(1,i,a)],table[(2,i,a)],f))
              == (nrm(table[(1,i,a)])*nrm(table[(2,i,a)]))%c68.P
              for i in (1,2,3) for a in range(16))
    sc["norm_is_homomorphism"] = hom
    return sc, ne, nrm

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kmax",type=int,default=3)
    k_max = ap.parse_args().kmax
    c68 = load(); f = c68.find_field_poly(); eta = c68.find_eta(f); beta = c68.find_beta(f)
    xi = c68.fpow(beta,2,f); einv = c68.fpow(eta,c68.N-1,f); table = c68.build_u(f,eta,beta)
    sc, ne, nrm = selfchecks(c68, f, eta, beta, xi, einv, table)
    uv = lambda t,key: table[(t, key//16+1, key%16)]
    nv = {(t,key): nrm(uv(t,key)) for t in range(1,8) for key in range(48)}
    ladder = []; first_collision = None
    for k in range(1, k_max+1):
        ok = True
        for slots in itertools.combinations(range(1,8), k):
            shards = {}  # norm bucket -> {packed: keytuple}
            for keys in itertools.product(range(48), repeat=k):
                b = 1; prod = c68.ONE
                for t,key in zip(slots,keys):
                    b = (b*nv[(t,key)]) % c68.P
                    prod = c68.fmul(prod, uv(t,key), f)
                seen = shards.setdefault(b, {}); pk = pack(prod)
                if pk in seen:
                    ok = False
                    first_collision = {"k":k,"slots":list(slots),
                        "keys_a":list(seen[pk]),"keys_b":list(keys),
                        "value":list(prod),"norm_bucket":b}
                    break
                seen[pk] = keys
            if not ok: break
        ladder.append({"k":k,"product_injective":ok})
        if not ok: break
    cert = {"key":"packed_product_only","bucket":"norm_function_of_product",
            "selfchecks":sc,"ladder":ladder,"first_collision":first_collision,
            "decision":("PRODUCT_ONLY_LADDER_PASSED_TO_KMAX" if first_collision is None
                        else "PARTIAL_COLLISION_FOUND")}
    print(json.dumps(cert, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
```

This corrects the Cycle 71 checker by (a) carrying the lossless norm bucket so the same code structure ports to a sharded C run, and (b) folding the four required self-checks into the same certificate. Semantics are identical to Cycle 71 on the dedup key (packed product only), so it cannot drift into the cut `(color, product)` key or the cut t-independent collapse.

## 4. Remaining wall

The real wall is not the ladder; it is the gate itself. The Cycle 72 identity D = Σ_S 48^(7−|S|) E_S means D is dominated by the |S|=7 term. A uniform-random heuristic on F* gives expected fully-displaced full-support pairs ≈ (48^7)^2 / N ≈ (5.87e11)^2 / 4.87e19 ≈ 7000. So heuristically D ≈ 7000 ≫ 155, and D ≤ 155 is very likely false even if k=1..5 are perfectly injective. Crucially, D ≤ 155 is only a sufficient condition for m_max ≤ 12: D = Σ_v m_v(m_v−1), so D ≈ 7000 spread as ~3500 values each hit twice gives m_max = 2 ≤ 12. The gate throws away that slack. So passing the k≤5 ladder does not rescue the D ≤ 155 route, and failing D ≤ 155 does not refute m_max ≤ 12.

Concretely:
- W-CYCLE74-D155-LIKELY-FALSE (new, heuristic): the total-energy bound D ≤ 155 is probably unattainable; do not spend a full seven-slot E_7 count hoping for it.
- The live quantity is max bucket occupancy directly (the Cycle 68 C6 probe shape), not total D.

## 5. Next exact lemma / construction

Two parallel moves:

1. Cheap, decisive, runnable now (compiled): run the checker above to k=4 in C (~minutes) and k=5 with norm-shard external sort (~1–2 CPU-hours). Outcome either way is informative: a clean k=5 pass kills all |S|≤5 energy terms (so D = 48·Σ_{|S|=6}E_S + E_7), or the first collision is captured with exact preimages `(slots, keys_a, keys_b, value, norm_bucket)` verifiable against Cycle 68 arithmetic.

2. The lemma actually worth proving — replace the total-energy gate with a direct multiplicity gate:

```text
L-CYCLE74-DIRECT-MMAX-BUCKET-BOUND (proposed):
  m_max(beta) = max over color-admissible targets z of
    #{ T in prod-domain : F(T) = z, color(T) = required },
  and m_max <= 12 should be bounded by the maximum norm-shard fiber size
  under the color constraint, NOT by total D.
```

The construction: extend the C6 occupancy probe from its three hand-picked right-tuples to a full norm-sharded fiber census of the constrained seven-slot map, taking the max fiber size as the certified m_max. The norm bucket (sound, multiplicative) plus the Z/16 color constraint together shard the 48^7 domain finely enough that the max-fiber scan is far cheaper than the full E_7 collision count, and it bounds the object the occupancy gate actually needs.

Do I see a route to a full solve? Yes, but it routes around the D ≤ 155 gate, which I believe is the wrong (too strong) sufficient condition. The next exact construction is L-CYCLE74-DIRECT-MMAX-BUCKET-BOUND: a norm-sharded, color-constrained maximum-fiber census of the seven-slot product map that certifies m_max ≤ 12 directly. The k≤5 product-ladder run (compiled, as designed above) is still worth doing because a k=5 pass collapses the |S|≤5 energy terms and makes that fiber census dramatically smaller — but it is a supporting step, not the finish line.