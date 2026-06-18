# Cycle 25 Audit: Q-Zero detM-Nonzero Split Branch

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL with structured JSONL
recovery.

## Run

- Run id: `2026-06-18T11-18-04-005Z-cycle25-qzero-detm-nonzero-split-5a7d890d`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T11-18-04-005Z-cycle25-qzero-detm-nonzero-split-5a7d890d`
- Lane: isolated RS-MCA VS Code credited terminal lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL copied to
  `../raw/20260618_CYCLE25_QZERO_DETM_NONZERO_SPLIT_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 25 gives one useful algebraic identity and one sharper wall, but it
overclaims the consequence of `Q==0`.

Bank:

- the six-term Plucker/Laplace expansion of the determinant consistency
  polynomial `Q(z_0,z_1)`;
- the separation between the `z`-free source invariant
  `det M=(c_b/kappa^2)D` and the slope-fiber determinant `Q(z)`;
- the sharper rank-stratified wall:
  `W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY`.

Do not bank:

- the answer's claim that `Q(z)=0 iff z in C2`;
- the answer's claim that `Q==0` identically implies every `z in F` is a
  realized slope;
- a `Theta(q_line)` counterpacket;
- a proof of `O(p)` for the `Q==0` branch.

The determinant `Q(z)` is a necessary consistency condition for the affine
system `L_z(tau)=0`. It is sufficient only on the rank-three stratum for the
three coefficient columns. If those columns have rank `<3`, the determinant
may vanish while the affine system remains inconsistent. This is exactly why
Cycle 15 already required the rank/determinant pair and why Cycle 16 rejected
the raw claim that `Q==0` alone is a counterpacket.

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

## Banked Identity: Six-Term Plucker/Laplace Formula For `Q`

Cycle 15 writes the affine fiber equation

```text
L_z(tau)=iota(tau)-z mu(tau)=0 in A=F[X]/E
```

as a `B`-linear system in `tau=(tau_1,tau_2,tau_3)`. In the `F`-basis
`{u,b}` of `A`, write each column as

```text
c_i(z)=s_i(z)u+t_i(z)b,
```

with `s_i,t_i in F`. Expanding in the `B`-basis `{u, alpha u, b, alpha b}`,
let

```text
<x,y> = x_0 y_1 - x_1 y_0
```

be the alternating `B`-area form on `F=B+alpha B`. Then the `4 x 4`
determinant

```text
Q(z)=det_B[c_1(z) | c_2(z) | c_3(z) | c_0(z)]
```

has the six-term expansion

```text
Q = <s_1,s_2><t_3,t_0> - <s_1,s_3><t_2,t_0>
  + <s_1,s_0><t_2,t_3> + <s_2,s_3><t_1,t_0>
  - <s_2,s_0><t_1,t_3> + <s_3,s_0><t_1,t_2>.
```

This is a purely multilinear Laplace expansion along the two `u`-coordinate
rows and two `b`-coordinate rows. It verifies the general Plucker shape behind
Cycle 16's audit-only trace/Gram target, but it does not by itself prove the
specific trace/Gram criterion in Cycle 16.

Because each column is degree `<=1` in the two `B`-coordinates of `z`, the
determinant has total degree `<=4`. Therefore the Cycle 16 safe-side lemma
remains:

```text
Q not identically zero => C2 <= 4p.
```

## Banked Separation: `detM` Does Not Decide `Q`

Cycle 24 cuts the source-valid `D=0` branch:

```text
D=N(ell)kappa,
N(ell)=prod_{a in F_p}E(a),
```

so source-valid denominators give `D!=0` off `R0`. Cycle 20 gives

```text
det M=(c_b/kappa^2)D.
```

Thus, on `c_b!=0`, `det M!=0`. This is a `z`-free coefficient-frame invariant.
The determinant `Q(z)` is a slope-fiber consistency invariant. No banked
identity implies

```text
Q==0 => D=0
```

or

```text
D!=0 => Q not identically zero.
```

The `Q==0`, `D!=0`, `det M!=0` branch is therefore a genuine remaining wall,
not a hidden repeat of the Cycle 24 `D=0` branch.

## Audit Correction: `Q==0` Is Not A Counterpacket

For fixed `z`, realizability of a slope means the affine system

```text
c_1(z)tau_1+c_2(z)tau_2+c_3(z)tau_3+c_0(z)=0 in B^4
```

has a solution. The determinant equation

```text
Q(z)=0
```

is equivalent to linear dependence of the four columns. It is sufficient for
realizability only when the first three columns have rank `3`, because then
the fourth column lies in their span. If the first three columns have rank
`<3`, the determinant vanishes automatically after rank drop and may say
nothing about whether `c_0(z)` lies in the smaller span.

Therefore:

```text
realized slope => Q(z)=0,
```

but in general

```text
Q(z)=0 does not imply realized slope.
```

Consequently, do not bank the recovered answer's statement

```text
Q==0 identically => C2=p^2.
```

The correct counterpacket trigger remains:

```text
Q==0 identically
AND source-valid
AND enough rank/consistency conditions to realize Theta(p^2) slopes
AND distinct D-split cubics retained
```

over a growing prime family.

## Exact New Wall

The live wall is sharpened to:

```text
W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY
```

Decide the rank-stratified consistency problem on the source-valid
`Q==0`, `D!=0`, `det M!=0` branch.

For fixed `z`, let

```text
C(z)=[c_1(z)|c_2(z)|c_3(z)] in Mat_{4 x 3}(B),
c_0(z) in B^4.
```

The exact conditions are:

```text
rank C(z)=3:  Q(z)=0 is necessary and sufficient.
rank C(z)<3:  all rank(C)+1 minors of [C(z)|c_0(z)] must vanish.
```

The next theorem/counterpacket task is to prove one of:

1. On the source-valid `Q==0`, `D!=0`, `det M!=0` branch, the set of `z` for
   which the full rank-stratified consistency conditions hold is `O(p)`;
2. or there is a source-valid growing-prime family for which those conditions
   hold for `Theta(p^2)=Theta(q_line)` slopes and distinct `D`-split cubics.

Equivalently, compute the ideal generated by:

- all coefficients of `Q(z_0,z_1)` if attacking the identically-zero branch;
- the relevant rank and augmented-rank minors of `[C(z)|c_0(z)]`;
- source-valid nonzero conditions inverted:
  `kappa`, `c_b`, `D`, `det M`, and `prod_{a in F_p}E(a)`;
- separatedness / nonzero-on-`D` constraints.

This is a rank-stratified saturation problem, not just a `15`-coefficient
`Q`-saturation problem.

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- `Q(z)=0 iff z in C2` without a rank-three hypothesis;
- `Q==0` alone gives `C2=p^2`;
- `Q==0` alone gives a counterpacket;
- the specific Cycle 16 trace/Gram criterion as proved;
- any corrected-reserve theorem, full MCA bound, `q_gen` consequence,
  protocol/list/CA/MCA/line-decoding/curve-MCA/SNARK statement, or prize solve.

