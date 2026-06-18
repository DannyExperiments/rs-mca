# Cycle 26 Audit: Q-Zero Rank-Consistency Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL with structured JSONL
recovery.

## Run

- Run id: `2026-06-18T11-42-37-221Z-cycle26-qzero-rank-consistency-45abe900`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T11-42-37-221Z-cycle26-qzero-rank-consistency-45abe900`
- Lane: isolated RS-MCA VS Code credited terminal lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL copied to
  `../raw/20260618_CYCLE26_QZERO_RANK_CONSISTENCY_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 26 gives a useful rank-stratification reduction for the affine
`tau`-space, but it does not settle the full source-valid split-cubic branch.

Bank:

- the DEP/NONDEP dichotomy for
  `C(z)=[c_1(z)|c_2(z)|c_3(z)]`;
- the implication `c notin B` and `c_b != 0` force the NONDEP case;
- in NONDEP, rank-drop occurs on only `O(p)` slopes, so the Cycle 16 safe side
  remains `Q not identically zero => O(p)`;
- in DEP, realizability requires augmented-rank conditions and is not enlarged
  by the rank drop.

Do not bank:

- a proof of `O(p)` on the full `Q==0` branch;
- a `Theta(q_line)` counterpacket;
- the claim that `Q==0` alone realizes `Theta(q_line)` slopes after the
  distinct split-cubic gate;
- the displayed `Q_4` formula as proved without an independent symbolic/local
  checker;
- any corrected-reserve, `q_gen`, protocol, list, CA, MCA, line-decoding,
  curve-MCA, SNARK, or prize statement.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0`, meaning `kappa=u wedge b != 0`.
- Source-valid denominator condition: `E` is nonzero on `D=F_p`.
- Cycle 24 gives `D!=0` off `R0` for source-valid denominators.

## Banked Reduction: DEP/NONDEP

Let

```text
C(z)=[c_1(z)|c_2(z)|c_3(z)] in Mat_{4 x 3}(B).
```

Define:

```text
NONDEP := at least one 3x3 minor of C(z) is not identically zero,
DEP    := all 3x3 minors of C(z) vanish identically.
```

Cycle 26 argues that in the `c notin B` branch, the leading symbols of columns
`1` and `2` are `-c_b c` and `-c_b`. Since `c_b != 0` and `c notin B`, these
are `B`-independent. Thus there is no universal `B`-linear dependence among
the three columns, so the branch is NONDEP.

This is bankable as a narrow rank statement subject to the Cycle 15/16 column
definitions.

## Banked Reduction: NONDEP Safe Side

In NONDEP, the rank-drop locus

```text
rank_B C(z) <= 2
```

is the common zero set of bounded-degree nonzero minors in the two `B`
coordinates of `z`. Thus it contributes only `O(p)` slopes.

Away from that rank-drop locus, `rank_B C(z)=3`, so the determinant condition

```text
Q(z)=det_B[c_1(z)|c_2(z)|c_3(z)|c_0(z)]=0
```

is necessary and sufficient for the affine consistency condition

```text
c_0(z) in span_B(c_1(z),c_2(z),c_3(z)).
```

Therefore:

```text
NONDEP and Q not identically zero => realized affine slopes are O(p).
```

This is the source-valid part of the Cycle 16 safe side, now with the rank
stratification made explicit. It still does not prove the split-cubic branch
because `Q==0` identically remains possible and because affine consistency in
`tau in B^3` must still retain distinct `D`-split cubics.

## Banked Reduction: DEP Does Not Create Slopes

In DEP, `Q` vanishes identically for rank reasons. This does not create a
counterpacket. Realizability requires the augmented rank conditions for

```text
[c_1(z)|c_2(z)|c_3(z)|c_0(z)].
```

Equivalently, `c_0(z)` must lie in the lower-dimensional column span. This
gives additional bounded-degree equations, so DEP can only shrink the realized
set unless those augmented conditions vanish identically. Cycle 26 therefore
sharpens the residual DEP wall to the augmented-identically-zero locus.

## Audit-Only Target: The Proposed `Q_4` Obstruction

The recovered answer proposes a top-degree obstruction:

```text
Q_4 = N(c_b) *
      ( Im_alpha(c) Im_alpha(q2^0)
      + Im_alpha(conj(c) w) Im_alpha(q2^2)
      - Im_alpha(w) Im_alpha(q2^1) )
```

with

```text
w=c^2-d,
q2^2=P,
q2^1=d+Pc,
q2^0=cd+P w.
```

It claims:

```text
Q_4 != 0 => Q not identically zero => O(p)
```

on NONDEP.

This is not yet banked as proved. The formula was hand-derived in the model
answer and needs an independent symbolic/local checker against the Cycle 15/16
definitions before it becomes a bankable lemma. It is, however, a high-value
next target because it gives a concrete scalar obstruction to the remaining
`Q==0` branch.

## Exact New Wall

The live wall is sharpened to:

```text
W-F1-AA-RES-T2J3-QZERO-Q4-SPLIT-GATE
```

Tasks:

1. Verify or refute the proposed `Q_4` formula from the Cycle 15/16 column
   definitions.
2. If correct, prove `Q_4 != 0` under the source-valid NONDEP hypotheses, or
   produce a source-valid family with `Q_4=0` and all lower coefficients of
   `Q` zero.
3. Carry the distinct `D`-split cubic gate explicitly: affine
   `tau in B^3` consistency is not enough for a line-incidence lower bound.
4. In the DEP branch, decide the augmented-identically-zero locus, especially
   the narrow `c in B`, `d notin B` possibility.

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- `Q==0` alone gives `Theta(q_line)` realized source-valid slopes;
- the `Q_4` formula is proved without an independent check;
- `Q_4` nonzero is forced by source-validity;
- affine `tau in B^3` consistency automatically keeps distinct split cubics;
- any corrected-reserve theorem, full MCA bound, `q_gen` consequence,
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement, or prize solve.
