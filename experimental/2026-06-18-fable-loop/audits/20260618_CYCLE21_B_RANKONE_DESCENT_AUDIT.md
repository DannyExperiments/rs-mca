# Cycle 21 Audit: B-Rank-One Descent

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL.

## Run

- Run id: `2026-06-18T08-56-10-692Z-cycle21-b-rankone-descent-5db3401b`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T08-56-10-692Z-cycle21-b-rankone-descent-5db3401b`
- Lane: isolated RS-MCA VS Code credited terminal ads lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL recovery copied
  to `../raw/20260618_CYCLE21_B_RANKONE_DESCENT_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 21 gives useful source-checkable algebra below the Cycle 20
`B`-rank-one descent wall, but it does not prove that the descent equations are
independent of rank-one collapse and it does not give a source-valid
counterpacket.

Bank the differential gates and the sharper `D`-kernel-alignment wall. Do not
bank the recovered answer's informal statement that descent can be satisfied
independently by tuning lower coefficients of `W`; that needs either an
elimination proof or an explicit source-valid family.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0`, meaning `kappa=u wedge b != 0`.
- Also assume `c_b=-Q_E(b)/kappa != 0` for the slope normal form and
  `W_{n-1} != 0` for the stated leading-data ratio.
- This is a restricted line-incidence/residue calculation only.

## Notation

Use the Cycle 20 notation:

```text
E=X^2+cX+d,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b,
c_b=-Q_E(b)/kappa,
eta=(c^2-d)+c tau_1+tau_2.
```

On the `Delta1==0` branch, Cycle 20 banked

```text
q1=c_b eta,
q2=lambda_0^(0)+(P_E(u,b)/kappa)eta,
p1=lambda_0^(0)-(c+P_E(u,b)/kappa)eta-A/kappa,
p2=(Q_E(u)/kappa)eta-A'/kappa,
```

where

```text
A=(ell Q) wedge b,
A'=u wedge (ell Q).
```

The slope roots are, up to the same fixed translation convention as Cycle 20,

```text
w^+-=(+-sqrt(delta_z)-A/kappa)/(2 c_b eta),
delta_z=(p1-q2)^2+4q1p2 in B[tau_1,tau_2].
```

Let

```text
L(f)=partial_{tau_1} f - c partial_{tau_2} f.
```

This is the coefficient of `df wedge d eta`, since
`eta=(c^2-d)+c tau_1+tau_2`.

## Banked Lemma 1: Differential Gate For The Two Branches

On the nonsingular discriminant locus where the displayed square-root
coordinate is legitimate,

```text
2 c_b eta (dw^+- wedge d eta)
  = +-(1/(2 sqrt(delta_z))) (d delta_z wedge d eta)
    - d(A/kappa) wedge d eta.
```

Equivalently, with

```text
J_delta=L(delta_z),
J_A=L(A/kappa),
```

one has

```text
dw^+- wedge d eta = 0
  iff
J_delta = +- 2 sqrt(delta_z) J_A.
```

Thus simultaneous collapse of both branches away from `delta_z=0` implies

```text
J_delta=0,
J_A=0.
```

Caveat: the ramified discriminant stratum `delta_z=0` needs separate handling
before this is used in a paper-facing proof.

## Banked Lemma 2: Collapse Reduces To Two Scalar Gates

The Cycle 20 normal form gives

```text
delta_z
 = C_2 eta^2
   + 2(c+2P)(A/kappa)eta
   - 4 c_b(A'/kappa)eta
   + (A/kappa)^2,
```

where `C_2` is independent of `(tau_1,tau_2)` for this calculation and
`P=P_E(u,b)/kappa`.

Applying `L`, using `L(eta)=0`, gives

```text
J_delta
 = [2(c+2P)J_A - 4 c_b J_Aprime] eta
   + 2 J_A(A/kappa),
J_Aprime=L(A'/kappa).
```

Therefore, under `c_b != 0` and `eta` nonconstant, simultaneous branch
collapse is equivalent to

```text
J_A=0,
J_Aprime=0.
```

This is a statement only about the slope-normal-form collapse mechanism. It is
not a `C2` bound and not a protocol/list/CA/MCA statement.

## Banked Lemma 3: The Cycle 20 Gate Is The Resultant Of The Collapse Gates

For `D=F_p`, the quotient coefficients from the earlier cycles give

```text
Q0=(W_{n-3}-d W_{n-1}) - W_{n-2} tau_1 + W_{n-1} tau_2,
Q1=(W_{n-2}-c W_{n-1}) - W_{n-1} tau_1.
```

Hence

```text
L(Q0)=-(W_{n-2}+c W_{n-1}),
L(Q1)=-W_{n-1}.
```

Set

```text
m=W_{n-2}+c W_{n-1},
w_1=W_{n-1}.
```

Using the Cycle 20 expansion

```text
(ell Q) wedge b = (ell wedge b)Q0 - P_E(b,ell)Q1,
u wedge (ell Q) = (u wedge ell)Q0 + P_E(u,ell)Q1,
```

one obtains the two collapse-gate forms

```text
kappa J_A      = -(ell wedge b)m + P_E(b,ell)w_1,
kappa J_Aprime = -(u wedge ell)m - P_E(u,ell)w_1.
```

Their `2 x 2` determinant is, up to the harmless sign convention from writing
the two rows,

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

This is the same gate banked in Cycle 20. Therefore:

```text
J_A=J_Aprime=0 with (m,w_1) nonzero
  implies D=0.

D != 0
  implies the simultaneous branch-collapse gates cannot both vanish.
```

When `D=0`, collapse is not automatic. It also requires the leading-data line

```text
(m:w_1)=(W_{n-2}+cW_{n-1}:W_{n-1})
```

to lie on the kernel line of the two collapse-gate forms.

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- that the descent equations `Im_alpha(p1+q2)=0` and
  `Im_alpha(det P)=0` are independent of the collapse gate;
- that the exact question has been refuted by a source-valid counterpacket;
- that `D != 0` alone gives the final `C2=O(p)` conclusion;
- collapse or non-collapse on the `D=0` locus;
- nonemptiness of an off-alignment seed stratum;
- any `Theta(q_line)` counterpacket;
- any above-reserve, `q_gen`, protocol, list-decoding, line-decoding, CA, MCA,
  curve-MCA, or SNARK consequence.

The recovered answer's independence sentence is a plausible attack direction
but not a proof. It lacks either a source-valid witness family or an
elimination argument showing the two base-descent equations leave the
leading-data ratio free off the kernel line.

## Sharpened Live Wall

The live wall is now:

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT
```

On the restricted `D=F_p`, `t=sigma=2`, `j=3`, off-`R0` branch, impose

```text
Delta1==0,
D==0,
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0.
```

Decide whether these equations force

```text
(W_{n-2}+cW_{n-1}:W_{n-1})
```

to be the kernel line of

```text
[(ell wedge b), -P_E(b,ell);
 (u wedge ell),  P_E(u,ell)].
```

If yes, the `D=0` branch collapses by the banked differential gates. If no, an
off-kernel source-valid family is the first serious seed for a
`Theta(q_line)` counterpacket in this sub-reserve toy window.

## Next Task

Run a focused proof/counterpacket/elimination prompt for
`W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`. The highest-value output would be one
of:

- a proof that base descent plus `D=0` forces the kernel alignment;
- a source-valid symbolic/growing-prime off-kernel family;
- an explicit elimination ideal/resultant certificate showing what remains;
- a small verifier script that can test the alignment condition on candidate
  data without merging `q_gen` and `q_line`.
