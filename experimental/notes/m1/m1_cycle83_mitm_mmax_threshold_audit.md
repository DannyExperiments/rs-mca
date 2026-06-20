# Cycle 83 MITM Mmax Threshold Audit

## Verdict

```text
EXACT_NEW_WALL / PLAN
```

Confidence: high that this is not a proof or counterpacket. The worker had a
read-only environment and explicitly marked the returned census code as
`UNRUN`.

The full raw artifacts are preserved in:

```text
experimental/notes/m1/cycle83_mitm_mmax_threshold_raw/
```

The original run completed with:

```text
OK_WITH_NONFATAL_STREAM_WARNING
captureWarning = Claude CLI stream-json parse warning: 1 malformed line(s)
```

but a clean `response.md` and raw JSON/JSONL artifacts were present.

## What Cycle 83 Actually Adds

Cycle 83 sharpens the remaining finite target:

```text
V-CYCLE83-MITM-MMAX-THRESHOLD-CERTIFICATE
W-CYCLE83-COLOR-FILTERED-MITM-MMAX-CENSUS
```

It emphasizes that the Cycle 82 minimum-distance-5 guardrail cannot by itself
prove:

```text
m_max(beta) <= 12.
```

Singleton-type reasoning would only give a huge bound, so the live wall is the
exact color-filtered maximum-fiber computation.

## Useful Reduction

Use the banked L/R split:

```text
L_img = products on slots {1,2,3}, |L_img| = 48^3 = 110592.
R_img = products on slots {4,5,6,7}, |R_img| = 48^4 = 5308416.
```

with the color-filtered incidence formula:

```text
m(v)=#{ l in L_img :
        v l^{-1} in R_img
        colorL(l)+colorR(v l^{-1}) = 4 mod 16 }.
```

The target is a threshold census capped at `13`:

```text
count[v] += 1;
abort and output a packet if count[v] reaches 13.
```

No full histogram is required.

## Resource Accounting From Cycle 83

Cycle 83 estimates:

```text
|P_0| = 52,747,567,104 compatible products.
|F| = 17^16 approximately 4.866e19.
expected accidental colliding pairs about 28.5.
```

The worker argues that duplicates should be rare and structured, so a
duplicate detector is preferable to storing the full product histogram.

It proposes three execution layers:

1. Bloom-filter duplicate detector plus exact recount. Approximate memory:
   about `66GB`; exactness relies on Bloom no-false-negative candidate capture
   plus a second exact pass.
2. Deterministic shard/reduce. Approximate disk: `0.5-0.85TB` scratch for
   exact 16-byte keys or hashes plus exact verification.
3. Recompute shards with low disk. Approximate cost: many passes, around one
   to several days.

Given the current local disk state, none of these were run by Codex in this
heartbeat.

## Local Storage Note

During banking, the Mac was effectively out of disk:

```text
/System/Volumes/Data: about 118MiB free, 100% capacity.
```

Codex removed six no-token RS-MCA `*-preview-*` Packy staging directories from
the same project lane to unblock raw preservation and compact audit writes.
Paid/completed run artifacts were not deleted.

The disk remains tight and is far below the scratch requirement for the
deterministic MITM census.

## Next Exact Wall

```text
W-CYCLE84-MITM-DUPLICATE-DETECTOR-EXECUTION
```

Before another large local census attempt, choose the execution surface:

```text
local cleanup enough for another Packy source snapshot;
or external/server run with >=66GB RAM for Bloom detector;
or external/server run with >=1TB scratch for deterministic shard reduce.
```

The next mathematical result is still:

```text
PROOF / BANKABLE_LEMMA: m_max(beta)<=12 threshold certificate;
COUNTERPACKET: explicit 13-fold colored packet.
```

Cycle 83 does not bank either one.

