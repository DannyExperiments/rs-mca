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

### 2026-06-18 - Fable loop cycle 22, decoupling and nonemptiness wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle23_nonemptiness_split_count.md`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 22 banks the decoupling identity
  `Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2` on `Delta1==0`, after
  reducing `D=0` alignment to the single scalar gate `J_A=0`.
- **How it is useful:** It creates a much sharper residual wall:
  `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS`. The cleanest possible
  off-kernel seed lives on the explicit stratum `c in B`, `d notin B`, where
  alignment is impossible if the stratum is source-valid and nonempty.
- **What to do next:** Run Cycle 23 to decide nonemptiness and split-cubic
  slope count on that stratum. Do not bank a counterpacket until a growing
  `Omega(p^2)` source-valid family is supplied.

### 2026-06-18 - Fable loop cycle 23, c-in-B D-kernel emptiness

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE23_CINB_DKERNEL_EMPTINESS_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle23_cinb_dkernel_identity_check.py`,
  and `experimental/2026-06-18-fable-loop/README.md`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / AUDIT.
- **What is being added:** Cycle 23 cuts the `c in B`, `d notin B`, `D=0`,
  off-`R0` branch by the closed form
  `D=-mu^2(c^2/4-d)kappa`, after `ell=[X^p-X]_E` collapses to
  `mu*(xi+c/2)`.
- **How it is useful:** The previous nonemptiness target is no longer a
  possible counterpacket seed on `c in B`; the only surviving `D=0` branch is
  the complementary nonsplit-coefficient lane `c notin B`.
- **What to do next:** Attack `W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C`: compute
  `[X^p-X]_E` for `c notin B`, rederive `D`, and decide whether
  `D=0`, `Delta1==0`, off-`R0` gives `O(p)` slopes or a growing
  `Omega(p^2)=Omega(q_line)` seed.

### 2026-06-18 - Fable loop cycle 24, nonsplit-c D-kernel prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle24_nonsplit_c_dkernel.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT.
- **What is being added:** A no-internet homerun prompt attacks the remaining
  nonsplit-`c` branch after Cycle 23 closes the `c in B` half.
- **How it is useful:** This keeps the loop on the only remaining place where
  a `Theta(q_line)` seed could hide inside the restricted `t=2,j=3`
  `D=0` branch.
- **What to do next:** Audit the Cycle 24 answer conservatively and bank only
  source-valid proof, counterpacket, route cut, or exact new wall material.

### 2026-06-18 - Fable loop cycle 24, D-kernel norm route cut

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle24_dkernel_norm_identity_check.py`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / AUDIT.
- **What is being added:** Cycle 24 banks the factorization
  `D=N(ell)kappa`, with
  `ell=[X^p-X]_E=mu*(xi+c/2)+delta_c` and
  `N(ell)=prod_{a in F_p}E(a)`. Since source-valid denominators are nonzero
  on `D=F_p`, `N(ell)!=0`; off `R0`, `kappa!=0`; hence the source-valid
  `D=0` branch is empty in the restricted `t=2,j=3` window.
- **How it is useful:** This cuts the nonsplit-`c` wall and subsumes Cycle 23:
  the route can stop searching for `Theta(q_line)` counterpackets on `D=0`
  off `R0` and return to the determinant-split `Q==0`, `D!=0` branch.
- **What to do next:** Run Cycle 25 against
  `W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT`: decide whether the remaining
  `Q==0`, `det M!=0` source-valid distinct-split branch gives only `O(p)`
  slopes or a growing `Theta(q_line)` counterpacket.

### 2026-06-18 - Fable loop cycle 25, Q==0 detM nonzero prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle25_qzero_detm_nonzero_split.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and Packy route-board
  source files.
- **Status:** AUDIT.
- **What is being added:** A no-internet homerun prompt attacks
  `W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT`, the remaining non-`D=0`
  determinant-split branch after Cycle 24 cut source-valid `D=0` off `R0`.
- **How it is useful:** This keeps the loop on the only currently live place
  where a `Theta(q_line)` seed might still hide in the restricted `t=2,j=3`
  toy window.
- **What to do next:** Audit the Cycle 25 answer conservatively and bank only
  source-valid proof, counterpacket, route cut, bankable lemma, or exact new
  wall material.

### 2026-06-18 - Fable loop cycle 25, Q-zero rank correction

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle26_qzero_rank_consistency.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 25 banks the six-term Plucker/Laplace
  expansion for `Q(z_0,z_1)` and confirms that `det M` is a separate
  `z`-free invariant from `Q`. The audit rejects the recovered answer's
  overclaim that `Q==0` alone realizes every slope.
- **How it is useful:** The live wall is now the exact rank-stratified
  consistency problem: `Q==0` is only a necessary condition unless the three
  coefficient columns have rank `3`; rank-drop strata need augmented-rank
  minors. This avoids a false counterpacket route.
- **What to do next:** Run Cycle 26 against
  `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`: prove `O(p)`, produce a
  source-valid growing-prime counterpacket, or isolate the rank/minor
  elimination certificate.

### 2026-06-18 - Fable loop cycle 26, Q-zero rank-consistency prompt

- **Agent/model:** Codex directing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle26_qzero_rank_consistency.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and Packy route-board
  source files.
- **Status:** AUDIT.
- **What is being added:** A no-internet homerun prompt attacks the
  rank-stratified consistency wall left by Cycle 25.
- **How it is useful:** This asks the next worker to solve the corrected wall
  rather than repeat the false implication `Q==0 => all slopes`.
- **What to do next:** Audit the Cycle 26 answer conservatively and bank only
  source-valid proof, counterpacket, route cut, bankable lemma, or exact new
  wall material.

### 2026-06-18 - Fable loop cycle 26, rank dichotomy audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle27_q4_split_gate.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 26 banks the DEP/NONDEP rank dichotomy for
  the affine `tau` system. In the `c notin B`, `c_b != 0` branch, the columns
  are NONDEP; then rank-drop costs only `O(p)` slopes, so `Q` not identically
  zero gives the existing `O(p)` safe side.
- **How it is useful:** The remaining wall is no longer vague
  rank-consistency. It is the concrete `Q==0` obstruction, with a proposed
  top-degree scalar `Q_4`, plus the still-separate distinct split-cubic gate.
- **What to do next:** Run Cycle 27 against
  `W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE`: verify or refute the proposed
  `Q_4` formula, prove or refute source-valid `Q_4 != 0`, and do not promote
  affine `tau in B^3` consistency to actual line-incidence without the
  distinct split-cubic gate.

### 2026-06-18 - Fable loop cycle 27, Q4 obstruction audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE27_Q4_SPLIT_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE27_Q4_SPLIT_GATE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle28_q4_proof_audit.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / AUDIT.
- **What is being added:** Cycle 27 banks, conservatively, the candidate top
  coefficient
  `Q_4=N(c_b)*(Im(d)^2-Im(c)*Im(conj(c)d))`. Its locator identity says that
  for `c notin B`, `Q_4=0` iff `E` has an `F_p` root, i.e. iff the Cycle 24
  locator norm `prod_{a in F_p}E(a)` vanishes; source-validity excludes this.
  For `c in B`, separatedness gives `d notin B`, so `Q_4=N(c_b)*Im(d)^2`
  is also nonzero.
- **How it is useful:** This appears to cut the remaining `Q==0` branch in the
  restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3` window,
  reducing it to the Cycle 16 safe side `Q` nonzero implies `O(p)` slopes.
- **What to do next:** Run Cycle 28 against
  `W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT` to independently rederive the formula and
  decide whether this can be promoted from audit/banked lemma to a local proof.

### 2026-06-18 - Fable loop cycle 28, restricted Q4 proof audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE28_Q4_PROOF_AUDIT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle29_t2j4_locator_norm_top_symbol.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF / ROUTE_CUT / AUDIT, restricted local theorem only.
- **What is being added:** Cycle 28 confirms the `q1/q2` closed forms from the
  Cycle 20 wedge identities and verifies the Cycle 27 top coefficient
  `Q_4=N(c_b)*(Im(d)^2-Im(c)*Im(conj(c)d))`. Source-validity and separatedness
  force `Q_4!=0` in both `c notin B` and `c in B` branches.
- **How it is useful:** The source-valid `Q==0` branch is empty in the
  restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`, `t=sigma=2`, `j=3` window, so
  Cycle 16 gives `C2<=4p=O(p)`. This cuts the current sub-reserve toy branch.
- **What to do next:** Run Cycle 29 against
  `W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL`: test whether the same
  locator-norm top-symbol mechanism persists at `t=2,j=4`.

### 2026-06-18 - Fable loop cycle 29, T2J4 locator top-symbol wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle30_t2j4_split_quartic_gate.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 29 shows that the Cycle 28 determinant route
  changes meaning at `t=2,j=4`: the bad-line affine system has four parameters
  in a four-dimensional `B`-space, so `det_B M(z)` is an invertibility
  determinant rather than an incidence obstruction. Its top symbol is still
  controlled by the same source-valid locator quantity `Q_4`.
- **How it is useful:** This prevents overextending the `j=3` proof. The live
  wall is now the distinct split-quartic gate for the rational map
  `z -> tau(z)`, which could either give `O(p)` or expose a sub-reserve
  `Theta(q_line)` counterpacket seed.
- **What to do next:** Run Cycle 30 against
  `W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE`: prove an `O(p)` hit bound for the
  totally split distinct locus, produce a source-valid growing-prime
  counterpacket, or reduce the gate to a precise curve/Frobenius/norm
  condition.

### 2026-06-18 - Fable loop cycle 30, T2J4 split-quartic gate

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle31_t2j4_split_quadric_collapse.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 30 reduces the `j=4` gate to one
  source-correct `F`-quadric on elementary-symmetric 4-subset coordinates.
  Codex's finite scan through `p=29` leans toward `O(p)`-scale counts, not the
  recovered answer's naive `Theta(q_line)` heuristic.
- **How it is useful:** The live wall is now a concrete hidden-collapse
  question: prove the split locus on `Phi(e(T))=0` is only `O(p)`, or find a
  source-valid family with positive-density slopes that escapes the random
  scans.
- **What to do next:** Run Cycle 31 against
  `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE`: search for rational-root,
  discriminant, trace/norm, or Frobenius structure forcing `O(p)`, while
  keeping the counterpacket alternative open.

### 2026-06-18 - Fable loop cycle 31, T2J4 split-quadric collapse

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle31_t2_j4_scaling_spotcheck_certificate.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle32_t2j4_quartic_monodromy_s4.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 31 proposes that the `t=2,j=4` split locus is
  governed by quartic monodromy of `L_{tau(z)}` rather than by a hidden
  rational-root collapse. Codex rejects the stronger overclaim that the finite
  scans already prove positive density, but banks the discriminant/resolvent
  monodromy computation as the next exact wall.
- **How it is useful:** It redirects the live branch from qualitative scan
  interpretation to a crisp algebraic certificate:
  `W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4`.
- **What to do next:** Run Cycle 32 to compute or source-audit the quartic
  discriminant/resolvent and settle the correct base-field model for
  `z in F_{p^2}` with splitting over `B=F_p`.

### 2026-06-18 - Fable loop cycle 32, quartic monodromy base-field audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle33_a2b_monodromy_certificate.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 32 cuts the one-variable `B(z)` / `F(z)`
  framing for the `t=2,j=4` quartic family. The source-correct model is a
  two-dimensional `B`-surface `A^2_B` with coordinates `z=z_0+alpha z_1`.
  Codex also adds a local Cramer-system factorization histogram checker,
  matching direct support enumeration away from the singular determinant curve.
- **How it is useful:** The live wall is now a precise surface monodromy and
  singular-bound certificate problem:
  `W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE`.
- **What to do next:** Run Cycle 33 against
  `W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE`: prove or refute that the
  singular determinant curve contributes only `O(p)` slopes and that the
  off-curve quartic family has arithmetic/geometric monodromy with positive
  split density. Do not promote the checker output to `PROOF` or
  `COUNTERPACKET`.

### 2026-06-18 - Fable loop cycle 33, A2_B singular curve bound

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle34_a2b_dominance_resolvent.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 33 banks the restricted singular-bound
  lemma: under the Cycle 29 top-symbol nonzero hypotheses, the determinant
  locus `Delta(z_0,z_1)=0` in the `t=2,j=4` `A^2_B` model has degree at most
  four and contributes at most `4p` split slopes.
- **How it is useful:** It removes the singular determinant curve as a
  possible `Theta(q_line)=Theta(p^2)` source and isolates the real off-curve
  problem: dominance and resolvent/monodromy of `tau(z_0,z_1)`.
- **What to do next:** Run Cycle 34 against
  `W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT`: decide generic `B`-Jacobian rank
  of `z -> tau(z)` and compute or reduce the substituted quartic
  resolvent/discriminant and constant-field test. Do not promote this local
  lemma to a corrected-reserve, MCA, protocol, or prize theorem.

### 2026-06-18 - Fable loop cycle 34, A2_B dominance and resolvent reduction

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle35_a2b_geometric_s4_checker_spec.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 34 banks the restricted dominance lemma:
  on the source-valid dense open of the `t=2,j=4` `A^2_B` model, the rational
  off-curve map `z -> tau(z)=M(z)^(-1)(-C_0(z))` has generic `B`-Jacobian rank
  two and is birational onto the Cycle 30 quadric image.
- **How it is useful:** It cuts the rank-one / hidden curve-collapse route for
  `O(p)` off-curve counts. The remaining gate is geometric monodromy and
  constant-field stability, not dimension collapse.
- **What to do next:** Run Cycle 35 against
  `W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4`: prove geometric transitivity or full
  `S_4`, prove no constant-field obstruction, or produce an exact symbolic
  checker/certificate for the discriminant, resolvent, and constant-field
  tests. Do not promote this local branch to a corrected-reserve, MCA,
  protocol, or prize theorem.

### 2026-06-18 - Fable loop cycle 35, finite-place S4 certificate

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle36_a2b_uniform_s4.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL /
  AUDIT.
- **What is being added:** Cycle 35 banks a finite-place monodromy certificate:
  for a fixed source-valid restricted `t=2,j=4` instance, off-Delta squarefree
  factorization types `"4"` and `"13"` force arithmetic `S_4`; the even
  degree-one type cuts the sign constant-field obstruction, giving
  `G_geom=G_arith=S_4` for that tested instance.
- **How it is useful:** It reinterprets the Cycle 32 histograms as serious
  monodromy evidence and cuts the constant-field route for tested instances.
  It does not yet supply a uniform growing-prime counterpacket.
- **What to do next:** Run Cycle 36 against
  `W-F1-AA-RES-T2J4-A2B-UNIFORM-S4`: either construct an explicit source-valid
  infinite family with uniform geometric `S_4`, or find the exact obstruction
  that kills the counterpacket seed. Do not promote this local branch to a
  corrected-reserve, MCA, protocol, or prize theorem.

### 2026-06-18 - Fable loop cycle 36, explicit family and single-prime S4 wall

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE36_A2B_UNIFORM_S4_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle37_single_prime_s4_cert.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 36 gives an explicit source-valid
  growing-prime denominator family for primes `p = 3 mod 4`:
  `B=F_p`, `F=F_{p^2}=B(alpha)`, `alpha^2=-1`,
  `E=X^2+alpha X+1`, `b=X`. It also reduces the uniform geometric `S_4`
  route to a finite single-prime certificate, with a Codex correction that
  quartic transitivity/geometric irreducibility must be certified in addition
  to resolvent irreducibility and discriminant nonsquareness.
- **How it is useful:** This replaces the vague uniform-S4 wall with the
  concrete target `W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT`. Success would
  create a restricted local `Theta(q_line)` counterpacket seed; failure should
  identify the actual obstruction.
- **What to do next:** Run Cycle 37 to build or specify a reproducible
  single-prime checker/certificate for the explicit family, keeping
  `q_gen=p` and `q_line=p^2` separate and avoiding any MCA/protocol upgrade.

### 2026-06-18 - Fable loop cycle 37, single-prime checker attempt

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle37_single_prime_s4_cert_local_result.txt`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle38_homerun_full_solve_big_leap.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 37 hand-checks the source-validity gates for
  the Cycle 36 explicit family and proposes a pure-Python single-prime checker.
  Codex ran the checker locally and found it type-malformed as written, so no
  `S_4` certificate is banked.
- **How it is useful:** The route is now honest: source-valid gates are fine,
  but the finite certificate remains unproved and the model's checker cannot be
  trusted without repair.
- **What to do next:** Run Cycle 38 as a homerun prompt: either repair/bypass
  the checker and produce real progress, find the obstruction, or step back to
  the highest-value route toward the proximity problem.

### 2026-06-18 - Fable loop cycle 38, homerun S4 checker repair

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_RECOVERED_CLAUDE_JSONL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_TUI_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE38_HOMERUN_CREDIT_SURFACE_RUNNER_RESULT.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_result.txt`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle38_single_prime_s4_cert_patched_stderr.txt`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle39_symbolic_goodred_s4.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 38 identifies and repairs the exact type
  error in the Cycle 37 single-prime `S_4` checker. The repaired checker uses
  `W_{n-1..n-4}=1,alpha,1+alpha,1` as actual `F`-elements and runs locally at
  `p=31`, reporting `PASS_S4_finite_place=true` with `"4"` and `"13"`
  factorization witnesses.
- **How it is useful:** This converts the previous checker crash into
  reproducible finite-place monodromy evidence for the explicit restricted
  family. It still does not prove a uniform theorem or counterpacket.
- **What to do next:** Run Cycle 39 against
  `W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED`: prove symbolic/good-reduction
  `S_4` for the explicit family, find the exact obstruction, or produce a
  sharper certificate/wall. Future theorem runs should use the clean non-ad
  lane unless ad credit is explicitly requested.

### 2026-06-18 - Fable loop cycle 39, locator-collapse good-reduction split

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RESPONSE.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.jsonl`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle39_locator_collapse_verify_result.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle40_subcase_goodred_certificate.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What is being added:** Cycle 39 proves the restricted locator-collapse
  lemma for the explicit `t=2,j=4` family:
  `[X^p-X]_E=alpha` when `(-5/p)=+1`, and `[X^p-X]_E=-2X` when
  `(-5/p)=-1`. Codex adds a finite sanity checker confirming the formula on
  sample primes from both subcases.
- **How it is useful:** It removes the false impression that the quartic
  surface family varies freely with `p`; after the collapse, there are two
  fixed subcase models. The existing `p=31` S4 certificate covers only
  Subcase B.
- **What to do next:** Run Cycle 40 against
  `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE`: certify Subcase A and the
  good-reduction bridge, or cut one subcase by proving reducibility, an `A_4`
  trap, or a constant-field obstruction.

### 2026-06-18 - Fable loop cycle 40, subcase finite-place geometric S4

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE40_SUBCASE_GOODRED_RESPONSE.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.jsonl`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE40_SUBCASE_GOODRED_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle40_subcase_goodred_checker_result.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/prompts/20260618_cycle41_char0delta_goodred.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 40 upgrades the finite-place monodromy
  criterion: off-singular factorization types `"4"` and `"13"` certify
  `G_arith=G_geom=S_4` at that tested prime. Codex extracted and ran the
  supplied parametrized checker; it reports `all_pass=true`, with Subcase A
  passing at `p=7,23,43,47` and Subcase B passing at `p=11,19,31,59`.
- **How it is useful:** The Subcase A finite-place gap is no longer merely a
  proposed scan. The live obstruction has moved to characteristic-zero branch
  data and good reduction, not finite-place `S_4`.
- **What to do next:** Run Cycle 41 against
  `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA`: compute/certify the
  characteristic-zero determinant/discriminant data and a good-reduction prime
  per subcase, or identify the exact obstruction below that wall.
