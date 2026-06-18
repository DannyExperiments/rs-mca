# Cycle 22 Audit: D-Kernel Alignment Decoupling

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL.

## Run

- Run id: `2026-06-18T09-27-25-778Z-cycle22-d-kernel-alignment-ae350bc2`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T09-27-25-778Z-cycle22-d-kernel-alignment-ae350bc2`
- Lane: isolated RS-MCA VS Code credited terminal ads lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- `output_files/`: no deliverables written. The model reported `Write` was
  denied despite the run being staged with output files allowed.
- Audited provenance artifact: readable structured Claude JSONL recovery copied
  to `../raw/20260618_CYCLE22_D_KERNEL_ALIGNMENT_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 22 source-checks a useful decoupling identity below
`W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT`. It does not provide a source-valid
counterpacket and does not close the `D=0` branch.

Bank the exact identities: `Delta1==0` is exactly the two base-descent
conditions, the `D=0` branch reduces alignment to one scalar gate `J_A=0`, and
on `Delta1==0` the imaginary part of this scalar gate satisfies the
`DECOUPLE` identity below.

Do not bank nonemptiness of the off-kernel stratum, any `C2` lower bound, or
any `Theta(q_line)` counterpacket.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0`, meaning `kappa=u wedge b != 0`.
- Also assume `c_b=-Q_E(b)/kappa != 0`, `W_{n-1} != 0`, and avoid
  discriminant ramification when translating branch-collapse statements.
- This is a restricted line-incidence/residue calculation only.

## Notation

Use the Cycle 20 and Cycle 21 notation:

```text
E=X^2+cX+d,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b,
eta=(c^2-d)+c tau_1+tau_2.
```

Set

```text
g1=ell wedge b,
g2=P_E(b,ell),
h1=u wedge ell,
h2=P_E(u,ell),
M_ker=[[g1,-g2],[h1,h2]],
D=g1 h2+g2 h1.
```

Let

```text
Q0=(W_{n-3}-dW_{n-1})-W_{n-2}tau_1+W_{n-1}tau_2,
Q1=(W_{n-2}-cW_{n-1})-W_{n-1}tau_1,
m=W_{n-2}+cW_{n-1},
w_1=W_{n-1}.
```

Then

```text
A=g1 Q0-g2 Q1,
A'=h1 Q0+h2 Q1,
J_A=L(A/kappa),
J_Aprime=L(A'/kappa),
L=partial_{tau_1}-c partial_{tau_2}.
```

## Banked Lemma 1: `Delta1==0` Is Exactly Base Descent

Cycle 20 put the determinant in monic form

```text
Delta=tau_3^2-(p1+q2)tau_3+detP.
```

Splitting over `F=B+alpha B`, the `alpha`-part is

```text
Delta1=-Im_alpha(p1+q2) tau_3+Im_alpha(detP).
```

Therefore

```text
Delta1==0
  iff
Im_alpha(p1+q2)=0
and
Im_alpha(detP)=0.
```

This is not a route cut; it confirms that the prompt's `Delta1==0` plus the
two base-descent equations is just `Delta1==0`.

## Banked Lemma 2: On `D=0`, Alignment Is One Scalar Gate

Cycle 21 already banked

```text
kappa J_A      = -g1 m+g2 w_1,
kappa J_Aprime = -h1 m-h2 w_1.
```

Thus

```text
M_ker [m,w_1]^T = -kappa [J_A,J_Aprime]^T.
```

With `kappa!=0`,

```text
(m:w_1) in ker M_ker
  iff
J_A=J_Aprime=0.
```

If `D=0` and the first row `(g1,-g2)` is nonzero, the two rows are dependent.
Then there is `rho` with

```text
h1=rho g1,
h2=-rho g2,
J_Aprime=rho J_A.
```

Consequently, on `D=0`,

```text
alignment
  iff
J_A=0
  iff
g1 m=g2 w_1
  iff
(m:w_1)=(g2:g1).
```

The kernel line is therefore

```text
(P_E(b,ell): ell wedge b).
```

## Banked Lemma 3: Differential Dictionary

Cycle 20 gives

```text
p1+q2=2L_c-c eta-A/kappa,
L_c=cd+d tau_1.
```

Since `L(eta)=0` and `L(L_c)=d`,

```text
J_A=2d-L(p1+q2).
```

Also

```text
p2=(Q_E(u)/kappa)eta-A'/kappa,
```

so

```text
J_Aprime=-L(p2).
```

Finally, applying Leibniz to `detP=p1q2-p2q1`, using
`L(q1)=0`, `L(q2)=d`, `L(p1)=d-J_A`, gives

```text
L(detP)=d(p1+q2)-J_A q2+J_Aprime q1.
```

## Banked Lemma 4: The `DECOUPLE` Identity

On `Delta1==0`, write

```text
p1+q2=f_0+f_1 tau_1+f_2 tau_2,
f_i in B.
```

The `tau_2` coefficient comes only from `-c eta` and `-A/kappa`. Since the
`tau_2` coefficient of `Q0` is `w_1=W_{n-1}` and the `tau_2` coefficient of
`Q1` is zero,

```text
f_2=-c-(g1 w_1)/kappa.
```

Because

```text
L(p1+q2)=f_1-c f_2
```

and `f_1,f_2 in B`, the imaginary projection gives

```text
Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2.       (DECOUPLE)
```

Consequences:

- The base-descent condition makes `f_2` a base-field element, but does not by
  itself set `J_A=0`.
- If `Im_alpha(c)!=0`, alignment requires the additional scalar condition
  `f_2=-2 Im_alpha(d)/Im_alpha(c)` plus the real part of `J_A=0`.
- If `c in B` and `d notin B`, then `Im_alpha(c)=0` and
  `Im_alpha(d)!=0`, so for odd characteristic

```text
Im_alpha(J_A)=2 Im_alpha(d) != 0.
```

Thus alignment is impossible on any source-valid point of the stratum

```text
Delta1==0,
D=0,
c in B,
d notin B.
```

This is the sharpest bankable Cycle 22 conclusion. It is conditional on the
stratum being nonempty under the remaining source constraints.

## Banked Lemma 5: `detP` Descent Identity On `D=0`

On `D=0`, write `J_Aprime=rho J_A`. If `detP` and `p1+q2` lie in
`B[tau_1,tau_2]`, then applying `Im_alpha` to the differential dictionary gives

```text
-Im_alpha(c) partial_{tau_2}(detP)
  =
Im_alpha(d)(p1+q2)-Im_alpha(J_A(q2-rho q1)).
```

This identity is bankable. The informal conclusion that `detP` descent is
"independent" of alignment should not be treated as a theorem without an
elimination proof or a witness family.

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- a full counterpacket;
- nonemptiness of the off-kernel stratum;
- a `C2=Theta(q_line)` split-cubic lower bound;
- collapse or non-collapse of the entire `D=0` branch;
- any above-reserve, `q_gen`, protocol, list-decoding, line-decoding, CA, MCA,
  curve-MCA, or SNARK consequence.

Also do not bank the inline checker as a verified deliverable. No `output_files`
were produced, and the pasted script is only a sketch for a future checker.

## Sharpened Live Wall

The live wall is now:

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS
```

Focus on the stratum

```text
c in B,
d notin B,
Delta1==0,
D=0,
off R0,
c_b!=0,
W_{n-1}!=0.
```

On this stratum, Cycle 22's `DECOUPLE` identity makes alignment impossible.
The remaining questions are:

1. Is this stratum source-valid and nonempty after all constraints from
   `E`, `Bnum`, `W`, `ell=[X^p-X]_E`, `Delta1==0`, and `D=0` are imposed?
2. If nonempty, does it realize `Omega(p^2)` distinct split-cubic bad slopes,
   or only `O(p)`?

Outcomes:

- Empty stratum or only `O(p)` slopes: this closes the `D=0` branch in the
  restricted `t=2,j=3` toy window.
- Nonempty stratum plus `Omega(p^2)` split-cubic slopes: this gives the first
  source-valid `Theta(q_line)` counterpacket seed in the sub-reserve toy
  window.

## Next Task

Run a focused proof/counterpacket/source-audit prompt for
`W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS`. The highest-value output
is not another differential identity. It is one of:

- an elimination proof that the `c in B`, `d notin B` stratum is empty;
- a proof that it has only `O(p)` split-cubic slopes;
- a source-valid symbolic/growing-prime witness family with `Omega(p^2)`
  slopes;
- a precise checker/certificate schema that computes the full
  `W -> (p1,p2,q1,q2)` pipeline and tests the stratum without merging
  `q_gen` and `q_line`.
