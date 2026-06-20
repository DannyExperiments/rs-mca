# Cycle 79 Common-Ratio Bound Audit

## Verdict

```text
BANKABLE_LEMMA / ROUTE_CUT / PLAN
```

Confidence: high for the complement-involution identities and the local
Codex certificate; unknown for the target numerical bound
`m_max(beta)<=12`.

Cycle 79 does **not** prove:

```text
m_max(beta) <= 12
```

and it does **not** produce a `13`-fold packet in `P_0`. The worker again had
only read access and returned no executed output files.

## Banked Lemma

### L-CYCLE79-COMPLEMENT-INVOLUTION

Let the admissible 8-subsets of `Z/16Z` be

```text
E_1={0,1,2,3,5,11,12,13}
E_2={0,1,2,3,4,8,9,14}
E_3={0,1,2,4,5,7,11,14}.
```

The family `B_{i,a}=a+E_i` is closed under complement with involution

```text
tau(1,a) = (2,a+6)
tau(2,a) = (1,a+10)
tau(3,a) = (3,a+8)
```

modulo `16`.

For every slot `t`, the Cycle 68 slot values satisfy

```text
u_t(i,a) u_t(tau(i,a)) = 3^(-2t) (beta^32 - 9^t).
```

Therefore the seven-slot product map satisfies

```text
Phi(tau(T)) = K / Phi(T),
K = prod_{t=1}^7 3^(-2t)(beta^32 - 9^t).
```

The involution preserves the constrained shell `P_0` because complement sends
each slot color `c` to `8-c`, and `7*8-4 == 4 mod 16`.

Thus the multiplicity function is symmetric:

```text
m(v) = m(K/v).
```

If `v^2=K`, then the corresponding fiber is self-paired by `tau`; in
particular self-paired fibers have even size.

## Route Cut

The coherent common-ratio formulation by itself is equivalent to the fiber
count: every product fiber automatically supplies a coherent ratio set. It is
a useful language, but it does not independently bound `m_max`.

The new real structure from Cycle 79 is the tau-symmetry. It may cut a census
or feed an additive-energy argument, but it does not yet imply the desired
constant `12`.

## Local Follow-Up

Codex added and ran:

```text
experimental/scripts/cycle79_involution_verifier.py
experimental/notes/m1/cycle79_involution_certificate.json
```

The certificate decision is:

```text
CYCLE79_INVOLUTION_OK
```

It verifies:

```text
48 complement checks;
all seven per-slot product pairing constants;
35 deterministic random P_0 samples satisfying Phi(T)Phi(tau(T))=K.
```

An attempted pure-Python all-triples product-injectivity follow-up was
interrupted as too slow for a heartbeat turn and is not banked.

## Remaining Wall

The next exact finite wall is:

```text
V-CYCLE80-MINDIST-OR-SYMMETRIC-ENERGY
L-CYCLE79-MINDIST-EXACT
W-CYCLE79-SYMMETRIC-ENERGY-BOUND
```

Acceptable next progress:

1. Run an optimized theorem-grade three-slot product-collision scan and decide
   whether the product-fiber minimum distance is exactly `3` or at least `4`.
2. If a three-slot collision exists, extract the explicit minimal coherent
   ratio packet and test whether it extends toward a `13`-fold fiber.
3. If no three-slot collision exists, bank the stronger distance lower bound
   and use it in the tau-symmetric energy bound.
4. Prove a tau-symmetric additive-energy bound strong enough to imply
   `m_max(beta)<=12`, or show an explicit obstruction.

## What To Do Next

Stage Cycle 80 against the exact minimum-distance / symmetric-energy target.
This is narrower than another broad census plan and directly exploits the
only new structure banked by Cycle 79.
