# Cycle 84 exact certificate pipeline

## Decision target

For the Cycle 68 model, compute

\[
m(v)=\#\{(k_1,\dots,k_7):\sum_t c(k_t)=4\pmod {16},\ \prod_tu_t(k_t)=v\}
\]

and either certify `max_v m(v) <= 12` or emit thirteen raw witnesses for one
common product.

## Exact model

- `F = F_17[X]/(X^16 + X^8 + 3)`; coefficients are stored little-endian.
- `N = 17^16-1 = 48,661,191,875,666,868,480`.
- `g = 1+X`; the program verifies `g^N=1` and `g^(N/q)!=1` for
  `q in {2,3,5,29,18913,41761,184417}`. Hence `g` has order `N`; since the
  quotient has `17^16` elements, this also verifies that the quotient is a
  field and that every nonzero element has a unique exponent in `[0,N)`.
- `eta=6X^9`, `beta=X+2`; the program verifies `ord(eta)=256`, `eta^16=3`,
  and `beta^256 != 1`.
- The 48 states in every slot are generated from the Cycle 68 formula, not
  loaded from an opaque table:

  `u_t(i,a)=(-1)^a p_i(beta^2 3^{-a} eta^{-2t})`,

  with the three banked degree-8 polynomials and colors
  `c(i,a)=s_i+8(a mod 2) mod 16`.

## Bankable linearization lemma

The group order factors as

`N = 256 * 9 * 5 * 29 * 18913 * 41761 * 184417`.

The program computes every state discrete logarithm by deterministic
Pohlig-Hellman, using a complete lookup table in each of these seven coprime
factors, reconstructs by CRT, and verifies `g^e=u_t(i,a)` independently for
all 336 states.

Thus every compatible seven-slot product has the exact canonical key

`E = sum_t e_t(k_t) mod N`, `0 <= E < N`,

and field multiplication in the 52,747,567,104-pair census is replaced by one
66-bit modular addition.

Canonical setup hashes from the executed self-test:

- state records: `4cb6ea024522568419f1e5c51d18f38bde78ca14dfdce950411a907af982b497`
- left records:  `0fbb49337f20496968c07b9a62e49d1b92e304a0ec32e4d9da785181e28d2ffe`
- right records: `27615bb17707290e43dd8d1f1496eb94889b8f66b917308a847ebb2a67466a89`

## Zero-false-negative exact-max reduction

For canonical `E in [0,N)`, define `fp(E)=E mod 2^64`.

1. Equal field products have equal canonical exponents, hence equal
   fingerprints.
2. Therefore every exact fiber of size at least two lies inside a repeated
   fingerprint run.
3. Since `N<3*2^64`, one fingerprint has at most three possible exact keys:
   `fp`, `fp+2^64`, `fp+2*2^64` (discarding values `>=N`).
4. Stage 1 enumerates every compatible pair exactly once, external-sorts all
   fingerprints, and records every fingerprint whose run length is at least
   two.
5. Stage 2 re-enumerates every compatible pair and, only for those repeated
   fingerprints, counts the full 66-bit exponent and retains the first
   thirteen pair indices.
6. The finalizer checks that the three exact subcounts for every repeated
   fingerprint sum back to its Stage-1 run length. It then knows every
   non-singleton exact fiber. Consequently it computes the exact `m_max`, not
   just an upper bound.

No probabilistic assumption is used. Fingerprint collisions cause extra replay
work only; they cannot remove a true collision.

## Record and shard format

Stage 1 uses 256 shards. The shard is bits 63..56 of `fp(E)`. The file payload
stores bits 55..0 in seven little-endian bytes. Equal fingerprints always enter
one shard.

Exact Stage-1 payload:

`52,747,567,104 * 7 = 369,232,969,728 bytes = 343.875 GiB`.

Each shard reducer reconstructs the full 64-bit fingerprint, performs an exact
four-pass radix sort on the 56-bit payload, and emits:

- record count;
- distinct fingerprint count;
- repeated fingerprint count;
- maximum projected run;
- SHA-256 of the canonical sorted full-64-bit stream;
- all `(fingerprint, projected_count)` records with count at least two.

## Commands

Compile:

```bash
g++ -O3 -std=c++17 -march=native cycle84_mitm_certificate.cpp \
  -o cycle84_mitm_certificate
```

Executed setup check:

```bash
./cycle84_mitm_certificate selftest cycle84_selftest.json
```

For `W` independent emit/replay workers:

```bash
mkdir -p RUN
for w in $(seq 0 $((W-1))); do
  ./cycle84_mitm_certificate emit RUN "$w" "$W" &
done
wait

for s in $(seq 0 255); do
  ./cycle84_mitm_certificate reduce-shard RUN "$s" "$W" &
  # throttle this loop to the number of shards that fit RAM
 done
wait

./cycle84_mitm_certificate merge-reduce RUN "$W"

for w in $(seq 0 $((W-1))); do
  ./cycle84_mitm_certificate replay RUN "$w" "$W" &
done
wait

./cycle84_mitm_certificate finalize RUN "$W"
```

The emit and replay commands partition the 110,592 left rows by a deterministic
contiguous interval. Their union is disjoint and exhaustive.

## PASS certificate

`RUN/certificate/PASS_mmax.json` contains:

- exact `m_max`;
- model constants;
- setup table hashes;
- fingerprint definition;
- number of repeated fingerprints;
- number and hash of all exact nontrivial fibers;
- reference to `RUN/reduce/manifest.json`.

`RUN/reduce/manifest.json` contains all 256 shard summaries and canonical
sorted-stream hashes. The finalizer refuses PASS unless:

- Stage 1 contains exactly `P0=52,747,567,104` records;
- replay contains exactly the same number of scanned compatible pairs;
- every repeated fingerprint's replay total equals its Stage-1 run length;
- the exact maximum is at most 12.

## FAIL certificate

`RUN/certificate/FAIL_13_packet.json` contains:

- the common canonical exponent and 16 field coefficients;
- thirteen distinct `(left_index,right_index)` pairs;
- all seven raw `k`, `(i,a)`, colors, state coefficients, and state logs;
- left, right, and full field products for every representation;
- left, right, and total color sums.

The finalizer recomputes every listed product both as `g^E` and by direct
multiplication of the seven field states before writing the packet.

## Independent replay

1. Check the source SHA-256 and compile with another C++17 compiler.
2. Run `selftest`; require the three canonical setup hashes above.
3. Regenerate emit parts with any worker count. Worker count may differ because
   reducer hashes are taken after canonical per-shard sorting.
4. Require all 256 sorted-stream hashes and summaries to match.
5. Rerun replay/finalize; require the candidate reconciliation checks and final
   exact-fiber hash to match.
6. For a FAIL packet, a small independent checker can ignore discrete logs and
   directly multiply the seven listed coefficient vectors modulo
   `X^16+X^8+3`, checking common product and color 4 thirteen times.

## Resource envelope

- Setup tables: below 0.2 GiB RAM.
- Stage 1 scratch: exactly 343.875 GiB plus filesystem metadata.
- One shard: about 1.34 GiB payload on average; radix reducer uses roughly
  3.2 GiB RAM for two `uint64` arrays.
- Stage 2: normally tiny; memory is proportional to the number of repeated
  64-bit fingerprints. A resource exhaustion abort is not a certificate.
- Arithmetic pass: 52.75 billion exact 66-bit additions, twice; no field
  multiplication occurs in the large scan.

## Status

The self-test and a one-million-record smoke shard were executed successfully.
The full 52.75-billion-record census is **UNRUN** here. No `m_max<=12` claim and
no counterpacket claim is made until `finalize` emits one of the two certificate
files above.
