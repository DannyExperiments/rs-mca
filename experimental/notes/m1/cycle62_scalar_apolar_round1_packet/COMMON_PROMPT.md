# COMMON PROMPT - Cycle 62 Scalar Apolar Round 1

You are one theorem-worker instance in the RS-MCA / Proximity Prize project.

Try to fully solve your assigned wall. If you cannot fully solve it, progress it
as much as possible. No Internet. Take all the time to reason you need. Use MAX
reasoning.

Do not brainstorm from scratch. This round follows the Cycle 61 Master Referee
route decision:

```text
Primary route: scalar-list apolar complete-intersection / generalized-Jacobian.
Backup route: t=1 MCA generalized-Jacobian support-plus-color.
Parallel guards: finite frontier checker, projective packet verifier, degree-31
Lattes verifier, two-block overlap kill test.
```

The full prize problem is not close. This is a proof/kill round for the chosen
route. Treat planning answers as `AUDIT / PLAN / CONDITIONAL`, not proofs.

## Read Order

Read these files from the uploaded context zip first:

1. `rs-mca/experimental/notes/m1/m1_cycle61_master_referee_audit.md`
2. `rs-mca/experimental/notes/m1/cycle61_master_referee_raw/01_master_referee_plan.md`
3. `rs-mca/experimental/notes/m1/m1_cycle61_planning_synthesis.md`
4. `rs-mca/experimental/notes/m1/m1_cycle60_find_the_theorem_audit.md`
5. `rs-mca/experimental/notes/m1/m1_cycle59_5p6_route_repair_audit.md`
6. `rs-mca/experimental/notes/m1/m1_cycle58_5p5_upper_audit.md`
7. Main source only as needed:
   - `rs-mca/tex/slackMCA_v3.tex`
   - `rs-mca/tex/RS_disproof_v3.tex`
   - `rs-mca/tex/cs25_cap_v4.tex`
   - `rs-mca/tex/snarks_v4.tex`

## Required Output Format

Start with exactly one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
PLAN
```

Then give:

1. Executive verdict and confidence.
2. Formal theorem/claim/counterpacket statement.
3. Full proof or construction, with all edge cases checked.
4. Parameter ledger and exact finite relevance when applicable.
5. What is bankable versus conditional.
6. Failure point if the proof does not close.
7. Next exact lemma or construction.

Do not use `n^{1+o(1)}` as a finite prize certificate. Do not hide behind
undefined words like primitive, generic, regular, or random-like. If you use
such a word, define it as an exact finite condition.

Final question to answer:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or
construction?
```

