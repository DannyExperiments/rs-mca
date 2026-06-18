Try to fully solve the problem. If you cannot fully solve it, progress it as
much as possible. No Internet.

You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director. This is Cycle 20. The immediate goal is not broad
summarization; it is to audit and, if possible, prove the rank-one/gate claims
suggested by Cycle 19's malformed-but-readable structured recovery.

# Target

```text
W-F1-AA-RES-T2J3-RANKONE-GATE-AUDIT
```

If the rank-one/gate formulas are correct, they may be the next crack in the
restricted F1 line-incidence wall. If they are false, identify the first false
identity and cut the route cleanly.

# Source files to read first

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE19_RESONANCE_COLLAPSE_AUDIT.md`

# Ledger

Keep these separate:

```text
B=F_p,        q_gen=p
F=F_{p^2},    q_line=p^2
q_chal unused
D=F_p,        n=p
t=sigma=2
j=n-a=r-t=3, so a=n-3, k=n-5
eta=sigma/n=2/n, sub-reserve
work off R0={kappa=[W]_E wedge [Bnum]_E=0}
```

Do not claim any corrected-reserve theorem, `q_gen` result, protocol result,
list-decoding result, CA, MCA, line-decoding, or curve-MCA consequence.

# Previously banked algebra

Cycle 14 banked, off `R0`, that `{[W]_E,b}` is an `F`-basis of `A=F[X]/E`,
with `b=[Bnum]_E`, and

```text
iota(tau)=A0(tau_1,tau_2)-tau_3[W]_E,
mu(tau)=B0(tau_1,tau_2)-tau_3 b,
A0=p1[W]_E+p2 b,
B0=q1[W]_E+q2 b.
```

Cycle 18 banked:

```text
Delta=wedge_{W,b}(iota,mu)
     =(p1-tau_3)(q2-tau_3)-p2 q1,
```

so after splitting `Delta=Delta0+alpha Delta1`,

```text
deg_{tau_3} Delta0=2, leading coefficient 1,
deg_{tau_3} Delta1<=1.
```

# Cycle 19 candidate formulas to audit

Cycle 19 was `HARNESS_MALFORMED_VISIBLE_TERMINAL`, so these are not banked.
Your job is to prove or refute them from source identities.

Work in `A=F[X]/E` with

```text
E=X^2+cX+d, xi=[X]_E, xi^2=-c xi-d,
u=[W]_E, b=[Bnum]_E, ell=[L_D]_E=[X^p-X]_E,
kappa=u wedge b.
```

Candidate closed forms:

```text
lambda_0^(1) = eta = (c^2-d) + c tau_1 + tau_2,
q1 = -(Q_E(b)/kappa) eta,
q2 = lambda_0^(0) + (P_E(u,b)/kappa) eta,
p1 = lambda_0^(0) - (c + P_E(u,b)/kappa) eta
     - (1/kappa)((ell Q) wedge b),
p2 = (1/kappa)(Q_E(u) eta - (u wedge ell Q)).
```

Here `P_E,Q_E` are the multiplication bilinear/quadratic forms induced by
reduction modulo `E`. You must define them explicitly if you use them.

Candidate rank-one lemma:

```text
q1 is a scalar multiple of eta.
```

Candidate quadric-branch normal form:

On `Delta1==0`, the slope discriminant descends to `B[tau_1,tau_2]`:

```text
delta_z=(p1-q2)^2+4q1p2=(p1+q2)^2-4 det P in B[tau_1,tau_2].
```

The slopes are, up to fixed `F`-translation,

```text
w^+- = ( +-sqrt(delta_z) - A/kappa ) / (2 c_b eta),
A=(ell Q) wedge b,
c_b=-Q_E(b)/kappa.
```

Candidate scalar gate:

```text
D=(ell wedge b) P_E(u,ell)+P_E(b,ell)(u wedge ell).
```

# Required output

Return exactly one primary label:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

Use `BANKABLE_LEMMA` only if you prove at least one of the formulas above
under exact hypotheses, with no hidden genericity.

Use `ROUTE_CUT` if a formula is false. Identify the first false identity and
which prior wall survives.

Use `EXACT_NEW_WALL` if the formulas are correct but the collapse question
reduces to a sharper named condition, for example:

```text
dw wedge d eta == 0 on the Delta1==0 locus
```

or an equivalent resultant/Jacobian/common-component gate.

Use `COUNTERPACKET` only if you produce source-valid growing-prime data or a
symbolic family with `C2/p^2` bounded below. Single-prime evidence is only
EXPERIMENTAL.

End by answering:

```text
Do you see a route to a full solve? If yes, what is the next exact lemma or construction?
```

# Forbidden upgrades

- Do not claim the Proximity Prize is solved unless every source hypothesis is
  discharged.
- Do not treat this sub-reserve `eta=2/n` window as a corrected-reserve theorem.
- Do not merge `q_gen` and `q_line`.
- Do not infer any protocol denominator saving.
- Do not cite finite scans as proof.
- Do not use internet or web sources.
