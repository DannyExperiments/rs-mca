# Cycle 23 Prompt: D-Kernel Nonemptiness And Split Count

Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 23.

## Target

```text
W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT-NONEMPTINESS
```

Do not summarize the whole repository. Attack this exact wall.

## Read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE21_B_RANKONE_DESCENT_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE22_D_KERNEL_ALIGNMENT_AUDIT.md`

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

## Banked Cycle 22 reduction

Use notation:

```text
E=X^2+cX+d,
u=[W]_E,
b=[Bnum]_E,
ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b,
g1=ell wedge b,
g2=P_E(b,ell),
h1=u wedge ell,
h2=P_E(u,ell),
D=g1 h2+g2 h1.
```

On `Delta1==0`, write

```text
p1+q2=f_0+f_1 tau_1+f_2 tau_2,
f_i in B.
```

Cycle 22 banks:

```text
alignment on D=0
  iff
J_A=0
  iff
(W_{n-2}+cW_{n-1}:W_{n-1})=(g2:g1).
```

It also banks the decoupling identity:

```text
Im_alpha(J_A)=2 Im_alpha(d)+Im_alpha(c) f_2.       (DECOUPLE)
```

Therefore, on the stratum

```text
c in B,
d notin B,
Delta1==0,
D=0,
```

alignment is impossible in odd characteristic, because

```text
Im_alpha(J_A)=2 Im_alpha(d) != 0.
```

## Exact question

Settle the residual stratum:

```text
c in B,
d notin B,
Delta1==0,
D=0,
off R0,
c_b=-Q_E(b)/kappa != 0,
W_{n-1} != 0.
```

Question A:

Is this stratum source-valid and nonempty after the definitions of

```text
ell=[X^p-X]_E,
u=[W]_E,
b=[Bnum]_E,
Q0,Q1,p1,p2,q1,q2,
Delta1,
D
```

are imposed?

Question B:

If it is nonempty, does it realize `Omega(p^2)` distinct split-cubic bad slopes
over growing primes, or only `O(p)`?

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

`PROOF`: prove the stratum is empty or prove it has only `O(p)` split-cubic
slopes, thereby closing this restricted `D=0` branch.

`COUNTERPACKET`: give a source-valid symbolic/growing-prime family in the
stratum with `Omega(p^2)=Omega(q_line)` distinct split-cubic bad slopes.
Single-prime evidence alone is not enough.

`BANKABLE_LEMMA`: prove a smaller exact implication: for example, a necessary
condition that makes the stratum empty under `ell=[X^p-X]_E`, or a slope-count
bound on a meaningful subcase.

`ROUTE_CUT`: identify a false premise in Cycle 22's decoupling or stratum
formulation.

`EXACT_NEW_WALL`: isolate a strictly sharper algebraic condition below
nonemptiness/split-count, preferably an explicit elimination ideal,
resultant, or finite checker specification.

If tool writing is unavailable, do not spend time trying to create files.
Give the proof, counterpacket, or checker specification inline.

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
