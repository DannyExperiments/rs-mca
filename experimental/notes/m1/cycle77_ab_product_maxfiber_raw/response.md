I'll start by reading the file index and the core project files to understand the current state.I only have the `Read` tool available in this environment. I cannot run code or write files. I'll state this explicitly in my deliverable, mark any code `UNRUN`, and provide the analysis inline. Let me read the core strategic files.The key state is clear. Let me read the Cycle 76 audit and the Cycle 77 prompt packet, plus the model definition files.Now let me read the Cycle 77 prompt packet and the underlying model/slot definitions.Now I need the actual slot/color definitions. Let me read the certification scripts and the model brief.The critical file is the Cycle 68 slot factorization checker that builds `u_t(k)`. Let me find and read it.I have the full picture now. I've read the model definition (`cycle68_slot_factorization_checker.py`), the right-half certificate logic (`cycle76_fast_right_half_check.py`), the Cycle 76 audit, and the Cycle 77 prompt. Let me verify two more anchors before writing: the banked-lemmas context for `m_max` and the Cycle 75 left-half certificate.I have enough to write the deliverable. Let me confirm my tool situation and one model constant before finalizing.

Note on environment: my only available tool in this harness is `Read`. I cannot execute code, run a census, or write files to `output_files`. So I deliver everything inline, and any code below is explicitly `UNRUN`.

---

# RS-MCA Cycle 77 — AB Product Max-Fiber / Max-Intersection Wall

## 1. Executive verdict and confidence

ROUTE_CUT on "prove `≤12` by hand": there is no hand proof of `max_v |A ∩ vB^{-1}| ≤ 12`. The quantity is a worst-case fiber size of a structured 7-block multiplicative map; closing it at the constant `12` requires an exact finite census (a run). I have only `Read`, so I cannot run it.

What I can bank, fully rigorously and without a run:

- BANKABLE_LEMMA (exact reduction): `m_max` is the max multiplicity of the single evaluation map `S ↦ ∏_{c∈S}(β²−c)` over "configurations" `S`, and equivalently a 7-block subset-sum collision problem mod `N=17^16−1`. This is sharper than `A∩vB^{-1}` and exposes legal norm shard keys.
- BANKABLE_LEMMA (coding/structural): a product fiber is a code of length 7 over alphabet `[48]`; its minimum Hamming distance is controlled by subset-product injectivity. Unconditionally (from the banked single-slot injectivity C5) `d ≥ 2`. With cheap additional all-subset injectivity certificates the ladder reaches `m_max ≤ 48`. This does not reach `12`, but it is the honest provable ceiling.
- AUDIT (heuristic, not proof): a uniform-random model predicts only `≈ 29` colliding tuple-pairs inside `P_0`, so the true `m_max` is almost certainly `2` or `3`, comfortably under `12` with large margin. The injectivity already proven on both halves is consistent with collision suppression.
- PLAN + exact certificate schema: a meet-in-the-middle, norm-sharded, color-filtered census that outputs `MMAX_CERTIFIED_LE_12` (or a `THIRTEEN_FOLD_PACKET`). I give the precise algorithm and `UNRUN` code.

Confidence: high that `m_max ≤ 12` is true (heuristic margin is ~4 orders of magnitude on the collision count); high that the reduction lemmas are correct (derived from the machine-checked C1 factorization); the constant `12` itself is only certifiable by the census.

## 2. Exact results

### 2.1 BANKABLE_LEMMA `L-CYCLE77-CONFIG-EVALUATION-REDUCTION` (PROOF)

From the Cycle 68 checker, machine-checked block C1, the slot table satisfies, for `k=16(i−1)+a`,
```
u_t(k) = 3^{-t} · ∏_{b ∈ bset(i,a)} (β² − η^{2t+16b}),   bset(i,a) = {(a+e) mod 16 : e ∈ E_i}.
```
Let `ξ = β²`. For a 7-tuple `T=(k_1,…,k_7)`, `k_t=(i_t,a_t)`,
```
Φ(T) = ∏_{t=1}^7 u_t(k_t) = 3^{-28} · ∏_{c ∈ S(T)} (ξ − c),
S(T) = ⊔_{t=1}^7 C_t,   C_t = { η^{2t+16b} : b ∈ bset(i_t,a_t) } ⊂ R_t = η^{2t}·F_17*.
```
Facts (each proved): (i) `∑_{t=1}^7 t = 28`, so the constant is `3^{-28}`. (ii) `η` has order 256 (`η^16=3`, and `3` is a primitive root mod 17, order 16). (iii) The cosets `R_1,…,R_7` are disjoint: `η^{2(t−t')} ∈ ⟨η^16⟩=F_17*` iff `8 | (t−t')`, impossible for `1≤|t−t'|≤6`. (iv) `|C_t|=8`, so `|S(T)|=56`, and `T ↦ S(T)` is a bijection onto the set of configurations (recover `k_t` from `S∩R_t`; the 48 subsets per coset are distinct, C3). (v) Every factor `ξ−c ≠ 0` (`build_u` asserts `u≠0`).

Therefore
```
Φ(T) = Φ(T')  ⟺  ∏_{c∈S(T)}(ξ−c) = ∏_{c∈S(T')}(ξ−c),
m_max(β) [color-free]  =  max multiplicity of the map  S ↦ ∏_{c∈S}(ξ−c).
```
Discrete-log form: fix a primitive root `γ` of `F*`, set `L_c = log_γ(ξ−c) ∈ Z/N`. A configuration chooses, in each of 7 blocks (cosets) of 16 weights, one of 48 admissible 8-subsets; two configurations collide iff their block-subset-sums of `{L_c}` are equal mod `N`. This is `≡` the `A∩vB^{-1}` bound but refined to 7 blocks, which is what enables sharding.

Legal shard keys (functions of the product, per discipline): for any subfield `F_{17^d} ⊆ F` with `d | 16`, the relative norm `N_{F/F_{17^d}}(Φ(T))` is multiplicative and a function of `Φ(T)` alone. `N_{F/F_17}` lands in `F_17*` (16 shards); `N_{F/F_{17^8}}` lands in `F_{17^8}*` (up to `17^8−1≈6.97×10^9` shards). These are admissible MITM keys.

### 2.2 BANKABLE_LEMMA `L-CYCLE77-FIBER-IS-A-CODE` (PROOF, with a conditional tail)

Fix a value `v`. Its fiber `Φ^{-1}(v)` is a set of 7-tuples over `[48]`. Claim: if `T≠T'` lie in the same fiber and `D ⊆ {1,…,7}` is the set of coordinates where they differ, then the product map on slot-set `D` is **non-injective**.

Proof: the agreeing coordinates contribute equal factors, so `∏_{t∈D} u_t(k_t) = ∏_{t∈D} u_t(k'_t)` with `(k_t)_{t∈D} ≠ (k'_t)_{t∈D}`. ∎

Contrapositive ⇒ a Hamming-distance bound on the fiber-as-code:

- Unconditional now (single-slot injectivity C5 is banked): `|D| ≠ 1`, so **min distance `d ≥ 2`**. (Two tuples in a fiber cannot differ in exactly one slot.)
- If all 2- and 3-subset product maps are injective (21+35 cheap checks, each `≤48^3`), then `d ≥ 4`.
- Adding all 4-subset injectivity (banked for `{4,5,6,7}`; the other 34 are cheap): `d ≥ 5`.
- Adding all 5-subset injectivity (`C(7,5)=21` maps, each `48^5≈2.5×10^8`): `d ≥ 6 ⟹` any 2 coordinates determine the tuple `⟹ m_max ≤ 48² = 2304`.
- Adding all 6-subset injectivity (`7` maps, each `48^6≈1.2×10^{10}`): `d ≥ 7 ⟹` any single coordinate determines the tuple `⟹ m_max ≤ 48`.

So the strongest clean structural ceiling is `m_max ≤ 48`, conditional on an all-subset injectivity certificate up to size 6. This is genuinely tighter than the trivial `|A|`/`|B|` bounds and is the honest "no-census" wall. It does **not** reach `12`: the gap from `48` to `12` is exactly what the census must close. Norms give no within-fiber reduction (all tuples in a fiber share the same `v`, hence the same norms).

### 2.3 AUDIT — second-moment estimate (heuristic, NOT a proof)

Under a uniform-random model for `Φ` on `P_0` (`|P_0| = 52{,}747{,}567{,}104`, `|F*| = 17^16−1 ≈ 4.8665×10^{19}`):
```
E[ #ordered colliding pairs in P_0 ] ≈ |P_0|² / |F*| ≈ 2.78×10^{21} / 4.87×10^{19} ≈ 57.1,
```
i.e. `≈ 29` unordered colliding pairs. With so few collisions, the max fiber is almost surely `2` (perhaps `3`), far below `12`. The half-map injectivity already certified (zero collisions among `48^3` and `48^4`) is consistent with the structure suppressing, not amplifying, collisions. This is strong evidence that the census will return `m_max ∈ {1,2,3}` and that **no 13-fold packet exists** — but it is a heuristic, not a certificate.

## 3. Counterpacket assessment

COUNTERPACKET (`THIRTEEN_FOLD_PACKET`): none constructible by hand, and the second-moment estimate argues none exists. A 13-fold fiber would contribute `≥13` to the first moment and `≥13·12=156` ordered pairs to a collision budget whose expectation over all of `P_0` is `≈57`. Producing one would require a strong, presently unidentified low-degree multiplicative identity among the 112 atoms `{ξ−c}`. I found no such identity in the shape data (`E_1,E_2,E_3` and their cyclic shifts) by inspection. Verdict: a counterpacket is very unlikely; the census is the decider.

## 4. Exact certificate schema → `MMAX_CERTIFIED_LE_12` (PLAN + UNRUN code)

This is the acceptable "compiled/sharded census paired with a clear certificate schema." It computes `m_max` **exactly**, with colors, using only packed-field-product equality.

Algorithm (meet-in-the-middle, norm-sharded, color-filtered):
1. Build `A` = the 110592 left products `u1·u2·u3`, each tagged with its (well-defined, since left-injective) color sum `c_L ∈ Z/16` and key. Build `B` = the 5308416 right products `u4·u5·u6·u7`, tagged with `c_R`.
2. Shard by `s = N_{F/F_17}(value) ∈ F_17*` (a legal product-function key, 16 shards). For a fiber over `v`, every contributing `a∈A`, `b∈B` satisfies `N(a)·N(b)=N(v)`; so only `(a,b)` with `N(a)N(b)=s` can co-occur in an `s`-shard fiber. (For more parallelism, refine with `N_{F/F_{17^2}}` or `N_{F/F_{17^8}}`.)
3. Within a shard, stream all `(a,b)` pairs with `N(a)N(b)=s` and `c_L+c_R ≡ 4 (mod 16)`; emit `v=a·b` to disk buckets keyed by `hash(v)`; external-sort each bucket; the run-length of equal `v` is that fiber's `P_0` multiplicity. Track the global max. (Color-free max is obtained by dropping the `c_L+c_R≡4` filter; report both.)
4. Decision: if global max `≤ 12` emit `MMAX_CERTIFIED_LE_12`; if a `v` with multiplicity `≥13` is found, emit `THIRTEEN_FOLD_PACKET` with the 13 tuples, their colors, and `v`.

Work is `O(|A|·|B|/16)` field multiplications per the F_17-norm shard (`≈3.7×10^{10}` per shard), trivially parallel; the norm filter and color filter remove most pairs before emission. Feasible in compiled C across a few cores/machines.

`UNRUN` reference implementation (reuses `cycle68_slot_factorization_checker.py`; equality key = packed product only):

```python
# UNRUN — requires execution + cluster sharding; here for schema clarity only.
import importlib.util, itertools
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "c68", "experimental/scripts/cycle68_slot_factorization_checker.py")
c68 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c68)

P, NDEG = 17, 16
f   = c68.find_field_poly(); eta = c68.find_eta(f); beta = c68.find_beta(f)
tbl = c68.build_u(f, eta, beta)
S_COLOR = {1:15, 2:9, 3:12}
def color(k): i,a = k//16+1, k%16; return (S_COLOR[i] + 8*(a%2)) % 16
def uval(t,k): i,a = k//16+1, k%16; return tbl[(t,i,a)]
def fmul(x,y): return c68.fmul(x,y,f)
def pack(v):
    key=0
    for c in reversed(tuple(list(v)+[0]*(NDEG-len(v)))): key=key*P+(c%P)
    return key
def norm17(v):  # N_{F/F17}(v) = v^{(17^16-1)/16}, a legal product-function shard key
    e=(P**NDEG-1)//(P-1); return pack(c68.fpow(v, e, f))

# A: left 3-slot products (injective => color well-defined), tagged (key,color)
A=[]
for k1 in range(48):
  u1=uval(1,k1); c1=color(k1)
  for k2 in range(48):
    u12=fmul(u1,uval(2,k2)); c12=(c1+color(k2))%16
    for k3 in range(48):
      A.append((pack(fmul(u12,uval(3,k3))),(c12+color(k3))%16,(k1,k2,k3)))
# B: right 4-slot products, tagged similarly (built the same way over slots 4..7)
# ... (symmetric; omitted for brevity)

# Census core (per F17-norm shard s): for legal pairs emit v=a*b under
# color filter (cL+cR)%16==4, bucket by hash(v), external-sort, take max run length.
# Decision: max_mult<=12 -> MMAX_CERTIFIED_LE_12 ; >=13 -> THIRTEEN_FOLD_PACKET.
```

Certificate JSON schema to emit:
```json
{"model":{"field_poly":[...],"eta":[...],"beta":[...]},
 "key":"packed_product_only","shard_key":"N_{F/F17}(product)",
 "color_filter":"sum_t color(k_t) == 4 (mod 16)",
 "m_max_product_colorfree": <int>, "m_max_P0_with_colors": <int>,
 "decision": "MMAX_CERTIFIED_LE_12" | "THIRTEEN_FOLD_PACKET",
 "witness": null | {"v":<packed>,"tuples":[[k1..k7] x13],"colors":[...]}}
```

## 5. What remains open

The single open item is the exact value of `m_max`. Everything else is settled or reduced: the equality key is the packed product; both halves are injective; `m_max` equals the configuration-evaluation multiplicity (2.1); the structural ceiling without a census is `m_max ≤ 48` (2.2, conditional on subset-injectivity up to size 6); heuristics put the true value at `2`–`3` (2.3). Closing `≤ 12` requires running the §4 census (or, more cheaply, just proving full 7-slot injectivity if the census shows `m_max=1`).

## 6. Next exact lemma / construction

`L-CYCLE78-FULL-PRODUCT-INJECTIVITY-OR-EXACT-MMAX`: run the §4 norm-sharded MITM census to compute `m_max` exactly. Concretely, the next exact step that is *both* cheap and decisive:

> Certify all-subset product injectivity up to size 6 (the 34 missing 4-subsets, the 21 5-subsets, the 7 6-subsets). If all pass, bank `m_max ≤ 48` unconditionally (2.2). Then run the single F_17-norm-sharded MITM pass; if it returns max multiplicity `1`, the full 7-slot map is injective and `m_max = 1 ≤ 12` (`MMAX_CERTIFIED_LE_12`, with maximal margin); otherwise it returns the exact `m_max` and, if `≥13`, the explicit packet.

If a fast partial-sum prefilter is wanted before the full census, the highest-value micro-lemma is: tabulate the 4-slot right block-subset-sums `{L_c}` restricted modulo the F_17-norm (16 classes) and confirm the per-class right-product counts, which lets the census skip the `≈15/16` of `(a,b)` pairs whose norms cannot match — turning the census from `|A||B|` into `≈|A||B|/16` before the color filter.