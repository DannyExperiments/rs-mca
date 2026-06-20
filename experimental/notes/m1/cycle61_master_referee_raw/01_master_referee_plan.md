# 1. Executive Decision

**Primary route: D — scalar-list apolar complete-intersection route, not the circuit-transversal route.**

Start with the first nontrivial scalar stratum
[
\deg A=\sigma+1,\qquad \deg B=j=r-\sigma,
]
replace the loose resultant ledger by an exact generalized-Jacobian fiber formulation, and then prove or kill a quotient-conditioned finite local limit.

**Backup route: C — the (t=1) MCA generalized-Jacobian base case.**

Start with
[
t=1,\qquad \deg A=\sigma,\qquad \deg B=j,
]
but include the external-color map. Counting supports alone does not count MCA slopes.

**Confidence**

* D is the correct immediate priority: **0.80**.
* C is the correct backup: **0.65**.
* The repaired program eventually reaches a full solve: **0.35–0.40**.
* The next two rounds produce a full two-prize solve: **below 0.10**.

This is a **route-repair and kill-test phase**, with a credible theorem-bearing branch. It is not a closing phase.

The current exception-by-exception MCA route is not convergent. It keeps finding new point-fiber, Lattès, high-genus, configuration-character, and puncture-heredity complications without proving how their contributions aggregate on one line. D avoids that aggregation problem long enough to settle the cleaner scalar challenge and identify the correct algebra for C.

# 2. Why Other Routes Are Deprioritized

| Candidate                                             | Status               | Decision                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A. Lattès / split-rational registry**               | **Parallel support** | Verify the frontier-relevant projective packet and one Lattès packet. Do not build a registry. A registry does not bound collective overlap, and the Lattès packets may lie below already-certified failure floors.                                                                    |
| **B. Support-theoretic split-rational overlap cover** | **Deprioritized**    | This currently combines two unknowns: defining canonical containers and aggregating many inequivalent systems. Higher genus is not discrepancy-only, and positive-dimensional families make taxonomy-first closure doubtful. Give it one restricted two-system kill-test.              |
| **C. Primitive (t=1) apolar/GJ base case**            | **Backup**           | It has an exact finite abelian-group formulation and correctly absorbs the divisor-product packet through (G_{\mathrm{eff}}). But it addresses only one MCA slice and does not reduce arbitrary (t), (d>\sigma), hereditary envelopes, or line-level aggregation.                      |
| **D. Scalar-list apolar/circuit theorem**             | **Primary**          | The apolar CI is static, syndrome-canonical, gauge-invariant, and controls all error-weight layers. The first nontrivial stratum is explicit. If extended, it solves scalar lists and hence all official same-field interleavings. Circuits remain diagnostics, not the final theorem. |
| **E. Finite checker and threshold ledger**            | **Parallel support** | Mandatory, but not a mathematical upper theorem. It must identify the exact reserve and remaining integer budget. It cannot replace the local-limit theorem.                                                                                                                           |

The circuit-transversal formulation inside D is specifically demoted. Since the minimum circuit hitting number differs from the list size by at most
[
\left\lfloor\frac{r-1}{\sigma}\right\rfloor,
]
a global transversal theorem is almost the original list problem and can consume the entire finite certificate.

# 3. Dependency DAG

## Scalar/list challenge

```text
EXACT INTERLEAVED-LIST THRESHOLD                                  [UNKNOWN]
├── Exact target Tq=floor(qcode/2^128) and radius staircase       [BANKED]
├── Exact scalar full-coordinate numerator                        [BANKED]
├── Same-field scalar-to-interleaved projection                    [BANKED]
├── All-layer apolar complete-intersection theorem                 [VERIFY_FIRST]
│   ├── Is=(A,B), deg A+deg B=r+1                                [VERIFY_FIRST]
│   ├── Locator criterion for every e≤j                           [VERIFY_FIRST]
│   ├── Full-coordinate iff gcd(U,V)=1                            [VERIFY_FIRST]
│   └── Low-generator collapse: e<b ⇒ e=d and P∼A                [VERIFY_FIRST]
├── First nontrivial stratum d=σ+1, b=j                           [VERIFY_FIRST]
│   ├── Generalized-Jacobian fiber equivalence                     [VERIFY_FIRST]
│   ├── Effective subgroup Geff and exact Fourier formula          [VERIFY_FIRST]
│   ├── Model modulus [0]+σ[∞] local limit                         [UNKNOWN]
│   └── Arbitrary degree-(σ+1) modulus local limit                 [UNKNOWN]
├── Higher deg(V) / subresultant induction                         [UNKNOWN]
├── Sum over all locator degrees with explicit constants           [UNKNOWN]
├── Finite upper certificate at the first candidate reserve         [UNKNOWN]
└── Previous-reserve scalar lower certificate                      [LIKELY]

Circuit-transversal as the final list wall                          [FALSE-CUT]
Arbitrary rational-function norm-character ledger                   [FALSE-CUT]
Boundary-layer-only treatment of the actual list                    [FALSE-CUT]
Ambient q^σ occupancy without effective-image conditioning          [FALSE-CUT]
```

## MCA challenge

```text
EXACT MCA THRESHOLD                                                 [UNKNOWN]
├── Exact syndrome transverse-secant formulation                    [BANKED]
├── Exact j-set padding for overagreement                           [BANKED]
├── Restricted lower/failure mechanisms                             [BANKED]
├── Finite target and reserve/radius staircase                      [BANKED]
├── One fixed support block-system packing                          [VERIFY_FIRST]
│   ├── Projective equality-scale packet                            [VERIFY_FIRST]
│   ├── Degree-31 Lattès packet                                     [VERIFY_FIRST]
│   └── Multiple-system weighted overlap                            [UNKNOWN]
├── t=1 shifted-RS/apolar normal form                               [VERIFY_FIRST]
│   ├── d=σ generalized-Jacobian support fiber                      [VERIFY_FIRST]
│   ├── Effective subgroup conditioning                             [VERIFY_FIRST]
│   ├── External-color collision formula                            [UNKNOWN]
│   ├── Model subset-product/color local limit                      [UNKNOWN]
│   └── d>σ rational-pair inverse                                   [UNKNOWN]
├── Hereditary envelope potential over arbitrary punctures           [UNKNOWN]
├── Denominator-free assembly over all t                            [UNKNOWN]
└── Exact finite MCA upper certificate                              [UNKNOWN]

Critical-seed completion as a weaker counting theorem                [FALSE-CUT]
General compression t>σ to t≤σ                                     [FALSE-CUT]
Point-fiber quotients as a complete configuration ledger             [FALSE-CUT]
Genus≥2 automatically treated as square-root discrepancy             [FALSE-CUT]
Pure n^(1+o(1)) finite safe-side certificate                          [FALSE-CUT]
```

# 4. Round 1 Execution Plan — Exactly 9 Workers

## Worker 1 — Scalar apolar foundation referee

**Wall:** `L-LIST-APOLAR-ALL-LAYER-CI`

**Objective:** Independently prove the all-layer scalar theorem for (C=\operatorname{RS}[F,L,k]): the CI structure, locator criterion for every (e\le j), unique (P=AU+BV) decomposition, full-coordinate criterion (\gcd(U,V)=1), and low-generator collapse.

**Success:** Complete proof covering (s=0), (d=b), roots at infinity, non-split generators, homogenization, small characteristic, and generator shear.

**Failure:** One explicit (F,L,k,s,E) violating any claimed equivalence.

**Expected label:** `BANKABLE_LEMMA`

## Worker 2 — Minimal scalar generalized-Jacobian formalizer

**Wall:** `L-LIST-MINIMAL-CI-GJ-FIBER`

**Objective:** Prove the exact lemma stated in Section 9 below for
[
\deg A=\sigma+1,\qquad \deg B=j>\sigma+1.
]
This must turn the entire minimal-stratum scalar list into one generalized-Jacobian subset-product fiber, plus the possible locator (A).

**Success:** Exact bijection, (G_\Delta) order formula, (G_{\mathrm{eff}}), Fourier formula, generator-shear invariance, and auxiliary-form independence.

**Failure:** An explicit CI whose list and generalized-Jacobian fiber differ.

**Expected label:** `BANKABLE_LEMMA`

## Worker 3 — Primary local-limit proof lane

**Wall:** `W-LIST-MODEL-GJ-QUOTIENT-CONDITIONED-LOCAL-LIMIT`

**Objective:** Work only with
[
\Delta=[0]+\sigma[\infty]
]
and a cyclic smooth domain (H=\alpha\mu_n). Let (Q_{\mathrm{per}}) be the quotient generated by characters whose pullbacks through (\alpha_\Delta) are constant on cosets of a proper subgroup of (H). Prove
[
N_\Delta(b)
\le
\frac{N_{Q_{\mathrm{per}}}(\pi b)}{|\ker\pi|}
+
C_\sigma\frac{\binom{n}{j}}{|G_{\mathrm{eff}}|}
+
P_\sigma(n),
]
with explicit integer (C_\sigma,P_\sigma).

**Success:** A proved finite inequality usable by the certificate checker, with no asymptotic placeholders.

**Failure:** A parameterized nonperiodic family exceeding every stated residual bound.

**Expected label:** `PROOF`

## Worker 4 — Primary-route counterpacket hunter

**Wall:** Same wall as Worker 3.

**Objective:** Search for exact rich fibers after conditioning on (G_{\mathrm{eff}}) and (Q_{\mathrm{per}}). Use exhaustive small fields for structural discovery, then attempt an official-rate parameterized construction.

**Success:** An exact official-rate packet, (q<2^{256}), whose minimal-stratum scalar list exceeds (T_q) and is not accounted for by (Q_{\mathrm{per}}).

**Failure:** Only toy anomalies, support counts without full-coordinate verification, or packets already represented by the declared quotient.

**Expected label:** `COUNTERPACKET`

## Worker 5 — Backup (t=1) MCA support-plus-color theorem

**Wall:** `L-JR-T1-GJ-FIBER-AND-COLOR`

**Objective:** For the shifted (t=1) code and (\deg A=\sigma,\deg B=j), prove the generalized-Jacobian support equivalence and derive the exact external-color function
[
\chi(T,c)=-\lambda_Tc.
]
Characterize when two generalized-Jacobian supports yield the same MCA slope.

**Success:** An exact formula for the distinct-color numerator, not merely the number of support representations.

**Failure:** A concrete color collision contradicting the proposed formula or showing support-fiber size cannot control slope count as stated.

**Expected label:** `BANKABLE_LEMMA`

## Worker 6 — Exact frontier and certificate ledger

**Wall:** `RS-PRIZE-FRONTIER-V1`

**Objective:** Build the exact code-specific scanner described in Section 7. It must preserve (q_{\rm gen},q_{\rm line},q_{\rm code},q_{\rm chal}) separately and refuse to treat unproved terms as upper certificates.

**Success:** Reproducible JSON and human-readable output identifying, for each code, the first reserve not already killed and the exact remaining upper budget.

**Failure:** Floating-point verdicts, field conflation, rate-only outputs, or a “safe” result based on (n^{1+o(1)}).

**Expected label:** `AUDIT`

## Worker 7 — Projective equality-scale packet verifier

**Wall:** `V-PROJECTIVE-SUBLINE-M-EQUAL-SIGMA`

**Objective:** Independently reproduce the Cycle 60 construction with
[
p=2^{19}-1,\quad n=2^{19},\quad k=2^{17},\quad
M=\sigma=2^{14},
]
including the (\psi(X)=(X+2)/(2X+1)) block system, the choice of (\vartheta), the (28{,}048{,}800) distinct slopes, transversality, proper-envelope exclusion, full monomial action ranks, and
[
T_F=16{,}776{,}960.
]

**Success:** Machine-verifiable exact certificate for every algebraic and numerical claim.

**Failure:** Any incorrect degree, squarefreeness, collision bound, action-rank claim, envelope claim, or threshold comparison.

**Expected label:** `AUDIT`

## Worker 8 — Degree-31 Lattès verifier

**Wall:** `V-LATTES-31`

**Objective:** Verify the curve order, 31-isogeny kernel, explicit rational map, full-fiber distribution, field/domain admissibility, pole removal, slope distinctness, transversality, envelope exclusion, and exact target comparison.

**Success:** A complete machine-readable packet certificate.

**Failure:** Any arithmetic, constant-field, fiber, regularity, or noncontainment failure.

**Expected label:** `AUDIT`

The degree-113 packet waits. It is not entitled to a second worker unless the degree-31 packet fails or the frontier checker shows it is uniquely relevant.

## Worker 9 — Two-block-system route kill-test

**Wall:** `W-MCA-TWO-BLOCK-COMMON-UNION-RIGIDITY`

**Objective:** For two separable maps (R,S) with no common right factor, study exact supports that are simultaneously unions of full (R)-fibers and full (S)-fibers. Bound the number of connected components in the block-incidence graph, or construct many nontrivial common unions on one envelope-free syndrome line.

**Success:** An explicit family showing that pairwise support overlap cannot be charged by a bounded registry without an additional invariant.

**Failure:** A proved finite component/common-union bound strong enough to make B precise.

**Expected label:** `ROUTE_CUT`

# 5. Round 2 Conditional Plan

A Round 1 “verification” requires Workers 1 and 2 to pass and Worker 3 either to prove its model theorem or to reduce it to one strictly narrower explicit estimate without a Worker 4 counterpacket.

## If Round 1 verifies D

Allocate all 9 workers as follows:

* **3** independent methods for arbitrary degree-((\sigma+1)) moduli: Fourier/conductor, algebraic geometry, and additive-combinatorial local limit.
* **2** workers on the next slices (\deg V=1) and (\deg V=2), with exact fixed-defect and subresultant accounting.
* **1** all-layer summation and finite scalar certificate.
* **1** official-rate counterpacket red team.
* **1** adjacent-reserve scalar lower certificate and interleaved transfer.
* **1** transfer of the verified method to the (t=1,d=\sigma) MCA backup.

## If Round 1 kills D

Allocate:

* **3** workers to identify the counterpacket inside the exact generalized-Jacobian/restriction algebra.
* **2** workers to formulate and independently falsify a repaired theorem.
* **1** worker to determine whether the packet changes an official list threshold.
* **1** worker to advance C as the new primary route.
* **1** worker to integrate the packet into the finite checker.
* **1** master referee to decide whether D is repairable or permanently cut.

A scalar packet is route-killing only if it is parameterized or official-scale and is not merely a missed quotient of (G_\Delta).

## If Round 1 produces another exception family

Do not append another named ledger term.

Allocate:

* **3** workers to decide whether it is functorially generated by (G_\Delta), a subresultant, or the apolar restriction algebra.
* **2** workers to prove a canonical bounded-complexity formulation and assignment rule.
* **1** frontier worker to test official relevance.
* **1** worker to search for a second independent family; a second unrelated statistic is a taxonomy kill.
* **1** worker on the C backup.
* **1** referee to accept the repaired algebraic class or cut the route.

## If Round 1 is inconclusive

Allocate:

* **2** workers to fixed (\sigma=2,3) model-modulus Fourier theorems.
* **2** workers to exhaustive small-field and symbolic-orbit enumeration.
* **1** worker to close unresolved edge cases in the all-layer CI theorem.
* **1** worker to attack arbitrary (A) in the minimal scalar stratum directly.
* **1** worker on the (t=1) MCA color theorem.
* **1** worker on the exact frontier checker.
* **1** referee to issue a proof/counterpacket/route-cut decision.

No Round 2 worker is assigned to a broad all-genus registry under this branch.

# 6. Human / PRZ Review Priorities

PRZ should inspect these claims in this order:

1. **All-layer scalar apolar identity:**
   [
   p_E\in(I_s)_e
   \iff
   s\in\operatorname{span}{h_x:x\in E},
   ]
   for every (e\le j).

2. **Full-coordinate criterion:** in the unique decomposition
   [
   p_E=AU_E+BV_E,
   ]
   the syndrome representation is full-coordinate iff
   [
   \gcd(U_E,V_E)=1.
   ]

3. **Low-generator collapse:**
   [
   e<b\quad\Longrightarrow\quad e=d,;p_E\sim A,
   ]
   and hence a scalar fiber of size at least two requires (d\ge\sigma+1).

4. **Minimal scalar generalized-Jacobian equivalence:** the exact lemma in Section 9, including nonreduced (\Delta), nonsplit closed points, generator shear, and the equal-degree edge case.

5. **Effective-image correction:** the main denominator is (|G_{\mathrm{eff}}|), not (|G_\Delta|) or (q^\sigma), and coherent characters must be charged jointly through a quotient.

6. **(t=1) external-color formula:** verify that the support-to-color map counts distinct slopes correctly; support multiplicity must not be mistaken for MCA numerator.

7. **Projective equality-scale packet:** verify the (\vartheta)-avoidance argument, distinct-slope polynomial degree bound, full monomial action ranks, and proper-envelope claim.

8. **Finite staircase convention:** if (\widehat\sigma) is minimally safe, distinguish the largest safe grid radius from the supremal transition radius, whose endpoint is unsafe.

9. **Degree-31 Lattès packet:** only after Items 1–8. It is a verification target, not a banked theorem or a reason to build a registry.

# 7. Scripts / Checkers To Write

## `rs_prize_frontier_v1.py`

**Input**

```json
{
  "code_id": "...",
  "n": "...",
  "k": "...",
  "domain_descriptor": "...",
  "q_gen": "...",
  "q_line": "...",
  "q_code": "...",
  "q_chal": "...",
  "reserve_range": ["..."],
  "certified_lower_terms": ["..."],
  "certified_upper_terms": ["..."],
  "conditional_terms": ["..."]
}
```

**Output**

For every reserve: (j), exact targets, exact lower maximum, exact proved upper total, unresolved budget, safe/fail/unknown, assumption flags, and both radius conventions.

**Verifies/falsifies**

* Code-specific threshold claims.
* Field-ledger consistency.
* Frontier relevance of projective and Lattès packets.
* Any attempt to use asymptotics as a finite certificate.

## `scalar_apolar_ci_verify.sage`

**Input:** finite field, evaluation set (L), (k,\sigma), and syndrome (s).

**Output:** CI generators and degrees; every split locator of degree (e\le j); ((U,V)); gcd; direct syndrome coefficients; full-coordinate comparison; circuit minors.

**Verifies/falsifies**

Workers 1 and 2’s foundational identities.

## `minimal_ci_gj_fiber.sage`

**Input:** (F,L,\sigma,A,B) with (\deg A=\sigma+1,\deg B=j).

**Output:** divisor algebra (H^0(\Delta,\mathcal O_\Delta)), (G_\Delta), boundary images, (G_{\mathrm{eff}}), target class, exact fiber histogram in enumerable cases, and comparison with the actual list.

**Verifies/falsifies**

The final next lemma and the effective-subgroup denominator.

## `model_modulus_fourier_scan.sage`

**Input:** (F,H,j,\sigma), with (\Delta=[0]+\sigma[\infty]).

**Output:** exact fiber counts, Fourier coefficients, periodic-character subgroup, quotient (Q_{\mathrm{per}}), quotient-conditioned contribution, and maximum residual.

**Verifies/falsifies**

Worker 3’s local-limit theorem and Worker 4’s candidate packets.

## `mca_t1_gj_color_scan.sage`

**Input:** (t=1) shifted-code instance, syndrome, external evaluation point, and reserve.

**Output:** generalized-Jacobian support fibers, representation coefficients, external colors, color collisions, and exact distinct-slope count.

**Verifies/falsifies**

The C backup route.

## `verify_projective_subline_packet.sage`

**Input:** fixed packet parameters or an equivalent manifest.

**Output:** exact block system, admissible (\vartheta) count, support locators, slope set, action ranks, envelope test, occupancy ledger, and target comparison.

**Verifies/falsifies**

The equality-scale projective packet.

## `verify_lattes31_packet.sage`

**Input:** elliptic curve, kernel generator, field tower, domain, and proposed map.

**Output:** curve order, kernel, Vélu map, separability, fiber distribution, pole normalization, support identities, slope count, transversality, envelope status, and target comparison.

**Verifies/falsifies**

The degree-31 packet only.

## `two_block_overlap_kill.sage`

**Input:** (F,L,R,S,a), induced full-block systems, and optional defects.

**Output:** common-right-factor/refinement certificate, block-incidence graph, component count, common-union supports, minimum weighted cover, and any syndrome-line envelope witness.

**Verifies/falsifies**

Whether B has a viable pairwise base theorem.

No script may output `SAFE` from floating-point logarithms.

# 8. Stop Conditions

## Abandon D as the primary route

Abandon it if either:

1. the all-layer CI/full-coordinate theorem is false; or
2. an official-rate or parameterized (d=\sigma+1) packet exceeds the finite target after exact (G_{\mathrm{eff}}) and periodic-quotient conditioning, and its statistic is not generated by the finite apolar restriction/subresultant algebra.

A small-field irregularity alone is not enough.

## Rewrite the “primitive” theorem

Rewrite immediately whenever:

* the proposed denominator is (q^\sigma) rather than (|G_{\mathrm{eff}}|);
* several characters contribute coherently through one quotient;
* the residual bound fails after the quotient actually declared in the theorem.

The word “primitive” is forbidden unless it means the explicitly defined Fourier residual after a specified quotient projection.

## Stop expanding quotient taxonomy

Stop when either:

* a second verified exception requires an algebraically unrelated statistic not generated by apolar restriction, generalized Jacobians, resultants, or bounded-degree subresultants; or
* Worker 9 exhibits unbounded nonrefining block-system overlap without a common right factor or proper envelope.

At that point, replace taxonomy by a direct support-module/Fourier theorem.

## Switch from MCA to scalar list first

This condition is already met, subject to Workers 1 and 2 surviving audit:

* MCA still requires line-level aggregation and hereditary puncture closure.
* Scalar lists have a static all-layer canonical object.
* The projective and Lattès packets do not themselves supply the missing MCA aggregation theorem.

Therefore D is primary now.

## Switch from theorem proving to finite-checker first

Do so if the checker cannot identify:

* the first candidate reserve;
* a strict previous-reserve lower certificate;
* the exact field paying each term; or
* the remaining integer budget below (T_q).

No theorem worker should optimize constants against an unspecified reserve or an asymptotic margin.

## Stop Lattès work

After degree 31 is verified, stop unless the frontier checker shows it changes the first unresolved reserve for an official code. Do not verify degree 113 merely to enlarge a registry.

# 9. Final Next Lemma

## `L-LIST-MINIMAL-CI-GJ-FIBER`

Let
[
C=\operatorname{RS}[F,L,k],\qquad r=n-k,\qquad j=r-\sigma,
]
and let (s\ne0) have apolar ideal
[
I_s=(A,B),
\qquad
\deg A=\sigma+1,\qquad
\deg B=j>\sigma+1,\qquad
\gcd(A,B)=1.
]

Let
[
\Delta=V(A).
]
Choose a linear form (L_*) nonvanishing on (\Delta), and define
[
G_\Delta
========

H^0(\Delta,\mathcal O_\Delta)^\times/F^\times,
]
[
\alpha_\Delta(x)
================

\left[
\left.\frac{L_x}{L_*}\right|*\Delta
\right],
\qquad
x\in L\setminus\operatorname{Supp}\Delta,
]
and
[
b*\Delta
========

\left[
\left.\frac{B}{L_*^j}\right|_\Delta
\right].
]

Prove:

1. The only full-coordinate listed locator of degree (<j) is (A), when (A) is monic, squarefree, and completely (L)-split.

2. For (T\in\binom Lj),
   [
   T\text{ is a full-coordinate representation of }s
   ]
   if and only if
   [
   T\cap\operatorname{Supp}\Delta=\varnothing
   \quad\text{and}\quad
   \prod_{x\in T}\alpha_\Delta(x)=b_\Delta
   \quad\text{in }G_\Delta.
   ]

3. Consequently,
   [
   N_s(\sigma)
   ===========

   \mathbf 1_{{A\text{ is squarefree and }L\text{-split}}}
   +
   N_{\Delta,j}(b_\Delta).
   ]

4. With
   [
   G_{\mathrm{eff}}
   ================

   \left\langle
   \alpha_\Delta(x)\alpha_\Delta(x_0)^{-1}:
   x\in L\setminus\operatorname{Supp}\Delta
   \right\rangle,
   ]
   all (j)-fold products lie in one coset of (G_{\mathrm{eff}}), and (N_{\Delta,j}(b)) has the exact finite Fourier expansion over that effective group.

5. The statement is independent of (L_*) and invariant under every admissible generator change
   [
   B\mapsto cB+AC.
   ]

This is narrow, immediately assignable, and it makes the next hard object unambiguous.

**Do I see a route to a full solve?** Yes, conditionally: prove this lemma, prove the resulting finite scalar subset-product local limit, extend through bounded (\deg V), close the scalar/interleaved certificate, and transfer the same algebra to the (t=1) MCA branch. The remaining MCA support-overlap and hereditary-envelope theorems would still be required. The current registry-first route does not reach a full solve; this repaired route plausibly does.
