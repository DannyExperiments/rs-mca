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
