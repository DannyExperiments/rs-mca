Both code tools are blockedn ths harness(same conraint Cycles 19–20
workedundr),so this is ananalyic audit derived dirctlyfom the banked
Cycle 12/14/20 multiplicaton identities, not a CAS run.Ire-derived the
load-bearing stepsby hand.

---
Primary label

BANKABLE_LEMMA

  Secondary: EXACT_NEW_WALL (a strictly sharper, explicit criterion below
  dw∧dη==0).

  The exact question — "do the two descent equations force dw∧dη==0?" — has
  answerNo,notbythemselves.Iprovedw∧dη≡0isgovernedbytheCycle‑20gate
  D (as an explicit 2×2 resultant) together with an alignment of the leading
W-data, and that te descen equationsdo notcontol hatcombination.This

isexactlythe"smallerexactimplicationinvolvingthedescentequations,D,

dw∧dη,andtheresultantstructure"bullet.

  Ledger (kept separate)

  B=F_p, q_gen=p; F=F_{p^2}=B+αB, q_line=p^2; q_chal unused. D=F_p, n=p. t=σ=2,
  j=3.η_reserve=2/n,sub-reserve.OffR0={κ=u∧b=0}.Restricted
  line-incidence/residue calculation only.

  Setup recap (source-checked, off R0)

  With c_b=-Q_E(b)/κ, A=(ℓQ)∧b, A'=u∧(ℓQ), P=P_E(u,b)/κ, L_c=λ0^{(0)}=cd+d τ1,
  Q_u=Q_E(u),thebankedformsgive

q1=c_bη,q2=L_c+Pη,

p1=L_c-(c+P)η-A/κ,p2=(Q_u/κ)η-A'/κ,

w^±=(±√δ_z-A/κ)/(2c_bη),δ_z∈B[τ1,τ2]onΔ1==0.

  I take the audit's proxy dw∧dη==0 (the F-valued 2-form, η=(c^2-d)+cτ1+τ2) as
  thedefinitionofdim_BIm(w)=1,andworkwiththewedgeoperator
  L(f):=[df∧dη]=∂_1 f - c∂_2 f, which is an F-linear derivation with L(η)=0 (so
L kills any fuction of η).

LemmaA—differentialreduction(exactidentity)

  Because the denominator of w^± is 2c_b η, d(2c_bη)∧dη=0, so the quotient rule
  collapses:

2c_bη·(dw^±∧dη)=±(1/(2√δ_z))(dδ_z∧dη)-(d(A/κ)∧dη).

  Writing J_δ:=L(δ_z), J_A:=L(A/κ) (constant, since A/κ is affine), this is

dw^±∧dη=0⟺J_δ=±2√δ_z·J_A.(A)

  Proof: w=N/M, M=2c_bη, N=√δ_z - A/κ; dw∧dη=(1/M)dN∧dη since dM∧dη=0; and
  d√δ_z=dδ_z/(2√δ_z).∎

  Requiring both branches w^+,w^- to collapse (the condition relevant to C2,
  sincebothquadraticrootsarerealized)forces,byadding/subtracting(A)
  with √δ_z≠0,

dw^+∧dη≡0anddw^-∧dη≡0⟺J_δ=0andJ_A=0.(A')

  Lemma B — collapse reduces to two scalar gates

  From the closed forms, δ_z = C_2 η^2 + 2(c+2P)(A/κ)η - 4c_b(A'/κ)η + (A/κ)^2
  withC_2constantinτ.ApplyingL(Leibniz,L(η)=0):

J_δ=[2(c+2P)J_A-4c_bJ_{A'}]η+2J_A(A/κ),J_{A'}:=L(A'/κ).

  Hence J_A=0 ⟹ J_δ=-4c_b J_{A'}η, and with c_b≠0, η≢0:

{J_δ=0andJ_A=0}⟺{J_A=0andJ_{A'}=0}.(B)

  So both-branch collapse ⟺ J_A=0 ∧ J_{A'}=0: i.e. both A/κ=(ℓQ)∧b/κ and
  A'/κ=u∧(ℓQ)/κareaffinefunctionsofη.

  Lemma C — the gate D is the resultant of the two collapse gates

  From Cycle 12 (D=F_p): Q0=(W_{n-3}-dW_{n-1})-W_{n-2}τ1+W_{n-1}τ2,
  Q1=(W_{n-2}-cW_{n-1})-W_{n-1}τ1,soL(Q0)=-(W_{n-2}+cW_{n-1}),L(Q1)=-W_{n-1}.
  With A/κ=((ℓ∧b)Q0-P_E(b,ℓ)Q1)/κ, A'/κ=((u∧ℓ)Q0+P_E(u,ℓ)Q1)/κ, set
m:=W_{n-2}+cW_{n-1}, w_1:=W_{n-1}:

κJ_A=-(ℓ∧b)m+P_E(b,ℓ)w_1,

κJ_{A'}=-(u∧ℓ)m-P_E(u,ℓ)w_1.

  These are two F-linear forms in (m,w_1). A nonzero (m,w_1) annihilating both
  existsiffthedeterminantvanishes,andthatdeterminantisexactlythe
  Cycle‑20 gate:

det[(ℓ∧b)-P_E(b,ℓ);(u∧ℓ)P_E(u,ℓ)]

=(ℓ∧b)P_E(u,ℓ)+P_E(b,ℓ)(u∧ℓ)=D.

  Therefore, assuming W_{n-1}≠0 (so (m,w_1)≠0):

dw∧dη≡0(bothbranches)⟺J_A=J_{A'}=0⟺D=0AND(W_{n-2}+cW_{n-1}:
  W_{n-1}) on ker(I,II).

  In particular dw∧dη≡0 ⟹ D=0, and D≠0 ⟹ dw∧dη≢0. ∎

  Direct answer to the exact question

  No. The descent equations Im_α(p1+q2)=0, Im_α(det P)=0 (which are conditions
  ontheτ-dependenceofδ_z)donotforcedw∧dη≡0.ByLemmaC,collapseis
  forced exactly by the τ-independent gate D=0 plus alignment of the leading
W-data with ker(I,II). Since D depndsonly n (E,u,b,ℓ)whilethedescent

conditionscanbesatisfiedbytuningthelowercoefficientsofW(whichmove

L_c,A/κ,A'/κ,δ_zbutleaveDfixed),thetwoareindependentconditions.

Hence:

  - The forcing implication asked for is false as stated — collapse is a
  non-genericdegenerationthatmustbeforcedbyD,notbydescent.

-Conversely,dw∧dη≡0isnotnecessaryforC2=O(p):onD≠0Cycle16'sQ≢0⟹
  C2≤4p already gives O(p) even though dw∧dη≢0. So C2=O(p) holds on D≠0 by the
  curve-in-(z_0,z_1)mechanism,notbyη-functional-dependence.

  This relocates any possible Θ(q_line) seed entirely onto the gate locus D=0.

  Secondary EXACT_NEW_WALL (strictly below dw∧dη==0)

W-F1-AA-RES-T2J3-D-KERNEL-ALIGNMENT

OnΔ1==0∧D==0,offR0,withW_{n-1}≠0:

dw∧dη≡0⟺(W_{n-2}+cW_{n-1}:W_{n-1})∝ker[(ℓ∧b),-P_E(b,ℓ);(u∧ℓ),
  P_E(u,ℓ) ].

Counterpacketseed=source-valid(E,Bnum,W)withΔ1==0,D=0,Q≡0,W_{n-1}≠0,

leadingdataOFFthatkernelline,andenoughdistinctD-splitcubics;there

dw∧dη≢0istheprecisenon-collapseseedforC2=Θ(p^2)=Θ(q_line).

  What is banked vs not

  Bank (proven, exact, off R0, restricted D=F_p,t=σ=2,j=3): Lemma A
  (differentialreductiondw^±∧dη=0⟺J_δ=±2√δ_zJ_A);LemmaB(both-branch
  collapse ⟺ J_A=J_{A'}=0); Lemma C (D is the 2×2 resultant of the two collapse
gates; dw∧dη≡0 ⟹ D=0; D≠0 ⟹ dw∧dη≢0,givenW_{n-1}≠0); andtheobservation

thatdw∧dη≡0issufficient-but-not-necessaryforC2=O(p).

  Do not bank: collapse or non-collapse on D=0; nonemptiness of the seed stratum
  (notexhibited—noscans);anyC2boundonΔ1==0∧D=0;anyΘ(q_line)
  counterpacket; anything at/above corrected reserve; any q_gen, protocol,
list/line/curve-decoding, CA,MCA, or SNARK consequence.

Forbidden-upgradecompliance

  No Prize solve/disproof; η=2/n stays sub-reserve; q_gen/q_line separate; no
  protocoldenominatorsaving;nolist/line/CA/MCAupgrade;nointernet;no
  finite scan cited as proof (none run).

---

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
  construction?

Doyouseearoutetoafullsolve?Ifyes,whatisthenextexactlemmaor
cnstruction?

NotafullPrizesolve—thisisthesub-reserveη=2/ntoywindow,soevena
  clean resolution closes only restricted t=2,j=3 local F1. But there is a
  concrete,code-freeroutetoclosingthewindow,nowsharplylocalizedby
  Lemmas A–C. The next exact lemma is the D=0 resonance compatibility test:

NEXTEXACTLEMMA(finitesymbolic;needsaCASbutnoasymptotics):

OnD==0,parametrizeker(I,II)byasingleF-direction(m:w_1)=κ_dir.

ImposethedescentequationsIm_α(p1+q2)=Im_α(detP)=0asidentitiesin
  B[τ1,τ2],

treating(W_{n-1},W_{n-2},W_{n-3},c,d,u,b,ℓ)assourceunknownswith

Eseparated/aperiodic,[Bnum]_E≠0,W_{n-1}≠0.Thendecide:

(a)doesΔ1==0∧D==0force(W_{n-2}+cW_{n-1}:W_{n-1})ONTOκ_dir

(=>dw∧dη≡0,windowclosed,C2=O(p));or

(b)isthereasource-validsolutionOFFκ_dirwithQ≡0and≥cp^2distinct

D-splitcubicsrealized(=>thefirstΘ(q_line)seed)?

Equivalently:computeRes_{τ_3}(Δ0,Δ1)andtestwhether,modulo(I),(II)and
  D=0,

itcarriestheη-rank-onefactor;thisisafiniteGröbner/resultantproblem
  in

B[τ1,τ2]withtheleading-dataalignmentasthesingledecisivecoordinate.

  This is the single decisive construction: it either banks C2=O(p) for the full
  t=2,j=3windoworexposesthefirstsource-validΘ(q_line)seed—andLemmaC
  has reduced "where to look" from the whole Δ1==0 surface to the explicit
one-coordinate alignmen teston D=0.
