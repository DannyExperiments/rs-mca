# Cycle 84 finite wall: exact proof that \(m_{\max}(\beta)=2\)

## Verdict

For the explicit Cycle 84 seven-slot product/color model over

\[
F=\mathbf F_{17}[X]/(X^{16}+X^8+3),\qquad \eta=6X^9,\qquad \beta=X+2,
\]

the color-filtered product multiplicity satisfies

\[
\boxed{m_{\max}(\beta)=2}.
\]

In particular, \(m_{\max}(\beta)\le 12\). This resolves the Cycle 84 finite MITM wall. It is a model-level theorem, not by itself a prize-level resolution.

## Exact census theorem

With left slots \(\{1,2,3\}\), right slots \(\{4,5,6,7\}\), and color target
\(c_L+c_R\equiv4\pmod {16}\), the exact census is

| quantity | exact value |
|---|---:|
| compatible left/right pairs | 52,747,567,104 |
| distinct products | 52,747,567,092 |
| singleton product fibers | 52,747,567,080 |
| double product fibers | 12 |
| fibers of multiplicity \(\ge3\) | 0 |
| ordered off-diagonal collision count \(D\) | 24 |
| \(m_{\max}(\beta)\) | 2 |

Thus the exact model occupancy is 52,747,567,092, exceeding \(2^{32}\) by 48,452,599,796.

## Proof

### 1. Exact logarithmic reduction

The multiplicative group \(F^*\) has order

\[
N=17^{16}-1=48,661,191,875,666,868,480
 =2^8 3^2\cdot5\cdot29\cdot18913\cdot41761\cdot184417.
\]

The element \(\gamma=X+1\) is primitive. For every one of the 336 nonzero slot values \(u_t(i,a)\), an exponent
\(\lambda_t(i,a)\in\mathbf Z/N\mathbf Z\) was computed and then independently checked by exact field arithmetic:

\[
\gamma^{\lambda_t(i,a)}=u_t(i,a).
\]

Consequently, for any seven-slot tuple \(q=(q_1,\ldots,q_7)\),

\[
\prod_{t=1}^7u_t(q_t)=
\gamma^{\Lambda(q)},\qquad
\Lambda(q)=\sum_{t=1}^7\lambda_t(q_t)\pmod N.
\]

Because \(\gamma\) is primitive, two seven-slot products are equal if and only if their log sums are congruent modulo \(N\).

The standard-library verifier proves irreducibility of \(X^{16}+X^8+3\), verifies the factorization of \(N\), verifies primitivity of \(\gamma\), reconstructs all 336 slot values from the defining polynomials, and checks all 336 exponent identities and colors.

### 2. Exact MITM representation

The banked three-slot and four-slot product injectivity results imply that tuple enumeration and image enumeration agree on both sides. The checker constructs all

\[
|L|=48^3=110,592,\qquad |R|=48^4=5,308,416
\]

records, storing their exact log sum and color. Right records are sorted in 16 color buckets. For each left record of color \(c\), only the right bucket of color \(4-c\pmod {16}\) is used.

The independent color-class count gives exactly

\[
\sum_{c\in\mathbf Z/16\mathbf Z}|L_c|\,|R_{4-c}|=52,747,567,104
\]

compatible pairs.

### 3. Exhaustive, collision-safe sharding

The log group \([0,N)\) is partitioned into 1,536 disjoint half-open intervals

\[
I_s=\left[\left\lfloor\frac{Ns}{1536}\right\rfloor,
          \left\lfloor\frac{N(s+1)}{1536}\right\rfloor\right),
\quad 0\le s<1536.
\]

For every left record \(x\) and compatible right color bucket, binary search enumerates exactly the right sums \(y\) for which \((x+y)\bmod N\in I_s\). Translation by \(-x\) produces either one ordinary interval or two wraparound intervals, so no candidate is omitted or duplicated.

Within a shard, the exact key is the full offset

\[
d=(x+y\bmod N)-\min I_s.
\]

The largest shard width is

\[
\left\lceil N/1536\right\rceil=31,680,463,460,720,618<2^{55}.
\]

Hence \(d+1\) fits completely in the low 56 bits of the table entry; the high 8 bits hold the exact multiplicity. The 64-bit mixing function is used only to choose the initial probe location. Equality is tested on the full offset, and linear probing resolves hash collisions. Therefore hash collisions cannot create false product collisions or hide real ones. The checker aborts immediately at multiplicity 13; otherwise it records the exact maximum.

All 1,536 shards completed. Their compatible-pair counts sum to 52,747,567,104, proving complete coverage. The maximum count in any exact key was 2.

### 4. Exact aggregate checks

The aggregate values were

\[
P=52,747,567,104,\qquad U=52,747,567,092,\qquad D=24.
\]

Already \(D=24\le155\) invokes the banked Cycle 69/80 energy gate and proves the requested bound \(m_{\max}\le12\). The exact unique count sharpens this further. For any fiber histogram \(m(v)\),

\[
P-U=\sum_{m(v)>0}(m(v)-1),\qquad
D=\sum_v m(v)(m(v)-1).
\]

Therefore

\[
D-2(P-U)=\sum_{m(v)>0}(m(v)-1)(m(v)-2).
\]

The exact census gives \(P-U=12\) and \(D=24\), so the left side is zero. Every summand on the right is a nonnegative integer. Hence every occupied fiber has multiplicity 1 or 2. This proves \(m_{\max}\le2\) independently of the checker's separately recorded maximum field. The explicit double witness below gives equality.

It follows that there are exactly 12 double fibers and all other occupied fibers are singletons. The Cycle 79 involution has no occupied self-dual fiber; accordingly the double fibers occur in six involution pairs and \(D\equiv0\pmod4\), as observed. An independent sort-and-run-length reducer agrees with the hash reducer both on collision-free audit shard 0 and on collision shard 25, where it independently returns 34,337,925 pairs, 34,337,924 distinct keys, \(D=2\), and maximum 2.

### 5. Explicit witness that the maximum is at least 2

Both following color-compatible seven-slot tuples have product log

\[
814,364,899,710,808,391
\]

and product field coefficients

\[
(3,16,6,13,15,10,10,11,8,5,12,9,13,6,4,3).
\]

First tuple:

\[
((1,4),(2,10),(3,14),(1,12),(3,0),(2,6),(3,8)).
\]

Second tuple:

\[
((2,0),(2,11),(1,7),(1,1),(3,9),(2,8),(1,14)).
\]

Their total colors are both 4 modulo 16, and they differ in all seven slots, consistent with the banked minimum-distance-5 certificate. Exact field multiplication verifies that their products agree. Combined with the exhaustive upper bound \(m_{\max}\le2\), this proves \(m_{\max}=2\).

## Reproduction

Run the exact slot-log verifier:

```bash
python3 cycle84_verify_discrete_logs_stdlib.py
```

Compile and run the self-contained exact checker:

```bash
g++ -O3 -std=c++17 -pthread cycle84_exact_mmax_checker.cpp -o cycle84_exact_mmax_checker
./cycle84_exact_mmax_checker 0 1536 1536 4 full_certificate.json
```

The required output fields are:

```text
compatible_pairs      = 52747567104
distinct_products     = 52747567092
D_offdiagonal_ordered = 24
m_max                 = 2
hit_value_log         = null
```

## Next exact bankable statement

**L-CYCLE84-EXACT-COLOR-FILTERED-MMAX.** For the explicit Cycle 84 model at \(\beta=X+2\), the color-filtered product-fiber histogram is

\[
n_1=52,747,567,080,\qquad n_2=12,\qquad n_j=0\ (j\ge3).
\]

By the already-banked Cycle 65/66 nonzero scalar factorization, the corresponding exact thickened-color occupancy is 52,747,567,092. The next construction is to enter this exact model certificate, its assumptions, and its threshold comparison into the finite frontier ledger.
