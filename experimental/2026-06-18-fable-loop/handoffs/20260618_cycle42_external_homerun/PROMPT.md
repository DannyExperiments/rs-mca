# Cycle 42 External-Model Homerun Prompt

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are an external mathematical co-director for the RS-MCA / Proximity Prize
loop. Work only from the files in this packet. Do not use web access. Keep the
ledgers separate:

- `q_gen`
- `q_line`
- `q_chal`
- `B`
- `F`

Do not promote any statement to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, prize, or `COUNTERPACKET` status
unless the exact source hypotheses are proved.

## Current Highest-Value Target

Attack:

```text
W-F1-AA-RES-T2J4-A2B-S4-SUBCASEA-GOODRED-OBSTRUCTION
```

and, if you resolve it, continue immediately to:

```text
W-F1-AA-RES-T2J4-A2B-S4-BSIDE-GLOBAL-DENSITY
```

## Current State

We are in the restricted `t=2,j=4` branch with:

```text
p = 3 mod 4
B = F_p
F = F_{p^2} = B(alpha)
alpha^2 = -1
D = F_p
q_gen = p
q_line = p^2
E = X^2 + alpha X + 1
b = X
u = [W]_E = 1 + X
W_{n-1..n-4} = 1, alpha, 1+alpha, 1
```

Cycle 39 proved the locator collapse:

```text
Subcase A: (-5/p)=+1, equivalently p=2,3 mod 5, ell=alpha.
Subcase B: (-5/p)=-1, equivalently p=1,4 mod 5, ell=-2X.
```

Cycle 40 proved finite-place geometric `S_4` from factorization types `"4"`
and `"13"` on an off-singular tested line. Codex ran the Cycle 40 checker:

```text
Subcase A finite-place S4 passes at p=7,23,43,47.
Subcase B finite-place S4 passes at p=11,19,31,59.
```

Cycle 41 supplied a characteristic-zero good-reduction bridge and a checker,
but its checker was type-malformed as written. Codex preserved the original
failure, then made two minimal local repairs in a separate patched copy:

1. `ell=i` is represented as `(i,0)` in `K[X]/E`, not as a bare Gaussian
   scalar.
2. Flattened real/imaginary scalar equations are wrapped as Gaussian scalars
   with zero imaginary part before Gaussian determinant operations.

The patched checker then ran locally. Result:

```text
Subcase B: GOOD_REDUCTION_at_p0=true at p0=19,31,59.
Subcase A: GOOD_REDUCTION_at_p0=false at p0=7,23,43,47,67,83.
```

For all scanned A primes, `G1=true` but `G2=false` and `G3=false`, so the
failure is specifically separability/disjointness of `Delta_L` and/or `Ddisc`
on the tested line `z_1=z_0`.

## Read First

Read the packet manifest, then read these files:

```text
MANIFEST.md
ACTIVE_WALLS.md
BANKED_LEMMAS.md
CUTS_AND_FALSE_ROUTES.md
ROUTE_BOARD_CURRENT.md
audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md
audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md
audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md
audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md
audits/20260618_CYCLE41_CHAR0DELTA_GOODRED_AUDIT.md
raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RECOVERED_FINAL_ASSISTANT.md
local_checks/20260618_cycle40_subcase_goodred_checker_result.json
local_checks/20260618_cycle41_char0delta_checker_from_response.py
local_checks/20260618_cycle41_char0delta_checker_result.json
local_checks/20260618_cycle41_char0delta_checker_patched.py
local_checks/20260618_cycle41_char0delta_checker_patched_result.json
local_checks/20260618_cycle41_char0delta_goodprime_scan_result.json
tex/RS_disproof_v3.tex
tex/cs25_cap_v4.tex
tex/proximity_blueprint_v3.tex
tex/slackMCA_v3.tex
tex/snarks_v4.tex
```

Use the `.tex` files only for exact source definitions/hypotheses.

## Main Tasks

1. Independently rederive the characteristic-zero line-cover model over
   `K=Q(i)` for Subcases A and B. Do not trust the patched checker until you
   verify the algebra from the source definitions.
2. Audit the two Codex repairs to the Cycle 41 checker. Decide whether they
   are mathematically correct, insufficient, or wrong.
3. Resolve the A-side obstruction. Determine whether the A failure is:
   - a true branch-collision / non-etale obstruction for `z_1=z_0`;
   - an artifact of choosing the line `z_1=z_0`;
   - a bug in the reconstructed char-0 model/checker;
   - or a genuine route cut for Subcase A.
4. If a different line is needed for Subcase A, specify the exact line-search
   and good-reduction certificate. If possible, give a self-contained checker
   or explicit `Delta_L`, `Ddisc`, and resultant data.
5. If Subcase B's good-reduction certificate is source-valid, push it as far as
   possible: compute or specify the bad-prime set over `Z[i]` and the
   Chebotarev/Lang-Weil split-density step.
6. Try to solve the full problem from this branch. If the branch cannot solve
   the problem, state the exact next lemma/construction that would move it.

## Required Output

Use these labels literally:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `EXPERIMENTAL`

Do not summarize terminal/provenance junk as mathematics. Treat raw model
outputs as provenance and audits/checker results as the evaluated material.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```
