# Cycle 78 Exact Mmax Census Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / PLAN
```

Confidence: high for the left-right incidence reduction and the route cut;
unknown for the exact finite value of `m_max(beta)`.

Cycle 78 does **not** prove:

```text
m_max(beta) <= 12.
```

It also does not produce a `13`-fold packet. The worker again had only `Read`
tool access, so all returned code is `UNRUN`.

## Banked Lemma

### L-CYCLE78-LR-INCIDENCE-REDUCTION

Let

```text
L(k_1,k_2,k_3)=u_1(k_1)u_2(k_2)u_3(k_3),
R(k_4,k_5,k_6,k_7)=u_4(k_4)u_5(k_5)u_6(k_6)u_7(k_7).
```

By Cycle 75 and Cycle 76, both maps are product-injective. Hence for each
field value `v`,

```text
m(v) =
#{ l in L_img : v l^{-1} in R_img
   and colorL(l)+colorR(v l^{-1}) = 4 mod 16 }.
```

Thus the finite target is exactly an incidence problem between the left product
set and multiplicative translates of the right product set, with the color
condition as a filter. Equality remains packed field product only.

## Route Cut

A hand proof of the numerical constant `12` has not emerged. Cycle 78 argues
that the route is now computational or requires a new finite product-set
incidence theorem. Subset-injectivity ladders can certify product-fiber
distance and give ceilings such as `m_max<=48`, but do not reach `12` by
themselves.

The next proof-level non-computational wall is:

```text
L-CYCLE79-COMMON-RATIO-BOUND
```

where a fiber of size `m` yields a coherent set

```text
Delta subset Ratios(L_img) cap Ratios(R_img)
```

of size `m`, and the desired conclusion is `|Delta|<=12` or `<=11`
depending on normalization.

## Returned Code Status

The answer included Python/C sketches for a sharded exact census. They are
useful as design notes only. They were not executed and were not written into
`output_files` by the worker.

## Remaining Wall

```text
V-CYCLE79-COMMON-RATIO-BOUND-OR-CENSUS
W-CYCLE79-COHERENT-RATIO-SET-SIZE
```

Acceptable next progress:

1. Prove a coherent ratio-set bound giving `m_max<=12`.
2. Find an explicit coherent ratio set of size `13`, yielding a
   counterpacket target.
3. Produce a theorem-grade exact census implementation plus a small executable
   certificate format that Codex can run locally in bounded shards.

## What To Do Next

Stage Cycle 79 against the common-ratio formulation. This is narrower than
asking again for broad exact census code and gives the worker a concrete
finite theorem to prove or kill.

## Local Follow-Up

Codex added and ran:

```text
experimental/scripts/cycle78_lr_incidence_sanity.py
experimental/notes/m1/cycle78_lr_incidence_sanity_certificate.json
```

This is only a bounded sanity check, not a proof of `m_max<=12`. It verifies on
25 deterministic sample pairs that:

```text
full product = left product * right product
full color = left color + right color mod 16
```

with equality keyed by packed field product and color used only as the domain
filter. The certificate decision is:

```text
LR_INCIDENCE_SAMPLE_PASS
```
