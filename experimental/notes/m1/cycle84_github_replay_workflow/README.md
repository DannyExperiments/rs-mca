# Cycle84 GitHub Replay Workflow Template

Status: AUDIT / VERIFICATION.

This folder preserves a manual-dispatch GitHub Actions workflow for replaying
the Cycle84 finite certificate:

```text
cycle84-certificate-replay.yml
```

Codex attempted to publish this file directly under `.github/workflows/`, but
GitHub rejected the push because the available OAuth token lacks the `workflow`
scope:

```text
refusing to allow an OAuth App to create or update workflow
`.github/workflows/cycle84-certificate-replay.yml` without `workflow` scope
```

The workflow is therefore kept here for an authorized maintainer or token to
copy into:

```text
.github/workflows/cycle84-certificate-replay.yml
```

## Jobs

The `light-certificate` job:

- verifies `SHA256SUMS.txt` for the banked Cycle84 raw artifacts;
- unpacks `cycle84_mmax2_certificate_bundle.zip`;
- reruns `verify_certificate.py`;
- requires `CYCLE84_EXACT_MMAX2_CERTIFICATE_VERIFIED`,
  `exact_true_m_max = 2`, and
  `exact_true_occupancy = 52747567092`.

The optional `full-replay` job:

- recompiles `src/tau_fold_full_optimized.cpp`;
- reruns the 16,384-shard projected census;
- verifies projected max multiplicity `2`, folded energy `60`, and projected
  energy `120`;
- recompiles and reruns `src/tau_duplicate_lift.cpp`;
- verifies `true_collision_tau_orbits = 6`,
  `true_double_fibers = 12`,
  `exact_true_ordered_offdiagonal_energy = 24`,
  `exact_true_m_max = 2`, and
  `exact_true_occupancy = 52747567092`.

## Dispatch

After installing the workflow with a credential that has `workflow` scope:

```bash
gh workflow run cycle84-certificate-replay.yml \
  --repo DannyExperiments/rs-mca-prz-fork \
  --ref cycle58-5p5-audit \
  -f run_full_replay=true
```

If GitHub runner limits block the full replay, dispatch with
`run_full_replay=false` to obtain the light public receipt, then run the heavy
projected census on a larger VM.
