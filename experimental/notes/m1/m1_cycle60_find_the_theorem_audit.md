# Cycle 60 Find-The-Theorem Audit

**Date:** 2026-06-20  
**Status:** AUDIT / COUNTEREXAMPLE / CONDITIONAL / BANKABLE_LEMMA  
**Scope:** Nine theorem-worker returns from the Cycle 60 packet under
`experimental/notes/m1/cycle60_find_the_theorem_raw/`.

## Verdict

Cycle 60 is significant route repair, not a prize solve.

The round does not prove the MCA or scalar list safe-side theorem. It does,
however, change the shape of the theorem we should try to prove. Three proposed
shortcuts are now too narrow:

1. A genus-zero or projective-stabilizer split-rational quotient ledger is not
   enough. The quotient registry must include genus-one Lattes/isogeny packets.
2. A point-fiber quotient ledger is not enough for the near-balanced
   jet-residue branch. Configuration-space divisor-norm characters can save a
   condition.
3. A seed-local critical-kernel completion theorem is not a weaker intermediate
   lemma once coefficient vectors are included; it collapses to the original
   colored full-secant fiber problem.

The constructive side is also sharper: fixed-partition QAR packing,
information-set petal bounds, hereditary MDS-3-core extraction, the `t=1`
apolar complete-intersection normal form, and scalar list circuit transversals
all give cleaner finite objects for the next route board.

## Main Route Changes

### 1. Lattes / Genus-One Quotient Branch

Raw files:

- `01_lattes_degree31_counterpacket.md`
- `02_lattes_degree113_counterpacket.md`

Two independent returns propose finite official-style counterpackets based on
elliptic-isogeny Lattes maps. The first uses a degree-31 construction; the
second uses a degree-113 CM-Lattes construction. Both claim large transverse
MCA slope sets while ordinary monomial, toric, and projective-subline
quotient tests miss the packet.

Conservative classification:

```text
COUNTEREXAMPLE / EXACT_NEW_WALL / VERIFY_ARITHMETIC
```

If the arithmetic checks out, the quotient taxonomy should be organized by
Galois-closure geometry:

```text
g = 0: PGL2 subgroup-chain quotients
g = 1: generalized Lattes / elliptic-isogeny quotients
g >= 2: primitive finite-discrepancy branch
```

New wall labels:

```text
W-SRQ-GENUS-0/1-MONODROMY-CONTAINER
W-MCA-LATTES-SPLIT-RATIONAL-QAR-COVER
W-SRQ-HIGH-GENUS-FROBENIUS-DISCREPANCY-CONTAINER
```

Bankable sublemmas suggested by the returns:

- Three full projective-subline fibers force descent after target Mobius
  transformation.
- Split-fiber Galois-closure point budget:
  `s_R |G| <= #X_R(K) <= q0 + 1 + 2 g_R sqrt(q0)`.
- Low-genus taxonomy: genus zero gives PGL2 quotient chains; genus one gives
  Lattes/isogeny quotient chains.

These should be independently checked before promotion.

### 2. Fixed-Partition And Fixed-Core QAR Bounds

Raw files:

- `03_fixed_partition_qar_packing.md`
- `04_fixed_core_petal_bound.md`

These are useful because they replace an over-strong "cover every
fixed-defect packet literally" demand with denominator-free support-counting
theorems.

Conservative classification:

```text
BANKABLE_LEMMA / ROUTE_CUT
```

Main bankable statements:

- Fixed-partition QAR packing:
  for a fixed equal-fiber partition `pi:L -> Omega`, envelope-clean retained
  quotient slopes satisfy
  `|Z_pi| <= (n/sigma) binom(N-1, k/M)`, capped by `|F|`.
- Information-set petal theorem:
  fixing a `k`-point core `U`, slopes with at least `s` extra agreements have
  at most `floor((r-c_U)/(s-c_U))` petals; envelope-free lines give
  `floor(r/s)`.
- Fixed-core QAR bound:
  one equal-fiber quotient system contributes at most
  `floor(r/s) binom(N, k/M)` slopes before the field-size cap.

Route impact: the quotient term should be support-theoretic and partition
based, not primarily a denominator action-rank statement.

### 3. Divisor-Norm / Configuration-Space Characters

Raw file:

- `05_divisor_norm_character_counterpacket.md`

This cuts the proposed
`W-JR-PRIMITIVE-CRITICAL-KERNEL-COMPLETION` in its current form. The return
constructs a `t=1 < sigma` packet using the product character of the error
locator:

```text
T |-> c0(L_T) = (-1)^j prod_{x in T} x
```

This is a quotient on the configuration space `Sym^j(H)`, not on individual
evaluation points. It can save one condition and produce many more slopes than
the occupancy term alone predicts.

Conservative classification:

```text
COUNTEREXAMPLE / ROUTE_CUT / EXACT_NEW_WALL
```

New wall:

```text
W-JR-CORANK-ONE-DIVISOR-NORM-CHARACTER-TRICHOTOMY
```

Corrected ledger must include at least:

```text
occupancy
+ point-fiber quotients
+ divisor-norm / configuration characters
+ envelopes
+ remaining primitive discrepancy
```

### 4. Hereditary MDS-3-Core Extraction

Raw file:

- `06_hereditary_mds_3_core.md`

This does not prove the full primitive container theorem, but it isolates a
canonical obstruction. Every sufficiently large envelope-free packet contains
a low-degree split-locator syzygy whose thinned agreement hypergraph is a
3-core.

Conservative classification:

```text
BANKABLE_LEMMA / EXACT_NEW_WALL
```

New wall:

```text
W-MCA-FINITE-CRITICAL-SEED-H2-DEFECT-CHARGE
```

This reframes the primitive MCA problem: after quotient and envelope removal,
large unexplained packets should be charged through H2-defective critical seed
containers or by occupancy.

### 5. `t=1` Apolar Complete-Intersection Normal Form

Raw file:

- `07_t1_apolar_split_numerator.md`

This return is important because it shows that the lowest jet-residue stratum
is already ordinary RS decoding for dimension `k+1`, with an external
evaluation color. It gives a canonical apolar complete-intersection form for
the unresolved `t=1` problem.

Conservative classification:

```text
BANKABLE_LEMMA / ROUTE_CUT
```

Route cut: the proposed critical-seed completion lemma is not a weaker next
step; once a full-coordinate seed fixes the syndrome, completions are just the
original colored syndrome-fiber count minus the seed.

New wall:

```text
W-JR-T1-PRIMITIVE-APOLAR-SPLIT-NUMERATOR-INVERSE
```

This is the correct next exact base case before trying general fat-infinity
or `1 < t < sigma` jet-residue statements.

### 6. Scalar List Circuit Transversal

Raw file:

- `08_scalar_list_circuit_transversal.md`

This tightens the grand list branch. The interleaved projection theorem is
still treated as closed in the same-field official target regime, and the
remaining scalar list problem is expressed as a low-arity full-support circuit
transversal problem.

Conservative classification:

```text
BANKABLE_LEMMA / COUNTEREXAMPLE / EXACT_NEW_WALL
```

Bankable objects:

- Exact scalar full-support identity:
  actual list size is a maximum over canonical nonzero-error syndrome
  representations, not raw feasible padded supports.
- Full-support circuit reduction:
  if a set hits all full-support circuits, the remaining list contributes at
  most `floor((r-1)/sigma)` codewords.
- Overagreement is weighted by actual reserve `tau(P)`, not handled by a
  separate crude layer sum.

New wall:

```text
W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER
```

The file also gives a non-official-domain star/Sidon packet showing that
split-rational quotient plus common-core containers alone cannot be a general
scalar list theorem; low-affine-rank polynomial envelopes are necessary.

### 7. Minimal Finite Container Package

Raw file:

- `09_finite_container_package.md`

This is a useful referee-style package. It says the exact safe-side theorem
should be denominator-free:

```text
M_C(sigma) = max over syndrome lines of transverse secant intersections
L_C(sigma) = max over syndromes of actual scalar full-support lists
```

It also introduces a finite projective-subline counterpacket showing that
split-rational closure and the equality scale `M = sigma` are mandatory.

Conservative classification:

```text
CONDITIONAL / COUNTEREXAMPLE / AUDIT
```

Main corrected target:

```text
quotient container = realized split-rational block system
```

not:

```text
quotient container = denominators with low d_M(E)
```

The finite theorem package is not close. It still needs:

- support-theoretic split-rational cover;
- hereditary envelope branching;
- primitive occupancy/discrepancy;
- scalar list circuit cover;
- exact integer comparison with `floor(q / 2^128)`.

## Current Best Next Lemmas

The next route should not try another broad "solve everything" statement. It
should split into verifiable modules:

1. **Verify the Lattes arithmetic.**
   Check the elliptic curve orders, subgroup sizes, full fibers, slope counts,
   noncontainment, and official field/domain admissibility in the degree-31 and
   degree-113 packets.

2. **Build the split-rational / Lattes registry.**
   Formalize:
   ```text
   W-SRQ-GENUS-0/1-MONODROMY-CONTAINER
   ```
   with finite packet charges by full-fiber profile and action-rank metadata.

3. **Prove the support-theoretic split-rational cover.**
   For one envelope-free affine syndrome line, show large realized
   split-rational containers can be covered with bounded total profile weight,
   or the varying defects generate a hereditary envelope.

4. **Attack the divisor-norm trichotomy.**
   Formalize:
   ```text
   W-JR-CORANK-ONE-DIVISOR-NORM-CHARACTER-TRICHOTOMY
   ```
   for corank-one JR degeneracy.

5. **Resolve the `t=1` apolar base case.**
   Formalize:
   ```text
   W-JR-T1-PRIMITIVE-APOLAR-SPLIT-NUMERATOR-INVERSE
   ```
   before trying the full fat-infinity jet-residue theorem.

6. **Scalar list circuit cover.**
   Formalize:
   ```text
   W-LIST-LOW-ARITY-SPLIT-DENOMINATOR-CIRCUIT-COVER
   ```
   and include low-affine-rank envelope circuits, not only quotient/core
   packets.

## Bottom Line

Cycle 60 is one of the more important route-repair rounds so far. It does not
make the problem "close" in the one-lemma sense. It does make the map more
honest: quotient structure is broader than previously stated, primitive
remainders need configuration-character and H2-core handling, and scalar list
decoding has a sharper full-support circuit formulation.
