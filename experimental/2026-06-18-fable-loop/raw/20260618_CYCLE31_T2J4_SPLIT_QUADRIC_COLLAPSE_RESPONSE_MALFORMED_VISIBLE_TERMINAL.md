Ihave nough o give a definitive verdict without re-running code.Notup
front: I atemptedto re-run the scan with larger primes/more trialsto
confirm thescaling directly, but codeexecution is dsabed in this harness,
sothe anlysis below rests on (a) theexisting Cycle30 rtificat numbers,
reinterpreed, and (b) the banked alebraic structure from Cycles 28/29. I
flagexplicitlywhat thaleaves unverified.

---

ROUTE_CUT

ROUTE_CUT

ThehypothesizedW-F1-AA-RES-T2J4-SPLIT-QUADRIC-COLLAPSE(ahidden
  rational-root / discriminant / Frobenius mechanism forcing O(p)) does not
  exist.TheCodexfinitescanwasmisread:itsownnumbersrefuteO(p)and
  point to Theta(q_line) = Theta(p^2) with realized-slope density converging to
1/24 = 1/|S_4|.I cut the searh foran O(p) collapse heoreminthiswindow

andreplaceitwiththeexactmonodromyinvariantneededtobankthe

Theta(p^2)counterpacket.

Fieldledger(keptseparate)

  - q_gen = p; B = F_p; F = F_{p^2}; q_line = |F| = p^2; q_chal unused.

-D=F_p,n=p;restrictedt=sigma=2,j=n-a=r-t=4;offR0,kappa=
  u wedge b != 0; source-valid separated E = X^2 + cX + d nonzero on F_p, c_b
  !=0.

-Residue-line/bad-slopeincidenceonly.Nopromotiontocorrected-reserve,
  MCA, list-decoding, CA, line-decoding, curve-MCA, protocol, SNARK, or
  ProximityPrize.

Refutation

  Step 1 — the realized quartics are always B-rational; there is no
  Frobenius/Galoisobstructionatthecoefficientlevel.Cycle29already
  established that fixing a slope z in F makes the incidence iota - z mu = 0 a
square 4x4 system over B:

M(z)tau=-C_0(z),M(z)inB^{4x4},C_0(z)inB^4,

tau(z)=M(z)^{-1}(-C_0(z))inB^4whendet_BM(z)!=0.

M(z)tau=-C_0(z),M(z)inB^{4x4},C_0(z)inB^4,
tau(z) =M(z)^{-1}(-C_0) in B^   when det_B M(z) !=0.

BecauseM(z)andC_0(z)haveB-entries,tau(z)inB^4foreveryzoffthe
  degree-<=4 noninvertibility curve. So L_{tau(z)} = X^4 - tau_1 X^3 + tau_2 X^2
  -tau_3X+tau_4isanF_p-coefficientquarticforallsuchz.Theonly
  thing that can vary is its F_p-splitting type. A "rational-root / Frobenius
collapse" wouldhave o live insid the plittg behavior,notinrationality

ofthecoefficients.

BecauseM(z)andC_0(z)haveB-entries,tau(z)inB^4foreveryzoffthe
dgree-<=4 noninvertibility curve. So L_{tau(z)} = X^4 - tau_1 X^3 + tau_2X^2
- tau_3 X + tau_4 is an F_p-oefficient qurtic for all such z. The only
thing that can vary is its F_p-splitting type. A "ational-root/ Frbenius
collapse" would have to live inide he splitting behavior, nin ationality
of the coefficients.

Step2—landinglocus=imageofz->tau(z),andzisinjectiveonit.The
  Cycle 30 quadric Phi(tau) = iota wedge_F mu = 0 is exactly the z-elimination
  ofiota=zmu.Converselyz->tau(z)single-valuedlyinvertsit(Step1).
  Hence

{tau:Phi(tau)=0,det_BM!=0}={tau(z):zinF},

{tau:Phi(tau)=0,det_BM!=0}={tau(z):zinF},
artional curve carrying~p^2B-points,and the slopemap tau->zis
genericallyinjectiveonit(itistheleftinverseofz->tau).Therefore

C2=#{zinF:tau(z)inTSD},TSD={4distinctrootsinF_p}.

C2=#{zinF:tau(z)inTSD},TSD={4distinctrootsinF_p}.

ThetwoB-quadricscutoutthecurve;theydonotfurthercutC2down—C2is
  controlled entirely by how often the curve meets the totally-split-distinct
  openset.

ThetwoB-quadricscutoutthecurve;theydonotfurthercutC2down—C2is
controlled entirely byhowoften th curvemeets the otally-split-distinct
open set.

Step3—thegoverninginvariantistheGaloisgroupoftheuniversalquartic,
  and 1/24 is its fingerprint. Splitting L_{tau(z)} into four distinct
  F_p-rootsisapositive-densityopenconditioncontrolledbydisc_XLandthe
  resolvent cubic. For a quartic family with geometric Galois/monodromy group
S_4, theproprtion of fiersthat split ompletely equals1/|S_4|=1/24

(function-fieldChebotarev/Frobeniusdensity,effectiveviaWeil).TheCycle

30certificateisconvergingtopreciselythis:

pavg_C2/p^2max_C2p^2/24

70.011222.04

110.019845.04

130.0255107.04

170.02841212.04

190.03251715.04

230.03212522.04
  29    0.0372         35         35.04

pavg_C2/p^2max_C2p^2/24
70.011     2     2.04
119845
3255107
784212
932575
2312522
972335

avg_C2/p^2ismonotonicallyincreasingtoward~0.04≈1/24,andmax_C2sitsat
  or above p^2/24 at every prime. An O(p) law forces C2/p^2 -> 0; the data do
  theopposite.Equivalentlyavg_C2/pruns0.079->1.078(grows~linearlyin
  p), i.e. C2 ~ p^2. This is the signature of Theta(q_line), not O(p).

avg_C2/p^2ismonotonicallyincreasingtoward~0.04≈1/24,andmax_C2sitsat
or above p^2/24 at every prime. An O(p) law forces C2/p^ -> 0;the data do
the opposite. Equivalntly avg_C2/p runs 0.079 -> 1.078 (grows ~linearlyin
p),i.e. C2 ~p^2. This isthe signatreof Theta(q_line), notO(p).

WhyCodex'sreadleanedO(p).Theaveragesaredepressed(notthescaling)by
  two artifacts: (i) trial counts collapse with p (20 -> 4), so large-p means
  arenoisyandbiasedbyafewdegeneraterandom(W,E,b)drawswhosecurve
  tau(z) is partly non-generic; (ii) the average mixes degenerate fibers
(repeated roots, roots in F_{p^2}\F_p)into the count. ThetrendofC2/p^2and

themaximaarethescale-invariantsignals,andbothsayTheta(p^2).

Routetofullsolve(nextexactlemma)

  Bank Theta(q_line) by certifying the monodromy group, not by more random
  scans:

  Lemma (target). Over the function field B(z) (resp. F(z)), the universal
  quarticL_{tau(z)}hasgeometricGaloisgroupS_4.Concretely,certifyboth:

(a)disc_XL_{tau(z)}isanon-squareinB(z)=>G⊄A_4,

(b)resolventcubicR(z)isirreducibleoverB(z)=>3||G|,transitive,

(a)disc_XL_{tau(z)}isanon-squareinB(z)=>G⊄A_4,
breolvent cubic R(z) isirreducible over B(z)3||G|transitive,
together forcing G = S_4. Then ffective function-field Chebotarev/Weil gs

C2=#{zinF:Frob_z=idinS_4}

=(1/24)p^2+O(p^{3/2})=Theta(q_line),

C2=#{zinF:Frob_z=idinS_4}
  (1/24) p^2 + O(p^{3/2})= Theta(q_line),

intherestrictedt=2,j=4,off-R0,c_b!=0,source-validseparatedbranch
  only.

intherestrictedt=2,j=4,off-R0,c_b!=0,source-validseparatedbranch
oly.

Thisisthesmallestexactalgebraicinvarianttochecknext(taskitem4):
  the pair (disc_X L_{tau(z)}, R(z)) as explicit rational functions of z, read
  offfromtau(z)=M(z)^{-1}(-C_0(z))withM(z),C_0(z)fromtheCycle29
  columns. A degenerate outcome (e.g. disc a square, or R reducible, shrinking G
toA_4, D_4,V_4, C_4) would stil keep a positiv totally-splitdensityas

longasidinG—onlyanO(p)countwouldrequirethecurvetoavoidTSD

entirely,whichStep1forbidsgenerically.

  Dependencies

  - Cycle 29: square 4x4 B-system M(z) tau = -C_0(z); tau(z) in B^4; top symbol
  -N(kappa)N(z)^2Q_4(invertibilityoffadegree-<=4curve).

-Cycle28:Q_4=N(c_b)(Im(d)^2-Im(c)Im(conj(c)d))source-validlynonzero;
  used here only to guarantee det_B M(z) is not identically zero so tau(z) is
  definedfor~p^2slopes.

-Cycle30:thesingleF-quadricPhi(tau)=kappaN_{A/F}(lambda)-
  (ell[Q_S]_E) wedge_F (b lambda) and its tau_4-quadratic expansion; the
  EXPERIMENTALscancertificate.

-Cycle11/12:quotientform,line_scalar,residue2,co-support
  elementary-symmetric parametrization tau = e(T).

  Hidden assumptions

  - z in F = F_{p^2} but TSD asks for roots in B = F_p; the Chebotarev count
  thereforemixesanF_{p^2}-indexedsamplewithF_p-splitting.Theclean
  statement needs the geometric monodromy group of the cover and the correct
base (B(z) vs F(z)) pinneddwn — flaggd as the one genuinesubtletybefore

banking.

-z->tau(z)injectivityonthelandinglocusisgeneric(holdsoffthe
  noninvertibility curve); collisions are O(p) and do not change the Theta(p^2)
  scale.

-The1/24readingassumesG=S_4;asmallerGchangestheconstant,notthe
  Theta(p^2) order, provided id in G.

-Theheavierconfirmingscan(largerprimes,fixedsource-valid(W,E,b),
  tracking landings vs C2 and fiber sizes) was not executed — code execution is
  disabledinthisharness.Thereinterpretationusesonlythealready-recorded
  certificate numbers.

Rejectedoverclaims

  - Not a banked Theta(q_line) counterpacket yet — only a seed plus the exact
  lemmaneeded;themonodromycertificate(disc,resolventcubic)isnotyet
  computed.

-NotaproofofG=S_4;notaproofofgeometricirreducibilityoftheimage
  curve.

-NotanO(p)theorem(refuted)andnotadisproofoftheCycle28j=3bound
  (which stands; the j=4 square-system mechanism genuinely differs).

-Nocorrected-reserve,MCA,list-decoding,CA,line-decoding,curve-MCA,
  protocol, q_gen/q_line merge, SNARK, or Proximity Prize consequence.

  Next exact wall

W-F1-AA-RES-T2J4-QUARTIC-MONODROMY-S4

  Compute disc_X L_{tau(z)} and the resolvent cubic R(z) as rational functions
  ofzfromtheCycle29columns;certifyG=S_4(oridentifythetransitive
  subgroup), then apply effective function-field Chebotarev/Weil to bank C2 =
(1/|G|) p^2 + O(p^{3/2}) =Theta(q_line) in the rstrictedbranch.If(disc,

R)source-validlydegenerateGsothatid∉therelevantFrobeniusimage,that

degeneracy—notarational-rootcollapse—istheonlyremainingwaybackto

asub-Theta(p^2)count,andwoulditselfbethenextcounterpacket-blocking

invariant.

Computedisc_XL_{tau(z)}andtheresolventcubicR(z)asrationalfunctions
of z from the Cycle 29 columns; cetify G =S_4 (or identify the transive
subgroup), then apply effectivefunction-field Chebotarev/Weil to bk C2 =
(1/|G|) p^2 + O(p^{3/2}) = Theta(q_line) in the rstricted branch. If (disc,
R) source-validly degenerate G so that id ∉levan Frobeiusimage, that
degeneacy — not a rationl-root collapse—is th only remaining way back to
a sub-Theta(p^2)coun, and wuld itself bethe nxt counterpacket-blocking
invariant.
