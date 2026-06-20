# Cycle 61 Master Referee Audit

**Date:** 2026-06-20
**Status:** AUDIT / PLAN / CONDITIONAL
**Raw input:** `experimental/notes/m1/cycle61_master_referee_raw/01_master_referee_plan.md`

## Executive Verdict

The Master Referee answer is significant as a **route-selection result**, not
as theorem progress. It does what the prompt asked: it chooses a primary route,
demotes distractions, gives stop conditions, and turns the next round into
falsifiable work.

I accept its main direction with one caveat:

- **Accepted primary:** scalar-list apolar complete-intersection route.
- **Accepted backup:** `t=1` MCA generalized-Jacobian support-plus-color route.
- **Accepted demotion:** Lattes/split-rational registry work becomes parallel
  verification, not the main route.
- **Caveat:** the finite checker should run alongside the first theorem round,
  because it decides which packets and constants are actually prize-relevant.

This is still a route-repair / kill-test phase. It is not a near-final solve
phase.

## What Changed

Before the Master Referee answer, the planning synthesis had several plausible
next priorities:

```text
A. Lattes / split-rational verification
B. support-theoretic split-rational overlap cover
C. primitive t=1 apolar / generalized-Jacobian base case
D. scalar list apolar/circuit theorem
E. finite checker and threshold ledger
```

The referee makes a clear call:

```text
Primary: D, but as an apolar complete-intersection / generalized-Jacobian
route, not as a circuit-transversal route.

Backup: C, the t=1 MCA generalized-Jacobian route, with external colors.
Parallel support: A and E.
Restricted kill test only: B.
```

That is useful because it cuts the expanding MCA exception-ledger route and
moves the next proof effort into a static scalar object.

## Claims To Treat As Bankable Planning, Not Proof

The following are good planning claims but still require proof/audit:

- The all-layer scalar apolar identity should be the first foundation check.
- The minimal scalar stratum should be
  `deg A = sigma + 1`, `deg B = j`.
- The correct denominator for the local-limit count is an effective group
  `G_eff`, not naive `q^sigma` occupancy.
- Circuit transversals are diagnostics, not the final theorem.
- Scalar list should temporarily lead MCA because it has a static canonical
  object and avoids line-level aggregation.

## Next Exact Lemma

The next exact lemma named by the referee is:

```text
L-LIST-MINIMAL-CI-GJ-FIBER
```

In short: for an apolar complete intersection

```text
I_s = (A, B),
deg A = sigma + 1,
deg B = j > sigma + 1,
gcd(A, B) = 1,
Delta = V(A),
```

prove that full-coordinate listed locators of degree `j` are exactly the
`j`-subsets whose product in the generalized Jacobian group `G_Delta` equals
the target class `b_Delta`, with the count taken over the effective subgroup
`G_eff`, and with invariance under generator shear.

## Director Evaluation

This is the strongest current planning answer because it has three virtues:

1. **It narrows the object.** The scalar-list apolar CI is much cleaner than
   all-denominator MCA.
2. **It gives a falsifiable first lemma.** Workers can prove or kill
   `L-LIST-MINIMAL-CI-GJ-FIBER` directly.
3. **It preserves the finite-prize discipline.** The checker remains parallel
   and is forbidden from accepting asymptotic `n^{1+o(1)}` language as a
   certificate.

The main risk is that the scalar route may not transfer enough to MCA. That is
why the `t=1` MCA color theorem remains the backup lane in Round 1 rather than
being postponed indefinitely.

## Recommended Next 9-Instance Round

Use the Master Referee allocation with only a light director adjustment:

1. `L-LIST-APOLAR-ALL-LAYER-CI`
2. `L-LIST-MINIMAL-CI-GJ-FIBER`
3. `W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT`
4. counterpacket hunter for the same local-limit wall
5. `L-JR-T1-GJ-FIBER-AND-COLOR`
6. `RS-PRIZE-FRONTIER-V1`
7. projective equality-scale packet verifier
8. degree-31 Lattes verifier
9. two-block-system overlap kill test

This is not nine attempts at a full solve. It is a disciplined proof/kill
round around the scalar apolar route with enough parallel support to prevent
route blindness.

## Stop Conditions I Accept

- Cut the scalar route if the all-layer CI or full-coordinate criterion is
  false.
- Rewrite the primitive theorem if it uses naive `q^sigma` rather than
  `G_eff`.
- Stop expanding quotient taxonomy if a second unrelated exception family
  appears outside apolar restriction, generalized Jacobians, resultants, or
  bounded-degree subresultants.
- Stop Lattes registry work after degree 31 unless the finite checker says it
  changes the first unresolved official reserve.

## Director Call

The next proof round should follow this plan. I would not run another broad
"try to solve the prize" prompt now. The best next move is a targeted
9-instance round centered on proving or killing
`L-LIST-MINIMAL-CI-GJ-FIBER` and its model local-limit sequel.

