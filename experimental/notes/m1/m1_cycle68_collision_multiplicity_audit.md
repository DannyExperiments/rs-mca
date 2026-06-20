# Cycle 68 Collision Multiplicity Audit

## Verdict

```text
BANKABLE_LEMMA / EXACT_NEW_WALL / PLAN
```

Confidence: high for the disjoint-coset factorization and local checker;
unknown for the final bound `m_max(beta) <= 12`.

Cycle 68 does not prove the decision target

```text
m_max(beta) <= 12.
```

It also does not find a 13-fold collision. It banks a stronger structural
reduction:

```text
L-CYCLE68-DISJOINT-COSET-FACTORIZATION
```

and makes the remaining wall a seven-slot sumset-multiplicity problem over the
336-entry slot table.

## Banked Lemma

Let

```text
F = F_17[X] / (X^16 + X^8 + 3),
eta = 6 X^9,
beta = X + 2,
xi = beta^2.
```

For a tuple `T in P_0`, encoded by choices `(i_t,a_t)` for `t=1,...,7`, put

```text
B_t = (a_t + E_{i_t}) mod 16,   |B_t|=8.
```

Cycle 68 proves:

```text
rho_beta(T)
 = (beta - 1) * prod_{t=1}^7 prod_{b in B_t}
     (beta^2 - eta^(2t + 16b)).
```

The constant is exactly `beta - 1`.

Consequences:

1. Slot `t` only uses roots with logarithm congruent to `2t mod 16`.
   For `t=1,...,7`, these residue classes are pairwise disjoint.
2. The 112 slot roots are exactly `mu_128 \\ mu_16`; the anchor `beta-1`
   accounts for the missing `mu_16` direction.
3. The color is the set-sum:

```text
color_t = sum_{b in B_t} b mod 16 = s_i + 8(a_t mod 2).
```

4. The map from admissible tuples to set-tuples `(B_1,...,B_7)` is bijective.
5. The full problem reduces to a sevenfold product/sumset over 336 table
   entries:

```text
Occ(beta)
 = #{ prod_t u_t(B_t) : sum_t color_t(B_t) = 4 mod 16 }.
```

## Local Verification

Codex saved and ran:

```text
experimental/scripts/cycle68_slot_factorization_checker.py
```

The checker validates:

- all 336 slot factorizations;
- 16 random brute-force support products against the factorization;
- distinctness of the 48 translated slot sets;
- color equals set-sum mod 16;
- the full slot-product oracle
  `prod_{b in Z/16}(beta^2 - eta^(2t+16b)) = beta^32 - 3^(2t)`;
- single-slot injectivity;
- a small certified lower-bound probe for multiplicity.

Local certificate:

```text
experimental/notes/m1/cycle68_slot_factorization_certificate.json
```

The certificate decision is:

```text
REDUCTION_VERIFIED__FULL_MMAX_REQUIRES_COMPILED_RUN
```

The lower-bound probe observed `m_max_lower_bound_probe=1`; this is not a proof
of the global upper bound.

## Remaining Wall

The exact remaining wall is:

```text
W-CYCLE68-SLOT-SUMSET-MULTIPLICITY
```

Equivalently, in discrete-log coordinates:

```text
L-CYCLE68-SLOT-LOG-INDEPENDENCE
```

Bound short relation multiplicity among the 112 elements

```text
beta^2 - eta^(2t + 16b),
  t=1,...,7, b in Z/16,
```

subject to the admissible slot/set constraints.

The decision target remains:

```text
m_max(beta) <= 12
```

because Cycle 67 banked:

```text
Occ(beta) >= |P_0| / m_max(beta),
|P_0| / 12 > 2^32,
|P_0| / 13 < 2^32.
```

## Next Action

Stage Cycle 69 on either:

1. a structural proof or counterpacket for `L-CYCLE68-SLOT-LOG-INDEPENDENCE`;
2. or a concrete bounded-multiplicity compiled verifier design that certifies
   `m_max(beta) <= 12` without materializing the full `>2^32` occupied-value
   set.

The second path is decisive if implemented in C/Rust; the first path is the
remaining symbolic hope.

