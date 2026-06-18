I've completed the derivation and verified it by hand against the banked Cycle 23 identity. Code execution and file writing are denied in this harness (same constraint Cycles 19–23 recorded), so I deliver the analytic audit inline with a copy-pasteable checker, and every load-bearing identity is re-derived from the banked Cycle 12/14/20/21 multiplication table.

---

## Primary label

```text
BANKABLE_LEMMA + ROUTE_CUT
```

The nonsplit-`c` D-kernel lane `W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C` is **empty** under its own hypotheses. The result also unifies Cycle 23 into one basis-free identity.

## Headline

Off `R0` (`kappa = u wedge b != 0`), in the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3` window,

```text
D = N(ell) * kappa,     N(ell) = prod_{a in F_p} E(a),
```

where `N` is the norm (determinant of multiplication) on `A=F[X]/E`. Hence `D=0` off `R0` happens **iff `E` has a root in `B=F_p`**, which is exactly the condition that `E` is **not** separated. The wall hypothesis "`E` separated" therefore makes the stratum empty — regardless of `c in B` or `c notin B`.

## Setup (source-checked, off `R0`)

```text
E=X^2+cX+d,  A=F[X]/E,  xi=[X]_E,  xi^2=-c xi-d,
u=[W]_E,  b=[Bnum]_E,  ell=[X^p-X]_E=[L_D]_E   (D=F_p, so L_D=X^p-X),
kappa=u wedge b,
x wedge y = x0 y1 - x1 y0,
P_E(x,y) = x0 y0 - c x0 y1 + d x1 y1.
```

The conjugate of `y=y0+y1 xi` over `F` is `ybar=(y0-c y1)-y1 xi` (root swap `xi -> xi^*=-c-xi`). The master identity, verified by direct expansion using `xi^2=-c xi-d`:

```text
x * ybar = P_E(x,y) - (x wedge y) xi.            (MASTER)
```

## Q1 — closed form of `ell` for `c notin B`

Put `s := xi + c/2` (note `c/2 in F`, so this is legal whether or not `c in B`). Then `s^2 = c^2/4 - d =: w in F`. Two routes to `s^p` must agree in `A`:

```text
freshman:    s^p = (xi+c/2)^p = xi^p + (c/2)^p = (xi+ell) + c^p/2,
scalar pow:  s^p = (s^2)^((p-1)/2) s = w^((p-1)/2) s = nu s,   nu:=w^((p-1)/2).
```

Equating and solving for `ell` (with `mu := nu - 1`):

```text
ell = mu*s + (c - c^p)/2 = mu*(xi + c/2) + delta_c,
delta_c := (c - c^p)/2 = (c - c^tau)/2.
```

In coordinates on `{1,xi}`, `s=(c/2,1)`, so

```text
ell = ( mu*c/2 + delta_c , mu ),     i.e.  ell0=(nu c - c^p)/2,  ell1=mu.
```

`delta_c` is the imaginary part of `c`; it vanishes exactly when `c in B`, recovering the banked Cycle 23 form `ell = mu*s`. So the only new term in the nonsplit-`c` lane is the additive Frobenius-defect `delta_c`.

## Q2 — `D` as a bilinear form

Apply (MASTER) with `z=ellbar`: write `u*ellbar=P+Q xi` and `b*ellbar=R+S xi` where `P=P_E(u,ell)`, `Q=-(u wedge ell)`, `R=P_E(b,ell)`, `S=-(b wedge ell)`. Then

```text
D = (ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell) = SP - RQ = (u*ellbar) wedge (b*ellbar).
```

Since `wedge` is an alternating `F`-bilinear 2-form on the rank-2 module `A`, any `F`-linear map `T` scales it by `det T`; multiplication by `ellbar` has `det = N(ellbar)=N(ell)`. Therefore

```text
D = N(ellbar) (u wedge b) = N(ell)*kappa,      N(ell)=P_E(ell,ell)=ell0^2 - c ell0 ell1 + d ell1^2.
```

All `(u,b)`-dependence sits in `kappa`; the `(c,d)`-dependence is the scalar `N(ell)`. Polarizing `N` at `ell = mu*s + delta_c*1` (the cross term `B(s,1)=c/2 - c/2 = 0` drops out) gives the explicit gate scalar

```text
N(ell) = delta_c^2 - mu^2 w,     w=c^2/4-d.        (LAMBDA)
```

For `c in B`, `delta_c=0` and `N(ell)=-mu^2 w = -mu^2(c^2/4-d)`, so `D=-mu^2(c^2/4-d)kappa` — **exactly** the banked Cycle 23 identity, now obtained as a special case.

The norm-as-resultant form is the decisive one. Since `ell = prod_{a in F_p}[X-a]_E` and `N` is multiplicative, `N([X-a]_E)=E(a)`, so

```text
N(ell) = prod_{a in F_p} E(a).        (RES)
```

(Cross-check of (LAMBDA)=(RES) for `c in B`: `prod_{a}(a^2+ca+d)=prod_{t in F_p}(t^2-w) = -(beta-beta^p)^2 = -w(w^{(p-1)/2}-1)^2 = -mu^2 w`. Matches.)

## Q3 — joint solvability of `{D=0, Delta1==0, off R0, c notin B}`

**Not solvable when `E` is separated; the stratum is empty.**

From (RES), off `R0`:

```text
D=0  <=>  N(ell)=0  <=>  prod_{a in F_p} E(a)=0  <=>  E has a root a in B=F_p.
```

If `E(a)=0` with `a in F_p`, then `a^p=a` and `E^tau(a)=E^tau(a^p)=E(a)^p=0`, so `(X-a) | gcd(E,E^tau)` and `E` is **not** separated. Contrapositive:

```text
E separated  ==>  E has no root in F_p  ==>  N(ell) != 0  ==>  D != 0   (off R0).
```

So `{D=0, off R0, E separated}` is empty, and a fortiori its `c notin B` slice is empty. The auxiliary conditions `Delta1==0`, `c_b=-Q_E(b)/kappa != 0`, `W_{n-1} != 0` are never reached — emptiness is forced by `D=0 + separated + off R0` alone.

Within the `c notin B` lane this is sharp: for `c notin B`, a shared root of `E,E^tau` is forced into `F_p` (otherwise the shared root and its Frobenius image would form a full Galois orbit, putting `E^tau`, hence `c,d`, in `B[X]` — contradicting `c notin B`). Thus on `c notin B`:

```text
D=0  (off R0)   <=>   E not separated   <=>   E has a root in F_p.
```

The D-kernel `D=0` locus in the nonsplit-`c` lane is exactly the non-separated locus the wall excludes.

## Q4 — split-cubic slope set on this lane

Vacuous. Because `{D=0, off R0, E separated, c notin B}` has no source-valid point, there is no co-support family to count: the `O(p)` vs `Omega(p^2)=Omega(q_line)` dichotomy does not arise on this lane and **no `Theta(q_line)` counterpacket can be seeded here**. Off the `D=0` lane (`D!=0`), the controlling invariant reverts to the Cycle 16 determinant `Q(z_0,z_1)`, not `D`; `D` contributes no new danger.

## Net banked implication

```text
Off R0, restricted D=F_p, t=sigma=2, j=3:
  D = N(ell)*kappa,  N(ell)=prod_{a in F_p}E(a)=delta_c^2-mu^2 w,
  ell = mu*(xi+c/2)+delta_c,  mu=w^{(p-1)/2}-1,  w=c^2/4-d,  delta_c=(c-c^p)/2.
  E separated  ==>  D!=0  ==>  {D=0,off R0,E separated} empty, incl. c notin B.
```

This closes `W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C` as `ROUTE_CUT` and supersedes the Cycle 23 `c in B` emptiness as a corollary of one identity.

## Banked vs not

Bank (proven, exact, off `R0`, restricted window): (MASTER); the basis-free `D=N(ell)*kappa`; the closed form `ell=mu*(xi+c/2)+delta_c`; the gate scalar `N(ell)=delta_c^2-mu^2 w`; the resultant form `N(ell)=prod_{a in F_p}E(a)`; the equivalence `D=0 off R0 <=> E has a root in F_p <=> E not separated`; emptiness of `{D=0,off R0,E separated}` and its `c notin B` slice.

Do **not** bank: any nonemptiness or split-count statement for a `c notin B` lane (none survives); any `C2` bound for the full `D=0` branch beyond this window; any `Theta(q_line)` counterpacket; any corrected-reserve, `q_gen`, protocol, list-/line-/curve-decoding, CA, MCA, or SNARK consequence. The recovered `Delta1==0` landing criterion `delta_z in QR(F_p)` is still not banked.

## Forbidden-upgrade compliance

No Prize solve/disproof; `eta=2/n` stays sub-reserve; `q_gen`/`q_line` kept separate; no protocol denominator saving; no list/line/CA/MCA/SNARK upgrade; no internet; no finite scan cited as proof.

## New live wall

With both `c in B` (Cycle 23) and `c notin B` (this cycle) D-kernel lanes cut, the surviving `D=0` route is gone for separated `E`. The off-`R0` separated wall returns to the Cycle 16 line:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT  (Q==0 branch, distinct D-split cubics retained).
```

Since separated `E` forces `D!=0`, the rank/determinant analysis must proceed via `Q(z_0,z_1)` with `det M = (c_b/kappa^2)D != 0`; the next exact task is whether `Q==0` is compatible with `det M != 0` on source-valid distinct-split data, or whether that too collapses to `O(p)`.

## Checker (harness denied Write/execute — copy to `output_files/CHECKER.py`)

Experimental consistency harness only, not a proof.

```python
#!/usr/bin/env python3
"""Cycle 24: W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C consistency checker (NOT a proof).
Verifies, for B=F_p, F=F_{p^2}, A=F[X]/(X^2+cX+d):
  (1) ell=[X^p-X]_E = mu*(xi+c/2)+delta_c,  mu=w^((p-1)/2)-1, w=c^2/4-d, delta_c=(c-c^p)/2;
  (2) D=(ell^b)P_E(u,ell)+P_E(b,ell)(u^ell) = N(ell)*kappa;
  (3) N(ell)=prod_{a in F_p} E(a) = delta_c^2 - mu^2 w;
  (4) E separated (gcd(E,E^tau)=1) and kappa!=0  =>  D!=0  (stratum empty),
      and D=0 off R0 occurs only where E has a root in F_p (non-separated).
"""
from __future__ import annotations

def find_nonresidue(p):
    sq={(i*i)%p for i in range(p)}
    for a in range(2,p):
        if a not in sq: return a
    raise ValueError(p)

# F=F_{p^2}=F_p[t]/(t^2-nr); element (x,y)=x+y t
def fadd(p,X,Y): return ((X[0]+Y[0])%p,(X[1]+Y[1])%p)
def fsub(p,X,Y): return ((X[0]-Y[0])%p,(X[1]-Y[1])%p)
def fmul(p,nr,X,Y): return ((X[0]*Y[0]+nr*X[1]*Y[1])%p,(X[0]*Y[1]+X[1]*Y[0])%p)
def fpow(p,nr,X,e):
    out=(1,0)
    while e:
        if e&1: out=fmul(p,nr,out,X)
        X=fmul(p,nr,X,X); e>>=1
    return out
def ftau(p,X): return (X[0]%p,(-X[1])%p)            # x->x^p
def finv(p,nr,X):
    n=(X[0]*X[0]-nr*X[1]*X[1])%p; ni=pow(n,p-2,p)
    return ((X[0]*ni)%p,((-X[1])*ni)%p)

# A=F[X]/(X^2+cX+d); element (z0,z1)=z0+z1 xi, c,d,z0,z1 in F
def amul(p,nr,c,d,X,Y):
    M=lambda A,B: fmul(p,nr,A,B)
    c0=fsub(p,M(X[0],Y[0]),M(d,M(X[1],Y[1])))
    c1=fsub(p,fadd(p,M(X[0],Y[1]),M(X[1],Y[0])),M(c,M(X[1],Y[1])))
    return (c0,c1)
def axipow(p,nr,c,d,e):                              # [X^e]_E
    out=((1,0),(0,0)); base=((0,0),(1,0))
    while e:
        if e&1: out=amul(p,nr,c,d,out,base)
        base=amul(p,nr,c,d,base,base); e>>=1
    return out

def wedge(p,nr,X,Y): return fsub(p,fmul(p,nr,X[0],Y[1]),fmul(p,nr,X[1],Y[0]))
def PE(p,nr,c,d,X,Y):
    M=lambda A,B: fmul(p,nr,A,B)
    return fadd(p,fsub(p,M(X[0],Y[0]),M(c,M(X[0],Y[1]))),M(d,M(X[1],Y[1])))

def separated(p,nr,c,d):
    ct,dt=ftau(p,c),ftau(p,d)
    if c==ct and d==dt: return False                 # E in B[X], E=E^tau
    if c==ct: return True                            # E-E^tau = d-d^p const !=0
    r=fmul(p,nr,fsub(p,dt,d),finv(p,nr,fsub(p,c,ct)))# unique common-root candidate
    Er=fadd(p,fadd(p,fmul(p,nr,r,r),fmul(p,nr,c,r)),d)
    return Er!=(0,0)

def run(p):
    nr=find_nonresidue(p); inv2=pow(2,p-2,p); inv4=pow(4,p-2,p)
    samples=[((1,0),(0,1)),((0,1),(1,0)),((1,1),(2,3)),((2,1),(1,4)),((3,2),(5,1))]
    checked=0; sep_off_R0=0; D0_offR0=0; D0_with_Fp_root=0
    xi=((0,0),(1,0))
    for c0 in range(p):
      for c1 in range(p):                            # c1!=0 => c notin B
        c=(c0,c1); half_c=fmul(p,nr,c,(inv2,0)); s=(half_c,(1,0))
        ctau=ftau(p,c); delta_c=fmul(p,nr,fsub(p,c,ctau),(inv2,0))
        for d0 in range(p):
          for d1 in range(p):
            d=(d0,d1)
            w=fsub(p,fmul(p,nr,fmul(p,nr,c,c),(inv4,0)),d)
            if w==(0,0): continue                    # double root: separable-via-w edge, skip
            nu=fpow(p,nr,w,(p-1)//2); mu=fsub(p,nu,(1,0))
            ell_cf=(fadd(p,fmul(p,nr,mu,s[0]),delta_c),fmul(p,nr,mu,s[1]))
            xip=axipow(p,nr,c,d,p); ell=(fsub(p,xip[0],xi[0]),fsub(p,xip[1],xi[1]))
            assert ell==ell_cf,(p,c,d,ell,ell_cf)                       # (1)
            Nell=PE(p,nr,c,d,ell,ell)
            prodE=(1,0)
            for a in range(p):
                Ea=fadd(p,fadd(p,fmul(p,nr,(a,0),(a,0)),fmul(p,nr,c,(a,0))),d)
                prodE=fmul(p,nr,prodE,Ea)
            assert Nell==prodE,(p,c,d,Nell,prodE)                       # (3)
            lam=fsub(p,fmul(p,nr,delta_c,delta_c),fmul(p,nr,fmul(p,nr,mu,mu),w))
            assert lam==Nell,(p,c,d,lam,Nell)                           # (LAMBDA)
            sep=separated(p,nr,c,d)
            has_root=any(fadd(p,fadd(p,fmul(p,nr,(a,0),(a,0)),
                                       fmul(p,nr,c,(a,0))),d)==(0,0) for a in range(p))
            for (u0,u1),(b0,b1) in samples:
                u=((u0,u1%p),(u1,(u0+1)%p)); b=((b0,(b1+1)%p),(b1,b0%p))
                kappa=wedge(p,nr,u,b)
                if kappa==(0,0): continue
                g1=wedge(p,nr,ell,b); g2=PE(p,nr,c,d,b,ell)
                h1=wedge(p,nr,u,ell); h2=PE(p,nr,c,d,u,ell)
                D=fadd(p,fmul(p,nr,g1,h2),fmul(p,nr,g2,h1))
                assert D==fmul(p,nr,Nell,kappa),(p,c,d,u,b,D)           # (2)
                checked+=1
                if sep:
                    assert D!=(0,0),(p,c,d,u,b)                         # (4) emptiness
                    sep_off_R0+=1
                if D==(0,0):
                    D0_offR0+=1
                    if has_root: D0_with_Fp_root+=1
    return dict(p=p,checked=checked,separated_off_R0=sep_off_R0,
                D0_offR0=D0_offR0,D0_all_have_Fp_root=(D0_offR0==D0_with_Fp_root))

if __name__=="__main__":
    for p in (3,5,7,11):
        r=run(p)
        print(f"p={r['p']}: checked={r['checked']}, separated-off-R0 samples (all D!=0)="
              f"{r['separated_off_R0']}, D=0-off-R0 samples={r['D0_offR0']}, "
              f"every D=0 has an F_p-root (non-separated)={r['D0_all_have_Fp_root']}")
    print("PASS: ell closed form, D=N(ell)*kappa, N(ell)=prod E(a), and "
          "separated=>D!=0 verified; D=0 off R0 only on non-separated E.")
```

Expected behavior: all assertions pass; for every prime, `separated-off-R0` samples all have `D!=0`, and every `D=0` off-`R0` sample sits on a non-separated `E` with a root in `F_p` — the experimental shadow of the proof that the nonsplit-`c` D-kernel stratum is empty.
