import itertools, random

# coefficient lists low-to-high over F_p

def trim(a,p):
    a=[x%p for x in a]
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def deg(a,p): return len(trim(a,p))-1

def add(a,b,p,scale=1):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n): c[i]=((a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0))%p
    return trim(c,p)

def mul(a,b,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return trim(c,p)

def divmodp(a,b,p):
    a=trim(a,p)[:]; b=trim(b,p)
    if b==[0]: raise ZeroDivisionError
    q=[0]*max(1,len(a)-len(b)+1); inv=pow(b[-1],-1,p)
    while len(a)>=len(b) and a!=[0]:
        k=len(a)-len(b); c=a[-1]*inv%p; q[k]=c
        for i in range(len(b)): a[i+k]=(a[i+k]-c*b[i])%p
        a=trim(a,p)
    return trim(q,p),trim(a,p)

def gcdp(a,b,p):
    a=trim(a,p); b=trim(b,p)
    while b!=[0]:
        _,r=divmodp(a,b,p); a,b=b,r
    inv=pow(a[-1],-1,p)
    return trim([(x*inv)%p for x in a],p)

def evalp(a,x,p):
    v=0
    for c in reversed(a): v=(v*x+c)%p
    return v

def monic(a,p):
    a=trim(a,p); inv=pow(a[-1],-1,p)
    return trim([x*inv%p for x in a],p)

def prod_locator(T,p):
    z=[1]
    for x in T: z=mul(z,[(-x)%p,1],p)
    return z

def proportional_mod(P,B,A,p):
    rb=divmodp(B,A,p)[1]; rp=divmodp(P,A,p)[1]
    out=[]
    for c in range(1,p):
        if add(rp,rb,p,scale=-c)==[0]: out.append(c)
    return out

def rand_monic(d,p): return [random.randrange(p) for _ in range(d)]+[1]

def check_case(p,A,B,j,L):
    roots={x for x in L if evalp(A,x,p)==0}
    for T in itertools.combinations(L,j):
        P=prod_locator(T,p)
        cs=proportional_mod(P,B,A,p)
        lhs=bool(cs)
        rhs=not bool(set(T)&roots) and bool(cs)
        if lhs!=rhs: return False,("degree-j",T,roots,cs)
        if lhs:
            # congruence to unit B forces P to be a unit modulo A
            if set(T)&roots: return False,("unit",T,roots,cs)
    # Low layers: full iff P is scalar A, which can happen only e=deg A.
    d=deg(A,p)
    for e in range(j):
        for E in itertools.combinations(L,e):
            P=prod_locator(E,p)
            q,r=divmodp(P,A,p)
            full=(r==[0] and deg(q,p)==0)
            intrinsic=(e==d and monic(P,p)==monic(A,p))
            if full!=intrinsic: return False,("low",E,P,A,q,r)
    return True,None

def main():
    random.seed(20260620); total=0
    hand=[
      (7, mul(mul([6,1],[5,1],7),[4,1],7), [3,2,0,0,1],4), # split reduced roots 1,2,3
      (7, mul(mul([6,1],[6,1],7),[6,1],7), [1,1,0,0,1],4), # triple root 1
      (7, mul([1,0,1],[5,1],7), [2,0,3,0,1],4),            # irreducible quad * root 2 (t^2+1 irreducible mod7? actually roots ±? 3^2+1=3; no)
    ]
    for p,A,B,j in hand:
        while deg(gcdp(A,B,p),p)>0: B[0]=(B[0]+1)%p
        ok,info=check_case(p,A,B,j,list(range(p))); total+=1
        if not ok: print("FAIL hand",p,A,B,info); return 1
    for p in [3,5,7,11]:
      for d in range(2,min(5,p)):
       for j in range(d+1,min(p,d+3)+1):
        if j>p: continue
        for _ in range(25):
            A=rand_monic(d,p); B=rand_monic(j,p)
            for __ in range(100):
                if deg(gcdp(A,B,p),p)==0: break
                B=rand_monic(j,p)
            if deg(gcdp(A,B,p),p)>0: continue
            ok,info=check_case(p,A,B,j,list(range(p))); total+=1
            if not ok: print("FAIL",p,d,j,A,B,info); return 1
    print("PASS",total,"CI cases")
    return 0
if __name__=='__main__': raise SystemExit(main())
