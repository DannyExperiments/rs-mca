# Cycle 43 Reserve-Lift Homerun Audit

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT / EXPERIMENTAL.

Run:

- Packy run directory:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T23-35-34-020Z-cycle43-reserve-lift-homerun-a410a6ef`
- Lane: clean non-ad `artifact_stream`.
- Model/profile: `claude-opus-4-8`, `max`, `fable_full_experiment`.
- Harness status: `OK_WITH_NONFATAL_STREAM_WARNING`.
- Nonfatal warning: `Claude CLI stream-json parse warning: 1 malformed line(s)`.
- Output files: none; the model stated it could not write output files and
  included the requested deliverables inline in `response.md`.

## Preserved Artifacts

Raw/run receipts:

- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RESPONSE.md`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RAW.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RAW.jsonl`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RUN_RESULT.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_RUN_STATUS.json`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_PROMPT_SENT.md`
- `raw/cycle43_reserve_lift_homerun/20260618_CYCLE43_RESERVE_LIFT_INPUT_MANIFEST.json`

The clean theorem content is `response.md`, preserved as
`20260618_CYCLE43_RESERVE_LIFT_RESPONSE.md`. The large JSONL has a parse
warning, but `run_result.json` records `captureWarningFatal=false`, and
`response.md` is clean theorem content.

## Input-Snapshot Caveat

The model reported that the referenced Cycle 41 and Cycle 42 audit files were
not present in the mounted source snapshot. It nevertheless read the updated
Packy project route-board files, which already contained the Cycle 42
restricted closure and false-route cut. Therefore this audit banks only claims
that can be justified from:

- the clean Cycle 43 response;
- the updated project route-board summaries in the run snapshot;
- already banked local audit state in this repository.

Do not treat Cycle 43 as an independent audit of the full Cycle 42 returned
checker package. Cycle 42 remains the source for the fixed restricted branch
closure.

## Ledger

Cycle 43 keeps the restricted ledgers separate:

- `q_gen = p`;
- `B = F_p`;
- `F = F_{p^2}`;
- `q_line = p^2`;
- `q_chal` unused;
- `D = F_p`;
- denominator degree / reserve parameter `t = sigma`;
- cosupport size `j = n-a`.

The prior fixed branch remains:

```text
t = sigma = 2,
j = 4,
N_split(p) = p^2/24 + O(p^(3/2))
           = q_line/24 + O(q_line^(3/4)).
```

This is not a corrected-reserve, fixed-rate, generated-field, MCA/list,
line-decoding, curve-MCA, protocol, SNARK, prize, or final `COUNTERPACKET`
statement.

## Main Cycle 43 Claims

### 1. Counting Skeleton

Cycle 43 proposes the organizing count:

```text
N_split <= #Land(j,t),

#Land(j,t) heuristically ~ C(p,j) / p^{2(t-1)}
                         = C(p,j) / q_line^{t-1},

N_split heuristically ~ min(q_line, C(p,j)/p^{2(t-1)}).
```

The rigorous part is the upper bound: every realized slope needs at least one
landing cosupport. The equidistribution main term is not proved in Cycle 43.
It is bankable only as a route-organizing heuristic/reduction because it
matches the previously banked fixed regimes:

```text
j=2, t=2: C(p,2)/p^2 = O(1);
j=3, t=2: C(p,3)/p^2 = O(p);
j=4, t=2: C(p,4)/p^2 = p^2/24 + lower terms.
```

Audit status: BANKABLE_LEMMA as a counting reduction / heuristic skeleton,
not as a proved asymptotic theorem.

### 2. Quartic/S4 Mechanism Does Not Literally Reserve-Scale

Cycle 43 argues that the fixed `t=2,j=4` mechanism lives at the square point

```text
j = 2t.
```

In the reserve-scale regime one expects

```text
t = sigma >= C n/log n,
j = Theta(n),
```

so

```text
j >> 2t.
```

Thus the square Cramer system and the single quartic monodromy problem are no
longer the right objects in the reserve-scale regime. A separate diagonal
scaling attempt with `j=2t -> infinity` also cannot preserve a fixed positive
split density through the same monodromy idea: for a transitive group of
degree `j`, the totally split Frobenius density is `1/|G| <= 1/j -> 0`.

Audit status: ROUTE_CUT for the literal route

```text
amplify the fixed t=2,j=4 quartic/S4 mechanism directly to reserve scale.
```

This does not cut the reserve-scale route itself. It redirects the live route
away from quartic monodromy and toward underdetermined cosupport
equidistribution.

### 3. New Exact Wall

Cycle 43 names the new wall:

```text
W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION
```

The wall is to prove or refute reserve-scale equidistribution / anticollision
for the cosupport-residue map

```text
rho(T) = [I_{D\T}]_E,
Land = {T : rho(T) in F*b},
Slopes = {z in F : exists T, rho(T)=z b}.
```

Cycle 43 identifies a concrete analytic handle: for nontrivial multiplicative
characters `chi` of `A^*=(F[X]/E)^*`, the subset-product moments are elementary
symmetric sums

```text
e_j({chi(xi-d)}_{d in F_p}),   xi=[X]_E.
```

Positive-density reserve lift now depends on cancellation / decoupling /
anticollision for these structured subset-product and quotient-residue laws,
plus explicit separated growing-degree denominators.

Audit status: EXACT_NEW_WALL / BANKABLE_LEMMA as a sharper reduction target.

## Critical Caveats

The following are not banked:

- a positive-density reserve lift;
- a corrected-reserve counterpacket;
- a generated-field theorem;
- a full MCA/list/line-decoding/curve-MCA/protocol/SNARK/prize result;
- a proof of the equidistribution statement;
- a proof that the threshold `sigma ~ H_2(delta)n/(2 log n)` is sufficient;
- any local checker evidence for the underdetermined regime.

The entropy/codimension threshold is useful and probably important, but Cycle
43 proves neither the needed cancellation nor slope anticollision.

## Banked / Cut / Next Wall

Bank:

```text
BANKABLE_LEMMA:
The reserve-scale question is governed by cosupport-residue landing counts.
The heuristic skeleton min(q_line, C(p,j)/p^{2(t-1)}) unifies the banked
j=2, j=3, and j=4 fixed regimes, but remains conditional on
equidistribution/anticollision for reserve scale.
```

Cut:

```text
ROUTE_CUT:
The literal fixed t=2,j=4 quartic/S4 monodromy mechanism does not scale to
reserve. Reserve scale is underdetermined (j >> 2t), and diagonal balanced
scaling j=2t has totally split density <= 1/j -> 0.
```

New wall:

```text
W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION
```

Subtargets:

1. Prove cancellation in `e_j({chi(xi-d)}_{d in F_p})` for nontrivial
   characters in the reserve window.
2. Prove quotient decoupling for `[I_{D\T}]_E`, not merely product
   equidistribution for `[L_T]_E`.
3. Bound landing multiplicities
   `max_z #{T in Land : rho(T)=z b}`.
4. Exhibit explicit separated aperiodic denominator families
   `deg E = sigma = Theta(n/log n)` with no roots on `D=F_p`.

## Recommended Next Action

Do not launch Cycle 44 until Danny has seen the significance of Cycle 43. If
continuing, the next best prompt is a targeted checker/spec attack on
`W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION`, especially the finite
experiment suggested by Cycle 43:

```text
fix t=2 and sweep j upward (j=4,5,6,...) at p=23,31,43;
measure |Slopes|/p^2, #Land, and max landing multiplicity.
```

If the ratio climbs toward a positive constant, the underdetermined route is
live. If it stalls, hunt the collapse mechanism as a `ROUTE_CUT`.
