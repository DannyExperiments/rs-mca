I'll start by reading the file index, then the core project files to understand the exact state of this problem.I'll read the core project state files and the banked certificates in parallel.Let me read the current-cycle source files: the Cycle 77 audit, the subset-injectivity check script and certificate, and the slot factorization checker that defines the model.Now let me read the model-defining scripts and the existing certificates in parallel.Now the critical file: the Cycle 68 checker that defines the field, eta, beta, and the slot value tables.I have the model and the banked structure. Let me read the remaining certificates and the AB max-fiber raw analysis, and check the runtime environment in parallel.I have the model and banked structure. Let me read the remaining key files: the Cycle 76 right-half script/certificate, the AB max-fiber raw response, and the route-board labels.## 1. Executive verdict and confidence

No full solve is possible *in this turn*, for a hard environmental reason: this harness exposes only a read tool. I cannot execute code, and I cannot write into `output_files`. So everything below that is code is marked **`UNRUN`**, and I make no proof claim from it (per your hard requirement).

That said: **yes, there is a clean route to a full solve**, and it is now a finite, *feasible* computation rather than an open theorem. The banked Cycle 75/76 injectivity facts collapse the seven-slot census into a two-factor multiplicative-incidence census whose exact cost is `|P_0| = 52,747,567,104` field multiplies with bounded memory (shardable to a few GB). That is a few CPU-hours single-core in C, minutes on a cluster. I give the exact reduction (proved), the run-ready exact-census code, and a cheaper guaranteed-feasible bankable rung.

Confidence:
- The reduction lemma (Section 2) is correct: **high**. It is elementary given the banked injectivity.
- That the provided census code, if run, decides `m_max ≤ 12` vs a 13-fold packet exactly: **high**.
- The value of `m_max` itself: **unknown**. Note the Cycle 68 `C6` "lower-bound probe" is vacuous — because `L` is injective every `p_left` bucket has count 1, so it only ever returns `lb = 1`. Nothing currently banks any nontrivial lower *or* upper bound below the Singleton `48`.

Classification of this deliverable: **`BANKABLE_LEMMA`** (the L·R incidence reduction) **+ run-ready census (UNRUN)**, not `PROOF`, not `COUNTERPACKET`.

## 2. The exact bankable lemma (this is the new content)

**L-CYCLE78-LR-INCIDENCE-REDUCTION.**
Write `L(k1,k2,k3) = u1·u2·u3` and `R(k4,k5,k6,k7) = u4·u5·u6·u7`, so `Phi(T) = L·R`. Banked: `L` is injective with `|L_img| = 110592` (Cycle 75) and `R` is injective with `|R_img| = 5308416` (Cycle 76). All `u`-values are nonzero, so `L_img, R_img ⊂ F^*`.

Then for every field value `v`,
```
m(v) = #{ T in P_0 : Phi(T) = v }
     = #{ l in L_img : v·l^{-1} in R_img  and  colorL(l) + colorR(v·l^{-1}) ≡ 4 (mod 16) },
```
and `m_max(beta) = max_v m(v)`.

*Proof.* `Phi(T)=v` means `L(k_{123})·R(k_{4567}) = v`. By injectivity of `L` and `R`, a tuple `T` is determined by the pair `(ℓ, r) = (L,R) ∈ L_img × R_img`, and conversely each such pair with `ℓr=v` is one tuple. Injectivity of `L` makes the left color sum `colorL` a well-defined function of `ℓ` (its unique preimage), likewise `colorR` of `r=v/ℓ`. The `P_0` filter `Σ_t color = 4` becomes `colorL(ℓ)+colorR(r) ≡ 4`. ∎

This is the precise object to census. Two consequences:

- **Equality is purely the packed product** `ℓr=v` (your hard requirement). Color is only the domain filter, never an equality key.
- **Legal shard key.** Any group homomorphism `χ: F^* → G` gives `χ(v)=χ(ℓ)χ(r)`, a function of the product — so sharding the count dictionary by `χ` is legal (it bounds memory, it never decides equality). I use `χ(x)=x^{(q-1)/256} ∈ μ_256` (valid: `17^16 ≡ 1 mod 256`), routed via per-slot `μ_256`-log tables so no per-tuple exponentiation is needed.

**What subset-injectivity alone can give (and why it stops at 48).** By the Cycle 77 fiber-as-code lemma, if all `≤6`-subset product maps are injective then every fiber has Hamming distance `≥7`; Singleton over alphabet 48, length 7, gives `m_max ≤ 48^{7-7+1} = 48`. That is bankable but cannot reach 12. The 3+4 split above is strictly stronger structure and is what makes the *exact* census cheap.

## 3. Feasibility

- **Naive census** (materialize all `48^7 = 5.87×10^11` products, sort): ~9.4 TB. Infeasible.
- **Reduced census via L·R** (Section 2): iterate only color-compatible pairs `= |P_0| = 5.27×10^10`; each pair is one 16×16 field multiply plus a dict bump. Shard the live dictionary by `χ_256` so each pair is emitted into exactly one shard pass (group `L` by `idx256(ℓ)`, `R` by `idx256(r)`; shard `s` pairs `L_a × R_{s-a}`). Live memory per shard ≈ `|P_0|/256 ≈ 2.1×10^8` keys (≈5 GB); use `256×9` shards (μ_9 is also available, `9 | 17^2−1`) for ≈0.6 GB. Total work stays `5.27×10^10`. **Single-core C ≈ a few hours; trivially parallel by shard.** Pure CPython is ~days, so the operator should run the C core, or PyPy.

## 4. Run-ready code (UNRUN — read-only harness, not executed here)

I could not write these into `output_files` (only a read tool is available); paste them in as `CHECKER.py` and `census_core.c`. `CHECKER.py` reuses the exact Cycle 68 model so results are directly comparable to the banked certificates.

```python
#!/usr/bin/env python3
# CYCLE78 exact m_max census + subset-injectivity ladder.   STATUS: UNRUN.
# Reduction: Phi = L(1,2,3)*R(4,5,6,7), both injective (Cycles 75,76).
#   m(v) = #{ l in L_img : v/l in R_img and colorL(l)+colorR(v/l) == 4 mod 16 }.
# Equality key = packed field product only. Color = domain filter only.
# chi(x)=x^{(q-1)/256} in mu_256 is a product-homomorphism => legal shard key.
import importlib.util, itertools, json, sys, random
from pathlib import Path
P=17; NDEG=16; Q=P**NDEG; QM1=Q-1
ONE=(1,)+(0,)*(NDEG-1)
C68=Path(__file__).resolve().parent/"cycle68_slot_factorization_checker.py"

def load68():
    s=importlib.util.spec_from_file_location("c68",C68)
    m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
def dense(v):
    o=[0]*NDEG
    for i,x in enumerate(v[:NDEG]): o[i]=x%P
    return tuple(o)
def fmul(a,b):                       # multiply mod X^16 + X^8 + 3
    t=[0]*31
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y: t[i+j]=(t[i+j]+x*y)%P
    for d in range(30,15,-1):
        c=t[d]%P
        if c:
            t[d-8]=(t[d-8]-c)%P; t[d-16]=(t[d-16]-3*c)%P   # X^d=-X^{d-8}-3X^{d-16}
    return tuple(t[:16])
def fpow(a,e):
    r=ONE; b=a
    while e>0:
        if e&1: r=fmul(r,b)
        b=fmul(b,b); e>>=1
    return r
def pack(v):
    k=0
    for c in reversed(v): k=k*P+c
    return k

def build_model():
    c=load68(); f=c.find_field_poly(); eta=c.find_eta(f); beta=c.find_beta(f)
    raw=c.build_u(f,eta,beta); tab={}
    for t in range(1,8):
        for k in range(48):
            i=k//16+1; a=k%16; tab[(t,k)]=dense(raw[(t,i,a)])
    S={1:15,2:9,3:12}
    col=[(S[k//16+1]+8*((k%16)&1))%16 for k in range(48)]
    return f,eta,beta,tab,col

def build_chi(tab):                  # per-slot mu_256 log tables
    e=QM1//256; rng=random.Random(1)
    while True:
        x=tuple(rng.randrange(P) for _ in range(NDEG))
        if any(x):
            z=fpow(x,e)
            if fpow(z,128)!=ONE: gen=z; break
    pm={}; cur=ONE
    for i in range(256): pm[pack(cur)]=i; cur=fmul(cur,gen)
    return {(t,k):pm[pack(fpow(tab[(t,k)],e))] for t in range(1,8) for k in range(48)}

def build_side(tab,col,idx,slots):   # returns dict packed_value->(val_tuple,color,idx256,keys); asserts injective
    out={}
    for keys in itertools.product(range(48),repeat=len(slots)):
        v=ONE; cc=0; ix=0
        for s,k in zip(slots,keys):
            v=fmul(v,tab[(s,k)]); cc=(cc+col[k])%16; ix=(ix+idx[(s,k)])%256
        pk=pack(v)
        if pk in out:
            print(json.dumps({"decision":"SUBSET_COLLISION_FOUND","slots":list(slots),
                "keys_a":list(out[pk][3]),"keys_b":list(keys),"value":pk})); sys.exit(0)
        out[pk]=(v,cc,ix,keys)
    return out

def census(L,R):
    Lg=[[] for _ in range(256)]; Rg=[[] for _ in range(256)]
    for pk,(v,cc,ix,kt) in L.items(): Lg[ix].append((v,cc,kt))
    for pk,(v,cc,ix,kt) in R.items(): Rg[ix].append((v,cc,kt))
    best=0; wit=None
    for s in range(256):             # one shard's products live at a time
        d={}
        for a in range(256):
            La=Lg[a]; Rb=Rg[(s-a)%256]
            if not La or not Rb: continue
            for (lv,lc,lkt) in La:
                need=(4-lc)%16
                for (rv,rc,rkt) in Rb:
                    if rc!=need: continue
                    key=pack(fmul(lv,rv))
                    lst=d.get(key)
                    if lst is None: d[key]=[(lkt,rkt)]
                    else:            lst.append((lkt,rkt))
        for key,lst in d.items():
            if len(lst)>best: best=len(lst); wit=(key,lst)
    return best,wit

def main():
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument("--ladder",type=int,default=0,help="check all r-subsets up to this size, then exit")
    ap.add_argument("--census",action="store_true",help="run exact m_max census")
    a=ap.parse_args()
    f,eta,beta,tab,col=build_model(); idx=build_chi(tab)
    if a.ladder:
        for sz in range(1,a.ladder+1):
            for slots in itertools.combinations(range(1,8),sz):
                build_side(tab,col,idx,slots)   # exits on first collision
        print(json.dumps({"decision":f"ALL_SUBSETS_UP_TO_{a.ladder}_PRODUCT_INJECTIVE",
            "fiber_min_distance_lower_bound":a.ladder+1,
            "singleton_mmax_upper_bound": 48**(7-(a.ladder+1)+1) if a.ladder>=6 else None,
            "note":"distance>=7 (ladder 6) gives m_max<=48; not <=12"})); return
    if a.census:
        L=build_side(tab,col,idx,(1,2,3)); R=build_side(tab,col,idx,(4,5,6,7))
        best,(val,lst)=(*census(L,R),)
        dec="THIRTEEN_FOLD_PACKET" if best>=13 else "MMAX_CERTIFIED_LE_12" if best<=12 else "MMAX_EXACT"
        print(json.dumps({"decision":dec,"m_max":best,
            "P0":52747567104,"key":"packed_product_only",
            "witness":{"value":val,"members":[{"left":list(l),"right":list(r)} for l,r in lst]}
                      if best>=13 else None}, indent=2))
if __name__=="__main__": main()
```

C hot path for the census (port of `census`); identical model, packed-product equality:

```c
/* census_core.c  STATUS: UNRUN.  Build: cc -O3 census_core.c -o census
 * Reads two binary tables produced by a small dumper from CHECKER.build_side:
 *   L: 110592 records, R: 5308416 records, each = {uint8 coef[16]; uint8 color; uint8 idx256;}
 * Multiplies mod X^16+X^8+3, color-filters (cL+cR==4 mod16), shards by (idxL+idxR)&255,
 * tracks max multiplicity. Use an open-addressing uint128->count map per shard. */
#include <stdint.h>
#include <string.h>
static inline void fmul(const uint8_t*a,const uint8_t*b,uint8_t*o){
    int t[31]; memset(t,0,sizeof t);
    for(int i=0;i<16;i++) if(a[i]) for(int j=0;j<16;j++) if(b[j]) t[i+j]+=a[i]*b[j];
    for(int d=0;d<31;d++) t[d]%=17;
    for(int d=30;d>=16;d--){ int c=t[d]%17; if(c){ t[d-8]=((t[d-8]-c)%17+17)%17;
        t[d-16]=((t[d-16]-3*c)%17+17)%17; } }
    for(int i=0;i<16;i++) o[i]=(uint8_t)(((t[i]%17)+17)%17);
}
/* pack 16 base-17 digits into __int128 key; insert into per-shard hashmap; keep max.
 * Group L by idx256 (256 buckets) and R by idx256; for shard s iterate a=0..255,
 * pair L[a] x R[(s-a)&255] with color filter; build map for shard s only, then free.
 * On count>=13, dump all (left,right) record indices for that key as the packet. */
```

## 5. Certificate schema (PENDING — would be emitted by a real run)

```json
{
  "decision": "MMAX_CERTIFIED_LE_12 | THIRTEEN_FOLD_PACKET | SUBSET_COLLISION_FOUND | UNRESOLVED_PENDING_RUN",
  "m_max": null,
  "P0": 52747567104,
  "key": "packed_product_only",
  "subset_results": "ladder mode: ALL_SUBSETS_UP_TO_k_PRODUCT_INJECTIVE",
  "witness": null
}
```
Current state in this turn: `"decision":"UNRESOLVED_PENDING_RUN"`, `"m_max":null` — code is `UNRUN`.

## 6. What remains open

- The actual value of `m_max(beta)`. Nothing below Singleton's `48` is banked; the only "probe" in repo (`C6`) is vacuous under `L`-injectivity. So `≤12` is unproven and `≥13` is unwitnessed.
- Whether the cheap ladder route (all `≤6`-subsets injective ⇒ `m_max ≤ 48`) even completes — that is feasible to bank now (`--ladder 6`) but it strictly cannot reach `12`.
- An *analytic* `≤12` (no full census) would require bounding the common-ratio object `Ratios(L) ∩ Ratios(R)`; computing that is itself census-scale, so the product census is the shortest path.

## 7. Next exact lemma / construction

Primary, decisive: **run the Section-4 exact census** (`census_core.c`, sharded by `χ_256·χ_9`). It returns either `m_max ≤ 12` (PROOF) or an explicit 13-fold packet with all seven slot keys per member and the packed `v` (COUNTERPACKET). This is the full solve; it is gated only on compute, which this harness denies.

Cheap bankable rung to stage first: **`CHECKER.py --ladder 6`** (all 1–6-subsets; 7 size-6 subsets at `48^6` each is minutes in C). If clean, it banks `L-CYCLE78-FIBER-DISTANCE-GE-7 ⇒ m_max ≤ 48` — a real new wall narrower than "≤48 from pairs only," and it validates the model end-to-end before the big run.

Next exact theorem target if a census-free proof is wanted: **L-CYCLE78-COMMON-RATIO-BOUND** — show every `Δ ⊆ Ratios(L) ∩ Ratios(R)` that is "coherent" (`∃ ℓ_1∈L_img, r_1∈R_img` with `ℓ_1δ^{-1}∈L_img` and `r_1δ∈R_img` for all `δ∈Δ`) has `|Δ| ≤ 11`. A size-`m` fiber yields exactly such a `Δ` of size `m`, so this would give `m_max ≤ 12` directly and is the sharpest finite object beyond the census.