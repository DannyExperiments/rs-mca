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
