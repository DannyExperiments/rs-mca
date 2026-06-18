# Cycle 28 Q4 Proof Audit

Status: PROOF / ROUTE_CUT / AUDIT.

Repository proof-status tag: PROVED for the restricted local theorem stated
below only. This does not prove a corrected-reserve theorem, MCA theorem,
protocol ledger statement, or the Proximity Prize.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
argument below is audited against the previously banked Cycle 16/20/25 facts.

Source artifacts:

- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RAW.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RUN_RESULT.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_CREDIT_SURFACE_RUNNER_RESULT.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2}`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, `j = n-a = r-t = 3`.
- Branch: off `R0`, `kappa = u wedge b != 0`, source-valid denominator
  `E=X^2+cX+d` separated and nonzero on `F_p`, with `c_b != 0`.

This is a residue-line / bad-slope incidence theorem in a sub-reserve toy
window only.

## Restricted Theorem

In the restricted ledger above, the determinant consistency polynomial
`Q(z_0,z_1)` from Cycle 16 is never identically zero. Therefore the realized
slope set satisfies

```text
C2 <= #{z in F : Q(z)=0} <= 4p = O(p) = O(n).
```

The distinct split-cubic line-incidence gate can only shrink this set.

## Proof Audit

Cycle 28 independently rederived the pending `q1/q2` forms from the Cycle 20
wedge definitions:

```text
q1=(B0 wedge b)/kappa,
q2=(u wedge B0)/kappa,
B0=lambda_0 b,
```

using the banked expansion identity

```text
(lambda_0 x) wedge y =
lambda_0^(0)(x wedge y) - lambda_0^(1) P_E(y,x),
```

with

```text
lambda_0^(0)=c d + d tau_1,
lambda_0^(1)=eta=(c^2-d)+c tau_1+tau_2.
```

This gives

```text
q1 = -(Q_E(b)/kappa) eta = c_b eta,
q2 = lambda_0^(0) + (P_E(u,b)/kappa) eta.
```

Writing `P=P_E(u,b)/kappa` and `w=c^2-d`,

```text
q2^2=P,
q2^1=d+P c,
q2^0=c d+P w.
```

From the Cycle 25 six-term Plucker/Laplace formula for `Q`, the degree-4 part
is `N(z)^2 Q_4`, where the terms involving `beta_3` vanish and

```text
Q_4 =
  <beta_1,beta_2><delta_3,delta_0>
+ <beta_1,beta_0><delta_2,delta_3>
- <beta_2,beta_0><delta_1,delta_3>.
```

Substitution gives the Cycle 26 displayed form

```text
Q_4 = N(c_b) *
      ( Im(c) Im(q2^0)
      + Im(conj(c) w) Im(q2^2)
      - Im(w) Im(q2^1) ).
```

The `P`-linear part cancels identically because the `P`-part of `q2` is
collinear with `eta`, the rank-one direction of `q1`. The resulting closed
form is

```text
Q_4 = N(c_b) * ( Im(d)^2 - Im(c) Im(conj(c)d) ).
```

In coordinates `c=c_0+alpha c_1`, `d=d_0+alpha d_1`,

```text
Q_4 = N(c_b) * (c_1^2 d_0 - c_0 c_1 d_1 + d_1^2).
```

If `c notin B`, then `c_1 != 0` and the unique `a* in F_p` with
`Im(E(a*))=0` is

```text
a* = -Im(d)/Im(c).
```

Then

```text
Q_4 = N(c_b) * Im(c)^2 * E(a*).
```

Thus

```text
Q_4=0
iff E has a root in F_p
iff prod_{a in F_p} E(a)=0.
```

Source-validity excludes roots on `F_p`, so `Q_4 != 0`.

If `c in B`, then

```text
Q_4 = N(c_b) * Im(d)^2.
```

Separatedness excludes `d in B` in this branch, so `Im(d) != 0` and again
`Q_4 != 0`.

Since `N(z)^2` is not the zero polynomial, `Q_4 != 0` implies `Q` is not
identically zero. Cycle 16 then gives the `4p` upper bound.

## Dependencies

- Cycle 16: restricted determinant setup and safe side
  `Q not identically zero => C2 <= 4p`.
- Cycle 20: source-checked wedge formulas for `q1`, `q2`, `lambda_0`, and
  the rank-one direction `eta`.
- Cycle 25: six-term Plucker/Laplace expansion for `Q`.
- Cycle 24: locator norm identity `N(ell)=prod_{a in F_p}E(a)` as a
  consistency cross-check; the direct root argument already proves
  source-valid nonvanishing.

## Rejected Overclaims

- Not a corrected-reserve theorem. Here `eta=sigma/n=2/n`.
- No `q_gen` / `q_line` merge.
- No `q_chal` or verifier-field statement.
- No list-decoding, CA, MCA, line-decoding, curve-MCA, protocol, SNARK, or
  Proximity Prize consequence.
- No converse `Q(z)=0 => realized slope` is used.
- No finite experiment is used as proof.

## Route Cut

Do not keep searching for source-valid `Theta(q_line)` counterpackets in the
restricted `t=2,j=3`, off-`R0`, `c_b != 0`, source-valid separated branch.
The `Q==0` branch is empty because `Q_4 != 0`.

## Next Exact Wall

`W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL`.

The next target is to extract the top-degree coefficient of the slope
consistency determinant for `t=2`, `j=4` and decide whether it is a nonzero
`B`-scalar times a power of the same locator norm

```text
prod_{a in F_p}E(a).
```

If this persists, it suggests a route to the whole `t=2` family in the same
toy window. If it fails source-validly, the failure is the next possible
sub-reserve counterpacket seed.
