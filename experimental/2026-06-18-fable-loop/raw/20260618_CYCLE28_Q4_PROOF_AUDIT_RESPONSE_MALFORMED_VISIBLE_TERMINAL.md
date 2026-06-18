Code execution isdisabled n this harness (permssiondenied),so I verified
the algebra by hand symbolically rar than nuericaly. Th compuation is
elementary enough o check rigorously on paper, and I did each step twice.
Here i the audit.

---
PROOF (of the rsricted-window Q_4 facts and the C2=O(p) upper bound; notof
anything above it)

Fieldledger

  - B = F_p, q_gen = p. F = F_{p^2} = B(α), α^2 = θ nonsquare, q_line = p^2.
  q_chalunused—keptseparatefromq_gen,q_line.

-D=F_p,n=p.t=σ=2,j=n−a=r−t=3.η_reserve=σ/n=2/n,
  sub-reserve.

-A=F[X]/E,E=X^2+cX+d,ξ=[X]_E,u=[W]_E,b=[Bnum]_E,κ=u∧b,ℓ
  = [X^p−X]_E.

-OffR0(κ≠0);source-valid(EnonzeroonF_p);separated(gcd(E,E^τ)=1);
  c_b = −Q_E(b)/κ ≠ 0.

-Conjugationf̄=f_0−αf_1,Im(f)=f_1,areaform⟨x,y⟩=Im(x̄y)=x_0y_1−
  x_1y_0, with scaling law ⟨λx,λy⟩ = N(λ)⟨x,y⟩.

  Proof / verification

  I reconstructed the columns from Cycle 15/16 verbatim, c_i(z) = s_i(z)u +
  t_i(z)b:

s_1 = p1^1 −z q1^1,  t_1 = p2^1 − zq2^1

s_2=p1^2−zq1^2,t_2=p2^2−zq2^2

s_3=−1,t_3=z

s_0=p1^0−zq1^0,t_0=p2^0−zq2^0

  Writing s_i = σ_i − zβ_i, t_i = γ_i − zδ_i: (β_1,β_2,β_0)=(q1^1,q1^2,q1^0),
  β_3=0;(δ_1,δ_2,δ_0)=(q2^1,q2^2,q2^0),δ_3=−1.

  (Q1) Six-term expansion + degree-4 extraction. In each of the six Cycle-25
  termsthetopz-partof⟨s_i,s_j⟩isN(z)⟨β_i,β_j⟩andof⟨t_k,t_l⟩is
  N(z)⟨δ_k,δ_l⟩ (scaling law with λ=z). So the degree-4 part of Q is N(z)^2 ·
Q_4 with

Q_4=⟨β_1,β_2⟩⟨δ_3,δ_0⟩−⟨β_1,β_3⟩⟨δ_2,δ_0⟩+⟨β_1,β_0⟩⟨δ_2,δ_3⟩

+⟨β_2,β_3⟩⟨δ_1,δ_0⟩−⟨β_2,β_0⟩⟨δ_1,δ_3⟩+⟨β_3,β_0⟩⟨δ_1,δ_2⟩.

  β_3=0 kills terms 2,4,6, leaving exactly the three Cycle-27 terms.

  I closed the "pending q1/q2" gap directly from the Cycle 20 wedge definitions
  (q1=(B0∧b)/κ,q2=(u∧B0)/κ,B0=λ_0b)usingthebankedexpansionidentity(λ_0
  x)∧y = λ_0^{(0)}(x∧y) − λ_0^{(1)} P_E(y,x), λ_0^{(0)}=cd+dτ_1,
λ_0^{(1)}=η=(c^2−d)+cτ_1+τ_2:

  - (λ_0 b)∧b = −η P_E(b,b) = −η Q_E(b) ⟹ q1 = −(Q_E(b)/κ)η = c_b η. So
  (β_1,β_2,β_0)=c_b(c,1,w),w=c^2−d.

-u∧(λ_0b)=λ_0^{(0)}κ+ηP_E(u,b)⟹q2=λ_0^{(0)}+Pη,P=P_E(u,b)/κ.
  Hence q2^0=cd+Pw, q2^1=d+Pc, q2^2=P.

  This is the mechanical check Cycle 26/27 flagged as outstanding; it passes.

  Substituting (scaling law on the β's, δ_3=−1 so ⟨·,δ_3⟩=±Im):

Q_4=N(c_b)·[Im(c)·Im(q2^0)+Im(c̄w)·Im(q2^2)−Im(w)·Im(q2^1)]

  —reproducingthedisplayedCycle26formulaexactly.

  (Q3) P-cancellation and closed form. The P-linear functional
  φ(P)=Im(c)Im(Pw)+Im(c̄w)Im(P)−Im(w)Im(Pc)isB-linear;
  φ(1)=Im(c)Im(w)−Im(w)Im(c)=0 and φ(α)=c_1w_0+(c_0w_1−c_1w_0)−w_1c_0=0, so φ≡0.
The cancellation is sructural: q2'sP-part is Pη, collinearwithq1=c_bη.

TheP-freeremainder,incoordinates(Im(w)=2c_0c_1−d_1,

Im(cd)=c_0d_1+c_1d_0):

Q_4/N(c_b)=Im(c)Im(cd)−Im(w)Im(d)=c_1^2d_0−c_0c_1d_1+d_1^2.

  And Im(d)^2 − Im(c)Im(c̄d) = d_1^2 − c_1(c_0d_1−c_1d_0) = d_1^2 − c_0c_1d_1 +
  c_1^2d_0.Identical.FormulaVERIFIED.

  (Q4) Locator identity. For a∈F_p, Im(E(a)) = c_1 a + d_1. If c∉B (c_1≠0),
  a^*=−d_1/c_1∈F_pistheuniquepointwithE(a^*)∈B,and
  c_1^2 E(a^*) = d_1^2 − c_0c_1d_1 + c_1^2 d_0 = Q_4/N(c_b), so

Q_4=N(c_b)·Im(c)^2·E(−Im(d)/Im(c)),Q_4=0⟺EhasanF_p-root⟺
  ∏_{a∈F_p}E(a)=N(ℓ)=0.

  This is the same locator norm Cycle 24 attached to D=N(ℓ)κ. Two independent
  routeslandingon∏_{a∈F_p}E(a)isstrongcorroborationofthecolumnforms.
  VERIFIED.

  (Q5) Source-valid nonvanishing, both branches.

  - c∉B: source-valid ⟹ E≠0 on F_p ⟹ N(ℓ)≠0 ⟹ E(a^*)≠0 ⟹ Q_4≠0.

-c∈B(c_1=0):Q_4=N(c_b)Im(d)^2;separatednessforbidsd∈B(elseE^τ=E),so
  d_1≠0 ⟹ Q_4≠0.

-c∉B:source-valid⟹E≠0onF_p⟹N(ℓ)≠0⟹E(a^*)≠0⟹Q_4≠0.
∈ (c_1=0): Q_4=N(c_b)Im(d)^2; separatedness forbids d∈B (elseE^τ=E),so
d_1≠0⟹ Q_4≠0.

Soseparated+source-valid+offR0+c_b≠0⟹Q_4≠0onbothbranches.
  CONFIRMED.

  (Q6) What is proved. N(z)=z_0^2−θz_1^2 is anisotropic, so N(z)^2≢0 with no
  B-linearfactor;Q_4≠0(scalar)⟹degree-4part≢0⟹degQ=4⟹Q≢0.Theupper
  bound needs only the necessity direction realized slope ⟹ Q(z)=0 (a solution
forces column dependence),whih holdsunonditionally —norank

stratificationrequired.Anonzerototal-degree-≤4polynomialoverF_phas≤4p

zerosinB^2,so

C2≤#{z∈F:Q(z)=0}≤4p=O(p)=O(n).

  The distinct split-cubic gate restricts realized slopes to a subset of
  {Q(z)=0},soitcanonlyshrinkthecount.TheQ≡0counterpacketbranchis
  therefore empty across the entire source-valid separated off-R0 t=2, j=3
winw.

Dependencylist

  - Cycle 15/16: column construction c_i(z)=s_i u + t_i b, fiber equation
  L_z=ι−zμ=0,Schwartz–Zippelsafeside(Q≢0⟹C2≤4p).

-Cycle25:six-termPlücker/LaplaceexpansionofQ.

-Cycle20:q1=(B0∧b)/κ,q2=(u∧B0)/κ,B0=λ_0b,expansionidentity,
  c_b=−Q_E(b)/κ; Cycle 12 λ_0 coordinates λ_0^{(0)}=cd+dτ_1, λ_0^{(1)}=η.

-Cycle24:D=N(ℓ)κ,N(ℓ)=∏_{a∈F_p}E(a)(cross-check,notload-bearingfor
  Q_4).

-Necessitydirectionrealized⟹Q(z)=0(Cycle 25),theonlypartusedforthe
  upper bound.

  Hidden assumptions

  - The six-term Plücker expansion is taken from Cycle 25 with its stated signs.
  TheQ_4≠0/Q≢0conclusionisrobusttoanyoverallsignornonzero-scalar
  error in that expansion, since only nonvanishing is used.

-λ_0^{(0)},λ_0^{(1)}andtheexpansionidentityaretakenfromCycle12/20
  banked forms; I re-derived q1, q2 from them but did not re-derive them from
  theabsoluteraw[W]_E,A0,B0definitions.

-O(p)upperboundusesonlynecessity,soitdoesnotdependontheCycle26
  NONDEP rank stratification (that machinery is needed only for a converse/lower
  bound).

-Source-valid=EnonzeroonF_p;separated=gcd(E,E^τ)=1;bothκ≠0and
  c_b≠0 assumed.

-Verificationwasby-handsymbolic(kernelexecutionwasunavailable);a
  finite checker over p=7,11,13 against raw Cycle 14/15 columns would convert
  "by-hand"to"machine-confirmed,"butthealgebraaboveiscompleteand
  self-contained.

  Rejected overclaims

  - Not a corrected-reserve result (η=2/n, sub-reserve).

-Noq_gen/q_linemerge;q_chaluntouched.

-Nolist-decoding,CA,MCA,line-decoding,curve-MCA,protocol,SNARK,or
  Proximity-Prize consequence.

-DoesnotasserttheconverseQ(z)=0⟹realizedslope(Cycle25'srejected
  claim); only the upper bound is claimed.

-DoesnotclaimQ≡0⟹Θ(q_line)anywhere—thatbranchisshownempty,not
  realized.

-Finitechecks(ifrun)wouldbeconfirmation,nevertheproof.

  Verdict on Cycle 27

  Cycle 27's Q_4 derivation is correct: the formula Q_4 = N(c_b)(Im(d)^2 −
  Im(c)Im(c̄d)),theP-cancellation,thelocatoridentityforc∉B,and
  source-valid nonvanishing on both branches all reproduce from the source/audit
definition.Nobad sign, no missinghypothesis, no falsesource-validity

implication,noq2failure,nosource-validQ_4=0exampleexists.Cycle27's

conservativeBANKABLE_LEMMAself-labelcanbepromoted:withtheq2closed

formnowconfirmedagainsttheCycle20wedgeidentity,therestrictedt=2,

j=3branchisagenuinePROOFthatQisneveridenticallyzeroandC2=O(p)in

thiswindow.

Routetoafullsolve

  Yes — for this restricted line-incidence sub-problem the t=2, j=3 wall is
  closed.Thenextexactlemmaisthegeneralizationtheauditsalreadyname:

W-F1-AA-RES-T2-HIGHER-J-LOCATOR-NORM (and the T3J2 companion)

  Claim to prove: for t=2 and arbitrary j, the top-degree coefficient of the
  slope-consistencydeterminantQisanonzeroB-multipleofapowerofthesame
  Frobenius-locator norm N(ℓ)=∏_{a∈F_p}E(a). The quotient λ_0 has degree j−1,
sothe columns and the Plücker expansion scale accodingly;ifthetopsymbol

staysapowerofN(ℓ),source-validitykillsQ≡0forthewholet=2family,

givingC2=O(p)uniformlyinthetoywindow.Thisremainsstrictlysub-reserve

andyieldsnoprotocol,q_gen,MCA,orreserveconsequence.

  Next exact wall

  W-F1-AA-RES-T2J4-LOCATOR-NORM-TOP-SYMBOL: extract the top-degree coefficient
  ofQfort=2,j=4fromtherawcolumnsanddecidewhetheritequalsanonzero
  B-scalar times N(ℓ)^m for some m≥1. Failure on a source-valid stratum is the
precise seedfor a growing-prime sub-reserve countepacket;successextends

theC2=O(p)prooftoalljatt=2.
