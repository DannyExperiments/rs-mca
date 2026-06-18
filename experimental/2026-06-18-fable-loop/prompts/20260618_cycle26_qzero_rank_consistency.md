# Cycle 26 Prompt: Q-Zero Rank-Consistency Wall

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 26.

## Target

```text
W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY
```

Do not summarize the repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/CUTS_AND_FALSE_ROUTES.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE24_NONSPLIT_C_DKERNEL_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`

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

## Banked Facts You May Use

Cycle 16 safe side:

```text
Q not identically zero => C2 <= 4p.
```

Cycle 24 source-valid `D=0` cut:

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a),
source-valid and off R0 => D != 0.
```

Cycle 25 Plucker/Laplace determinant identity:

```text
Q = <s_1,s_2><t_3,t_0> - <s_1,s_3><t_2,t_0>
  + <s_1,s_0><t_2,t_3> + <s_2,s_3><t_1,t_0>
  - <s_2,s_0><t_1,t_3> + <s_3,s_0><t_1,t_2>.
```

Cycle 25 audit correction:

```text
Q(z)=0 is only a necessary consistency condition in general.
It is sufficient only when C(z)=[c_1(z)|c_2(z)|c_3(z)] has rank 3.
If rank C(z)<3, augmented rank conditions for [C(z)|c_0(z)] are needed.
```

## Exact Question

Settle the rank-stratified consistency problem on the source-valid branch:

```text
source-valid E nonzero on D=F_p,
E separated in the loop sense gcd(E,E^tau)=1,
off R0,
c_b=-Q_E(b)/kappa != 0,
D!=0,
det M=(c_b/kappa^2)D != 0,
Q(z_0,z_1)==0 identically,
distinct D-split cubics T subset F_p, |T|=3 retained.
```

For fixed `z`, let

```text
C(z)=[c_1(z)|c_2(z)|c_3(z)] in Mat_{4 x 3}(B),
c_0(z) in B^4.
```

The exact realized-slope condition is

```text
c_0(z) in span_B(c_1(z),c_2(z),c_3(z)).
```

Questions:

1. Prove that, on the source-valid `Q==0`, `D!=0`, `det M!=0` branch, the
   rank-stratified consistency set has size `O(p)`.
2. Or produce a source-valid symbolic/growing-prime family where the
   rank-stratified consistency set has size `Theta(p^2)=Theta(q_line)` and
   distinct `D`-split cubics are retained.
3. If neither is reachable, isolate the smallest exact rank/minor
   factorization, elimination ideal, or finite-checker certificate that decides
   this branch.

Do not repeat the false implication `Q==0 => every slope is realized`.

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

`PROOF`: prove the live branch gives only `O(p)` slopes or is empty.

`COUNTERPACKET`: give a source-valid symbolic/growing-prime family with
`Theta(p^2)=Theta(q_line)` realized slopes after the rank-stratified
consistency test. Single-prime evidence is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication, such as rank-drop forcing
`O(p)`, full-rank `Q==0` impossibility under source-validity, or a determinant
factorization that decides the branch.

`ROUTE_CUT`: identify a false premise in Cycles 15/16/24/25.

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

