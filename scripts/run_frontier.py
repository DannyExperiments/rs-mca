import numpy as np, time, sys
from sympy import primitive_root

def subgroup(p, N):
    g = primitive_root(p)
    return [pow(g, (p - 1) // N * i, p) for i in range(N)]

def half_states(elems, p, lmax):
    by_size = {0: {(0, 0)}}
    for x in elems:
        new = {}
        for sz, st in by_size.items():
            if sz + 1 > lmax: continue
            tgt = new.setdefault(sz + 1, set())
            for (a, b) in st:
                tgt.add(((a + x) % p, (b + a * x) % p))
        for sz, st in new.items():
            by_size.setdefault(sz, set()).update(st)
    out = {}
    for sz, st in by_size.items():
        if st:
            arr = np.array(sorted(st), dtype=np.int64)
            out[sz] = (arr[:, 0].copy(), arr[:, 1].copy())
    return out

def psi2_cover(p, N, l):
    Q = subgroup(p, N)
    half = N // 2
    SL = half_states(Q[:half], p, l)
    SR = half_states(Q[half:], p, l)
    bitmap = np.zeros(p * p, dtype=bool)
    for i in range(0, l + 1):
        j = l - i
        if i not in SL or j not in SR: continue
        aL, bL = SL[i]; aR, bR = SR[j]
        chunk = max(1, int(1.5e7) // max(1, len(aR)))
        for s in range(0, len(aL), chunk):
            aLs, bLs = aL[s:s+chunk, None], bL[s:s+chunk, None]
            e1 = (aLs + aR[None, :]) % p
            e2 = (bLs + bR[None, :] + aLs * aR[None, :]) % p
            bitmap[(e1 * p + e2).ravel()] = True
    return int(bitmap.sum()), p * p

N, l = 32, 18
for p in [int(x) for x in sys.argv[1:]]:
    t0 = time.time()
    cov, tot = psi2_cover(p, N, l)
    line = f"p={p:>6}: coverage {cov:>9}/{tot:<9} onto={str(cov==tot):>5} missing={tot-cov:<8} [{time.time()-t0:5.1f}s]"
    print(line, flush=True)
    with open("frontier_results.txt", "a") as f:
        f.write(line + "\n")
