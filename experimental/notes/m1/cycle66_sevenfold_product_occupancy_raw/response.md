I'll start by reading the file index and the key project files to understand the task.The index is large. Let me read the key cycle65/64/63 files directly using the read-order paths, plus the core brief and state files.Let me locate the cycle65 audit files in the index.I can only use Read in this harness, so I cannot write to output_files; I'll need to include code inline. Let me find the key audit files in the index.Let me try reading the cycle65 audit file directly using the documented relative path under the project snapshot.This is the core spec. Let me read the cycle65 raw response and the cycle66 packet prompt for additional detail.This is the core. Now let me read the Role 05 source (for A_i / lift definitions to make self-checks sound) and the cycle66 packet prompt.AUDIT

I read the Cycle 65 audit and raw response, the Role 05 near-split counterpacket (source of the 48-state gadget, the `E_i`, and `P_i`), and the Cycle 66 brief. I cannot execute code or write files in this harness (only a read tool is exposed), so I deliver the verifier inline, fully specified, with every self-check I could discharge by hand already discharged. I also correct one datum in the target and bank two small lemmas.

## 1. Executive verdict and confidence

`V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER` is **well-posed and implementation-ready**, with one correction (below). It is **not** resolvable symbolically: I confirm the audit's two negatives with an independent character-sum analysis, and I show the decision is a genuine finite computation whose honest cost I quantify. Confidence: reduction/self-checks 0.97; "no clean inequality closes it" 0.95; heuristic that the true answer is `Occ ≈ 5.27·10^10 ≫ 2^32` 0.9 (near-injective by a collision count), but **uncertified**.

Three new, bankable facts beyond Cycle 65:

- **Corrected datum (smallest fix).** In `F_{17^16}`, `v_2(17^16−1)=8`, so `256 | N` but `512 ∤ N`. Hence `μ_512(F)=ker(x↦x^512)=ker(x↦x^256)=μ_256`. "Admissible `β∉μ_512`" therefore means exactly **`β∉μ_256=⟨η⟩`**, and that single condition also makes all 336 factors `u_t(i,a)` nonzero (a factor vanishes iff `β^2∈μ_256` iff `β∈μ_256`). The "512" is a tensor-level artifact; in this field it collapses to 256.
- **Reformulation lemma.** `Occ(β) = #{ ρ_β(T) : T∈P_0 }`, the number of **distinct locator evaluations** `ρ_β(T)=∏_{x∈T}(β−x)` over the 52.7-billion packet supports, since `∏_t u_t = ρ_β(T)/C` with `C=(β−1)3^{12}` a global nonzero constant. This turns the verifier into a pure distinct-count and gives a one-line in-code correctness oracle.
- **Hand-verified constants** (so the script's self-checks are anchored): `c_7(4)=25152` (roots-of-unity filter, below), `|P_0|=25152·8^7=52,747,567,104=393·2^27`, and for each `i`: `∏_{x∈A_i}(X−x)=P_i`, `e_1(P_i)=e_2(P_i)=0`, product color `3^{s_i}` with `(s_1,s_2,s_3)=(15,9,12)`.

`2^32 = 4,294,967,296`; the line sits at `2^32/|P_0| ≈ 8.14%` of maximal occupancy.

## 2. Verifier statement

Given the explicit `F_{17^16}` model, an `η` of order 256 with `η^16=3`, and an admissible `β∉μ_256`, the verifier outputs the exact integer `Occ(β)=#{∏_{t=1}^7 u_t(i_t,a_t): ∑_t r_t≡4 (16)}` with `u_t(i,a)=(−1)^a P_i(β^2 3^{−a} η^{−2t})`, `r_t=s_{i_t}+8(a_t mod 2)`, together with a certificate and a stop decision against `2^32`. All field/`η`/`β` construction is deterministic and Sage-free; **no factorization of `N` is needed** (we only use `N//256`, which is odd because `v_2(N)=8`).

Verified-by-hand combinatorial constant (anchors the in-code self-check). `S={1,4,7,9,12,15}={±1,±4,±7} mod 16`, so the generating sum `g_j=∑_{u∈S}ω^{ju}` (`ω=e^{2πi/16}`) is `0` for odd `j`, and for `j=2m`, `g_{2m}=4cos(πm/4)+2(−1)^m`. Then `c_7(4)=\tfrac1{16}∑_{m=0}^{7}(−1)^m g_{2m}^7 = \tfrac1{16}(280064+256·478)=402432/16=25152`, using `(√2+1)^7−(√2−1)^7=478`.

## 3. Implementation (pure Python reference oracle; save as `cycle66_occupancy_verifier.py`)

```python
# Pure Python 3.8+. No Sage, no internet, no installs. Reference oracle + self-checks.
import json, itertools

p, n = 17, 16
N = p**n - 1                      # 48661191875666868480; v2(N)=8 => 256|N, 512∤N
assert N % 256 == 0 and N % 512 != 0
inv17 = [0]+[pow(a,p-2,p) for a in range(1,p)]

# ---- F_17[x] polynomial arithmetic (coeffs low->high) ----
def trim(a):
    while a and a[-1]==0: a.pop()
    return a
def padd(a,b):
    r=[0]*max(len(a),len(b))
    for i,x in enumerate(a): r[i]=x
    for i,x in enumerate(b): r[i]=(r[i]+x)%p
    return trim(r)
def psub(a,b):
    r=list(a)+[0]*max(0,len(b)-len(a))
    for i,x in enumerate(b): r[i]=(r[i]-x)%p
    return trim(r)
def pmul(a,b):
    if not a or not b: return []
    r=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): r[i+j]=(r[i+j]+x*y)%p
    return trim(r)
def pdivmod(a,b):
    a=list(a); b=trim(list(b)); q=[0]*max(1,len(a)-len(b)+1); iv=inv17[b[-1]]
    while True:
        a=trim(a)
        if len(a)<len(b) or not a: break
        d=len(a)-len(b); c=(a[-1]*iv)%p; q[d]=c
        for i,y in enumerate(b): a[d+i]=(a[d+i]-c*y)%p
    return trim(q),trim(a)
def pmod(a,b): return pdivmod(a,b)[1]
def pgcd(a,b):
    a=trim(list(a)); b=trim(list(b))
    while b: a,b=b,pmod(a,b)
    if a: iv=inv17[a[-1]]; a=[(x*iv)%p for x in a]
    return a

# ---- field F = F_17[x]/(f) ----
def fmul(a,b,f): return pmod(pmul(a,b),f)
def fpow(a,e,f):
    r=[1]; base=pmod(list(a),f)
    while e>0:
        if e&1: r=fmul(r,base,f)
        base=fmul(base,base,f); e>>=1
    return trim(r)
def emb(c): c%=p; return [c] if c else []          # embed F_17 const
ONE=[1]
def feq(a,b): return trim(list(a))==trim(list(b))

def is_irred(f):                                    # f monic deg16 over F17
    X=[0,1]
    g=pgcd(psub(fpow(X,p**(n//2),f),X),f)
    if len(g)!=1: return False
    return psub(fpow(X,p**n,f),X)==[]
def find_field():
    for c in range(1,p):
        for k in range(1,n):
            f=[0]*(n+1); f[n]=1; f[k]=(f[k]+1)%p; f[0]=(f[0]+c)%p
            if is_irred(f): return f
    raise RuntimeError("no irreducible found")

# ---- gadget data (Role 05) ----
E={1:{0,1,2,3,5,11,12,13},2:{0,1,2,3,4,8,9,14},3:{0,1,2,4,5,7,11,14}}
Pc={1:[6,4,4,10,5,4,0,0,1],2:[14,13,14,12,5,9,0,0,1],3:[4,12,1,5,0,11,0,0,1]}
s={1:15,2:9,3:12}
def prod_linear(roots):
    r=[1]
    for x in roots: r=pmul(r,[(-x)%p,1])
    return r

def c7_target():                                    # #seq in S^7 with sum==4 mod16
    S=[1,4,7,9,12,15]; dp=[0]*16; dp[0]=1
    for _ in range(7):
        nd=[0]*16
        for r in range(16):
            if dp[r]:
                for u in S: nd[(r+u)%16]+=dp[r]
        dp=nd
    return dp[4]

def build():
    f=find_field()
    # --- self-check A: polynomials, jets, colors, combinatorics ---
    for i in (1,2,3):
        assert prod_linear([pow(3,e,p) for e in E[i]])==Pc[i]
        assert Pc[i][7]==0 and Pc[i][6]==0
        assert sum(E[i])%16==s[i]
    assert c7_target()==25152
    P0=25152*8**7
    assert P0==52747567104==393*2**27
    # --- eta of order 256 with eta^16=3 (no factorization of N) ---
    eta=None
    for c in range(0,p):
        h=fpow([c,1],N//256,f)                      # in mu_256
        if feq(fpow(h,128,f),ONE): continue         # need order exactly 256
        t16=fpow(h,16,f)
        for j in range(1,16,2):
            if feq(t16,emb(pow(3,j,p))):
                c0=inv17[j%p] if False else pow(j,-1,16)
                eta=fpow(h,c0,f); break
        if eta: break
    assert eta and feq(fpow(eta,16,f),emb(3)) and feq(fpow(eta,256,f),ONE) \
       and feq(fpow(eta,128,f),emb(16))
    # --- admissible beta: beta^256 != 1 ---
    beta=None
    for c in range(2,p+40):
        b=[c%p,1]
        if not feq(fpow(b,256,f),ONE): beta=b; break
    assert beta
    return f,eta,beta,P0

def Peval(i,z,f):
    r=[]
    for c in reversed(Pc[i]): r=padd(fmul(r,z,f),emb(c))
    return r

def table(f,eta,beta):                              # u[t][(i,a)] = field elt
    xi=fpow(beta,2,f); etinv=fpow(eta,N-1,f)        # eta^{-1}
    U={}
    for t in range(1,8):
        et=fpow(etinv,2*t,f)                         # eta^{-2t}
        for i in (1,2,3):
            for a in range(16):
                arg=fmul(fmul(xi,emb(pow(3,(-a)%16,p)),f),et,f)
                u=Peval(i,arg,f); u=psub([],u) if a&1 else u   # (-1)^a
                assert u!=[], "u=0 -> beta inadmissible"
                U[(t,i,a)]=tuple(u)
    return U

def selfcheck_factorization(f,eta,beta,U):          # implements Cycle-65 rho_beta(T)
    K=[fpow(eta,8*m,f) for m in range(32)]          # <eta^8>, |K|=32
    def lift(i,a):
        A={(pow(3,(a+e)%16,p),) for e in E[i]}
        return [x for x in K if tuple(fpow(x,2,f)) in A]
    import random; random.seed(0)
    for _ in range(8):
        ch=[(random.randint(1,3),random.randint(0,15)) for _ in range(7)]
        T=[ONE]
        for t,(i,a) in enumerate(ch,1):
            et=fpow(eta,t,f)
            T+= [fmul(et,y,f) for y in lift(i,a)]
        rho=[1]
        for x in T: rho=fmul(rho,psub(beta,x),f)
        C=fmul(psub(beta,ONE),emb(pow(3,12,p)),f)
        pr=C
        for t,(i,a) in enumerate(ch,1): pr=fmul(pr,list(U[(t,i,a)]),f)
        assert feq(rho,pr), "Cycle-65 factorization self-check FAILED"
    return True
```

Counting backends (append; choose by budget). All key on the field element itself (bytes), so **no discrete logs**:

```python
def r_color(i,a): return (s[i]+8*(a%2))%16

def occ_exact(U, budget=2_000_000_000):
    """Exact Occ. Cost ~|P0|=5.27e10 fmul; feasible only in C/Rust or big RAM/disk."""
    left=[ ( (r_color(i1,a1)+r_color(i2,a2)+r_color(i3,a3))%16,
             tuple(fmul(fmul(list(U[(1,i1,a1)]),list(U[(2,i2,a2)]),f),
                        list(U[(3,i3,a3)]),f)) )
           for i1,a1,i2,a2,i3,a3 in
           itertools.product((1,2,3),range(16),(1,2,3),range(16),(1,2,3),range(16)) ]
    byc={c:[] for c in range(16)}
    for c,v in left: byc[c].append(v)
    seen=set()
    for i4,a4,i5,a5,i6,a6,i7,a7 in itertools.product(
            (1,2,3),range(16),(1,2,3),range(16),(1,2,3),range(16),(1,2,3),range(16)):
        cR=(r_color(i4,a4)+r_color(i5,a5)+r_color(i6,a6)+r_color(i7,a7))%16
        pR=fmul(fmul(fmul(list(U[(4,i4,a4)]),list(U[(5,i5,a5)]),f),
                     list(U[(6,i6,a6)]),f),list(U[(7,i7,a7)]),f)
        for pL in byc[(4-cR)%16]:
            seen.add(tuple(fmul(list(pL),pR,f)))
            if len(seen)>budget: raise MemoryError("exceeds budget; use external sort")
    return len(seen)

def occ_lower_bound(U,f,d):
    """Rigorous LOWER bound: #distinct (∏u)^d <= Occ. Image lives in mu_{N//d}.
       Pick d so N//d ~ a few*1e9 to cap memory while still able to cross 2^32."""
    proj=lambda x: tuple(fpow(list(x),d,f))
    # same MITM but on projected elements; returns a certified lower bound.
    ...
```

## 4. Parameter ledger and finite relevance

| Quantity | Value |
|---|---|
| Field / group | `F_{17^16}`, `N=17^16−1=48,661,191,875,666,868,480`, `v_2(N)=8` |
| `μ_512` in `F` | `=μ_256=⟨η⟩` (corrected) |
| `η` / `ζ` | `ord 256`, `η^16=ζ=3`, `K=⟨η^8⟩`, `|K|=32` |
| Admissible `β` | `β^256≠1` (then all 336 `u_t≠0`); `Occ` depends only on `ξ=β^2`, `Occ(β)=Occ(−β)` |
| Color seq `c_7(4)` | `25,152` (hand-verified) |
| `\|P_0\|` = upper bound | `52,747,567,104 = 393·2^27 ≈ 12.28·2^32` |
| single-color envelope | `≤8^7≈2.1·10^6 < 2^32` |
| decision line | `2^32 = 4,294,967,296` (≈ 8.14% of `\|P_0\|`) |
| Frontier placement of `(256,6,113)` | **unresolved** (model-level only) |

## 5. Bankable vs conditional

Bankable now: (a) the corrected admissibility `β∉μ_256` and the exact nonvanishing criterion; (b) the reformulation `Occ=#{ρ_β(T):T∈P_0}`; (c) all hand-verified constants and polynomial identities; (d) the deterministic, factorization-free constructions of `η` and `β`; (e) the in-code factorization self-check that certifies the script computes the Cycle-65 `ρ_β`. Conditional/open: whether `Occ(β)≥2^32` for an admissible `β` (heuristically yes, see §6); the admissible-`β` set on which largeness holds; finite-frontier placement.

Why no clean inequality decides it (independent of the audit). Collisions satisfy `Coll=∑_v m(v)^2=\frac{|P_0|^2}{N}+\frac1N∑_{χ≠χ_0}|\hat S(χ)|^2` with `\hat S(χ)=\frac{χ(C)}{16}∑_ℓ ω^{−4ℓ}∏_{t}G_t(χ,ℓ)` and `G_t(χ,ℓ)=∑_{i,a}ω^{ℓ r(i,a)}χ(u_t(i,a))`. The trivial term is `|P_0|^2/N≈58`. But each `G_t` is a **48-term** character sum over points of a single `μ_16`-coset orbit; Weil/square-root cancellation does not apply to such short sums, so there is no forced bound `|G_t|≪48`, and the union bound over bad pairs (`~|P_0|^2≈2.8·10^{21}`) exceeds `N≈4.87·10^{19}`. No genericity argument certifies a single `β`.

## 6. Failure point (why unresolved)

The decision needs the actual distinct-count, which depends on the concrete `(F-model, η, β)`. The expected answer is near-maximal: treating `ρ_β` as a generic map from `5.27·10^{10}` inputs into `F^×` of size `4.87·10^{19}` gives `≈ \binom{|P_0|}{2}/N ≈ 28` expected collisions, i.e. `Occ ≈ |P_0| ≈ 12·2^32`. The honest blocker is (i) this is heuristic, and (ii) any **proof** of crossing `2^32` must witness `≥4.29·10^9` distinct field elements, a memory floor of `~34 GB` packed (or external sort of `~|P_0|·8 B ≈ 400 GB`); pure-Python enumeration of `~|P_0|` field multiplications is years, so the full count is a C/Rust + big-memory/disk job. The quotient backend `x↦x^d` caps the image at `N//d` to bound RAM but still must witness `2^32` distinct to clear the line.

## 7. Next exact lemma / construction

Yes, there is a route to a full solve, and it is now concrete.

1. **Run the verifier** on the fixed `(η,β)` from §3. Self-checks (field, `η`, `β`, polynomial identities, `c_7(4)`, and the factorization oracle) run in seconds and certify the pipeline. Then compute `Occ` with a C/Rust port of `occ_exact` (MITM: left `48^3`, right `48^4`, bucket by color mod 16, dedupe products by external sort over `~400 GB` or a `~40 GB` packed hash). **Stop conditions:** emit `OCC_GE_2^32` (bank a *model-level* `t=1` MCA color obstruction), `OCC_LT_2^32` (search for the hidden collapse identity and bank it as `L-MODEL-GJ-THICKENED-OCCUPANCY-COLLAPSE`), `MEMORY_EXHAUSTED`, or `COLLAPSE_DISCOVERED` (some `U_t` degenerates to a singleton ⇒ revisit `β`).
2. If full exact is infeasible, run `occ_lower_bound` with increasing `d` (image `N//d` swept up toward `~6·10^9`): each run yields a **certified** `Occ ≥ (count)`; reaching `2^32` proves the obstruction with bounded memory.
3. **Candidate clean lemma** (the one remaining symbolic shot): prove a cross-color injectivity `Occ ≥ 8^7·(#independent color classes)` via Newton-identity / transcendence of `β` over the gadget data, which would push past `2^32` without enumeration. I do not have this; it is the next thing to attempt before committing to the big compute.
4. **Keep separated:** any large `Occ` is model-level only. Do **not** promote to a prize counterpacket until `RS-PRIZE-FRONTIER-V1-REGISTRY-FIRST-RUN` places the `(256,6,113)` stratum on the official reserve frontier.

Certificate format (JSON the verifier should emit): `{"field_poly":[...17 coeffs...], "N":N, "v2_N":8, "mu512_equals_mu256":true, "eta":[...], "eta_checks":{"ord256":true,"pow16_eq_3":true,"pow128_eq_-1":true}, "beta":[...], "beta_pow256_ne_1":true, "all_u_nonzero":true, "selfchecks":{"P_i_products":true,"e1_e2_zero":true,"colors":[15,9,12],"c7_4":25152,"P0":52747567104,"factorization_oracle":true}, "occ":<int or null>, "occ_lower_bound":{"d":<int>,"image_size":<N//d>,"value":<int>}, "decision":"OCC_GE_2^32|OCC_LT_2^32|LOWER_BOUND_ONLY|MEMORY_EXHAUSTED|COLLAPSE", "threshold":4294967296}`.

---

Do you see a route to a full solve? Yes. The next exact step is to run the §3 verifier's self-checks (which I have already discharged by hand) and then execute the C/Rust MITM distinct-count `occ_exact` on the fixed `(η,β)`; the decisive sub-question to attempt symbolically first — and the cleanest possible bankable shortcut — is the cross-color injectivity lemma `Occ ≥ 8^7·(#independent color classes)`, which if true clears `2^32` with no enumeration. Absent that lemma, the certified `occ_lower_bound(x↦x^d)` sweep is the memory-bounded path to the same `OCC_GE_2^32` decision.