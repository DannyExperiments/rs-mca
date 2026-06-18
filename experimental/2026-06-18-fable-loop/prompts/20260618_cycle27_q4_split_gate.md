# Cycle 27 Prompt: Q4 Obstruction And Split-Cubic Gate

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 27.

## Target

```text
W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE
```

Do not summarize the repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/CUTS_AND_FALSE_ROUTES.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_AUDIT.md`

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

Cycle 24:

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a),
source-valid and off R0 => D != 0.
```

Cycle 25:

```text
Q(z)=0 is only necessary in general.
It is sufficient when C(z)=[c_1(z)|c_2(z)|c_3(z)] has rank 3.
Rank-drop strata require augmented-rank conditions.
```

Cycle 26:

```text
NONDEP := some 3x3 minor of C(z) is not identically zero.
DEP    := all 3x3 minors of C(z) vanish identically.

c notin B and c_b != 0 => NONDEP.

NONDEP and Q not identically zero => O(p) affine-consistent slopes.
```

Cycle 26 proposed but did not prove the following top-degree obstruction:

```text
Q_4 = N(c_b) *
      ( Im_alpha(c) Im_alpha(q2^0)
      + Im_alpha(conj(c) w) Im_alpha(q2^2)
      - Im_alpha(w) Im_alpha(q2^1) )

w=c^2-d,
q2^2=P,
q2^1=d+Pc,
q2^0=cd+P w.
```

## Exact Question

Settle the next obstruction.

1. Verify or refute the displayed `Q_4` formula from the Cycle 15/16 column
   definitions. If the formula is wrong, give the corrected top-degree
   coefficient of `Q(z_0,z_1)`.
2. If the formula is correct, prove or refute:

```text
source-valid,
E nonzero on D=F_p,
E separated gcd(E,E^tau)=1,
off R0,
c_b != 0,
c notin B,
D != 0,
det M=(c_b/kappa^2)D != 0
=> Q_4 != 0.
```

3. If `Q_4=0` can occur source-validly, decide whether all lower coefficients
   of `Q` can also vanish while the distinct `D`-split cubic gate is retained.
4. Treat affine `tau in B^3` consistency and actual distinct split-cubic
   line-incidence separately. Do not use affine consistency alone as a
   `Theta(q_line)` counterpacket.

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

`PROOF`: prove the live branch gives only `O(p)` source-valid distinct-split
slopes or is empty.

`COUNTERPACKET`: give a source-valid symbolic/growing-prime family with
`Theta(p^2)=Theta(q_line)` realized slopes after the distinct split-cubic gate.
Single-prime evidence is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication, such as corrected `Q_4`,
source-valid `Q_4 != 0` on a branch, or a split-gate obstruction.

`ROUTE_CUT`: identify a false premise in Cycles 15/16/25/26.

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
