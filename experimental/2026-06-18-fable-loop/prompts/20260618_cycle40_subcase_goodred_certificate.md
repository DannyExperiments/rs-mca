# Cycle 40 Prompt: Subcase Good-Reduction S4 Certificate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are continuing the RS-MCA / Proximity Prize Fable loop as a skeptical
mathematical co-director. Work only from mounted repository/context files. Do
not use web access. Keep these ledgers separate:

- `q_gen`
- `q_line`
- `q_chal`
- `B`
- `F`

Do not promote any statement to corrected-reserve, MCA, CA, list-decoding,
line-decoding, curve-MCA, protocol, SNARK, prize, or `COUNTERPACKET` status
unless the exact source hypotheses are proved.

## Current Target

Attack exactly:

```text
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE
```

Cycle 39 banked a restricted `PROOF`-level locator-collapse lemma for the
explicit `t=2,j=4` family:

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
ell = [X^p-X]_E
```

The lemma:

```text
Subcase A: (-5/p)=+1, equivalently p=2,3 mod 5, ell=alpha.
Subcase B: (-5/p)=-1, equivalently p=1,4 mod 5, ell=-2X.
```

Cycle 38's `p=31` finite-place `S_4` certificate is only Subcase B. It does
not certify Subcase A, and it does not by itself prove good reduction.

## Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RESPONSE.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify_result.json`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`
- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `ROUTE_BOARD_CURRENT.md`

Use `.tex` files only if you need exact source definitions or hypotheses.

## Required Output

Choose the strongest route you can justify. Acceptable outcomes:

1. **PROOF / BANKABLE_LEMMA:** a subcase-separated symbolic/good-reduction
   certificate proving the needed geometric/arithmetic `S_4` behavior for the
   explicit family on a growing-prime set.
2. **BANKABLE_LEMMA / EXPERIMENTAL / AUDIT:** a reproducible finite-place
   certificate for Subcase A, preferably at `p=7`, `23`, `43`, or `47`, plus
   the existing Subcase B `p=31` certificate alignment.
3. **EXACT_NEW_WALL:** a sharper obstruction below subcase good reduction,
   with the next exact lemma stated.
4. **ROUTE_CUT:** a proof that one subcase is reducible, trapped in `A_4`, has
   a constant-field obstruction, or otherwise cannot yield the restricted
   local seed.

If you can write deliverables, write only under `output_files/`.

Preferred deliverables:

- `output_files/cycle40_subcase_goodred_result.md`
- `output_files/cycle40_subcase_goodred_checker.py`
- `output_files/cycle40_subcase_certificate.json`
- `output_files/cycle40_next_prompt.md`

If you cannot execute code inside the harness, still write the checker/spec
and state exactly what remains unrun. Codex can execute a self-contained
Python checker afterward if needed.

Use these labels literally:

- `PROOF`
- `COUNTERPACKET`
- `BANKABLE_LEMMA`
- `ROUTE_CUT`
- `EXACT_NEW_WALL`
- `AUDIT`
- `EXPERIMENTAL`

End by answering:

Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
