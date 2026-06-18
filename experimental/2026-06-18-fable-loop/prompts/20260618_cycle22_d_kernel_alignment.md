# Cycle 22 Prompt: D-Kernel Alignment Wall

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 22.

## Target

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT
```

Do not summarize the whole repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE20_RANKONE_GATE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`

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

This is still a restricted line-incidence/residue calculation. Do not claim any
corrected-reserve, `q_gen`, protocol, list, CA, MCA, line-decoding, curve-MCA,
or SNARK consequence without a theorem.

## Banked facts

Use Cycle 20 notation:

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

On `Delta1==0`, Cycle 20 banks the slope normal form

```text
w^+-=(+-sqrt(delta_z)-A/kappa)/(2 c_b eta),
A=(ell Q) wedge b,
A'=u wedge (ell Q),
delta_z in B[tau_1,tau_2].
```

Cycle 21 banks the differential collapse gates. Let

```text
L(f)=partial_{tau_1} f - c partial_{tau_2} f,
J_A=L(A/kappa),
J_Aprime=L(A'/kappa).
```

Away from the discriminant ramification stratum, simultaneous collapse of both
slope branches is equivalent to

```text
J_A=0,
J_Aprime=0.
```

Writing

```text
m=W_{n-2}+c W_{n-1},
w_1=W_{n-1},
```

Cycle 21 banks

```text
kappa J_A      = -(ell wedge b)m + P_E(b,ell)w_1,
kappa J_Aprime = -(u wedge ell)m - P_E(u,ell)w_1.
```

Their determinant is the Cycle 20 gate

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

So `D != 0` blocks simultaneous branch collapse; when `D=0`, collapse is
equivalent to leading-data alignment:

```text
(m:w_1)=(W_{n-2}+cW_{n-1}:W_{n-1})
```

lies on the kernel line of

```text
[(ell wedge b), -P_E(b,ell);
 (u wedge ell),  P_E(u,ell)].
```

## Exact question

On the restricted `Delta1==0` branch, impose the base-descent equations

```text
Im_alpha(p1+q2)=0,
Im_alpha(det P)=0.
```

Also impose the gate

```text
D=0.
```

Do these equations force the leading-data alignment

```text
(W_{n-2}+cW_{n-1}:W_{n-1}) in ker
[(ell wedge b), -P_E(b,ell);
 (u wedge ell),  P_E(u,ell)]?
```

Or can one produce source-valid data satisfying `Delta1==0`, `D=0`, and the
two base-descent equations, but with the leading-data ratio off the kernel line?

## Desired output

Return exactly one primary label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

`PROOF`: prove the base-descent equations plus `D=0` force the kernel
alignment, under explicit hypotheses such as `kappa!=0`, `c_b!=0`,
`W_{n-1}!=0`, and away from discriminant ramification.

`COUNTERPACKET`: give source-valid symbolic or growing-prime data satisfying
the equations but off the kernel line. Single-prime evidence alone is not
enough; give a route to `C2/q_line` bounded below.

`BANKABLE_LEMMA`: prove a smaller exact implication involving `D`, the
alignment condition, `Im_alpha(p1+q2)`, `Im_alpha(detP)`, or the resultant
structure.

`ROUTE_CUT`: identify a false premise in Cycle 20 or Cycle 21's banked setup.

`EXACT_NEW_WALL`: isolate a strictly sharper algebraic condition below
`D`-kernel alignment, preferably an explicit elimination ideal, resultant, or
finite checker specification.

If output files are allowed in this run and you cannot close the wall by hand,
write a minimal checker or certificate schema under `output_files/` that tests
the `D=0` kernel-alignment condition on candidate symbolic/finite data. Do not
use internet sources.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

## Forbidden upgrades

- Do not claim the Proximity Prize is solved.
- Do not treat this `eta=2/n` window as corrected-reserve.
- Do not merge `q_gen` and `q_line`.
- Do not infer protocol denominator savings.
- Do not use internet or web sources.
- Do not cite finite scans as proof.
