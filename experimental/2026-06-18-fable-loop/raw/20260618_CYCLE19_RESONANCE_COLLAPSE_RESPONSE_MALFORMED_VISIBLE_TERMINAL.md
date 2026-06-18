I have the full reduction chain and thesource-level algebra. Codeexecution
is denied in this harness(as in Cycles 14–18), so this is an analytic run
worked directlyfromthebankedCycle12/14multiplicationidentitiesin
A=F[X]/E.Ipushedtheslopeformstoclosedformandfoundthe
  image-dimension question is sharper — and more dangerous — than the Cycle 18
  framingassumed.

BANKABLE_LEMMA

Ledger(keptstrictlyseparate)

B=F_p,q_gen=p;F=F_{p^2}=B+alphaB,alpha^2=gnonsquare,q_line=p^2;

q_chalunused

D=F_p,n=p;t=sigma=2,j=3,a=n-3,k=n-5;eta=2/nSUB-RESERVE

WorkoffR0={kappa:=[W]_Ewedge[Bnum]_E=0}.Line-incidence/residuecalc
  only.

E=X^2+cX+dmonic,c,dinF,separated(E^tau!=E),nonzeroonD;xi=[X]_E;
   xi^2=-c xi-d

u:=[W]_E,b:=[Bnum]_E(deg<2sob=b0+b1xi),ell:=[L_D]_E=[X^p-X]_E
  (tau-independent).

  What I verified from source (Cycle 12/14, exact, no experiment)

  From lambda_0 = xi^3 - tau_1 xi^2 + tau_2 xi and Q=[Q_S]_E (Cycle 12),
  reducingmodEandchangingtothe{u,b}basisviathealternatingformx
  wedge y = x^(0)y^(1)-x^(1)y^(0), the four Cycle-14 affine forms are exactly:

lambda_0^(1)=:eta=(c^2-d)+ctau_1+tau_2[therank-oneform]

q1=-(Q_E(b)/kappa)*etaQ_E(x)=x0^2-cx0x1
  + d x1^2

q2=lambda_0^(0)+(P_E(u,b)/kappa)*etaP_E(x,y)=x0y0-c
  x0 y1 + d x1 y1

p1=lambda_0^(0)-(c+P_E(u,b)/kappa)eta-(1/kappa)(ellQwedgeb)
  p2 = (1/kappa)[ Q_E(u) eta - (u wedge ell Q) ]

  The two Q-dependent terms are affine in (tau_1,tau_2):

(ellQ)wedgeb=(ellwedgeb)Q^(0)-P_E(b,ell)Q^(1),uwedge(ellQ)=(u
  wedge ell)Q^(0) + P_E(u,ell)Q^(1), with Q^(0)=W_{n-3}-dW_{n-1} -W_{n-2}tau_1 +
  W_{n-1}tau_2,Q^(1)=(W_{n-2}-cW_{n-1})-W_{n-1}tau_1.

  Lemma 1 (rank-one leading coefficient)

  q1 = -(Q_E(b)/kappa)*eta is a scalar multiple of the single affine form eta.
  Sotheleadingcoefficientoftheslopequadraticisrank-onein
  (tau_1,tau_2), vanishing exactly on the F-line eta=0. Note lambda_0^(0)=cd+d
tau_1 cancels out of all three slope-formsq1, p1-q2, p2(itsurvivesonlyin

thenon-slopetracep1+q2).Proof:(lambda_0b)wedgeb=-eta·Q_E(b)by

direct2x2expansion;dividebykappa.∎

  Lemma 2 (quadric-case slope normal form — the Delta1==0 case demanded)

  In the quadric stratum Delta1==0 (i.e. Delta in B[tau]), the two B-conditions
  arep1+q2inB[tau]anddetP:=p1q2-p2q1inB[tau].Hencethe
  slope-quadratic discriminant descends to the base field:

delta_z:=(p1-q2)^2+4q1p2=(p1+q2)^2-4detPinB[tau_1,tau_2].

  Writing c_b=-Q_E(b)/kappa, A:=(ell Q) wedge b, the slopes are, up to a fixed
  F-translation(whichpreservescardinality),

z=const_F+w,w^±=(±sqrt(delta_z)-A/kappa)/(2c_b*eta),
  delta_z in B[tau].

  Therefore in the quadric case C2 = O(p) iff the image of w^± is 1-dimensional
  overB,i.e.thetwoB-coordinatesofwarealgebraicallydependentas
  functions on B^2.

  The correction (this tempers Cycle 18)

  Cycle 18 banked the collapse as "plausible." The normal form shows it is not
  generic.w=(±sqrt(delta_z)-A/kappa)/(2c_b·eta)isaratioofF-valued
  functions on B^2; eta is rank-one and delta_z in B, but A=(ell Q) wedge b is a
generic rn-two F-afine form. A generic such ratio has2-dimensional

B-image,i.e.C2=Theta(p^2).Socollapsecanonlycomefromtheresonance

constraintsforcingA(andthenumerator±sqrt(delta_z)-A/kappa)intorank-one

alignmentwitheta.Concretely:

COLLAPSE(C2=O(p))<=>ontheDelta1==0stratum,A/kappaandsqrt(delta_z)
  are

functionsofetaalone(modtheB-linestructure),

equivalentlydw^deta==0onthesurface.

  This is the same tau-independent obstruction in disguise: writing the three
  slope-formsinthebasis{eta,Q^(0),Q^(1)},theP^2(F)-imagedegeneratesiff

D:=(ellwedgeb)P_E(u,ell)+P_E(b,ell)(uwedgeell)vanishes,

  and D is not identically zero (e.g. u=ell gives D=(ell wedge b)Q_E(ell) != 0
  generically).SoD(builtonlyfromE,u,b,ell)isareal,computablescalar
  gate; the residual wall is whether the resonance conditions on (p1+q2, det P)
force the B-level dependence (not merely the P^2-level D=0).TheCycle15p=7

datum(C2<=6onforcedR_a)isconsistentwiththegatefiringonthe

resonancestratum,butitissingle-primeEXPERIMENTALanddoesnotdecideit.

Whynottheotherlabels

  - Not PROOF: I did not show the resonance conditions force dim_B Im(w)=1. The
  normalformmakesplainthatcollapseisanon-genericdegenerationthatmust
  be forced; I cannot certify it by hand and code is denied.

-NotCOUNTERPACKET:dually,Ididnotexhibitsource-valid(E,Bnum,W)with
  Delta1==0 and dim_B Im(w)=2 over a growing-p family. Asserting one would
  violatetheno-finite-scan/sub-reserveguards.

-NotROUTE_CUT:everyCycle12–18stepchecksoutagainstthesource
  multiplication identities; the monicity lemma and safe side are correct. The
  onlythingIcorrectedisanover-optimisticexpectationofcollapse,nota
  false step.

  Sharpened exact wall + exact next step

W-F1-AA-RES-T2J3-RESONANCE-SLOPE-MAP-COLLAPSE(sharpened,bothbranches)

  Quadric branch Delta1==0: with q1=c_b·eta (rank one), delta_z in B[tau], and

w^±=(±sqrt(delta_z)-A/kappa)/(2c_beta),A=(ellQ)wedgeb,

provedim_BIm(w)=1oneverysource-valid(p1+q2,detP)inB[tau]stratum

(=>C2=O(p)),ORbuildsource-validdatawithdim_BIm(w)=2overgrowingp.

  Graph branch deg_{tau3} g=1: same question after substituting tau3=-h/s.

  Exact next step — a finite symbolic check that needs no growing prime: on the
  Delta1==0locus,computedw^deta(equivalentlyRes_{tau3}(Delta0,Delta1)
  factor structure, or the gate D together with the two B-descent conditions).
dw^ dea ≡ 0 ⟺collapse ⟺closes corrected local F1 T2J3inthiswindow

(stillsub-reserveeta=2/n).Anonzerodw^detaonasource-validstratumis

theprecisecounterpacketseed;onlythenrunagrowing-pfamily

(p=11,13,17,19,23)filteredtoDelta1==0watchingC2/p^2.

Non-claims(explicit)

  No solve/disproof of the Proximity Prize; no conj:B; no proof of collapse and
  noTheta(q_line)counterpacket;nothingatorabovecorrectedreserve(eta=2/n
  sub-reserve, so even a Theta(q_line) here would not refute corrected MCA); no
q_gen satementand no q_gen/q_lin merge;nprotocol/denominatorsaving;no

conversiontolist/line/curvedecoding,CA,MCA,orSNARK;finitescanscited

onlyasEXPERIMENTAL;malformedterminaltextnotused.

Whattobank:Lemma1(rank-oneq1,lambda_0^(0)cancellation),Lemma2
  (quadric

normalformwithdelta_zinBandthew^±ratio),thegatescalarD,andthe

correctionthatcollapseisnon-generic.DoNOTbankcollapseora
  counterpacket.
