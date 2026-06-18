# Cycle 41 Homerun Prompt: Characteristic-Zero Delta / Good-Reduction Bridge

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

This is a homerun/full-solve swing at the current restricted branch: either
bridge the finite-place geometric `S_4` certificates to characteristic zero
and the growing-prime route, or identify the exact obstruction that prevents
that bridge.

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
W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA
```

Cycle 39 proved the locator collapse in the explicit `t=2,j=4` family:

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

The collapse:

```text
Subcase A: (-5/p)=+1, equivalently p=2,3 mod 5, ell=alpha.
Subcase B: (-5/p)=-1, equivalently p=1,4 mod 5, ell=-2X.
```

Cycle 40 banked the finite-place geometric `S_4` criterion:

```text
factorization types "4" and "13" on an off-singular tested line
  => G_arith = G_geom = S_4 at that finite prime.
```

Codex then executed Cycle 40's checker locally. Result: `all_pass=true`.

Subcase A passes at `p=7,23,43,47`.
Subcase B passes at `p=11,19,31,59`.

This is still only finite-place evidence. The missing bridge is the
characteristic-zero branch data and good-reduction certificate.

## Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_result.json`
- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `ROUTE_BOARD_CURRENT.md`

Use `.tex` files only if you need exact source definitions or hypotheses.

## Required Output

Choose the strongest route you can justify. Acceptable outcomes:

1. **PROOF / BANKABLE_LEMMA:** a source-valid characteristic-zero
   good-reduction bridge for one or both subcases. This must state the
   characteristic-zero determinant/branch object, show a finite prime is a
   good-reduction prime, and explain how tame specialization transports
   geometric `S_4`.
2. **BANKABLE_LEMMA / EXPERIMENTAL / AUDIT:** a reproducible exact symbolic or
   finite-field elimination plan with enough detail for Codex to run locally
   and certify `Delta(z_0,z_1)`, `disc_X L_tau`, and one good prime per
   subcase.
3. **EXACT_NEW_WALL:** a sharper obstruction below `CHAR0DELTA`, naming the
   next exact algebraic object.
4. **ROUTE_CUT:** a proof that one subcase is reducible, trapped in `A_4`, has
   a constant-field obstruction, or otherwise cannot globalize.

If you can write deliverables, write only under `output_files/`.

Preferred deliverables:

- `output_files/cycle41_char0delta_result.md`
- `output_files/cycle41_char0delta_checker.py`
- `output_files/cycle41_char0delta_certificate.json`
- `output_files/cycle41_next_prompt.md`

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
