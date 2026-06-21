# ROLE 07: Public Replay Trusted Registry

Your job is to turn the Cycle84 public replay into a clean trusted-registry
entry.

Do not re-solve the math. Audit reproducibility and certificate status.

Use:

```text
cycle84_github_replay_receipt.md
m1_cycle84_wallbreaker_returns_audit.md
cycle84_wallbreaker_returns_raw/SHA256SUMS.txt
.github/workflows/cycle84-certificate-replay.yml
```

Required:

1. State the exact trusted theorem/certificate ID(s):

```text
L-CYCLE84-EXACT-COLOR-FILTERED-MMAX
V-CYCLE84-GITHUB-PUBLIC-REPLAY
```

or better names.
2. List source artifacts, hashes, runner receipt, and exact outputs.
3. Define what the replay proves and what it does not prove.
4. Produce a registry entry suitable for `RS-PRIZE-FRONTIER-V1`.
5. Identify any reproducibility gap that remains, such as no independent
   implementation, compiler dependence, generated certificate trust, or
   missing artifact hash.

Return `BANKABLE_LEMMA` or `AUDIT`. Be conservative.
