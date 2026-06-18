# Cycle 36 A2_B Uniform S4 Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance; the
mathematical content below is source-audited conservatively from that recovery
and prior committed companion files.

Source artifacts:

- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RAW.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RUN_RESULT.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Branch: off `R0`, source-valid separated quadratic denominator, with
  `c_b != 0`, `kappa != 0`, and the Cycle 28/29 top-symbol nonvanishing
  hypotheses in force.

This is only a residue-line / bad-slope incidence calculation in one local
branch. It is not a corrected-reserve theorem, MCA claim, list-decoding claim,
CA claim, line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Explicit Family Candidate

Cycle 36 gives a useful source-valid growing-prime denominator family:

```text
nr = -1
p = 3 mod 4
alpha^2 = -1
B = F_p
F = F_{p^2}=B(alpha)
E = X^2 + alpha X + 1
b = [Bnum]_E = X
D = F_p
```

Source-valid checks:

- For `a in F_p`, `E(a)=(a^2+1)+alpha*a`. The imaginary part vanishes only
  when `a=0`, and then `E(0)=1`. Thus `E` has no root on `D=F_p`.
- `E-E^tau=2 alpha X`; a common root would force `X=0`, but `E(0)=1`, so
  `E` and `E^tau` are separated in odd characteristic.
- `c=alpha` is not in `B`, so the `c_b != 0` branch is active.

The remaining free-data hypotheses, including `kappa != 0`, are finite
nonvanishing conditions on the chosen integer lifts for the local `u` and
top-coefficient data. This reduces the infinite-family construction problem
to a fixed finite-data choice plus a finite set of excluded primes.

This is banked as a source-valid family candidate, not as a counterpacket.

## Banked Reduction To A Finite S4 Certificate

Cycle 36's useful reduction is:

```text
If one fixed good-prime specialization of the explicit family certifies the
right geometric quartic monodromy data, then good-reduction monotonicity can
promote the relevant nonsquare/discriminant and irreducibility conditions to
all but finitely many primes in the same p = 3 mod 4 family.
```

The intended certificate checks a one-parameter slice
`z_1=m z_0+e` of the `A^2_B` slope surface. On that slice, build
`M(z)`, `C_0(z)`, `tau(z)=M(z)^(-1)(-C_0(z))`, and the quartic
`L_tau`. Then certify:

1. `Delta=det_B M(z)` is not identically zero and has the expected top symbol.
2. The quartic `L_tau` is geometrically irreducible/transitive over the
   function field, or equivalently a finite-place check supplies a 4-cycle
   specialization.
3. The cubic resolvent is absolutely irreducible over the function field.
4. The quartic discriminant numerator has nonconstant squarefree part, hence is
   nonsquare over the algebraic closure of the base function field.

If these hold, then the geometric monodromy is `S_4` on that slice, hence the
surface family also has geometric monodromy `S_4`.

## Correction To The Raw S4 Criterion

Do not bank the raw response's shorter statement

```text
resolvent absolutely irreducible + nonsquare discriminant ==> S_4
```

without a separate transitivity/geometric-irreducibility hypothesis for the
quartic. A quartic with a linear factor and irreducible cubic factor can have
an `S_3` subgroup action that still makes the resolvent irreducible and the
discriminant nonsquare.

The corrected criterion for future use is:

```text
quartic transitive/geometrically irreducible
+ resolvent absolutely irreducible
+ discriminant nonsquare
==> geometric monodromy S_4.
```

A finite-place certificate with factorization types `"4"` and `"13"` is a
clean way to supply the needed transitivity and nontrivial cycle data.

## Constant Field

Cycle 36 correctly notes that once `G_geom=S_4` is proven, there is no separate
constant-field obstruction:

```text
G_geom normal G_arith <= S_4 and G_geom=S_4 ==> G_arith=G_geom=S_4.
```

This cuts only the constant-field question conditional on geometric `S_4`.
It does not prove geometric `S_4`.

## Experimental Evidence Reinterpretation

Cycle 36 reinterprets the Cycle 30/32 small-prime data as compatible with a
`p^2/24` split-density heuristic rather than decisive `O(p)` collapse. This is
only `EXPERIMENTAL`: small primes near `p=24` make `p` and `p^2/24`
numerically close, so the scan does not decide the asymptotic.

The practical consequence is not a theorem; it is that finite random scanning
is lower value than a symbolic or finite-place monodromy certificate.

## Conditional Counterpacket Seed

If the corrected finite S4 certificate succeeds for the explicit family above,
then the local restricted branch would plausibly yield

```text
C2 = p^2/24 + O(p^(3/2)) = Theta(q_line)
```

for almost all primes `p = 3 mod 4`, after excluding the singular determinant
curve and bad reductions.

This remains conditional. Do not bank a `COUNTERPACKET`.

Missing pieces:

- a fixed source-valid choice of the remaining free data with `kappa != 0`;
- a reproducible certificate for a good prime and a generic slice;
- the corrected transitivity/quartic-irreducibility check;
- a good-reduction statement with excluded primes recorded;
- a Chebotarev/Lang-Weil estimate with complexity controlled for this
  restricted family.

## Next Exact Wall

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

For the explicit family `E=X^2+alpha X+1`, `b=X`, `nr=-1`, and a fixed choice
of the remaining integer data with `kappa != 0`, produce a reproducible
single-prime certificate at one good prime `p0 = 3 mod 4`:

1. build `M(z)`, `C_0(z)`, `tau(z)`, `L_tau`, discriminant numerator, and
   cubic resolvent on a generic line `z_1=m z_0+e`;
2. certify the expected determinant/top-symbol and source-validity gates;
3. certify quartic transitivity/geometric irreducibility, ideally by a
   4-cycle finite-place specialization;
4. certify resolvent absolute irreducibility and discriminant nonsquareness;
5. record a machine-checkable certificate and all excluded hypotheses.

Success would make the uniform restricted counterpacket seed highly concrete.
Failure would expose the actual obstruction: forced reducibility, forced square
discriminant, hidden bad reduction, or source-validity failure.

## Rejected Overclaims

- Do not cite Cycle 36 as a proof of the Proximity Prize problem.
- Do not cite Cycle 36 as a corrected-reserve, MCA, CA, list-decoding,
  line-decoding, curve-MCA, protocol, or SNARK theorem.
- Do not cite Cycle 36 as a `COUNTERPACKET`.
- Do not merge `q_gen=p` with `q_line=p^2`.
- Do not use the visible terminal scrape as mathematics.
