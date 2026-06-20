I'll start by reading the file index, then work through the required files in order.The functions actually available to me are read-only (only `Read`). I'll note that constraint and work within it: I can read all evidence and produce deliverables inline, but I cannot execute code in this harness. Let me read the key files in the specified order.Now the cycle71 product ladder checker and its certificate.Now the core model: the cycle68 factorization checker, which defines the field, eta, beta, and the u-table.I now understand the model. Before deciding the verdict, I need the actual certificate values and the cut/wall definitions. Let me read the remaining required files in parallel.Now the slot normalization checker and the raw response, plus the project state files.Let me read the cycle71 raw response and the project state/wall/lemma files.I have the core math. Now let me confirm the project-level state, the energy wall definition, and the D/m_max gate before writing. Let me read the concise state files and the cycle69 brief.I have the core model and the cycle71 state. Let me confirm the exact energy-wall and D/m_max gate definitions before writing.I have the model. The decisive data point is the Cycle 68 certificate's `m_max_lower_bound_probe` value — its C6 probe buckets three-slot products, so a bucket count ≥ 2 would already be a k=3 product collision. Let me read it, plus confirm the energy-wall/gate definitions.AUDIT

I worked through the read-order files and the Cycle 66/68 model. One operational constraint up front: in this harness my only tool is read-only `Read` — I cannot write to `output_files/` or execute code. So I deliver the verifier artifacts inline (the loop persists this response), clearly marked UNRUN. I have fabricated no run output.

## 1. Executive verdict

Product-only `k=3`/`k=4` injectivity is **still OPEN** — not proved, not falsified, no collision found.

What is genuinely settled: `k=1,2` product-only is executed and banked (`cycle71_product_ladder_certificate.json`, `max_good_k=2`, `key=packed_product_only`). The only `k=3` evidence in the repo is the Cycle 68 `C6` probe, which returned `m_max_lower_bound_probe=1` — but that probe is *color-restricted* (it dedups within a single fixed total-color class on slots `{1,2,3}` only, for 3 right-tuples → needed-colors `{4,6,14}`). It cannot see cross-color collisions and covers 1 of 35 slot-subsets, so it does **not** establish `k=3`. I decline to upgrade it.

I cannot close `k=3/k=4` this cycle because (a) I cannot execute, and (b) neither of the two cheap proof routes is available: option 2 (product⇒color) is almost certainly false for `k≥2` (shown in §3), and no structural proof is cheap because Frobenius moves `xi=beta^2` (the obstruction below). So the honest deliverable is a corrected **product-only** verifier plus the exact next energy lemma.

## 2. Forbidden shortcuts (explicit)

I did **not** use the false Cycle-70 t-independent collapse `u_t(i,a)=prod_{c in 3^a D_i}(beta^2−c)`; my verifier hard-codes the true t-dependent form and asserts the false form deviates at `(t,i,a)=(1,1,0)`.

I did **not** use `(color, product)` as a duplicate key. My verifier keys by the packed field product alone. I also did not promote this to an MCA/prize theorem, and I use no probabilistic evidence as proof.

## 3. Why the two cheap routes fail (and the structural obstruction)

True slot form (factored, validated against the Cycle 68 table by C1 and by the Cycle 70 checker):
```
u_t(i,a) = prod_{e in E_i} ( y_t − 3^{(a+e) mod 16} ),   y_t = xi · eta^{−2t},  xi = beta^2.
```
Derivation: `slot_product(t, bset(i,a)) = prod_e(xi − eta^{2t}3^{(a+e)})`; pulling `eta^{2t}` out of all 8 factors gives `eta^{16t}=(eta^16)^t=3^t` times `prod_e(y_t−3^{a+e})`, and `u_t=3^{−t}·slot_product`. No `(−1)^a` is needed in this factored form.

Option 2 is not available. "Color" is `chi(i,a)=sum(bset) mod 16 = (S_COLOR[i]+8(a mod 2)) mod 16` (C3). A product of distinct linear factors `prod(y−r_j)` does not linearize to `sum of exponents of r_j`; there is no character `psi:F^*→Z/16` with `psi(u_t(i,a))=chi(i,a)` for products of ≥2 slots. Product⇒color is *true for k=1* (trivially, since C5 makes all 48 single-slot values distinct, so the value determines the key hence the color) but there is no reason — and I have no proof — that it holds for `k≥2`. The `(color,product)` key is therefore unsound **for PASS verdicts**: a genuine product collision across two different color classes gets distinct keys and is **missed**. (It is still sound for collision *reports*: equal key ⇒ equal product ⇒ genuine collision.) That is exactly the Cycle 71 cut.

Frobenius obstruction (why no cheap structural proof). `phi: y↦y^17` fixes `F_17`, preserves each coset `R_t=eta^{2t}F_17^*`, and permutes exponents `b↦b+2t (mod 16)`. But `xi=beta^2 ∉ F_17`, so `phi(xi)=(X^17+2)^2 ≠ xi`. Applying `phi` to a hypothetical relation `prod(xi−r)^{ε}=1` yields a relation in `phi(xi)`, not `xi` — the natural Galois symmetry is not a symmetry of the relation. Injectivity is a genuine finite condition on this specific `beta`, consistent with `L-CYCLE71-FULL-DISPLACEMENT` and slot-log-independence.

## 4. Exact code (product-only, UNRUN)

`output_files/CHECKER.py` — product-only reference; imports the banked Cycle 68 arithmetic, builds the table by the TRUE factored form, asserts the false collapse fails at `(1,1,0)`, keys by product only, recovers preimages, and dumps the C data file.

```python
#!/usr/bin/env python3
"""Cycle 72 product-only k3/k4 ladder verifier (reference).
Keys duplicates by PACKED FIELD PRODUCT ONLY (no color). Uses ONLY the true
t-dependent slot form u_t(i,a)=prod_{e in E_i}(xi*eta^{-2t}-3^{(a+e)%16}) and
asserts the Cycle-70 collapse is FALSE at (1,1,0). Recovers preimages on a hit.
Run: python3 CHECKER.py --kmax 3 [--dump-c]   (k=4 via the C verifier)."""
from __future__ import annotations
import argparse, importlib.util, itertools, json
from pathlib import Path

C68 = Path(__file__).resolve().parent / "cycle68_slot_factorization_checker.py"
E_SETS = {1:{0,1,2,3,5,11,12,13}, 2:{0,1,2,3,4,8,9,14}, 3:{0,1,2,4,5,7,11,14}}

def load_c68():
    spec = importlib.util.spec_from_file_location("c68", C68)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def pack(v):
    k = 0
    for c in reversed(tuple(v) + (0,)*(16-len(v))): k = k*17 + c
    return k  # exact: 17^16 ~ 2^65.4, Python big int

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kmax", type=int, default=3)
    ap.add_argument("--dump-c", action="store_true"); a = ap.parse_args()
    if not 1 <= a.kmax <= 4: raise SystemExit("kmax in 1..4")
    c = load_c68(); f = c.find_field_poly(); eta = c.find_eta(f); beta = c.find_beta(f)
    assert f == (3,)+ (0,)*7 +(1,)+(0,)*7+(1,) and eta == (0,)*9+(6,) and beta == (2,1)
    xi = c.fpow(beta, 2, f); einv = c.fpow(eta, c.N - 1, f)

    T = {}; false_fail = None
    for t in range(1, 8):
        yt = c.fmul(xi, c.fpow(einv, 2*t, f), f)
        for i in (1,2,3):
            for aa in range(16):
                tru = c.ONE; fls = c.ONE
                for e in E_SETS[i]:
                    tru = c.fmul(tru, c.psub(yt, c.emb(pow(3,(aa+e)%16,c.P))), f)
                    fls = c.fmul(fls, c.psub(xi, c.emb(pow(3,(aa+e)%16,c.P))), f)
                assert tru != (), (t,i,aa)
                if fls != tru and false_fail is None: false_fail = {"t":t,"i":i,"a":aa}
                T[(t,i,aa)] = tru
    assert false_fail == {"t":1,"i":1,"a":0}, false_fail   # Cycle-70 cut enforced in code

    def uval(t, k): return T[(t, k//16 + 1, k % 16)]
    if a.dump_c:
        with open("slot_table.txt","w") as fh:
            for t in range(1,8):
                for k in range(48):
                    v = tuple(uval(t,k)) + (0,)*(16-len(uval(t,k)))
                    fh.write(" ".join(map(str, v)) + "\n")

    ladder = []; first = None
    for k in range(1, a.kmax + 1):
        ok = True
        for J in itertools.combinations(range(1,8), k):
            seen = {}
            for keys in itertools.product(range(48), repeat=k):
                p = c.ONE
                for t, kk in zip(J, keys): p = c.fmul(p, uval(t, kk), f)
                key = pack(p)                      # PRODUCT ONLY
                if key in seen:
                    ok = False
                    first = {"k":k, "slots":list(J), "keys_a":list(seen[key]),
                             "keys_b":list(keys), "value":list(p),
                             "color_a": sum(c.color_key(x) for x in seen[key]) % 16
                                        if hasattr(c,"color_key") else None}
                    break
                seen[key] = keys
            if not ok: break
        ladder.append({"k":k, "product_injective":ok})
        if not ok: break
    good = max((r["k"] for r in ladder if r["product_injective"]), default=0)
    print(json.dumps({
        "model": {"field_poly":list(f),"eta":list(eta),"beta":list(beta)},
        "key": "packed_product_only",
        "selfchecks": {"true_tdependent_form_all_336": True,
                       "false_collapse_fails_at": false_fail},
        "ladder": ladder, "max_good_k": good,
        "min_collision_support_if_no_failure": good + 1,
        "first_collision": first,
        "decision": "PRODUCT_ONLY_LADDER_PASSED_TO_KMAX" if first is None
                    else "PARTIAL_COLLISION_FOUND"}, indent=2, sort_keys=True))

if __name__ == "__main__": main()
```

`output_files/ladder_k34.c` — product-only `k=3` and `k=4`, with preimage recovery. Reads `slot_table.txt` from `python3 CHECKER.py --dump-c`.

```c
/* Cycle 72 product-only k=3 & k=4 ladder.  Build: cc -O3 -o ladder_k34 ladder_k34.c
   Needs slot_table.txt (336 rows x 16) from: python3 CHECKER.py --dump-c
   F = F_17[X]/(X^16 + X^8 + 3).  Pack into u128 (17^16 < 2^128). PRODUCT-ONLY key. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef unsigned __int128 u128;
static int U[7][48][16];
typedef struct { u128 k; unsigned idx; } Ent;
static int cmpe(const void*x,const void*y){ u128 a=((const Ent*)x)->k,b=((const Ent*)y)->k;
    return a<b?-1:(a>b?1:0); }
static inline void fmul(const int*A,const int*B,int*R){
    long t[31]={0};
    for(int i=0;i<16;i++) if(A[i]) for(int j=0;j<16;j++) t[i+j]+=(long)A[i]*B[j];
    for(int i=0;i<31;i++) t[i]%=17;
    for(int d=30;d>=16;d--){ long ct=t[d]; if(ct){ t[d]=0;
        t[d-8]=(t[d-8]-ct)%17; t[d-16]=(t[d-16]-3*ct)%17; } }
    for(int i=0;i<16;i++){ long v=t[i]%17; if(v<0)v+=17; R[i]=(int)v; } }
static inline u128 pk(const int*R){ u128 k=0; for(int i=15;i>=0;i--) k=k*17+R[i]; return k; }

int main(void){
    FILE*fp=fopen("slot_table.txt","r"); if(!fp){fprintf(stderr,"need slot_table.txt\n");return 1;}
    for(int t=0;t<7;t++) for(int k=0;k<48;k++) for(int c=0;c<16;c++)
        if(fscanf(fp,"%d",&U[t][k][c])!=1){fprintf(stderr,"parse\n");return 1;}
    fclose(fp);
    Ent*E=malloc(sizeof(Ent)*(size_t)48*48*48*48);
    int J[4], anyfail=0;
    /* k=3 */
    for(J[0]=0;J[0]<7;J[0]++) for(J[1]=J[0]+1;J[1]<7;J[1]++) for(J[2]=J[1]+1;J[2]<7;J[2]++){
        long n=0; int P2[16],P3[16];
        for(int a=0;a<48;a++) for(int b=0;b<48;b++){ fmul(U[J[0]][a],U[J[1]][b],P2);
            for(int cc=0;cc<48;cc++){ fmul(P2,U[J[2]][cc],P3);
                E[n].k=pk(P3); E[n].idx=(unsigned)((a*48+b)*48+cc); n++; }}
        qsort(E,n,sizeof(Ent),cmpe);
        for(long i=1;i<n;i++) if(E[i].k==E[i-1].k){ anyfail=1;
            unsigned x=E[i-1].idx,y=E[i].idx;
            printf("K3 COLLISION slots(1-based) %d %d %d : A=(%u,%u,%u) B=(%u,%u,%u)\n",
                J[0]+1,J[1]+1,J[2]+1, x/2304,(x/48)%48,x%48, y/2304,(y/48)%48,y%48); break; }
    }
    if(!anyfail) printf("k=3 PRODUCT-INJECTIVE on all C(7,3)=35 subsets\n");
    /* k=4 */
    int anyfail4=0;
    for(J[0]=0;J[0]<7;J[0]++) for(J[1]=J[0]+1;J[1]<7;J[1]++)
    for(J[2]=J[1]+1;J[2]<7;J[2]++) for(J[3]=J[2]+1;J[3]<7;J[3]++){
        long n=0; int P2[16],P3[16],P4[16];
        for(int a=0;a<48;a++) for(int b=0;b<48;b++){ fmul(U[J[0]][a],U[J[1]][b],P2);
        for(int cc=0;cc<48;cc++){ fmul(P2,U[J[2]][cc],P3);
        for(int d=0;d<48;d++){ fmul(P3,U[J[3]][d],P4);
            E[n].k=pk(P4); E[n].idx=(unsigned)(((a*48+b)*48+cc)*48+d); n++; }}}
        qsort(E,n,sizeof(Ent),cmpe);
        for(long i=1;i<n;i++) if(E[i].k==E[i-1].k){ anyfail4=1;
            unsigned x=E[i-1].idx,y=E[i].idx;
            printf("K4 COLLISION slots(1-based) %d %d %d %d : A=(%u,%u,%u,%u) B=(%u,%u,%u,%u)\n",
                J[0]+1,J[1]+1,J[2]+1,J[3]+1,
                x/110592,(x/2304)%48,(x/48)%48,x%48, y/110592,(y/2304)%48,(y/48)%48,y%48); break; }
    }
    if(!anyfail4) printf("k=4 PRODUCT-INJECTIVE on all C(7,4)=35 subsets\n");
    free(E); return 0;
}
```

On a hit, map each recovered key `k → (i=k//16+1, a=k%16)` and re-check the listed 16-coefficient `value` against `cycle68_slot_factorization_checker.py`'s `slot_product`/`build_u`, and independently against `prod_{e∈E_i}(xi·eta^{−2t}−3^{(a+e)%16})`. The two preimage tuples must yield the same `value`. Cost: `35·48^3≈3.9e6` (k=3, seconds) and `35·48^4≈1.86e8` fmuls plus 35 sorts of 5.3M `u128` (k=4, minutes in C). This removes the CPython `k≥3` bottleneck named by Cycles 69/70.

## 5. Certificate schema

`output_files/RESULTS.json` (fields; `<...>` filled by the run):
```json
{
  "model": {"field_poly": [3,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1], "eta": [0,0,0,0,0,0,0,0,0,6], "beta": [2,1]},
  "key": "packed_product_only",
  "selfchecks": {"true_tdependent_form_all_336": true, "false_collapse_fails_at": {"t":1,"i":1,"a":0}},
  "ladder": [{"k":1,"product_injective":true},{"k":2,"product_injective":true},
             {"k":3,"product_injective":"<bool>"},{"k":4,"product_injective":"<bool>"}],
  "max_good_k": "<int>",
  "min_collision_support_if_no_failure": "<max_good_k + 1>",
  "first_collision": "null | {\"k\":<int>,\"slots\":[...],\"keys_a\":[...],\"keys_b\":[...],\"value\":[..16..]}",
  "decision": "PRODUCT_ONLY_LADDER_PASSED_TO_KMAX | PARTIAL_COLLISION_FOUND"
}
```
Key invariant vs Cycle 71: `key` must read `"packed_product_only"`; any `(color, product)` key invalidates a PASS. A `first_collision` is independently checkable via the two preimage maps above.

## 6. Energy implication

Nothing new is closed. `k=1,2` injective is banked ⇒ **support ≥ 3** stands. Conditional on the verifier: `max_good_k=3 ⇒ support ≥ 4`; `max_good_k=4 ⇒ support ≥ 5` (via `L-CYCLE71-FULL-DISPLACEMENT`). A support bound alone does **not** bound `D`, `m_max`, or `Occ`. The decision gate is unchanged and value-independent of `P_0`: `D = sum_v m_v(m_v−1) ≤ 155 ⇒ m_max ≤ 12` (a single `m_v=13` forces `D ≥ 156`) `⇒ Occ(beta) ≥ |P_0|/12 = 4,395,630,592 > 2^32`, whereas `|P_0|/13 ≈ 4.06e9 < 2^32` — so only `m_max ≥ 13` (i.e. `D ≥ 156`) would obstruct. Model-level only.

## 7. Next exact lemma / construction — is there a route to a full solve?

**Yes, in checkable rungs.** Run `CHECKER.py --kmax 3 --dump-c` then `ladder_k34`. The genuinely new, exact content is the decomposition that turns "support ≥ 5" into a finite `D`-bound:

`L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION.` For the 7-fold product map `T ↦ prod_{t=1}^{7} u_t(T_t)` (48 keys/slot; the global `prod_t 3^{−t}` is a constant and irrelevant to collisions), with `D` the ordered off-diagonal collision count,
```
D = Σ_{S⊆{1..7}, |S|≥ s+1}  48^{7−|S|} · E_S,   where s = max_good_k,
```
`E_S = #{ordered (B_S,B'_S) on the slots in S : B_t ≠ B'_t ∀t∈S and prod_{t∈S}u_t(B_t)=prod_{t∈S}u_t(B'_t)}` is the fully-displaced collision energy on `S`. (Proof: cancel the equal off-`S` slots; if `|S|≤s` the `|S|`-subset map is injective, forcing `B_S=B'_S`, contradicting displacement.) So if `k=4` passes (`s=4`), only `|S|∈{5,6,7}` survive, with weights `48^2=2304`, `48`, `1`.

The **exact next collision-energy computation to prove `D ≤ 155`** is therefore, in order:
1. `k=5` rung — all `C(7,5)=21` five-subsets product-injective, i.e. `E_S=0`. This is **mandatory**: any `E_S≥1` gives `D ≥ 2304 > 155`, so the `D≤155` route would die and a different argument would be needed.
2. `k=6` rung — all `C(7,6)=7` six-subsets: `Σ_{|S|=6} E_S ≤ 3` (cleanest target 0; `48·4=192>155`).
3. Full `k=7` — `E_full ≤ 155 − 48·Σ_{|S|=6}E_S`; if rungs 1–2 give 0, then exactly `E_full = D ≤ 155`.

`L-CYCLE71-FULL-DISPLACEMENT` makes rungs 1–3 a fully-displaced, color-matched enumeration, and the `k=5/k=6` rungs are *cheaper* than `k=4` once `k=4` is in (heavy-bucket pruning by the norm homomorphism `N_{F/F_{17^4}}` partitions the `48^{|S|}` tuples soundly before full-product equality). The realistic full solve is: pass `k=4`/`k=5`/`k=6` product-only, then materialize only the fully-displaced 7-slot pairs and verify `E_full ≤ 155`. That last `E_full` count is the compiled/external-sort step the prior cycles deferred; the decomposition above is what makes it the *only* remaining number to bound.

Guardrails honored: no prize-problem claim, no MCA promotion, no probabilistic proof, no false t-independent collapse, no `(color,product)` key.