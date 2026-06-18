# Cycle 18 Audit: Homerun Monicity Lemma And Resonance Slope-Map Wall

Status: BANKABLE_LEMMA / EXACT_NEW_WALL / AUDIT.

Primary classification: EXACT_NEW_WALL.

Secondary classification: BANKABLE_LEMMA, restricted to the monicity lemma and
the already-safe complete-intersection side described below.

## Run

- Run id: `2026-06-18T07-35-54-758Z-cycle18-homerun-full-solve-big-leap-5b378eb7`
- Run dir:
  `/Users/danielcabezas/packy-fable-ui/projects/rs-mca-proximity-prize-research/runs/2026-06-18T07-35-54-758Z-cycle18-homerun-full-solve-big-leap-5b378eb7`
- Lane: isolated RS-MCA VS Code credited terminal ads lane.
- Launcher: `/Users/danielcabezas/packy-fable-ui/.codex-vscode-launchers/rs-mca-current`
- App workaround: private no-xattr VS Code copy at
  `/Users/danielcabezas/packy-fable-ui/.vscode-app-sandbox/Visual Studio Code.app`.
- Harness result: `ok=false`,
  `classification=HARNESS_MALFORMED_VISIBLE_TERMINAL`,
  `answerSource=terminal_tui`, `terminalMalformedVisible=true`.
- `response.md`: absent.
- Audited provenance artifact: readable structured Claude JSONL recovery copied
  to `../raw/20260618_CYCLE18_HOMERUN_RECOVERED_CLAUDE_JSONL.md`.
- Malformed visible-terminal text is preserved separately and is not banked as
  mathematics.

## Verdict

Cycle 18 did not solve or disprove the Proximity Prize and did not close F1. It
does contain a source-backed algebraic reduction in the restricted
`D=F_p`, `t=sigma=2`, `j=3`, off-`R0` toy window:

1. the landing determinant is monic quadratic in `tau_3` after changing to the
   `{[W]_E,b}` basis from Cycle 14;
2. after splitting `Delta=Delta0+alpha Delta1`, the base component `Delta0` is
   monic degree `2` in `tau_3`, while `deg_{tau_3} Delta1<=1`;
3. the remaining resonance obstruction is therefore sharper than the Cycle 16
   rank-determinant wall: it is a two-variable rational slope-image problem on
   the non-coprime `gcd(Delta0,Delta1)` branch.

Bank the monicity lemma and the sharpened exact wall. Do not bank the proposed
collapse of the rational slope map; that is the next theorem-sized target.

Confidence: moderate. The monicity lemma follows from already-banked Cycle 14
identities. The final collapse route is plausible but unproved.

## Field And Parameter Ledger

- `B=F_p`, `q_gen=p`.
- `F=F_{p^2}`, `q_line=p^2`.
- `q_chal` unused.
- `D=F_p`, so `n=p`.
- `t=sigma=2`.
- `j=n-a=r-t=3`; hence `a=n-3`, `k=n-5`.
- `eta=sigma/n=2/n`, sub-reserve.
- Work is off `R0={ wedge([W]_E,[Bnum]_E)=0 }` unless explicitly stated.
- This is a line-incidence/residue calculation only. It is not list decoding,
  CA, MCA, line decoding, curve-MCA, or a protocol ledger statement.

## Source-Checked Inputs

Cycle 14 banked, off `R0`, that `{[W]_E,b}` is an `F`-basis of
`A=F[X]/E`, with `b=[Bnum]_E`, and

```text
iota(tau)=A0(tau_1,tau_2)-tau_3[W]_E,
mu(tau)=B0(tau_1,tau_2)-tau_3 b,
A0=p1[W]_E+p2 b,
B0=q1[W]_E+q2 b,
```

where `p_i,q_i in F` are affine-linear in `(tau_1,tau_2)`.

Cycle 15/16 banked the affine fiber equation

```text
L_z(tau)=iota(tau)-z mu(tau)=0
```

and the determinant-consistency safe side: if the Cycle 15 polynomial
`Q(z_0,z_1)` is not identically zero, then `C2<=4p=O(p)=O(n)` in this
restricted window.

## Bankable Lemma: Monicity In `tau_3`

In the `{[W]_E,b}` coordinate determinant,

```text
iota = (p1 - tau_3)[W]_E + p2 b,
mu   = q1[W]_E + (q2 - tau_3)b.
```

Therefore

```text
Delta(tau) := wedge_{W,b}(iota,mu)
            = (p1 - tau_3)(q2 - tau_3) - p2 q1.
```

As a polynomial in `tau_3`, `Delta` is monic of degree `2` with leading
coefficient `1 in B`. Splitting over `F=B+alpha B`,

```text
Delta=Delta0+alpha Delta1,
Delta0,Delta1 in B[tau_1,tau_2,tau_3],
```

gives

```text
deg_{tau_3} Delta0 = 2, with leading coefficient 1,
deg_{tau_3} Delta1 <= 1.
```

This is a proof-level algebraic consequence of the Cycle 14 affine forms, not
finite experimental evidence. It remains restricted to the current toy window
and off-`R0` basis condition.

## Safe-Side Corollary

If `Delta0` and `Delta1` have no common component over the algebraic closure of
`B`, then the landing locus

```text
{Delta0=0} cap {Delta1=0} subset B^3
```

has dimension at most `1` and bounded degree. Hence it has `O(p)` `B`-points,
and the slope set satisfies `C2=O(p)=O(n)`.

This rephrases the Cycle 13/16 safe side in the monic determinant coordinates.
Use the algebraic-closure version of the coprimality condition in future proof
work; a bare finite-field gcd test is not by itself the cleanest statement of
geometric coprimality.

## Sharpened Exact Wall

The remaining large-slope branch is the non-coprime resonance branch:

```text
g := gcd(Delta0,Delta1) nonconstant.
```

Since `deg_{tau_3} Delta1<=1`, every nontrivial common factor has only the
following shapes:

```text
1. Delta1 == 0, giving a full monic base quadric surface; or
2. deg_{tau_3} g = 1, so g=s(tau_1,tau_2) tau_3+h(tau_1,tau_2).
```

In case 2, the resonance surface is generically the graph

```text
tau_3 = -h/s,
```

so the slope formula reduces to a two-variable rational map

```text
z(tau_1,tau_2) = (p1+h/s)/q1,
```

where defined. Equivalently, slopes are controlled by the coefficient map

```text
mu_coef : (tau_1,tau_2) -> [q1 : (p1-q2) : p2] in P^2(F)
```

from the Cycle 14 slope quadratic

```text
q1 z^2 - (p1-q2) z - p2 = 0.
```

The live wall is therefore sharpened to:

```text
W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE
```

Target:

```text
On every source-valid non-coprime resonance stratum in the restricted
D=F_p, t=sigma=2, j=3, off-R0 window, prove that the rational slope map above
has one-dimensional image, forcing C2=O(p), or exhibit a growing-p source-valid
family where it is generically finite and C2=Theta(p^2)=Theta(q_line).
```

## What Is Not Banked

Do not bank:

- a full solution or disproof of the Proximity Prize;
- a proof of `conj:B`;
- a proof that the resonance slope map collapses;
- a `Theta(q_line)` counterpacket;
- any statement above corrected reserve;
- any `q_gen` conclusion from this `q_line` toy window;
- any conversion to list decoding, CA, MCA, support-wise line-MCA,
  line-decoding, curve-MCA, or protocol ledgers;
- malformed visible-terminal text as theorem content.

## Next Prompt Target

Ask the next worker to attack exactly:

```text
W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE
```

and require one of:

- a proof that every source-valid non-coprime resonance stratum has
  one-dimensional slope image;
- a source-valid growing-prime counterpacket with `C2/p^2` bounded below;
- a route cut showing that the monicity reduction does not apply to the
  source object;
- a sharper exact wall below the rational image-dimension question.
