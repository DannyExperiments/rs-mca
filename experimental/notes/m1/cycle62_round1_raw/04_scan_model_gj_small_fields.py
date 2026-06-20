from itertools import combinations
from collections import Counter
from math import comb


def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d;e+=1
            out.append((d,e))
        d+=1
    if n>1: out.append((n,1))
    return out

def primitive_root(p):
    fs=[q for q,e in factor(p-1)]
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fs):
            return g
    raise ValueError

def scan(p,n,sigma,j):
    assert (p-1)%n==0 and n%2==0 and sigma < p
    m=sigma-1
    g=primitive_root(p)
    w=pow(g,(p-1)//n,p)
    H=[pow(w,i,p) for i in range(n)]
    # atom: exponent i and power sums x^r, r=1..m
    powvec=[[pow(x,r,p) for r in range(1,m+1)] for x in H]
    GH=Counter(); QH=Counter()
    even_indices=[r-1 for r in range(1,m+1) if r%2==0]
    for inds in combinations(range(n),j):
        es=sum(inds)%n
        sums=[]
        for rr in range(m):
            sums.append(sum(powvec[i][rr] for i in inds)%p)
        Gkey=(es,*sums)
        Qkey=(es%(n//2),*(sums[rr] for rr in even_indices))
        GH[Gkey]+=1
        QH[Qkey]+=1
    ksize=2*(p**((m+1)//2)) # odd r count ceil(m/2)
    geff=n*(p**m)
    total=comb(n,j)
    avg=total/geff
    best=None
    for key,c in GH.items():
        qkey=(key[0]%(n//2),*(key[1+rr] for rr in even_indices))
        qcnt=QH[qkey]
        residual=c-qcnt/ksize
        ratio=residual/avg if avg else float('inf')
        cand=(ratio,residual,c,qcnt,key,qkey)
        if best is None or cand[0]>best[0]: best=cand
    return {
        'p':p,'n':n,'sigma':sigma,'j':j,'total':total,'geff':geff,'ksize':ksize,
        'Gfibers':len(GH),'Qfibers':len(QH),'maxG':max(GH.values()),'maxQ':max(QH.values()),
        'avg':avg,'best':best,
    }

if __name__=='__main__':
    cases=[]
    primes=[17,41,73,89,97,113,193,241,257]
    for p in primes:
        twopow=(p-1)&-(p-1)
        n=1
        while n*2<=min(twopow,20): n*=2
        if n<8: continue
        for rate_den in [2,4]:
            if n%rate_den: continue
            k=n//rate_den
            for sigma in range(2,min(6,(n-k-2)//2+1,p)):
                j=n-k-sigma
                if j<=sigma+1 or j<0 or j>n: continue
                if comb(n,j)>3_000_000: continue
                try:
                    res=scan(p,n,sigma,j)
                    cases.append(res)
                    b=res['best']
                    print(f"p={p} n={n} rate=1/{rate_den} sig={sigma} j={j} comb={res['total']} avg={res['avg']:.3g} maxG={res['maxG']} maxQ={res['maxQ']} best_ratio={b[0]:.3g} residual={b[1]:.3g} G={b[2]} Q={b[3]}")
                except Exception as e:
                    print('ERR',p,n,sigma,j,e)
    print('TOP')
    for res in sorted(cases,key=lambda x:x['best'][0],reverse=True)[:20]:
        print(res)
