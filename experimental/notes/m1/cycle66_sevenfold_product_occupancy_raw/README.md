# Cycle 66 Sevenfold Product Occupancy Raw Artifacts

This directory preserves the raw Packy/Fable `artifact_stream` return for
Cycle 66:

```text
run id:
2026-06-20T06-39-36-450Z-cycle66-sevenfold-product-occupancy-verifier-d160e13f
target:
V-CYCLE65-SEVENFOLD-PRODUCT-OCCUPANCY-VERIFIER
```

Preserved files:

- `response.md`
- `raw_response.jsonl`
- `raw_response.json`
- `run_result.json`
- `input_manifest.json`
- `prompt_sent.md`
- `FILE_INDEX_FOR_MODEL.md`
- `selfcheck_certificate.json`
- `SHA256SUMS.txt`

The run completed as `OK_WITH_NONFATAL_STREAM_WARNING`; the warning was one
malformed stream-json line, but `response.md` and `raw_response.*` were written.
No output files were produced by the worker.

Codex added `selfcheck_certificate.json` by running
`experimental/scripts/cycle66_occupancy_selfcheck.py`, a bounded local
verification of the finite-field setup and Cycle 65 factorization identities.
