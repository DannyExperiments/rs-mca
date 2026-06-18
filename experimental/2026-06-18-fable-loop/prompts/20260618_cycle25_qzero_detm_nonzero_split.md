# Cycle 25 Prompt: Q==0 With detM Nonzero

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 25.

## Target

```text
W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT
```

Do not summarize the repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/CUTS_AND_FALSE_ROUTES.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`

## Ledger

Keep these separate:

```text
B=F_p,        q_gen=p
F=F_{p^2},    q_line=p^2
q_chal unused
D=F_p,        n=p
t=sigma=2
j=n-a=r-t=3, so a=n-3, k=n-5
eta_reserve=sigma/n=2/n, sub-reserve
work off R0, i.e. kappa=[W]_E wedge [Bnum]_E != 0
```

This remains a restricted line-incidence/residue calculation. Do not claim any
corrected-reserve, `q_gen`, protocol, list, CA, MCA, line-decoding, curve-MCA,
or SNARK consequence without a theorem.

## Banked Reductions You May Use

Cycle 13:

```text
Delta=Res(L_T,E)*([I_S]_E wedge [Bnum]_E),
Res(L_T,E)!=0 on valid supports.
```

After splitting `Delta=Delta_0+alpha Delta_1`, the safe complete-intersection
side gives `C2=O(p)` off `R0 union Ra union Rb`.

Cycle 15:

Landing `[I_S]_E=z b` is equivalent to

```text
L_z(tau)=iota(tau)-z mu(tau)=0 in A=F[X]/E.
```

For fixed `z=z_0+alpha z_1`, this is an affine `B`-linear system in
`tau=(tau_1,tau_2,tau_3) in B^3`. Let the columns be

```text
c1(z), c2(z), c3(z) in A ~= B^4
```

and let

```text
Q(z_0,z_1)=det_B[c1(z)|c2(z)|c3(z)|c0(z)].
```

Cycle 16:

```text
Q not identically zero  =>  C2 <= 4p = O(p)
```

in this `D=F_p`, `t=sigma=2`, `j=3` test regime. The only possible
`Theta(q_line)` branch is therefore

```text
Q(z_0,z_1) == 0 identically.
```

Cycle 20:

```text
det M=(c_b/kappa^2)D,
c_b=-Q_E(b)/kappa.
```

Cycle 24:

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a).
```

For source-valid denominators nonzero on `D=F_p`, `N(ell)!=0`; off `R0`,
`kappa!=0`; hence the source-valid `D=0` branch is empty. In the live branch
you may assume

```text
D != 0,
det M != 0
```

whenever `c_b != 0`.

## Exact Question

Settle the remaining determinant-split branch:

```text
source-valid E nonzero on D=F_p,
E separated in the loop sense gcd(E,E^tau)=1,
off R0,
c_b=-Q_E(b)/kappa != 0,
Q(z_0,z_1)==0 identically,
D!=0,
det M=(c_b/kappa^2)D != 0,
distinct D-split cubics T subset F_p, |T|=3 retained.
```

Questions:

1. Reconstruct the exact `Q(z_0,z_1)` determinant from Cycles 15/16/18/20.
2. Decide whether `Q==0` and `det M!=0` are compatible with source-valid
   data, or whether they force a hidden degeneracy already excluded.
3. If compatible, decide whether the split-cubic slope image is still `O(p)`
   or whether there is a growing-prime source-valid family with
   `C2=Theta(p^2)=Theta(q_line)`.
4. If a proof/counterpacket is too large, isolate the smallest exact algebraic
   condition, invariant, elimination ideal, or finite-checker certificate that
   would decide this branch.

## Desired Output

Return exactly one primary label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

`PROOF`: prove the live branch empty or prove an `O(p)` split-cubic slope
bound under the stated restrictions.

`COUNTERPACKET`: give a source-valid symbolic/growing-prime family with
`Theta(p^2)=Theta(q_line)` distinct split-cubic bad slopes. Single-prime
evidence is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication, such as `Q==0` forcing a
rank-one slope map, a descent identity under `det M!=0`, or a usable
factorization of `Q`.

`ROUTE_CUT`: identify a false premise in Cycles 15/16/18/20/24.

`EXACT_NEW_WALL`: isolate a strictly sharper algebraic condition, elimination
ideal, resultant, or finite checker specification.

If tool writing is unavailable, do not spend time trying to create files. Give
the proof, counterpacket, or checker specification inline.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Forbidden Upgrades

- Do not claim the Proximity Prize is solved.
- Do not treat this `eta=2/n` window as corrected-reserve.
- Do not merge `q_gen` and `q_line`.
- Do not infer protocol denominator savings.
- Do not use internet or web sources.
- Do not cite finite scans as proof.

