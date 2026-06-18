Ihaveenough to give arigorous verdict. Let me confirmthe one umerical
sanity check that bcks my main lemma agast therecordedsingular_z counts
before writing.

  The recorded singular counts (singular_z: p=7→11, 11→11, 13→13, 17→20, 19→26,
  23→18,29→33)areallfarbelow4p(28,44,52,68,76,92,116),whichis
  exactly what my degree bound predicts. That is the one empirical fact my proof
nees tobe csiten with, and it is. Nocde run is required;the

deliverableisaproofplusareduction.

  ---

  BANKABLE_LEMMA

BANKABLE_LEMMA

Icanbankoneunconditionalrestrictedlemma(thesingular-curveO(p)bound),
  give an exact reduction of the positive-density question, and pin the
  obstructionsharply.Icannotbankpositivedensity,S_4,orTheta(q_line):
  the histogram is not upgradable to a certificate.

  Field ledger

  - q_gen = p. B = F_p. F = F_{p^2} = B(alpha). q_line = |F| = p^2. q_chal
  unused.

-D=F_p,n=p;restrictedregimet=sigma=2,j=n-a=r-t=4;offR0;
  source-valid separated E = X^2 + cX + d nonzero on F_p, c_b != 0 on that
  branch.

-z=z_0+alphaz_1,(z_0,z_1)inA^2_B.Theparameterspaceistheaffine
  B-surface A^2_B, counted at its F_p-points; this is not a one-variable B(z) or
  F(z)Chebotarevcount.

-Scope:residue-line/bad-slopeincidenceonly.Notcorrected-reserve,MCA,
  list-decoding, CA, line-decoding, curve-MCA, protocol, SNARK, or Proximity
  Prize.

  Task 1 verdict: not upgradable to a certificate

  The Cycle 32 checker is a numeric histogram at finitely many small primes. A
  finitehistogramcancertifyneitheramonodromygroupnortheabsenceofa
  constant-field extension, and both are needed for any density statement. So
the checker stays EXPERIMENTAL. Whatth Cycle 29/30 equationsdosupport

rigorouslyis(i)LemmaAbelowand(ii)thereduction.Thecheckerisalso

validatedasanimplementation:offDelta=0itreproducesthedirectsupport

enumeration(match=Truewheneversingular_split_C2=0),sotheresidual

singular_split_C2in{1,2}rowsareboundaryartifacts,notcheckererrors.

  Task 2: PROOF that Delta = 0 contributes only O(p) split slopes

  This is the one fully provable item.

  1. By the Cycle 32 base model, the columns C_i(z) = P_i - m_z(R_i) are
  affine-linearin(z_0,z_1)becausem_z=z_0I_4+z_1A_alphaisB-linear.
  Hence each entry of M(z) has total degree <= 1 in (z_0,z_1), and

Delta(z_0,z_1)=det_BM(z)hastotaldegree<=4.

2.Deltaisnotthezeropolynomial:Cycle29'stop-symbolcomputationgives

TopSym(Delta)=-N(kappa)*N(z)^2*Q_4,

withN(kappa)!=0andQ_4!=0source-valid.SinceN(z)^2isthesquareof
  the (anisotropic) norm form of F/B, the degree-4 part of Delta is a nonzero
  binaryquartic;thusdegDelta=4exactlyandDelta!≡0.

3.Schwartz–ZippeloverF_p:anonzeropolynomialoftotaldegreedintwo
  variables has at most d·p zeros in F_p^2. Therefore

#{(z_0,z_1)inF_p^2:Delta=0}<=4p.

4.Everysplitslopearisingfromthesingularlocusisinparticularapoint
  of {Delta = 0}. Hence the singular curve contributes at most 4p = O(p) split
  slopes—independentofthemonodromygroupandunconditionalgivensource
  validity.

  Consistency: recorded singular_z is between ~p and ~1.4p, and
  singular_split_C2in{0,1,2},bothcomfortablyunder4p.(Theleadingform
  N(z)^2 vanishes over F_p only at the origin, which is why the curve carries
~p, not ~4p,points.)

  This bound is bankable as the restricted lemma:

L-T2J4-A2B-SINGULAR-OP:theDelta=0locuscontributes<=4psplitslopes.

  Task 3: the exact monodromy theorem needed

  It is not any single one of the offered options; it is a conjunction, split
  intoageometricpart(controlswhichgroup)andanarithmeticpart(controls
  whether the density constant is realized).

  For L_tau = X^4 - tau_1 X^3 + tau_2 X^2 - tau_3 X + tau_4 with cubic resolvent

R(y)=y^3-tau_2y^2+(tau_1tau_3-4tau_4)y-(tau_1^2tau_4-4tau_2
  tau_4 + tau_3^2):

  - Geometric G_geom = S_4 over \bar B(z_0,z_1) ⟺ both disc_X L_tau is a
  nonsquarein\barF_p(z_0,z_1)andR(y)isirreducibleover\barF_p(z_0,z_1).
  (Resolvent irreducible ⟹ 3 | |G| ⟹ G in {A_4, S_4}; disc nonsquare ⟹ G ⊄ A_4;
together⟹ S_4.)

-ThedensityconstantisgovernedbythearithmeticgroupG_arithover
  B(z_0,z_1) = F_p(z_0,z_1), with G_geom ⊴ G_arith. The extra hypothesis needed
  isG_arith=G_geom,i.e.noconstant-fieldextension:thefieldofconstants
  of the S_4-splitting field is exactly F_p. Equivalently, the discriminant
double coverad te resolvent cubiccoverare each geometricallyirreducible.

  Only with both parts does function-field Chebotarev / Lang–Weil on the surface
  give

#{split(z_0,z_1)inA^2(F_p)}=p^2/|G|+O(p^{3/2}),

whichforS_4isp^2/24+O(p^{3/2}).

  Task 4: a smaller transitive group suffices (and is preferable for a seed)

  For a Theta(q_line) = Theta(p^2) counterpacket seed one needs only positive
  densityofcompletely-splitfibers,i.e.density1/|G_geom|>0,whichholds
  for any transitive G ⊆ S_4 provided G_arith = G_geom. So S_4 is not required.
The miniml transitve sugrups areV_4 and C_4 (both order4),givingthe

largestsplitdensity1/4;D_4→1/8,A_4→1/12,S_4→1/24.Hencethe

counterpacketonlyneeds:(a)L_taugeometricallyirreducibleover\bar

F_p(z_0,z_1)(transitivity),and(b)noconstant-fieldextension.Thisis

strictlyweakerthantheS_4targetcarriedsinceCycle31,anditisthe

rightthingtochasenext.

  Task 5: the sharpest obstruction

  Not a checker error (the checker matches direct enumeration off Delta=0), and
  notprimarilyaconstant-fieldextension(thatonlyrescalestheconstant,it
  does not by itself kill positivity). The sharpest live obstruction is failure
ofgeeric dominance / dimension collapse of z -> ta(z):

  tau(z) = M(z)^{-1}(-C_0(z)) is a rational map A^2_B --> A^4. If its image is
  genuinely2-dimensional(genericB-Jacobianrank2)withtransitivemonodromy,
  the split count is Theta(p^2). If instead the image collapses to a curve
(rank <=1),the pli coun is governed by a1-dimensionalLang–Weilcount

andisO(p)—exactlythe"hiddencollapse"theCycle30random-Tscanflirted

with.TheCycle32full-zenumerationarguesagainstcollapse:hist_C2/p^2

sitsat0.018–0.039,stable/risingtoward1/24,ratherthandecayingto0.But

"stableratioatsevensmallprimes"isevidence,notaproofofrank2.

  So the obstruction is concretely: the generic Jacobian rank of z -> tau and
  thegeometricGaloisdataofR(y)anddisc_XL_tauoverF_p(z_0,z_1)are
  uncomputed. These are finite symbolic computations valid for all large p —
which iswhat acertificte would require,and which a small-primehistogram

structurallycannotsupply.

Dependencylist

  - Cycle 32 base-field model: A^2_B, m_z = z_0 I_4 + z_1 A_alpha, affine-linear
  columns,degDelta<=4.

-Cycle29topsymbol:TopSym(Delta)=-N(kappa)N(z)^2Q_4,source-valid
  nonzero ⟹ Delta !≡ 0.

-Cycle30:explicitPhi(tau)two-quadricreductionandthesplit-gate
  definition.

-Cycle24/28:locator-normnonvanishingandQ_4sourcevalidity.

-Cycle11utilitiesunderlyingtheCycle32checker(validatedoffDelta=0).

-Standard:Schwartz–ZippeloverF_p;quarticresolvent-cubicGalois
  criterion; function-field Chebotarev / Lang–Weil with O(q^{dim-1/2}) error.

  Hidden assumptions

  - Source validity (kappa != 0, c_b != 0, E separated and nonzero on F_p, off
  R0)holds,soTopSym(Delta)!=0anddegDelta=4.

-plargeenoughthattheCycle29quotientrecursionisunaffectedbythe-X
  tail of X^p - X.

-TheO(p)lemmacountspointsofthecurve;itboundssplitslopesfromthe
  singular locus regardless of whether tau is defined there, so it needs no
  monodromyinput.

-Lang–Weil/Chebotarevwouldadditionallyrequirethebadlocus(singular
  curve + branch/discriminant locus) to be O(p), which Lemma A supplies for the
  Delta=0part.

  Rejected overclaims

  - No proof of G_geom = S_4, of G_arith = G_geom, or of any Chebotarev density
  constant.

-NoproofofC2=Theta(q_line);nosource-validcounterpacket.

-NoproofoftheoppositeO(p)collapseeither—thefull-zdataleans
  against it but does not settle it.

-TheO(p)singularboundisonlyfortheDelta=0locus;itsaysnothingabout
  the off-curve count.

-Noq_gen/q_linemerge;nopromotiontocorrected-reserve,MCA,CA,
  list-decoding, line-decoding, curve-MCA, protocol, SNARK, or prize status.

  Next exact wall

W-F1-AA-RES-T2J4-A2B-DOMINANCE-RESOLVENT

  A symbolic (all-large-p), not numeric, certificate of three items over
  F_p(z_0,z_1):

  1. Generic B-Jacobian rank of z -> tau(z) (rank 2 ⟹ 2-dimensional image,
  rulingouttheO(p)collapse;rank<=1⟹collapseandC2=O(p)).

2.FactorizationoftheresolventcubicR(y)andthesquareclassofdisc_X
  L_tau over both F_p(z_0,z_1) and \bar F_p(z_0,z_1) — giving G_arith, G_geom,
  andthetransitivityneededforaseed.

3.Theconstant-field-extensiontestG_arith=G_geom.

1.GenericB-Jacobianrankofz->tau(z)(rank2⟹2-dimensionalimage,
ruling outthe O(p) collapse;rank<= 1 ⟹collapse and C2 = O(p)).
2. Factrization ofthe reolvent cubicR(y) and the squareclass ofdisc_X
L_tau over both F_p(z_0,z_1) and \bar F_pz_0,z_1) —givingG_rith,G_geom,
and the tansitivity needed for a seed.
3. The constan-feld-xtnsintet G_arith=G_geom.

Routetoafullsolve:yes,conditionally.Item1aloneisdecisive—rank2
  plus transitivity (item 2, weaker than S_4) plus no-constant-extension (item
  3)yieldsaTheta(p^2)counterpacketseedviaLang–Weil,withLemmaAalready
  disposing of the singular boundary. The next lemma to attempt is exactly the
generic-rn-2 / dominancecmputationforz -> au.
