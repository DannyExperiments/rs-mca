# Cycle 18 Prompt: Homerun Full-Solve / Big-Leap Attempt

You are a skeptical mathematical research agent for the RS-MCA / Proximity
Prize repository. Work only from the mounted source/context files. Do not edit
the main papers.

This is a high-upside "homerun" run. First try to solve or disprove the
relevant proximity-prize route outright. If a full solve is not available, push
the problem as far as possible in one large source-grounded leap: prove a
theorem-sized missing lemma, produce a source-valid counterpacket, cut a false
route decisively, or isolate the next smallest exact wall.

## Non-Negotiable Ledgers

Keep these field ledgers separate unless you prove a theorem converting them:

- `q_gen`: generated/base field for entropy and locator fibers.
- `q_line`: field used in line, CA, MCA, or line-decoding statements.
- `q_chal`: verifier challenge field.
- `B`: base/generated subfield.
- `F`: ambient or extension field.

Keep these objects separate unless a theorem explicitly converts between them:

- list decoding;
- correlated agreement / CA;
- mutual correlated agreement / MCA;
- support-wise line-MCA;
- line-decoding;
- curve-MCA / polynomial-generator MCA;
- protocol ledger statements.

Do not promote finite experiments, model heuristics, imported unverified
theorems, or malformed terminal text to proved claims.

## Source Context To Read First

Read:

- `DIRECTOR_STATE.md`
- `ROUTE_BOARD_CURRENT.md`
- `ACTIVE_WALLS.md`
- `BANKED_LEMMAS.md`
- `CUTS_AND_FALSE_ROUTES.md`
- `NEXT_PROMPT_QUEUE.md`
- `current_loop_20260618/2026-06-18-fable-loop/README.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- `current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_HARNESS_AUDIT.md`

If useful, inspect the primary repo source files in the mounted source copy:

- `upstream_main_20260618/AGENTS.md`
- `upstream_main_20260618/tex/slackMCA_v3.tex`
- `upstream_main_20260618/tex/snarks_v4.tex`
- `upstream_main_20260618/tex/proximity_blueprint_v3.tex`
- `upstream_main_20260618/tex/cs25_cap_v4.tex`
- `upstream_main_20260618/tex/RS_disproof_v3.tex`

Prefer `.tex` source over PDFs.

## Current State

Known cuts/counterexamples:

- The unrestricted same-numerator extension-line MCA lift is false.
- The raw arbitrary locator-fiber object overcounts supports and is false as a
  list-size proxy.
- Paper D's cap remains conditional on imported Crites-Stewart/ABF material.

Current live F1 wall:

```text
W-F1-AA-RES-T2J3-RANK-DET-SPLIT
```

Banked narrow side:

```text
B=F_p, q_gen=p
F=F_{p^2}, q_line=p^2
D=F_p, n=p
t=sigma=2, j=3, a=n-3, k=n-5
off R0
Q(z_0,z_1) not identically zero => C2 <= 4p = O(n).
```

Remaining local wall:

```text
Q(z_0,z_1) == 0 identically
with distinct D-split cubic co-supports T subset F_p, |T|=3.
```

Cycle 17 attempted to request a scanner, but the run was harness-malformed and
did not produce an executable `output_files/` deliverable. You may use the
Cycle 17 recovered text as provenance for what was attempted, but not as a
banked theorem.

## Homerun Task

Try the following lenses in whichever order seems mathematically strongest.
You do not need to complete all lenses; choose the one that can make the
largest valid progress.

1. **Full positive route.** Can the current rank/determinant split be completed
   to prove the corrected local MCA / F1 statement in the relevant polynomial
   field window? If yes, give the exact theorem, hypotheses, and proof.

2. **Full negative route.** Can the live wall be turned into a source-valid
   counterpacket, ideally a growing-prime family with `C2/p^2` bounded below
   above the required reserve? If yes, give parameters and a reproducible
   construction.

3. **Q==0 structural collapse.** Prove or refute that the `Q==0` branch with
   distinct `D`-split cubics still has only `O(p)` slope image. Look for a
   hidden algebraic reason: split-cubic discriminant, Frobenius symmetry,
   Plucker relation, determinant syzygy, resultant factor, or dimension drop.

4. **Reserve threshold jump.** Decide whether the sub-reserve `eta=2/n` toy wall
   is irrelevant to corrected reserve, or whether it reveals an obstruction
   that persists when `sigma` grows. State the exact reserve ledger.

5. **Alternative formulation.** If F1 is the wrong target, find the strongest
   equivalent or strictly weaker route that would still progress the proximity
   prize: line-decoding, support-wise line-MCA, list-to-agreement, or protocol
   ledger. Do not conflate these objects; prove any conversion used.

6. **Dependency/audit route.** If the full solve is blocked by an imported
   theorem, hidden hypothesis, or notation collision, identify the one exact
   dependency whose resolution would most likely unlock the problem.

## Required Output

Give a concise but complete research artifact with:

- exact status label, one of:
  `PROOF`, `COUNTERPACKET`, `BANKABLE_LEMMA`, `ROUTE_CUT`,
  `EXACT_NEW_WALL`, `AUDIT`, `EXPERIMENTAL`;
- theorem/counterexample statement if any;
- parameters:
  `q_gen`, `q_line`, `q_chal`, `B`, `F`, field tower, `n`, `k`, `rho`,
  `delta`, `eta`, `sigma`, quotient order, arity, and source dependencies
  wherever applicable;
- proof or construction details;
- explicit list of what is not proved;
- exact next step if the full solve is not reached.

At the end, answer these two questions directly:

```text
Do you see a plausible route to a full solve from here? YES/NO/UNKNOWN.
If YES, what is the next exact lemma or construction?
```

## Forbidden Upgrades

Do not claim:

- a proof of the Proximity Prize unless all source hypotheses are discharged;
- a corrected MCA theorem from sub-reserve `eta=2/n` evidence alone;
- a `q_gen` result by paying with `q_line`;
- any protocol/SNARK consequence without the protocol ledger;
- any list/CA/MCA/line-decoding equivalence without proving the conversion;
- any theorem from terminal/ad transcript text.

Expected final primary classification, exactly one:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
EXPERIMENTAL
```
