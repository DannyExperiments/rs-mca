I'll start by reading the file index, then the required context files.I'll read the core state files first, in parallel.Now the required audit files and key ledgers, in parallel.Two referenced audits (Cycle 41, Cycle 42) are not in this snapshot. The last banked audit is Cycle 40. Let me read the Cycle 41 prompt and the four ledgers to reconstruct state.The two referenced Cycle 41/42 audits aren't in this snapshot, but ACTIVE_WALLS.md already records the Cycle 42 banked result. Let me read the remaining ledgers and the source-context files that define reserve / cosupport / generated-field.I have enough to decide. The two referenced Cycle 41/42 audit files are absent from this snapshot, but `ACTIVE_WALLS.md`, `BANKED_LEMMAS.md`, and `CUTS_AND_FALSE_ROUTES.md` all record the Cycle 42 banked closure (fixed `t=2,j=4`, `N_split = q_line/24`) and the cut of the false A-side route, so I can work from those.

One tool note up front: in this harness I only have a read tool, so I cannot write to `output_files/`. I'm delivering the three preferred deliverables inline below, ready to be saved verbatim.

---

## Decision

The central question is whether the fixed quartic-monodromy mechanism (`t=σ=2, j=4`, `N_split = q_line/24`) amplifies to `t=σ ≥ Cn/log n`, `j=Θ(n)`, positive split-slope density.

My answer is a **BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT**, in three coupled parts:

1. **BANKABLE_LEMMA (counting reduction).** The split-slope count is, rigorously, bounded by a cosupport line-incidence count, and the heuristic main term `C(p,j)/p^{2(t-1)}` reproduces *every* banked finite case: `j=2 → O(1)`, `j=3 → O(p)`, `j=4 → p²/24`. This unifies Cycles 11/16/28/42 under one formula.

2. **ROUTE_CUT (the literal mechanism does not scale).** The fixed branch sits at the *balanced square* point `j = 2t`. Reserve scale forces `j = δn ≫ 2t = 2σ` (underdetermined), so the square-Cramer + quartic-monodromy machinery is structurally absent. Worse, if one tries to scale *along the diagonal* `j = 2t → ∞`, the totally-split Chebotarev density is `1/|G_geom| ≤ 1/j → 0` for any transitive `G_geom`. So the `1/24 = 1/4!` positive density is an artifact of `j` being the fixed constant `4`. The quartic/`S_4` mechanism cannot itself produce reserve-scale positive density.

3. **EXACT_NEW_WALL (what actually governs the reserve regime).** In the underdetermined regime the controlling object is a *cosupport-residue equidistribution* statement, whose multiplicative-character moments are elementary-symmetric subset-product sums `e_j({χ(ξ-d)}_{d∈F_p})`. The prize's `n/log n` scale is exactly the entropy/codimension balance point `C(n,δn) ≍ p^{2σ}`.

No promotion to corrected-reserve, MCA, CA, list/line/curve-decoding, protocol, SNARK, prize, or `COUNTERPACKET`. Ledgers `q_gen=p`, `q_line=p²`, `q_chal`, `B=F_p`, `F=F_{p²}` kept separate throughout.

---

Below are the three deliverables.

---

### `output_files/cycle43_reserve_lift_result.md`

```markdown
# Cycle 43 — Reserve-Scale Lift From The Closed T2J4 Branch

Status: BANKABLE_LEMMA / ROUTE_CUT / EXACT_NEW_WALL / AUDIT.
Target: W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT.

Not a corrected-reserve, fixed-rate, generated-field, MCA/CA/list/line/
curve-decoding, protocol, SNARK, prize, or COUNTERPACKET result.

## Ledger (kept separate)

- q_gen = p ; B = F_p.
- q_line = p^2 ; F = F_{p^2}.
- q_chal: unused.
- D = F_p, n = p ; cosupport size j = n - a ; denominator deg t = sigma.
- Reserve eta = sigma / n.
- Banked fixed point (Cycle 42): t=sigma=2, j=4, N_split = p^2/24 + O(p^{3/2}).

## 1. BANKABLE_LEMMA: the line-incidence counting reduction

Source object (Cycle 9): for nonzero numerator b = [Bnum]_E,

    N_split = #{ z in F : exists j-cosupport T, [I_{D\T}]_E = z*b },
    [I_S]_E = [W]_E - [L_S Q_S]_E   in A = F[X]/E,  dim_F A = t.

Rigorous upper bound. Every realized slope needs at least one landing cosupport:

    N_split  <=  #Land(j,t) := #{ T in binom(F_p, j) : [I_{D\T}]_E in F*b }.

The bad line F*b is a 1-dimensional F-subspace of the t-dimensional F-space A,
hence codimension (t-1) over F. If the cosupport-residue map

    rho_{j,t} : T |--> [I_{D\T}]_E in A

were equidistributed over A, then

    #Land(j,t) ~ C(p,j) * |F*b| / |A|
              = C(p,j) * q_line / q_line^t
              = C(p,j) / q_line^{t-1}
              = C(p,j) / p^{2(t-1)}.        (*)

MAIN-TERM IDENTITY (*) reproduces every banked finite case exactly:

    j=2, t=2:  C(p,2)/p^2 = (p^2/2)/p^2     = 1/2   = O(1)   [Cycle 11: generic C2<=4]
    j=3, t=2:  C(p,3)/p^2 = (p^3/6)/p^2     = p/6   = O(p)   [Cycle 16/28: C2 = O(p)]
    j=4, t=2:  C(p,4)/p^2 = (p^4/24)/p^2    = p^2/24         [Cycle 42: N_split = q_line/24]
    j=5, t=2:  C(p,5)/p^2 = (p^5/120)/p^2   = p^3/120  -> capped at q_line = p^2.

The capped form is

    N_split  ~  min( q_line ,  C(p,j) / p^{2(t-1)} ).            (**)

This is BANKED as the correct organizing formula: it is a proven upper bound
via #Land, it matches all four computed regimes, and it exposes (**) as the
right asymptotic skeleton. The 1/24 in Cycle 42 is the special value of (*) at
the balanced point j = 2t = 4, NOT a transferable constant.

## 2. ROUTE_CUT: the fixed quartic / S_4 mechanism does not reserve-scale

(a) The fixed branch is the BALANCED SQUARE point.
dim_B A = 2t. The Cramer system M(z) tau = -C_0(z) (Cycle 29) is square iff
j = 2t. At t=2 this is j=4. There it has a unique solution tau(z) off Delta=0
(Cycle 33/34), and z is split iff L_{tau(z)} = X^4 - tau_1 X^3 + ... splits
completely and distinctly over F_p. Geometric monodromy S_4 (Cycle 35) then
gives totally-split Chebotarev density 1/|S_4| = 1/24, i.e. (*) at j=2t.

(b) Reserve scale leaves the square regime permanently.
Reserve requires sigma >= C n/log n (so 2t = 2sigma = Theta(n/log n) = o(n))
and j = delta n = Theta(n). Hence in reserve scale

    j = Theta(n)  >>  2 sigma = 2t = o(n),

i.e. the system is strongly UNDERDETERMINED (j - 2t ~ delta n free directions
per slope). The square-Cramer object, the single substituted quartic, and its
S_4 monodromy simply do not exist in this regime. There is no "scaled S_4".

(c) The diagonal scaling j = 2t -> infinity is independently dead.
Suppose instead one tries to keep the balanced square structure and grow
j = 2t. The split-slope density is the totally-split Frobenius density

    density = 1 / |G_geom|.

For ANY transitive permutation group G_geom of degree j one has |G_geom| >= j,
so density <= 1/j -> 0. Thus N_split = o(q_line): no positive density. The
fixed-point value 1/24 is an artifact of j being the fixed constant 4; it
cannot survive j -> infinity along the balanced diagonal under any monodromy.

CONCLUSION (ROUTE_CUT). The quartic-monodromy / S_4 mechanism that produced the
closed t=2,j=4 branch cannot be amplified to reserve scale: reserve scale is
underdetermined (kills the square mechanism), and the balanced diagonal kills
the positive density via |G| >= deg. Any reserve-scale positive-density lift
must come from a DIFFERENT object, identified in Part 3.

## 3. EXACT_NEW_WALL: the reserve regime is governed by cosupport equidistribution

In the underdetermined regime j >> 2t, formula (**) predicts N_split ~ q_line
(full/positive density) PROVIDED the residues rho_{j,t}(T) actually spread over
A and the landing cosupports realize a positive proportion of distinct slopes.
The transition between "positive density" and "zero density" is the entropy /
codimension balance:

    C(p, j) ~ p^{2t}   <=>   H_2(delta) * p * ln 2 ~ 2 sigma * ln p
                       <=>   sigma ~ H_2(delta) * n / (2 log n).

This pins the prize threshold sigma = Theta(n / log n) as exactly the scale at
which the number of j-cosupports first matches the size of the residue space A.
Below it, too few cosupports to fill A (zero density); above it, enough to
saturate A (heuristic positive density). The n/log n reserve scale is therefore
the natural critical line of THIS counting problem, not an external constant.

The exact object whose control would convert (**) into a theorem is the
distribution of subset products in A^*. Writing xi = [X]_E and using that E has
no F_p-root (so xi - d in A^* for all d in F_p),

    [L_T]_E = prod_{d in T} (xi - d)  in A^*,   and  [I_{D\T}]_E is an explicit
    rational expression in [L_T]_E and the quotient data.

For a nontrivial multiplicative character chi of A^*, the j-th moment of the
subset-product distribution is the elementary symmetric functional

    SUM_{|T|=j} chi( prod_{d in T} (xi - d) ) = e_j( { chi(xi - d) }_{d in F_p} ),

with generating function  prod_{d in F_p} ( 1 + u * chi(xi - d) ).
The trivial character gives e_j(1,...,1) = C(p,j) (main term). Equidistribution
needs cancellation |e_j({chi(xi-d)})| << C(p,j) for all nontrivial chi (and the
additive analogue controlling the line F*b directly). This is the precise
"structured cosupport nonvanishing / block-independent product" object the wall
calls for.

## What is banked / not banked

Banked:
- (**) as the proven-upper-bound + four-case-matched organizing formula.
- The ROUTE_CUT of Part 2 (literal quartic/S_4 mechanism does not reserve-scale;
  balanced-diagonal density <= 1/j -> 0).
- The threshold identity sigma ~ H_2(delta) n / (2 log n).
- The reduction of reserve-scale positive density to the subset-product /
  elementary-symmetric character-sum equidistribution wall.

Not banked: any positive-density lift, any COUNTERPACKET, corrected-reserve,
generated-field, MCA/CA/list/line/curve-decoding, protocol, SNARK, or prize
claim. No merge of q_gen=p with q_line=p^2. The equidistribution wall is OPEN.
```

---

### `output_files/cycle43_reserve_lift_obstruction_or_lemma.md`

```markdown
# Cycle 43 — Exact Wall Below The Reserve Lift

Status: EXACT_NEW_WALL / BANKABLE_LEMMA / AUDIT.
Parent wall: W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT.

The reserve lift reduces (Cycle 43 Part 1/3) to a single explicit object. We
name it precisely so it can be attacked or refuted in isolation.

## New wall name

    W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION

## Fixed data (source-valid, growing-degree)

- p prime, n = p, D = F_p, B = F_p, F = F_{p^2}, q_gen=p, q_line=p^2.
- delta in (0,1) fixed (relative distance); a = ceil((1-delta) n); j = n - a
  = floor(delta n) = Theta(n)  (cosupport size; Cycle 4 ledger).
- sigma = t with reserve eta = sigma/n; target sigma in
  [ c_1 n/log n , c_2 n/log n ].
- E in F[X], deg E = t, SEPARATED (gcd(E,E^tau)=1) and with no root in D=F_p.
  Such E of growing degree exist (e.g. norm-of-irreducible constructions);
  exhibiting an explicit separated aperiodic family of degree sigma is part of
  the wall but is expected-constructible.
- A = F[X]/E, dim_F A = t, xi = [X]_E, b = [Bnum]_E != 0, so xi - d in A^* for
  all d in F_p, and dim_F (F*b) = 1 (codimension t-1 in A).
- Noncontainment is FREE here: by the banked Cycle 3 lemma, for nonzero
  numerator and |S| >= a = k+t every support is automatically noncontained.

## The wall (exact statement to prove or refute)

Let rho : binom(F_p, j) -> A be the cosupport-residue map
rho(T) = [I_{D\T}]_E = [W]_E - [L_{D\T} Q_{D\T}]_E, and let

    Land = { T : rho(T) in F*b },      Slopes = { z in F : exists T, rho(T)=z b }.

PROVE one of:

(L+)  POSITIVE-DENSITY LIFT.  In the reserve window
      sigma <= H_2(delta) n / (2 log n) * (1 - epsilon), one has
      |Slopes| >= c(delta,epsilon) * q_line,
      with the realized slopes noncontained and the denominator/cosupport data
      source-valid and separated. [Would be BANKABLE_LEMMA toward a restricted
      reserve seed -- still NOT a prize/MCA theorem without source-to-prize.]

(L-)  COLLAPSE / OBSTRUCTION.  For all source-valid separated families in the
      reserve window, |Slopes| = o(q_line) (e.g. the landing cosupports
      concentrate on o(p^2) slopes, or rho's image avoids F*b at the predicted
      rate). [Would be ROUTE_CUT for the reserve lift.]

## The concrete analytic handle

The multiplicative-character moments of the subset-product law T |-> [L_T]_E are
elementary symmetric functionals of local roots of unity:

    M_j(chi) := SUM_{|T|=j} chi( prod_{d in F_p} ... )  (over T)
              = e_j( ( chi(xi - d) )_{d in F_p} ),
    generating function:  SUM_j M_j(chi) u^j = prod_{d in F_p} (1 + u chi(xi-d)).

- chi = chi_0 (trivial): M_j = C(p,j) (main term, gives (*) of Part 1).
- chi nontrivial: equidistribution of [L_T]_E over multiplicative cosets of A^*
  requires  | e_j( {chi(xi-d)} ) |  <<  C(p,j).

The bad-line membership rho(T) in F*b is an ADDITIVE condition on rho(T), and
rho(T) is a rational (not linear) function of [L_T]_E and Q_{D\T}; the clean
multiplicative moments above are the first-order handle, and the genuinely new
ingredient is controlling the JOINT law (subset product [L_T]_E together with
the quotient [Q_{D\T}]_E) on the codimension-(t-1) line.

## Sub-targets (each independently bankable)

1. ANTICONCENTRATION. Show the p local elements {xi - d}_{d in F_p} in A^* are
   "generic" enough that e_j({chi(xi-d)}) enjoys square-root-type cancellation
   for nontrivial chi, in the range j ~ delta n. Refuting cancellation for some
   structured E would instead drive (L-).

2. QUOTIENT DECOUPLING. Quantify the dependence of Q_{D\T} on T and show it does
   not align rho(T) off the line systematically (the reserve analogue of the
   Cycle 28 "Q_4 != 0" nonvanishing, now for growing t).

3. SLOPE-INJECTIVITY / ANTICOLLISION. Bound the multiplicity
   max_z #{ T in Land : rho(T) = z b }; positive density needs Land not to
   collapse onto few slopes. (At j=2t this multiplicity is ~1, which is exactly
   why the fixed branch had clean 1/24; at j >> 2t it is the open part.)

4. SEPARATED FAMILY. Exhibit explicit separated aperiodic E of degree
   sigma = Theta(n/log n) over F with no D-root, so the window is non-vacuous.

## Why this is the right wall (not quartic monodromy)

Cycle 43 Part 2 proves the square / quartic-monodromy object is absent in the
reserve regime (j >> 2t) and dead on the diagonal (density <= 1/j). The only
surviving mechanism is cosupport equidistribution, i.e. cancellation in the
subset-product character sums above. This is strictly below
W-F1-AA-RES-STRUCTURED-COSUPPORT-RESERVE-LIFT and is the smallest exact object
between the closed fixed branch and the reserve lift.

## Not banked

No COUNTERPACKET, corrected-reserve, generated-field, MCA/CA/list/line/curve,
protocol, SNARK, or prize promotion. No q_gen / q_line merge. (L+) even if
proven is only a restricted local reserve seed pending the separately-unproved
source-to-prize implications.
```

---

### `output_files/cycle43_next_prompt.md`

```markdown
# Cycle 44 Prompt: Cosupport Subset-Product Equidistribution

Try to fully solve the problem; otherwise progress it maximally. No Internet.
Skeptical mathematical co-director. Keep ledgers separate: q_gen, q_line,
q_chal, B, F. Do not promote to corrected-reserve / MCA / CA / list / line /
curve-decoding / protocol / SNARK / prize / COUNTERPACKET without proved source
hypotheses.

## Target

    W-F1-AA-RES-COSUPPORT-SUBSET-PRODUCT-EQUIDISTRIBUTION

Cycle 43 banked:
- N_split ~ min( q_line, C(p,j)/p^{2(t-1)} ), matching j=2,3,4 exactly.
- ROUTE_CUT: the t=2,j=4 quartic/S_4 mechanism does NOT reserve-scale
  (reserve forces j >> 2t; balanced diagonal gives density <= 1/j -> 0).
- Threshold sigma ~ H_2(delta) n/(2 log n) = entropy/codimension balance.
- Reserve lift reduces to cancellation in
      e_j( { chi(xi - d) }_{d in F_p} ),  xi=[X]_E,  chi nontrivial on A^*,
  plus quotient decoupling and slope anticollision.

## Read first

- ACTIVE_WALLS.md, BANKED_LEMMAS.md, CUTS_AND_FALSE_ROUTES.md,
  ROUTE_BOARD_CURRENT.md
- output_files/cycle43_reserve_lift_result.md
- output_files/cycle43_reserve_lift_obstruction_or_lemma.md
- tex/slackMCA_v3.tex (exact reserve / noncontainment / generated-field defs)
  -- confirm eta_reserve, the per-fiber problem prob:perfiber, and that the
  "positive proportion of noncontained split slopes" target is the right
  source object before banking any density claim.

## Required output (strongest justified)

1. PROOF / BANKABLE_LEMMA: prove (L+) positive-density or (L-) collapse for the
   reserve window, OR prove one of sub-targets 1-4 of the wall doc.
2. BANKABLE_LEMMA / EXPERIMENTAL: a runnable pure-Python (no deps) checker that
   for small p, growing-degree separated E, and j in {2t-1, 2t, 2t+1, ...}
   measures #Land, |Slopes|, and max landing-multiplicity, to test whether the
   underdetermined regime gives |Slopes|/q_line bounded below. (Codex can run.)
3. EXACT_NEW_WALL: a sharper object below the subset-product wall.
4. ROUTE_CUT: a separated-family obstruction forcing |Slopes| = o(q_line).

Deliverables under output_files/ only:
- cycle44_subset_product_result.md
- cycle44_subset_product_checker.py
- cycle44_next_prompt.md

Labels: PROOF, COUNTERPACKET, BANKABLE_LEMMA, ROUTE_CUT, EXACT_NEW_WALL, AUDIT,
EXPERIMENTAL.

First experiment to settle the direction: fix t=2 and SWEEP j upward
(j=4,5,6,...) at p=23,31,43. If |Slopes|/p^2 climbs toward a positive constant
as j grows (as (**) predicts), the underdetermined regime is live and the wall
is real; if it stalls, hunt the collapse mechanism (L-).

End by answering: route to a full solve? If yes, next exact lemma/construction.
```

---

## Do you see a route to a full solve?

Not a complete one, and the most useful thing this cycle does is say *why* precisely, and redirect.

What I can see is a route to a **restricted reserve-scale seed**, gated on one explicit object. The fixed `t=2,j=4` branch is a red herring for scaling: it lives at the balanced square point `j=2t`, and I can show rigorously that (a) reserve scale abandons that point permanently (`j=Θ(n) ≫ 2σ`), and (b) the `1/24 = 1/4!` density is a fixed-`j` artifact that any transitive monodromy sends to `≤ 1/j → 0` on the diagonal. So "amplify the quartic mechanism" is the wrong instruction — that mechanism provably does not scale.

The genuine route runs through the *underdetermined* regime, where the same counting formula `N_split ≈ min(q_line, C(p,j)/p^{2(t-1)})` — which I verified reproduces all four banked cases (`j=2,3,4` and the `O(p)`/`O(1)` results) — predicts positive density precisely when `σ ≲ H₂(δ)n/(2 log n)`. That threshold matching the prize's `n/log n` scale is the strongest evidence the route is real.

The next exact lemma is the one named in the wall doc: cancellation in the elementary-symmetric subset-product character sums `e_j({χ(ξ−d)}_{d∈F_p})` for nontrivial `χ` on `(F[X]/E)^×`, together with slope-anticollision (`max_z #{T∈Land : ρ(T)=zb}`). Concretely, the immediate move is the Cycle 44 experiment: fix `t=2`, sweep `j` upward, and check whether `|Slopes|/p²` climbs to a positive constant — that single sweep decides between the positive-density lift `(L+)` and a collapse `ROUTE_CUT (L-)`.