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

Cycle 23 c-in-B D-kernel emptiness answer:

- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RAW.json`
- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RUN_RESULT.json`
- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE23_NONEMPTINESS_SPLIT_COUNT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE23_CINB_DKERNEL_EMPTINESS_AUDIT.md`
- `local_checks/20260618_cycle23_cinb_dkernel_identity_check.py`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / AUDIT`.
- Banked content: in the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`,
  `t=sigma=2`, `j=3`, off-`R0` window, if `c in B` and `d notin B`, then
  `ell=[X^p-X]_E=mu*(xi+c/2)` and
  `D=-mu^2(c^2/4-d)kappa != 0`.
- Consequence: the `c in B`, `d notin B`, `D=0`, off-`R0` branch is empty;
  Cycle 22's nonemptiness/split-count target is closed on this subcase.
- Live wall: `W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C`, the complementary
  `c notin B` branch.
- Not banked: nonemptiness or split count in the `c notin B` lane, any
  `Theta(q_line)` counterpacket, corrected-reserve consequences, or any
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement.

Cycle 24 nonsplit-c D-kernel prompt:

- `prompts/20260618_cycle24_nonsplit_c_dkernel.md`
- Status: AUDIT / prompt staged.
- Purpose: attack the only surviving `D=0`, off-`R0`, separated-`E` lane:
  `c notin B`. The prompt asks for a closed form for `[X^p-X]_E`, a bilinear
  form for `D`, and a proof/counterpacket/exact wall for the joint
  `D=0`, `Delta1==0` split-cubic slope-count problem.

Cycle 24 D-kernel norm-factorization answer:

- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RAW.json`
- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RUN_RESULT.json`
- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`
- `local_checks/20260618_cycle24_dkernel_norm_identity_check.py`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / AUDIT`.
- Banked content: in the restricted `D=F_p`, `B=F_p`, `F=F_{p^2}`,
  `t=sigma=2`, `j=3`, off-`R0` window,
  `ell=[X^p-X]_E=mu*(xi+c/2)+delta_c`, with
  `mu=(c^2/4-d)^((p-1)/2)-1` and `delta_c=(c-c^p)/2`, and
  `D=N(ell)kappa`, where `N(ell)=prod_{a in F_p}E(a)`.
- Consequence: for source-valid residue-line denominators nonzero on
  `D=F_p`, `N(ell)!=0`; off `R0`, `kappa!=0`; therefore the entire
  source-valid `D=0`, off-`R0` branch is empty in this restricted window.
- Live wall: return to the non-`D=0` determinant-split branch,
  `W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT`.
- Not banked: any corrected-reserve theorem, full MCA bound, `q_gen`
  consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement,
  or claim that the Proximity Prize is solved.

Cycle 25 Q==0 with detM nonzero prompt:

- `prompts/20260618_cycle25_qzero_detm_nonzero_split.md`
- Status: AUDIT / prompt staged.
- Purpose: attack the remaining `Q==0`, `D!=0`, `det M!=0` distinct
  split-cubic branch after Cycle 24 cut the source-valid `D=0` branch.
  The prompt asks for a proof of `O(p)` slopes, a source-valid growing-prime
  `Theta(q_line)` counterpacket, or the exact next algebraic wall.

Cycle 25 Q-zero detM-nonzero answer:

- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RAW.json`
- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RUN_RESULT.json`
- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: the six-term Plucker/Laplace expansion for the determinant
  consistency polynomial `Q(z_0,z_1)`, and the separation between the
  `z`-free invariant `det M=(c_b/kappa^2)D` and the slope-fiber determinant
  `Q(z)`.
- Audit correction: the recovered answer overclaims that `Q(z)=0 iff z in C2`
  and that `Q==0` identically gives all `p^2` slopes. In fact `Q(z)=0` is only
  a necessary consistency condition unless the three coefficient columns have
  rank `3`; rank-drop strata require augmented-rank minors.
- Live wall: `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`.
- Not banked: any `Theta(q_line)` counterpacket, any proof of `O(p)` on the
  branch, any corrected-reserve theorem, full MCA bound, `q_gen` consequence,
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement, or prize solve.

Cycle 26 Q-zero rank-consistency prompt:

- `prompts/20260618_cycle26_qzero_rank_consistency.md`
- Status: AUDIT / prompt staged.
- Purpose: attack the rank-stratified consistency problem after Cycle 25
  corrected the false implication `Q==0 => every slope realized`. The prompt
  asks for an `O(p)` proof, a source-valid growing-prime counterpacket, or the
  exact rank/minor elimination certificate.

Cycle 26 Q-zero rank-consistency answer:

- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RAW.json`
- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RUN_RESULT.json`
- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: the DEP/NONDEP rank dichotomy; `c notin B` with `c_b != 0`
  forces NONDEP; in NONDEP, rank-drop costs only `O(p)` slopes, so
  `Q` not identically zero gives `O(p)` affine-consistent slopes.
- Audit correction: the proposed top-degree `Q_4` obstruction is promising but
  remains audit-only until verified independently from the Cycle 15/16 column
  definitions, and affine `tau in B^3` consistency must still be separated from
  the actual distinct `D`-split cubic line-incidence gate.
- Live wall: `W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE`.
- Not banked: any full `O(p)` proof on the `Q==0` branch, any
  `Theta(q_line)` counterpacket, any corrected-reserve theorem, full MCA bound,
  `q_gen` consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK
  statement, or prize solve.

Cycle 27 Q4 obstruction and split-cubic gate prompt:

- `prompts/20260618_cycle27_q4_split_gate.md`
- Status: AUDIT / prompt staged.
- Purpose: verify or refute the Cycle 26 `Q_4` formula, prove or refute
  source-valid `Q_4 != 0` on the NONDEP `c notin B` branch, and keep the
  distinct split-cubic gate separate from affine `tau` consistency.

Cycle 27 Q4 obstruction answer:

- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RAW.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RUN_RESULT.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE27_Q4_SPLIT_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE27_Q4_SPLIT_GATE_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / AUDIT`.
- Banked candidate: the corrected top coefficient of `Q` is
  `Q_4=N(c_b)*(Im(d)^2-Im(c)*Im(conj(c)d))`; the apparent `P`-dependence in
  the Cycle 26 display cancels because the `P`-part of `q2` is collinear with
  the rank-one direction of `q1`.
- Source-valid consequence, subject to independent confirmation of the column
  conventions: if `c notin B`, then
  `Q_4=N(c_b)*Im(c)^2*E(-Im(d)/Im(c))`, so `Q_4=0` iff `E` has an
  `F_p`-root iff `prod_{a in F_p}E(a)=0`. Source-validity excludes this.
  If `c in B`, then `Q_4=N(c_b)*Im(d)^2`, and separatedness excludes
  `d in B`. Thus `Q_4!=0` on both separated source-valid branches.
- Consequence: the source-valid `Q==0` branch in the restricted `t=2,j=3`
  window appears cut; by Cycle 16 this gives `O(p)` affine-consistent slopes,
  and the distinct split-cubic gate only shrinks the set.
- Audit correction: do not promote to `PROOF` until a fresh worker rederives
  the `Q_4` formula and the `q2` closed form from source definitions.
- Live wall: `W-F1-AA-RES-T2J3-Q4-PROOF-AUDIT`.
- Not banked: any corrected-reserve theorem, full MCA bound, `q_gen`
  consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement,
  or prize solve.

Cycle 28 Q4 proof-audit prompt:

- `prompts/20260618_cycle28_q4_proof_audit.md`
- Status: AUDIT / prompt prepared.
- Purpose: independently rederive the Cycle 27 `Q_4` formula from the
  Cycle 15/16/20/25 definitions, verify source-valid nonvanishing, and decide
  whether the restricted `t=2,j=3` branch can be promoted to a local proof or
  must remain an audit/exact wall.

Cycle 28 Q4 proof-audit answer:

- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RAW.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RUN_RESULT.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE28_Q4_PROOF_AUDIT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE28_Q4_PROOF_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `PROOF / ROUTE_CUT / AUDIT` for the restricted
  local theorem only.
- Proved restricted statement: in the `D=F_p`, `B=F_p`, `F=F_{p^2}`,
  `t=sigma=2`, `j=3`, off-`R0`, `c_b!=0`, source-valid separated window,
  the determinant consistency polynomial `Q` is never identically zero. Hence
  `C2<=4p=O(p)` by Cycle 16, and the distinct split-cubic gate only shrinks the
  realized slope set.
- Proof mechanism: `Q_4=N(c_b)*(Im(d)^2-Im(c)*Im(conj(c)d))`; for `c notin B`
  this equals `N(c_b)*Im(c)^2*E(-Im(d)/Im(c))`, so vanishing is equivalent to
  an `F_p` root of `E`; for `c in B`, it is `N(c_b)*Im(d)^2`, nonzero by
  separatedness.
- Route cut: do not search for source-valid `Theta(q_line)` counterpackets in
  this restricted `t=2,j=3` branch.
- Live wall: `W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL`.
- Not banked: any corrected-reserve theorem, full MCA bound, `q_gen`
  consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement,
  or prize solve.

Cycle 29 T2J4 locator-norm top-symbol prompt:

- `prompts/20260618_cycle29_t2j4_locator_norm_top_symbol.md`
- Status: AUDIT / prompt prepared.
- Purpose: test whether the Cycle 28 top-symbol mechanism persists at
  `t=2,j=4`, namely whether the highest-degree slope-consistency coefficient
  is a nonzero scalar times a power of `prod_{a in F_p}E(a)`.

Cycle 29 T2J4 locator-norm top-symbol answer:

- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RAW.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RUN_RESULT.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE29_T2J4_LOCATOR_NORM_TOP_SYMBOL_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Banked content: at `t=2,j=4`, the quotient depends on
  `tau_1,tau_2,tau_3`, while the locator residue introduces `tau_4`; the
  affine bad-line system has four parameters in the four-dimensional
  `B`-space `A=F[X]/E`. Thus the determinant is the square coefficient
  determinant `det_B M(z)`, an invertibility/uniqueness determinant, not the
  Cycle 28 incidence obstruction. The top symbol is
  `-N(kappa)N(z)^2Q_4`, with the same source-valid nonzero Cycle 28 locator
  quantity `Q_4`.
- Exact new wall: because affine consistency is generically automatic at
  `j=4`, the remaining source-correct problem is the split-quartic gate
  `W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE`.
- Not banked: any `O(p)` slope bound for `j=4`, any source-valid
  `Theta(q_line)` counterpacket, corrected-reserve theorem, full MCA bound,
  `q_gen` consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK
  statement, or prize solve.

Cycle 30 T2J4 split-quartic gate prompt:

- `prompts/20260618_cycle30_t2j4_split_quartic_gate.md`
- Status: AUDIT / prompt prepared.
- Purpose: attack the actual `j=4` gate: bound or refute the number of slopes
  for which `tau(z)=M(z)^(-1)(-C_0(z))` is the elementary-symmetric tuple of a
  distinct 4-subset of `F_p`.

Cycle 30 T2J4 split-quartic gate answer:

- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RAW.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RUN_RESULT.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE30_T2J4_SPLIT_QUARTIC_GATE_AUDIT.md`
- `local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py`
- `local_checks/20260618_cycle30_t2_j4_split_quartic_scan_certificate.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT`.
- Banked content: the `j=4` split-quartic gate is the vanishing of one
  `F`-quadric
  `Phi(tau)=kappa*N_{A/F}(lambda)-(ell[Q_S]_E) wedge_F (b*lambda)` on the
  elementary-symmetric tuple `tau=e(T)` of a distinct 4-subset `T`.
- Local experimental scan: direct finite counts through `p=29` lean toward
  `O(p)`-scale growth, not the recovered answer's generic
  `Theta(q_line)` heuristic.
- Exact new wall: `W-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE`.
- Not banked: any proof of `O(p)`, any `Theta(q_line)` counterpacket,
  corrected-reserve theorem, full MCA bound, `q_gen` consequence,
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement, or prize solve.

Cycle 31 T2J4 split-quadric collapse prompt:

- `prompts/20260618_cycle31_t2j4_split_quadric_collapse.md`
- Status: AUDIT / prompt prepared.
- Purpose: attack the hidden structure suggested by the finite scan: prove an
  `O(p)` split-collapse theorem for `Phi(e(T))=0`, or produce a source-valid
  family that realizes positive-density slopes despite the small-prime data.

Cycle 31 T2J4 split-quadric collapse answer:

- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RAW.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RUN_RESULT.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE31_T2J4_SPLIT_QUADRIC_COLLAPSE_AUDIT.md`
- `local_checks/20260618_cycle31_t2_j4_scaling_spotcheck_certificate.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `EXACT_NEW_WALL / AUDIT`.
- Banked content: Cycle 31 does not prove that `O(p)` collapse is impossible
  and does not bank a `Theta(q_line)` counterpacket. It does identify the next
  exact invariant: compute the quartic discriminant/resolvent/monodromy of
  `L_{tau(z)}` and decide whether the split locus has positive density.
- Local experimental spot-check: small extended scans at `p=31` and `p=37`
  make the earlier phrase "leans O(p)" too strong, but still do not prove
  `1/24` density or any asymptotic.
- Exact new wall: `W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4`.
- Not banked: any proof of `O(p)`, any proof that `O(p)` is impossible, any
  `Theta(q_line)` counterpacket, corrected-reserve theorem, full MCA bound,
  `q_gen` consequence, protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK
  statement, or prize solve.

Cycle 32 T2J4 quartic monodromy prompt:

- `prompts/20260618_cycle32_t2j4_quartic_monodromy_s4.md`
- Status: AUDIT / prompt prepared.
- Purpose: audit the exact discriminant/resolvent/monodromy invariant for
  `L_{tau(z)}`, including the base-field issue for `z in F_{p^2}` and
  splitting over `B=F_p`.

Cycle 32 T2J4 quartic monodromy answer:

- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RAW.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RUN_RESULT.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE32_T2J4_QUARTIC_MONODROMY_BASE_FIELD_AUDIT.md`
- `local_checks/20260618_cycle32_t2_j4_monodromy_histogram.py`
- `local_checks/20260618_cycle32_t2_j4_monodromy_histogram_certificate.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `ROUTE_CUT / EXACT_NEW_WALL / EXPERIMENTAL / AUDIT`.
- Banked content: the `t=2,j=4` quartic family is a two-dimensional
  `B`-surface family over `A^2_B` with coordinates `z=z_0+alpha z_1`, not a
  one-variable `B(z)` or `F(z)` family. A local Cramer-system histogram checker
  matches direct support enumeration away from the singular determinant curve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-MONODROMY-CERTIFICATE`.

Cycle 33 A2_B monodromy certificate prompt:

- `prompts/20260618_cycle33_a2b_monodromy_certificate.md`
- Status: AUDIT / prompt prepared.
- Purpose: decide whether the Cycle 32 checker and Cycle 29/30 equations can
  be upgraded into a real surface monodromy / singular-curve certificate, or
  whether a constant-field, singular-curve, or checker obstruction remains.

Cycle 33 A2_B monodromy certificate answer:

- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RAW.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RUN_RESULT.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE33_A2B_MONODROMY_CERTIFICATE_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / CONDITIONAL / EXACT_NEW_WALL /
  AUDIT`.
- Banked content: in the restricted `D=F_p`, `B=F_p`,
  `F=F_{p^2}`, `t=sigma=2`, `j=4` branch, assuming the Cycle 29 top-symbol
  nonzero hypotheses, the singular determinant curve
  `Delta(z_0,z_1)=0` has degree at most four and contributes at most `4p`
  split slopes.
- Not banked: positive off-curve split density, `S_4`, arithmetic/geometric
  monodromy equality, a `Theta(q_line)` counterpacket, corrected-reserve
  theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/SNARK statement, or
  prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT`.

Cycle 34 A2_B dominance/resolvent prompt:

- `prompts/20260618_cycle34_a2b_dominance_resolvent.md`
- Status: AUDIT / prompt prepared.
- Purpose: decide whether the off-curve rational map
  `tau(z_0,z_1)=M(z)^(-1)(-C_0(z))` has generic `B`-Jacobian rank two and
  whether the substituted quartic resolvent/discriminant gives a transitive
  monodromy/constant-field certificate.

Cycle 34 A2_B dominance/resolvent answer:

- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RAW.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RUN_RESULT.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE34_A2B_DOMINANCE_RESOLVENT_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL /
  AUDIT`.
- Banked content: in the restricted `D=F_p`, `B=F_p`,
  `F=F_{p^2}`, `t=sigma=2`, `j=4` branch, on the stated source-valid dense
  open, the off-curve rational map
  `psi:z |-> tau(z)=M(z)^(-1)(-C_0(z))` has generic `B`-Jacobian rank two and
  is birational onto the Cycle 30 quadric image.
- Route cut: the attempted rank-one / hidden curve-collapse explanation for
  `O(p)` off-curve split count is eliminated in this branch.
- Not banked: positive off-curve split density, `S_4`, arithmetic/geometric
  monodromy equality, a `Theta(q_line)` counterpacket, corrected-reserve
  theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/SNARK statement, or
  prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-GEOMETRIC-S4`.

Cycle 35 A2_B geometric S4 / constant-field prompt:

- `prompts/20260618_cycle35_a2b_geometric_s4_checker_spec.md`
- Status: AUDIT / prompt prepared.
- Purpose: attack the remaining off-curve gate directly: prove geometric
  transitivity or full `S_4`, prove arithmetic/geometric equality, or produce
  an explicit symbolic checker/certificate for the discriminant, resolvent,
  and constant-field tests over `B(z_0,z_1)`.

Cycle 35 A2_B geometric S4 answer:

- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RAW.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RUN_RESULT.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE35_A2B_GEOMETRIC_S4_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE35_A2B_GEOMETRIC_S4_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: a finite-place monodromy certificate. In a fixed
  source-valid restricted `t=2,j=4` `A^2_B` instance, off-Delta squarefree
  factorization types `"4"` and `"13"` force `G_arith=S_4`; because `"13"` is
  even, the sign constant-field obstruction is also cut, so
  `G_geom=G_arith=S_4` for that tested instance.
- Experimental application: the Cycle 32 `p=29` histogram includes `"4"`,
  `"13"`, and `"1111"` and is compatible with the `S_4` cycle index.
- Not banked: a uniform source-valid counterpacket, a growing-prime
  `Theta(q_line)` theorem, corrected-reserve theorem, MCA/CA/list/
  line-decoding/curve-MCA/protocol/SNARK statement, or prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-UNIFORM-S4`.

Cycle 36 A2_B uniform S4 prompt:

- `prompts/20260618_cycle36_a2b_uniform_s4.md`
- Status: AUDIT / prompt prepared.
- Purpose: either upgrade the finite-place `S_4` certificate into a uniform
  source-valid growing-prime restricted counterpacket seed, or kill it by
  finding the exact obstruction.

Cycle 36 A2_B uniform S4 answer:

- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RAW.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RUN_RESULT.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE36_A2B_UNIFORM_S4_CREDIT_SURFACE_RUNNER_RESULT.json`
- `audits/20260618_CYCLE36_A2B_UNIFORM_S4_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: an explicit source-valid growing-prime denominator family
  for primes `p = 3 mod 4`,
  `B=F_p`, `F=F_{p^2}=B(alpha)`, `alpha^2=-1`,
  `E=X^2+alpha X+1`, `b=X`, plus a reduction of uniform geometric `S_4` to a
  finite single-prime certificate after good-reduction monotonicity.
- Correction: the raw criterion "resolvent irreducible plus nonsquare
  discriminant" must also include quartic transitivity/geometric
  irreducibility. A finite-place type `"4"` supplies this; types `"4"` and
  `"13"` are the preferred certificate.
- Not banked: a `COUNTERPACKET`, a uniform `Theta(q_line)` theorem,
  corrected-reserve theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/
  SNARK statement, or prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT`.

Cycle 37 single-prime S4 certificate prompt:

- `prompts/20260618_cycle37_single_prime_s4_cert.md`
- Status: AUDIT / prompt prepared.
- Purpose: produce a reproducible one-good-prime certificate for the explicit
  Cycle 36 family, with quartic transitivity, resolvent, discriminant, and
  source-validity gates separated.

Cycle 37 single-prime S4 certificate answer:

- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RAW.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RUN_RESULT.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle37_single_prime_s4_cert_unrun_model_checker.py`
- `local_checks/20260618_cycle37_single_prime_s4_cert_local_result.txt`
- `audits/20260618_CYCLE37_SINGLE_PRIME_S4_CERT_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and the visible-terminal scrape is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: Cycle 37 hand-checks the explicit family source-validity
  gates and the `kappa != 0` normalization, but does not produce a working
  single-prime `S_4` certificate.
- Local Codex follow-up: the inline checker crashes with a tuple/field-element
  type mismatch, so the checker is not bankable as written.
- Live wall remains `W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT`, but the next
  prompt is a broader homerun attempt.

Cycle 38 homerun prompt:

- `prompts/20260618_cycle38_homerun_full_solve_big_leap.md`
- Status: AUDIT / prompt prepared.
- Purpose: take a big-leap/full-solve swing after the Cycle 37 checker failure:
  repair or bypass the certificate route, find an obstruction, or identify a
  higher-value route toward the proximity problem.

Cycle 38 homerun answer:

- `raw/20260618_CYCLE38_HOMERUN_RECOVERED_CLAUDE_JSONL.md`
- `raw/20260618_CYCLE38_HOMERUN_RAW.json`
- `raw/20260618_CYCLE38_HOMERUN_RUN_RESULT.json`
- `raw/20260618_CYCLE38_HOMERUN_RESPONSE_MALFORMED_VISIBLE_TERMINAL.md`
- `raw/20260618_CYCLE38_HOMERUN_TUI_RUNNER_RESULT.json`
- `raw/20260618_CYCLE38_HOMERUN_CREDIT_SURFACE_RUNNER_RESULT.json`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_checker.py`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_result.txt`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_stdout.txt`
- `local_checks/20260618_cycle38_single_prime_s4_cert_patched_stderr.txt`
- `audits/20260618_CYCLE38_HOMERUN_S4_REPAIR_AUDIT.md`
- Harness status: `HARNESS_MALFORMED_VISIBLE_TERMINAL`; no clean
  `response.md` was produced. The readable structured-JSONL recovery was
  audited conservatively and terminal scrape text is not banked as
  mathematics.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: Cycle 38 finds the exact type error in the Cycle 37 checker:
  four free top coefficients were residue-pairs but `qres` consumes them as
  `F`-elements. The repaired checker uses
  `W_{n-1..n-4}=1,alpha,1+alpha,1`.
- Local Codex follow-up: the patched checker runs at `p=31` and reports
  `PASS_S4_finite_place=true`, with `"4"` and `"13"` factorization witnesses,
  nonsquare-discriminant evidence, and no singular points on the tested line.
- Not banked: a uniform growing-prime theorem, geometric `S_4` over
  `B(z_0,z_1)`, a `COUNTERPACKET`, corrected-reserve theorem, MCA/CA/list/
  line-decoding/curve-MCA/protocol/SNARK statement, or prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-S4-SYMBOLIC-GOODRED`.

Cycle 39 symbolic good-reduction prompt:

- `prompts/20260618_cycle39_symbolic_goodred_s4.md`
- Status: AUDIT / prompt prepared.
- Purpose: upgrade the repaired `p=31` finite-place `S_4` evidence to a
  symbolic/good-reduction lemma for the explicit family, or identify the exact
  obstruction that prevents globalization.

Cycle 39 symbolic good-reduction answer:

- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RESPONSE.md`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.json`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE39_SYMBOLIC_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle39_locator_collapse_verify.py`
- `local_checks/20260618_cycle39_locator_collapse_verify_result.json`
- `audits/20260618_CYCLE39_SYMBOLIC_GOODRED_AUDIT.md`
- Harness status: clean `artifact_stream`; `response.md` is the theorem
  answer and raw receipts are preserved separately.
- Mathematical audit status: `PROOF / BANKABLE_LEMMA / EXACT_NEW_WALL /
  AUDIT`.
- Banked content: the locator collapses in `A=F[X]/(E)`:
  `[X^p-X]_E=alpha` for `(-5/p)=+1` and `[X^p-X]_E=-2X` for `(-5/p)=-1`.
  Thus the explicit `t=2,j=4` surface family is fixed within two congruence
  subcases rather than changing freely with `p`.
- Local Codex follow-up: the finite sanity checker confirms the collapse on
  sample primes from both subcases with `all_ok=true`.
- Not banked: Subcase A monodromy, a good-reduction certificate, a uniform
  growing-prime theorem, a `COUNTERPACKET`, corrected-reserve theorem,
  MCA/CA/list/line-decoding/curve-MCA/protocol/SNARK statement, or prize
  solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-SUBCASE`.

Cycle 40 subcase good-reduction prompt:

- `prompts/20260618_cycle40_subcase_goodred_certificate.md`
- Status: AUDIT / prompt prepared.
- Purpose: prove or refute the subcase-separated good-reduction/S4 certificate
  below the Cycle 39 locator collapse, especially Subcase A (`ell=alpha`) and
  the explicit good-reduction bridge.

Cycle 40 subcase good-reduction answer:

- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RESPONSE.md`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.json`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE40_SUBCASE_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle40_subcase_goodred_checker_from_response.py`
- `local_checks/20260618_cycle40_subcase_goodred_checker_result.json`
- `audits/20260618_CYCLE40_SUBCASE_GOODRED_AUDIT.md`
- Harness status: clean enough `artifact_stream`; `response.md` is the theorem
  answer. The run has one nonfatal stream-json parse warning but no terminal or
  ad transcript is involved.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: the finite-place histogram criterion `"4"` plus `"13"`
  proves `G_arith=G_geom=S_4` at the tested prime. This upgrades the prior
  `p=31` Subcase B certificate to geometric `S_4`.
- Local Codex follow-up: the parametrized checker from the response was
  extracted and executed locally. It reports `all_pass=true`: Subcase A passes
  at `p=7,23,43,47`, and Subcase B passes at `p=11,19,31,59`.
- Not banked: a characteristic-zero determinant/discriminant computation, a
  certified good-reduction prime, tame-specialization globalization, a
  Chebotarev/Lang-Weil density theorem, a `COUNTERPACKET`,
  corrected-reserve theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/
  SNARK statement, or prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-S4-GOODRED-CHAR0DELTA`.

Cycle 41 homerun characteristic-zero Delta prompt:

- `prompts/20260618_cycle41_char0delta_goodred.md`
- Status: AUDIT / prompt prepared.
- Purpose: attack the missing characteristic-zero branch determinant,
  quartic discriminant, and good-reduction bridge per subcase.

Cycle 41 characteristic-zero Delta answer:

- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RECOVERED_FINAL_ASSISTANT.md`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RESPONSE_STREAM_MALFORMED.md`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.json`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RAW.jsonl`
- `raw/20260618_CYCLE41_CHAR0DELTA_GOODRED_RUN_RESULT.json`
- `local_checks/20260618_cycle41_char0delta_checker_from_response.py`
- `local_checks/20260618_cycle41_char0delta_checker_result.json`
- `local_checks/20260618_cycle41_char0delta_checker_patched.py`
- `local_checks/20260618_cycle41_char0delta_checker_patched_result.json`
- `local_checks/20260618_cycle41_char0delta_goodprime_scan_result.json`
- `audits/20260618_CYCLE41_CHAR0DELTA_GOODRED_AUDIT.md`
- Harness status: source-audited `artifact_stream` recovery. The dashboard
  `response.md` contains duplicated partial stream text, so it is preserved as
  malformed stream provenance only. The final coherent assistant message was
  recovered from `raw_response.jsonl` and audited conservatively.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL /
  EXPERIMENTAL / AUDIT`.
- Banked content: the tame good-reduction bridge is now an explicit
  `(G1,G2,G3)` gate for the fixed subcase line cover. After a minimal local
  checker repair, Subcase B passes good reduction at `p0=19,31,59`.
- Local Codex follow-up: the model's original checker fails with a type error;
  the patched checker represents `ell=i` as `(i,0)` and wraps flattened
  scalar equations as Gaussian scalars. The patched good-prime scan finds no
  Subcase A good prime among `p0=7,23,43,47,67,83`; all fail the separability
  and disjointness gates.
- Not banked: independent source derivation of the char-0 checker, Subcase A
  characteristic-zero `S_4`, a full surface good-reduction result, the
  explicit bad-prime set, Chebotarev/Lang-Weil density, a `COUNTERPACKET`,
  corrected-reserve theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/
  SNARK statement, or prize solve.
- Live wall: `W-F1-AA-RES-T2J4-A2B-S4-SUBCASEA-GOODRED-OBSTRUCTION`.

Cycle 42 external-model homerun handoff:

- `handoffs/20260618_cycle42_external_homerun/PROMPT.md`
- `handoffs/20260618_cycle42_external_homerun/MANIFEST.md`
- Status: AUDIT / handoff prepared.
- Purpose: send a different model a focused packet to independently audit the
  Cycle 41 characteristic-zero checker, resolve the Subcase A obstruction, and
  push the Subcase B global-density route if the checker survives source audit.

Cycle 42 external 5.5 Pro answers:

- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_A.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_B.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_C.md`
- `raw/cycle42_external_5p5_pro/20260618_CYCLE42_5P5PRO_ANSWER_D.md`
- `raw/cycle42_external_5p5_pro/cycle42_goodred_density_checker.py`
- `raw/cycle42_external_5p5_pro/cycle42_goodred_density_certificate.json`
- `raw/cycle42_external_5p5_pro/cycle42_exact_resultants.json`
- `raw/cycle42_external_5p5_pro/cycle42_bad_prime_sets.json`
- `raw/cycle42_external_5p5_pro/cycle42_corrected_char0_goodred_checker_result.json`
- `raw/cycle42_external_5p5_pro/cycle42_corrected_char0_density_certificate.md`
- `raw/cycle42_external_5p5_pro/cycle42_t2j4_goodred_checker.py`
- `raw/cycle42_external_5p5_pro/cycle42_t2j4_goodred_checker_result.json`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_goodred_density_checker_external.py`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_external.py`
- `local_checks/cycle42_external_5p5_pro/20260618_cycle42_t2j4_goodred_checker_localrun.py`
- `audits/20260618_CYCLE42_EXTERNAL_5P5PRO_GOODRED_DENSITY_AUDIT.md`
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT /
  EXACT_NEW_WALL / AUDIT / EXPERIMENTAL`.
- Consensus result: the Cycle 41 A-side `G2/G3` failure is a false negative
  from using raw affine/Cramer branch data as if it were intrinsic. The
  corrected primitive/projective or horizontal-line certificates give Subcase
  A good reduction at `p=7`; Subcase B has good reduction at `p=19` or `p=31`.
- Banked content: cut the route "A fails raw G2/G3, therefore A cannot
  globalize"; record the fixed `t=2,j=4` branch as externally certified up to
  split-slope density
  `N_split(p)=p^2/24+O(p^(3/2))=q_line/24+O(q_line^(3/4))`, pending local
  SymPy/Sage rerun or PRZ review.
- Local Codex follow-up: the Python checkers were inspected and syntax-checked,
  but local execution is blocked because `sympy` is not installed in either
  system Python or the bundled Codex Python. No dependency was fetched.
- Not banked: corrected-reserve counterpacket, fixed-rate counterpacket,
  generated-field theorem, smooth multiplicative-domain theorem, CA/list/
  line-decoding/curve-MCA/protocol/SNARK statement, or Proximity Prize solve.
- Live wall: `W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT`.

Cycle 43 reserve-lift homerun:

- `prompts/20260618_cycle43_reserve_lift_homerun.md`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RESPONSE.md`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RAW.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RAW.jsonl`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RUN_RESULT.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RUN_STATUS.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_PROMPT_SENT.md`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_INPUT_MANIFEST.json`
- `audits/20260618_CYCLE43_RESERVE_LIFT_HOMERUN_AUDIT.md`
- Harness status: clean non-ad `artifact_stream`; `OK_WITH_NONFATAL_STREAM_WARNING`
  from one malformed stream-json line; `response.md` is usable theorem
  content. No `output_files/` deliverables were written by the model.
- Mathematical audit status: `BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL /
  AUDIT / EXPERIMENTAL`.
- Banked content: the literal fixed `t=2,j=4` quartic/S4 mechanism does not
  reserve-scale. Reserve scale has `j=Theta(n) >> 2t=Theta(n/log n)`, so the
  square Cramer/quartic monodromy object disappears; diagonal scaling
  `j=2t -> infinity` has totally split density at most `1/j -> 0`.
- Route-organizing lemma: realized slopes are controlled by cosupport landing
  counts, with heuristic skeleton
  `N_split ~ min(q_line, C(p,j)/p^{2(t-1)})`, matching the banked `j=2`,
  `j=3`, and `j=4` fixed regimes. This is not banked as a proved reserve
  asymptotic because equidistribution/anticollision is still open.
- New live wall:
  `W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`.
- Not banked: positive-density reserve lift, corrected-reserve
  counterpacket, generated-field theorem, MCA/CA/list/line-decoding/
  curve-MCA/protocol/SNARK statement, or prize solve.

Cycle 44 cosupport subset-product homerun:

- `prompts/20260619_cycle44_cosupport_subset_product_homerun.md`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_RESPONSE.md`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_RAW.json`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_RAW.jsonl`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_RUN_RESULT.json`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_RUN_STATUS.json`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_PROMPT_SENT.md`
- `raw/cycle44_cosupport_subset_product_homerun/20260619_CYCLE44_COSUPPORT_INPUT_MANIFEST.json`
- `audits/20260619_CYCLE44_COSUPPORT_MOMENT_IDENTITY_AUDIT.md`
- Status: clean non-ad `artifact_stream`; `response.md` is usable theorem
  content. No `output_files/` deliverables were written by the model.
- Run directory:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-19T00-05-26-501Z-cycle44-cosupport-subset-product-homerun-11471e45`.
- Target: `W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`.
- Mathematical audit status: `BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT /
  EXPERIMENTAL`.
- Banked content: exact cosupport moment identity for
  `rho(T)=[I_{D\T}]_E` in the restricted `D=F_p` branch,
  `rho(T)=-ell Lambda(T)^(-1)N(T)`, where both `N(T)` and `Lambda(T)` are
  affine-linear in the elementary symmetric functions `e_m(T)`. Cycle 44 also
  gives an exact additive-character landing formula whose main term is
  `binom(p,j)/p^(2(t-1))`.
- New live wall:
  `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION`; preferred subwall:
  `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION`.
- Not banked: first-moment cancellation, the L2 anticollision estimate,
  positive-density reserve lift, corrected-reserve counterpacket,
  generated-field theorem, MCA/CA/list/line-decoding/curve-MCA/protocol/SNARK
  statement, or prize solve.

Cycle 45 external L2 anticollision packet:

- `handoffs/20260619_cycle45_l2_anticollision_external/README.md`
- `handoffs/20260619_cycle45_l2_anticollision_external/PROMPT_COMMON.md`
- `handoffs/20260619_cycle45_l2_anticollision_external/ROLE_PROMPTS.md`
- `handoffs/20260619_cycle45_l2_anticollision_external/MANIFEST.md`
- Status: EXTERNAL_MODEL_PACKET / AUDIT.
- Target:
  `W-F1-AA-RES-SYMMETRIC-FUNCTION-CANCELLATION-L2-ANTICOLLISION`.
- Purpose: give six fresh external 5.5 Pro-style instances the same banked
  Cycle 44 identity and ledgers, but different roles: proof-builder,
  falsifier hunter, source auditor, finite checker designer, homerun attempt,
  and obstruction reducer.

Cycle 45 external random-anchor L2 audit:

- `raw/cycle45_external_random_anchor_l2/20260619_CYCLE45_RANDOM_ANCHOR_L2_CERTIFICATE.md`
- `raw/cycle45_external_random_anchor_l2/cycle45_random_anchor_reserve_lift_certificate.md`
- `raw/cycle45_external_random_anchor_l2/20260619_cycle45_moment_formula_checker.py`
- `raw/cycle45_external_random_anchor_l2/20260619_cycle45_moment_formula_checker_sample.txt`
- `audits/20260619_CYCLE45_EXTERNAL_RANDOM_ANCHOR_L2_AUDIT.md`
- Status: `PROOF / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT /
  EXPERIMENTAL`.
- Banked content: the literal uniform-in-anchor L2 wall is false, but the
  existential random-anchor L2 reserve lift is proved in the restricted
  additive `D=F_p`, `F=F_{p^2}`, `q_line=p^2` residue-line branch.
- Key lemma:
  `rank_F(w -> (R_T(w),R_T'(w))) = t + min(t, |T\T'|)`. This gives exact
  independence once cosupports differ in at least `t` exchanged points and
  yields `M_2 <= (1+o(1)) #Land^2/q_line` whenever
  `binom(p,j)/p^(2t) -> infinity`.
- Reserve consequence: for `t=(C+o(1))p/log_2 p`, `k/p -> rho`, and
  `C < H_2(rho)/2`, a source-valid deterministic anchor exists with
  `(1-o(1))p^2` slopes, and the strict interior gives all `p^2` slopes for
  sufficiently large `p`.
- Not banked: generated-field theorem, smooth multiplicative-domain theorem,
  corrected-reserve sufficiency theorem, protocol/SNARK statement, or
  Proximity Prize solve.
- New full-problem wall:
  `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING`.

Cycle 45 deep literature audit:

- `raw/cycle45_deep_lit_audit/20260619_CYCLE45_DEEP_LIT_AUDIT_RAW.txt`
- `audits/20260619_CYCLE45_DEEP_LIT_AUDIT.md`
- Status: `AUDIT / ROUTE_CUT / EXACT_NEW_WALL`.
- Lit-audit verdict: the exact Cycle 45 exchange-distance pair-rank theorem
  was not identified as a stated theorem in the surveyed literature, though
  proximity-gap, folded-RS, subspace-polynomial, and interleaved-RS rank
  methods are nearby prior art.
- Route cut: Cycle 45 is not promoted to a full grand MCA solve because
  `D=F_p subset F_{p^2}` may not be an admissible "smooth evaluation domain"
  in the intended multiplicative/protocol sense.
- Correction: the lit AI confused `C^{equiv m}` with Reed-Muller or
  multiplicity-code notation in one passage. Locally, `C^{equiv m}` is the
  `m`-interleaved Reed-Solomon code with column distance.
- New walls:
  `W-F1-AA-RES-SMOOTH-DOMAIN-ADMISSIBILITY`,
  `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING`, and
  `W-F1-LIST-INTERLEAVED-BRIDGE`.

Cycle 46 targeted wallbreaker 5.5 Pro audit:

- `raw/cycle46_targeted_wallbreaker_5p5/`
- `audits/20260619_CYCLE46_TARGETED_WALLBREAKER_AUDIT.md`
- Status: `PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL /
  AUDIT`.
- New major claim: the Cycle45 pair-rank lemma is domain-free. For arbitrary
  `D subset F_Q`, the exact same image/rank proof gives
  `rank_F(R_T,R_T') = t + min(t, |T\T'|)`.
- New scalar-MCA route: replace the constant near-shell bound by the
  domain-uniform Bessel/shell factor
  `J <= exp(2 sqrt(aj/Q)) <= exp(n/sqrt(Q))`. This is subexponential when
  `Q >= n`, so smooth prime-field multiplicative subgroups with
  `log q=o(n)` should give `emca=1` in the strict range `c < H_2(rho)`.
- Route cut: `W-F1-AA-RES-FROBENIUS-COMPRESSED-LANDING` is no longer the
  preferred scalar-MCA wall unless the official challenge disallows the
  prime-field smooth-subgroup route or forces the quadratic extension ledger.
- New preferred scalar walls:
  `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT` and
  `W-F1-AA-SMOOTH-PRIME-SUBGROUP-MCA-COUNTERPACKET`.
- List-side update: a direct `m`-anchor zero-residue construction gives a
  column-distance interleaved list lower bound with exponent
  `H_2(rho)-m c`, but this may be ordinary volume behavior rather than a full
  grand list-decoding threshold.

Cycle 46 instance-3 Frobenius-compression supplement:

- `raw/cycle46_instance3_frobenius_supplement/`
- `audits/20260619_CYCLE46_INSTANCE3_FROBENIUS_COMPRESSED_AUDIT.md`
- Status: `PROOF_CANDIDATE / BANKABLE_LEMMA / ROUTE_CUT / AUDIT`.
- The extra instance-4 file is another Cycle45 balanced/random-anchor
  restricted additive certificate, consistent with the banked theorem.
- New instance-3 claim: take `E=H(X)(X-theta)`, `B_num=H(X)`,
  `theta in F_{p^2}\F_p`, and `H in F_p[X]` of degree `t-1`. The
  Frobenius envelope `J=lcm(E,E^(p))=H m_theta` has degree `t+1`, so
  the base-polynomial residue image `U` has `F_p`-dimension `t+1`,
  contains `F_{p^2}b`, and contains every cosupport residue for
  `F_p`-valued anchors.
- Entropy consequence: with `Lambda=binom(p,j)/p^(t+1)` and shell loss
  `exp(O(sqrt p))`, the additive branch reaches the full strict range
  `C < H_2(rho)` if the nonminimal denominator datum is accepted.
- Caveat: `gcd(E,B_num)=H`, so the rational direction reduces to
  `-1/(X-theta)`. This is literally allowed by the local residue-datum
  definition, but it may be considered a nonminimal-denominator artifact by a
  reviewer. It is not promoted to a final prize claim.

Cycle 47 domain-uniform Bessel moment audit:

- `raw/cycle47_domain_uniform_bessel_5p5/`
- `audits/20260619_CYCLE47_DOMAIN_UNIFORM_BESSEL_AUDIT.md`
- Status: `PROOF_CANDIDATE / BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT`.
- Major claim: the domain-uniform Bessel wall
  `W-F1-AA-RES-DOMAIN-UNIFORM-BESSEL-MOMENT` is closed at the
  algebraic/source-local lower-branch level. The exact pair-rank lemma is
  domain-free, and the near-shell factor is
  `J <= I_0(2 sqrt(aj/Q)) <= exp(2 sqrt(aj/Q))`.
- Smooth-domain consequence: for a smooth multiplicative domain `L subset F^*`,
  take `E=X^t`, `B_num=1`, `f=w/E`, and `g=-1/E`. There exists an anchor with
  at least a `1-J/lambda` fraction of bad slopes, and all slopes are bad if
  `lambda=binom(n,k+t)/Q^t > QJ`.
- Entropy consequence: when `k/n -> rho`, `t=(c+o(1))n/log_2 Q`, and
  `log_2 Q=o(n)`, the source-local lower/failure branch gives
  `epsilon_mca=1` throughout the strict range `c < H_2(rho)`.
- Not solved: the matching safe-side upper theorem above entropy, literal
  survey Definition 4.3 alignment, and the grand list-decoding threshold.
- New main wall:
  `W-MCA-AA-RES-ENTROPY-BOUNDARY-MATCHING-UPPER`, equivalently a uniform
  high-cloud inverse theorem for balanced arbitrary-anchor residue clouds after
  quotient-pullback and tangent/contained templates are separated.
