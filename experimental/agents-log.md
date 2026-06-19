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

### 2026-06-18 - Fable loop cycle 41, characteristic-zero good-reduction bridge

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RECOVERED_FINAL_ASSISTANT.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RESPONSE_STREAM_MALFORMED.md`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.json`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.jsonl`,
  `experimental/2026-06-18-fable-loop/raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RUN_RESULT.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle41_char0delta_checker_from_response.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle41_char0delta_checker_result.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle41_char0delta_checker_patched.py`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle41_char0delta_checker_patched_result.json`,
  `experimental/2026-06-18-fable-loop/local_checks/20260618_cycle41_char0delta_goodprime_scan_result.json`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE41_CHAR0DELTA_GOODRED_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/handoffs/20260618_cycle42_external_homerun/PROMPT.md`,
  `experimental/2026-06-18-fable-loop/handoffs/20260618_cycle42_external_homerun/MANIFEST.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT.
- **What is being added:** Cycle 41 reduces the characteristic-zero
  good-reduction bridge to explicit `(G1,G2,G3)` gates for the fixed subcase
  line cover. Codex recovered the coherent final answer from JSONL because the
  dashboard `response.md` contained duplicated partial stream text. The
  original model checker fails with a type error; a minimal patched copy runs.
- **How it is useful:** The patched checker reports Subcase B good reduction
  at `p0=19,31,59`, while Subcase A fails the good-reduction gates at every
  scanned A-prime `7,23,43,47,67,83`. This makes the live wall sharper: finite
  `S_4` is not the bottleneck; the A-side branch separability/disjointness
  obstruction is.
- **What to do next:** Send the Cycle 42 external-model homerun packet. The
  next model should independently rederive the characteristic-zero model,
  audit the Codex checker repairs, decide whether the A-side failure is a real
  `ROUTE_CUT` or a line/checker artifact, and, if possible, push the B-side
  good-reduction certificate through global-density.

### 2026-06-18 - Cycle 42 external 5.5 Pro good-reduction and density audit

- **Agent/model:** Codex auditing four external 5.5 Pro answer files and their
  returned checker/certificate artifacts.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle42_external_5p5_pro/`,
  `experimental/2026-06-18-fable-loop/local_checks/cycle42_external_5p5_pro/`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT /
  EXPERIMENTAL.
- **What is being added:** Four external answers agree that Cycle 41's A-side
  failure was a false negative: the patched checker used an overstrong raw
  affine/Cramer good-reduction gate rather than the primitive/projective tame
  cover. The returned machine certificates report Subcase A good reduction at
  `p=7`, Subcase B good reduction at `p=19` or `p=31`, finite `"4"` + `"13"`
  S4 witnesses, and split-slope density
  `N_split(p)=p^2/24+O(p^(3/2))`.
- **How it is useful:** The fixed restricted `t=2,j=4` monodromy branch no
  longer looks stuck at A-side good reduction. The false route "A fails raw
  G2/G3, hence A cannot globalize" is cut. The next live wall is reserve
  scaling, not another quartic good-prime search.
- **Local execution caveat:** Codex inspected and syntax-checked the Python
  checkers, but local symbolic execution is blocked because `sympy` is absent
  from both system Python and the bundled Codex Python. No dependency was
  fetched or installed. The result is banked as an external-machine
  certificate pending local SymPy/Sage rerun or PRZ review.
- **What to do next:** Discuss before prompting again. If accepted, the next
  target is `W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT`, with aliases
  `W-F1-AA-RES-T2J4-TO-CORRECTED-RESERVE-SLOPE-PRESERVING-LIFT` and
  `W-F1-AA-RES-RESERVE-SCALED-GENERATED-FIELD-QUARTIC-CORE-LIFT`.

### 2026-06-19 - Cycle 43 reserve-lift homerun prompt launched

- **Agent/model:** Codex launched `claude-opus-4-8` with
  `fable_full_experiment` in clean non-ad `artifact_stream` mode.
- **Run directory:** `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T23-35-34-020Z-cycle43-reserve-lift-homerun-a410a6ef`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260618_cycle43_reserve_lift_homerun.md`
  and `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** active run / pending audit.
- **Target:** `W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT`.
- **Why this prompt:** Cycle 42 appears to close the fixed restricted
  `t=2,j=4` branch, so Cycle 43 asks whether that quartic-monodromy mechanism
  can be lifted to reserve scale (`t=sigma >= C n/log n`, `j=Theta(n)`) or
  whether there is a theorem-sized obstruction to scaling.
- **Lane choice:** Clean artifact stream was used instead of the VS Code ads
  lane because ad credit was not working and theorem progress is higher
  priority.

### 2026-06-19 - Cycle 43 reserve-lift homerun audit

- **Agent/model:** Codex auditing `claude-opus-4-8` Cycle 43 response.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle43_reserve_lift_homerun/`,
  `experimental/2026-06-18-fable-loop/audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT /
  EXPERIMENTAL.
- **What is being added:** Cycle 43 cuts the literal route of directly
  amplifying the fixed `t=2,j=4` quartic/S4 mechanism to reserve scale. In
  reserve scale, `j=Theta(n)` while `2t=2sigma=Theta(n/log n)`, so the square
  Cramer/quartic object disappears; along the balanced diagonal `j=2t`, totally
  split monodromy density is at most `1/j -> 0`.
- **How it is useful:** It redirects the live route to a sharper object:
  `W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`. The useful
  heuristic skeleton is
  `N_split ~ min(q_line, C(p,j)/p^{2(t-1)})`, matching the banked `j=2`,
  `j=3`, and `j=4` regimes, but reserve-scale equidistribution and slope
  anticollision remain open.
- **What to do next:** Discuss before launching Cycle 44. If continuing, attack
  subset-product/cosupport equidistribution directly, preferably first with a
  finite sweep fixing `t=2` and increasing `j` to see whether
  `|Slopes|/p^2` grows toward a positive constant or stalls.

### 2026-06-19 - Cycle 44 cosupport subset-product homerun launched

- **Agent/model:** Codex launched `claude-opus-4-8` with
  `fable_full_experiment` in clean non-ad `artifact_stream` mode.
- **Run directory:** `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle44_cosupport_subset_product_homerun.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** active run / pending audit.
- **Target:** `W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`.
- **What is being added:** A slower homerun prompt against the Cycle 43 exact
  wall, explicitly asking for a source-valid reserve lift through cosupport
  subset-product equidistribution, or the smallest exact lemma, obstruction,
  or falsifier below it.
- **How it is useful:** It points the next theorem-worker call at the actual
  reserve-scale bottleneck rather than another fixed quartic/S4 audit.
- **What to do next:** Preserve and audit only clean `response.md` and explicit
  `output_files/` deliverables. Do not bank Cycle 44 mathematics until the
  answer is classified conservatively.

### 2026-06-19 - Cycle 44 cosupport moment identity audit

- **Agent/model:** Codex auditing `claude-opus-4-8` Cycle 44 response.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle44_cosupport_subset_product_homerun/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE44_COSUPPORT_MOMENT_IDENTITY_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.
- **What is being added:** Cycle 44 banks the exact cosupport moment identity
  `rho(T)=-ell Lambda(T)^(-1)N(T)` for `rho(T)=[I_{D\T}]_E`, with both
  `N(T)` and `Lambda(T)` affine-linear in the elementary symmetric functions
  of `T`. It also banks the exact landing-count character identity with main
  term `binom(p,j)/p^(2(t-1))`.
- **How it is useful:** The reserve wall is no longer the vague
  subset-product/equidistribution object. It is sharpened to
  `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION`, especially the
  `L2` anticollision bound
  `M_2 <= #Land + (1+o(1))#Land^2/q_line`.
- **What is not banked:** No proof of cancellation, no proof of the L2
  anticollision estimate, no positive reserve-density result, no generated
  field or MCA consequence, and no final counterpacket.
- **What to do next:** Prepare a role-split external 5.5 Pro packet or next
  theorem prompt against the L2 anticollision wall: either prove the moment
  anticollision estimate or produce a source-valid growing-family falsifier
  with a high-multiplicity slope.

### 2026-06-19 - Cycle 45 external L2 anticollision packet

- **Agent/model:** Codex preparing prompts for six fresh external 5.5 Pro-style
  instances.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/handoffs/20260619_cycle45_l2_anticollision_external/`,
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`, and this log.
- **Status:** EXTERNAL_MODEL_PACKET / AUDIT.
- **Target:** `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION`.
- **What is being added:** A role-split packet with common context plus six
  roles: proof-builder, falsifier hunter, source auditor, finite checker
  designer, homerun full-solve attempt, and obstruction reducer.
- **Why:** Cycle 44 produced a precise L2 wall. Six identical homerun prompts
  would waste model diversity; the role split probes proof and failure modes
  separately while keeping the same banked identity and ledgers.

### 2026-06-19 - Cycle 45 external random-anchor L2 audit

- **Agent/model:** Codex auditing external 5.5 Pro-style Cycle 45 answers and
  local artifacts from Downloads.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle45_external_random_anchor_l2/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE45_EXTERNAL_RANDOM_ANCHOR_L2_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT /
  EXPERIMENTAL.
- **What is being added:** The external round cuts the universal fixed-anchor
  version of `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION`,
  but proves the existential random-anchor L2 reserve lift in the restricted
  additive branch `D=F_p`, `F=F_{p^2}`, `q_line=p^2`.
- **Bankable lemma:** For supports/cosupports at exchange distance `r`,
  `rank_F(w -> (R_T(w),R_T'(w))) = t + min(t,r)`. Thus random-anchor residues
  are exactly independent once the supports differ in at least `t` exchanged
  points.
- **Reserve consequence:** With `lambda=binom(p,j)/p^(2t)`, there exists a
  deterministic anchor with `M_2 <= (1+o(1))#Land^2/p^2` whenever
  `lambda -> infinity`; in the strict entropy range
  `t=(C+o(1))p/log_2 p`, `C < H_2(rho)/2`, this gives `(1-o(1))p^2` slopes
  and all `p^2` slopes for sufficiently large `p` under the stronger finite
  gap `lambda >> p^2`.
- **Audit caveats:** The result needs `b=[B_num]_E != 0`, should use a
  nondegenerate additive pairing if `E` is not squarefree, and should prefer
  an aperiodic separated denominator such as `X^t+alpha X+1` for final source
  hygiene.
- **What is not banked:** No generated-field theorem, no smooth
  multiplicative-domain theorem, no corrected-reserve sufficiency theorem, no
  protocol/SNARK statement, and no Proximity Prize solve.
- **New wall:** `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING`, i.e. a transfer or
  compression lemma that would reduce the landing codimension from
  `2(t-1)` `B`-dimensions to `t-1` and move the entropy threshold from
  `H_2(rho)/2` toward the generated-field scale `H_2(rho)`.

### 2026-06-19 - Cycle 45 deep literature audit

- **Agent/model:** Codex auditing the user-provided deep lit-AI report plus
  public/source checks.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle45_deep_lit_audit/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE45_DEEP_LIT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** AUDIT / ROUTE_CUT / EXACT_NEW_WALL.
- **Lit-audit conclusion:** No duplicate of the exact Cycle 45
  exchange-distance pair-rank theorem was identified, but there is substantial
  related prior art in proximity gaps, folded RS / multiplicity decoding,
  subspace-polynomial list decoding, and interleaved-RS rank methods.
- **Route cut:** Do not promote the restricted additive branch directly to a
  full grand MCA solve. The official challenge says "smooth evaluation
  domain"; the restricted branch uses `D=F_p subset F_{p^2}` and may not match
  the intended multiplicative/generated smooth-domain setting.
- **Correction:** The lit-AI output incorrectly drifts from the local
  `C^{equiv m}` notation to Reed-Muller/multiplicity-code language. In local
  source, `C^{equiv m}` is the `m`-interleaved Reed-Solomon code with column
  distance.
- **New walls:** `W-F1-AA-RES-SMOOTH-DOMAIN-ADMISSIBILITY`,
  `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING`, and
  `W-F1-LIST-INTERLEAVED-BRIDGE`.

### 2026-06-19 - Cycle 46 targeted wallbreaker audit

- **Agent/model:** Codex auditing six fresh external 5.5 Pro-style targeted
  wallbreaker answers. Outputs 02 and 03 are byte-identical duplicates.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle46_targeted_wallbreaker_5p5/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE46_TARGETED_WALLBREAKER_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT /
  EXACT_NEW_WALL / AUDIT.
- **What changed:** The smooth-domain wall may be much weaker than the Cycle45
  lit audit suggested. The pair-rank theorem is domain-free: for arbitrary
  `D subset F_Q`, `rank_F(R_T,R_T') = t + min(t, |T\T'|)`.
- **New scalar-MCA route:** The constant Cycle45 shell bound is not needed.
  The domain-uniform shell factor is
  `J <= exp(2 sqrt(aj/Q)) <= exp(n/sqrt(Q))`, hence subexponential for
  `Q >= n`. This should allow smooth prime-field multiplicative subgroups
  with `log q=o(n)` to reach `emca=1` throughout the strict range
  `c < H_2(rho)`.
- **Route cut:** Frobenius compression is no longer the preferred scalar-MCA
  wall unless official rules force the quadratic extension ledger or exclude
  prime-field smooth subgroups.
- **New walls:** `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT`,
  `W-F1-AA-SMOOTH-PRIME-SUBGROUP-MCA-COUNTERPACKET`,
  `W-F1-LIST-M-ANCHOR-ZERO-RESIDUE-DISTINCTNESS`, and
  `W-F1-LIST-CORRELATED-COMMON-SUPPORT-RANK-COMPRESSION`.
- **List-side caution:** The direct `m`-anchor construction gives a real
  column-distance interleaved lower bound with exponent `H_2(rho)-m c`, but it
  may be ordinary volume behavior, not a full grand list-decoding threshold.
- **What to do next:** Formalize/source-audit the domain-uniform Bessel moment
  theorem and smooth-prime-subgroup MCA counterpacket, then compare literally
  against the official grand MCA challenge wording.

### 2026-06-19 - Cycle 46 instance-3 Frobenius-compression supplement

- **Agent/model:** Codex auditing one additional attachment plus one pasted
  external 5.5 Pro-style instance-3 answer.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle46_instance3_frobenius_supplement/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE46_INSTANCE3_FROBENIUS_COMPRESSED_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT / AUDIT.
- **What changed:** Instance 3 gives a literal Frobenius-compressed additive
  construction with `E=H(X)(X-theta)` and `B_num=H`, where
  `J=lcm(E,E^(p))=H m_theta` has degree `t+1`. For `F_p`-valued anchors, all
  cosupport residues land in a `t+1` dimensional `F_p`-space `U` containing
  the slope line `F_{p^2}b`.
- **Entropy consequence:** The effective mean becomes
  `Lambda=binom(p,j)/p^(t+1)`, with shell loss `exp(O(sqrt p))`; hence the
  additive/base-field branch reaches `C < H_2(rho)` if the nonminimal
  denominator presentation is accepted.
- **Caveat:** `gcd(E,B_num)=H`, so the direction reduces to
  `-1/(X-theta)`. The local residue-datum definition does not forbid this,
  but a reviewer may classify it as a nonminimal-denominator or low-denominator
  artifact. It is not a smooth-domain or prize-level promotion by itself.
- **What to do next:** Decide whether reduced denominators are required; then
  test whether the same envelope proof works cleanly on smooth multiplicative
  subgroups/cosets `D subset F_p^*`.

### 2026-06-19 - Cycle 47 domain-uniform Bessel moment audit

- **Agent/model:** Codex auditing six fresh external 5.5 Pro-style answers
  against the repo-aware Cycle 47 Bessel packet.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle47_domain_uniform_bessel_5p5/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE47_DOMAIN_UNIFORM_BESSEL_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** PROOF_CANDIDATE / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **Consensus:** Five answers classify
  `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT` as `PROOF`; the admissibility
  auditor classifies it as algebraic `PROOF` with literal-official promotion
  conditional on matching the survey's MCA Definition 4.3 to the source
  support-wise definition.
- **Banked theorem candidate:** For any distinct-point domain `D subset F_Q`,
  the pair-rank lemma is domain-free:
  `rank_F(w -> (R_S(w),R_S'(w))) = t + min(t, |S\S'|)`. The shell factor is
  `J <= I_0(2 sqrt(aj/Q)) <= exp(2 sqrt(aj/Q))`, giving an anchor with missed
  slopes at most `QJ/lambda`, where
  `lambda=binom(n,k+t)/Q^t`.
- **Smooth-domain lower branch:** For smooth multiplicative `L subset F^*`,
  `E=X^t`, `B_num=1`, `f=w/E`, and `g=-1/E` give a source-local MCA failure
  branch. If `lambda > QJ`, every slope is bad. Asymptotically, for
  `t=(c+o(1))n/log_2 Q` and `log_2 Q=o(n)`, this reaches the strict range
  `c < H_2(rho)`.
- **Not solved:** The matching safe-side upper theorem, the exact official
  threshold, and the list-decoding grand challenge remain open. The list-side
  `m`-anchor construction gives the ordinary exponent `H_2(rho)-mc`, not the
  scalar MCA coefficient for `m>=2`.
- **New main wall:** `W-MCA-AA-RES-ENTROPY-BOUNDARY-MATCHING-UPPER`: a uniform
  high-cloud inverse theorem for balanced arbitrary-anchor residue clouds,
  after quotient-pullback, tangent/contained, and residual-list templates are
  separated.

### 2026-06-19 - Cycle 48 upper-inverse refresh audit

- **Agent/model:** Codex auditing nine upper/inverse external answers pasted
  inline or attached after the Cycle 47 lower-branch packet.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/handoffs/cycle48_upper_inverse_context_20260619.zip`,
  `experimental/2026-06-18-fable-loop/raw/cycle48_upper_inverse_5p5/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE48_UPPER_INVERSE_REFRESH_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** COUNTERPACKET / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What changed:** The Cycle 47 lower/failure branch remains banked, but the
  safe-side upper theorem was not solved. The naive wall
  `W-MCA-AA-RES-ENTROPY-BOUNDARY-MATCHING-UPPER` is too coarse.
- **Major route cut:** Literal quotient-pullback aperiodicity is insufficient.
  Quotient-component denominators with `E | m(X^M)` and fixed-defect
  quotient-anchor packets can produce large reduced balanced clouds above
  entropy, even when they are not syntactically `E_0(X^M)` and survive
  tangent, same-witness, contained, low-denominator, residual-list, and
  Frobenius/base-core tests.
- **New quotient invariant:** for each quotient scale `M`, classify
  `xi_M=[X^M]_E` by `d_M(E)=deg minpoly_F(xi_M)`. Low `d_M(E)` marks a
  quotient-component packet; `d_M(E)=1` is the punctured-fiber coequalizer
  obstruction.
- **Banked reductions:** all-`t` support-syndrome normal form; fixed tangent
  core cap `j+1`; locator-scroll `E`-resonant circuit certificate; residual
  slack injection and degree inflation; finite line-occupancy correction; and
  official-target interleaved-list projection to scalar list.
- **New main wall:** `W-MCA-SYNDROME-TRANSVERSE-SECANT-ENTROPY-INVERSE`, with
  companion walls `W-MCA-QUOTIENT-ACTION-RANK-INVERSE`,
  `W-MCA-AA-RES-LOCATOR-SCROLL-SECTION-OR-QUOTIENT`,
  `W-MCA-HIGH-DENOMINATOR-THICK-RESIDUE-COMPRESSION`, and
  `W-L1-ARBITRARY-WORD-FULL-SUPPORT-LOCAL-LIMIT-ABOVE-CORRECTED-RESERVE`.
- **Finite warning:** a correct finite safe-side statement must include
  `R_line=ceil(binomial(n,k+t)/Q^(t-1))`; a bare `n^{1+o(1)}` bound immediately
  after the entropy equality is not the prize-level finite theorem.

### 2026-06-19 - Cycle 49 syndrome transverse-secant audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle49_syndrome_transverse_secant_inverse/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE49_SYNDROME_TRANSVERSE_SECANT_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What changed:** The upper-side MCA problem is reformulated as an exact
  Hankel-pencil locator-kernel problem. For `t=r-j`, `u+zv in W_T` iff
  `(H(u)+zH(v))ell_T=0`, where `ell_T` is the monic degree-`j` complement
  locator.
- **Banked reduction:** With `K0=ker H(u) cap ker H(v)`, the moving part of
  the pencil lives in `V=F[X]_{<=j}/K0`, `dim V<=2t`. Kronecker minimal indices
  have total degree at most `t`, producing a reduced moving scroll of degree at
  most `t`.
- **Route cut:** Do not claim that removing the common core and bounding scroll
  degree gives an `O(n)` slope bound. Structured split locators can concentrate
  on quotient-aligned scrolls, matching the Cycle48 quotient-component
  obstruction.
- **New wall:** `W-MCA-REDUCED-MOVING-SCROLL-INCIDENCE`, with first subtarget
  `W-MCA-REDUCED-MOVING-SCROLL-BALANCED-INDEX`.
- **What to do next:** Ask for a proof or source-valid counterpacket for the
  balanced-minimal-index case:
  if all right minimal indices of `H(u)+zH(v)` differ by at most one, prove
  `#{z : M_z meets Proj_V(Split_L^sf)} <= R_line+(j+1)`, or exhibit the first
  genuinely aperiodic counterpacket.

### 2026-06-19 - Cycle 50 balanced-index prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle50_reduced_moving_scroll_balanced_index.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused theorem-worker prompt for
  `W-MCA-REDUCED-MOVING-SCROLL-BALANCED-INDEX`, asking for a proof or
  counterpacket to the balanced right-minimal-index reduced moving-scroll
  incidence bound.
- **How it is useful:** Keeps the next loop on the smallest genuinely
  aperiodic subwall exposed by Cycle49 rather than re-litigating the whole
  upper theorem.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  then audit conservatively before updating the route board.

### 2026-06-19 - Cycle 50 reduced moving-scroll balanced-index audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle50_reduced_moving_scroll_balanced_index/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE50_REDUCED_MOVING_SCROLL_BALANCED_INDEX_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What changed:** Cycle50 identifies the reduced moving-scroll count as a
  rank-one value-set problem. For each split locator `ell_T`, put
  `(a(T),b(T))=(H(u)ell_T,H(v)ell_T)`. A transverse locator realizes a unique
  slope iff `rank[a(T)|b(T)]<=1` and `b(T)!=0`.
- **Banked reduction:** Moving fibers are pairwise disjoint after quotienting
  `K0=ker H(u) cap ker H(v)`, and the finite random-incidence baseline is still
  `R_line=ceil(binomial(n,k+t)/Q^(t-1))`.
- **Route cuts:** Balanced right minimal indices do not remove all quotient or
  bounded-defect quotient-action packets. Also, averaged random-anchor landing
  bounds do not imply deterministic per-line upper bounds.
- **Audit correction:** Distinct slope image `Z(u,v)` and total landing count
  `R(u,v)` must be kept separate. A bound on `R(u,v)` is sufficient for MCA,
  but stronger than the actual numerator bound on `Z(u,v)`.
- **New wall:** `W-MCA-BALANCED-SCROLL-CONFIG-EQUIDISTRIBUTION`; next target:
  `W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING`.

### 2026-06-19 - Cycle 51 value-set-vs-landing prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle51_balanced_scroll_valueset_vs_landing.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-BALANCED-SCROLL-VALUESET-VS-LANDING`, forcing the next theorem worker
  to bound the distinct slope image `Z(u,v)` or produce a counterpacket with
  many distinct slopes, not merely many total landings.
- **How it is useful:** Prevents the upper-bound route from accidentally
  replacing the actual MCA numerator by a stronger but different first-moment
  landing count.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit the result before any promotion.

### 2026-06-19 - Cycle 51 balanced-scroll value-set audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle51_balanced_scroll_valueset_vs_landing/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE51_BALANCED_SCROLL_VALUESET_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **What changed:** The value-set wall is now separated from the landing-count
  wall. With `R=sum_z nu(z)`, `Z=#{z:nu(z)>=1}`, and `M2=sum_z nu(z)^2`,
  the sharp inequality is `Z>=R^2/M2`; L2 anticollision pushes the image lower
  bound upward and cannot upper-bound the safe-side MCA numerator.
- **Route cut:** Do not use Cycle44/Cycle47 L2 anticollision as the positive
  upper theorem. The upper route must either prove the stronger landing bound
  `R<=R_line+O(j)` or directly count the distinct value set.
- **New wall:** `W-MCA-BALANCED-SCROLL-VALUESET-MONODROMY-DENSITY`; next
  target `W-MCA-BALANCED-SCROLL-TOTALLY-SPLIT-DENSITY`.

### 2026-06-19 - Cycle 52 totally-split density prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle52_balanced_scroll_totally_split_density.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-BALANCED-SCROLL-TOTALLY-SPLIT-DENSITY`, asking for direct
  monodromy/splitting-density control of the distinct slope image.
- **How it is useful:** Moves the safe-side route away from L2/landing moments
  and toward the actual value-set numerator.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit conservatively.

### 2026-06-19 - Cycle 52 totally-split density audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle52_balanced_scroll_totally_split_density/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE52_TOTALLY_SPLIT_DENSITY_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** ROUTE_CUT / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.
- **What changed:** The monodromy-density formulation is cut. The actual
  fixed-domain MCA object is the discrete configuration of fully `L`-split
  locators, not a free-root cover over the slope line.
- **Banked content:** The reduced moving-scroll incidence is
  `Config cap S`, equivalently the vanishing of degree-2 symmetric determinants
  `a_i(T)b_l(T)-a_l(T)b_i(T)` in the elementary symmetric data of `T`.
- **Route cut:** A `1/j` totally-split density belongs to a relaxed/free-root
  or square-regime cover and is not equivalent to the finite target
  `Z_mov<=R_line+O(j)`.
- **New wall:** `W-MCA-PER-LINE-SYMMETRIC-DETERMINANTAL-INCIDENCE`.

### 2026-06-19 - Cycle 53 symmetric-determinantal prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle53_per_line_symmetric_determinantal_incidence.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-PER-LINE-SYMMETRIC-DETERMINANTAL-INCIDENCE`, asking for a proof,
  counterpacket, or sharper reduction for the deterministic degree-2 symmetric
  determinant incidence bound on `L`-split locators.
- **How it is useful:** Keeps the loop on the fixed-domain per-line incidence
  problem after the free-root monodromy route was cut.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit conservatively.

### 2026-06-19 - Cycle 53 slope-summed character audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle53_per_line_symmetric_determinantal_incidence/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE53_SLOPE_SUMMED_CHARACTER_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **Harness note:** `OK_WITH_NONFATAL_STREAM_WARNING`; one malformed
  stream-json line, usable answer text, raw artifacts preserved before audit.
- **What changed:** The deterministic per-line incidence wall is now an exact
  signed character-sum problem:
  `R=binomial(n,j)/Q^(t-1)-Q*K0_split+Err`.
- **Banked reduction:** `Err=Q^{-t} sum_z sum_{y!=0} S(y,z)`, where the phase
  rewrites as the Cycle44-style cosupport elementary-symmetric sum
  `sum_{x in L\T} beta_x(z)Y(x)prod_{y' in T}(x-y')`.
- **Route cut:** Determinantal codimension plus Bezout is not enough for the
  fixed-domain `L`-split locator bound. Balanced minimal index gives phase
  nondegeneracy only; cancellation remains unproved.
- **New wall:** `W-MCA-PER-LINE-SLOPE-SUMMED-CHARACTER-CANCELLATION`.
- **What to do next:** Stage the first subcase prompt
  `W-MCA-T2-SLOPE-SUMMED-COSUPPORT-CANCELLATION`, asking for a proof of
  `Err<=O(j)` in `t=2` or a source-valid aperiodic counterpacket.

### 2026-06-19 - Cycle 54 t=2 cancellation prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle54_t2_slope_summed_cosupport_cancellation.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-T2-SLOPE-SUMMED-COSUPPORT-CANCELLATION`, the first nontrivial
  specialization of the Cycle53 slope-summed character wall.
- **How it is useful:** Forces the next worker to separate genuine
  cancellation from phase nondegeneracy in the smallest case, or else produce a
  source-valid balanced/transverse/quotient-separated aperiodic counterpacket.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit conservatively.

### 2026-06-19 - Cycle 54 artifact-stream run launched

- **Agent/model:** Codex launching `claude-opus-4-8`.
- **Run path:** `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T10-47-16-076Z-cycle54-t2-slope-summed-cosupport-cancellation-a3e20c65`.
- **Status:** RUN_ACTIVE / GENERATING.
- **Harness:** `artifact_stream`, `claude-opus-4-8`, effort `max`,
  `fable_full_experiment` with system prompt mode `replace`, max budget `$20`,
  output files allowed.
- **Source sync:** Packy project source was refreshed from
  `experimental/2026-06-18-fable-loop/` and `experimental/agents-log.md`
  before launch.
- **Heartbeat:** `rs-mca-cycle49-heartbeat` retargeted to Cycle54 at a
  10-minute cadence.

### 2026-06-19 - Cycle 54 t=2 determinantal quadric audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle54_t2_slope_summed_cosupport_cancellation/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE54_T2_DETERMINANTAL_QUADRIC_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / PROOF / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **Harness note:** `OK`; no stream warning, no `output_files/`, raw artifacts
  preserved before audit.
- **What changed:** The `t=2` slope-summed character wall has a z-eliminated
  determinant form: `R=#{T split : D(T)=0,b(T)!=0}`.
- **Banked lemma:** `D(T)=a_0(T)b_1(T)-a_1(T)b_0(T)` expands as a canonical
  quadratic form in the locator coefficients `ell_T`.
- **Banked proof:** The `j=1` subcase has `R<=2=O(j)` because a projective line
  meets the Veronese conic in at most two points.
- **Route cut/correction:** The `t=2` phase is not generally a single
  elementary-symmetric `e_j` sum; for `j>=2` it involves multiple elementary
  symmetric coordinates.
- **New wall:** `W-MCA-T2-DETERMINANTAL-QUADRIC-SPLIT-COUNT`.
- **What to do next:** Stage `W-MCA-T2J2-DETERMINANTAL-CONIC-SPLIT-PAIR-COUNT`,
  the smallest open case: count split pairs `{s,s'}` on one conic after
  quotient/imprimitive pairs are removed.

### 2026-06-19 - Cycle 55 t=2,j=2 conic prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle55_t2j2_determinantal_conic_split_pair.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-T2J2-DETERMINANTAL-CONIC-SPLIT-PAIR-COUNT`, the smallest open
  subcase after Cycle54 proved `j=1`.
- **How it is useful:** It asks the next worker to prove the conic split-pair
  count, produce a source-valid aperiodic counterpacket, or reduce it to an
  exact Weil/Stepanov-style character-sum statement.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit conservatively.

### 2026-06-19 - Cycle 55 artifact-stream run launched

- **Agent/model:** Codex launching `claude-opus-4-8`.
- **Run path:** `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T11-04-49-776Z-cycle55-t2j2-determinantal-conic-split-pair-c74bc45f`.
- **Status:** RUN_ACTIVE / GENERATING.
- **Harness:** `artifact_stream`, `claude-opus-4-8`, effort `max`,
  `fable_full_experiment` with system prompt mode `replace`, max budget `$20`,
  output files allowed.
- **Source sync:** Packy project source was refreshed from
  `experimental/2026-06-18-fable-loop/` and `experimental/agents-log.md`
  before launch.
- **Heartbeat:** `rs-mca-cycle49-heartbeat` should now target Cycle55 at a
  10-minute cadence.

### 2026-06-19 - Cycle 55 t=2,j=2 conic audit

- **Agent/model:** Codex auditing `claude-opus-4-8`.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/raw/cycle55_t2j2_determinantal_conic_split_pair/`,
  `experimental/2026-06-18-fable-loop/audits/20260619_CYCLE55_T2J2_CONIC_AUDIT.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** BANKABLE_LEMMA / PROOF / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
- **Harness note:** `OK_WITH_NONFATAL_STREAM_WARNING`; one malformed
  stream-json line, usable answer text, no `output_files/`.
- **What changed:** The `t=2,j=2` wall is now an explicit conic/curve problem.
  For `T={s,s'}`, the determinant is `D(s+s',ss')=0`.
- **Banked proof:** After removing tangent/core and quotient/coset components,
  the split-pair curve is bidegree `(2,2)` and Weil gives
  `R=binomial(n,2)/Q+O(sqrt(Q))`.
- **Route cut:** The literal `+O(1)` target is cut in the large-domain
  genus-one regime; a `Theta(sqrt(Q))` Frobenius-trace fluctuation is the
  expected obstruction.
- **Counterpacket status:** The response gives a plausible
  `Theta(sqrt(Q))` excess seed, but it is not banked as `COUNTERPACKET` until a
  local checker and source-validity audit verify a concrete growing family.
- **New wall:** `W-MCA-T2J2-CONIC-SPLIT-PAIR-COUNT-CORRECTED`.
- **What to do next:** Stage `W-MCA-T2J2-CONIC-SQRT-COUNTERPACKET-CHECK`:
  verify the conic identity and search for non-core, non-coset examples with
  excess `~sqrt(Q)`.

### 2026-06-19 - Cycle 56 conic sqrt counterpacket-check prompt staged

- **Agent/model:** Codex.
- **Files added or changed:** `experimental/2026-06-18-fable-loop/prompts/20260619_cycle56_t2j2_conic_sqrt_counterpacket_check.md`,
  `experimental/2026-06-18-fable-loop/README.md`, and
  `experimental/2026-06-18-fable-loop/SHA256SUMS.txt`.
- **Status:** STAGED_PROMPT / AUDIT.
- **What is being added:** A focused prompt for
  `W-MCA-T2J2-CONIC-SQRT-COUNTERPACKET-CHECK`, the finite/source-validity
  check created by Cycle55.
- **How it is useful:** It forces the next worker to either promote the
  `Theta(sqrt(Q))` genus-one fluctuation seed into a real source-valid
  `COUNTERPACKET`, or kill it by identifying the exact source hypothesis that
  restores the desired bound.
- **What to do next:** Launch via artifact stream, preserve the raw response,
  and audit conservatively.

### 2026-06-19 - Cycle 56 artifact-stream run launched

- **Agent/model:** Codex launching `claude-opus-4-8`.
- **Run path:** `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T11-37-03-979Z-cycle56-t2j2-conic-sqrt-counterpacket-check-a15f0ab3`.
- **Status:** RUN_ACTIVE / GENERATING.
- **Harness:** `artifact_stream`, `claude-opus-4-8`, effort `max`,
  `fable_full_experiment` with system prompt mode `replace`, max budget `$20`,
  output files allowed.
- **Source sync:** Packy project source was refreshed from
  `experimental/2026-06-18-fable-loop/` and `experimental/agents-log.md`
  before launch.
- **Heartbeat:** `rs-mca-cycle49-heartbeat` should now target Cycle56 at a
  10-minute cadence.
