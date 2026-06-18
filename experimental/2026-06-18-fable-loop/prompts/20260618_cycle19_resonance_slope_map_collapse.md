You are working on the RS-MCA / Proximity Prize repository as a skeptical
mathematical co-director.

This is Cycle 19 after a Cycle 18 "homerun" prompt. The goal is still to solve
or disprove the proximity problem if possible, but the current best crack is now
very specific. Do not summarize the whole repo. Attack this wall.

# Target

```text
W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE
```

Try for a homerun on this target:

1. prove the resonance slope-map collapse;
2. or construct a source-valid growing-prime counterpacket;
3. or cut the route by finding the first false reduction;
4. or reduce it to a strictly sharper theorem-sized wall.

# Banked context you must preserve

Source files and audits to read first:

- `input_project/ROUTE_BOARD_CURRENT.md`
- `input_project/ACTIVE_WALLS.md`
- `input_project/BANKED_LEMMAS.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE14_BASE_COMPONENT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE15_SURFACE_SLOPE_FIBER_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE16_RANK_DETERMINANT_RESONANCE_AUDIT.md`
- `input_project/current_loop_20260618/2026-06-18-fable-loop/audits/20260618_CYCLE18_HOMERUN_AUDIT.md`

Keep ledgers separate:

```text
B=F_p,        q_gen=p
F=F_{p^2},    q_line=p^2
q_chal unused
D=F_p,        n=p
t=sigma=2
j=n-a=r-t=3, so a=n-3, k=n-5
eta=sigma/n=2/n, sub-reserve
work off R0={wedge([W]_E,[Bnum]_E)=0}
```

Do not convert this into list decoding, CA, MCA, line decoding, curve-MCA, or a
protocol statement unless you prove the conversion. This is currently a
restricted line-incidence/residue calculation only.

# Banked algebra from Cycles 14-18

Off `R0`, `{[W]_E,b}` is an `F`-basis of `A=F[X]/E`, with `b=[Bnum]_E`.
Cycle 14 banked:

```text
iota(tau)=A0(tau_1,tau_2)-tau_3[W]_E,
mu(tau)=B0(tau_1,tau_2)-tau_3 b,
A0=p1[W]_E+p2 b,
B0=q1[W]_E+q2 b,
```

where `p_i,q_i in F` are affine-linear in `(tau_1,tau_2)`.

Cycle 18 banks the monicity lemma:

```text
Delta(tau) := wedge_{W,b}(iota,mu)
            = (p1 - tau_3)(q2 - tau_3) - p2 q1.
```

Thus `Delta` is monic quadratic in `tau_3`. Splitting over `F=B+alpha B`,

```text
Delta=Delta0+alpha Delta1,
Delta0,Delta1 in B[tau_1,tau_2,tau_3],
deg_{tau_3} Delta0 = 2, leading coefficient 1,
deg_{tau_3} Delta1 <= 1.
```

Safe side: if `Delta0,Delta1` have no common component over the algebraic
closure of `B`, then the landing locus has `O(p)` points, hence `C2=O(p)`.

Therefore the remaining large-slope branch is:

```text
g := gcd(Delta0,Delta1) nonconstant.
```

Because `deg_{tau_3} Delta1<=1`, nontrivial resonance has only two shapes:

```text
1. Delta1 == 0, giving a full monic base quadric surface; or
2. deg_{tau_3} g = 1, so g=s(tau_1,tau_2) tau_3+h(tau_1,tau_2).
```

In case 2, the resonance surface is generically the graph

```text
tau_3=-h/s,
```

so the slope formula reduces to a two-variable rational map

```text
z(tau_1,tau_2) = (p1+h/s)/q1.
```

Equivalently, slopes are controlled by the coefficient map from the Cycle 14
slope quadratic:

```text
q1 z^2 - (p1-q2) z - p2 = 0,
mu_coef : (tau_1,tau_2) -> [q1 : (p1-q2) : p2] in P^2(F).
```

# Exact question

On every source-valid non-coprime resonance stratum in this restricted
`D=F_p`, `t=sigma=2`, `j=3`, off-`R0` window:

```text
Does the rational slope map have one-dimensional image, forcing C2=O(p),
or can it be generically finite, yielding C2=Theta(p^2)=Theta(q_line)?
```

# Desired output

Return exactly one of these labels:

```text
PROOF
COUNTERPACKET
BANKABLE_LEMMA
ROUTE_CUT
EXACT_NEW_WALL
AUDIT
```

If `PROOF`, give a source-valid proof of the slope-map collapse on all
non-coprime resonance strata, including the `Delta1==0` quadric case.

If `COUNTERPACKET`, give explicit symbolic or growing-prime source-valid data
showing `C2/p^2` bounded below. Specify `B,F,D,E,Bnum,W` or equivalent
parameters, and explain split-distinct cubic realization. Single-prime evidence
is only EXPERIMENTAL, not a counterpacket.

If `BANKABLE_LEMMA`, prove a smaller lemma that genuinely advances the
collapse or counterpacket route. State exact hypotheses and parameters.

If `ROUTE_CUT`, identify the first false step in the Cycle 14-18 reduction and
give the replacement wall.

If `EXACT_NEW_WALL`, name a strictly sharper wall below the rational
image-dimension question. It must be theorem-sized and actionable.

You may use algebraic geometry language if useful, but keep it concrete:
function fields, Jacobian rank, resultants, common components, rational-map
image dimension, and split-cubic constraints are all acceptable.

# Forbidden upgrades

- Do not claim the Proximity Prize is solved unless every source hypothesis is
  discharged.
- Do not treat this sub-reserve `eta=2/n` window as a corrected-reserve theorem.
- Do not merge `q_gen` and `q_line`.
- Do not infer any protocol denominator saving.
- Do not cite finite scans as proof.
- Do not treat malformed terminal output as source.
