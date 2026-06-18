Cyce 26 atack: W-F1-AA-RES-T2J3-QZERO-RANK-CONSISTENCY

  Ledger respected: B=F_p (q_gen=p), F=F_{p^2} (q_line=p^2), q_chal unused,
  D=F_p(n=p),t=sigma=2,j=3,eta_reserve=2/nsub-reserve,offR0
  (kappa=u∧b≠0). Restricted line-incidence/residue calculation only; no
q_gen/protocol/lit/CA/MCA/line-decoding/urve-MCA/SNARKclaim.

  I worked the realized-slope condition c_0(z) ∈ span_B(c_1(z),c_2(z),c_3(z))
  directly,intheF-planemodel.TheresultcorrectsagapinhowCycle25's
  audit framed the rank-drop strata, and isolates a single explicit scalar
obstrucion.

SetupIuse

  Off R0, {u,b} (u=[W]_E, b=[Bnum]_E) is an F-basis of A=F[X]/E, so the F-linear
  isoA≅F^2,c=su+tb↦(s,t),carrieseachcolumntoavector
  v_i(z)=(s_i(z),t_i(z))∈F^2, and F^2≅B^4 via {1,α}. From Cycle 25/20:

v_1=(p1^1-zq1^1,p2^1-zq2^1),v_2=(p1^2-zq1^2,p2^2-zq2^2),

v_3=(-1,z),v_0=(p1^0-zq1^0,p2^0-zq2^0),

q1=c_b·η,η=(c^2-d)+cτ_1+τ_2⟹q1^1=c_bc,q1^2=c_b,q1^0=c_b(c^2-d).

  Realizable slope z ⟺ v_0(z) ∈ span_B(v_1(z),v_2(z),v_3(z)) ⊆ F^2≅B^4. Write
  ⟨x,y⟩:=Im_α(x̄y)forthealternatingB-areaform(so⟨x,y⟩=0⟺x,yare
  B-proportional). Let C(z)=[v_1|v_2|v_3]∈Mat_{4×3}(B).

  The rank stratification, done correctly

  Define the two strata by the 3×3 minors of C(z) as polynomials in (z_0,z_1):

DEP:=all3x3minorsofC(z)vanishidentically(rank_BC(z)<=2forall
  z),

NONDEP:=some3x3minorofC(z)isnotidenticallyzero(rank_BC(z)=3
  generically).

  Lemma 1 (when c∉B, the branch is always NONDEP). The z-leading symbols of
  columns1,2areâ_1=-q1^1=-c_bcandâ_2=-q1^2=-c_b.AuniversalB-dependence
  β_1v_1+β_2v_2+β_3v_3≡0 forces, on the s-coordinate z-leading part, c_b(β_1
c+β_2)=0; with c_b≠0 and c∉B this gives β_1=β_2=0, thenthet-coordinae

z-leadingpartgivesβ_3=0.Sonouniversaldependence⟹NONDEP.(When

c∈B,d∉B,separatednessstillholdsbut1,careB-dependent,soDEPbecomes

possible—thatistheoneresidualsub-casebelow.)

  Lemma 2 (NONDEP collapses the wall to a single Q-decision; rank-drop is
  negligible).OnNONDEPtherank-droplocus{rank_BC(z)≤2}isthecommonzero
  set of finitely many nonzero bounded-degree polynomials in (z_0,z_1), hence
O(p) point.For every z off that locus, rank_B C(z)=3,soQ(z)=0 is necesary

andsufficient.Therefore

NONDEP,Q≢0⟹C2⊆{Q=0}∪{rank-drop}=O(p)+O(p)=O(p)[Cycle16],

NONDEP,Q≡0⟹everyzofftheO(p)rank-droplocusisrealizable⟹C2=
  p^2 - O(p) = Θ(p^2).

  This is the precise correction to the Cycle 25 audit. The audit worried that
  rank-dropstratamightmakeQ≡0insufficientandsecretlyrescueO(p).On
  NONDEP that worry is void: rank-drop is only O(p) values of z, so the
augmeted-minrcondiionshere cannot change th asymptotic count. OnNONDEP

thewallisexactly"Q≡0?"—noranksubtletysurvives.(Idonotassert

Q≡0happens;andtheΘ(p^2)conclusionisstillgatedbythe

distinct-split-cubicrequirement,seebelow.)

  Lemma 3 (DEP restricts, it does not expand). If DEP holds (rank_B C(z)≤2 for
  allz),thenQ≡0automaticallyandcarriesnoinformation.Realizabilityis
  v_0(z)∈U(z) with U(z)=span_B C(z) of B-dimension ≤2, i.e. two independent
B-linearconditions ℓ_1(z)·v_0(z)=ℓ_2(z)·v_0(z)=0, eachabounded-degree

polynomialin(z_0,z_1).TheircommonzerosetisO(p)(apropersubvariety)

unlessbothvanishidentically.Soarankdropmakestherealizableset

smaller,neverΘ(p^2),exceptinthesingledegenerateeventwherethe

augmented4×4matrix[c_1|c_2|c_3|c_0]hasrank_B≤2identically.

  Net structural statement (rank-correct, replaces the false "Q≡0 ⟹ every slope
  realized"):

C2=Θ(p^2)⟺therealizablelocus{z:c_0(z)∈span_BC(z)}is2-dimensional

⟺(NONDEPandQ≡0)or(DEPandthetwoaugmentedconditions
  ≡ 0).
  OtherwiseC2=O(p).

The explicitfirst obstructin (degree-4 oeffcint ofQ)

  Using s_i=a_i+m_z(â_i), t_i=c_i+m_z(t̂_i) and ⟨m_z x,m_z y⟩=N(z)⟨x,y⟩, the
  degree-4partofQfactorsasN(z)^2·Q_4withN(z)=z·z̄the(nonzero,
  anisotropic) norm form. Since â_3=0 (column 3 is z-constant in s), three of
the six Plückerterms dropand

Q_4=N(c_b)·[Im_α(c)·Im_α(q2^0)+Im_α(c̄·w)·Im_α(q2^2)−Im_α(w)·Im_α(q2^1)
  ],

w=c^2−d,q2^2=P,q2^1=d+Pc,q2^0=cd+P·w,P=P_E(u,b)/κ.

  Because N(z)^2 ≢ 0:

Q_4≠0⟹Q≢0⟹C2=O(p)(onNONDEP,henceontheentirec∉Bbranch).

  The factor N(c_b)≠0 (source-valid c_b≠0) and the appearance of Im_α(c)≠0 (c∉B)
  makeQ_4genericallynonzero.SoaΘ(p^2)seedonthec∉Bbranchrequiresthe
  explicit scalar equation Q_4=0 plus all lower-order coefficients of Q to
vanish, plusthe pli-cuic gate. This isstrcly sharperthan "is Q≡0": it

isrank-stratified,anditpinsthefirstvanishingcoefficientinclosed

form.(IpresentQ_4ascomputedfromthebankedclosedforms;the

deterministiccheckerbelowshouldconfirmitbeforeitistreatedasmore

thanaguide.)

  Where det M sits (kept separate, per Cycle 25)

  det M=(c_b/κ^2)D, with D=N(ℓ)κ=κ∏_{a∈F_p}E(a)≠0 (Cycle 24), is the z-free
  coefficient-framedeterminantofτ↦[q1:p1−q2:p2]∈P^2(F).Itgovernswhether
  the witnessing co-support τ(z) exists and is non-degenerate (relevant to the
distic-D-split-cubic gte X^3−τ_1X^2+τ_2X−τ_3 splittingwith distincroots

inF_p),butitislogicallyindependentofthez-fiberobjectQ.Itneither

forcesNONDEPnordecidesQ≡0.Sothisbranchisgenuinelyliveandisnota

disguisedre-runoftheCycle24D=0cut.

  Answers to the three questions

  1. Not fully proved. But the rank stratification is resolved: rank-drop can
  onlyreduceC2(Lemma2onNONDEP,Lemma3onDEP).SoO(p)holdsonNONDEP
  whenever Q≢0, in particular whenever Q_4≠0; and c∉B source-valid data are
always NONDEP.

2.Notproduced,andnotcitingscans.AΘ(p^2)seedisnowpinnedtoa
  measure-zero event: (NONDEP & Q≡0) forcing Q_4=0 and all lower coefficients,
  orthesingleDEP-degeneratelocuswithc∈B,d∉B.
  3. Smallest exact decider isolated below.

  Smallest exact decider (checker / elimination ideal)

I_Q=idealofthe<=15coefficientsQ_{kl}ofQ(z_0,z_1)(topcoeff=
  N-form * Q_4 above),

I_aug=idealoftheaugmented-rankconditionsfortheDEPlocus(3x3minors
  of [C|c_0]),

I_valid=(∏_{a∈F_p}E(a))·κ·c_b·detMinverted(Rabinowitsch),+gcd(E,E^τ)=1
  (separated).

  Decide:  is V(I_Q) ∩ {NONDEP} ∩ {source-valid}  empty,  AND

isV(I_aug)∩{DEP,c∈B,d∉B}∩{source-valid}empty?

Ifbothempty⟹PROOF:C2=O(p)onthewholebranch.

  checker(p):

input:c,d∈F;W_{n-1},W_{n-2},W_{n-3};u,b∈F(residue-linedata)
    filter: ∏_{a∈F_p}E(a)≠0 ; gcd(E,E^τ)=1 ; κ≠0 ; c_b≠0 ; detM≠0

build:η,P,q_i,p_i,c_b;columnsv_0..v_3;4x4B-detQ;3x3minorsofC
  and of [C|c_0]

emit:stratum∈{NONDEP,DEP},degQ,Q_4,[Q_{kl}],Q_identically_zero,

rankdrop_count,augmented_ideal_dim,C2=#{z:c_0(z)∈span_BC(z)},

split_distinct_countamongwitnessingτ(z),status

flag:(NONDEP&Q≡0)OR(DEP&augmented≡0),source-valid,splitcubics
  retained

→candidateΘ(q_line)seed(NOTproof)

  Primarylabel

  BANKABLE_LEMMA

  Banked (restricted D=F_p, t=σ=2, j=3, off R0, source-valid):

  1. DEP/NONDEP dichotomy via C(z)-minors, with c∉B ⟹ NONDEP (leading symbols
  c_bc,c_bareB-independent).

2.NONDEPreduction:rank-dropisO(p)points,soQ≢0⟹C2=O(p)and
  Q≡0⟹C2=Θ(p^2); the rank-stratification adds nothing on NONDEP. This corrects
  theCycle25audit'sopenworry.

3.DEPrestriction:auniversalrankdropturnsrealizabilityintotwo
  augmented B-conditions, giving O(p) unless they vanish identically; rank drop
  nevermanufacturesΘ(p^2)exceptinthatexplicitdegeneratelocus.

4.Explicitdegree-4obstruction:deg-4partofQisN(z)^2·Q_4withthe
  closed Q_4 above; Q_4≠0 ⟹ Q≢0 ⟹ C2=O(p), and Q_4 is generically nonzero
  (N(c_b)Im_α(c)factor).

  Residual EXACT_NEW_WALL: W-F1-AA-RES-T2J3-QZERO-RANK-IDEAL — decide emptiness
  ofV(I_Q)∩{NONDEP,source-valid}andofthe
  DEP/c∈B,d∉B/augmented-identically-zero locus, both saturated at
κ·c_b·detM·∏_aE(a).

  Not banked: any O(p) proof on the full live branch, any counterpacket, any
  corrected-reserve/q_gen/protocol/list/CA/MCA/line-decoding/SNARKconsequence,
  any finite-scan-as-proof. I did not repeat Q≡0 ⟹ every slope realized: the
Θ(p^2) conclusion is conditinal on NONDEP, carris an O(p)rank-drop

correction,andremainsgatedbythedistinct-split-cubicrequirement.

Routetoafullsolve?

  Yes, and it is now a single bounded inequation plus one narrow locus, not the
  open-ended"isQ≡0."

Next exact lemma to prove (orrefute):on NONDEP source-valid data, Q_4≠ 0.

Concretely,showthe≤9-parametersystem

Im_α(c)·Im_α(cd+Pw)+Im_α(c̄w)·Im_α(P)−Im_α(w)·Im_α(d+Pc)=0,

c∉B,κ≠0,c_b≠0,∏_{a∈F_p}E(a)≠0,P=P_E(u,b)/κ

  has no source-valid solutions (Gröbner saturation over Q, p carried
  symbolicallyviaN(ℓ)=∏E(a)).Ifso,Q≢0ontheentirec∉Bbranch⟹C2=O(p)
  there, and the whole wall reduces to the lone c∈B, d∉B DEP-degenerate locus,
where Cycle 22/24's Im_α decupling identities (Im_α(J_A)=2Im_α(d)+Im_α(c)f_2)

arethenaturalnexttool.TheN(c_b)Im_α(c)structureofQ_4makesemptiness

(PROOF,C2=O(p))themorelikelyoutcome,butitisnotyetdecided.
