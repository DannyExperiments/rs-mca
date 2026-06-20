I'll start by reading the file index, then the key project files.Let me read the priority project files and the directly relevant cycle materials.The director state is clear. Let me read the current Cycle 78/79 materials and the certificates.Let me read the Cycle 79 prompt packet and the underlying scripts/certificates to understand the exact model.Now the key scripts that define the model. Let me read them.This is a deep finite-algebra problem. Let me ground myself in the exact model by reading the remaining key files, then verify computationally.Now let me read the certificates and the right-half script, plus the banked lemmas and active walls.Let me read the right-half script and certificate, plus the Cycle 78 raw response and incidence-sanity files.I have the model fully. Let me read the Cycle 78 raw response, the LR sanity check, and the route/wall/queue files to see what's been tried and expected.## 1. Executive verdict and confidence

No full solve is reachable in this session, and I want to be precise about why. In this harness only the `Read` tool is exposed to me. I cannot execute code or write to `output_files`. So I cannot run the census, and every code block below is marked `UNRUN`. I also cannot, by hand, produce the discrete‑log/field data needed to certify the numeric constant `12` or to exhibit a 13‑collision: that part is genuinely arithmetic and needs a compiled run.

What I *can* do, and did, is sharpen the route with new, fully hand‑proved structure that was not in the Cycle 78 bank:

- A clean reduction of the entire problem to a **weighted 8‑subset‑sum collision on a 7×16 exponent grid** (dlog linearization).
- A proof that the 48‑set family is **closed under complementation**, with an **explicit involution τ**.
- A consequent **global symmetry of the multiplicity function**: an explicit involution on `P_0` with `m(v) = m(K/v)`.

Confidence: high on all banked items below (each is a finite hand computation or follows from the model identities C1/C4 already in `cycle68_slot_factorization_checker.py` and the run certificates of Cycles 75–77). Low/none on the constant `12` itself — unchanged, still census‑gated.

The honest headline: the "coherent ratio set" reformulation, taken alone, is *equivalent* to the fiber count (coherence is automatic, see §2.5), so it does not by itself yield a bound. The new leverage is the involution symmetry, which is real but not sufficient for 12.

## 2. Proof / bankable reduction

### 2.1 Exact product form (rigorous, from C1/C4)

From the model, with `xi = beta^2`, `zeta = eta^16` (order 16), and the C1 identity `u_t(k) = 3^{-t} · prod_{b in B_{i,a}} (xi − eta^{2t+16b})`:

```text
Phi(T) = 3^{-28} · prod_{(t,b) in G(T)} ( xi − eta^{2t+16b} ),   28 = 1+...+7.
```

`G(T) ⊆ [7]×Z_16` picks, in each row `t`, exactly one of the 48 allowed 8‑sets `B_{i,a}` (so |G(T)|=56). The map `φ(t,b)=2t+16b mod 256` is injective on the grid; its image is exactly the 112 exponents `e` that are even and `e ≢ 0 (mod 16)`. Each grid factor `xi − eta^e` is nonzero (every `b` lies in some legal set, and C‑checks force `u_t(k) ≠ 0`).

### 2.2 dlog linearization (rigorous)

`F* ` is cyclic of order `N = 17^16 − 1`. Fix a generator `g` and set `w_e := dlog_g(xi − eta^e)` for the 112 grid exponents. Then

```text
dlog Phi(T) = −28·dlog 3 + Σ_{(t,b) in G(T)} w_{2t+16b}   (mod N).
```

Define the per‑row weight `W_t(B) = Σ_{b in B} w_{2t+16b}`. Collisions become an additive problem:

```text
Phi(T) = Phi(T')  ⇔  Σ_t W_t(B_t) = Σ_t W_t(B'_t)  (mod N).
```

So `m_max` is the maximum multiplicity of the 7‑fold sumset of the seven injective families `{W_t(B) : B in B}` (each of size 48), restricted to the color shell. This is the "common‑ratio" object made fully explicit: a coherent `Δ` is exactly a set of common signed subset‑sum differences.

### 2.3 Color is the b‑coordinate sum (rigorous, hand‑verified)

`color(k) = Σ_{b in B_{i,a}} b (mod 16)`, because `Σ_{e in E_i}(a+e) = 8a + Σ E_i` and `Σ E_1=47≡15, Σ E_2=41≡9, Σ E_3=44≡12`. Hence `P_0` is precisely "total grid b‑coordinate sum ≡ 4 (mod 16)".

### 2.4 Complement closure and the explicit involution τ (rigorous, hand‑verified)

I verified the three complement relations in `Z_16` directly:

```text
E_1^c = E_2 + 6,    E_2^c = E_1 + 10,    E_3^c = E_3 + 8.
```

(Check: `E_2+6={4,6,7,8,9,10,14,15}=E_1^c`; `E_1+10={5,6,7,10,11,12,13,15}=E_2^c`; `E_3+8={3,6,8,9,10,12,13,15}=E_3^c`.)

Therefore the family `B = {a+E_i}` is **closed under complement**, with involution

```text
τ(1,a) = (2, a+6),   τ(2,a) = (1, a+10),   τ(3,a) = (3, a+8)   (indices mod 16),
```

i.e. `B_{i,a}^c = B_{τ(i,a)}`. It is an involution (`τ² = id`) and fixed‑point‑free on each slot (an 8‑set never equals its complement).

Since the 16 row‑`t` factors multiply to `prod_{b=0..15}(xi − eta^{2t}zeta^b) = beta^32 − 9^t` (C4, using `eta^32 = 9`), I get the **per‑slot multiplicative pairing**:

```text
u_t(k) · u_t(τk) = 3^{-2t} (beta^32 − 9^t)   ( ≠ 0 ),   for every slot t and index k.
```

### 2.5 Global involution symmetry of the census (rigorous)

Extend τ coordinatewise to tuples. Then

```text
Phi(T) · Phi(τT) = prod_{t=1}^{7} 3^{-2t}(beta^32 − 9^t) = 3^{-56} prod_{t=1}^{7}(beta^32 − 9^t) =: K  (constant, ≠ 0).
```

Color behaves as `color(τk) = 8 − color(k) (mod 16)` (since `Σ_{0..15} b = 120 ≡ 8`), so over 7 slots `Σ color(τk_t) ≡ 56 − Σ color(k_t) ≡ 8 − Σ (mod 16)`. For `T ∈ P_0` (sum ≡ 4): `8 − 4 = 4`. **τ preserves `P_0`.**

Conclusion (bankable):

```text
L-CYCLE79-COMPLEMENT-INVOLUTION:
τ is a fixed-point-free involution of P_0 with Phi(τT) = K / Phi(T).
Hence the multiplicity function satisfies  m(v) = m(K/v)  for all v,
and any self-paired value (v² = K) has even fiber size.
```

This is why the coherent‑ratio reformulation alone does not bound `m_max`: it is the same fiber count viewed multiplicatively (the "coherence" of `Δ = {l_i/l_1 = r_1/r_i}` holds for *every* fiber automatically). The genuinely new constraint added this cycle is the τ‑symmetry, which pairs fibers `v ↔ K/v` but does not cap a single fiber at 12.

## 3. Code status

All code is **UNRUN** (read‑only harness; only `Read` available). The verifier below is cheap (only the 7×48 field table plus a few samples) and is safe for Codex to run to confirm §2.4–2.5.

```python
# UNRUN — Cycle 79 involution/reduction verifier. Reuses cycle68 build_u.
# Checks: (A) complement involution τ on the 48-set family,
#         (B) per-slot constant u_t(k)·u_t(τk) = 3^{-2t}(beta^32 − 9^t),
#         (C) Phi(T)·Phi(τT) = K and τ preserves P_0, on random T.
import importlib.util, itertools, random, json
from pathlib import Path
spec = importlib.util.spec_from_file_location(
    "c68", "experimental/scripts/cycle68_slot_factorization_checker.py")
c68 = importlib.util.module_from_spec(spec); spec.loader.exec_module(c68)
f = c68.find_field_poly(); eta = c68.find_eta(f); beta = c68.find_beta(f)
xi = c68.fpow(beta, 2, f); tbl = c68.build_u(f, eta, beta)
def U(t,i,a): return tbl[(t,i,a)]
def tau(i,a):                      # (i,a) -> complement set's (i',a')
    return {1:(2,(a+6)%16),2:(1,(a+10)%16),3:(3,(a+8)%16)}[i]
# (A) τ realizes set complement: B_{i,a}^c == B_{τ(i,a)}
ES=c68.E_SETS
for i in (1,2,3):
    for a in range(16):
        B={(a+e)%16 for e in ES[i]}; j,b=tau(i,a)
        assert ({(b+e)%16 for e in ES[j]}) == ({x for x in range(16)}-B)
# (B) per-slot constant
def emb(c): return c68.emb(c)
inv9=c68.fpow(emb(9),c68.N-1,f)
for t in range(1,8):
    Ct=c68.psub(c68.fpow(beta,32,f), emb(pow(9,t,17)))      # beta^32 − 9^t
    c=c68.fmul(c68.fpow(emb(pow(3,2*t,17)),c68.N-1,f),Ct,f) # 3^{-2t}·Ct
    for i in (1,2,3):
        for a in range(16):
            j,b=tau(i,a)
            assert c68.fmul(U(t,i,a),U(t,j,b),f)==c
# (C) global involution on random P0 tuples
K=c68.ONE
for t in range(1,8):
    Ct=c68.psub(c68.fpow(beta,32,f), emb(pow(9,t,17)))
    K=c68.fmul(K, c68.fmul(c68.fpow(emb(pow(3,2*t,17)),c68.N-1,f),Ct,f), f)
def color(i,a): return (c68.S_COLOR[i]+8*(a%2))%16
rng=random.Random(0); ok=0
for _ in range(200):
    T=[(rng.randint(1,3),rng.randint(0,15)) for _ in range(7)]
    if sum(color(i,a) for i,a in T)%16!=4: continue
    Tt=[tau(i,a) for (i,a) in T]
    assert sum(color(i,a) for i,a in Tt)%16==4          # τ preserves P0
    P=c68.ONE; Q=c68.ONE
    for t,(i,a) in enumerate(T,1): P=c68.fmul(P,U(t,i,a),f)
    for t,(i,a) in enumerate(Tt,1): Q=c68.fmul(Q,U(t,i,a),f)
    assert c68.fmul(P,Q,f)==K; ok+=1
print(json.dumps({"A_complement_involution":True,"B_slot_constant":True,
                  "C_global_involution_samples":ok,"decision":"INVOLUTION_OK"}))
```

The full census remains a compiled/sharded job (as Cycle 78 concluded). Cheapest exact framing: `m_max ≥ 13` iff the convolution of `A = im(W_123)` (48³ values) and `B = im(W_4567)` (48⁴) has a value of multiplicity ≥ 13 — i.e. additive energy / "12 coherent common differences." Over `Z/N` (no FFT) this is a hash‑histogram over `L×R` (≈5.9e11 products) with sharding by a hash prefix, in C, hours‑scale. Design only; UNRUN.

## 4. What remains open

- The constant `12` is unproven and no 13‑witness is exhibited. Both are census‑gated.
- Whether `m_max` is attained at a τ‑self‑paired value (`v² = K`, even fiber) or a paired value — open.
- The exact minimum distance of the collision code (Cycle 77 gives ≥ 3; is it exactly 3?) — open and feasible to settle by a bounded 3‑row product‑collision scan.
- Whether the τ‑symmetric, injective per‑row weight sets force an additive‑energy bound near 12 — open; this is the only visible route to a *non*‑census proof.

## 5. Next exact lemma or construction

Two concrete, ordered targets.

Next lemma (hand/cheap, theorem‑grade):

```text
L-CYCLE79-MINDIST-EXACT:
Decide the exact minimum distance d of the collision code
{(T,T') : Phi(T)=Phi(T')}. Cycle 77 ⇒ d ≥ 3. Run the bounded
3-row collision scan: for each unordered triple of rows {s,t,u} and the
two complementary "active vs anchor" set choices, test whether
  prod over 3 active rows = prod over 3 anchor rows  (packed key)
has any solution with the other 4 rows fixed. Output d, and if d=3 the
explicit minimal coherent Δ. This feeds a distance-based fiber filter.
```

Next construction (the real bound attempt), using §2.5:

```text
W-CYCLE79-SYMMETRIC-ENERGY-BOUND:
Each W_t : B → Z/N is injective and τ-antisymmetric: W_t(B)+W_t(τB)=c_t,
so im(W_t) is symmetric about c_t/2. Prove a multiplicity bound for the
7-fold sumset of seven such symmetric 48-sets (equivalently bound
max_S |A ∩ (S−B)| with A=im W_123, B=im W_4567, both τ-symmetric and
collision-free at distance ≥ 3). Target: max multiplicity ≤ 12, or
extract from the symmetry a small candidate set S (the τ-fixed shell
v²=K) on which to run a *bounded* exact convolution instead of the full
census.
```

The τ‑fixed shell is the most promising practical lever: by §2.5 the extremal fiber is either on `v² = K` (a small, enumerable locus once one square root of `K` is known) or comes in a `v ↔ K/v` pair, which roughly halves the census search and gives Codex a far cheaper targeted run than the blind `5.3e10`‑tuple sweep.