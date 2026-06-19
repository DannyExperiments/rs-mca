# Cycle 58 Nine-Lane Homerun Handoff

Status: EXPERIMENTAL / AUDIT.

This handoff packet is designed for nine fresh 5.5 Pro theorem-worker instances.
Upload the zip once per instance, paste `COMMON_CONTEXT.md` first, then paste one
role prompt from `prompts/`.

Do not ask every worker to "solve the whole prize" without a lane. The current
state is lower/failure-side progress plus an open upper-side inverse theorem.
The lanes below are meant to produce either a proof, a counterpacket, a route
cut, or the next exact wall.

## Files

- `COMMON_CONTEXT.md` - shared context for every worker.
- `context/` - selected Cycle 49-57 review index, audits, and staged prompt.
- `prompts/01_global_syndrome_inverse.md`
- `prompts/02_locator_scroll_circuit_inverse.md`
- `prompts/03_t2_high_j_quadric_split_count.md`
- `prompts/04_quotient_component_counterpacket_hunter.md`
- `prompts/05_all_denominator_mca_auditor.md`
- `prompts/06_overbalanced_thick_residue_compression.md`
- `prompts/07_scalar_list_local_limit.md`
- `prompts/08_finite_prize_threshold_auditor.md`
- `prompts/09_referee_formalizer_overclaim_hunter.md`
- `MANIFEST.md`

## Recommended Assignment

Use all nine distinct lanes if coverage matters. If using duplicates, duplicate
lanes 1, 2, and 3 first.

Recommended upload flow:

1. Upload the zip to each fresh instance.
2. Paste `COMMON_CONTEXT.md`.
3. Paste exactly one file from `prompts/`.
4. Ask the worker to read `context/PRZ_REVIEW_INDEX.md` and the relevant
   cycle audit files before answering.

## Conservative Status Rule

Every response must end with exactly one of:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

The worker may use repository labels too:

```text
PROVED / CONDITIONAL / CONJECTURAL / EXPERIMENTAL / AUDIT / COUNTEREXAMPLE
```

Do not promote a route sketch to a theorem.
