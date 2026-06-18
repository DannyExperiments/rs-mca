# Cycle 35 A2_B Geometric S4 Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance; the
mathematical content below is audited conservatively from that recovery and
the prior committed companion files.

Source artifacts:

- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RAW.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RUN_RESULT.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Branch: off `R0`, source-valid separated quadratic `E=X^2+cX+d`
  nonzero on `F_p`, with `c_b != 0`, `kappa != 0`, and the Cycle 28/29
  top-symbol nonvanishing hypotheses in force.

This is only a residue-line / bad-slope incidence calculation. It is not a
corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Finite-Place Certificate

Cycle 35 banks a finite-place monodromy certificate:

```text
L-T2J4-A2B-GEOM-CERT.
For a fixed source-valid restricted t=2,j=4 A^2_B instance, suppose the
off-Delta squarefree specializations of L_tau over F_p contain factorization
types "4" and "13". Then G_arith = S_4. If an even type "1111", "13", or
"22" occurs at an F_p-place, then the constant field is exactly F_p, hence
G_geom=G_arith. In particular, types "4" and "13" together already give
G_geom=G_arith=S_4, because "13" is even.
```

Proof skeleton:

1. At an unramified `F_p`-point, the squarefree factorization pattern of the
   specialized quartic gives the cycle type of an arithmetic Frobenius element
   by the usual Dedekind specialization argument.
2. A factorization type `"4"` gives a 4-cycle; a type `"13"` gives a 3-cycle.
   No proper transitive subgroup of `S_4` contains both a 4-cycle and a
   3-cycle. Therefore the arithmetic monodromy group is `S_4`.
3. The constant-field quotient `G_arith/G_geom` is cyclic. For
   `G_arith=S_4`, the only nontrivial cyclic quotient is the sign quotient
   `S_4/A_4`.
4. A degree-one Frobenius in a nontrivial sign quotient would have to lie in
   the odd coset. Thus observing an even degree-one Frobenius type
   (`"1111"`, `"13"`, or `"22"`) cuts the constant-field obstruction.
5. Therefore the tested instance has `G_geom=G_arith=S_4`.

This is a per-instance certificate. It is not a uniform-in-`p` theorem.

## Experimental Application To Cycle 32 Data

Cycle 32's recorded finite data includes, for example,

```text
p=29 seed=0 solved=808 singular=33
hist={'1111': 33, '112': 193, '13': 259, '22': 101, '4': 197,
      'nonsquarefree': 25}
```

The types `"4"` and `"13"` both occur off the determinant curve, and `"13"`
and `"1111"` are even. Under the scanner's source-validity and off-Delta
assumptions, Cycle 35's finite-place certificate reads this as
`G_geom=G_arith=S_4` for that tested instance.

This upgrades the interpretation of the recorded finite histogram, but only as
`EXPERIMENTAL / AUDIT` evidence unless the checker output and source-valid
instance are independently verified. It still does not give an infinite
family.

## Route Cut

Cycle 35 cuts a narrow version of the constant-field-obstruction route:

```text
ROUTE_CUT: in any tested source-valid instance where the squarefree
off-Delta factorization types include "4" and "13", the constant-field
obstruction is absent and the monodromy is S_4.
```

This is not a global route cut for all possible instances or all primes.

## Counterpacket Status

Do not bank a full `COUNTERPACKET`.

Cycle 35's recovered answer calls the result a conditional counterpacket seed:
if one can produce a source-valid growing-prime family satisfying the finite
certificate uniformly, then the restricted `t=2,j=4` branch would have
positive split-slope density, heuristically `1/24`, hence
`Theta(q_line)=Theta(p^2)` bad slopes in that local branch.

That would be a serious sub-reserve counterpacket seed, but it is not yet
source-valid as an infinite family.

Missing pieces:

- an explicit source-valid family for infinitely many primes;
- a uniform proof that the family has `G_geom=G_arith=S_4`;
- a uniform Chebotarev/Lang-Weil estimate with controlled complexity;
- verification that all hypotheses feeding Cycle 29/30/33/34 remain valid in
  the family.

## Next Exact Wall

```text
W-F1-AA-RES-T2J4-A2B-UNIFORM-S4
```

Upgrade the finite-place certificate to a uniform source-valid family:

1. Choose or construct explicit source-valid parameters
   `(E, b, W_{n-1},...,W_{n-4})` for infinitely many primes.
2. Prove that the resulting quartic family over `\bar B(z_0,z_1)` has
   geometric monodromy `S_4`, for example by a one-line slice whose cubic
   resolvent is irreducible and whose discriminant numerator is nonsquare.
3. Prove arithmetic/geometric equality, i.e. no constant-field obstruction.
4. Conclude a genuine growing-prime `Theta(q_line)` restricted counterpacket
   seed, or find the precise obstruction.

## Rejected Overclaims

- Do not cite Cycle 35 as a proof of a full Proximity Prize disproof.
- Do not cite Cycle 35 as a corrected-reserve, MCA, CA, list-decoding,
  line-decoding, curve-MCA, protocol, or SNARK theorem.
- Do not cite Cycle 35 as a uniform `Theta(q_line)` counterpacket yet.
- Do not merge `q_gen=p` and `q_line=p^2`.
- Do not treat the malformed visible-terminal checker text as code; use the
  recovered structured answer only as provenance and audit the checker before
  running or banking it.
