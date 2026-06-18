# Cycle 37 Single-Prime S4 Certificate Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance; the
mathematical content below is source-audited conservatively from that recovery,
prior committed companion files, and one bounded local Codex execution attempt.

Source artifacts:

- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RAW.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RUN_RESULT.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`
- `local_checks/20260618_cycle37_single_prime_s4_cert_local_result.txt`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n=p`.
- Restricted regime: `t=sigma=2`, `j=n-a=r-t=4`.
- Candidate family: `p = 3 mod 4`, `alpha^2=-1`,
  `E=X^2+alpha X+1`, `b=X`.

This remains only a restricted residue-line / bad-slope incidence calculation.
It is not a corrected-reserve theorem, MCA claim, list-decoding claim, CA
claim, line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, or
Proximity Prize solution.

## Banked Hand Checks

Cycle 37 independently re-states and hand-checks the source-valid gates for
the Cycle 36 explicit family:

- For `a in F_p`, `E(a)=(a^2+1)+alpha*a`, so `E` has no root on `D=F_p`.
- `E-E^tau=2 alpha X`; a common root would force `X=0`, but `E(0)=1`.
- The branch `c notin B`, `c_b != 0` is active because `c=alpha`.
- The remaining free data can be chosen with `kappa != 0`; in the proposed
  normalization, `kappa` is the `X^0` component of `u=[W]_E`, so `u=1+X`
  gives `kappa=1`.
- With `c=alpha`, `d=1`, the Cycle 28/29 top symbol quantity is
  `Q_4=N(c_b) != 0`, so `Delta=det_B M(z)` is not identically zero.
- Therefore the Cycle 33 singular determinant curve bound remains available:
  `Delta=0` contributes at most `4p` slopes in this restricted branch.

These are `BANKABLE_LEMMA / AUDIT` confirmations of previously banked gates.

## Checker Attempt

Cycle 37 supplied an inline pure-Python checker specification intended to scan
a line at `p0=31` for off-`Delta` factorization types `"4"` and `"13"`.
Codex extracted and ran that checker locally without installing dependencies.

Result:

```text
returncode=1
TypeError: unsupported operand type(s) for %: 'tuple' and 'int'
```

The failure occurs inside the finite-field multiplication used by the checker:
some variables intended to be `F`-elements are represented as residue pairs of
`F`-elements. Thus the checker is type-malformed as written.

This is not a mathematical disproof of the single-prime S4 route. It only means
Cycle 37 did not produce a working certificate.

## Certificate Status

Do not bank `PROOF`.

Do not bank a single-prime `S_4` certificate.

Do not bank a `COUNTERPACKET`.

The corrected certificate target remains:

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

A valid future certificate must include:

1. fixed remaining data with `kappa != 0`;
2. a correctly typed implementation of `A=F[X]/E`, the `B`-linear system
   `M(z)tau=-C_0(z)`, and `tau(z)`;
3. a good-prime line or surface scan excluding `Delta=0`;
4. quartic transitivity/geometric irreducibility, preferably a type `"4"`
   specialization;
5. a type `"13"` or equivalent 3-cycle/resolvent witness;
6. discriminant nonsquareness or an odd-cycle witness;
7. explicit source-validity and bad-place exclusions.

## Next Prompt Direction

The next run should not merely ask for the same checker again. The best next
move is a homerun-style prompt: allow the worker to either repair the checker
and complete the single-prime certificate, produce a direct obstruction, or
step back and identify a different proof/counterpacket route that could
progress the whole RS-MCA proximity problem.

## Rejected Overclaims

- Do not cite Cycle 37 as a working checker.
- Do not cite Cycle 37 as a proof of geometric `S_4`.
- Do not cite Cycle 37 as a counterpacket.
- Do not merge `q_gen=p` with `q_line=p^2`.
- Do not use the visible terminal scrape as mathematics.
