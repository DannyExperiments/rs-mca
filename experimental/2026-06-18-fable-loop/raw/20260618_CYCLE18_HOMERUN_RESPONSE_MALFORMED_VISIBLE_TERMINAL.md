Both Write and code executio are dniedin this harness — the same
operatioal wall the Cycle 16/17audits recorded (output_files/ could not be
produced; deliverablesweregivn inline). I cannot create flesunder
outpu_files/ or run thescanner, so per theestablished fallback I deliver
the research artifact inline. The mathematicalcontentbelow iswhat matters,
and it does notdepndon execution:  is a hand proof rea directly off the
banked Cycle14/15 column consruction.

---

Cycle18ResearchArtifact—W-F1-AA-RES-T2J3-RANK-DET-SPLIT

  Exactstatuslabel

EXACT_NEW_WALL(primary)

BANKABLE_LEMMA(secondary:themonicitylemma+safe-sideO(p),below)

  I did not reach PROOF (full collapse) or COUNTERPACKET. I made the largest
  source-validleapavailablewithoutcomputation:astructurallemmathat
  removes the τ3 variable from the dangerous stratum and reduces the residual
wall from a 3-variable surface problemto a singl 2-variablerational-map

image-dimensionquestion.

  Parameters / ledger (kept strictly separate)

B=F_p,q_gen=p
  F = F_{p^2},    q_line = p^2

q_chalunused

B-subfield=F_p;F=ambientextension;towerF/Bdegree2
  D = F_p,        n = p

t=sigma=2,j=n-a=r-t=3,a=n-3,k=n-5
  rho = k/n = (n-5)/n

eta=sigma/n=2/n(SUB-RESERVE)

quotientorder=3(moniccubicco-supportL_T);arity=2-termlineMCAtest
  Work off R0 = { kappa := wedge([W]_E,[Bnum]_E) = 0 }.

delta:T2J3-sliceagreementradius(notinvoked).

Sourcedeps(allinternal/banked):Cycle9W=L_SQ_S+I_S;Cycle12closed
  form

Q_S(e1,e2)indep.ofe3;Cycle13base-quadricsplitDelta=Delta0+alpha
  Delta1 ;
  Cycle14/15columns+affineformsp_i,q_i;Cycle16safe-sidebound.
  No external (Crites–Stewart/ABF) import is used.

  The new bankable lemma (monicity in τ3)

  Off R0, {[W]_E, b} (with b=[Bnum]_E) is an F-basis of A=F[X]/E. Write the
  landing2-forminthatbasis(thedeterminantofcoordinates,soleading
  coefficient is a literal 1, not the code's un-normalized κ-scaled wedge; the
two differ by the nonzero scalar κ∈Foff R0 and have thesamezerolocus):

iota=A0-tau3[W]_E=(p1-tau3)[W]_E+p2b,

mu=B0-tau3b=q1[W]_E+(q2-tau3)b,

Delta(tau):=wedge_{W,b}(iota,mu)
              = (p1 - tau3)(q2 - tau3) - p2 q1,

  where p_i,q_i are the Cycle-14 affine forms in (tau1,tau2).

  Lemma (monicity). As a polynomial in τ3, Delta is monic of degree exactly 2
  withleadingcoefficient1∈B.Consequently,splittingDelta=Delta0+α
  Delta1 with Delta0,Delta1 ∈ B[τ1,τ2,τ3]:

deg_{tau3}Delta0=2(monic,leadingcoeff1),
  deg_{tau3} Delta1 <= 1.

  Proof. [L_T]_E = ν(τ1,τ2) − τ3·1_A because L_T = X^3 − τ1 X^2 + τ2 X − τ3 and
  onlytheconstanttermcarriesτ3,linearlywithcoefficient−1;reductionmod
  the monic quadratic E preserves this. Hence iota,mu are affine in τ3 with
τ3-cefficientsexactly −[W]_E, −b (this is precisely heidentityaffine_pq

assertsasafail-loudcheckintheCycle17scanner:iota−(A0−τ3[W]_E)=0,

mu−(B0−τ3b)=0).Theτ3^2coefficientofDeltaiswedge_{W,b}(−[W]_E,−b)

=wedge_{W,b}([W]_E,b)=1inthe{W,b}-basis.Theleadingcoefficientis

therefore1∈B;splittingoverF=B⊕αBsendsaB-coefficient1entirelyto

Delta0,soDelta1haszeroτ3^2-coefficient.∎

  This is bankable (no experiment, no imported theorem, no reserve claim, no
  ledgermerge).

  Safe-side corollary (re-derives and tightens Cycle 13/16)

  Landing locus L = {Delta = 0} = {Delta0 = 0} ∩ {Delta1 = 0} ⊂ B^3.

  Corollary. If gcd(Delta0, Delta1) = 1 in B[τ1,τ2,τ3], then L is at most a
  curve,#L=O(p),andC2=O(p)=O(n).

  Proof. Coprime Delta0,Delta1 define surfaces with no common component, so L
  hasdimension≤1;withdegDelta0=2,degDelta1≤2(eachp_i,q_iaffinein
  (τ1,τ2)), Bézout bounds deg L ≤ 4, giving #L ≤ O(p) points over F_p. Each
lanig point yields one slope z=(p1−τ3)/q1, so C2 ≤ #L=O(p).∎

  This recovers the Cycle 16 C2 ≤ 4p regime intrinsically (the "Q≢0" condition
  isimpliedbygcd=1),withouttheAUDIT-onlytrace/Gramcriterion.

Sharpened exactwall (the leap on lens3)

  The only way to leave the O(p) regime is gcd(Delta0,Delta1) ≠ 1 (this is
  exactlytheCycle13resonanceRa/Rb,nowgivenintrinsically).Themonicity
  lemma controls that common factor:

g:=gcd(Delta0,Delta1),gnonconstant.

Sincedeg_{tau3}Delta1<=1:
    either  Delta1 ≡ 0           (Delta = Delta0 in B[tau], full monic quadric
  surface),

ordeg_{tau3}g=1,g=s·tau3+h,s,hinB[tau1,tau2],degs<=1,
  deg h<=2.

  In the second case the resonance surface is the graph τ3 = −h/s, so
  substitutingintotheslopeformulaeliminatesτ3entirely:

z(tau1,tau2)=(p1-tau3)/q1=(p1+h/s)/q1ontheresonancegraph,

  a rational map B^2 ⇢ F of bounded degree. Equivalently (Cycle 14 slope
  quadratic),everylandingslopeisarootof

q1z^2-(p1-q2)z-p2=0,

  so the slope map factors through the coefficient map

mu_coef:(tau1,tau2)|-->[q1:(p1-q2):p2]inP^2(F).

  Therefore the residual wall reduces to one image-dimension question:

W-F1-AA-RES-T2J3-RANK-DET-SPLIT(sharpened):

Onasource-validresonancestratum(gcd(Delta0,Delta1)!=1),doesthe

2-variablemap(tau1,tau2)|->z(equivalentlymu_coefintoP^2(F))
  have 1-dimensional image  =>  C2 = O(p) = O(n)  (collapse),

orgenerically-finite(0-dim)fibers=>C2=Theta(p^2)=Theta(q_line)?

  This is a strict reduction: from "count slopes on a Θ(p^2)-point surface in
  B^3"to"isafixedbounded-degreerationalmapB^2⇢Ffiberedbycurves."It
  is decidable by one Jacobian/resultant identity (dz ∧ d(anything) ≡ 0 modulo
the resonnce relatons, i.e.functional dependence of zonasingle

coordinate),whichisexactlywhattheunrunCycle17scannerwouldsamplebut

whichasymboliccheckcansettleoutright.

  What is NOT proved (explicit)

  - No proof that the resonance slope map has 1-dim image (no collapse proof)
  andnoC2=Θ(q_line)counterpacket.Thedichotomyaboveisopen.

-Noproofofconj:B,noProximity-Prizeclaim;sourcehypotheses
  undischarged.

-Nothingatorabovecorrectedreserve:eta=2/nissub-reserve,soevena
  Θ(q_line) counterpacket here would not refute corrected MCA.

-Noq_genstatement(theΘ(p^2)wouldbeaq_linephenomenon;neverpaidinto
  q_gen).

-NoCA/MCA/list-decoding/line-decoding/protocol/SNARKconsequence;
  the T2J3 object is a curve-/line-incidence count and no conversion is claimed.
  -TheCycle16trace/Gramcriterionisstillnotverified;notusedhere.

-TheCycle15forced-Rap=7datum(C2≤6)leansagainstacounterpacketbutis
  single-prime, sub-reserve EXPERIMENTAL evidence and is not promoted.

  Other lenses (brief)

  - Lens 1 (full positive): blocked exactly on the image-dimension question
  above.

-Lens2(fullnegative):notconstructed;theonlyfiniteevidenceargues
  against it.

-Lens4(reserve):ledgeriseta=sigma/n=2/n,sub-reserve.Theopen
  sub-question that decides relevance: does the gcd(Delta0,Delta1)≠1 resonance
  obstructionpersistassigmagrows(degE=t=sigma),wheretheanalogous
  landing form is monic of degree sigma in the top symmetric variable? If yes,
the walli on-route; if it is specialto sigma=2, it isatoy.

-Lens5:T2J3line-incidence≠line-decoding≠CA;keptseparate,no
  conversion used.

-Lens6:forthiswallthesingleblockingdependencyisthe(currently
  un-runnable) symbolic image-dimension check, not an imported theorem; Paper
  D'sCrites–Stewart/ABFconditionalityisorthogonalhere.

Exact next step

  Settle the image dimension of mu_coef:(τ1,τ2)↦[q1:(p1−q2):p2] ∈ P^2(F) on each
  source-validresonancestratum,intwoequivalentforms:

  1. Symbolic: compute J = ∂(z, w)/∂(τ1,τ2) for an auxiliary coordinate w, or
  theresultantRes_{τ3}(Delta0,Delta1)anditsfactorstructure;imageisa
  curve ⟺ z is functionally dependent on one coordinate ⟺ a fixed ≤O(1)-degree
relationR(z)≡0holds.

2.Finite(whenexecutionisrestored):runthebankedCycle17
  rank_det_split_scanner.py on p=7,11,13,17,19,23, filtered to Delta1≡0 and
  deg_{τ3}gcd=1strataseparately,watchingC2/p^2.Singleprimesremain
  EXPERIMENTAL; only a growing family with C2/p^2 bounded below would be a
counterpacket candidae (sub-reserve).

1.Symbolic:computeJ=∂(z,w)/∂(τ1,τ2)foranauxiliarycoordinatew,or
the resutant Res_{τ3}(Delta0,Delta1) anditsfactor structure; mgisa
curve ⟺ z is functionally dependent on one coordinate ⟺ a fixd≤O(1)-degree
relation R(z)≡0 holds.
2. Finite whenexecutionisrestored):runthebankedCycle17
rank_de_split_scanner.pyonp=7,11,13,17,19,23, filtered toDelta1≡0and
deg_{τ3}gcd=1 strta searately, watching C2/p^2. Singl primes remain
EXPERIMENTAL;only growing family with C2/p^2 bounded below would bea
counterpacketcandidate (sub-reserve).

---

Doyouseeaplausibleroutetoafullsolvefromhere?YES.

IfYES,whatisthenextexactlemmaorconstruction:

ProvetheRESONANCESLOPE-MAPCOLLAPSELEMMA—oneverysource-validstratum

withgcd(Delta0,Delta1)!=1(D=F_p,t=sigma=2,j=3,offR0),therational

slopemap(tau1,tau2)|->z=(p1+h/s)/q1[resp.thequadriccase
  Delta1==0]

has1-dimensionalimage,equivalentlythethreeF-affineformsq1,(p1-q2),p2

satisfyafixedbounded-degreefunctionaldependenceforcing

#image(mu_coef)=O(p).ThisyieldsC2=O(p)onallresonancestrataand,

combinedwiththemonicitylemma'ssafeside,closesthecorrectedlocalF1

T2J3statementinthiswindow(stillsub-reserveeta=2/n).Thecontrapositive

construction—exhibitingsource-validq1,(p1-q2),p2withgenerically-finite

mu_coefoveragrowing-pfamily—istheexactcounterpackettobuildifthe

collapsefails.

Doyouseeaplausibleroutetoafullsolvefromhere?YES.
IfYES, whatis the nxt exac lemma or construction:
Prove the RESONANCESLOPE-MAP COLLAPSE LEMMA — on everysource-validstratum
with gcd(Delta0,Delta1) != 1 (D=F_p, t=sigma=2, j=3, off R0), the rationl
slope map (tau1tau2) |-> z = (p1 + h/s)/q1  [resp. the quadric case
Delta1==0]
has 1-dimensionalimage,equivalentlythethreeF-affineformsq1,(p1-q2),p2
stisfy a fixed bounded-dgree fuctionaldepndence forcing
#image(mu_coef)= O(p). This yields C2 = O(p) on allresonancestrataand,
cobined with themonicity lemma's safe side,closesthe corrcted locl F1
T2J3 statement inthis window (still sub-reserve eta=2/n). Th contrapositive
construcion —exhibting surce-vaid q1,(p1-q2),p2 with genrically-finite
mu_coef overagrowing-p family — is the exact counterpacket to buid if th
collapse fails.
