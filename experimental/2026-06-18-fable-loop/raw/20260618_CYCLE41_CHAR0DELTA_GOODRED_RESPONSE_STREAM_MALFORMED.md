I'll start by reading the file index and the key context files.Let me read the key context files in parallel.Now let me read the Cycle 40 audit, checker, and result.Now the key checker and its result, plus the Cycle 40 response with the surface model.Let me read the checker result, the Cycle 40 response, and the ledger/wall files.Now let me read the Cycle 40 response and the ledger/wall files.I have the core technical picture. Let me verify the wall labeling discipline and the Cycle 33 top-symbol claim referenced in the bridge.I have the full picture. I've read the Cycle 39 collapse lemma, the Cycle 40 finite-place geometric `S_4` criterion and its `all_pass=true` checker result, the Cycle 33 top-symbol degree bound, and the active wall. 

Two operational facts shape this cycle, exactly as in Cycles 39–40: only the `Read` tool is actually wired in this harness (no `create_file`/`bash` despite the advertised output-file mode), so I deliver artifacts inline, clearly labeled, and I run by hand the parts I can settle exactly. The new mathematical content here is genuinely runnable and I verified it against the audited finite-place witnesses.

---

# Cycle 41 result — `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA`

Status: `BANKABLE_LEMMA` (explicit characteristic-zero branch object, verified to reduce to the audited finite-place model) + `EXPERIMENTAL` (symbolic `Delta|_L`, `disc_X L|_L`, bad-modulus computation — specified, UNRUN here) + `EXACT_NEW_WALL`. Not `PROOF` of either subcase (good reduction not yet certified), not `COUNTERPACKET`, not `ROUTE_CUT`, not MCA/CA/list/line/curve-MCA/protocol/SNARK/prize. Ledgers separate: `q_gen=p`, `q_line=p^2`, `B=F_p`, `F=F_{p^2}`, `q_chal` unused.

## The decisive new object: the explicit char-0 cover

Cycle 39 collapsed `ell` to a fixed element per subcase, so the cover no longer moves with `p`. That means it lifts verbatim to `K = Q(i)`, `A = K[X]/(E)`, `E = X^2 + iX + 1`. Reducing powers of `X` mod `E` (with `X^2=-1-iX`):

```text
X^0=(1,0)  X^1=(0,1)  X^2=(-1,-i)  X^3=(i,-2)  X^4=(2,3i)   [pairs = c0 + c1 X]
```

For `tau=(t1,t2,t3,t4)` write `L_tau(X)=X^4 - t1 X^3 + t2 X^2 - t3 X + t4`. The two A-elements the graph equation needs are (computed exactly):

```text
lam = [L_tau]_E = ( t4 - t2 - i t1 + 2 ,  2 t1 - i t2 - t3 + 3i )
Qres = [Q_S(tau)]_E = ( 1 - i t1 + i t2 - t3 ,  t2 + i )         (w=(1, i, 1+i, 1))
```

With `W = u - z b = (1, 1-z)`, put `s = 1-z = s0 + i s1`, `s0 = 1-z0`, `s1 = -z1`. The graph equation `W·lam - ell·Qres = 0` splits into its real/`alpha` parts, giving a **4×4 `B`-linear system** `M(z)·(t1,t2,t3,t4)^T = R(z)` whose entries are affine in `(s0,s1)`, hence `Delta = det M` has total degree `<= 4` (consistent with Cycle 33's `deg <= 4`, `TopSym = -N(kappa)N(z)^2 Q_4`).

Subcase A (`ell = i`, scalar):

```text
                 t1          t2          t3        t4    |  rhs
Re I  :   [ -1-2 s0,      -s1,         s0,        1 ]    | -(2 + 3 s1)
Im I  :   [ -1-2 s1,       s0,       1+s1,        0 ]    |  (1 + 3 s0)
Re II :   [  2+3 s1,     -2 s0,      -1-s1,      s0 ]    | -(1 + 5 s0)
Im II :   [   -3 s0,    -2-2 s1,      s0,        s1 ]    | -(3 + 5 s1)
```

Subcase B (`ell = -2X`, non-scalar):

```text
                 t1          t2          t3        t4    |  rhs
Re I  :   [   -2 s0,     -3-s1,        s0,        1 ]    | -(2 + 3 s1)
Im I  :   [ -1-2 s1,       s0,         s1,        0 ]    |  (2 + 3 s0)
Re II :   [  2+3 s1,     -2 s0,      -3-s1,      s0 ]    | -(4 + 5 s0)
Im II :   [ -2-3 s0,    -1-2 s1,      s0,        s1 ]    | -(3 + 5 s1)
```

These two systems are the characteristic-zero branch/determinant objects `CHAR0DELTA` demanded. They are genuinely different covers (no automorphism collapses `ell=i` to `ell=-2X`), so each carries its own `Delta` and good prime.

## Verification against the audited finite-place witnesses (run by hand)

I reduced each system mod the relevant prime at the recorded witness fiber and recovered the audited factorization type — this is independent confirmation that the lift is correct.

Subcase A, `p=7`, `z=(0,0)` (so `s0=1,s1=0`), where the checker recorded `witness_13=[0,0]`:

```text
solve mod 7  =>  tau = (6, 3, 0, 2)
L_tau = X^4 + X^3 + 3X^2 + 2  (mod 7)
X=1 is a root; quotient X^3+2X^2+5X+5 has no root in F_7  =>  type "13"   ✓
```

Subcase B, `p=11`, `z=(0,0)`, recorded `witness_13=[0,0]`:

```text
solve mod 11 =>  tau = (6, 0, 5, 5)
L_tau = X^4 + 5X^3 + 6X + 5  (mod 11)
X=4 is a root; quotient X^3+9X^2+3X+7 has no root in F_11  =>  type "13"  ✓
```

Both match the audited `cycle40` result JSON exactly. The char-0 systems are correct.

## The bridge, with the gate made minimal and runnable

The both-parity geometric-`S_4` criterion (Cycle 40) is proved **along a fixed line** `L` (`m=1,e=0`, i.e. `z1=z0`). So the object whose monodromy is certified is the degree-4 cover of the `z0`-line. On `L` everything is a **one-variable** polynomial in `z0` over `Z[i]`, so the good-reduction certificate is a 1-variable computation:

```text
Bridge (tame specialization, SGA1 Exp. XIII, deg 4 prime-to-p0 for p0>=5):
  IF the line cover has good reduction at p0 -- Delta|_L(z0) and the quartic
     discriminant numerator D|_L(z0) keep their Q(i)-degree mod p0, stay
     coprime, and stay separable mod p0 --
  THEN  G_geom,p0(line) = G_geom,Qbar(i)(line).
  Cycle 40 gives G_geom,p0(line) = S_4, hence G_geom,Qbar(i)(line) = S_4,
  hence the surface geometric group = S_4 (line group <= surface group <= S_4).
  Then for every other good prime p of the subcase, G_geom,p = S_4, and
  Chebotarev/Lang-Weil gives off-Delta split density -> 1/24.
```

The only unrun piece is the explicit `Delta|_L`, `D|_L`, and the integer "bad modulus" whose prime factors are the only places where good reduction can fail. If `p0=7` (A) / `p0=31` (B) does not divide that modulus, the bridge closes for that subcase. This is `CHECKER.py` below — pure Python, exact `Q(i)` arithmetic, no dependencies.

## `CHECKER.py` (intended `output_files/cycle41_char0delta_checker.py`)

```python
#!/usr/bin/env python3
"""Cycle 41 char0 / good-reduction bridge checker (line-restricted, z1=z0).
Builds the explicit char-0 cover over K=Q(i) along the tested line, computes
Delta|_L(z0), the quartic-discriminant numerator D|_L(z0), and the integer
BADMOD whose prime factors are the ONLY primes where line good reduction can
fail. If a candidate p0 (7 for subcase A, 31 for subcase B) does not divide
BADMOD, SGA1 XIII transports the Cycle 40 G_geom,p0(line)=S4 to char 0.
Ledger separate: q_gen=p, q_line=p^2, B=F_p, F=F_{p^2}, q_chal unused.
NOT MCA/CA/list/line/curve/protocol/SNARK/prize.  Exact Gaussian-rational."""
from fractions import Fraction as Fr

# ---- Q(i) scalars: (re, im) with Fraction entries ----
G0=(Fr(0),Fr(0)); G1=(Fr(1),Fr(0))
def gi(n): return (Fr(n),Fr(0))
def gadd(a,b): return (a[0]+b[0], a[1]+b[1])
def gsub(a,b): return (a[0]-b[0], a[1]-b[1])
def gneg(a): return (-a[0],-a[1])
def gmul(a,b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def gdiv(a,b):
    d=b[0]*b[0]+b[1]*b[1]
    return ((a[0]*b[0]+a[1]*b[1])/d, (a[1]*b[0]-a[0]*b[1])/d)
def giszero(a): return a[0]==0 and a[1]==0

# ---- polynomials in z0 over QNow let me read the four ledger files to align with labeling discipline and confirm current wall state.I have the complete technical and bookkeeping picture from Cycles 33, 38, 39, 40, the active wall, and the two checkers/results. I can only `Read` in this harness (no write/exec tool is wired, exactly as Cycles 39–40 documented), so I deliver the artifacts inline with their intended `output_files/` paths and mark the checker UNRUN for Codex.

---

## Cycle 41 result — `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA`

Status: `BANKABLE_LEMMA` (the tame good‑reduction bridge, stated with exact hypotheses and the correct logical direction) + `EXPERIMENTAL` (an exact char‑0 `Delta`/`disc` good‑reduction checker, specified and runnable, UNRUN here) + `EXACT_NEW_WALL` + `AUDIT`. Not `PROOF` (the good‑reduction certificate is not executed here), not `COUNTERPACKET`, not `ROUTE_CUT`. Ledgers separate: `q_gen=p` (`B=F_p`), `q_line=p^2` (`F=F_{p^2}=B(alpha)`), `q_chal` unused. No MCA/CA/list/line/curve‑MCA/protocol/SNARK/prize promotion.

### 1. The decisive correction: the bridge runs in the *easy* direction

The wall text (and the Cycle 40 response) frames the missing step as "transport finite‑place `S_4` **up** to characteristic zero via a good‑reduction certificate." That is the right object but the loop has been treating it as if good reduction were needed to *create* char‑0 `S_4`. It is not. The standard reduction theory of tame covers of the line gives an **isomorphism** of geometric monodromy under good reduction, and the conclusion "char‑0 group `= S_4`" then follows from the finite‑place `S_4` already banked, with no Chebotarev and no density input. Good reduction is genuinely needed only for the *downward, outward* transport to the other primes of the subcase (globalization).

`BANKABLE_LEMMA` — **Tame good‑reduction bridge for the fixed subcase cover.**
Let `K=Q(i)`, `R=Z[i][1/N]`. Fix one subcase and its Cycle‑39 constant:
```
A = K[X]/(E),  E = X^2 + i X + 1,   b=[X],  u=[1+X],  W=(1, i, 1+i, 1),
ell = i        (Subcase A),     ell = -2[X]   (Subcase B).
```
On the line `L: z_1=z_0`, build `M(z_0)tau=-C_0(z_0)` exactly as in the Cycle 38/40 construction but over `K[z_0]`; set `tau(z_0)=M^{-1}(-C_0)` and
```
L_{tau}(X)=X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4  in  K(z_0)[X].
```
Let `Delta_L(z_0)=det_K M(z_0) in Z[i][z_0]` (the pole/det locus) and let `Ddisc(z_0) in Z[i][z_0]` be the numerator of `disc_X L_{tau}` (i.e. `disc_X L_{tau} = Ddisc/Delta_L^6`). Let `p_0 ≡ 3 mod 4`, `p_0 ∤ 24`, lying in the subcase residue class mod 5. Suppose, in `F_{p^2}=Z[i]/(p_0)`:
```
(G1) lead(Delta_L) != 0  and  lead(Ddisc) != 0           [no branch point escapes to infinity]
(G2) Res(Delta_L, Delta_L') != 0  and  Res(Ddisc, Ddisc') != 0   [each factor stays separable]
(G3) Res(Delta_L, Ddisc) != 0                            [pole locus and disc locus stay disjoint]
```
Then the degree‑4 cover on `L` has **good reduction at `p_0`**, it is tame, and
```
G_geom( L_tau / Kbar(z_0) )  ≅  G_geom( L_tau / Fbar_p(z_0) ).
```

Proof. `(G1)–(G3)` say the reduced branch divisor `{Delta_L=0} ∪ {Ddisc=0}` on `P^1_{z_0}` stays étale and of constant degree mod `p_0` (distinct, finite branch points). The cover is degree 4 with `Gal ⊆ S_4`, `|S_4|=24` prime to `p_0`, so it is tame. For a tamely ramified cover of the line whose branch divisor has good reduction, the specialization map on tame fundamental groups `pi_1^{t}(P^1_{Fbar_p}∖B̄) → pi_1^{t}(P^1_{Kbar}∖B)` is an isomorphism (SGA1 Exp. XIII, Cor. 2.12 plus the tame‑quotient surjectivity; Beckmann, *Ramified primes in fields of moduli*, 1989; Fried–Völklein). The monodromy representation factors through this group on both sides, so the geometric Galois images coincide. ∎

`COROLLARY` — **char‑0 geometric `S_4`, per subcase, conditional on `(G1)–(G3)` at one prime.**
By Cycle 39, reducing the fixed char‑0 model mod `p_0` (with `p_0` inert, `Z[i]/(p_0)=F_{p^2}`, and `[X^{p_0}-X]_E≡ell`) reproduces exactly the Cycle 40 finite model. By Cycle 40, `G_geom(Fbar_p) = S_4` at `p_0=7` (Subcase A) and `p_0=31` (Subcase B) via the both‑parity `"4"`+`"13"` argument. Hence, if `(G1)–(G3)` hold at that `p_0`, then `G_geom(Kbar(z_0)) = S_4` for that subcase. This settles the "geometric `S_4` over `Q(i)(z_0)`" item the wall lists as *not banked* — modulo the finite check `(G1)–(G3)`, which is exactly `CHAR0DELTA`.

`COROLLARY` (globalization shape, not yet discharged). Once char‑0 `S_4` is known, every prime `q ≡ 3 mod4`, `q ≡` (subcase) `mod 5`, `q∤24`, with `q ∤ disc_{z_0}(Delta_L·Ddisc)·Res(Delta_L,Ddisc)·lead(...)` over `Z[i]`, is a good‑reduction prime, so `G_geom(Fbar_q)=S_4` there too. The bad set is the finite set of primes dividing those `Z[i]`‑integers. The remaining global step is then Chebotarev/Lang–Weil for the off‑branch split density `→ 1/24` — a *separate* wall.

### 2. Why this is now a finite, exact, char‑0 computation (no `p`‑dependence)

Cycle 33 already bounds `deg Delta_L ≤ 4` and gives `TopSym(Delta) = -N(kappa)·N(z)^2·Q_4` with `N(kappa)≠0`, `Q_4=N(c_b)≠0`, so `Delta_L ≢ 0` over `K`. With `tau_j` of the form `(deg ≤4)/Delta_L`, `disc_X L_{tau}` is weighted‑degree‑6 in the `tau_j`, so `Ddisc` has `deg_{z_0} ≤ 24`. Both `Delta_L` and `Ddisc` are extractable exactly over `Z[i]` by Cramer + interpolation, and `(G1)–(G3)` are three resultant/leading‑coefficient nonvanishings mod `p_0` in `F_{p^2}`. This is bounded and decidable; the only reason it is not discharged in this answer is the absence of an execution tool.

### 3. `CHECKER.py` — intended `output_files/cycle41_char0delta_checker.py` (UNRUN here)

Exact `Q(i)` arithmetic; mirrors the Cycle 38/40 construction so the reduction mod `p_0` provably matches the finite model; extracts `Delta_L`, `Ddisc` over `Z[i]` by interpolation; certifies `(G1)–(G3)` at `p_0=7` (A) and `p_0=31` (B).

```python
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
    def b4(r): return [r[0][0],r[0][1],r[1][0],r[1][1]]   # 4 Gaussian -> but parts are Gaussian; flatten to Gaussian list
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
    out={"A":run_subcase("A",I,7),         # ell=i,   p0=7
         "B":run_subcase("B",(G(0),G(-2)),31)}  # ell=-2X, p0=31
    out["both_good_reduction"]=out["A"]["GOOD_REDUCTION_at_p0"] and out["B"]["GOOD_REDUCTION_at_p0"]
    print(json.dumps(out,indent=2,default=str))
```

Honest caveats on the checker: it is self‑contained and exact, but UNRUN in this harness. Two implementation risks Codex should watch: (a) the `Ddisc` interpolation degree bound (`≤24`) — if `deg_Ddisc_Q` saturates at 30, raise the node count; (b) the `qres`/`lam` reconstruction must reproduce the Cycle 40 finite output when reduced — Codex should sanity‑check by also reducing this model mod `p0` and confirming it reproduces the banked histograms (`p=7`: `{"4":1,"13":2,"112":1}`; `p=31`: `{"1111":1,"112":5,"13":11,"22":6,"4":6,"nonsquarefree":2}`). If the reduction does not match, the char‑0 model is mis‑specified and the bridge does not apply.

### 4. `RESULTS.json` — intended `output_files/cycle41_char0delta_certificate.json`

```json
{
  "target": "W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA",
  "status": ["BANKABLE_LEMMA(tame_goodreduction_bridge)","EXPERIMENTAL(char0_Delta_disc_checker_UNRUN)","EXACT_NEW_WALL","AUDIT"],
  "ledger": {"q_gen":"p","q_line":"p^2","B":"F_p","F":"F_{p^2}=B(alpha)","q_chal":"unused"},
  "char0_model": {
    "field":"K=Q(i)","E":"X^2 + i X + 1","b":"[X]","u":"[1+X]","W":[1,"i","1+i",1],
    "subcaseA":{"ell":"i","p0_target":7,"residue":"p=3mod4 & p=2,3mod5"},
    "subcaseB":{"ell":"-2X","p0_target":31,"residue":"p=3mod4 & p=1,4mod5"}
  },
  "bridge_lemma": {
    "name":"tame good-reduction => G_geom(char0) ≅ G_geom(F_{p0})",
    "hypotheses":["(G1) lead(Delta_L),lead(Ddisc) != 0 mod p0","(G2) Res(Delta_L,Delta_L'),Res(Ddisc,Ddisc') != 0 mod p0","(G3) Res(Delta_L,Ddisc) != 0 mod p0","p0 prime to 24 (tame)"],
    "conclusion":"with Cycle39 collapse + Cycle40 finite S_4: G_geom(Q(i)-bar(z0)) = S_4 for that subcase",
    "direction_note":"good reduction gives ISO; char-0 S_4 needs only the finite S_4 already banked, no Chebotarev"
  },
  "depends_on_banked": ["Cycle39 locator collapse ell=i / ell=-2X","Cycle40 finite geometric S_4 (4 & 13 both-parity)","Cycle33 deg Delta<=4, TopSym(Delta)!=0"],
  "discharged_here": "logical reduction of CHAR0DELTA to three resultant nonvanishings at one prime per subcase, plus runnable exact checker",
  "not_discharged_here": "execution of (G1)-(G3) (no exec tool in harness)",
  "globalization_after": "bad primes = those dividing disc_{z0}(Delta_L*Ddisc)*Res(Delta_L,Ddisc)*lead over Z[i]; then Chebotarev/Lang-Weil density 1/24",
  "excluded_primes": [2,3,5],
  "not_banked": ["good reduction certified at any prime (checker unrun)","char0 S_4 unconditionally","uniform Theta(q_line)","COUNTERPACKET","corrected-reserve","MCA/CA/list/line/curve-MCA/protocol/SNARK/prize","any merge of q_gen=p with q_line=p^2"]
}
```

### 5. `EXACT_NEW_WALL`

The within‑`CHAR0DELTA` reduction is now sharp: the wall is no longer "find the right char‑0 object" but "verify three exact resultant nonvanishings at `p0=7` (A) and `p0=31` (B)." If Codex runs the checker and `both_good_reduction=true`, char‑0 geometric `S_4` is banked for both subcases and the live wall advances to globalization:

```
W-F1-AA-RES-T2J4-A2B-S4-GLOBAL-DENSITY
```
Targets there: (i) the explicit `Z[i]` bad‑prime finite set `S_bad = { q : q | disc_{z0}(Delta_L·Ddisc)·Res(Delta_L,Ddisc)·lead }`; (ii) for `q ∉ S_bad` in the subcase residue class, `G_geom(Fbar_q)=S_4` by the bridge run downward; (iii) Lang–Weil/Chebotarev for off‑branch identity‑Frobenius density `→ 1/24`, giving `Theta(q_line)` split slopes in the restricted local branch for almost all good `q` per subcase — still only a restricted local counterpacket seed, not corrected‑reserve/MCA/prize.

If instead the checker returns `GOOD_REDUCTION_at_p0=false` for a subcase at the chosen `p0`, that is not a route cut: choose the next passing prime (`23,43,47` for A; `11,19,59` for B) and rerun, since the Cycle‑40 finite `S_4` holds at all of them. A genuine `ROUTE_CUT` signal would be `(G2)` failing at *every* passing prime of a subcase (branch divisor never reduces étale), which would point to a structural non‑reduced branch component over `Z[i]`.

### 6. `NEXT_PROMPT.md` — intended `output_files/cycle41_next_prompt.md`

Attack `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA` to closure, then `…-GLOBAL-DENSITY`. Require: (a) execute `cycle41_char0delta_checker.py`; first confirm the char‑0 model reduces mod `p0` to the banked Cycle‑40 histograms (`p=7`, `p=31`), then bank `(G1)–(G3)` and the `PROOF`‑level corollary `G_geom(Q(i)-bar(z0))=S_4` per subcase; (b) emit the explicit `Z[i]` polynomials `Delta_L(z0)`, `Ddisc(z0)` and the finite bad‑prime set `S_bad`; (c) only after (a)–(b), the Chebotarev/Lang–Weil density step with an explicit error term. Keep `q_gen=p` and `q_line=p^2` separate; promote nothing past restricted‑local‑seed without source hypotheses.

---

Do you see a route to a full solve? For the restricted `t=2, j=4`, `A^2_B` branch: yes, and Cycle 41 shortens it by one conceptual step and removes the apparent need for Chebotarev to *reach* characteristic zero. The next exact construction is the bridge corollary made effective: run the supplied exact `Q(i)` checker to verify `(G1)–(G3)` — `lead`, two `Res(·,·')`, and `Res(Delta_L,Ddisc)` nonzero in `F_{p^2}` — at `p0=7` (Subcase A, `ell=i`) and `p0=31` (Subcase B, `ell=-2X`). Those three nonvanishings, with the already‑banked Cycle 39 collapse and Cycle 40 finite `S_4`, give `G_geom(Q(i)-bar(z0))=S_4` for both subcases via tame good‑reduction (`SGA1 XIII` / Beckmann). Then the only remaining wall is `GLOBAL-DENSITY`: the finite `Z[i]` bad‑prime set plus the `1/24` split‑density count. Honest boundary: I could not execute the checker (only `Read` is wired), so `CHAR0DELTA` is reduced to a finite certified computation but not yet discharged; nothing here is corrected‑reserve, MCA, or prize status — it remains a restricted local seed, and the two subcases are genuinely distinct covers (`ell=i` vs `ell=-2X`), each requiring its own good prime.