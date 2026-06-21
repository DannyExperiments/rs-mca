# ROLE 03: Frontier Ledger Builder

Your job is to build the exact finite-frontier ledger entry implied by
Cycle84, if any.

Use the `RS-PRIZE-FRONTIER-V1` specification. Do not use heuristics.

Required output:

1. Identify the objective: MCA, scalar list, or a model-level thickened-color
   occupancy diagnostic.
2. Identify all fields:

```text
q_gen
q_line
q_code
q_chal
```

3. Identify the reserve, radius, `n`, `k`, `sigma`, `j`, and support size for
   the Role05/Cycle84 stratum.
4. Determine the exact native target:

```text
T_line = floor(q_line / 2^128)
```

or explain why the `2^32` comparison is only a research benchmark.
5. Produce a JSON-like certified lower-term entry, with theorem IDs and
   dependency IDs.
6. Decide whether the ledger row is `FAIL`, `UNKNOWN`, or only
   `RESEARCH_MODEL_FAIL`.

If the certificate is not official-prize-relevant, state the exact missing
normalization or scaling needed to make it relevant.
