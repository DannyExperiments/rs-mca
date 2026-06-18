# Cycle 19 Audit: Resonance Collapse Rank-One Candidate

Status: AUDIT / HARNESS_MALFORMED_VISIBLE_TERMINAL.

Candidate mathematical status from recovered provenance:
BANKABLE_LEMMA candidate / EXACT_NEW_WALL candidate.

## Run

- Run id: `2026-06-18T08-06-29-704Z-cycle19-resonance-slope-map-collapse-a62c41af`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T08-06-29-704Z-cycle19-resonance-slope-map-collapse-a62c41af`
- Lane: isolated RS-MCA VS Code credited terminal ads lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- `response_recovered_claude_jsonl.md`: readable, copied to
  `../raw/20260618_CYCLE19_RESONANCE_COLLAPSE_RECOVERED_CLAUDE_JSONL.md`.
- `output_files/`: empty.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 19 did not produce a clean theorem artifact under the wrapper rules. It
should not be treated as a promoted proof, counterpacket, or banked lemma.

The recovered structured text is nevertheless mathematically useful provenance:
it proposes a closed-form rank-one structure for the Cycle 14 slope forms and a
sharper scalar gate for the resonance-collapse wall. The next run should audit
or prove these formulas directly from the Cycle 12/14 multiplication identities.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0={ wedge([W]_E,[Bnum]_E)=0 }`.
- This is still a restricted line-incidence/residue calculation only.

## Candidate Content To Audit Next

The recovered answer claims that, in `A=F[X]/E` with
`E=X^2+cX+d`, `xi=[X]_E`, `xi^2=-c xi-d`,
`u=[W]_E`, `b=[Bnum]_E`, and `ell=[L_D]_E=[X^p-X]_E`, the Cycle 14
affine forms have the closed structure:

```text
lambda_0^(1) = eta = (c^2-d) + c tau_1 + tau_2,
q1 = -(Q_E(b)/kappa) eta,
q2 = lambda_0^(0) + (P_E(u,b)/kappa) eta,
p1 = lambda_0^(0) - (c + P_E(u,b)/kappa) eta
     - (1/kappa)((ell Q) wedge b),
p2 = (1/kappa)(Q_E(u) eta - (u wedge ell Q)).
```

Here `kappa=u wedge b`, and `P_E,Q_E` are the multiplication bilinear/quadratic
forms induced by reduction modulo `E`.

The important candidate lemma is:

```text
q1 is a scalar multiple of the single affine form eta.
```

The recovered answer also claims that in the `Delta1==0` quadric branch,
the discriminant of the slope quadratic descends to `B[tau_1,tau_2]`:

```text
delta_z := (p1-q2)^2 + 4 q1 p2
         = (p1+q2)^2 - 4 det P in B[tau_1,tau_2],
```

and the slopes have the normal form, up to fixed `F`-translation,

```text
w^+- = ( +-sqrt(delta_z) - A/kappa ) / (2 c_b eta),
A=(ell Q) wedge b,
c_b=-Q_E(b)/kappa.
```

If correct, this sharpens the current wall: collapse is not generic. It would
have to be forced by the resonance conditions through a rank-one dependence of
`A/kappa` and `sqrt(delta_z)` on `eta`.

The recovered answer proposes the scalar gate

```text
D := (ell wedge b) P_E(u,ell) + P_E(b,ell)(u wedge ell).
```

as the obstruction measuring whether the `P^2(F)` coefficient image degenerates.

## What Is Not Banked

Do not bank from Cycle 19 yet:

- the closed formulas for `p_i,q_i`;
- the rank-one `q1` lemma;
- the quadric normal form;
- the scalar gate `D`;
- collapse or non-collapse;
- a `Theta(q_line)` counterpacket;
- any corrected-reserve statement;
- any `q_gen` statement;
- any protocol/list/CA/MCA/line-decoding consequence.

These are candidate advances pending a clean source-valid proof or checker.

## Next Target

Ask the next worker to audit/prove or refute the recovered Cycle 19 formulas:

```text
W-F1-AA-RES-T2J3-RANKONE-GATE-AUDIT
```

Required outcome:

- `BANKABLE_LEMMA`: prove the rank-one `q1` formula, quadric normal form, and
  gate `D` from source identities;
- `ROUTE_CUT`: identify the first false formula and return to the previous
  wall;
- `COUNTERPACKET`: produce source-valid growing-prime data only if the formulas
  expose a genuine `Theta(q_line)` branch;
- `EXACT_NEW_WALL`: isolate the next smaller algebraic condition, preferably
  `dw wedge d eta == 0` on the `Delta1==0` locus.
