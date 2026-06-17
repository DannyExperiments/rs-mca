# Agents Log

This file is the working ledger for agent-created material in `experimental/`.
Use it to record every new note, script, scan, formalization stub, or audit before
the material is promoted into `tex/` or `scripts/`.

The log is not a proof-status authority. It is a coordination record: what was
added, why it might matter, and what a human or later agent should check next.
Keep entries concise and link to the relevant files.

## Entry Format

```markdown
### YYYY-MM-DD - Short title

- **Agent/model:** Name the agent or model, for example `GPT-5.5 Pro`,
  `Claude Fable 5`, or `Codex`.
- **Files added or changed:** List paths under `experimental/`, `tex/`,
  or `scripts/`.
- **Status:** PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT /
  COUNTEREXAMPLE.
- **What is being added:** State the claim, note, scan, script, or certificate
  in one or two sentences.
- **How it is useful:** Say which paper, theorem, problem, ledger, or toy case
  the material supports.
- **What to do next:** Give the next verification, cleanup, proof step,
  experiment, or promotion decision.
```

## Entries

### 2026-06-17 - Open PR triage integration

- **Agent/model:** Codex.
- **Files added or changed:** Integrated experimental material from PRs #1,
  #2, #3, and #46 through #66; added
  `experimental/pr-triage-2026-06-17.md`; renamed PR #55's dither scanner to
  `experimental/quotient_profile_dither.py` with matching `.md` note.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** One-by-one triage of the open PR queue and local
  integration of accepted experimental notes, scanners, certificates, and
  audit bundles.
- **How it is useful:** Preserves useful agent contributions while enforcing
  the repository rule that new material starts in `experimental/` and Papers
  A-D remain unchanged.
- **What to do next:** Run verifiers and audits on the integrated material,
  review mathematical notes before promotion, and close the original PRs as
  manually integrated once the integration commit is pushed.

### 2026-06-18 - Fable loop cycle 1, F1 arbitrary anchors

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Audit of an Opus 4.8 artifact-stream response on
  balanced arbitrary anchors in `def:residue`. The bankable part is the
  quadratic reduction from arbitrary extension anchors to a paired base
  interpolation-residue readout modulo `Ehat=lcm(E,E^tau)`.
- **How it is useful:** Narrows F1: arbitrary anchors do not introduce a new
  extension-only invariant in the quadratic case, but they enlarge the base
  object beyond the monic locator image.
- **What to do next:** Audit or prove the resulting base-field slope-image
  packing statement. Do not use the raw generalized per-fiber endpoint from the
  model answer without repair, since arbitrary low-degree anchors can create
  huge raw fibers.

### 2026-06-18 - Fable loop cycle 2 first attempt hung

- **Agent/model:** Codex supervising `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_HUNG_RUN.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle2_retry_paired_base_readout_short.md`.
- **Status:** AUDIT / HARNESS_FAILED.
- **What is being added:** The first Cycle 2 paired-base-readout audit attempt
  exceeded the normal answer window, ended with
  `CLAUDE_CAPTURE_WARNING_FATAL`, and produced no final theorem classification.
- **How it is useful:** Prevents later agents from treating the partial
  source-reading trace as mathematics and records the shortened retry prompt.
- **What to do next:** Retry the same target with the short prompt and a
  20-minute external watchdog. Bank only a clean `response.md` with an explicit
  final classification.

### 2026-06-18 - Codex local paired-base-readout audit

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_PAIRED_BASE_READOUT_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** A bounded local audit of the Cycle 1 arbitrary-anchor
  reduction. It confirms the factor-through paired base readout, isolates slope
  uniqueness for nonzero numerator residue, and records that shrinking to an
  `a`-subset preserves interpolation but not necessarily noncontainment.
- **How it is useful:** Refines the live F1 target into slope-image/bad-locus
  packing rather than raw arbitrary-anchor fiber bounds.
- **What to do next:** Compare against the Opus retry answer when available,
  then package only the agreed bankable statements for PR review.

### 2026-06-18 - Fable loop cycle 2 retry, paired base readout

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The shortened retry completed cleanly and confirmed
  the paired base interpolation-residue factorization for quadratic balanced
  arbitrary anchors, while sharpening the remaining target into slope-image /
  bad-locus packing rather than raw arbitrary-anchor fiber size.
- **How it is useful:** Refines F1: the balanced quadratic arbitrary-anchor
  issue is now a base-field packing wall `W-F1-AA`, not an extension-only
  invariant problem.
- **What to do next:** Ask the next worker to attack `W-F1-AA` directly:
  prove a slope-image packing bound, or produce a finite/source-valid
  arbitrary-anchor counterpacket after tangent/contained separation.
