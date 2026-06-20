# Cycle 76 Right-Half And Direct Mmax Audit

## Verdict

```text
BANKABLE_LEMMA / PROOF / PLAN
```

Confidence: high for the local right-half product-injectivity certificate and
the one-sided fiber reduction; unknown for the full `m_max(beta)<=12` target.

Cycle 76 does **not** prove:

```text
m_max(beta) <= 12.
```

It does close the MITM product-injectivity split:

```text
left  slots {1,2,3}: 48^3 = 110592 products, all distinct;
right slots {4,5,6,7}: 48^4 = 5308416 products, all distinct.
```

The left half was already certified in Cycle 75. Codex locally added and ran a
faster right-half checker after the Cycle 76 Fable answer returned with only
read-only tool access.

## Banked Lemmas / Certificates

### L-CYCLE76-ONE-SIDED-INJECTIVE-FIBER-REDUCTION

Let

```text
A = {prod_{t=1}^3 u_t(k_t)}
B = {prod_{t=4}^7 u_t(k_t)}.
```

Using only left-half product injectivity, every product fiber in the constrained
domain `P_0` injects into

```text
{T_R : v / prod(T_R) in A}.
```

After the local right-half certificate, both `A` and `B` are honest sets, so
the remaining target is the exact product-set intersection bound:

```text
m_max(beta) <= max_v |A cap v B^{-1}|.
```

The color condition defining `P_0` can only reduce this upper bound. The proof
is the direct map from a fiber witness `(T_L,T_R)` to `T_R`; left injectivity
gives at most one compatible `T_L`.

### L-CYCLE76-RIGHT-HALF-PRODUCT-INJECTIVITY

Codex added:

```text
experimental/scripts/cycle76_fast_right_half_check.py
```

and ran it locally. It specializes multiplication to the banked modulus:

```text
X^16 + X^8 + 3,
```

and checks equality by packed field product only.

Certificate:

```text
experimental/notes/m1/cycle76_right_half_mmax_raw/cycle76_fast_right_half_certificate.json
```

The certificate says:

```text
right_45:   2304 products, all distinct;
right_67:   2304 products, all distinct;
right_4567: 5308416 products, all distinct;
decision: RIGHT_HALF_PRODUCT_INJECTIVE.
```

This is an executed local certificate, unlike the read-only Fable-returned code.

## Raw Fable Answer Status

The Cycle 76 Fable answer is banked raw at:

```text
experimental/notes/m1/cycle76_right_half_mmax_raw/
```

The worker again exposed only `Read`; it could not execute or write files. Its
inline checker is therefore `UNRUN`. The bankable part of that answer is the
one-sided reduction and the exact next-step schema. The executed certificate is
Codex-local.

## Remaining Wall

The live finite model wall is now:

```text
V-CYCLE77-AB-PRODUCT-MAXFIBER
W-CYCLE77-MAX-INTERSECTION-A-B-INVERSE
```

Explicitly, with both sides product-injective, prove:

```text
max_v |A cap v B^{-1}| <= 12,
```

or find an explicit `13`-fold collision in the original constrained domain
`P_0`.

Equivalently, the remaining object is a seven-slot product-set incidence, not
another injectivity-ladder rung.

## What To Do Next

Cycle 77 should attack the exact max-intersection problem. Acceptable outputs:

1. `PROOF`: a source-valid proof that `max_v |A cap v B^{-1}| <= 12` or,
   better, `m_max(beta)<=12`;
2. `COUNTERPACKET`: a concrete `13`-fold fiber in `P_0`;
3. `BANKABLE_LEMMA`: an exact reduction that makes the max-intersection check
   substantially smaller than `|A||B|`;
4. `PLAN`: compiled/sharded census code is useful only if paired with a clear
   certificate schema. Unrun code alone is not a proof.
