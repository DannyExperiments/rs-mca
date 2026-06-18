EXACT_NEW_WALL

⏵⏵dn't ask on (sift+tab to cycle) · esc tointerrpt

  I worked the t=2, j=4 case by hand against the banked Cycle
  11/12/16/20/24/25/28objects(kernelexecutionisdisabledinthisharness,so
  no finite checker was run; flagged below). The headline finding is a clean
structural break: the Cycle 28 mechanism doesno extendtoj=4,andthe

reasonisexactandbankable.

  Field and parameter ledger

  - B = F_p, q_gen = p. F = F_{p^2} = B(alpha), alpha^2 = theta nonsquare,
  q_line=p^2.q_chalunused,keptseparate.

-D=F_p,n=p.t=sigma=2,nowj=n-a=r-t=4;hencea=n-4,k=
  n-6. eta = sigma/n = 2/n, sub-reserve.

-A=F[X]/E,E=X^2+cX+d,xi=[X]_E,xi_m=[X^m]_E,u=[W]_E,b=
  [Bnum]_E, ell = [X^p-X]_E = [L_D]_E, kappa = u wedge b.

-OffR0(kappa!=0);source-valid(EnonzeroonF_p);separated
  (gcd(E,E^tau)=1); c_b = -Q_E(b)/kappa != 0.

-Conjugationfbar=f_0-alphaf_1,Im(f)=f_1,N=N_{F/B},w=c^2-d.

  This is a restricted residue-line/bad-slope incidence calculation only.

  1. The t=2, j=4 quotient and affine system

  Co-support T = D\S, |T| = 4, with tau_i = e_i(T), i=1..4. Euclidean division W
  =L_SQ_S+I_S,degQ_S<=j-1=3,L_S=L_D/L_T,L_D=X^p-X.UsingL_S
  L_T = X^p-X the sub-leading coefficients of L_S are the complete homogeneous
symmetrics h_i(T) (h_1=u_1,h_2=tau_1^2-tau_2, h_3=tau_1^3-2tau_1

tau_2+tau_3),andthedivisionrecursiongivestheclosedform(validforp

pastthefirstfewcoefficients,degW=n-1):

Q_S=W_{n-1}X^3

+(W_{n-2}-W_{n-1}tau_1)X^2

+(W_{n-3}-W_{n-2}tau_1+W_{n-1}tau_2)X

+(W_{n-4}-W_{n-3}tau_1+W_{n-2}tau_2-W_{n-1}tau_3),

  i.e. [X^{j-1-i}]Q_S = sum_{m=0}^{i} (-1)^m W_{n-1-i+m} tau_m (tau_0=1). This
  reproducestheCycle11(j=2)andCycle12(j=3)formsexactly,andconfirms
  the family pattern: Q_S depends on tau_1,...,tau_{j-1} only (here
tau_1,tau_2,tau_3, no u_4).

  The locator residue is affine in all four parameters:

lambda=[L_T]_E=xi_4-tau_1xi_3+tau_2xi_2-tau_3xi_1+tau_4,
  mu  = b*lambda,          iota = u*lambda - ell*[Q_S]_E,

L_z(tau)=iota-z*mu=sum_{i=1}^{4}tau_iC_i(z)+C_0(z)=0inA~=B^4.

  Co-support parameters and columns C_i(z) = P_i - z R_i:

C_4=(u)-z(b)

C_3=(-uxi+W_{n-1}ell)-z(-bxi)

C_2=(uxi_2-ell(W_{n-1}xi+W_{n-2}))-z(-bxi_2)[R_2=+bxi_2]

C_1=(-uxi_3+ell(W_{n-1}xi_2+W_{n-2}xi+W_{n-3}))-z(-bxi_3)

  with R_i = (-1)^i b xi_{4-i}.

  2. What replaces Q — the parameter count meets the ambient dimension

  At j=3: 3 parameters (tau_1,tau_2,tau_3), ambient dim_B A = 2t = 4.
  Consistency="-C_0liesinthe3-dimcolumnspan"=onecodimension-1
  equation, the 4x4 determinant Q(z)=det_B[C_1|C_2|C_3|C_0]. That is the
incidence obstruction whose Q_4 != 0gave C2 <= 4p.

  At j=4: 4 parameters (tau_1,...,tau_4), ambient still B^4 (since t is
  unchanged).Thecoefficientmatrix

M(z)=[C_1(z)|C_2(z)|C_3(z)|C_4(z)]isalready4x4overB.

  So Q (the augmented 4x4 det) has no direct analogue: the augmented matrix
  [C_1|C_2|C_3|C_4|C_0]is4x5,andwhendet_BM(z)!=0thesystemM(z)tau=
  -C_0(z) has a unique solution tau(z) in B^4 — affine consistency holds for
every such z. The natural determinant is now the squarecoefficient

determinantdet_BM(z),whoserolehasflipped:itisthe

uniqueness/invertibilitylocus,notanincidenceobstruction.Thisisthe

"missing-determinant"failuremodeoftaskitem6.

3-4.Topsymbolandlocatorfactorization

  Each C_i(z) = P_i - z R_i; the degree-4-in-z part (top symbol) takes every
  -zR_i:

TopSym=det_B[m_z(-R_1)|...|m_z(-R_4)]=det_B(m_z)*
  det_B[-R_1|-R_2|-R_3|-R_4],

  m_z = multiplication by z in F on A. As a B-map on A ~= B^4, det_B(m_z) =
  N(z)^2(sameN(z)^2prefactorasCycle28).ThesignbookkeepingR_i=(-1)^ib
  xi_{4-i} gives det_B[-R_1|..|-R_4] = det_B[b xi_3 | b xi_2 | b xi_1 | b xi_0]
= det_B(m_b)*det_B[xi_3|xi_2|xi_1|xi_0]. Wihxi_0=(1,0),xi_1=(0,1),

xi_2=(-d,-c),xi_3=(cd,c^2-d)over{1,xi},the4x4B-determinantcollapsesto

det_B[xi_3|xi_2|xi_1|xi_0]=-(Im(c)Im(cd)-Im(d)Im(w))=-(Q_4/
  N(c_b)),

  the same degree-1 locator factor as Cycle 28 (Q_4/N(c_b) = c_1^2 d_0 - c_0 c_1
  d_1+d_1^2).Withdet_B(m_b)=N(Q_E(b))=N(c_b)N(kappa):

TopSym(det_BM(z))=-N(kappa)*N(z)^2*Q_4

=-N(kappa)N(c_b)Im(c)^2*N(z)^2*E(-Im(d)/Im(c))
  (c notin B).

  So yes, the top symbol factors as a source-valid-nonzero B-scalar times N(z)^2
  timesthelocatorfactor,andthelocatorcontentisexactlytheCycle28
  Q_4-quantity: TopSym = 0 iff E has an F_p-root iff N(ell)=prod_{a in
F_p}E(a)=0. By Cycle 28 (cntin B: Q_4 = N(c_b)Im(c)^2E(a*),

a*=-Im(d)/Im(c);cinB:Q_4=N(c_b)Im(d)^2,nonzerobyseparatedness)the

factorissource-validlynonzeroonbothbranches.N(kappa)!=0offR0.

  Exponent: the locator enters to m=1 (the same single active evaluation E(a*)
  asj=3),notagrowingpower,andismultipliedbyN(z)^2(alsounchangedfrom
  j=3). The literal full norm N(ell) is degree-p; the top symbol is not
literally N(ell)^m bu hesingle factor E(a*) whose zerolocusequalsthatof

N(ell).

  5-6. Consequence: the mechanism does NOT extend; exact new wall

  The clean top symbol proves det_B M(z) not identically zero, hence M(z) is
  invertibleoffadegree-<=4curve(<=4pslopes).ButthisdoesNOTgiveC2=
  O(p). Unlike j=3, det_B M is the uniqueness determinant: for all but <= 4p
slopes hereisa unique affine pr-image tau(z) = M(z)^{-1}(-C_0(z)),so

affineconsistencyisgenericallyautomaticandimposesnoslopebound.The

boundmustnowcomeentirelyfromthegatethatwasslackatj<=3:

W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE:

bound#{zinF:tau(z)=(e_1,e_2,e_3,e_4)ofadistinct4-subsetTsubset
  F_p }.

  Two structural warnings fall out, and I deliberately do not resolve them:

  - The unique-pre-image fact is a fiber statement (<=1 co-support per slope off
  thecurve),whichistheoppositeofafiber-collapsebound.Thereare~
  C(p,4) ~ p^4/24 split quartics but only p^2 slopes, so the affine layer no
longer obstructs C2 rom reaching Theta(p^2)=Thea(q_line).Thisisagenuine

sub-reservecounterpacketseed—exactlythefailuremodeCycle28's"routeto

fullsolve"flagged—butitisNOTacounterpacket:nogrowing-primefamily,

noprovensurjectivityontoapositive-densityslopeset,andsingle-prime

scanswouldbeexperimentalonly.

-Thetop-symbolmechanism(locator-controlled,source-validnonzero,with
  constant exponents N(z)^2, locator m=1) persists; what fails is its
  slope-boundingconsequence,becausethedeterminantitisthetopsymbolof
  changed meaning when #params rose from j-1<2t to j=2t.

  Bankable sub-lemma (inside this wall)

  In the restricted D=F_p, t=sigma=2, j=4, off-R0, source-valid separated c_b!=0
  window:thej=4quotientclosedformabove;theaffinesystemhas4
  parameters with square coefficient matrix M(z)=[C_1|C_2|C_3|C_4]; and
TopSym(det_BM)= -N(kappa)N(z)^2 Q_4,source-validly nonzero,withQ_4the

Cycle28locatorquantity(vanishingiffN(ell)=0).Hencedet_BMnot

identicallyzero,sotheslope->co-supportmapisgenericallyawell-defined

degree-<=4rationalmapz->tau(z).

Dependencylist

  - Cycle 11/12: family pattern for Q_S, [e_j^?]-independence, lambda reduction,
  Delta/L_zsetup.

-Cycle16:c_i(z)=s_iu+t_ibcolumns,Q≢0=>C2<=4p(necessitydirection
  only).

-Cycle20:q1=c_beta,q2=lambda_0^(0)+Peta,expansionidentity,
  c_b=-Q_E(b)/kappa, gate det M=(c_b/kappa^2)D.

-Cycle24:D=N(ell)kappa,N(ell)=prod_{ainF_p}E(a);source-valid
  nonvanishing.

-Cycle25:six-termPlucker/LaplaceshapeandthedetM(z-free)vsQ(z)
  (fiber) separation.

-Cycle28:Q_4=N(c_b)(Im(d)^2-Im(c)Im(cbard)),Q_4∝E(a*),source-valid
  nonvanishing both branches.

  Hidden assumptions

  - Q_S closed form uses p large enough that W_{n-1..n-4} are genuine top
  coefficientsandthe-XtailofL_D=X^p-Xdoesnotreachthetopjquotient
  coefficients (Cycle 11/12 style hypothesis).

-Thelambda_0/expansion-identityinputsaretakenfrombankedCycle12/20
  forms; I re-derived Q_S, the columns, and det_B[xi_3|xi_2|xi_1|xi_0] directly,
  butreusedtheQ_4closedformfromCycle28ratherthanre-derivingitfrom
  raw A0/B0.

-det_B(m_z)=N(z)^2anddet_B(m_b)=N(Q_E(b))=N(c_b)N(kappa)usedet_B=
  N_{F/B} o det_F for F-linear endomorphisms of A.

-Nofinitecheckerwasrun(kerneldisabled).Aby-pscanoverp=7,11,13
  against raw Cycle 14/15 columns would convert this from "by-hand" to
  "machine-confirmed";recommendedbeforeanypromotion.

Rejectedoverclaims

  - NOT a C2=O(p) proof for j=4: the top symbol does not bound slopes once the
  affinedeterminantbecomestheuniquenessdeterminant.

-NOTacounterpacket:theTheta(q_line)riskisunproven(nogrowing-prime
  family, no split-quartic image lower bound).

-NoclaimthetopsymbolequalsN(ell)^m;itisscalar*N(z)^2*(single
  locator factor E(a*), zero-locus = {N(ell)=0}), exponent m=1.

-Sub-reserve(eta=2/n),localonly.Nocorrected-reserve,q_gen/q_linemerge,
  q_chal, list/CA/MCA/line-decoding/curve-MCA/protocol/SNARK, or
  Proximity-Prizeconsequence.
  - No converse det_B M(z)=0 => realized slope.

  Next exact wall

  W-F1-AA-RES-T2J4-SPLIT-QUARTIC-GATE: with tau(z)=M(z)^{-1}(-C_0(z)) the unique
  affinepre-image(offthe<=4pcurvedet_BM(z)=0),bound#{zinF:X^4-
  tau_1(z)X^3 + tau_2(z)X^2 - tau_3(z)X + tau_4(z) splits into 4 distinct roots
inF_p\S}. Prve either (i) this imagei O(p) (extendingthet=2lawtoj=4),

or(ii)exhibitasource-validgrowing-primefamilyrealizing

Theta(p^2)=Theta(q_line)distinctslopes(thesub-reservecounterpacketseed).

  Do I see a route to a full solve?

  Not a clean one at j=4 via the j<=3 mechanism — it provably stops here. The
  honestnextlemmaisthesplit-quarticimage-count,framedasa
  curve-meets-split-locus problem: the degree-<=4 rational slope-to-co-support
map z ->tau(z)lands in the spae of monic quarics; hequestionishow

oftenithitsthetotally-split-distinctF_plocus.Anaturalattackisto

composez->tau(z)withthediscriminantandthep-power"splitoverF_p"

condition(eachrootinF_pisaFrobenius-fixedcondition),turningthegate

intoincidenceofafixedlow-degreecurvewiththeFrobenius/split

stratification—butIhavenotreducedthattoabankedbound,andthe

abundanceofsplitquartics(~p^4vsp^2slopes)meansthecounterpacket

directionisliveandmustbesettledbyagrowing-primefamily,notasserted.
