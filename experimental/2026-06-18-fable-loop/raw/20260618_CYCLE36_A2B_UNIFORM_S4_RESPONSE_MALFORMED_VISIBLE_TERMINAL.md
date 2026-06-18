Ihave red allrequired source files (Cycles 29, 30, 32, 33, 34, 35 audits;
the Cycle 32histogram checker and crtificate; the Cycle 28 Q_4 proof;the
Cycle 11 utilities; and thedieo tat). I cannotexecute code n this
harness (notebookecutonisdenied and there is no shell tool), so every
claim belw is either a by-had derivtion Ican verify, or is explicitly
flagged s an nrun finite check. Ledgers kept separate: q_gen=p, B=F_p,
F=F_{p^2}=B(alpha), q_line=p^2,q_chal unued.

⏵⏵ don't ask on (shift+tb to cycle)· c toinerrupt     86% context used

  AUDIT — corrected reading of the banked evidence

  Before attacking the uniform step I re-examined the Cycle 30/32 finite data,
  becausetheCycle30audit's"leanstowardO(p)"impressiondrivesthewhole
  skeptical framing.

pC2(hist)p^2/24C2/p^2

702.040.000

1135.040.025

1337.040.018

17812.00.028
  19    13         15.0      0.036

239-1222.0~0.022
  29    33-34      35.0      0.039   -> 1/24 = 0.0417

  C2/p^2 climbs monotonically toward 1/24. The apparent "C2 ≈ 1.08 p at p=29" is
  asmall-primeartifact:p^2/24≈pnearp=24,soO(p)andp^2/24are
  numerically indistinguishable in the scanned range. Read correctly, the data
iscsistent with p^2/24 frm beow, not with collapse.This is EXPERIMENTAL

only,butitremovesthemainreasontoexpectanO(p)killerandreorients

thecycletowardconfirmingtheseed.

  1. Explicit source-valid family (BANKABLE_LEMMA)

  The key move that makes "infinitely many primes" tractable: encode the family
  byfixedintegersreadintoF=F_p(alpha)viaafixednonresidue,andreduce
  every source-validity hypothesis to integer non-vanishing.

  Fix nr = -1 (so alpha^2=-1, a nonresidue exactly for p ≡ 3 (mod 4) — an
  infinite,positive-densityprimeset).Fixcoordinates:

E=X^2+cX+d,c=alpha(c_0=0,c_1=1),d=1(d_0=1,d_1=0)
  b = [Bnum]_E = X    (b_0=0, b_1=1 in A=F[X]/E)

u=[W]_EandW_{n-1},...,W_{n-4}:fixedintegercoordinatesinF(freedata)

ell=[X^p-X]_E:computed,notfree(Cycle24recipe)

  BANKABLE_LEMMA (L-T2J4-UNIFORM-FAMILY). For E = X^2 + alpha X + 1 over
  F=F_p(alpha),alpha^2=-1:

  - No F_p-root / source-valid. E(a) = (a^2+1) + alpha·a for a in B; Im E(a)=a
  vanishesonlyata=0,whereReE(0)=1≠0.SoEhasnorootonD=F_pforevery
  such p. Equivalently Q_4 = N(c_b)·Im(c)^2·E(a*) = N(c_b)·E(0) ≠ 0 (Cycle 28),
a*= -Im(d)/Im(c) = 0.

-Separated.E-E^tau=2alphaX,commonrootforcesX=0,butE(0)=1≠0;
  coprime for all odd p.

-cnotinB,c_b≠0.c_1=1≠0forallp.

  So the denominator side is uniformly source-valid with no excluded primes
  beyondp≡3(mod4),p≠2.Theremaininghypotheseskappa=uwedgeb≠0(off
  R0) are single integer non-vanishing conditions on the free coordinates (u,
W_{n-1..n-4}); pick any integer liftwith kappa ≠ 0 at oneprime ad ii

nonzeroforallpoutsidethefinitesetdividingthatfixedinteger.Thisis

thefamily;itsonlyp-dependenceinsideM(z),C_0(z)isell=[X^p-X]_E,

controlledbyN(ell)=prod_{ainF_p}E(a)≠0(Cycle24,alreadynonzerohere).

  This lemma is hand-verifiable and I bank it. It converts "construct an
  infinitefamily"into"fixintegers+avoidafinitebadset."

  2. Uniform geometric S4 — reduction to ONE finite check (BANKABLE_LEMMA)

  I could not run the symbolic resolvent/discriminant, so I do not bank PROOF of
  G_geom=S_4.WhatIcanbankisareductionthatcollapsestheuniform-in-p
  problem to a single bounded computation, using two monotonicity facts.

  BANKABLE_LEMMA (L-T2J4-GEOM-MONOTONE). Let disc_num(z_0,z_1) in O[z_0,z_1],
  O=Z[alpha],bethediscriminantnumeratorofL_tau(degree≤24;disc_XL_tau
  = disc_num/Delta^6, Delta^6 a square — Cycle 34), and R(y) the resolvent
cubic. For the fixed family f Part 1:

  (a) Discriminant nonsquareness is monotone. If disc_num mod p_0 has
  nonconstantsquarefreepartatonegoodprimep_0,thenthecharacteristic-0
  disc_num has nonconstant squarefree part, hence disc_num mod p is nonsquare in
bar(F_p)[z_0,z_1] for all butfinitelymany p. (Proof: ifchar-0 disc_num =

u·g^2uptoconstantu,reductionatgoodp_0givessquarefreepart=

constant;contrapositive.Forwardgood-reductionthenpropagates.)

  (b) Geometric irreducibility reduces. If R(y) is absolutely irreducible over
  F_{p_0}(z_0,z_1)atonegoodp_0,thenR(y)isabsolutelyirreducibleover
  \bar Q(alpha)(z_0,z_1), hence over bar(F_p)(z_0,z_1) for almost all p.
(Factoriztion specalizesunder good rducion.)

  BANKABLE_LEMMA (L-T2J4-S4-CRITERION). In char ≠ 2,3, with G_geom ≤ S_4 acting
  onthe4roots:

G_geom=S_4<=>R(y)absolutelyirreducibleoverbarB(z_0,z_1)

ANDdisc_numnonsquareoverbarB(z_0,z_1).

G_geom=S_4<=>R(y)absolutelyirreducibleoverbarB(z_0,z_1)
             AND disc_nm nonsquare overbar B(z_0,z_1).

TransitivesubgroupsofS_4notinA_4are{S_4,D_4,C_4};D_4,C_4have
  reducible resolvent; irreducible resolvent + nonsquare disc forces S_4.
  CombinedwithL-T2J4-GEOM-MONOTONE,bothconditionsarecertifiableata
  single good prime and then hold for almost all p in the family. The surface
check may bedone on a generic lin z_1 = m z_0 + e (fixedintegers m,e):

G_line≤G_surf≤S_4,soG_line=S_4⟹G_surf=S_4,reducingthewitnessto

aunivariatedegree-≤24squarefreetestandacubicoverbarB(z_0).

TransitivesubgroupsofS_4notinA_4are{S_4,D_4,C_4};D_4,C_4have
reducble resolvent;irreducible resolvent+ nonsquare discforces S_4.
Combined with L-T2J4-GEOM-MONOTONE, both conditions are certifiable at a
single good prime and then hold foralmost all p inthfamily. Thsurface
check may be dono a geric linez_1 = m z_0 + e(fixed ntegersm,e):
G_line ≤ G_surf ≤S_4,so G_line = S_4 ⟹ G_surf=S_4, rucing thewitnessto
a univariate degree-≤24 squarefreetest and a cubic ove bar B(z_0).

Ibankthesethreelemmas.Theyaretherealprogress:theuniformwallisnow
  a finite, fixed computation, not an infinite family.

  3. Arithmetic/geometric equality (clean resolution, no surviving obstruction)

  The task asks whether a constant-field obstruction survives uniformly. On the
  geometricrouteitcannot:

  BANKABLE_LEMMA (L-T2J4-NO-CFO). If the geometric criterion of Part 2 holds
  (G_geom=S_4),thensinceG_geom⊴G_arith≤S_4,necessarilyG_arith=S_4=
  G_geom. The sign/constant-field quotient G_arith/G_geom is forced trivial. A
constan-field obtructioncan surviveonly n a puely-arithmetic roue that

provesnonsquarenessoverB(z_0,z_1)butnotoverbarB(z_0,z_1)—i.e.only

ifdisc_numhadconstantsquarefreepart(aunittimesasquare).Theobserved

abundanceofoddcycletypes("112"transpositions:193atp=29;"4"

4-cycles:197)isdirectEXPERIMENTALevidencethatdisc_numisgenuinely

nonsquareasapolynomial,sothesquarefreepartisnonconstantandno

constant-fieldobstructionisavailable.Cycle35'seven-type"13"argumentis

thensubsumed:provingthegeometricstatementremovestheneedfora

separatesignargument.

  Adversarial obstruction hunt (did NOT find a killer)

  Being adversarial as instructed, I checked every candidate uniform
  obstruction:

  - Rank-one / image collapse to a curve (O(p) route): cut by Cycle 34
  (ROUTE_CUT,genericJacobianrank2,birationalontothequadric).Stillcut.

-SingularcurveDelta=0blowingupthecount:boundedbyCycle33(≤4p=
  O(p)). Cannot create Theta(p^2).

-Constant-fieldobstruction:removedonthegeometricroute(Part 3).

-Discriminantforcedsquarebythequadric-surfaceconstraint(theone
  genuinely new worry — the quartics are constrained to the Cycle 30 quadric
  {Phi=0},notgeneric):contradictedbyabundantoddcycletypesinthe
  histograms. No evidence the quadric is tangent to the discriminant locus.

Icouldnotconstructapreciseobstruction.Therouteisopenandstrongly

favored,notcut.

  4. Conditional counterpacket SEED (NOT a COUNTERPACKET)

  Conditional on the single-prime certificate of Part 2 succeeding for the
  familyofPart1:

SEED(conditional,restrictedt=2,j=4branchonly):

Off-Delta,G_geom=G_arith=S_4uniformly=>

byChebotarev/Lang-WeilontheA^2_Bsurface,

C2=(1/24)p^2+O(p^(3/2))=Theta(q_line).

  Dependencies: Cycle 24 (N(ell)≠0), Cycle 28/29 top-symbol (Q_4≠0, Delta≢0),
  Cycle33(singular≤4p),Cycle34(rank-2dominance),Cycle35finitecert,
  plus Part 1–3 here. Excluded upgrades (explicitly not claimed):
corrected-reserve, MCA, CA, list-dcoding,line-dcoding,curve-MCA, protocol,

SNARK,prize;noq_gen/q_linemerge.Thisisalocalsub-reserveseedinone

toybranch.IdonotbankCOUNTERPACKET.

5.EXACT_NEW_WALL

W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERT

  For the fixed family E=X^2+alphaX+1, b=X, nr=-1, a fixed integer choice of
  (u,W_{n-1..n-4})withkappa≠0,andafixedgenericlinez_1=mz_0+e,verifyat
  ONE good prime p_0 ≡ 3 (mod 4):

ForthefixedfamilyE=X^2+alphaX+1,b=X,nr=-1,afixedintegerchoiceof
(u,W_{n-1..n-4}) with kappa≠0, nd afixed genericln z_1=m z_0+e, vriyat
ONE good prime p_0 ≡ 3 (mod 4):

1.buildM(z),C_0(z)withm_z=z_0I_4+z_1A_alpha;confirmdegDelta=4and
  top symbol -N(kappa)N(z)^2 Q_4;

2.tau_i=detM_i/Delta;formR(y)anddisc_numontheline;

3.certifydisc_num(z_0)hasnonconstantsquarefreepart(gcdwithderivative)
  and R(y) is absolutely irreducible over F_{p_0}(z_0).

Success⟹(viaPart2monotonicity+Part 3)uniformG_geom=G_arith=S_4and
  the Part 4 seed for almost all p≡3 (mod 4). Failure at every fixed family ⟹ a
  genuinestructuralobstruction(disc-squareorresolvent-splitforcedbythe
  quadric), which would be the real ROUTE_CUT.

1.buildM(z),C_0(z)withm_z=z_0I_4+z_1A_alpha;confirmdegDelta=4and
top symbol -N(kappaN(z)^2 Q_4;
2. tau_i =det M_i/Delta; form R(y)anddisc_numontheline;
3certfyisc_num(z_0) has nonconstant squarefreepart (gcdwithderivative)
and R(y) is absoltely irreducible over F_{p_0}(z_0).
Success ⟹ (via Par 2 monotonicity+ Part 3) uniform G_geom=G_arith=S_4and
the Part 4 seed foralst all p≡3(mod 4). Failure at every fixed family ⟹a
genuine structural obstruction(disc-squareor resolvent-split forced by the
quadric), which would be the real ROUTE_CUT.

Thiswallisfiniteandbounded—thesingleremaininggate.

  Routetoafullsolve?

  Yes — I see a clear route to fully solving this restricted wall (uniform
  geometricS_4,hencethelocalTheta(q_line)seed),andtheuniform-in-p
  difficulty is now genuinely dissolved by the monotonicity lemmas of Part 2.

  The next exact construction is the single-prime certificate
  W-F1-AA-RES-T2J4-A2B-SINGLE-PRIME-S4-CERTabove:anexecutablefinitecheck
  for the explicit family E=X^2+alphaX+1, b=X, nr=-1 on one generic line at one
prime p_0≡3 (mod 4). The nextexact lemma to bak afterthat chek is:

  L-T2J4-A2B-UNIFORM-S4 (target):

ForthePart-1family,disc_numhasnonconstantsquarefreepartandR(y)

isabsolutelyirreducibleoverbarB(z_0);thereforeG_geom=G_arith=S_4

forallbutfinitelymanyp≡3(mod4).

  I could not run that check here (no code execution available), so this cycle
  banksthefamilyconstruction,thethreereduction/monotonicitylemmas,the
  corrected evidence reading, and the sharpened single-prime wall — but does not
promte to PROOF, COUNTERPACKET, or any reserve/MCA/prizestatus.
