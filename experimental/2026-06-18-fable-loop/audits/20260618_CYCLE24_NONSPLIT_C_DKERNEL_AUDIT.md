# Cycle 24 Audit: Nonsplit-c D-Kernel Cut

Status: BANKABLE_LEMMA / ROUTE_CUT / AUDIT.

Harness status: HARNESS_MALFORMED_VISIBLE_TERMINAL.

## Run

- Run id: `2026-06-18T10-20-59-560Z-cycle24-nonsplit-c-dkernel-c5b74f9e`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T10-20-59-560Z-cycle24-nonsplit-c-dkernel-c5b74f9e`
- Lane: isolated RS-MCA VS Code credited terminal lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`,
  `noOutputTimedOut=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL copied to
  `../raw/20260618_CYCLE24_NONSPLIT_C_DKERNEL_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 24 gives a source-valid restricted route cut. In the `D=F_p`, `B=F_p`,
`F=F_{p^2}`, `t=sigma=2`, `j=3`, off-`R0` window, the Cycle 20/21 gate

```text
D=(ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)
```

factors as

```text
D=N(ell) kappa,
N(ell)=prod_{a in F_p} E(a).
```

Here `ell=[X^p-X]_E=[L_D]_E` and `kappa=u wedge b`. Therefore on any actual
source-valid residue-line datum, where the denominator `E` is nonzero on
`D=F_p`, `N(ell)!=0`. Off `R0`, `kappa!=0`, so `D!=0`.

Thus the whole `D=0`, off-`R0`, source-valid branch in this restricted
`t=2,j=3` residue-line calculation is empty. This cuts the previous nonsplit
`c notin B` wall and also subsumes the Cycle 23 `c in B`, `d notin B` lemma.

This remains a restricted local line-incidence/residue result only. It is not a
corrected-reserve theorem, not a `q_gen` statement, and not a protocol, list,
CA, MCA, line-decoding, curve-MCA, or SNARK statement.

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
- Separated quadratic convention used in this loop: `gcd(E,E^tau)=1`.

## Notation

Work in

```text
A=F[X]/E,
E=X^2+cX+d,
xi=[X]_E,
u=[W]_E,
b=[Bnum]_E,
ell=[X^p-X]_E,
kappa=u wedge b.
```

The Cycle 21/22 convention is

```text
x wedge y = x_0 y_1 - x_1 y_0,
P_E(x,y)=x_0 y_0 - c x_0 y_1 + d x_1 y_1.
```

## Banked Lemma 1: Frobenius Closed Form For `ell`

Put

```text
s=xi+c/2,
w=c^2/4-d,
nu=w^((p-1)/2),
mu=nu-1,
delta_c=(c-c^p)/2.
```

Since `s^2=w`, in `A`

```text
s^p=w^((p-1)/2)s=nu s.
```

On the other hand,

```text
s^p=xi^p+c^p/2=xi+ell+c^p/2.
```

Solving gives

```text
ell=mu*(xi+c/2)+delta_c.
```

Equivalently, in the basis `{1,xi}`,

```text
ell=(mu*c/2+delta_c, mu).
```

When `c in B`, `delta_c=0`, recovering the Cycle 23 form
`ell=mu*(xi+c/2)`.

## Banked Lemma 2: `D=N(ell)kappa`

Let the conjugate in `A` be induced by `xi -> -c-xi`. Direct expansion gives
the master identity

```text
x * ybar = P_E(x,y) - (x wedge y) xi.
```

Apply this with `y=ell`. Then

```text
u*ellbar = P_E(u,ell) - (u wedge ell)xi,
b*ellbar = P_E(b,ell) - (b wedge ell)xi.
```

Taking the coordinate wedge of these two products yields

```text
(u*ellbar) wedge (b*ellbar)
  = (ell wedge b)P_E(u,ell)+P_E(b,ell)(u wedge ell)
  = D.
```

Multiplication by `ellbar` is an `F`-linear endomorphism of the rank-two
algebra `A`, so it scales the wedge by its determinant, namely `N(ell)`.
Therefore

```text
D=N(ell) kappa.
```

In coordinates,

```text
N(ell)=P_E(ell,ell)=delta_c^2-mu^2 w.
```

Since

```text
ell=[prod_{a in F_p}(X-a)]_E,
```

multiplicativity of the norm gives the more useful resultant form

```text
N(ell)=prod_{a in F_p} N([X-a]_E)=prod_{a in F_p} E(a).
```

## Consequence: The Source-Valid `D=0` Branch Is Empty Off `R0`

For a source-valid residue-line datum over `D=F_p`, the denominator `E` is
nonzero on every `a in F_p`. Hence

```text
prod_{a in F_p} E(a) != 0.
```

Therefore

```text
N(ell) != 0.
```

Off `R0`, `kappa != 0`, so the factorization `D=N(ell)kappa` gives

```text
D != 0.
```

Thus the system

```text
D=0,
off R0,
E nonzero on D=F_p
```

has no points in this restricted `t=2,j=3` calculation. The additional Cycle 24
conditions

```text
c notin B,
E separated,
Delta1==0,
c_b=-Q_E(b)/kappa != 0,
W_{n-1} != 0
```

are never reached.

If the denominator-nonvanishing hypothesis is temporarily ignored, the same
identity says `D=0` off `R0` exactly when `E` has an `F_p`-root. Such a root is
also a root of `E^tau`, so it violates the separated convention
`gcd(E,E^tau)=1`. This is a useful cross-check, but the source-valid
denominator condition is the cleaner reason the branch is empty.

## Route Cut

The live wall

```text
W-F1-AA-RES-T2J3-D-KERNEL-NONSPLIT-C
```

is cut. The previous `D=0` route is gone for source-valid off-`R0`
denominators in the restricted `D=F_p`, `t=2`, `j=3` window.

The next target should return to the non-`D=0` determinant-split branch:

```text
W-F1-AA-RES-T2J3-QZERO-DETM-NONZERO-SPLIT
```

There, `D!=0` and `det M=(c_b/kappa^2)D` are available, and the remaining task
is to decide whether the Cycle 16 determinant polynomial `Q(z_0,z_1)` can still
vanish on a source-valid distinct-split slope family large enough to give a
`Theta(q_line)` seed, or whether `Q==0` forces only `O(p)` slopes.

## Local Checker

Added:

```text
local_checks/20260618_cycle24_dkernel_norm_identity_check.py
```

The checker verifies, in deterministic tiny-field samples for `p=3,5,7,11`,
the identities

```text
ell=mu*(xi+c/2)+delta_c,
D=N(ell)kappa,
N(ell)=prod_{a in F_p} E(a)=delta_c^2-mu^2(c^2/4-d).
```

It also checks experimentally that no source-valid denominator nonzero on
`D=F_p` gives `D=0` off `R0`. This is experimental consistency evidence only;
the banked result is the algebraic proof above.

Run output:

```text
p=3: checked=243, source-valid off-R0 samples=171, separated off-R0 samples=162, D=0 off-R0 samples=72, every D=0 has base root=True
p=5: checked=2500, source-valid off-R0 samples=2040, separated off-R0 samples=2000, D=0 off-R0 samples=460, every D=0 has base root=True
p=7: checked=9604, source-valid off-R0 samples=8316, separated off-R0 samples=8232, D=0 off-R0 samples=1288, every D=0 has base root=True
p=11: checked=58564, source-valid off-R0 samples=53460, separated off-R0 samples=53240, D=0 off-R0 samples=5104, every D=0 has base root=True
PASS: Cycle 24 ell, D=N(ell)kappa, and resultant identities verified.
```

## Rejected Overclaims

Do not bank these statements from the recovered answer:

- any corrected-reserve conclusion;
- any full MCA bound;
- any `q_gen` consequence;
- any protocol denominator saving;
- any list-decoding, line-decoding, CA, curve-MCA, or SNARK consequence;
- any claim that the Proximity Prize is solved or disproved;
- any claim that finite checker output is proof.
