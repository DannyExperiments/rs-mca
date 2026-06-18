# 2026-06-18 Fable Loop

Status: EXPERIMENTAL / AUDIT.

This folder records Codex-managed Opus 4.8 co-director cycles after the manual integration of PR #62 into upstream `main`.

Source policy:

- Main papers are not edited here.
- Raw model outputs are provenance, not promoted claims.
- Audits decide what, if anything, should be treated as `BANKABLE_LEMMA`, `COUNTERPACKET`, `ROUTE_CUT`, or `EXACT_NEW_WALL`.

Cycle 1 target:

- F1 arbitrary-anchor balanced denominator gap in `tex/slackMCA_v3.tex:def:residue`, with balanced `t=sigma`.

Cycle 1 audit:

- `audits/20260618_CYCLE1_F1_ARBITRARY_ANCHOR_AUDIT.md`

Cycle 2 target:

- Adversarial audit of the paired base interpolation-residue readout from Cycle 1.

Cycle 2 first attempt:

- `audits/20260618_CYCLE2_PAIRED_BASE_READOUT_HUNG_RUN.md`
- Status: `HARNESS_FAILED` / `AUDIT`; no mathematics banked.

Cycle 2 retry prompt:

- `prompts/20260618_cycle2_retry_paired_base_readout_short.md`

Bounded local audit:

- `audits/20260618_CODEX_LOCAL_PAIRED_BASE_READOUT_AUDIT.md`

Cycle 2 retry audit:

- `audits/20260618_CYCLE2_PAIRED_BASE_READOUT_RETRY_AUDIT.md`
- Status: `BANKABLE_LEMMA` / `EXACT_NEW_WALL`.

Cycle 3 local audit:

- `audits/20260618_CODEX_LOCAL_NONCONTAINMENT_SUBSET_LEMMA.md`
- Status: `BANKABLE_LEMMA` / `AUDIT`.

Cycle 3 Fable audit:

- `audits/20260618_CYCLE3_W_F1_AA_NONCONTAINMENT_AUDIT.md`
- Status: `BANKABLE_LEMMA` / `EXACT_NEW_WALL`.

Cycle 4 balance-notation audit:

- `audits/20260618_CYCLE4_BALANCE_NOTATION_ROUTE_CUT_AUDIT.md`
- Status: `ROUTE_CUT` for `W-F1-AA-AGR` as a balanced wall; the noncontainment lemma remains banked.

Cycle 5 restored W-F1-AA audit:

- `raw/20260618_CYCLE5_W_F1_AA_RES_RAW.md`
- `audits/20260618_CYCLE5_W_F1_AA_RES_EXACT_WALL_AUDIT.md`
- Status: `EXACT_NEW_WALL` / `AUDIT`.
- Banked conservative content: restored `W-F1-AA` is sharpened to `W-F1-AA-RES`, the reserve-indexed paired-readout rigidity/value-count wall. This is not a proof of F1, not a protocol statement, and not a new corrected-reserve counterpacket.

Cycle 6 VS Code credited-terminal attempt:

- `raw/20260618_CYCLE6_W_F1_AA_RES_RIGIDITY_RAW_MALFORMED.json`
- `raw/20260618_CYCLE6_W_F1_AA_RES_RIGIDITY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE6_W_F1_AA_RES_RIGIDITY_RUN_RESULT.json`
- `audits/20260618_CYCLE6_W_F1_AA_RES_RIGIDITY_HARNESS_MALFORMED.md`
- Status: `HARNESS_MALFORMED_VISIBLE_TERMINAL` / `AUDIT`.
- No mathematics banked. The apparent rigidity lemma candidate is a retry target only because the VS Code visible-terminal artifact has missing letters/spaces and duplicated fragments; no clean `response.md` was produced.

Cycle 6B clean-retry attempt:

- `raw/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RAW_MALFORMED.json`
- `raw/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RUN_RESULT.json`
- `raw/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RECOVERED_CLAUDE_JSONL.md`
- `audits/20260618_CYCLE6B_W_F1_AA_RES_RIGIDITY_RECOVERED_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`.
- Mathematical audit status: `EXACT_NEW_WALL` / `AUDIT`, based on source-checking
  the recovered structured Claude JSONL answer. Banked route clarification:
  the same-slope kernel `E*F_{<k}[X]` is not the wall; the live wall is
  `W-F1-AA-RES-VALUECOUNT`, a value-count / collision law for distinct slopes
  in the paired-readout image on `F*[Bnum]_E`.

Cycle 7 value-count attempt:

- `prompts/20260618_cycle7_w_f1_aa_res_valuecount.md`
- `raw/20260618_CYCLE7_W_F1_AA_RES_VALUECOUNT_RECOVERED_CLAUDE_JSONL.md`
- `local_checks/20260618_cycle7_theta_multiplier_check.py`
- `audits/20260618_CYCLE7_W_F1_AA_RES_VALUECOUNT_TWISTED_READOUT_AUDIT.md`
- Harness note: the VS Code terminal `response.md` was visibly damaged despite
  `run_result.json` reporting `BANKABLE_LEMMA`; the clean receipt was recovered
  from Claude structured JSONL.
- Mathematical audit status: `ROUTE_CUT / EXACT_NEW_WALL`.
- Do not bank the claimed exact transfer to a base datum
  `(Ehat,b_hat,w0+theta*w1)`. The nonconstant CRT multiplier `theta` does not
  commute with support interpolation in general.
- Live wall: `W-F1-AA-RES-TWISTED-READOUT`, a value-count/collision theorem or
  counterpacket for `[interp_S(w0)]_Ehat + theta [interp_S(w1)]_Ehat`.

Cycle 8 twisted-readout attempt:

- `prompts/20260618_cycle8_w_f1_aa_res_twisted_readout.md`
- `raw/20260618_CYCLE8_W_F1_AA_RES_TWISTED_READOUT_RECOVERED_CLAUDE_JSONL.md`
- `local_checks/20260618_cycle8_twisted_readout_verify.py`
- `audits/20260618_CYCLE8_W_F1_AA_RES_TWISTED_READOUT_AUDIT.md`
- Harness status: clean structured Claude JSONL used for `response.md`.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL`.
- Banked content: `B[X]/Ehat ~= F[X]/E`, so the twisted readout is exactly
  `pi^{-1}([interp_S(w)]_E)`; the commutator with pointwise
  `theta*w1` is locator-divisible.
- Live wall: `W-F1-AA-RES-RESIDUE-COUNT`, a direct value-count/collision theorem
  or counterpacket for `[interp_S(w0)+alpha interp_S(w1)]_E`.

Cycle 9 line-incidence correction:

- `prompts/20260618_cycle9_w_f1_aa_res_residue_count.md`
- `raw/20260618_CYCLE9_W_F1_AA_RES_RESIDUE_COUNT_RECOVERED_CLAUDE_JSONL.md`
- `local_checks/20260618_cycle9_locator_quotient_incidence_check.py`
- `audits/20260618_CYCLE9_W_F1_AA_RES_RESIDUE_COUNT_LINE_INCIDENCE_AUDIT.md`
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL`.
- Banked content: the source MCA object is not raw residue cardinality. It is
  the bad-line slope/incidence count
  `#{z in F : exists S, [interp_S(w)]_E=z[Bnum]_E}`. The locator-quotient
  identity is `W=L_S Q_S+interp_S(w)`, `deg Q_S<=n-a-1`.
- Live wall: `W-F1-AA-RES-LINE-INCIDENCE`.

Cycle 10 manual route-cut reinforcement:

- `raw/20260618_CYCLE10_MANUAL_W_F1_AA_RES_RESIDUE_COUNT_RESPONSE.md`
- `audits/20260618_CYCLE10_MANUAL_RESIDUE_COUNT_ROUTE_CUT_AUDIT.md`
- Mathematical audit status: `ROUTE_CUT / EXACT_NEW_WALL / AUDIT`.
- Banked content: `ONLINE-SLOPE-COUNT` and `LINE-INCIDENCE` are the same
  source-corrected wall. Do not split them into separate targets.

Cycle 11 t=2, j=2 line-incidence audit:

- `prompts/20260618_cycle11_w_f1_aa_res_line_incidence.md`
- `raw/20260618_CYCLE11_W_F1_AA_RES_LINE_INCIDENCE_RESPONSE.md`
- `raw/20260618_CYCLE11_W_F1_AA_RES_LINE_INCIDENCE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE11_W_F1_AA_RES_LINE_INCIDENCE_RUN_RESULT.json`
- `local_checks/20260618_cycle11_t2_j2_line_incidence_verify.py`
- `audits/20260618_CYCLE11_T2_J2_LINE_INCIDENCE_AUDIT.md`
- Harness note: VS Code terminal response was malformed, but clean theorem text
  was recovered from Claude structured JSONL and written to `response.md`.
- Mathematical audit status: `BANKABLE_LEMMA / AUDIT`.
- Banked content: in the restricted regime `t=sigma=2`, `j=n-a=r-t=2`,
  `Q_S=C(X-s_T)+C1`, bad-line landing is one conic `det(s_T,p_T)=0`,
  `[p^2]det=wedge([W]_E,[Bnum]_E)`, and the nonresonant slope count is
  `O(n)` (`C2<=6n`, generically `C2<=4`).
- Not banked: `conj:B`, `j>=3`, `t>=3`, `q_gen` collapse, protocol/MCA/CA/
  list-decoding consequences.
- Next wall: `W-F1-AA-RES-T2J3`; secondary wall `W-F1-AA-RES-T3J2`.

Cycle 12 t=2, j=3 quotient/quadric audit:

- `prompts/20260618_cycle12_w_f1_aa_res_t2j3.md`
- `raw/20260618_CYCLE12_W_F1_AA_RES_T2J3_RESPONSE.md`
- `audits/20260618_CYCLE12_T2_J3_LINE_INCIDENCE_AUDIT.md`
- `local_checks/20260618_cycle12_t2_j3_line_incidence_scan.py`
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: `Q_S` depends on `tau_1,tau_2` and not `tau_3`; bad-line
  landing is a quadric with `[tau_3^2]Delta=wedge([W]_E,[Bnum]_E)`.
- Not banked: a `C2` slope bound. The live wall becomes slope-fiber collapse.

Cycle 13 base-component complete-intersection audit:

- `prompts/20260618_cycle13_base_component_complete_intersection.md`
- `raw/20260618_CYCLE13_BASE_COMPONENT_COMPLETE_INTERSECTION_RESPONSE.md`
- `audits/20260618_CYCLE13_BASE_COMPONENT_COMPLETE_INTERSECTION_AUDIT.md`
- `local_checks/20260618_cycle12_base_component_rank_scan.py`
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: off `R0 union Ra union Rb`, the base components
  `Delta_0,Delta_1` are coprime, so `#landings=O(p)` and hence `C2=O(n)` for
  `D=F_p`, `t=sigma=2`, `j=3`.
- Live wall: resonance strata `Ra/Rb`.

Cycle 14 resonance slope-map audit:

- `prompts/20260618_cycle14_base_component_resonance.md`
- `raw/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_RESPONSE.md`
- `audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`
- Mathematical audit status: `EXACT_NEW_WALL / AUDIT`.
- Banked content: the resonance strata are not source-excluded by the current
  hypotheses. The residual problem is the explicit slope map on a base surface:
  `q1 z^2-(p1-q2)z-p2=0`, `tau_3=p1-zq1 in B`.
- Live wall: `W-F1-AA-RES-T2J3-SURFACE-SLOPE-FIBER`.

Cycle 15 surface slope-fiber rank/determinant audit:

- `prompts/20260618_cycle15_surface_slope_fiber.md`
- `raw/20260618_CYCLE15_SURFACE_SLOPE_FIBER_RESPONSE.md`
- `raw/20260618_CYCLE15_SURFACE_SLOPE_FIBER_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE15_SURFACE_SLOPE_FIBER_RUN_RESULT.json`
- `audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `local_checks/20260618_cycle15_forced_ra_slope_scan.py`
- `local_checks/20260618_cycle15_forced_ra_slope_scan_certificate.md`
- Harness status: clean structured Claude JSONL was promoted to `response.md`;
  terminal transcript is revenue/debug evidence only.
- Mathematical audit status: `EXACT_NEW_WALL / AUDIT`.
- Banked content: the residual surface slope problem reduces to the affine
  equation `L_z(tau)=iota-z mu=0` in `A=F[X]/E`, with explicit `B`-columns
  `c1(z),c2(z),c3(z)` and determinant consistency polynomial
  `Q(z_0,z_1)`.
- Audit correction: rank `3` alone does not imply `Theta(q_line)` slopes.
  The safe wall is the rank/determinant pair: `Q!=0` gives a curve-sized
  slope set, while `Q==0` identically is the possible large-slope regime.
- Live wall:
  `W-F1-AA-RES-T2J3-SURFACE-SLOPE-FIBER-RANK-DETERMINANT`.

Cycle 16 rank/determinant resonance audit:

- `prompts/20260618_cycle16_rank_determinant_resonance.md`
- `raw/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_RAW.json`
- `raw/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_RUN_RESULT.json`
- `raw/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; terminal scrape is
  rejected. Clean structured Claude JSONL recovery is the audited math
  artifact.
- Source-mount audit: Packy source mirror was stale and did not include Cycle
  15 audit/certificate files; ledgers were sufficient for this run, but the
  source mirror must be repaired before Cycle 17.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: off `R0`, if `Q(z_0,z_1)` is not identically zero, then
  `C2<=4p=O(p)=O(n)` in the `D=F_p`, `t=sigma=2`, `j=3` regime.
- Audit-only content: the proposed trace/Gram criterion for `Q==0` is a useful
  verifier target but is not yet banked as proved.
- Live wall: `W-F1-AA-RES-T2J3-RANK-DET-SPLIT`, the `Q==0` branch restricted
  to distinct `D`-split cubics.

Cycle 17 rank-det split scanner attempt:

- `prompts/20260618_cycle17_rank_det_split_scanner.md`
- `raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RAW.json`
- `raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RUN_RESULT.json`
- `raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_TUI_RUNNER_RESULT.json`
- `audits/20260618_CYCLE17_RANK_DET_SPLIT_SCANNER_HARNESS_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no `response.md` was
  produced and no `output_files/` deliverables were written.
- Mathematical audit status: `AUDIT`; no theorem, counterpacket, or executable
  scanner is banked. The readable structured-JSONL recovery is preserved as
  provenance only.
- Current live wall remains `W-F1-AA-RES-T2J3-RANK-DET-SPLIT`.

Cycle 18 homerun / big-leap attempt:

- `prompts/20260618_cycle18_homerun_full_solve_or_big_leap.md`
- `raw/20260618_CYCLE18_HOMERUN_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE18_HOMERUN_RAW.json`
- `raw/20260618_CYCLE18_HOMERUN_RUN_RESULT.json`
- `raw/20260618_CYCLE18_HOMERUN_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE18_HOMERUN_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE18_HOMERUN_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE18_HOMERUN_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no `response.md` was
  produced. The readable structured-JSONL recovery is audited conservatively
  and the visible-terminal scrape is not banked as mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: in the restricted `D=F_p`, `t=sigma=2`, `j=3`, off-`R0`
  window, the Cycle 14 determinant in the `{[W]_E,b}` basis is monic
  quadratic in `tau_3`; after splitting `Delta=Delta0+alpha Delta1`,
  `Delta0` is monic degree `2` in `tau_3` and `deg_{tau_3} Delta1<=1`.
- Live wall:
  `W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE`.
- Not banked: a full proof/disproof, the resonance slope-map collapse itself,
  a `Theta(q_line)` counterpacket, any above-reserve statement, any `q_gen`
  conclusion, or any protocol/list/CA/MCA/line-decoding conversion.

Cycle 19 resonance slope-map collapse prompt:

- `prompts/20260618_cycle19_resonance_slope_map_collapse.md`
- Status: AUDIT / prompt staged.
- Target:
  `W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE`.
- Purpose: ask for a proof of the non-coprime resonance slope-map collapse, a
  growing-prime counterpacket, a route cut, or a sharper exact wall using the
  Cycle 18 monicity lemma as banked context.

Cycle 19 resonance collapse answer:

- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RAW.json`
- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RUN_RESULT.json`
- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE19_RESONANCE_COLLAPSE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE19_RESONANCE_COLLAPSE_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced.
- Mathematical audit status: `AUDIT`; the recovered structured text proposes
  candidate rank-one and scalar-gate formulas, but these are not yet banked as
  theorem content.
- Candidate next wall:
  `W-F1-AA-RES-T2J3-RANKONE-GATE-AUDIT`.

Cycle 20 rank-one/gate audit prompt:

- `prompts/20260618_cycle20_rankone_gate_audit.md`
- Status: AUDIT / prompt staged.
- Purpose: prove or refute the Cycle 19 candidate closed forms, the rank-one
  `q1` lemma, the quadric normal form, and the scalar gate `D`.

Cycle 20 rank-one/gate answer:

- `raw/20260618_CYCLE20_RANKONE_GATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE20_RANKONE_GATE_RAW.json`
- `raw/20260618_CYCLE20_RANKONE_GATE_RUN_RESULT.json`
- `raw/20260618_CYCLE20_RANKONE_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE20_RANKONE_GATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE20_RANKONE_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: closed forms for `p1,p2,q1,q2`; rank-one leading coefficient
  `q1=-(Q_E(b)/kappa)eta`; quadric-branch normal form; and gate identity
  `det M=(c_b/kappa^2)D`.
- Live wall: `W-F1-AA-RES-T2J3-B-RANKONE-DESCENT`.

Cycle 21 B-rank-one descent prompt:

- `prompts/20260618_cycle21_b_rankone_descent.md`
- Status: AUDIT / prompt staged.
- Purpose: decide whether the `Delta1==0` base-descent equations force
  `dw wedge d eta == 0`, or expose a source-valid `Theta(q_line)` seed.

Cycle 21 B-rank-one descent answer:

- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_RAW.json`
- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_RUN_RESULT.json`
- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE21_B_RANKONE_DESCENT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: differential gates for the two slope branches, reduction of
  simultaneous branch collapse to `J_A=J_Aprime=0`, and the identification of
  the Cycle 20 gate `D` as the resultant of those two collapse gates.
- Rejected overclaim: the recovered answer did not prove that the base-descent
  equations are independent of the collapse gate and did not give a
  source-valid counterpacket.
- Live wall: `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`.

Cycle 22 D-kernel alignment prompt:

- `prompts/20260618_cycle22_d_kernel_alignment.md`
- Status: AUDIT / prompt staged.
- Purpose: decide whether `Delta1==0`, `D==0`, and the two base-descent
  equations force the leading-data ratio
  `(W_{n-2}+cW_{n-1}:W_{n-1})` onto the collapse-kernel line, or whether an
  off-kernel source-valid family exists.

Cycle 22 D-kernel alignment answer:

- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RAW.json`
- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RUN_RESULT.json`
- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced and no `output_files/` deliverables were written.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: `Delta1==0` is exactly the two base-descent equations; on
  `D=0`, alignment reduces to `J_A=0`; and on `Delta1==0`,
  `Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2`.
- Rejected overclaim: no nonemptiness, slope lower bound, or counterpacket is
  banked.
- Live wall: `W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS`.

Cycle 23 nonemptiness/split-count prompt:

- `prompts/20260618_cycle23_nonemptiness_split_count.md`
- Status: AUDIT / prompt staged.
- Purpose: settle whether the explicit `c in B`, `d notin B`, `Delta1==0`,
  `D=0` off-kernel stratum is source-valid and nonempty, and if so whether it
  has `Omega(p^2)` or only `O(p)` split-cubic bad slopes.
