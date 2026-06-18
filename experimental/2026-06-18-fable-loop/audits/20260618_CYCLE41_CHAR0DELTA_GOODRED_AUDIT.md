# Cycle 41 Char0 Delta / Good-Reduction Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: source-audited `artifact_stream` recovery. The run completed
with `OK_WITH_NONFATAL_STREAM_WARNING` caused by one malformed stream-json
line. The dashboard `response.md` contains duplicated partial stream text, so
the raw `response.md` is preserved only as malformed stream provenance. The
final coherent assistant message was recovered from `raw_response.jsonl` and
is the text audited below.

Source artifacts:

- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RECOVERED_FINAL_ASSISTANT.md`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RESPONSE_STREAM_MALFORMED.md`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.json`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle41_char0delta_checker_from_response.py`
- `local_checks/20260618_cycle41_char0delta_checker_result.json`
- `local_checks/20260618_cycle41_char0delta_checker_patched.py`
- `local_checks/20260618_cycle41_char0delta_checker_patched_result.json`
- `local_checks/20260618_cycle41_char0delta_goodprime_scan_result.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`, with `alpha^2 = -1`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`.
- Restricted regime: `t = sigma = 2`, `j = 4`.
- Candidate family: primes `p = 3 mod 4`, `E=X^2+alpha X+1`, `b=X`,
  `u=[W]_E=1+X`, top data `W_{n-1..n-4}=1, alpha, 1+alpha, 1`.
- Cycle 39 subcases: `ell=alpha` when `(-5/p)=+1`; `ell=-2X` when
  `(-5/p)=-1`.

This is still a restricted local surface/line-cover branch. It is not a
corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, Proximity
Prize solution, or `COUNTERPACKET`.

## Banked Lemma: The Tame Good-Reduction Bridge

Cycle 41 correctly isolates the standard bridge:

If the fixed subcase cover over `K=Q(i)` on the tested line `L: z_1=z_0` has
good reduction at a prime `p0 >= 5`, then tame specialization identifies the
geometric monodromy group of the characteristic-zero line cover with the
geometric monodromy group of its reduction at `p0`.

The necessary good-reduction gate is explicit:

```text
G1: leading coefficients of Delta_L and Ddisc stay nonzero mod p0;
G2: Delta_L and Ddisc each remain separable mod p0;
G3: Delta_L and Ddisc remain disjoint mod p0.
```

Together with Cycle 40's finite-place `"4"` plus `"13"` geometric `S_4`
criterion, a passing `(G1,G2,G3)` check at a Cycle-40 prime proves
characteristic-zero geometric `S_4` for that fixed subcase line cover.

## Codex Local Checker Execution

The checker supplied in the recovered Cycle 41 answer is not executable as
written. It fails with:

```text
TypeError: 'Fraction' object is not subscriptable
```

Codex preserved that failure in
`local_checks/20260618_cycle41_char0delta_checker_result.json`.

Two minimal local repairs were then applied in a separate patched copy:

1. Represent `ell=i` as the residue pair `(i,0)` in `K[X]/E`; represent
   `ell=-2X` as `(0,-2)`.
2. Wrap flattened real/imaginary scalar equations as Gaussian scalars with
   zero imaginary part before feeding them into the Gaussian determinant code.

This patched checker runs locally.

Single-target patched result:

```text
Subcase A at p0=7:  GOOD_REDUCTION_at_p0=false
Subcase B at p0=31: GOOD_REDUCTION_at_p0=true
```

Good-prime scan result:

```text
Subcase A tested p0 = 7,23,43,47,67,83:
  G1=true for all, but G2=false and G3=false for all.
  No good-reduction prime found in the scanned A primes.

Subcase B tested p0 = 11,19,31,59:
  p0=11 fails G2;
  p0=19,31,59 pass G1,G2,G3.
```

Thus the patched local evidence supports characteristic-zero geometric `S_4`
for the Subcase B line cover, using `p0=19`, `31`, or `59`, subject to the
source audit of the reconstructed characteristic-zero line model.

Subcase A is now the important obstruction: it has finite-place geometric
`S_4` evidence from Cycle 40, but the Cycle 41 line-cover good-reduction gate
fails at every scanned A prime because the separability/disjointness gates
fail.

## What Is Bankable

Bank only the following:

1. The tame good-reduction bridge lemma and its `(G1,G2,G3)` gate.
2. The patched-checker execution as `EXPERIMENTAL / AUDIT` evidence.
3. The Subcase B good-reduction certificates at `p0=19,31,59`, conditional on
   the patched checker matching the source-defined characteristic-zero line
   cover.
4. The exact new A-side wall below `CHAR0DELTA`.

## What Is Not Banked

Do not promote Cycle 41 to any global theorem. The following remain unproved:

- an independently source-derived characteristic-zero `Delta_L` and `Ddisc`
  for both subcases;
- Subcase A characteristic-zero geometric `S_4`;
- a proof that the A-side failure is structural rather than a line/model
  artifact;
- a full two-dimensional surface good-reduction result;
- the finite bad-prime set over `Z[i]`;
- Chebotarev/Lang-Weil split-density with an explicit error term;
- a restricted local `Theta(q_line)` counterpacket seed;
- a `COUNTERPACKET`, corrected-reserve theorem, MCA/CA/list/line-decoding/
  curve-MCA/protocol/SNARK statement, or prize solve.

## Exact New Walls

Primary wall:

```text
W-F1-AA-RES-T2J4-A2B-S4-SUBCASEA-GOODRED-OBSTRUCTION
```

Resolve whether the A-side failure is:

1. a true structural branch-collision / non-etale obstruction for the line
   `z_1=z_0`;
2. an artifact of choosing that line rather than another finite-place
   certified line;
3. a bug in the reconstructed characteristic-zero cover/checker; or
4. evidence that Subcase A cannot globalize through this monodromy route.

Secondary wall:

```text
W-F1-AA-RES-T2J4-A2B-S4-BSIDE-GLOBAL-DENSITY
```

Assuming the Subcase B patched certificate survives source audit, compute the
explicit bad-prime set and prove the Chebotarev/Lang-Weil density step for
off-branch split slopes on the restricted B-side branch.

## Cycle 42 Recommendation

Use an external-model homerun prompt. Ask the model to fully solve if possible,
but focus it on independently rederiving the Cycle 41 characteristic-zero
line-cover model, auditing the two local repairs, and resolving the A/B
asymmetry. The best possible outcome is either:

- a source-valid repair proving good reduction for Subcase A, closing the
  two-subcase `CHAR0DELTA` wall; or
- a real `ROUTE_CUT` showing Subcase A cannot globalize through this line-cover
  route, plus a clean path to exploit the Subcase B global-density branch.
