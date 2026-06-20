# Cycle 72 Product-Only Ladder Audit

## Verdict

```text
AUDIT / BANKABLE_LEMMA / PLAN
```

Confidence: high that the response preserves the correct product-only
semantics and gives a valid collision-energy decomposition; unknown for the
`k=3/k=4` product-injectivity rungs, because no verifier was executed and no
collision was found.

Cycle 72 does **not** prove or kill:

```text
V-CYCLE71-PRODUCT-ONLY-K3-K4-LADDER-RUN
```

The worker only had read-only tools. It supplied reference Python/C verifier
code inline, but marked it `UNRUN`. Therefore this return is not a certificate
that `k=3` or `k=4` passes.

## Banked Lemma

### L-CYCLE72-DISPLACEMENT-ENERGY-DECOMPOSITION

Let

```text
F(T)=prod_{t=1}^7 u_t(T_t)
```

on the seven 48-value slot domains, and let

```text
D = #{ordered off-diagonal pairs (T,T') : F(T)=F(T')}.
```

For a subset `S` of slots, define `E_S` to be the ordered fully displaced
collision energy on `S`:

```text
E_S = #{(B_S,B'_S):
  B_t != B'_t for every t in S,
  prod_{t in S} u_t(B_t)=prod_{t in S} u_t(B'_t)}.
```

Then

```text
D = sum_{S subset {1,...,7}} 48^(7-|S|) E_S.
```

If every `s`-subset slot map is product-injective, then `E_S=0` for
`|S|<=s`, so only supports of size at least `s+1` survive. In particular, if
the product-only ladder passes through `k=4`, then only the `|S|=5,6,7`
terms remain:

```text
D = 2304 * sum_{|S|=5} E_S
  + 48   * sum_{|S|=6} E_S
  +        E_{1,...,7}.
```

This makes the next decisive model-level route exact:

1. prove `k=5` product-injectivity, otherwise any `E_S>=1` at `|S|=5` gives
   `D>=2304>155` and kills the `D<=155` route;
2. bound the six-slot fully displaced energies by total at most `3`, or
   preferably prove they vanish;
3. count the full seven-slot energy and check whether
   `D<=155`.

Together with Cycle 69's gate

```text
D <= 155 => m_max <= 12 => Occ(beta) >= |P_0|/12 > 2^32,
```

this is the correct finite arithmetic ladder below the Role 05 model packet.

## Route Status

The active wall remains:

```text
V-CYCLE71-PRODUCT-ONLY-K3-K4-LADDER-RUN
W-CYCLE69-SLOT-SUMSET-COLLISION-ENERGY
```

Cycle 72 confirms two route cuts already in force:

- Do not use the false Cycle 70 t-independent collapse.
- Do not key duplicate detection by `(color, product)` unless product equality
  is separately proved to force color equality.

It also gives a useful obstruction to the cheap color route: product equality
does not obviously determine the `Z/16` color for `k>=2`, and the Frobenius
action moves `xi=beta^2`, so the obvious Galois symmetry is not a symmetry of
the actual relation.

## Local Follow-Up

Codex attempted the existing product-only Python checker through `k=3`:

```text
python3 experimental/scripts/cycle71_product_ladder_checker.py --kmax 3
```

It did not finish inside a 30-second heartbeat bound and was terminated. No
partial output was banked. The only executed local product-only ladder
certificate remains the prior `k<=2` certificate:

```text
experimental/notes/m1/cycle71_product_ladder_certificate.json
```

## Next Prompt

Stage Cycle 73 against:

```text
V-CYCLE72-COMPILED-PRODUCT-ONLY-LADDER-AND-ENERGY
```

The next worker must either:

1. provide a genuinely executable product-only verifier with exact preimage
   recovery for `k=3/k=4`, preferably with a `k=5` extension plan;
2. prove a structural product-only rung;
3. output an explicit product collision.

No unrun pass should be accepted as evidence.

