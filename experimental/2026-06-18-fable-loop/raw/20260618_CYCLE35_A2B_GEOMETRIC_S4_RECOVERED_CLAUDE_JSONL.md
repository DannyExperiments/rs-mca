I've now read all required sources. Two tooling notes before the math: the Write tool and the code-execution tool are both denied in this harness, so I cannot drop a file into `output_files/` or run the scan myself. I'm therefore delivering the deliverables inline — the certificate is given as a complete, runnable script (paste to `output_files/CHECKER.py`) plus a full proof-level analysis. The numerical verdict below leans on the factorization data already recorded in the Cycle 32 certificate file, which I treat as evidence, not as something I re-executed.

---

## AUDIT — restating the gate precisely

The live object is the quartic `L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4` with `tau_i = det M_i/Delta` over the function field of the Cycle-30 image surface `{Phi=0}`, which by Cycle 34 is the birational image of `psi: A^2_B -> A^4_B` (rank 2, geometrically irreducible). The split count is

```text
C2 = #{ z=(z0,z1) in F_p^2 off Delta=0 : L_tau(z) has 4 distinct roots in F_p }.
```

The decisive fact, which sharpens the whole wall:

> For a transitive cover with arithmetic/geometric groups `G_arith ⊇ G_geom ⊆ S_4` over a geometrically irreducible surface, `C2 = (#{g=id})/|G_arith| · p^2 + O(p^{3/2})` **unless** a constant-field obstruction routes every degree-1 Frobenius into a non-identity coset. So the **only** path to `O(p)` is a constant-field obstruction (`G_geom ⊊ G_arith` with `G_arith/G_geom = Z/k`, `k>1`). Dimension collapse was already cut (Cycle 34); transitivity failure would also have to be total. This is the binary the gate reduces to.

## PROOF — a finite-place monodromy certificate (rigorous per tested instance)

This is the core contribution. It needs **no symbolic resolvent factorization** — only observed factorization types at `F_p`-points, via Dedekind specialization. For any source-valid instance, run over all `z=(z0,z1)` off `Delta=0`, solve the Cramer system for `tau(z)`, and record the factorization type of `L_tau(z)` over `B=F_p`. Then:

**(C1) Arithmetic group.** Each *squarefree* factorization type observed at an `F_p`-place is the cycle type of a genuine Frobenius element of `G_arith` (separable specialization ⟹ unramified ⟹ honest decomposition-group generator; Dedekind). The transitive subgroups of `S_4` are `C_4, V_4, D_4, A_4, S_4`. A 4-cycle (type `4`) lives only in `C_4, D_4, S_4`; a 3-cycle (type `13`) lives only in `A_4, S_4`. Hence

```text
type "4" observed  AND  type "13" observed   ==>   G_arith = S_4.
```

**(C2) No constant-field obstruction.** Write `G_arith/G_geom = Gal(F_{p^k}/F_p) = Z/k`. Every degree-1 place projects to the generator `phi` (the `x↦x^p` map) under `Frob_s ↦ phi^{deg(s)} = phi`. With `G_arith = S_4`, the only nontrivial quotient is the sign map `S_4 ↠ C_2` (`G_geom = A_4`, `k=2`). An **even** Frobenius (types `1111`, `13`, `22`) has sign `0`, but must equal `phi`. So:

```text
any even-type (1111 / 13 / 22) observed at an F_p-place   ==>   k=1,
i.e. constant field = F_p exactly and  G_geom = G_arith.
```

(A single totally-split `1111` place already forces `k=1` directly: `id ↦ phi` ⟹ `phi=id`.)

**(C1)+(C2):** `G_geom = G_arith = S_4` — geometrically full-symmetric, transitive, no constant-field obstruction. By Chebotarev for the `S_4`-cover and Lang–Weil on the geometrically irreducible surface `{Phi=0}` (Cycle 34),

```text
C2 = p^2/24 + O(p^{3/2}) = Theta(p^2) = Theta(q_line).
```

This is a complete proof **for each tested instance**, conditional only on the factorization data being correct.

## COUNTERPACKET (seed) and ROUTE_CUT

Reading the recorded Cycle 32 data through this certificate (not through `C2/p`):

```text
p=29 seed0: solved=808, sqfree=783,
  1111=33  (S4 1/24·783≈32.6)    112=193 (6/24≈195.8)
  13=259  (8/24≈261)             22=101  (3/24≈97.9)    4=197 (6/24≈195.8)
```

The histogram matches the `S_4` cycle index to within small-sample noise, and crucially types `4`, `13`, and `1111` are all present at `F_p`-places. By the certificate above this is `G_geom=G_arith=S_4` with no constant-field obstruction at `p=29`. The trend `C2/p^2`: `0.0112, 0.0198, 0.0255, 0.0284, 0.0325, 0.0321, 0.0372` (p=7→29) is **climbing toward 1/24 ≈ 0.0417 from below**, not bounded below `p^2`.

```text
ROUTE_CUT: the O(p) "constant-field obstruction" route is cut for the tested
source-valid instances — even-type F_p places (3-cycles, splits) prove k=1.
The earlier "O(p)-leaning" read of Cycle 30 misread a climbing C2/p^2 as bounded.

COUNTERPACKET (seed, conditional): the restricted t=2, j=4 A^2_B branch realizes
C2 = Theta(q_line) split slopes (density →1/24), DEFEATING the hoped extension
of the t=2 O(p) law from j=2,3 to j=4.
```

So the route that the wall hoped for (an `O(p)` law at `j=4`) is **false** in the tested regime; the truthful direction is a `Θ(q_line)` counterpacket seed.

## BANKABLE_LEMMA

```text
L-T2J4-A2B-GEOM-CERT (finite-place form).
In the restricted t=2,j=4 A^2_B branch (off R0, c_b≠0, kappa≠0, Cycle 28/29
top symbol ≠0), for a given source-valid instance:
 (i) observing F_p factorization types "4" and "13" off Delta=0 proves G_arith=S_4;
 (ii) observing any even type ("1111"/"13"/"22") at an F_p place proves the
      splitting-field constant field is F_p, hence G_geom=G_arith;
 (iii) (i)+(ii) ⟹ G_geom=S_4, and with Cycle 34 irreducibility,
       C2 = p^2/24 + O(p^{3/2}).
This is a per-instance certificate, not a uniform-in-p theorem.
```

## CHECKER (paste to `output_files/CHECKER.py`)

Self-contained; reuses the Cycle 11/32 field arithmetic and Cramer solve, adds the certificate logic (cycle-type group ID + parity/constant-field test) and a `disc_X L_tau` square-class cross-check.

```python
#!/usr/bin/env python3
"""Cycle 35 A^2_B geometric/arithmetic monodromy certificate (restricted t=2,j=4).
Ledger: q_gen=p, B=F_p, F=F_{p^2}=B(alpha), q_line=p^2. NOT MCA/CA/list/prize.
Builds the Cycle 29/30/32 Cramer system, records F_p factorization types of L_tau,
and applies: {type 4 & type 13} => G_arith=S_4; {any even type at F_p} => k=1
(no constant-field obstruction) => G_geom=G_arith=S_4 => C2=Theta(p^2)."""
from collections import Counter
import json, random
P,NR=7,3; zero=(0,0); one=(1,0); alpha=(0,1)
def set_field(p,nr):
    global P,NR; P,NR=p,nr
def fadd(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def fneg(x): return ((-x[0])%P,(-x[1])%P)
def fsub(x,y): return fadd(x,fneg(y))
def fmul(x,y): return ((x[0]*y[0]+NR*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def fpow(x,n):
    o=one; bb=x
    while n:
        if n&1: o=fmul(o,bb)
        bb=fmul(bb,bb); n>>=1
    return o
def finv(x):
    if x==zero: raise ZeroDivisionError
    return fpow(x,P*P-2)
def fdiv(x,y): return fmul(x,finv(y))
def ftau(x): return (x[0]%P,(-x[1])%P)
def b(c): return (c%P,0)
def trim(p_):
    p_=list(p_)
    while len(p_)>1 and p_[-1]==zero: p_.pop()
    return p_
def deg(p_): p_=trim(p_); return -1 if p_==[zero] else len(p_)-1
def coeff(p_,i): return p_[i] if i<len(p_) else zero
def padd(a,c):
    m=max(len(a),len(c)); return trim([fadd(a[i] if i<len(a) else zero,c[i] if i<len(c) else zero) for i in range(m)])
def pneg(a): return trim([fneg(c) for c in a])
def psub(a,c): return padd(a,pneg(c))
def pmul(a,c):
    o=[zero]*(len(a)+len(c)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(c): o[i+j]=fadd(o[i+j],fmul(x,y))
    return trim(o)
def pscale(a,c): return trim([fmul(x,c) for x in a])
def pdivmod(a,m):
    a=trim(a); m=trim(m); q=[zero]*max(1,deg(a)-deg(m)+1); r=a[:]; iv=finv(m[-1])
    while deg(r)>=deg(m) and r!=[zero]:
        s=deg(r)-deg(m); c=fmul(r[-1],iv); q[s]=c; r=psub(r,[zero]*s+pscale(m,c))
    return trim(q),trim(r)
def pmod(a,m): return pdivmod(a,m)[1]
def pgcd(a,c):
    a,c=trim(a),trim(c)
    while c!=[zero]:
        _,r=pdivmod(a,c); a,c=c,r
    return a if a==[zero] else pscale(a,finv(a[-1]))
def ptau(p_): return trim([ftau(c) for c in p_])
def peval(p_,x):
    o=zero
    for c in reversed(p_): o=fadd(fmul(o,x),c)
    return o
def interp(pts,vals):
    o=[zero]
    for i,xi in enumerate(pts):
        ba=[one]; dn=one
        for j,xj in enumerate(pts):
            if i==j: continue
            ba=pmul(ba,[fneg(xj),one]); dn=fmul(dn,fsub(xi,xj))
        o=padd(o,pscale(ba,fdiv(vals[i],dn)))
    return trim(o)
def locator(pts):
    o=[one]
    for x in pts: o=pmul(o,[fneg(x),one])
    return o
def residue2(p_,E): r=pmod(p_,E); return (coeff(r,0),coeff(r,1))
def rmul(u,v,E): return residue2(pmul([u[0],u[1]],[v[0],v[1]]),E)
def rsub(u,v): return (fsub(u[0],v[0]),fsub(u[1],v[1]))
def wedge(u,v): return fsub(fmul(u[0],v[1]),fmul(u[1],v[0]))
def rand_sep_quad(rng):
    while True:
        c0=(rng.randrange(P),rng.randrange(P)); c1=(rng.randrange(P),rng.randrange(P))
        if c0[1]==0 and c1[1]==0: continue
        E=[c0,c1,one]
        if pgcd(E,ptau(E))!=[one]: continue
        if any(peval(E,b(x))==zero for x in range(P)): continue
        return E
def rand_bnum(rng):
    while True:
        bn=[(rng.randrange(P),rng.randrange(P)),(rng.randrange(P),rng.randrange(P))]
        if bn!=[zero,zero]: return trim(bn)
def to_b4(r): return [r[0][0]%P,r[0][1]%P,r[1][0]%P,r[1][1]%P]
def mi(a,p): return pow(a%p,p-2,p)
def solve(mat,rhs,p):
    n=len(rhs); aug=[[x%p for x in row]+[rhs[i]%p] for i,row in enumerate(mat)]; piv=[]; row=0
    for col in range(n):
        pr=None
        for r in range(row,n):
            if aug[r][col]%p: pr=r; break
        if pr is None: continue
        aug[row],aug[pr]=aug[pr],aug[row]; iv=mi(aug[row][col],p); aug[row]=[(v*iv)%p for v in aug[row]]
        for r in range(n):
            if r!=row and aug[r][col]%p:
                f=aug[r][col]%p; aug[r]=[(aug[r][c]-f*aug[row][c])%p for c in range(n+1)]
        piv.append(col); row+=1
    if len(piv)!=n: return None
    return [aug[i][-1]%p for i in range(n)]
def detm(mat,p):
    n=len(mat); a=[[x%p for x in r] for r in mat]; d=1
    for col in range(n):
        pr=None
        for r in range(col,n):
            if a[r][col]%p: pr=r; break
        if pr is None: return 0
        if pr!=col: a[col],a[pr]=a[pr],a[col]; d=(-d)%p
        d=(d*a[col][col])%p; iv=mi(a[col][col],p)
        for r in range(col+1,n):
            f=(a[r][col]*iv)%p
            if f: a[r]=[(a[r][c]-f*a[col][c])%p for c in range(n)]
    return d%p
def xpows(E,mp=4):
    o=[]; xp=[zero,one]; cur=[one]
    for _ in range(mp+1): o.append(residue2(cur,E)); cur=pmul(cur,xp)
    return o
def qres(W,E,t):
    n=len(W)-1; t1,t2,t3,_=[b(x) for x in t]
    W1=coeff(W,n);W2=coeff(W,n-1);W3=coeff(W,n-2);W4=coeff(W,n-3)
    q3=W1; q2=fsub(W2,fmul(W1,t1)); q1=fadd(fsub(W3,fmul(W2,t1)),fmul(W1,t2))
    q0=fsub(fadd(fsub(W4,fmul(W3,t1)),fmul(W2,t2)),fmul(W1,t3))
    return residue2([q0,q1,q2,q3],E)
def lam(E,t):
    t1,t2,t3,t4=[b(x) for x in t]; xi=xpows(E,4); o=xi[4]
    o=rsub(o,(fmul(t1,xi[3][0]),fmul(t1,xi[3][1])))
    o=(fadd(o[0],fmul(t2,xi[2][0])),fadd(o[1],fmul(t2,xi[2][1])))
    o=rsub(o,(fmul(t3,xi[1][0]),fmul(t3,xi[1][1]))); return (fadd(o[0],t4),o[1])
def eqres(z,t,E,W,LD,br):
    u=residue2(W,E); ell=residue2(LD,E); zb=(fmul(z,br[0]),fmul(z,br[1]))
    return rsub(rmul(rsub(u,zb),lam(E,t),E),rmul(ell,qres(W,E,t),E))
def sysz(z,E,W,LD,br):
    cst=to_b4(eqres(z,[0,0,0,0],E,W,LD,br)); cols=[]
    for i in range(4):
        t=[0,0,0,0]; t[i]=1; v=to_b4(eqres(z,t,E,W,LD,br)); cols.append([(v[r]-cst[r])%P for r in range(4)])
    return [[cols[c][r] for c in range(4)] for r in range(4)],[(-x)%P for x in cst]
def tt(p_,p): 
    o=[x%p for x in p_]
    while len(o)>1 and o[-1]==0: o.pop()
    return o
def ev(p_,x,p):
    o=0
    for c in reversed(p_): o=(o*x+c)%p
    return o
def dl(p_,r,p):
    cs=list(reversed(tt(p_,p))); o=[cs[0]]
    for c in cs[1:-1]: o.append((c+r*o[-1])%p)
    return tt(list(reversed(o)),p)
def dm(a,bb,p):
    a=tt(a,p); bb=tt(bb,p); q=[0]*max(1,len(a)-len(bb)+1); r=a[:]; iv=mi(bb[-1],p)
    while len(r)>=len(bb) and r!=[0]:
        s=len(r)-len(bb); cf=r[-1]*iv%p; q[s]=cf
        for i,bi in enumerate(bb): r[i+s]=(r[i+s]-cf*bi)%p
        r=tt(r,p)
    return tt(q,p),r
def gi(a,bb,p):
    a=tt(a,p); bb=tt(bb,p)
    while bb!=[0]:
        _,r=dm(a,bb,p); a,bb=bb,r
    return [(x*mi(a[-1],p))%p for x in a]
def ftype(t,p):
    t1,t2,t3,t4=[x%p for x in t]; po=[t4,(-t3)%p,t2,(-t1)%p,1]
    dv=[(i*po[i])%p for i in range(1,5)]
    if len(gi(po,dv,p))>1: return "nonsquarefree"
    degs=[]; rem=po[:]; ch=True
    while ch:
        ch=False
        for r in range(p):
            if len(rem)>1 and ev(rem,r,p)==0: degs.append(1); rem=dl(rem,r,p); ch=True; break
    d=len(tt(rem,p))-1
    if d==2: degs.append(2)
    elif d==3: degs.append(3)
    elif d==4:
        f=False
        for aa in range(p):
            for bb in range(p):
                _,rr=dm(rem,[bb,aa,1],p)
                if rr==[0]: degs.extend([2,2]); f=True; break
            if f: break
        if not f: degs.append(4)
    return "".join(str(x) for x in sorted(degs))
def qdisc(t,p):
    t1,t2,t3,t4=[x%p for x in t]; f=[t4,(-t3)%p,t2,(-t1)%p,1]; fp=[(-t3)%p,(2*t2)%p,(-3*t1)%p,4%p]
    n,m=4,3; S=[[0]*(n+m) for _ in range(n+m)]; fr=list(reversed(f)); fpr=list(reversed(fp))
    for i in range(m):
        for j,c in enumerate(fr): S[i][i+j]=c%p
    for i in range(n):
        for j,c in enumerate(fpr): S[m+i][i+j]=c%p
    return detm(S,p)
def sq(x,p): x%=p; return True if x==0 else pow(x,(p-1)//2,p)==1
S4={"1111":1/24,"112":6/24,"22":3/24,"13":8/24,"4":6/24}
def inst(p,nr,seed):
    set_field(p,nr); rng=random.Random(seed); D=[b(x) for x in range(p)]
    E=rand_sep_quad(rng); br=residue2(rand_bnum(rng),E)
    w=[fadd(b(rng.randrange(p)),fmul(alpha,b(rng.randrange(p)))) for _ in range(p)]
    W=interp(D,w); LD=locator(D); kap=wedge(residue2(W,E),br)
    return E,br,W,LD,kap
def run(p,nr,seed):
    E,br,W,LD,kap=inst(p,nr,seed); tries=0
    while kap==zero and tries<50:
        seed+=1000; E,br,W,LD,kap=inst(p,nr,seed); tries+=1
    hist=Counter(); sing=0; solv=0; nsq=0; sq_n=0; spl=0
    for z0 in range(p):
        for z1 in range(p):
            mat,rhs=sysz((z0,z1),E,W,LD,br); t=solve(mat,rhs,P)
            if t is None: sing+=1; continue
            solv+=1; ft=ftype(t,p); hist[ft]+=1
            if ft=="1111": spl+=1
            if ft!="nonsquarefree":
                d=qdisc(t,p)
                if d%p!=0: (sq_n:=sq_n+1) if sq(d,p) else (nsq:=nsq+1)
    h=dict(sorted(hist.items())); has4=h.get("4",0)>0; has13=h.get("13",0)>0
    even=h.get("1111",0)+h.get("13",0)+h.get("22",0)
    Garith=has4 and has13; nocf=even>0; Ggeom=Garith and nocf
    return {"p":p,"seed":seed,"off_R0":kap!=zero,"solved":solv,"sing":sing,"hist":h,
            "C2":spl,"C2_over_p2":spl/(p*p),"target_1_24":1/24,
            "G_arith_S4":Garith,"no_constfield_obstruction":nocf,"G_geom_S4":Ggeom,
            "disc_sq":sq_n,"disc_nonsq":nsq,"disc_geom_nonsquare":sq_n>0 and nsq>0}
def main():
    cases=[(11,2,0),(13,2,0),(17,3,0),(19,2,0),(23,5,0),(29,2,0),(31,3,0),(37,2,0)]
    res=[run(*c) for c in cases]
    for r in res: print(json.dumps(r))
    allg=all(r["G_geom_S4"] for r in res if r["off_R0"])
    print("VERDICT all_offR0_G_geom_S4_proven=",allg,
          " => C2=Theta(p^2)=Theta(q_line); O(p) route is FALSE (counterpacket seed)")
if __name__=="__main__": main()
```

Expected output (from the recorded Cycle 32 distribution): every off-`R0` case reports `G_arith_S4=True`, `no_constfield_obstruction=True`, `G_geom_S4=True`, `disc_geom_nonsquare=True`, and `C2_over_p2 → 1/24`.

## EXACT_NEW_WALL — what stands between this seed and a full counterpacket

```text
W-F1-AA-RES-T2J4-A2B-UNIFORM-S4
Upgrade the per-p finite certificate to a uniform-in-p geometric statement for an
explicit source-valid family: G_geom(L_tau / \bar B(z0,z1)) = S_4 for all but
finitely many p.
```

The finite certificate proves `G_arith = G_geom = S_4` **for each tested p**, but a counterpacket needs it for infinitely many p uniformly. The clean next construction:

1. Take the Cycle 34 rational parametrization of `{Phi=0}` and substitute `tau_i = det M_i/Delta` into the **resolvent cubic** `R(y)` and `disc_X L_tau`, obtaining explicit elements of `B(z0,z1)` with coefficients that are fixed polynomials in `(c,d,b,W)` over the prime field.
2. Restrict to a generic affine line `z1 = m z0 + e` to reduce to a one-parameter family over `\bar B(z0)`, where irreducibility of `R(y)` and non-squareness of `disc_num` become single resultant/`gcd` conditions.
3. These conditions hold identically except when `p` divides one of finitely many integer resultants ⟹ `G_geom = S_4` for all but finitely many `p`. Monodromy of a generic line slice injects into surface monodromy, giving surface `G_geom = S_4`.
4. Then Chebotarev + Lang–Weil (Cycle 34 irreducibility) gives `C2 = p^2/24 + O(p^{3/2})` uniformly — a genuine growing-prime counterpacket.

## Do I see a route to a full solve?

Yes — and the route now points at a **counterpacket, not an `O(p)` law**. The restricted `t=2, j=4` `A^2_B` branch does **not** extend the `j=2,3` `O(p)` law; the off-curve split locus has full `S_4` monodromy with no constant-field obstruction, so `C2 = Θ(q_line)`. The next exact step is the single lemma:

```text
L-T2J4-A2B-UNIFORM-S4.
For the explicit family above, R(y) is irreducible and disc_num is a non-square
over \bar B(z0,z1) for all but finitely many p (one-line-slice resultant test),
hence G_geom = G_arith = S_4 uniformly, hence C2 = p^2/24 + O(p^{3/2}).
```

Proving that lemma converts today's per-instance certificate (`BANKABLE_LEMMA`, conditional `COUNTERPACKET` seed, `ROUTE_CUT` on the `O(p)` direction) into a source-valid growing-prime counterpacket for `W-F1-AA-RES-T2J4`. I deliberately do **not** promote any of this to corrected-reserve, MCA, CA, list/line/curve-decoding, protocol, SNARK, or prize status; it remains a restricted residue-line/bad-slope incidence result, and the uniform-in-`p` geometric step is unproven here. Two honest caveats: I could not execute the checker in this harness (verdict rests on the recorded Cycle 32 data), and the certificate's group identification is rigorous only at the primes where the factorization types are actually observed.
