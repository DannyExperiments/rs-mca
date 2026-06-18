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
