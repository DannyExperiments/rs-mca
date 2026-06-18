# Cycle 38 Prompt: Homerun Full-Solve Or Big-Leap Attempt

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

## Why This Is A Homerun Prompt

The current narrow line is:

```text
W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT
```

Cycle 36 produced an explicit source-valid family candidate:

```text
p = 3 mod 4
B=F_p
F=F_{p^2}=B(alpha)
alpha^2=-1
E=X^2+alpha X+1
b=X
q_gen=p
q_line=p^2
```

Cycle 37 hand-checked the source-valid gates, but its inline checker did not
run when Codex executed it locally. It failed with a type mismatch between
`F`-elements and residue-pairs. Therefore no single-prime `S_4` certificate
has been banked.

Instead of another incremental audit, take a big swing:

1. Try to fully solve or disprove the relevant RS-MCA proximity route.
2. If that is too large, produce the strongest source-valid local theorem,
   counterpacket seed, route cut, or exact new wall you can.
3. If the Cycle 36/37 `t=2,j=4` route is repairable, repair it and push it as
   far as possible.
4. If the route is a dead end, identify the exact obstruction and pivot to the
   next most promising attack.

## Context To Read First

Read these files before answering:

- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`
- `current_loop_20260618/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_local_result.txt`
- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `ROUTE_BOARD_CURRENT.md`

Use `.tex` files only if you need to check an exact source definition or
hypothesis.

## Suggested Big-Leap Angles

You may choose the best angle, but be explicit about which one you choose:

1. **Proof construction:** prove a local `O(p)` bound or a uniform `S_4`
   positive-density seed source-validly.
2. **Counterpacket construction:** produce a restricted local
   `Theta(q_line)` seed with exact hypotheses, without upgrading to MCA or
   protocol status.
3. **Checker repair:** repair the Cycle 37 type system and produce a
   certifiable finite-place result or a precise reason the implementation
   cannot decide the wall.
4. **Obstruction reduction:** find a hidden algebraic identity forcing
   reducibility, square discriminant, nontransitivity, or source-validity
   failure.
5. **Global route audit:** step back from `t=2,j=4` and identify the highest
   leverage route to the actual proximity problem across F1/L1/M1/L2/L3/X1,
   with one exact next lemma.

## Output Rules

If you can write deliverables, write only under `output_files/`.

Preferred deliverables:

- `output_files/cycle38_homerun_result.md`
- `output_files/cycle38_checker.py` if you repair or replace a checker
- `output_files/cycle38_certificate.json` if you obtain a finite certificate
- `output_files/cycle38_next_prompt.md` if the result is an exact new wall

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
