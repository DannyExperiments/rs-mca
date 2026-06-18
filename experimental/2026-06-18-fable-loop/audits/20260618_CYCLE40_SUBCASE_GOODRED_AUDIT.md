# Cycle 40 Subcase Good-Reduction Audit

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.

Harness status: clean enough `artifact_stream`. The run completed with
`OK_WITH_NONFATAL_STREAM_WARNING` caused by one malformed stream-json line, but
`response.md` was written and contains the theorem answer. There is no
terminal/ad transcript involved.

Source artifacts:

- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RESPONSE.md`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.json`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py`
- `local_checks/20260618_cycle40_subcase_goodred_checker_result.json`

## Ledger

- `q_gen = p`.
- `B = F_p`.
- `F = F_{p^2} = B(alpha)`, with `alpha^2 = -1`.
- `q_line = |F| = p^2`.
- `q_chal`: unused.
- Domain: `D = F_p`.
- Restricted regime: `t = sigma = 2`, `j = 4`.
- Candidate family: primes `p = 3 mod 4`, `E=X^2+alpha X+1`, `b=X`,
  `u=[W]_E=1+X`, and top free data
  `W_{n-1..n-4}=1, alpha, 1+alpha, 1`.

This remains a restricted residue-line / surface-monodromy branch. It is not
a corrected-reserve theorem, MCA claim, list-decoding claim, CA claim,
line-decoding claim, curve-MCA claim, protocol claim, SNARK claim, prize
solution, or `COUNTERPACKET`.

## Banked Lemma: Finite-Place Geometric S4 Criterion

Cycle 40 correctly sharpens the interpretation of the finite-place
factorization histograms.

Let `p >= 7`, `p` not dividing `24`, and let `L_tau(X)` be the degree-four
fiber polynomial along a fixed line in the tested surface. Suppose that, away
from nonsquarefree fibers, the factorization histogram over `F_p` contains
both:

```text
"4"    irreducible quartic
"13"   linear times irreducible cubic
```

Then the tested finite-place cover has:

```text
G_arith = G_geom = S_4.
```

Reason:

1. Type `"4"` gives a 4-cycle, so the arithmetic group is transitive and
   contains an odd permutation.
2. Type `"13"` gives a 3-cycle.
3. A transitive subgroup of `S_4` containing a 3-cycle and a 4-cycle is `S_4`.
4. Type `"4"` and type `"13"` have opposite permutation parity. For
   squarefree specializations this means the quartic discriminant takes both
   nonsquare and square values on the tested line. Hence the squarefree part of
   the discriminant is not constant, so the geometric group is not contained
   in `A_4`.
5. Since `G_geom` is normal in `G_arith=S_4`, the only normal subgroup not
   contained in `A_4` is `S_4` itself.

This upgrades the already-audited Cycle 38 `p=31` Subcase B certificate from
arithmetic `S_4` evidence to finite-place geometric `S_4` evidence.

## Codex Local Checker Execution

Cycle 40 supplied a parametrized pure-Python checker. Codex extracted it to

```text
local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py
```

and ran it locally. The result is saved at

```text
local_checks/20260618_cycle40_subcase_goodred_checker_result.json
```

The checker reports `all_pass=true`.

Subcase A (`p=3 mod4`, `p=2,3 mod5`, `ell=alpha`) passes at:

```text
p=7:  hist {"4":1, "13":2, "112":1}
p=23: hist {"4":3, "13":10, "112":7, "1111":1, "nonsquarefree":1}
p=43: hist {"4":10, "13":16, "22":4, "112":9, "1111":1, "nonsquarefree":2}
p=47: hist {"4":9, "13":23, "22":6, "112":3, "1111":3}
```

Subcase B (`p=3 mod4`, `p=1,4 mod5`, `ell=-2X`) passes at:

```text
p=11: hist {"4":3, "13":5, "22":1, "112":1, "nonsquarefree":1}
p=19: hist {"4":4, "13":4, "22":5, "112":3, "1111":1}
p=31: hist {"4":6, "13":11, "22":6, "112":5, "1111":1, "nonsquarefree":2}
p=59: hist {"4":17, "13":19, "22":6, "112":14, "1111":1, "nonsquarefree":1}
```

Therefore Subcase A is no longer merely a proposed scan: it has finite-place
geometric `S_4` evidence at multiple primes, including `p=7`.

## What Is Not Banked

Do not promote Cycle 40 to any global theorem. The following remain unproved:

- the characteristic-zero determinant `Delta(z_0,z_1)` for either fixed
  subcase cover;
- the numerator of `disc_X L_tau` over `Q(i)(z_0,z_1)`;
- a good-reduction prime certified from the characteristic-zero branch data;
- the tame-specialization bridge from a finite-place `S_4` certificate to the
  characteristic-zero geometric group;
- the Chebotarev/Lang-Weil density step for a growing-prime set;
- any `COUNTERPACKET`, corrected-reserve theorem, MCA/CA/list/line/curve-MCA
  claim, protocol claim, SNARK claim, or prize-level solution.

## Exact New Wall

The live wall is sharpened to:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA
```

The next theorem-sized target is to compute or certify, separately for
`ell=alpha` and `ell=-2X`, the characteristic-zero branch determinant and
quartic discriminant data needed to prove good reduction at at least one of
the finite primes already carrying geometric `S_4` evidence.

