# Cycle 31 T2J4 Split-Quadric Collapse Audit

Status: EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL. No clean `response.md`
was produced. The visible terminal scrape is not used as mathematics. The
readable Claude structured JSONL recovery is preserved as provenance and the
content below is audited conservatively.

Source artifacts:

- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RAW.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RUN_RESULT.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle31_t2_j4_scaling_spotcheck_certificate.md`

## Claim

Cycle 31 argues that the `t=2,j=4` split-quadric wall should be attacked by
quartic monodromy rather than by a hidden rational-root collapse. Its proposed
next invariant is:

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```

More precisely, compute the discriminant and cubic resolvent of the quartic

```text
L_{tau(z)} = X^4 - tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z)
```

where `tau(z)=M(z)^(-1)(-C_0(z))` is the Cycle 29/30 rational preimage.
Certify the geometric monodromy group, ideally `S_4`; then use the correct
function-field Chebotarev/Weil statement to decide whether completely split
fibers occur with positive density.

## Parameters

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2}`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`, so `n = p`.
- Restricted regime: `t = sigma = 2`, `j = n-a = r-t = 4`.
- Branch: off `R0`, `kappa != 0`, source-valid separated quadratic
  `E=X^2+cX+d` nonzero on `F_p`, with `c_b != 0` when using that branch.

This is a residue-line / bad-slope incidence calculation only. It is not a
list-decoding, CA, MCA, line-decoding, curve-MCA, `q_gen`, protocol, or SNARK
claim.

## Audit Judgment

Do not bank Cycle 31's strongest route cut.

It claims the hidden `O(p)` collapse "does not exist" and that the finite scan
already refutes `O(p)` in favor of `Theta(q_line)` with density approaching
`1/24`. That is not proved. The existing and new spot-check data are too small
and too sparse to distinguish `C2 = O(p)` with a growing constant from
`C2 ~ c p^2`, and no discriminant/resolvent/monodromy certificate was
computed.

What is bankable is narrower:

1. Cycle 31 correctly identifies the next algebraic invariant to audit:
   quartic monodromy of the family `L_{tau(z)}`.
2. The prior phrasing "finite scan leans O(p)" should be softened. The scan
   does not prove an `O(p)` trend; positive-density behavior remains plausible.
3. A future `Theta(q_line)` counterpacket requires an explicit source-valid
   monodromy or equivalent splitting-density certificate, not a dimension
   heuristic.

## Local Follow-Up

Codex ran one bounded local spot-check by importing the Cycle 30 scanner and
extending it to `p=31` and one `p=37` seed before stopping it for time.

```text
p=31 seed=1000 C2=27 C2/p=0.871 C2/p^2=0.0281 p^2/24=40.04
p=31 seed=1001 C2=29 C2/p=0.935 C2/p^2=0.0302 p^2/24=40.04
summary p=31 trials=2 avg=28.00 avg/p=0.903 avg/p^2=0.0291
p=37 seed=1000 C2=39 C2/p=1.054 C2/p^2=0.0285 p^2/24=57.04
```

This evidence is EXPERIMENTAL only. It does not validate Cycle 31's
`1/24` density claim. It does, however, justify keeping the positive-density
counterpacket route alive and asking for an exact monodromy audit.

## Rejected Overclaims

- Not a proof that the hidden `O(p)` collapse is impossible.
- Not a banked `Theta(q_line)` counterpacket.
- Not a proof that the geometric monodromy is `S_4`.
- Not a proof of a Chebotarev density constant.
- Not a proof that the base-field splitting condition for
  `z in F_{p^2}` is identical to the naive `B(z)` or `F(z)` function-field
  model.
- No corrected-reserve theorem, MCA bound, list-decoding, CA, line-decoding,
  curve-MCA, protocol, SNARK, or prize consequence.

## Next Wall

```text
W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4
```

Compute or source-audit:

1. `disc_X L_{tau(z)}` as a rational function in the two `B`-coordinates of
   `z in F_{p^2}`.
2. The quartic resolvent cubic or another exact transitive-subgroup invariant.
3. The correct base-field formulation: whether the family should be viewed
   over `B(z_0,z_1)`, over `F(z)`, or as a two-dimensional `B`-parameter
   family with an `F_p`-splitting condition.
4. A theorem or certificate deciding `O(p)` collapse versus positive-density
   `Theta(q_line)` realized slopes.

