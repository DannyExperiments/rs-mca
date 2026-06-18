#!/usr/bin/env python3
"""Cycle 41 characteristic-zero good-reduction checker for
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA.
Builds the fixed char-0 cover over K=Q(i) on the line z1=z0 (m=1,e=0),
extracts Delta_L(z0) (det/pole locus) and Ddisc(z0) (numerator of disc_X L_tau)
as polynomials over Z[i], and certifies good reduction (G1)-(G3) at one prime
per subcase: p0=7 (A, ell=i), p0=31 (B, ell=-2X). Pure Python (Fraction), no deps.
Ledger separate: q_gen=p, q_line=p^2, q_chal unused. NOT MCA/CA/list/line/
curve/protocol/SNARK/prize. Conclusion is conditional on the banked Cycle 39
collapse and the Cycle 40 finite-place geometric S_4."""
from fractions import Fraction as Fr
import json

# ---- Gaussian rationals g=(a,b)=a+bi, a,b Fr ----
def G(a,b=0): return (Fr(a),Fr(b))
def gadd(x,y): return (x[0]+y[0], x[1]+y[1])
def gsub(x,y): return (x[0]-y[0], x[1]-y[1])
def gneg(x): return (-x[0],-x[1])
def gmul(x,y): return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def gscal(x,c): return (x[0]*c, x[1]*c)
def gzero(x): return x[0]==0 and x[1]==0
def ginv(x):
    n=x[0]*x[0]+x[1]*x[1]
    return (x[0]/n, -x[1]/n)
def gdiv(x,y): return gmul(x,ginv(y))
I=G(0,1); ONE=G(1); ZERO=G(0)

def run_subcase(name, ell, p0):
    # residue elements of A=K[X]/(X^2+iX+1): (c0,c1)=c0+c1 X, c0,c1 Gaussian.
    # X^2 = -1 - iX.
    def rmul(a,b):
        a0,a1=a; b0,b1=b
        c0=gsub(gmul(a0,b0), gmul(a1,b1))
        c1=gsub(gadd(gmul(a0,b1),gmul(a1,b0)), gmul(I,gmul(a1,b1)))
        return (c0,c1)
    def rsub(a,b): return (gsub(a[0],b[0]), gsub(a[1],b[1]))
    # X^k mod E as residue elements
    XI=[(ONE,ZERO)]            # X^0
    Xres=(ZERO,ONE)            # X
    cur=(ONE,ZERO)
    for _ in range(4):
        cur=rmul(cur,Xres); XI.append(cur)
    # data
    b_res=(ZERO,ONE)           # b=[X]
    u=(ONE,ONE)                # u=[1+X]
    w1,w2,w3,w4=ONE,I,gadd(ONE,I),ONE   # W=(1,i,1+i,1)
    def lam(t):                # [X^4 - t1 X^3 + t2 X^2 - t3 X + t4]_E, t_j Gaussian scalars
        t1,t2,t3,t4=t
        o=XI[4]
        o=rsub(o,(gmul(t1,XI[3][0]),gmul(t1,XI[3][1])))
        o=(gadd(o[0],gmul(t2,XI[2][0])), gadd(o[1],gmul(t2,XI[2][1])))
        o=rsub(o,(gmul(t3,XI[1][0]),gmul(t3,XI[1][1])))
        return (gadd(o[0],t4), o[1])
    def qres(t):
        t1,t2,t3,_=t
        q3=w1
        q2=gsub(w2,gmul(w1,t1))
        q1=gadd(gsub(w3,gmul(w2,t1)),gmul(w1,t2))
        q0=gsub(gadd(gsub(w4,gmul(w3,t1)),gmul(w2,t2)),gmul(w1,t3))
        # residue of q0+q1 X+q2 X^2+q3 X^3
        o=(q0,ZERO)
        o=(gadd(o[0],ZERO),gadd(o[1],q1))            # + q1 X
        o=(gadd(o[0],gmul(q2,XI[2][0])),gadd(o[1],gmul(q2,XI[2][1])))
        o=(gadd(o[0],gmul(q3,XI[3][0])),gadd(o[1],gmul(q3,XI[3][1])))
        return o
    def eqres(z,t):
        left=rsub(u,(gmul(z,b_res[0]),gmul(z,b_res[1])))
        return rsub(rmul(left,lam(t)),rmul(ell,qres(t)))
    def b4(r):
        # Flatten c0+c1 X, with c0,c1 in Q(i), into four Q-equations
        # represented as Gaussian scalars with zero imaginary part.
        return [(r[0][0],Fr(0)),(r[0][1],Fr(0)),(r[1][0],Fr(0)),(r[1][1],Fr(0))]
    # build M(z),C0(z): t enters as Gaussian scalars (im part 0 expected); columns affine
    def build(z):
        const=b4(eqres(z,[ZERO]*4))
        cols=[]
        for k in range(4):
            e=[ZERO]*4; e[k]=ONE
            v=b4(eqres(z,e))
            cols.append([gsub(v[r],const[r]) for r in range(4)])
        M=[[cols[c][r] for c in range(4)] for r in range(4)]
        rhs=[gneg(x) for x in const]
        return M,rhs
    # Gaussian-rational 4x4 determinant and Cramer
    def det4(M):
        a=[row[:] for row in M]; d=ONE
        for col in range(4):
            piv=next((r for r in range(col,4) if not gzero(a[r][col])),None)
            if piv is None: return ZERO
            if piv!=col: a[col],a[piv]=a[piv],a[col]; d=gneg(d)
            d=gmul(d,a[col][col]); inv=ginv(a[col][col])
            for r in range(col+1,4):
                if not gzero(a[r][col]):
                    f=gmul(a[r][col],inv)
                    a[r]=[gsub(a[r][c],gmul(f,a[col][c])) for c in range(4)]
        return d
    def tau_at(z0):
        z=G(z0)                       # line z1=z0 -> z=z0+ i z0 = z0(1+i)
        z=gmul(G(z0),gadd(ONE,I))
        M,rhs=build(z); D=det4(M)
        if gzero(D): return None,ZERO
        t=[]
        for c in range(4):
            Mc=[row[:] for row in M]
            for r in range(4): Mc[r][c]=rhs[r]
            t.append(gdiv(det4(Mc),D))
        return t,D
    # disc_X of quartic via resolvent invariants (matches finite checker)
    def disc_val(t):
        t1,t2,t3,t4=t
        A=gneg(t2); B=gsub(gmul(t1,t3),gscal(t4,4))
        C=gneg(gsub(gadd(gmul(gmul(t1,t1),t4),gmul(t3,t3)),gscal(gmul(t2,t4),4)))
        term=gadd(gsub(gadd(gscal(gmul(gmul(A,B),C),18),
                            gmul(gmul(A,A),gmul(B,B))),
                       gscal(gmul(gmul(A,A),gmul(A,C)),4)),ZERO)
        term=gsub(term,gscal(gmul(gmul(B,B),B),4))
        term=gsub(term,gscal(gmul(C,C),27))
        return term
    # sample nodes z0 (integers) with Delta!=0; collect 31 for Ddisc (deg<=24) and 5 for Delta(deg<=4)
    nodes=[]; vals_D=[]; vals_Ddisc=[]
    z0=0
    while len(nodes)<31 and z0<400:
        t,D=tau_at(z0)
        if t is not None and not gzero(D):
            nodes.append(z0); vals_D.append(D)
            d6=gmul(gmul(gmul(D,D),gmul(D,D)),gmul(D,D))   # D^6
            vals_Ddisc.append(gmul(disc_val(t),d6))
        z0+=1
    # Lagrange interpolation over Q(i) given nodes (ints) and Gaussian values
    def interp(xs,ys):
        n=len(xs); coeffs=[ZERO]*n
        for i in range(n):
            # basis poly prod_{j!=i}(x-xj)/(xi-xj), build numerator poly then scale
            num=[ONE]; den=Fr(1)
            for j in range(n):
                if j==i: continue
                num=polmul_g(num,[gneg(G(xs[j])),ONE])
                den*=Fr(xs[i]-xs[j])
            scale=gscal(ys[i],Fr(1)/den)
            for k in range(len(num)):
                coeffs[k]=gadd(coeffs[k],gmul(num[k],scale))
        # trim
        while len(coeffs)>1 and gzero(coeffs[-1]): coeffs.pop()
        return coeffs
    def polmul_g(a,b):
        out=[ZERO]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]=gadd(out[i+j],gmul(x,y))
        return out
    DeltaL=interp(nodes[:5],vals_D[:5])      # deg<=4
    Ddisc =interp(nodes,vals_Ddisc)          # deg<=30, trims to true degree
    # clear denominators to Z[i]
    def clear(poly):
        from math import gcd
        L=1
        for c in poly:
            for part in (c[0],c[1]): L=L*part.denominator//gcd(L,part.denominator)
        return [(int(c[0]*L),int(c[1]*L)) for c in poly]
    DZ=clear(DeltaL); DdZ=clear(Ddisc)
    # ---- reductions mod p0 in F_{p^2}=F_p[i] ----
    P=p0
    def radd(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
    def rmulf(x,y): return ((x[0]*y[0]-x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
    def rsubf(x,y): return ((x[0]-y[0])%P,(x[1]-y[1])%P)
    def rzero(x): return x[0]%P==0 and x[1]%P==0
    def redpoly(pz): return [ (c[0]%P,c[1]%P) for c in pz ]
    def trimf(p):
        p=p[:]
        while len(p)>1 and rzero(p[-1]): p.pop()
        return p
    def deriv(p):
        return trimf([ (c[0]*k % P, c[1]*k % P) for k,c in enumerate(p) ][1:] or [(0,0)])
    def resultant(a,b):  # Sylvester det over F_{p^2}
        a=trimf(a); b=trimf(b); da=len(a)-1; db=len(b)-1
        if da<0 or db<0: return (0,0)
        n=da+db; S=[[(0,0)]*n for _ in range(n)]
        for i in range(db):
            for j,c in enumerate(reversed(a)): S[i][i+j]=c
        for i in range(da):
            for j,c in enumerate(reversed(b)): S[db+i][i+j]=c
        # determinant over F_{p^2}
        def finv(x):
            # inverse in F_{p^2}, x!=0
            nrm=(x[0]*x[0]+x[1]*x[1])%P
            ni=pow(nrm,P-2,P)
            return ((x[0]*ni)%P,(-x[1]*ni)%P)
        d=(1,0)
        M=[row[:] for row in S]
        for col in range(n):
            piv=next((r for r in range(col,n) if not rzero(M[r][col])),None)
            if piv is None: return (0,0)
            if piv!=col: M[col],M[piv]=M[piv],M[col]; d=((-d[0])%P,(-d[1])%P)
            d=rmulf(d,M[col][col]); inv=finv(M[col][col])
            for r in range(col+1,n):
                if not rzero(M[r][col]):
                    f=rmulf(M[r][col],inv)
                    M[r]=[rsubf(M[r][c],rmulf(f,M[col][c])) for c in range(n)]
        return d
    Dp=trimf(redpoly(DZ)); Ddp=trimf(redpoly(DdZ))
    G1=(not rzero(Dp[-1])) and (not rzero(Ddp[-1]))
    G2=(not rzero(resultant(Dp,deriv(Dp)))) and (not rzero(resultant(Ddp,deriv(Ddp))))
    G3=not rzero(resultant(Dp,Ddp))
    good=bool(G1 and G2 and G3 and (24 % P != 0))
    return {"subcase":name,"p0":p0,"ell":("i" if name=="A" else "-2X"),
            "deg_DeltaL_Q":len(DZ)-1,"deg_Ddisc_Q":len(DdZ)-1,
            "deg_DeltaL_modp":len(Dp)-1,"deg_Ddisc_modp":len(Ddp)-1,
            "G1_leading_nonzero":G1,"G2_each_separable":G2,
            "G3_loci_disjoint":G3,"tame":24%P!=0,
            "GOOD_REDUCTION_at_p0":good,
            "implies":"good=>G_geom(char0)=G_geom(F_{p0})=S_4 (Cycle40)"}

if __name__=="__main__":
    out={"A":run_subcase("A",(I,ZERO),7),        # ell=i,   p0=7
         "B":run_subcase("B",(ZERO,G(-2)),31)}   # ell=-2X, p0=31
    out["both_good_reduction"]=out["A"]["GOOD_REDUCTION_at_p0"] and out["B"]["GOOD_REDUCTION_at_p0"]
    print(json.dumps(out,indent=2,default=str))
