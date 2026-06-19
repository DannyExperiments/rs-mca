# PRZ Review Index: Cycle 49-57 Experimental Loop

## Claim

This file is the compact review index for the Codex/Opus 4.8 RS-MCA loop
through Cycles 49-57. It does not claim a prize-level solve. The integration in
this repository preserves the review index, cycle audits, and the Cycle 57
prompt for the upper-side MCA route after the Cycle 45-47 lower/failure branch
work.

The original PR #95 also carried raw JSONL responses, run manifests, zips, and
duplicated handoff context. Those large provenance artifacts were intentionally
not imported into `main`; consult the PR branch if raw model provenance is
needed. The files here are the durable review layer.

The most useful review object is the route refinement:

```text
W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE
```

with residue-coordinate companions:

```text
W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT
W-MCA-CONSTANT-RATE-HIGH-J-SPLIT-LOCATOR-INCIDENCE
```

## Status

AUDIT / EXPERIMENTAL.

Use the stronger internal route labels in the audit files only as local triage labels:

```text
BANKABLE_LEMMA      locally useful lemma or exact reduction
ROUTE_CUT           proposed route or target statement cut
EXACT_NEW_WALL      narrower next obstruction identified
COUNTERPACKET       candidate or verified refutation, depending on audit
```

Map these to the repository status labels conservatively:

```text
PROVED              only for self-contained local lemmas under stated assumptions
AUDIT               most cycle evaluations
EXPERIMENTAL        prompts, raw model outputs, small checks, route boards
COUNTEREXAMPLE      only when the audit file explicitly verifies a refutation
CONDITIONAL         only when an imported theorem or assumption is stated
CONJECTURAL         proposed inverse theorems and next-wall statements
```

No main paper is edited by this branch.

## Parameters

The cycle files keep separate ledgers for:

```text
q_gen       generated field / entropy ledger
q_line      line or slope field
q_chal      verifier challenge field, when relevant
B           base or generated field
F           ambient or extension field
n           domain size
k           RS dimension
rho         k/n
delta       decoding or MCA radius
sigma,t     reserve / denominator degree
j           complement size n-k-sigma or n-k-t
```

Do not use the extension field or line field to pay a generated-field entropy bill unless a file states a transfer theorem explicitly. The audits are intentionally conservative on this point.

## Existing Paper Dependency

Primary dependency is Paper B:

```text
tex/slackMCA_v3.tex
```

The exact object under review is the corrected-reserve MCA / residue-line local-limit side, especially the all-denominator normal form and the upper-side local-limit/inverse problem. Several audits also reference the distinction between list, CA, MCA, line-decoding, and syndrome-line formulations.

## Proof Idea Or Experiment

Recommended read order:

1. `audits/20260619_CYCLE49_SYNDROME_TRANSVERSE_SECANT_AUDIT.md`
   - Recasts the MCA upper wall as a syndrome transverse-secant inverse problem.
   - Status: AUDIT / exact reduction candidate.

2. `audits/20260619_CYCLE50_REDUCED_MOVING_SCROLL_BALANCED_INDEX_AUDIT.md`
   - Tests a moving-scroll balanced-index route.
   - Status: AUDIT / route refinement.

3. `audits/20260619_CYCLE51_BALANCED_SCROLL_VALUESET_AUDIT.md`
   - Checks whether scroll value-set size can substitute for landing control.
   - Status: AUDIT / route cut/refinement.

4. `audits/20260619_CYCLE52_TOTALLY_SPLIT_DENSITY_AUDIT.md`
   - Checks totally split density heuristics and their limits.
   - Status: AUDIT.

5. `audits/20260619_CYCLE53_SLOPE_SUMMED_CHARACTER_AUDIT.md`
   - Tests a slope-summed character cancellation route.
   - Status: AUDIT / route cut.

6. `audits/20260619_CYCLE54_T2_DETERMINANTAL_QUADRIC_AUDIT.md`
   - Moves to the `t=2` determinantal quadric toy wall.
   - Status: BANKABLE_LEMMA locally, AUDIT globally.

7. `audits/20260619_CYCLE55_T2J2_CONIC_AUDIT.md`
   - Finds a corrected conic split-pair count and a plausible square-root fluctuation seed.
   - Status: AUDIT / candidate counterpacket, not promoted.

8. `audits/20260619_CYCLE56_LOCAL_DOMAIN_REGIME_AUDIT.md`
   - Cuts the Cycle 55 seed as a fixed-rate official counterpacket because `t=2,j=2` forces `rho -> 1`.
   - Status: ROUTE_CUT / BANKABLE_LEMMA locally, AUDIT globally.

9. `prompts/20260619_cycle57_t2_high_j_quadric_split_count.md`
   - Stages the constant-rate replacement prompt.
   - Status: EXPERIMENTAL / provider-blocked, not launched.

Raw `response.md`, `raw_response.jsonl`, manifests, and run results were
present on the PR branch. They are provenance, not paper-ready claims, and are
not part of this compact integration.

## Ledger Impact

Banked route impact:

- The lower/failure branch from earlier cycles remains separate from the upper/safe-side theorem. Do not read Cycle 49-57 as proving the upper theorem.
- Balanced `t=2,j=2` conic analysis is a useful local algebraic test, but it is not an official fixed-rate challenge regime.
- Constant-rate MCA remains the live upper-side obstruction.
- The cleanest next global formulation is syndrome transverse-secant inverse, not a single fixed-denominator residue cloud.

Important cuts:

- Pairwise distance or Bessel-shell reasoning alone does not control the adversarial upper maximum.
- The conic square-root fluctuation seed does not by itself refute the official fixed-rate MCA target.
- A raw balanced theorem is not automatically a full scalar MCA theorem unless the all-denominator strata are controlled.

## Constants

No final finite prize constant is claimed in these files.

Local constants and estimates are cycle-specific. In particular:

- Cycle 55 discusses an `O(sqrt(Q))` conic fluctuation in a relaxed large-domain toy regime.
- Cycle 56 cuts that toy regime for official fixed-rate use because `t=2,j=2` implies `k=n-4`.
- Cycle 57 asks for the high-`j` constant-rate replacement.

Treat all asymptotic constants in prompts as hypotheses to audit, not as accepted theorem constants.

## Reproducibility

Reproducibility material retained in `main`:

```text
experimental/notes/f1/fable-loop/PRZ_REVIEW_INDEX.md
the original prompt archive
experimental/notes/f1/fable-loop/audits/
experimental/agents-log.md
```

The pre-existing `raw/` and `local_checks/` directories contain earlier cycle
artifacts already integrated before PR #95. They should not be read as a
complete raw archive for Cycles 49-57.

For a fresh agent:

1. Read this file.
2. Read the nine Cycle 49-57 audit/prompt files listed above.
3. Check `experimental/agents-log.md` for chronological state.
4. Use the PR #95 branch raw artifacts only if audit provenance is required.
5. Continue from Cycle 57 or supersede it with a sharper prompt for
   `W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE`.
