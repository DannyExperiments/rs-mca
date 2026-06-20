I'll start by reading the file index, then work through the key files systematically.I only have the Read tool available in this environment, so I cannot execute code or write output files. I'll note that explicitly in my deliverable and mark any code as UNRUN. Let me locate the key files. I'll try the most likely paths and search the index in parallel.Now the raw response and the checker scripts.Now the certificate and the raw response.I have the core model and the Cycle 72 state. Let me read the remaining required evidence files: the cuts/walls/lemmas and the cycle 68-71 audits.Let me use the project root files referenced in the prompt.Now let me read the remaining audits and state files in parallel.Now the cycle69, cycle70, cycle71 audits and the walls/lemmas files in parallel.BANKABLE_LEMMA

I worked through the read-order files and the Cycle 66/68 model. Operational constraint first: in this harness my only tool is read-only `Read`. I cannot write to `output_files/` or execute code. So I deliver every artifact inline, clearly marked `UNRUN`, and I have fabricated no run output. The prior Cycle 72 worker faced the same constraint.

## 1. Executive verdict and confidence

Product-only `k=3/k=4/k=5` injectivity is still **OPEN** — not proved, not falsified, no collision found. I cannot close it because I cannot execute, and no cheap structural proof exists (the Frobenius obstruction below stands).

What I *do* bank this cycle, with high confidence (hand-verified arithmetic):

- **L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL** — a clean reformulation that collapses each slot value to the evaluation of a fixed degree-8 polynomial *over the prime field* `F_17`. This is a strong independent self-check on the Cycle 68 table and a real speed-up.
- **L-CYCLE73-SOUND-NORM-BUCKET** — the principled, *lossless* replacement for the cut `(color, product)` key, which makes the `k≥5` rungs memory-tractable. It pins down exactly why color was unsound and norm is sound.
- A clarification (**L-CYCLE73-UNCONSTRAINED-D-DOMINATES**) that the decomposition's unconstrained `D` dominates the gate's constrained `D`, so bounding the unconstrained one suffices.

Confidence: high on the three lemmas (verified below by hand); the ladder rungs and `D≤155` remain unproven and all code is `UNRUN`.

## 2. What is proved / planned / open

**Proved (banked, hand-checked):**

The slot map factors through the prime field. Using `η^16 = 3` (verified: `η=6X^9`, `η^16 = 6^16·X^144 = 1·X^144`, and `X^144 = (X^8)^18 = N_{F_{17^2}/F_17}(X^8) = 3` since `u=X^8` satisfies `u^2+u+3=0`):

```text
u_t(i,a) = P_{S_j}(y_t),   y_t = β² η^{−2t} ∈ F,   P_{S}(Y)=∏_{c∈S}(Y−c) ∈ F_17[Y],
S_j = { 3^{(a+e) mod 16} : e ∈ E_i }  (one of 48 fixed 8-subsets of F_17^*).
```

Derivation of the cancellation that kills the spurious `(−1)^a`: the Cycle 68 build gives `u_t(i,a)=(−1)^a ∏_{e∈E_i}(ξ·3^{−a}·η^{−2t} − 3^e)`. Pull `3^{−a}` out of all 8 factors: `=(−1)^a·3^{−8a}·∏_e(y_t−3^{a+e})`. Since `3^8=16=−1` in `F_17`, `3^{−8a}=(−1)^a`, so `(−1)^a·3^{−8a}=1`. Hence `u_t(i,a)=∏_{e∈E_i}(y_t−3^{(a+e) mod 16})=P_{S_j}(y_t)`. I checked `P_1` against `P_COEFFS[1]`: `S_1=3^{E_1}={1,3,9,10,5,7,4,12}`, `∏=6 mod 17`, matching the constant term `6`. So `P_i` equals the Cycle 68 polynomial table exactly. Each slot value is one fixed prime-field polynomial evaluated at the slot's scalar `y_t`; only `y_t` moves with `t`.

The sound-bucket lemma: for any subfield `K⊆F`, `N_{F/K}` is a multiplicative homomorphism, so the per-tuple quantity `∏_t N(u_t)=N(∏_t u_t)=N(v)` is **a function of the product `v` alone**. Therefore keying/bucketing by `N(v)` never separates two equal-product tuples — it is lossless for both PASS and collision detection. Color fails precisely because it is *not* a function of `v` (it is the discrete-log-mod-16 of the root product, independent data), which is exactly the Cycle 71 cut. Concretely `N_{F/F_17}(u_t(j)) = ∏_{c∈S_j} χ_t(c)` where `χ_t` is the degree-16 characteristic polynomial of `y_t` over `F_17` — all in `F_17`.

`D` clarification: the gate's `m_v` runs over the color-constrained `P_0` (`|P_0|=8^7·25152=52,747,567,104`); the decomposition's `D` runs over all `48^7` tuples. Constrained pairs are a subset of all equal-product pairs, so `m_max^{constr}(m_max^{constr}−1) ≤ D_{constr} ≤ D_{unconstr}`. Hence `D_{unconstr} ≤ 155 ⇒ m_max ≤ 12 ⇒ Occ ≥ |P_0|/12 = 4,395,630,592 > 2^32` (and `|P_0|/13 ≈ 4.058e9 < 2^32`, so only `m_max≥13`, i.e. `D≥156`, obstructs). Bounding the *unconstrained* `D` suffices and is color-free.

**Planned (verifier + energy):** a single self-checking product-only verifier (§4) with norm bucketing and fully-displaced energy counting; the `k=5/6/7` energy schedule (§5).

**Open:** whether `k=3,4,5` are product-injective; the six-slot energies; `E_full`; therefore `D≤155`.

**Forbidden shortcuts (explicitly avoided):** I did not use the false t-independent Cycle 70 collapse (my checker asserts it fails at `(1,1,0)`). I did not use `(color,product)` as a duplicate key — only packed product, with `N(v)` as a *sound* bucket. No prize/MCA promotion; no probabilistic evidence as proof.

**Frobenius obstruction (why no cheap proof):** `φ:y↦y^17` fixes `F_17` and permutes the `P_S` arguments cleanly, but `ξ=β²∉F_17`, so `φ(y_t)≠y_t`; applying `φ` to a hypothetical relation `∏(y_t−c)^{ε}=1` lands on `φ(y_t)`, not `y_t`. The natural Galois symmetry is not a symmetry of the relation, so injectivity is a genuine finite condition on this `β`.

## 3. Explicit certificates

No collision found (none can be claimed without a run). Banked executed fact: `k=1,2` product-only injective (`cycle71_product_ladder_certificate.json`, `max_good_k=2`, `key=packed_product_only`). The Cycle 68 `C6` probe (`m_max_lower_bound_probe=1`) is **color-restricted** (dedups within one fixed total-color class on slots `{1,2,3}` only, 3 right-tuples → needed colors `{4,6,14}`); it covers 1 of 35 three-subsets and cannot see cross-color collisions, so it does **not** establish `k=3`. I decline to upgrade it. Certificate schema in §4.

## 4. Exact code (reference, UNRUN — I cannot execute or write files here)

Self-contained product-only verifier; imports the banked Cycle 68 arithmetic, builds the table the Cycle 68 way and re-derives it via the prime-field identity and asserts equality on all 336 entries, asserts the false collapse fails at `(1,1,0)` and `η^16=3`, checks the norm homomorphism (soundness witness), keys collisions by product only, recovers preimages, and optionally counts fully-displaced `E_S`.

```python
#!/usr/bin/env python3
"""Cycle 73 product-only ladder + displacement-energy verifier (reference, UNRUN).
Keys collisions by PACKED FIELD PRODUCT ONLY. N_{F/F17}(v) is a FUNCTION OF v
(homomorphic image) hence a LOSSLESS bucket -- unlike color. Self-checks the
prime-field slot identity u_t(j)=P_{S_j}(y_t) on all 336 entries.
Run: python3 CHECKER.py --kmax 3 [--energy]   # k>=4 use the C kernel."""
from __future__ import annotations
import argparse, importlib.util, itertools, json
from pathlib import Path
C68 = Path(__file__).resolve().parent / "cycle68_slot_factorization_checker.py"
E_SETS = {1:{0,1,2,3,5,11,12,13}, 2:{0,1,2,3,4,8,9,14}, 3:{0,1,2,4,5,7,11,14}}
def load_c68():
    s = importlib.util.spec_from_file_location("c68", C68)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kmax", type=int, default=3)
    ap.add_argument("--energy", action="store_true"); a = ap.parse_args()
    if not 1 <= a.kmax <= 7: raise SystemExit("kmax in 1..7")
    c = load_c68(); P = c.P
    f = c.find_field_poly(); eta = c.find_eta(f); beta = c.find_beta(f)
    assert f == (3,)+(0,)*7+(1,)+(0,)*7+(1,) and eta == (0,)*9+(6,) and beta == (2,1)
    assert c.fpow(eta,16,f) == c.emb(3), "eta^16 != 3"          # banked structural fact
    xi = c.fpow(beta,2,f); einv = c.fpow(eta, c.N-1, f)
    table = c.build_u(f, eta, beta)
    # --- self-check: prime-field identity (336x) + false-collapse cut ---
    false_fail = None
    for t in range(1,8):
        yt = c.fmul(xi, c.fpow(einv, 2*t, f), f)
        for i in (1,2,3):
            for aa in range(16):
                S = [pow(3,(aa+e)%16,P) for e in E_SETS[i]]
                tru = c.ONE
                for cc in S: tru = c.fmul(tru, c.psub(yt, c.emb(cc)), f)
                assert tru == table[(t,i,aa)], (t,i,aa)         # L-CYCLE73-PRIME-FIELD
                fls = c.ONE
                for cc in S: fls = c.fmul(fls, c.psub(xi, c.emb(cc)), f)
                if fls != tru and false_fail is None: false_fail = {"t":t,"i":i,"a":aa}
    assert false_fail == {"t":1,"i":1,"a":0}, false_fail        # Cycle-70 cut enforced
    def uval(t,k): return table[(t, k//16+1, k%16)]
    def pack(v):
        key = 0
        for x in reversed(tuple(v)+(0,)*(16-len(v))): key = key*P + x
        return key                                              # 17^16 ~ 2^65.4: Python big int
    Nexp = c.N//16
    def norm17(v):
        nv = c.fpow(v, Nexp, f); return nv[0] if nv else 0      # N_{F/F17}(v) in F_17
    # soundness witness: norm is a homomorphism (so norm-bucketing is lossless)
    p12 = c.fmul(uval(1,0), uval(2,0), f)
    assert norm17(p12) == (norm17(uval(1,0))*norm17(uval(2,0)))%P
    assert all(len({table[(t,i,aa)] for i in (1,2,3) for aa in range(16)})==48 for t in range(1,8))
    # --- product-only ladder (+ optional fully-displaced E_S for |S|>=5) ---
    ladder=[]; first=None; energy={}
    for k in range(1, a.kmax+1):
        ok=True
        for J in itertools.combinations(range(1,8), k):
            groups={}
            for keys in itertools.product(range(48), repeat=k):
                p=c.ONE
                for t,kk in zip(J,keys): p=c.fmul(p, uval(t,kk), f)
                pk=pack(p)
                if pk in groups:
                    if ok:
                        ok=False; a0=groups[pk][0]
                        first={"k":k,"slots":list(J),"keys_a":list(a0),
                               "keys_b":list(keys),"value":list(p)}
                    groups[pk].append(keys)
                else: groups[pk]=[keys]
            if a.energy and k>=5:
                es=0
                for lst in groups.values():
                    if len(lst)<2: continue
                    for x in lst:
                        for y in lst:
                            if x is not y and all(x[m]!=y[m] for m in range(k)): es+=1
                energy[str(list(J))]=es
            if not ok and not a.energy: break
        ladder.append({"k":k,"product_injective":ok})
        if not ok and not a.energy: break
    good=0
    for r in ladder:
        if r["product_injective"]: good=r["k"]
        else: break
    print(json.dumps({
        "model":{"field_poly":list(f),"eta":list(eta),"beta":list(beta)},
        "key":"packed_product_only",
        "selfchecks":{"prime_field_identity_all_336":True,"eta16_equals_3":True,
                      "norm_is_homomorphism":True,"false_collapse_fails_at":false_fail,
                      "single_slot_injective":True},
        "ladder":ladder,"max_good_k":good,"min_collision_support_if_no_failure":good+1,
        "first_collision":first,"displacement_energy_E_S":(energy or None),
        "decision":"PRODUCT_ONLY_LADDER_PASSED_TO_KMAX" if first is None
                   else "PARTIAL_COLLISION_FOUND"}, indent=2, sort_keys=True))
if __name__=="__main__": main()
```

Cost notes (honest): `k=3` is `35·48^3≈3.9M` products — borderline in CPython (tens of seconds, the heartbeat killer in Cycles 69–72), fine in C. `k=4` is `35·48^4≈1.86e8`; `k=5` is `21·48^5≈5.35e9` (≈85 GB if stored naively → **requires** bucketing). The `k=3/k=4` C kernel in the Cycle 72 `response.md` (the `unsigned __int128` packer with the `X^16=−X^8−3` reduction `t[d-8]-=ct; t[d-16]-=3*ct`) is correct as written; reuse it. The new piece for `k=5` and bounded memory is norm bucketing:

```c
/* k=5 product-only detector, memory-bounded by SOUND norm passes. UNRUN.
   norm17[t][k] = N_{F/F17}(u_t(k)) in 1..16, dumped alongside slot_table.txt.
   Pass r in 1..16 keeps only tuples whose product-norm == r (== prod_t norm17),
   so each pass stores <= 48^5/16 ~ 16M u128 keys (~256MB). Sound: equal product
   => equal norm => same pass, so no collision is ever split across passes. */
for (int r = 1; r <= 16; r++) {
  for each 5-subset J of {0..6}:
    n = 0;
    for (a..e in 0..47):                       /* incremental fmul over J */
      nm = (N[J0][a]*N[J1][b]*N[J2][cc]*N[J3][d]*N[J4][e]) % 17;
      if (nm != r) continue;                   /* route to its own pass */
      fmul5(...,P5); E[n].k = pk(P5); E[n].idx = enc(a,b,cc,d,e); n++;
    qsort(E,n,...);                            /* compare full products within pass */
    for (i=1;i<n;i++) if (E[i].k==E[i-1].k) report_collision_with_preimages(J,...);
}
/* finer partition (N to F_{17^2}, 288 classes) if 256MB/pass is still too big. */
```

Fully-displaced energy `E_S` (for the `D` bound) is the same enumeration but, instead of stopping at the first duplicate, count ordered pairs within each equal-product group that differ in *every* slot of `S`; accumulate `D = 2304·Σ_{|S|=5}E_S + 48·Σ_{|S|=6}E_S + E_full`.

**Certificate schema (`RESULTS.json`):**

```json
{ "model": {"field_poly":[3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],"eta":[0,0,0,0,0,0,0,0,0,6],"beta":[2,1]},
  "key": "packed_product_only",
  "selfchecks": {"prime_field_identity_all_336": true, "eta16_equals_3": true,
                 "norm_is_homomorphism": true, "false_collapse_fails_at": {"t":1,"i":1,"a":0},
                 "single_slot_injective": true},
  "ladder": [{"k":1,"product_injective":true}, ... ,{"k":5,"product_injective":"<bool>"}],
  "max_good_k": "<int>", "min_collision_support_if_no_failure": "<max_good_k+1>",
  "first_collision": "null | {k,slots,keys_a,keys_b,value[16]}",
  "displacement_energy_E_S": "null | {\"[t1,..]\": <int>, ...}",
  "decision": "PRODUCT_ONLY_LADDER_PASSED_TO_KMAX | PARTIAL_COLLISION_FOUND" }
```

A PASS requires `key == "packed_product_only"`; any `(color,product)` key invalidates it. A `first_collision` is independently checkable by mapping each key `k→(i=k//16+1, a=k%16)` and re-evaluating `∏_{c∈S}(y_t−c)` and the Cycle 68 `slot_product`, which must agree.

## 5. Next exact lemma / construction

The decisive, exact schedule (using `L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION` + the dominance clarification):

1. **`k=5` rung — mandatory.** Verify all `C(7,5)=21` five-subsets product-injective (`E_S=0`). Any `E_S≥1` gives `D≥2304>155` and kills the `D≤155` route. Run via the norm-bucketed C kernel above.
2. **`k=6` rung.** Need `Σ_{|S|=6}E_S ≤ 3` (cleanest target 0; `48·4=192>155`).
3. **Full `k=7`.** With rungs 1–2 at 0, `D = E_full`; verify `E_full ≤ 155` by enumerating only the fully-displaced 7-slot equal-product pairs. This is the external-sort step every prior cycle deferred; the decomposition makes `E_full` the single remaining number.

The new structural lemma `L-CYCLE73-PRIME-FIELD-SLOT-POLYNOMIAL` is the construction that should accelerate all three: it lets the verifier evaluate 48 fixed `F_17`-polynomials at 7 scalars `y_t` (instead of degree-16 field polynomial bookkeeping) and gives an independent cross-check; `L-CYCLE73-SOUND-NORM-BUCKET` is what makes `k=5/6/7` fit in memory without the unsound color key.

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

Yes — in checkable rungs, not by pure thought. The route is: run the norm-bucketed compiled verifier to (a) certify `k=3,4,5` product-injective and (b) count `Σ_{|S|=6}E_S` and `E_full`, then conclude `D ≤ 155 ⇒ m_max ≤ 12 ⇒ Occ(β) > 2^32`. The next exact lemma to *prove or measure* is **`L-CYCLE73-SUPPORT-7-ENERGY-BOUND`: `E_full ≤ 155` (ideally `=0`) given `k≤6` injectivity**, which by the decomposition is equivalent to the model target `D ≤ 155`. The next construction is the norm-bucketed C kernel (§4) producing the certificate schema above. I could not execute it here (read-only `Read` tool), so I mark all code `UNRUN` and claim no rung beyond the banked `k≤2`. This stays strictly model-level, not a prize/MCA theorem.