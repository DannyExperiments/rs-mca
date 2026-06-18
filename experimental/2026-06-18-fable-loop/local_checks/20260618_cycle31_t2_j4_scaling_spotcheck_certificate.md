# Cycle 31 T2J4 Scaling Spot-Check Certificate

Status: EXPERIMENTAL.

Purpose:

- Audit Cycle 31's reinterpretation of the Cycle 30 scanner.
- Distinguish, weakly and experimentally, between an `O(p)` split-collapse
  reading and a positive-density `Theta(p^2)` reading.

Command shape:

```bash
python3 - <<'PY'
import importlib.util
from pathlib import Path
scan_path = Path('experimental/2026-06-18-fable-loop/local_checks/20260618_cycle30_t2_j4_split_quartic_scan.py')
spec = importlib.util.spec_from_file_location('scan', scan_path)
scan = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scan)
# run scan.run_trial(p, nonresidue, seed) for p=31,37,...
PY
```

Observed output before the bounded check was stopped:

```text
cycle31_local_scaling_spotcheck: EXPERIMENTAL
p=31 nr=3 seed=1000 C2=27 C2/p=0.871 C2/p2=0.0281 p2/24=40.04 landings=27/31465 off_R0=True
p=31 nr=3 seed=1001 C2=29 C2/p=0.935 C2/p2=0.0302 p2/24=40.04 landings=30/31465 off_R0=True
summary p=31 trials=2 avg=28.00 avg/p=0.903 avg/p2=0.0291 p2/24=40.04 elapsed=31.5s
p=37 nr=2 seed=1000 C2=39 C2/p=1.054 C2/p2=0.0285 p2/24=57.04 landings=39/66045 off_R0=True
```

Interpretation:

- This is not proof of either asymptotic.
- The data do not justify Cycle 31's strong claim that `1/24` density is
  already visible.
- The data also make the earlier phrase "leans O(p)" too strong. The observed
  `C2/p` is still increasing slowly, while `C2/p^2` is not collapsing fast
  enough at these sizes to settle the matter.
- The next meaningful object is not another small random scan but the exact
  quartic monodromy / discriminant / resolvent invariant.

Rejected overclaims:

- Not a proof of `O(p)`.
- Not a `Theta(q_line)` counterpacket.
- Not a monodromy computation.

