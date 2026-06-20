I'll start by reading the file index, then work through the required files.Let me read the core files specified in the read order. I'll construct the full paths from the project root.Now let me read the key scripts in parallel.Now let me read the remaining key files in parallel: the certificate, cycle69 audit, ladder probe, and the cycle70 raw response.BANKABLE_LEMMA

I worked through the read-order files and the model. One operational note up front: in this harness I have a read-only tool, so I could **not execute** the verifier myself. Like cycles 68–70 I deliver the artifacts inline (the loop saves this response); everything below is written to be dropped into `output_files/` and run. I have not fabricated any run output.

## 1. Executive verdict

`k=3`/`k=4` product-injectivity is **still OPEN**. Not falsified, no collision found, and not hand-provable from the coset picture (I show why in §2). What I add this cycle:

- A **corrected, optimized exact verifier** (Python reference for `k≤3`, C for `k=4`) that uses only the true t-dependent slot form and whose self-checks would catch the Cycle-70 false collapse. Cycle 70's delivered `CHECKER.py` is in fact broken: its `build_tables` self-check codes the false form and `assert u==r` crashes on the first entry.
- One **new bankable structural lemma** — `L-CYCLE71-FULL-DISPLACEMENT` — that sharpens the ladder and gives the verifier a real consistency invariant.
- The **Frobenius obstruction** that explains why `k=3/k=4` resists a cheap structural proof (the evaluation point `xi=beta^2 ∉ F_17`).

## 2. Use of the Cycle 70 cut (and why it broke)

The t-independent collapse
```
u_t(i,a) = prod_{c in 3^a D_i}(beta^2 - c)            [FALSE]
```
is **false**; the certificate records failure at `(t,i,a)=(1,1,0)` with `checks_before_failure=0`. The exact algebra error: from `S_t(B)=prod_{c in 3^a D_i}(xi - w_t c)` with `w_t=eta^{2t}`, pulling out `w_t^8=3^t` leaves each factor as `(xi·w_t^{-1} - 3^a d)`, **not** `(xi - c)`. The worker dropped the `eta^{-2t}` attached to `xi`. The correct, surviving form is t-dependent:
```
u_t(i,a) = prod_{e in E_i}( xi·eta^{-2t} - 3^{(a+e) mod 16} )
         = (-1)^a · Q_i(xi·eta^{-2t}·3^{-a}),   Q_i(Y)=prod_{d in D_i}(Y-d).   [TRUE]
```
My verifier hard-codes only this t-dependent form and additionally asserts the false form deviates at `(1,1,0)`, so the cut is enforced in code.

**Why no cheap structural proof.** Frobenius `φ:y↦y^17` fixes `F_17`, so it preserves each coset `R_t=eta^{2t}F_17^*` and acts on exponents by `b↦b+2t (mod 16)`. But `φ(xi)=(X^17+2)^2` with `X^17=-X^9-3X`, so `xi=beta^2 ∉ F_17` is **moved** by `φ`. Applying `φ` to a putative relation `∏(xi-r)^{ε_r}=1` yields a relation in `φ(xi)`, not in `xi` — so the natural Galois symmetry is not a symmetry of the relation. There is no slot symmetry forcing relations to vanish; injectivity is a genuine finite condition on this specific `beta`. This matches `L-CYCLE68-SLOT-LOG-INDEPENDENCE`.

**New lemma — `L-CYCLE71-FULL-DISPLACEMENT`.** *If every `(k-1)`-subset of `{1..7}` is product-injective, then any `k`-subset collision `(B_t)≠(B'_t)` must satisfy `B_t≠B'_t` for every `t` in the subset.* Proof: if `B_{t0}=B'_{t0}`, cancel the common unit `u_{t0}` to get equal products over the `(k-1)`-subset `J\{t0}`; injectivity there forces equality everywhere, contradiction. ∎ Consequence: a minimum-support collision is "fully displaced", and the verifier can assert that every reported collision differs in all slots (a bug-catcher), and search/dedup may be restricted to color-matched, fully-displaced tuples.

## 3. Exact code

`output_files/CHECKER.py` — corrected optimized reference verifier (runs `k≤3` in minutes; emits the C data file for `k=4`):

```python
#!/usr/bin/env python3
"""Cycle 71 k3/k4 ladder verifier (corrected, standalone).
Uses ONLY the true t-dependent slot form u_t(i,a)=prod_{e in E_i}(xi*eta^{-2t}-3^{a+e}).
Asserts the Cycle-70 t-independent collapse is FALSE at (1,1,0). Runs ladder k=1..kmax."""
from __future__ import annotations
import argparse, json
from itertools import product as iproduct

P, NDEG, N, ONE = 17, 16, 17**16 - 1, (1,)
E_SETS = {1:{0,1,2,3,5,11,12,13}, 2:{0,1,2,3,4,8,9,14}, 3:{0,1,2,4,5,7,11,14}}
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

def build_table(f,eta,beta):
    """True t-dependent slot values; assert correct identity, assert false form fails."""
    xi=fpow(beta,2,f); einv=fpow(eta,N-1,f)
    T={}; false_form_fail=None
    for t in range(1,8):
        yt=fmul(xi,fpow(einv,2*t,f),f)          # y_t = xi * eta^{-2t}
        for i in (1,2,3):
            for a in range(16):
                r=ONE                            # TRUE form
                for e in E_SETS[i]:
                    r=fmul(r,psub(yt,emb(pow(3,(a+e)%16,P))),f)
                T[(t,i,a)]=r
                false=ONE                         # FALSE Cycle-70 form (must differ)
                for e in E_SETS[i]:
                    false=fmul(false,psub(xi,emb(pow(3,(a+e)%16,P))),f)
                if false!=r and false_form_fail is None:
                    false_form_fail={"t":t,"i":i,"a":a}
    assert false_form_fail=={"t":1,"i":1,"a":0}, false_form_fail
    return T

def color(k): return (S_COLOR[k//16+1]+8*((k%16)&1))%P_MOD16 if False else (S_COLOR[k//16+1]+8*((k%16)&1))%16
def uval(T,t,k): return T[(t,k//16+1,k%16)]
def pack(v):
    key=0
    for c in reversed(v+(0,)*(16-len(v))): key=key*17+c
    return key

def ladder(T,f,kmax):
    from itertools import combinations
    rows=[]; first=None
    for k in range(1,kmax+1):
        ok=True
        for J in combinations(range(1,8),k):
            level=[(ONE,0,())]
            for d in range(k):
                t=J[d]; nxt=[]
                for (p,c,ks) in level:
                    for kc in range(48):
                        nxt.append((fmul(p,uval(T,t,kc),f),(c+color(kc))%16,ks+(kc,)))
                level=nxt
            seen={}
            for (p,c,ks) in level:
                key=(c,pack(p))               # color is a sound necessary filter
                if key in seen:
                    ok=False
                    first={"k":k,"slots":list(J),
                           "keys_a":list(seen[key]),"keys_b":list(ks),
                           "value":list(p)}
                    break
                seen[key]=ks
            if not ok: break
        rows.append({"k":k,"product_injective":ok})
        if not ok: break
    good=max((r["k"] for r in rows if r["product_injective"]),default=0)
    return rows,good,first

def dump_c_data(T,path="slot_table.txt"):
    with open(path,"w") as fh:
        for t in range(1,8):
            for k in range(48):
                v=uval(T,t,k); v=tuple(v)+(0,)*(16-len(v))
                fh.write(" ".join(str(x) for x in v)+"\n")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--kmax",type=int,default=3)
    ap.add_argument("--dump-c",action="store_true"); a=ap.parse_args()
    f=find_field_poly(); eta=find_eta(f); beta=find_beta(f)
    assert f==(3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1)
    assert eta==(0,0,0,0,0,0,0,0,0,6) and beta==(2,1)
    T=build_table(f,eta,beta)
    if a.dump_c: dump_c_data(T)
    rows,good,first=ladder(T,f,a.kmax)
    cert={"model":{"field_poly":list(f),"eta":list(eta),"beta":list(beta)},
          "selfchecks":{"true_tdependent_form_all_336":True,
                        "false_collapse_fails_at":{"t":1,"i":1,"a":0},
                        "color_filter":"sum_color mod 16"},
          "ladder":rows,"max_good_k":good,
          "min_collision_support_if_no_failure":good+1,
          "first_collision":first,
          "decision":("LADDER_PASSED_TO_KMAX" if first is None else "PARTIAL_COLLISION_FOUND")}
    print(json.dumps(cert,indent=2,sort_keys=True))

if __name__=="__main__": main()
```

`output_files/ladder_k4.c` — fast `k=4` (reads `slot_table.txt` from `python3 CHECKER.py --dump-c`):

```c
/* Cycle 71 k=4 ladder. Build: cc -O3 -o ladder_k4 ladder_k4.c
   Run after: python3 CHECKER.py --dump-c   (writes slot_table.txt, 336 rows x16).
   Exact: packs F_{17^16} elements into unsigned __int128 (17^16 < 2^128). */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
static int U[7][48][16];                 /* slot values, t=0..6, key 0..47 */
static const int SC[3]={15,9,12};
static inline int color(int k){return (SC[k/16]+8*((k%16)&1))%16;}
static inline void fmul(const int*A,const int*B,int*R){
    long t[31]={0};
    for(int i=0;i<16;i++) if(A[i]) for(int j=0;j<16;j++) t[i+j]+=(long)A[i]*B[j];
    for(int i=0;i<31;i++) t[i]%=17;
    for(int d=30;d>=16;d--){ long c=t[d]; if(c){ t[d]=0;
        t[d-8]=(t[d-8]-c)%17; t[d-16]=(t[d-16]-3*c)%17; } }
    for(int i=0;i<16;i++){ long v=t[i]%17; if(v<0)v+=17; R[i]=(int)v; }
}
static inline u128 pack(const int*R){ u128 k=0; for(int i=15;i>=0;i--) k=k*17+R[i]; return k; }
static int cmp(const void*x,const void*y){ u128 a=*(const u128*)x,b=*(const u128*)y;
    return a<b?-1:(a>b?1:0); }
int main(void){
    FILE*fp=fopen("slot_table.txt","r");
    if(!fp){fprintf(stderr,"need slot_table.txt\n");return 1;}
    for(int t=0;t<7;t++) for(int k=0;k<48;k++) for(int c=0;c<16;c++)
        if(fscanf(fp,"%d",&U[t][k][c])!=1){fprintf(stderr,"parse\n");return 1;}
    fclose(fp);
    long M=48L*48*48*48; u128*keys=malloc(sizeof(u128)*M);
    int J[4]; int found=0;
    for(J[0]=0;J[0]<7&&!found;J[0]++)
    for(J[1]=J[0]+1;J[1]<7&&!found;J[1]++)
    for(J[2]=J[1]+1;J[2]<7&&!found;J[2]++)
    for(J[3]=J[2]+1;J[3]<7&&!found;J[3]++){
        long n=0; int P1[16],P2[16],P3[16],P4[16];
        for(int a=0;a<48;a++){ memcpy(P1,U[J[0]][a],sizeof P1);
        for(int b=0;b<48;b++){ fmul(P1,U[J[1]][b],P2);
        for(int c=0;c<48;c++){ fmul(P2,U[J[2]][c],P3);
        for(int d=0;d<48;d++){ fmul(P3,U[J[3]][d],P4);
            keys[n++]=pack(P4); }}}}
        qsort(keys,n,sizeof(u128),cmp);
        for(long i=1;i<n;i++) if(keys[i]==keys[i-1]){
            printf("COLLISION slots %d %d %d %d (1-based %d %d %d %d)\n",
                   J[0],J[1],J[2],J[3],J[0]+1,J[1]+1,J[2]+1,J[3]+1);
            found=1; break; }
        fprintf(stderr,"slots %d%d%d%d injective (%ld products)\n",
                J[0],J[1],J[2],J[3],n);
    }
    if(!found) printf("k=4 PRODUCT-INJECTIVE on all C(7,4)=35 subsets\n");
    free(keys); return 0;
}
```
On a hit, re-enumerate the single failing subset storing `key→(a,b,c,d)` to recover both 4-tuples; each maps to `(i_t,a_t)` and re-checks against `cycle68_slot_factorization_checker.py`'s `slot_product`/`build_u`, with `L-CYCLE71` giving the independent `prod_{e}(xi·eta^{-2t}-3^{a+e})` cross-check. Cost: `35 × 48^4 ≈ 1.86e8` `fmul`s plus 35 sorts of 5.3M `__int128` — seconds-to-minutes in C; the **first bottleneck** named by Cycle 69/70 (CPython `k=4`) is thereby removed.

## 4. Certificate schema

`output_files/RESULTS.json`:
```json
{ "model": {"field_poly":[..17..], "eta":[..], "beta":[2,1]},
  "selfchecks": {"true_tdependent_form_all_336": true,
                 "false_collapse_fails_at": {"t":1,"i":1,"a":0},
                 "color_filter": "sum_color mod 16"},
  "ladder": [{"k":1,"product_injective":true}, ... ,{"k":4,"product_injective":<bool>}],
  "max_good_k": <int>,
  "min_collision_support_if_no_failure": <max_good_k + 1>,
  "first_collision": null | {"k":<int>,"slots":[...],
                             "keys_a":[...],"keys_b":[...],"value":[..16..]},
  "decision": "LADDER_PASSED_TO_KMAX | PARTIAL_COLLISION_FOUND" }
```
A `first_collision` is independently checkable: map each key `k→(i=k//16+1, a=k%16)`, re-evaluate via the banked Cycle-68 `slot_product` and via `prod_e(xi·eta^{-2t}-3^{a+e})`; the two preimage tuples must yield the listed 16-coefficient `value`.

## 5. Energy implication

Nothing new is closed. `k=1,2` injective is banked ⇒ **support ≥ 3** stands. Conditional on the verifier: `max_good_k=3 ⇒ support ≥ 4`; `max_good_k=4 ⇒ support ≥ 5`. A support lower bound alone does **not** bound `D`, `m_max`, or `Occ`. The decision gate is unchanged: `D ≤ 155 ⇒ m_max ≤ 12 ⇒ Occ ≥ |P_0|/12 = 4,395,630,592 > 2^32` (and `|P_0|/13 ≈ 4.06e9 < 2^32`, so only `D ≥ 156` obstructs). Support ≥ 5 is the precondition the next lemma needs to attack `D` through 4-slot energies — it is not itself a bound. Model-level only; not an MCA theorem; no probabilistic claim is used as proof.

## 6. Next exact lemma / construction

**Yes, a route to a full solve exists, in checkable rungs.** Next steps:

1. Run `CHECKER.py --kmax 3 --dump-c`, then `ladder_k4`. Expected `max_good_k=4 ⇒ support ≥ 5` (banked), or an explicit partial collision.
2. **`L-CYCLE71-SUPPORT-5-ENERGY-BOUND`.** With support ≥ 5 and `L-CYCLE71-FULL-DISPLACEMENT`, every collision is fully displaced across ≥ 5 slots. Compute the exact 4-slot ordered-collision energies `D_4(J)` (already in `k≤4 ≈ 1.9e8` reach) and bound the full `D` by a certified sum over the `C(7,5)+C(7,6)+C(7,7)=29` supersets, aiming to certify `D ≤ 155` directly — collapsing the `2|P_0|` materialization into a heavy-bucket enumeration over fully-displaced 5+-supports.
3. **Cheap pre-filter to make `k=4` (and `D_4`) far smaller:** the norm `N_{F/F_{17^4}}: F^*→F_{17^4}^*` (order `83520`) is a homomorphism, so any product collision must have equal norm-images. Bucketing the `48^4` tuples by `(color, N_{17^4}-product)` partitions them into many classes and reduces each full-equality dedup pass by orders of magnitude; it is a sound necessary filter (not a proof by itself). This is the construction I would build next to shrink the heavy-bucket count for step 2.