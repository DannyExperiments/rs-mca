Both file-writing and code-execution are denied in this harness (the Jupyter kernel, `Bash`, and `Write` were all refused). Per the task's own rule — "If a dependency … would be needed, write a precise checker spec instead of pretending it ran" — I will not fabricate a run. I hand-verify everything that is hand-verifiable from the banked machinery, give the complete deterministic pure-Python checker inline so the operator can drop it into `output_files/` and run it, and classify the deliverable honestly.

## What I verified by hand (source-validity + structural gates)

For the explicit family `p ≡ 3 mod 4`, `NR=-1`, `F=F_p[α]`, `α²=-1`, `E=X²+αX+1`, `b=[Bnum]_E=X`, with preferred prime `p0=31` (`31 ≡ 3 mod 4`, so `-1` is a non-residue and `E` is `τ`-separated):

1. No `F_p` roots of `E`. For `a∈F_p`, `E(a)=(a²+1)+α·a`; the `α`-part is `a`, zero only at `a=0`, and `E(0)=1≠0`. ✓ (Cycle 36 gate.)
2. `E`/`E^τ` separation. `E−E^τ=2αX`; a shared root forces `X=0`, but `E(0)=1≠0`, separated in odd char. ✓
3. `c∉B` branch. `c=α∉F_p`, so the `c_b≠0` branch is active. ✓
4. `kappa≠0` is choosable explicitly. `kappa = wedge_F(u,[b]_E)` with `[b]_E=[X]_E=(0_F,1_F)`, so `wedge((u0,u1),(0,1)) = u0`. Hence **`kappa` equals the `X⁰`-component `u0` of `u=[W]_E`**. Choosing free data with `u0≠0` (e.g. `u = 1 + X`, i.e. `u0=1_F`) gives `kappa=1≠0`. ✓
5. Top symbol nonzero. With `c=α, d=1`: `Im(c)=1, Im(d)=0, Im(conj(c)·d)=Im(−α)=−1`, so the Cycle 28/29 quantity `Q_4 = N(c_b)·(Im(d)² − Im(c)Im(conj(c)d)) = N(c_b)·(0 − 1·(−1)) = N(c_b) ≠ 0`. Thus `TopSym(Δ) = −N(kappa)·N(z)²·Q_4 ≠ 0` as a polynomial, so `Δ=det_B M(z)` is not identically zero. ✓
6. Singular bound. `Δ` has total degree `≤4` in `(z₀,z₁)` (Cycle 32/33), nonzero, so `#{Δ=0} ≤ 4p` by Schwartz–Zippel — the singular locus contributes `O(p)` split slopes (Cycle 33 `L-T2J4-A2B-SINGULAR-OP`). ✓

These hand-checks reproduce the banked gates (Cycle 28/29/33/34/36). What they do **not** establish without execution is the off-`Δ` factorization data (`"4"` and `"13"`), which is a finite scan of the 4×4 Cramer system along a line — genuinely computational at `p=31`.

## The certificate logic (Cycle 35 `L-T2J4-A2B-GEOM-CERT`, with the Cycle 36 correction enforced)

On a fixed `B`-line `z₁=m z₀+e`, exclude points with `Δ(z)=0`. Solve `M(z)τ=−C₀(z)`, form `L_τ=X⁴−τ₁X³+τ₂X²−τ₃X+τ₄`, factor over `F_p`. The PASS condition is that the off-`Δ` squarefree types include **both `"4"` and `"13"`**:

- A type `"4"` is a 4-cycle; a type `"13"` is a 3-cycle. No proper transitive subgroup of `S_4` contains both a 4-cycle and a 3-cycle ⇒ `G_arith=S_4`. This is exactly the corrected criterion — transitivity is supplied by the 4-cycle itself, so I do **not** use the forbidden "irreducible resolvent + nonsquare disc ⇒ S_4" shortcut.
- `"13"` is an **even** permutation occurring at a degree-one place. The only nontrivial cyclic quotient of `S_4` is `S_4/A_4` (sign). An even degree-one Frobenius cannot sit in a nontrivial sign coset, so the constant field is exactly `F_p` and `G_geom=G_arith=S_4` on the line, hence on the surface `A²_B`.

A type `"4"` place is also a standalone witness that `disc_X L_τ` is **nonsquare** as a function (a 4-cycle is odd ⇒ disc is a non-residue there), and a no-`F_p`-root cubic resolvent at some place witnesses resolvent absolute irreducibility — both recorded as corroboration, not as the proof spine.

## The checker (complete, deterministic, pure Python — paste into `output_files/cycle37_single_prime_s4_cert.py`)

```python
#!/usr/bin/env python3
"""Cycle 37 single-prime S4 certificate, explicit A2_B family. Pure Python, no deps.
Ledger kept separate: q_gen=p (B=F_p); F=F_{p^2}=B(alpha); q_line=p^2; q_chal unused.
Branch: D=F_p, n=p, t=sigma=2, j=r-t=4, off R0. Family: nr=-1, p=3 mod4, alpha^2=-1,
E=X^2+alpha X+1, b=[Bnum]_E=X. NOT an MCA/CA/list/line/curve/protocol/SNARK/prize claim."""
import json
P, NR = 31, -1
ZF, OF, ALPHA = (0,0), (1,0), (0,1)
def fadd(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def fneg(x): return ((-x[0])%P,(-x[1])%P)
def fsub(x,y): return fadd(x,fneg(y))
def fmul(x,y): return ((x[0]*y[0]+NR*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def fpow(x,n):
    out=OF; b=x
    while n:
        if n&1: out=fmul(out,b)
        b=fmul(b,b); n>>=1
    return out
def finv(x): return fpow(x,P*P-2)
def trim(po):
    po=list(po)
    while len(po)>1 and po[-1]==ZF: po.pop()
    return po
def deg(po):
    po=trim(po); return -1 if po==[ZF] else len(po)-1
def coeff(po,i): return po[i] if i<len(po) else ZF
def pscale(a,c): return trim([fmul(x,c) for x in a])
def padd(a,b):
    m=max(len(a),len(b)); return trim([fadd(coeff(a,i),coeff(b,i)) for i in range(m)])
def psub(a,b): return padd(a,trim([fneg(c) for c in b]))
def pmul(a,b):
    out=[ZF]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]=fadd(out[i+j],fmul(x,y))
    return trim(out)
def pdivmod(a,mod):
    a=trim(a); mod=trim(mod); q=[ZF]*max(1,deg(a)-deg(mod)+1); r=a[:]; inv=finv(mod[-1])
    while deg(r)>=deg(mod) and r!=[ZF]:
        sh=deg(r)-deg(mod); c=fmul(r[-1],inv); q[sh]=c
        r=psub(r,[ZF]*sh+pscale(mod,c))
    return trim(q),trim(r)
def residue2(po,E):
    r=pdivmod(po,E)[1]; return (coeff(r,0),coeff(r,1))
def rmul(u,v,E): return residue2(pmul([u[0],u[1]],[v[0],v[1]]),E)
def rsub(u,v): return (fsub(u[0],v[0]),fsub(u[1],v[1]))
def b4(r): return [r[0][0]%P,r[0][1]%P,r[1][0]%P,r[1][1]%P]
def modinv(a): return pow(a%P,P-2,P)
def solve_lin(mat,rhs):
    n=len(rhs); aug=[[x%P for x in mat[i]]+[rhs[i]%P] for i in range(n)]; piv=[]; row=0
    for col in range(n):
        pv=next((r for r in range(row,n) if aug[r][col]%P),None)
        if pv is None: continue
        aug[row],aug[pv]=aug[pv],aug[row]; iv=modinv(aug[row][col])
        aug[row]=[(v*iv)%P for v in aug[row]]
        for r in range(n):
            if r!=row and aug[r][col]%P:
                f=aug[r][col]%P; aug[r]=[(aug[r][c]-f*aug[row][c])%P for c in range(n+1)]
        piv.append(col); row+=1
    return None if len(piv)!=n else [aug[i][-1]%P for i in range(n)]
def det4(mat):
    n=len(mat); a=[[x%P for x in row] for row in mat]; d=1
    for col in range(n):
        pv=next((r for r in range(col,n) if a[r][col]%P),None)
        if pv is None: return 0
        if pv!=col: a[col],a[pv]=a[pv],a[col]; d=(-d)%P
        d=(d*a[col][col])%P; iv=modinv(a[col][col])
        for r in range(col+1,n):
            if a[r][col]%P:
                f=(a[r][col]*iv)%P; a[r]=[(a[r][c]-f*a[col][c])%P for c in range(n)]
    return d%P
# poly-over-F_p helpers for factoring L_tau and the resolvent
def tt(po):
    po=[x%P for x in po]
    while len(po)>1 and po[-1]==0: po.pop()
    return po
def pe(po,x):
    o=0
    for c in reversed(po): o=(o*x+c)%P
    return o
def pdl(po,root):
    co=list(reversed(tt(po))); out=[co[0]]
    for c in co[1:-1]: out.append((c+root*out[-1])%P)
    return tt(list(reversed(out)))
def pdm(a,b):
    a=tt(a); b=tt(b); q=[0]*max(1,len(a)-len(b)+1); r=a[:]; iv=modinv(b[-1])
    while len(r)>=len(b) and r!=[0]:
        sh=len(r)-len(b); c=r[-1]*iv%P; q[sh]=c
        for i,bi in enumerate(b): r[i+sh]=(r[i+sh]-c*bi)%P
        r=tt(r)
    return tt(q),r
def pg(a,b):
    a=tt(a); b=tt(b)
    while b!=[0]: a,b=b,pdm(a,b)[1]
    return [(x*modinv(a[-1]))%P for x in a]
def ftype(tau):
    t1,t2,t3,t4=[x%P for x in tau]; po=[t4,(-t3)%P,t2,(-t1)%P,1]
    dv=[(i*po[i])%P for i in range(1,5)]
    if len(pg(po,dv))>1: return "nonsquarefree"
    degs=[]; rem=po[:]; ch=True
    while ch:
        ch=False
        for r in range(P):
            if len(rem)>1 and pe(rem,r)==0: degs.append(1); rem=pdl(rem,r); ch=True; break
    d=len(tt(rem))-1
    if d==2: degs.append(2)
    elif d==3: degs.append(3)
    elif d==4:
        fq=False
        for a in range(P):
            for b in range(P):
                if pdm(rem,[b,a,1])[1]==[0]: degs.extend([2,2]); fq=True; break
            if fq: break
        if not fq: degs.append(4)
    return "".join(str(x) for x in sorted(degs))
def resolvent_irred(tau):  # cubic R(y); irreducible over F_p iff no root in F_p
    t1,t2,t3,t4=[x%P for x in tau]
    A=(-t2)%P; B=(t1*t3-4*t4)%P; C=(-(t1*t1*t4-4*t2*t4+t3*t3))%P
    return all((((y*y*y)%P+A*y*y+B*y+C)%P)!=0 for y in range(P))
def legendre(a):
    a%=P
    return 0 if a==0 else (1 if pow(a,(P-1)//2,P)==1 else -1)
def disc_quartic(tau):  # disc(L) = disc(resolvent cubic) (same square class as disc_X L)
    t1,t2,t3,t4=[x%P for x in tau]
    A=(-t2)%P; B=(t1*t3-4*t4)%P; C=(-(t1*t1*t4-4*t2*t4+t3*t3))%P
    return (18*A*B*C-4*A*A*A*C+A*A*B*B-4*B*B*B-27*C*C)%P

# ---- explicit family + fixed free data (kappa = u0 != 0) ----
E=[OF,ALPHA,OF]                       # X^2 + alpha X + 1
LD=[ZF]*(P+1); LD[P]=OF; LD[1]=fsub(LD[1],OF)   # X^p - X = prod_{a in F_p}(X-a)
ell=residue2(LD,E)
b_res=(ZF,OF)                         # [X]_E
u=(OF,OF)                             # u=[W]_E = 1 + X  => u0=1 => kappa=1 != 0
w1,w2,w3,w4=(OF,ZF),(ZF,OF),(OF,OF),(OF,ZF)     # W_{n-1..n-4}, fixed free data
def xpow(E,k):
    powers=[]; cur=[OF]; xp=[ZF,OF]
    for _ in range(k+1): powers.append(residue2(cur,E)); cur=pmul(cur,xp)
    return powers
XI=xpow(E,4)
def lam(tau):
    t1,t2,t3,t4=[(x%P,0) for x in tau]
    o=XI[4]
    o=rsub(o,(fmul(t1,XI[3][0]),fmul(t1,XI[3][1])))
    o=(fadd(o[0],fmul(t2,XI[2][0])),fadd(o[1],fmul(t2,XI[2][1])))
    o=rsub(o,(fmul(t3,XI[1][0]),fmul(t3,XI[1][1])))
    return (fadd(o[0],t4),o[1])
def qres(tau):
    t1,t2,t3,_=[(x%P,0) for x in tau]
    q3=w1; q2=fsub(w2,fmul(w1,t1)); q1=fadd(fsub(w3,fmul(w2,t1)),fmul(w1,t2))
    q0=fsub(fadd(fsub(w4,fmul(w3,t1)),fmul(w2,t2)),fmul(w1,t3))
    return residue2([q0,q1,q2,q3],E)
def eqres(z,tau):
    left=rsub(u,(fmul(z,b_res[0]),fmul(z,b_res[1])))   # u - z*[X]_E
    return rsub(rmul(left,lam(tau),E),rmul(ell,qres(tau),E))
def build(z):
    const=b4(eqres(z,[0,0,0,0])); cols=[]
    for i in range(4):
        e=[0,0,0,0]; e[i]=1; v=b4(eqres(z,e)); cols.append([(v[r]-const[r])%P for r in range(4)])
    M=[[cols[c][r] for c in range(4)] for r in range(4)]; rhs=[(-x)%P for x in const]
    return M,rhs

def run(m,e):
    hist={}; singular=0; w4cycle=w13=None; resirr=disc_ns=None
    for z0 in range(P):
        z1=(m*z0+e)%P; z=(z0%P,z1%P)
        M,rhs=build(z)
        if det4(M)==0: singular+=1; continue
        tau=solve_lin(M,rhs)
        if tau is None: singular+=1; continue
        ft=ftype(tau); hist[ft]=hist.get(ft,0)+1
        if ft=="4":
            w4cycle=w4cycle or z
            if legendre(disc_quartic(tau))==-1: disc_ns=disc_ns or z
        if ft=="13":
            w13=w13 or z
            if resolvent_irred(tau): resirr=resirr or z
    passed=("4" in hist) and ("13" in hist)
    return {"p":P,"q_gen":P,"q_line":P*P,"NR":NR,"family":"E=X^2+alphaX+1,b=X,nr=-1",
            "free_data":{"u":"1+X (kappa=u0=1)","W_{n-1..n-4}":"(1),(alpha),(1+alpha),(1)"},
            "line":{"m":m,"e":e},"singular_on_line":singular,"hist":dict(sorted(hist.items())),
            "witness_4cycle":w4cycle,"witness_13":w13,"resolvent_irred_at":resirr,
            "disc_nonsquare_at":disc_ns,"PASS_S4_finite_place":passed}

if __name__=="__main__":
    best=None
    for e in range(P):
        for m in range(1,P):
            r=run(m,e)
            if r["PASS_S4_finite_place"]: best=r; break
        if best: break
    out=best if best else run(1,0)
    print(json.dumps(out,indent=2))
```

The driver scans candidate lines `(m,e)` deterministically and reports the first that satisfies the `"4"`+`"13"` PASS condition, emitting a machine-checkable JSON certificate (family, fixed free data with `kappa=1`, the line, the off-`Δ` histogram, the 4-cycle and 3-cycle witnesses, plus a disc-nonsquare place and a resolvent-irreducible place as corroboration).

## Classification

`EXPERIMENTAL / AUDIT` — this is a complete, deterministic checker **specification, unrun in this harness** (file-write and execution were both denied, so I cannot and do not assert that `"4"` and `"13"` appear for `p=31` with this exact free data). I therefore do **not** bank `BANKABLE_LEMMA` / `PROOF` for the single-prime certificate.

What is hand-verified and consistent with banked lemmas (carries independent of the run): the source-validity gates (no `F_p` root, `τ`-separation, `c_b≠0`), the explicit `kappa=u0=1≠0` choice, the top-symbol nonvanishing `Q_4=N(c_b)≠0`, and the `≤4p` singular bound. The corrected `S_4` criterion is enforced (transitivity via the 4-cycle, not the forbidden shortcut). Conditional reading: **if** an operator runs the script and the JSON shows `PASS_S4_finite_place: true`, that output is a per-instance bankable local certificate `G_geom=G_arith=S_4` for the `p=31` instance — a `CONDITIONAL COUNTERPACKET seed`, never an MCA/protocol/prize object, and never a `q_gen`/`q_line` merge.

Recorded exclusions/gates: singular determinant locus `Δ(z₀,z₁)=0` (skipped on the line, `O(p)`); non-squarefree quartic specializations (recorded as `nonsquarefree`, excluded from cycle-type evidence); ramified/bad places; the source-validity branch hypotheses (`E` separated, no `F_p` root, `c_b≠0`, `kappa≠0`); and the per-instance (not uniform-in-`p`) scope.

## Do you see a route to a full solve?

Not to a *full* prize-level solve from here — and the route board's separations forbid promoting any of this past a restricted local `t=2, j=4` sub-reserve object. But there is a clear route to the next genuine milestone, the uniform family (`W-F1-AA-RES-T2J4-A2B-UNIFORM-S4`), in two exact steps:

1. **Single-prime confirmation (this cycle, pending execution).** Run the checker above; if PASS, the `p=31` instance has geometric `S_4`. Next exact lemma to attempt: a *symbolic* (not finite-place) certificate over `\bar F_p(z₀,z₁)` — compute `disc_num(z₀,z₁)` and the resolvent `R(y)` as exact bivariate polynomials from `τ_i=det M_i/Δ`, and prove (a) `disc_num` has nonconstant squarefree part and (b) `R(y)` is absolutely irreducible, together with one explicit `"4"` slice for transitivity. That removes the dependence on a finite scan at the single prime.

2. **Good-reduction promotion (the actual remaining hard lemma).** State and prove `L-T2J4-A2B-GOODRED`: the `disc_num` squarefree-part-nonconstant and resolvent-absolute-irreducibility conditions are good-reduction-open in the `p≡3 mod 4` family, so a single good prime promotes `G_geom=S_4` to all but finitely many primes (with the excluded-prime set recorded). Combined with a restricted Lang–Weil/Chebotarev count of complexity bounded uniformly in `p`, this would upgrade the conditional seed to a genuine growing-prime `C2 = p²/24 + O(p^{3/2}) = Θ(q_line)` restricted counterpacket seed.

The honest obstruction ranking for step 2, in order of risk: (i) a hidden forced square factor in `disc_num` peculiar to this `E=X²+αX+1, b=X` family (would be `ROUTE_CUT`); (ii) constant-field drift across the family (already cut *conditional on* geometric `S_4`, but must be re-checked uniformly); (iii) uniform complexity control of the Lang–Weil error, which is where a `Θ(p²)` claim could still collapse to an `O(p^{3/2})` error swamping the main term for the relevant prime range. Step 1's symbolic certificate is the cheap, high-information next action and should be run first.
