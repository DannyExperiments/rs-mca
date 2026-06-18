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

### 2026-06-18 - Codex local balanced noncontainment subset lemma

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/audits/20260618_CODEX_LOCAL_NONCONTAINMENT_SUBSET_LEMMA.md`.
- **Status:** BANKABLE_LEMMA / AUDIT.
- **What is being added:** In a degree-`t` residue-line datum with nonzero
  numerator and balanced support size `a=k+t`, no degree-`<k` polynomial can
  agree with `-Bnum/E` on an `a`-subset. Thus balanced nonzero-numerator
  supports are automatically noncontained.
- **How it is useful:** Removes one suspected obstruction in `W-F1-AA`: in the
  balanced nonzero-numerator case, shrinking to an `a`-subset does not lose
  noncontainment.
- **What to do next:** Verify this lemma against the Cycle 3 Opus answer, then
  retarget `W-F1-AA` to the remaining slope-image packing problem.

### 2026-06-18 - Fable loop cycle 3, W-F1-AA noncontainment

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle3_w_f1_aa_noncontainment.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The run confirms the noncontainment subset issue is
  not the live balanced nonzero-numerator obstruction: supports of size at
  least `a=k+t` are automatically noncontained. The next wall is
  `W-F1-AA-AGR`, an agreement-rigidity/collision problem for paired readouts.
- **How it is useful:** Sharpens `W-F1-AA`: future work should control the
  high-agreement condition `nu(S)>=s_delta`, not ask whether noncontainment
  survives shrinking to an `a`-subset.
- **What to do next:** Attack `W-F1-AA-AGR`: prove a high-agreement collision
  rigidity theorem for arbitrary base anchors, or produce a finite
  high-agreement counterpacket.

### 2026-06-18 - Fable loop cycle 4, balance-notation route cut

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle4_audit_cycle3_balance_notation.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE4_BALANCE_NOTATION_AUDIT_RAW.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE4_BALANCE_NOTATION_ROUTE_CUT_AUDIT.md`.
- **Status:** ROUTE_CUT / BANKABLE_LEMMA / AUDIT.
- **What is being added:** Cycle 4 cuts Cycle 3's `W-F1-AA-AGR` as a balanced
  wall. Source notation has `a=ceil((1-delta)n)` and `sigma=a-k`, so balanced
  `t=sigma` gives `k+t=a=s_delta`; no extra high-agreement layer remains.
- **How it is useful:** Prevents a false detour. The balanced live target is
  restored to slope-image/bad-locus packing for the paired base readout, while
  retaining the noncontainment subset lemma.
- **What to do next:** Attack restored `W-F1-AA`: bound distinct slopes whose
  paired readout lands on `F*[Bnum]_E`, after tangent/zero-numerator and
  quotient-periodic contributions are separated.

### 2026-06-18 - Fable loop cycles 5-8, restored residue slope-image wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle5_restored_w_f1_aa_slope_image.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle6_w_f1_aa_res_rigidity_ads_lane.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle6b_w_f1_aa_res_rigidity_clean_retry.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle7_w_f1_aa_res_valuecount.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle8_w_f1_aa_res_twisted_readout.md`,
  matching `raw/` receipts, `audits/20260618_CYCLE5_W_F1_AA_RES_EXACT_WALL_AUDIT.md`,
  `audits/20260618_CYCLE6_W_F1_AA_RES_RIGIDITY_HARNESS_MALFORMED.md`,
  `audits/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RECOVERED_AUDIT.md`,
  `audits/20260618_CYCLE7_W_F1_AA_RES_VALUECOUNT_TWISTED_READOUT_AUDIT.md`,
  `audits/20260618_CYCLE8_W_F1_AA_RES_TWISTED_READOUT_AUDIT.md`,
  and related checks in `local_checks/`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What is being added:** These cycles refine `W-F1-AA` into the residue
  slope-image wall `W-F1-AA-RES`, discard malformed visible-terminal output as
  non-mathematical evidence, and bank only clean recovered theorem text plus
  locally checked residue/readout reductions.
- **How it is useful:** The work narrows F1 from arbitrary extension-line MCA
  to a concrete base-field residue-line packing problem while preserving the
  prompt/answer trail needed for later audit.
- **What to do next:** Continue separating tangent, zero-numerator, quotient,
  and twisted-readout components; use only clean `response.md` or recovered
  structured JSONL as mathematical input.

### 2026-06-18 - Fable loop cycles 9-10, residue count line-incidence route cut

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle9_w_f1_aa_res_residue_count.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle10_manual_residue_count_packet.md`,
  matching `raw/` receipts,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE9_W_F1_AA_RES_RESIDUE_COUNT_LINE_INCIDENCE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE10_MANUAL_RESIDUE_COUNT_ROUTE_CUT_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle9_locator_quotient_incidence_check.py`.
- **Status:** ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The naive residue-value counting route is cut as
  insufficient; the surviving target is a line-incidence formulation for the
  low-slack residue image.
- **How it is useful:** Prevents later agents from overclaiming a value-count
  proof and forces the next attack to control slope fibers geometrically.
- **What to do next:** Attack line-incidence directly in the smallest
  meaningful slack strata, with explicit `q_line`, `B`, `F`, `k`, and `t`.

### 2026-06-18 - Fable loop cycles 11-12, t=2 line-incidence scans

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle11_w_f1_aa_res_line_incidence.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle12_w_f1_aa_res_t2j3.md`,
  matching `raw/` receipts,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE11_T2_J2_LINE_INCIDENCE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE12_T2_J3_LINE_INCIDENCE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE12_ALT_LENS_BASE_COMPONENT_INTERSECTION.md`,
  and related `local_checks/20260618_cycle11_*` and `local_checks/20260618_cycle12_*` scripts.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** The `t=2` residue-line problem is split into
  low-dimensional incidence subcases; local scripts give reproducible finite
  checks while audits keep them experimental unless independently proven.
- **How it is useful:** Moves the live wall from a broad MCA lift question into
  concrete `t=2,j=2` and `t=2,j=3` incidence strata.
- **What to do next:** Prove or refute the base-component intersection bounds
  that the finite scans suggest; do not promote scan evidence to proof.

### 2026-06-18 - Fable loop cycles 13-14, base-component resonance wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle13_base_component_complete_intersection.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle14_base_component_resonance.md`,
  matching `raw/` receipts,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE13_BASE_COMPONENT_COMPLETE_INTERSECTION_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** The complete-intersection approach is refined to a
  base-component resonance obstruction: the easy transverse part can be bounded,
  but a structured resonant component remains.
- **How it is useful:** Identifies the next precise obstruction inside
  `W-F1-AA-RES-T2J3`, rather than leaving the wall as an undifferentiated
  incidence problem.
- **What to do next:** Analyze resonance by rank/determinant conditions and
  separate forced-base components from genuinely large slope fibers.

### 2026-06-18 - Fable loop cycles 15-16, rank-determinant split

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle15_surface_slope_fiber.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle16_rank_determinant_resonance.md`,
  matching `raw/` receipts,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle15_forced_ra_slope_scan.py`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 15 isolates a surface-slope fiber wall, and
  Cycle 16 banks the safe nonzero-rank-determinant side while naming the
  remaining `Q==0` split-distinct branch as the next exact wall.
- **How it is useful:** The current F1 attack is now a rank-determinant split:
  outside the resonant determinant locus the slope count is small, so progress
  depends on certifying or refuting the `Q==0` branch.
- **What to do next:** Build a reproducible scanner/certificate for the
  split-distinct `Q==0` branch and classify it as proof support,
  counterpacket, or exact wall.

### 2026-06-18 - Fable loop cycle 17, rank-det split scanner prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle17_rank_det_split_scanner.md`,
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT / EXPERIMENTAL.
- **What is being added:** A source-grounded prompt asks the next Fable run to
  produce an implementable scanner and certificate schema for the `Q==0`
  split-distinct branch of `W-F1-AA-RES-T2J3-RANK-DET-SPLIT`.
- **How it is useful:** This preserves the next attack in the repo before the
  model answer arrives, so other agents can reproduce the exact target and
  constraints.
- **What to do next:** When Cycle 17 completes, bank only clean `response.md`
  or clean structured JSONL recovery, commit any useful scanner/certificate
  under `experimental/`, and update this log again.

### 2026-06-18 - Fable loop cycle 17, malformed scanner response

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_HARNESS_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** AUDIT / HARNESS_MALFORMED_VISIBLE_TERMINAL.
- **What is being added:** Cycle 17 completed with a readable structured JSONL
  recovery but no promoted `response.md` and no written `output_files/`
  scanner. The recovered text is preserved as provenance only.
- **How it is useful:** Records the failed scanner attempt without promoting
  malformed terminal text or an unexecuted inline script to a claim.
- **What to do next:** Either build the scanner in a clean execution-capable
  lane or try a high-upside proof/counterpacket prompt against the live wall
  `W-F1-AA-RES-T2J3-RANK-DET-SPLIT`.

### 2026-06-18 - Fable loop cycle 18, homerun prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle18_homerun_full_solve_or_big_leap.md`.
- **Status:** AUDIT.
- **What is being added:** A high-upside prompt asks the worker to attempt a
  full solve/disproof first, and otherwise produce the largest source-grounded
  theorem, counterpacket, route cut, or exact new wall available.
- **How it is useful:** This deliberately rotates away from the local scanner
  lens after Cycle 17's malformed output, looking for an unexpected global
  route or sharper obstruction.
- **What to do next:** Audit the Cycle 18 answer conservatively. If it does not
  produce a major result, resume the normal targeted loop at the best refined
  wall it identifies.

### 2026-06-18 - Fable loop cycle 18, homerun monicity audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE18_HOMERUN_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 18 did not solve the prize problem, but it
  banks a restricted monicity lemma: in the `D=F_p`, `t=sigma=2`, `j=3`,
  off-`R0` window, the Cycle 14 determinant is monic quadratic in `tau_3`
  after changing to the `{[W]_E,b}` basis; hence `Delta0` is monic degree `2`
  in `tau_3` and `deg_{tau_3} Delta1<=1`.
- **How it is useful:** The live wall is sharpened from the `Q==0`
  rank-determinant split to a two-variable rational slope-image problem on
  non-coprime resonance strata:
  `W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE`.
- **What to do next:** Prove the resonance slope-map image is one-dimensional
  on every source-valid non-coprime stratum, or construct a growing-prime
  source-valid family where `C2/p^2` stays bounded below. Do not promote this
  sub-reserve toy-window result to a corrected-reserve, `q_gen`, protocol, or
  MCA/list-decoding statement.

### 2026-06-18 - Fable loop cycle 19, resonance slope-map collapse prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle19_resonance_slope_map_collapse.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT.
- **What is being added:** A narrow homerun prompt attacks the Cycle 18 wall
  `W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE`, asking for a proof of
  collapse, a growing-prime counterpacket, a route cut, or a strictly sharper
  exact wall.
- **How it is useful:** It preserves the big-leap strategy while preventing a
  broad solve-attempt from losing the banked monicity structure.
- **What to do next:** Audit the Cycle 19 answer conservatively and bank only
  clean `response.md`, clean structured JSONL recovery promoted to
  `response.md`, or explicit `output_files/` deliverables.

### 2026-06-18 - Fable loop cycle 19, malformed resonance-collapse answer

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE19_RESONANCE_COLLAPSE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE19_RESONANCE_COLLAPSE_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** AUDIT / HARNESS_MALFORMED_VISIBLE_TERMINAL.
- **What is being added:** Cycle 19 produced no clean `response.md`, but the
  recovered structured text suggests source-checkable rank-one and scalar-gate
  formulas for the `t=2,j=3` resonance problem.
- **How it is useful:** It gives the next precise audit target:
  `W-F1-AA-RES-T2J3-RANKONE-GATE-AUDIT`, without promoting malformed terminal
  capture or unverified formulas to theorem status.
- **What to do next:** Ask the next worker to prove or refute the closed forms,
  the rank-one `q1` lemma, the quadric normal form, and the gate scalar `D`.

### 2026-06-18 - Fable loop cycle 20, rank-one/gate audit prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle20_rankone_gate_audit.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT.
- **What is being added:** A narrow no-internet homerun prompt asks the worker
  to prove, refute, or sharpen the Cycle 19 rank-one/gate claims.
- **How it is useful:** This rotates from direct collapse proof to source-audit
  of the algebraic mechanism that would make collapse plausible or expose a
  counterpacket seed.
- **What to do next:** Audit the Cycle 20 answer and bank only clean theorem
  artifacts or explicit output files.

### 2026-06-18 - Fable loop cycle 20, rank-one/gate lemma

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE20_RANKONE_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** In the restricted `D=F_p`, `t=sigma=2`, `j=3`,
  off-`R0` window, Cycle 20 source-checks the closed forms for `p1,p2,q1,q2`,
  proves the rank-one leading coefficient, proves the quadric-branch normal
  form, and banks the gate identity `det M=(c_b/kappa^2)D`.
- **How it is useful:** It turns the residual collapse problem into a finer
  `B`-level descent wall on the `Delta1==0` branch rather than a generic
  slope-image question.
- **What to do next:** Prove or refute whether the base-descent equations
  `Im_alpha(p1+q2)=0` and `Im_alpha(det P)=0` force
  `dw wedge d eta == 0`.

### 2026-06-18 - Fable loop cycle 21, B-rank-one descent prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle21_b_rankone_descent.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT.
- **What is being added:** A no-internet homerun prompt attacks
  `W-F1-AA-RES-T2J3-B-RANKONE-DESCENT`, asking whether the `Delta1==0`
  descent equations force `dw wedge d eta == 0` or yield a counterpacket seed.
- **How it is useful:** This aims directly at the exact algebraic hinge left by
  Cycle 20.
- **What to do next:** Audit the Cycle 21 answer conservatively and continue
  with proof/counterpacket/source-audit lens rotation.

### 2026-06-18 - Fable loop cycle 21, D-kernel alignment wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE21_B_RANKONE_DESCENT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle22_d_kernel_alignment.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 21 banks the differential collapse gates for
  the `Delta1==0` slope branches and identifies the Cycle 20 gate `D` as the
  `2 x 2` resultant of the two gates. The recovered answer's stronger claim
  that base descent does not force collapse is not banked, because no
  elimination proof or source-valid off-kernel family was supplied.
- **How it is useful:** The live wall is sharpened to
  `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`: on `Delta1==0` and `D==0`, decide
  whether the two base-descent equations force
  `(W_{n-2}+cW_{n-1}:W_{n-1})` onto the collapse-kernel line.
- **What to do next:** Run Cycle 22 against the D-kernel alignment wall, with
  output files allowed if the worker can provide a finite checker/certificate
  rather than a hand proof.
