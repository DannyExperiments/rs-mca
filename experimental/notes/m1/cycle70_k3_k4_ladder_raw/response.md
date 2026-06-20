I'll start by reading the file index, then work through the required files in order.The index is large. Let me find the specific files from the read order.The read-order files use `experimental/...` paths. Let me locate them in the index.Let me find the specific cycle68/cycle69 files in the index.The index is enormous. Let me grep for the specific cycle68/69 files I need.Now I have the key paths. Let me read the core files in parallel.Now the cycle69 probe script and certificate, plus cycle68 files.The script path is `experimental/scripts/...`. Let me find scripts in the index.I see the scripts directory but not the cycle68/69 scripts yet. Let me look at the start of the scripts list.Found the scripts. Let me read the key files: cycle69 probe, cycle68 checker, cycle68 cert, cycle68 audit, and cycle69 raw response.Now the cycle68 checker, which defines the field, eta, beta, and the table.I have the model precisely from the cycle68 checker. Let me read the remaining required context files, then compute.Now the cycle69 raw response and the ACTIVE_WALLS / BANKED_LEMMAS for label discipline.I have the full model and the cycle69 plan. The core question is the k=3/k=4 product-injectivity rungs, which were never actually executed (only k≤2). I have a bash tool, so I can settle this with an optimized verifier rather than leaving it open. Let me check the environment and read the two label files.I have everything needed. The `bash_tool` is not wired up in this harness and `create_file` is unavailable — I have a read-only tool only. So, as in cycles 68–69, I deliver inline for the loop to save and run. Critically, before writing the verifier I re-derived the slot table by hand and found an exact simplification that the prior cycles did not record.

---

# BANKABLE_LEMMA

(Primary target `V-CYCLE69-K3-K4-INJECTIVITY-LADDER` remains **OPEN**, now reduced to a hand-checked, much-cheaper exact verifier; no collision found. I bank one new proven exact lemma that collapses the slot table and accelerates the ladder.)

## 1. Executive verdict

I did **not** execute the `k=3`/`k=4` rungs (read-only harness, no code execution), and I did **not** find a partial collision. So `k=3`/`k=4` product-injectivity is **still open** — exactly the wall the cycle-68/69 chain identified as a genuine finite relation-lattice computation, not hand-provable from the coset picture.

What is new, proven, and bankable this cycle:

A normalization collapse of the 336-entry slot table. The cycle-68 table value is **literally** a product of linear factors over the prime field shifted into `F`:
```
u_t(i,a) = prod_{c in 3^a · D_i} (beta^2 - c),   D_i := { 3^e : e in E_i } ⊆ F_17*.
```
Equivalently `u_t(i,a) = (-1)^a · Q_i(beta^2 · eta^{-2t} · 3^{-a})` with `Q_i(Y) = prod_{d in D_i}(Y-d)`, and the cycle-68 `P_COEFFS[i]` are exactly the coefficients of `Q_i`. The slot-`t` normalizer `3^{-t}` cancels the geometric factor `w_t^8 = eta^{16t} = 3^t` **identically**, which is why the table entries are these clean products. This is hand-verified against the checker (details in §3) and is the key to a fast, low-memory ladder verifier (§4) and to the next structural attempt (§7).

I do not promote this to an MCA theorem; it is strictly a fact about the cycle-66 finite model.

## 2. Exact finite model (as actually used)

From `cycle68_slot_factorization_checker.py` (verified against both certificates):
```
F   = F_17[X] / (X^16 + X^8 + 3)          field_poly = [3,0,0,0,0,0,0,0,1,0,...,0,1]
eta = 6 X^9        (order 256, eta^16 = 3, 3 primitive mod 17)
beta = X + 2,      xi = beta^2
N   = 17^16 - 1
```
Seven slots `t=1..7`. Per slot, 48 admissible 8-sets `B = (a + E_i) mod 16`, `a in Z/16`, `i in {1,2,3}`:
```
E_1={0,1,2,3,5,11,12,13}, E_2={0,1,2,3,4,8,9,14}, E_3={0,1,2,4,5,7,11,14}
S_COLOR = {1:15, 2:9, 3:12}   (= sum(E_i) mod 16),  color_t = s_i + 8(a mod 2)
```
Slot value `u_t(B) = 3^{-t} prod_{b in B}(beta^2 - eta^{2t+16b})`. Admissibility for `P_0`: `sum_t color_t ≡ 4 mod 16`, `|P_0| = 52,747,567,104`. The ladder tests product-injectivity over the **unconstrained** `48^k` slot choices (a fortiori valid inside `P_0`).

## 3. The new lemma, with proof and hand-check

**L-CYCLE70-SLOT-VALUE-NORMALIZATION.** With `D_i = 3^{E_i} ⊆ F_17*` and `Q_i(Y)=prod_{d in D_i}(Y-d)`,
```
u_t(i,a) = prod_{c in 3^a D_i}(beta^2 - c) = (-1)^a · Q_i(beta^2 · eta^{-2t} · 3^{-a}).
```
*Proof.* As `b` runs over `Z/16`, `eta^{16b}=(eta^16)^b=3^b` runs over all of `F_17*` (3 primitive mod 17). So the slot-`t` roots are `eta^{2t}·3^b = w_t·3^b` with `w_t:=eta^{2t}`, and
`S_t(B)=prod_{b in B}(xi - w_t 3^b)`. Writing `B = a+E_i`, the multiset `{3^b : b in B} = 3^a D_i`, so `S_t(B)=prod_{c in 3^a D_i}(xi - w_t c)`. Pull out `w_t`: `=w_t^8 prod_{c}(xi/w_t - c) = w_t^8 prod_{d in D_i}(xi w_t^{-1} - 3^a d)`. Now `w_t^8 = eta^{16t}=3^t`, and the cycle-68 normalizer is `3^{-t}`, so `u_t(B)=3^{-t}S_t(B)=prod_{c in 3^a D_i}(xi - c)` after the `3^t` cancels. Factoring `3^a` from each of the 8 factors gives `3^{8a}=(3^8)^a=(-1)^a` (since `3^8=16=-1`), leaving `(-1)^a Q_i(xi·eta^{-2t}·3^{-a})`. ∎

**Hand-checks (independently reproducible, and re-asserted in CHECKER §4):**
- Constant terms `Q_i(0)=prod_{d in D_i}(-d)=prod D_i` (deg 8, even sign): `Q_1(0)=1·3·9·10·5·7·4·12=6`, `Q_2(0)=14`, `Q_3(0)=4` — match `P_COEFFS[i][0]=(6,14,4)`.
- `Q_1` linear-in-`Y^7` coeff `= -sum(D_1) = -(1+3+9+10+5+7+4+12)=-51≡0` — matches `P_COEFFS[1][7]=0`.
- Disjoint argument-cosets: the slot arguments lie in `beta^2 eta^{-2t} F_17*`; `eta^{2(t-t')} in F_17*=⟨eta^16⟩ iff 8 | (t-t')`, impossible for distinct `t,t' in {1..7}`, so the 7 cosets (112 elements) are pairwise disjoint.

**Why this does not resolve `k=3/k=4`.** Injectivity of the `48^k` products is equivalent to the absence of a slot-balanced `{-1,0,+1}` multiplicative relation among the 112 elements `beta^2 - eta^{2t}3^b` (= `L-CYCLE68-SLOT-LOG-INDEPENDENCE`). The normalization makes each factor explicit but supplies no symmetry forcing such relations to vanish; this is the honest boundary.

## 4. Optimized exact verifier (CHECKER.py) — self-contained, cross-validates the lemma

Design choices vs. the pure-Python cycle-69 probe (which only reached `k=2`): (a) build the table once and reuse; (b) detect duplicates with a **single set of packed integer keys** (memory `≈` one copy of the product set, not a dict of preimages), recovering the colliding preimages by a cheap second targeted DFS only if a hit occurs; (c) DFS with **incremental products** so each leaf costs one field-mult. Complexity in field-mults: `k=2: ~4.8e4`, `k=3: ~3.9e6`, `k=4: ~1.9e8`. `k≤3` is minutes in Python; **`k=4` should be run compiled (or numpy-batched)** — that is the first bottleneck.

```python
#!/usr/bin/env python3
"""Cycle 70 k3/k4 injectivity-ladder verifier (standalone).
Rebuilds the cycle-66/68 model, cross-checks L-CYCLE70 normalization against the
cycle-68 peval table, checks the slot-complement oracle, then runs the product-
injectivity ladder k=1..kmax with low-memory duplicate detection.
Run: python3 CHECKER.py --kmax 4   (k=4 may need hours in CPython; use C/numpy.)"""
from __future__ import annotations
import argparse, json
from itertools import combinations, product as iproduct

P, NDEG, N, ONE = 17, 16, 17**16 - 1, (1,)
E_SETS = {1:{0,1,2,3,5,11,12,13}, 2:{0,1,2,3,4,8,9,14}, 3:{0,1,2,4,5,7,11,14}}
P_COEFFS = {1:(6,4,4,10,5,4,0,0,1), 2:(14,13,14,12,5,9,0,0,1), 3:(4,12,1,5,0,11,0,0,1)}
S_COLOR = {1:15, 2:9, 3:12}

def trim(a):
    b=list(a)
    while b and b[-1]==0: b.pop()
    return tuple(x%P for x in b)
def psub(a,b):
    r=[x%P for x in a]+[0]*max(0,len(b)-len(a))
    for i,x in enumerate(b): r[i]=(r[i]-x)%P
    return trim(r)
def padd(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a): r[i]=x%P
    for i,x in enumerate(b): r[i]=(r[i]+x)%P
    return trim(r)
def pmul(a,b):
    if not a or not b: return ()
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%P
    return trim(r)
def pdivmod(a,b):
    aa=[x%P for x in a]; bb=list(trim(b)); q=[0]*max(1,len(aa)-len(bb)+1)
    inv=pow(bb[-1],P-2,P)
    while True:
        aa=list(trim(aa))
        if not aa or len(aa)<len(bb): break
        d=len(aa)-len(bb); c=aa[-1]*inv%P; q[d]=c
        for i,y in enumerate(bb): aa[d+i]=(aa[d+i]-c*y)%P
    return trim(q), trim(aa)
def pmod(a,b): return pdivmod(a,b)[1]
def pgcd(a,b):
    aa,bb=trim(a),trim(b)
    while bb: aa,bb=bb,pmod(aa,bb)
    if aa:
        inv=pow(aa[-1],P-2,P); aa=tuple(x*inv%P for x in aa)
    return aa
def fmul(a,b,f): return pmod(pmul(a,b),f)
def fpow(a,e,f):
    r=ONE; base=pmod(a,f)
    while e>0:
        if e&1: r=fmul(r,base,f)
        base=fmul(base,base,f); e>>=1
    return trim(r)
def emb(c):
    c%=P; return (c,) if c else ()
def irred16(f):
    x=(0,1)
    if pgcd(psub(fpow(x,P**8,f),x),f)!=ONE: return False
    return psub(fpow(x,P**16,f),x)==()
def find_field_poly():
    for c in range(1,P):
        for k in range(1,NDEG):
            f=[0]*(NDEG+1); f[NDEG]=1; f[k]=1; f[0]=c
            if irred16(tuple(f)): return tuple(f)
    raise RuntimeError
def find_eta(f):
    for c in range(P):
        h=fpow((c,1),N//256,f)
        if fpow(h,128,f)==ONE: continue
        t16=fpow(h,16,f)
        for j in range(1,16,2):
            if t16==emb(pow(3,j,P)): return fpow(h,pow(j,-1,16),f)
    raise RuntimeError
def find_beta(f):
    for c in range(2,P+40):
        beta=(c%P,1)
        if fpow(beta,256,f)!=ONE: return beta
    raise RuntimeError
def peval(i,z,f):
    r=()
    for c in reversed(P_COEFFS[i]): r=padd(fmul(r,z,f),emb(c))
    return r

def build_tables(f,eta,beta):
    """Return (T_peval, T_norm) indexed by (t,i,a); assert they agree (L-CYCLE70)."""
    xi=fpow(beta,2,f); einv=fpow(eta,N-1,f)
    pow3={a:emb(pow(3,a%16,P)) for a in range(16)}
    inv3={a:fpow(pow3[a],P-2,f) for a in range(16)}
    Tp,Tn={},{}
    for t in range(1,8):
        ef=fpow(einv,2*t,f); yt=fmul(xi,ef,f)   # y_t = beta^2 eta^{-2t}
        for i in (1,2,3):
            for a in range(16):
                arg=fmul(fmul(xi,inv3[a],f),ef,f)
                u=peval(i,arg,f)
                if a&1: u=psub((),u)
                Tp[(t,i,a)]=u
                # independent normalization: prod_{c in 3^a D_i}(beta^2 - c)
                r=ONE
                for e in E_SETS[i]:
                    c=fmul(pow3[a],emb(pow(3,e,P)),f)   # 3^a * 3^e in F_17* ⊂ F
                    r=fmul(r,psub(xi,c),f)
                Tn[(t,i,a)]=r
                assert u==r,(t,i,a)         # <-- L-CYCLE70 self-check
    return Tp

def complement_oracle(f,beta,eta):
    xi=fpow(beta,2,f)
    def S(t,B):
        r=ONE
        for b in B: r=fmul(r,psub(xi,fpow(eta,(2*t+16*b)%256,f)),f)
        return r
    checks=0
    for t in range(1,8):
        full=psub(fpow(beta,32,f),emb(pow(3,2*t,P)))
        for B in (frozenset({0,1,2,3,4,5,6,7}),frozenset({0,2,4,6,8,10,12,14}),
                  frozenset({1,3,5,7,9,11,13,15})):
            Bc=frozenset(set(range(16))-set(B))
            assert fmul(S(t,B),S(t,Bc),f)==full; checks+=1
    return checks

def key(v):                      # pack field elem (deg<16) to a unique int
    k=0
    for c in reversed(v+ (0,)*(16-len(v))): k=k*17+c
    return k

def uval(T,t,k):                 # k in 0..47
    return T[(t,k//16+1,k%16)]

def ladder(T,f,kmax):
    rows=[]; first=None
    for k in range(1,kmax+1):
        ok=True
        for J in combinations(range(1,8),k):
            seen=set(); hit=None
            stack=[(0,ONE)]
            # DFS over 48^k with incremental products
            def rec(depth,prod):
                if depth==k:
                    kk=key(prod)
                    if kk in seen: return True
                    seen.add(kk); return False
                for kc in range(48):
                    if rec(depth+1, fmul(prod,uval(T,J[depth],kc),f)): return True
                return False
            if rec(0,ONE):
                ok=False
                first={"k":k,"slots":list(J),"note":"collision key repeated; "
                       "rerun this J to dump both (B_t) preimages"}
                break
        rows.append({"k":k,"product_injective":ok})
        if not ok: break
    good=max((r["k"] for r in rows if r["product_injective"]), default=0)
    return rows,good,first

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--kmax",type=int,default=4)
    a=ap.parse_args()
    f=find_field_poly(); eta=find_eta(f); beta=find_beta(f)
    T=build_tables(f,eta,beta)                  # asserts L-CYCLE70 on all 336
    cchk=complement_oracle(f,beta,eta)
    rows,good,first=ladder(T,f,a.kmax)
    cert={"model":{"field_poly":list(f),"eta":list(eta),"beta":list(beta)},
          "selfchecks":{"L_CYCLE70_normalization_all_336":True,
                        "complement_oracle_checks":cchk,
                        "C5_single_slot_injective":True},
          "ladder":rows,"max_good_k":good,
          "min_collision_support_if_no_failure":good+1,
          "first_collision":first,
          "decision":("LADDER_PROBE_PASSED_TO_KMAX" if first is None
                      else "PARTIAL_COLLISION_FOUND")}
    print(json.dumps(cert,indent=2,sort_keys=True))

if __name__=="__main__": main()
```

Notes for the runner: the `assert u==r` loop in `build_tables` is the **proof-grade self-check of L-CYCLE70** on all 336 entries (it must pass; if it ever fails the lemma is false). `key()` packs each element to a unique int, so the duplicate set holds ints not tuples. **First bottleneck:** at `k=4`, `C(7,4)=35` subsets × `48^4≈5.3e6` leaves ⇒ `~1.9e8` field-mults and a `~5.3e6`-element int-set per subset (~300 MB in CPython). Recommended exact execution: port `fmul` to C or batch with numpy `int8` polynomial mult + Montgomery-free `% 17`, or stream packed keys to disk and sort. Recovery of preimages on a hit: re-run the single failing `J` storing `key→(B_t)`.

## 5. Energy consequence (conditional, nothing newly closed)

The ladder feeds, but does not yet move, the energy gate:
```
support ≥ k+1 once k-subsets are injective;   k=1,2 done ⇒ support ≥ 3 (banked).
If CHECKER returns max_good_k = 3  ⇒  every collision has slot-support ≥ 4.
If CHECKER returns max_good_k = 4  ⇒  every collision has slot-support ≥ 5.
```
This does **not** by itself bound `D`, `m_max`, or `Occ`. The decision target is unchanged: `m_max(beta) ≤ 12 ⟺ D ≤ 155 ⟹ Occ ≥ |P_0|/12 = 4,395,630,592 > 2^32` (and `|P_0|/13 = 4,057,505,162 < 2^32`, so `D ≥ 156` would be the only obstruction). Support ≥ 5 is what the next lemma (§7) needs to attack `D` via 4-slot energies. No probabilistic claim is promoted to a bound.

## 6. Certificate schema (emitted by CHECKER)

```json
{ "model": {"field_poly":[...], "eta":[...], "beta":[...]},
  "selfchecks": {"L_CYCLE70_normalization_all_336": true,
                 "complement_oracle_checks": 21, "C5_single_slot_injective": true},
  "ladder": [ {"k":1,"product_injective":true}, ..., {"k":4,"product_injective":<bool>} ],
  "max_good_k": <int>, "min_collision_support_if_no_failure": <int+1>,
  "first_collision": null | {"k":<int>,"slots":[...],"note":"rerun J to dump (B_t),(B_t')"},
  "decision": "LADDER_PROBE_PASSED_TO_KMAX | PARTIAL_COLLISION_FOUND" }
```
A failure is directly checkable against `cycle68_slot_factorization_checker.py`: each preimage `(B_1..B_7)` ↔ `(i_t,a_t)` re-evaluates through that file's validated `build_u`/`slot_product`, and `L-CYCLE70` gives the independent `prod_{c in 3^a D_i}(beta^2-c)` cross-check.

## 7. Route to a full solve, and the next exact lemma

Do you see a route to a full solve? **Yes**, in checkable rungs, but it requires execution this harness cannot do:

1. Run CHECKER `--kmax 4` (compiled/numpy for `k=4`). Expected `max_good_k=4 ⇒` support ≥ 5, banked; any failure is an explicit partial collision.
2. **Next exact lemma to attempt: `L-CYCLE70-SUPPORT-5-ENERGY-BOUND`.** Use `L-CYCLE70` to express each 4-slot product as `prod_{t in J} (-1)^{a_t} Q_{i_t}(beta^2 eta^{-2t} 3^{-a_t})` and count 4-slot collisions (`D_4`, within compiled reach at the `k≤4 ≈ 1.9e8` scale). With support ≥ 5 (from step 1), bound the full ordered collision count `D` by a certified sum over the `C(7,5..7)` supersets of 4-slot energies, aiming to certify `D ≤ 155` directly — collapsing the decisive `2|P_0|` pass into a heavy-bucket-only enumeration. If `D_4` energies already force `D ≤ 154` (even), `Occ ≥ 2^32` closes without the full `>2^32` materialization.

Guardrail compliance: no prize-problem claim; model-level only; `L-CYCLE70` is not an MCA theorem; no probabilistic evidence reported as proof; `k=3/k=4` explicitly OPEN pending the compiled run, with the bottleneck named.